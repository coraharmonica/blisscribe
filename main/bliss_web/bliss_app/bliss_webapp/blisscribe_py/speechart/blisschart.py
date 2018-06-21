"""
BLISSCHART:

    A module for representing semantics in graphs with Blissymbols.
"""
from main.bliss_web.bliss_app.bliss_webapp.blisscribe_py.blisscribe import *
import speecharts
from images import *


class BlissChart(speecharts.LanguageChart):
    """
    A class for graphing semantics in Blissymbols.
    ~
    BlissChart takes text as input and can visualize graphs
    of Blissymbols.
    ~
    - Language is input in words.
    - Blissymbols are internally represented by 4-digit unicode IDs.
    - Graphs are visualized in Blissymbol characters.
    """
    def __init__(self, language):
        speecharts.LanguageChart.__init__(self, language)
        self.translator = BlissTranslator(language)
        self.translator.set_lang_parser(self)
        self.bliss_height = self.FONT_SIZE * 3

    def refresh(self):
        self.refresh_data()
        self.translator.refresh_bliss_dicts()

    def is_start_state(self, state):
        """
        Returns True if this state is a start state.

        :param state: int, number for a state
        :return: bool, whether state is a start state
        """
        return state in self.start_states

    def is_start_label(self, blissymbol):
        """
        Returns True if this Blissymbol is associated with a start state.

        :param blissymbol: Blissymbol, label for a state transition
        :return: bool, whether blissymbol is for a start state
        """
        return blissymbol in self.start_labels

    def pos_abbrevs(self, poses):
        """
        Returns a list of abbreviated parts of speech for all
        parts of speech in poses.

        :param poses: List[str], Penn Treebank parts of speech
        :return: List[str], abbreviated parts of speech
        """
        return [self.translator.abbreviate_pos(pos) for pos in poses]

    def punct_blissymbol(self, punct):
        """
        Returns this punctuation mark's Blissymbol.

        :param punct: str, punctuation mark
        :return: Blissymbol, blissymbol for punct
        """
        blissword = Blissymbol.PUNCT_MAP.get(punct, None)

        if blissword is not None:
            blissymbol = self.translator.make_blissymbol(blissword+".png", pos="WHITE", derivation="")
            return blissymbol
        else:
            return

    def blissword_blissymbol(self, blissword):
        """
        Returns this word's Blissymbol.

        :param blissword: str, word for Blissymbol
        :return: Blissymbol, this word's Blissymbol
        """
        return self.translator.blissword_to_blissymbol(blissword)

    def word_blissymbol(self, word):
        """
        Returns this word's Blissymbol.

        :param word: str, word to translate to Blissymbol
        :return: Blissymbol, this word's Blissymbol
        """
        if self.is_punct(word):
            blissymbol = self.punct_blissymbol(word)
        else:
            poses = None  # self.translator.convert_wikt_pos(self.word_pos(word, self.language))
            pos = poses[0] if poses is not None else self.translator.token_pos(word)
            trans_word = self.translator.make_translation_word(word, pos, language=self.language)
            blissymbol = trans_word.blissymbol

            if blissymbol is None and word[0].isupper():
                return self.word_blissymbol(word.lower())

        return blissymbol

    def words_to_blissymbols(self, text, derivations=False, grammatical=True):
        """
        Returns a list of Blissymbols corresponding to
        each word in this string of text.
        ~
        If derivations is False, adds each Blissymbol to states.
        Otherwise, adds each Blissymbol's derivative Blissymbols to states.
        ~
        If grammatical is False, adds all Blissymbols to states.
        Otherwise, adds all Blissymbols until one is unknown, then breaks.

        :param text: str, text to tokenize and convert to Blissymbols
        :param derivations: bool, whether to add Blissymbols or
            Blissymbol derivations
        :param grammatical: bool, whether words are grammatically ordered
        :return: List[Blissymbol], Blissymbols for words in words
        """
        blissymbols = list()

        for word in text:
            #print "\nFINDING BLISSYMBOL FOR", word
            blissymbol = self.word_blissymbol(word)
            #print("FOUND BLISSYMBOL.\n")

            if blissymbol is not None:
                if derivations:
                    blissymbols.extend(blissymbol.derivation_blissymbols())
                else:
                    #print word, blissymbol
                    blissymbols.append(blissymbol)
            elif grammatical and not self.contains_punct(word):
                break

        return blissymbols

    def text_to_blissymbols(self, text, derivations=False):
        """
        Returns a list of Blissymbols corresponding to
        each word in this string of text.
        ~
        If derivations is False, adds each Blissymbol to states.
        Otherwise, adds each Blissymbol's derivative Blissymbols to states.

        :param text: str, text to tokenize and convert to Blissymbols
        :param derivations: bool, whether to return Blissymbols or
            Blissymbol derivations
        :return: List[Blissymbol], Blissymbols for words in text
        """
        words = self.tokenize_words(text)
        return self.words_to_blissymbols(words, derivations)

    def text_to_bliss_sentences(self, text, derivations=False):
        """
        Returns a list of lists of Blissymbols corresponding to
        all words in each sentence in this string of text.
        ~
        If derivations is False, adds each Blissymbol to states.
        Otherwise, adds each Blissymbol's derivative Blissymbols to states.

        :param text: str, text to tokenize and convert to Blissymbols
        :param derivations: bool, whether to return Blissymbols or
            Blissymbol derivations
        :return: List[List[Blissymbol]], Blissymbols for sentences in text
        """
        text = self.unicodize(text)
        sentences = self.tokenize_words_sents(text)
        bliss_sentences = list()

        for sentence in sentences:
            bliss_sentence = self.words_to_blissymbols(sentence, derivations, grammatical=True)

            if len(bliss_sentence) != 0:
                self.add_start_label(bliss_sentence[0])
                short_sentences = self.shorter_sentences(bliss_sentence)
                bliss_sentences.extend(short_sentences)

        return bliss_sentences

    def shorter_sentences(self, sentence):
        sentences = list()
        last_sentence = [sentence[0]]

        for blissymbol in sentence[1:]:
            last_sentence.append(blissymbol)

            if self.is_start_label(blissymbol):
                sentences.append(last_sentence)
                last_sentence = list()

        if len(last_sentence) != 0:
            sentences.append(last_sentence)

        return sentences

    def add_word_state(self, word):
        """
        Adds this word's Blissymbol as a state to this BlissChart.

        :param word: str, word with Blissymbol to add as state
        :return: None
        """
        blissymbol = self.translator.word_to_blissymbol(word, self.language)
        self.add_bliss_state(blissymbol)

    def add_blissword_state(self, blissword):
        """
        Adds this blissword's Blissymbol as a state to this BlissChart.

        :param blissword: str, word for Blissymbol to add as state
        :return: None
        """
        blissymbol = self.translator.blissword_to_blissymbol(blissword)
        self.add_bliss_state(blissymbol)

    def add_bliss_state(self, blissymbol):
        """
        Adds this Blissymbol as a state to this BlissChart,
        adding its part-of-speech colour(s) to state_colours.

        :param blissymbol: Blissymbol, blissymbol to add as state
        :return: None
        """
        if blissymbol is not None:
            poses = self.pos_abbrevs(blissymbol.pos)
            self.add_bliss_pair(blissymbol, poses)

    def add_bliss_states(self, blissymbols, derivations=True):
        """
        Adds these Blissymbols as states to this BlissChart.
        ~
        If derivations is False, adds each Blissymbol to states.
        Otherwise, adds each Blissymbol's derivative Blissymbols to states.

        :param blissymbols: List[Blissymbol], Blissymbols to add as states
        :param derivations: bool, whether to add Blissymbols or their
            derivations as states
        :return: None
        """
        for blissymbol in blissymbols:
            if derivations:
                self.add_bliss_derivations(blissymbol)
                derivs = blissymbol.derivation_blissymbols()
                terminal_symbol = derivs[-1]
                bliss_states = self.label_states(terminal_symbol)
            else:
                self.add_bliss_state(blissymbol)
                bliss_states = self.label_states(blissymbol)
            self.add_success_states(bliss_states)

    def add_bliss_derivations(self, blissymbol):
        """
        Adds this Blissymbol's derivative Blissymbols as states
        to this BlissChart, adding their part-of-speech colour(s)
        to state_colours.

        :param blissymbol: Blissymbol, blissymbol to add as state
        :return: None
        """
        if blissymbol is not None:
            derivations = blissymbol.derivation_blissymbols()
            self.add_bliss_sentence(derivations)

    def add_bliss_sentence(self, sentence):
        """
        Adds this list of Blissymbols as a sentence to this
        BlissChart's states.

        :param sentence: List[Blissymbol], sentence to add as states
        :return: None
        """
        if len(sentence) != 0:
            self.transition_all(self.current_state, sentence)
            success_states = self.label_states(sentence[-1])
            self.add_success_states(success_states)
            self.current_state = 0

    def add_bliss_sentences(self, text, derivations=False):
        """
        Tokenizes all words from the sentences in this text, then
        translates word tokens to Blissymbols.  Adds Blissymbols
        for each sentence to this BlissChart's states.
        ~
        If derivations is False, adds each Blissymbol to states.
        Otherwise, adds each Blissymbol's derivative Blissymbols to states.

        :param text: str, text with sentences of words to add as states
        :param derivations: bool, whether to add Blissymbols or their
            derivations as states
        :return: None
        """
        bliss_sentences = self.text_to_bliss_sentences(text, derivations)

        for bliss_sentence in sorted(bliss_sentences, key=lambda bs: bs[0].unicode):
            self.add_bliss_sentence(bliss_sentence)

    def add_text_states(self, text, derivations=True):
        """
        Tokenizes each word in this text, translates the tokens to
        Blissymbols, then adds each Blissymbol sentence as states.
        ~
        If derivations is False, adds each Blissymbol to states.
        Otherwise, adds each Blissymbol's derivative Blissymbols to states.

        :param text: str, text with words to add as states
        :param derivations: bool, whether to add Blissymbols or
            their derivations as states
        :return: None
        """
        blissymbols = self.text_to_blissymbols(text, derivations)
        self.add_bliss_states(blissymbols, derivations)

    def add_bliss_pair(self, blissymbol, pos):
        """
        Adds this blissymbol-pos pair as a state to this Chart's dfa.
        ~
        Adds this blissymbol-pos pair to success_states.

        :param blissymbol: Blissymbol, Blissymbol to add to DFA with pos
        :param pos: Set(str), parts of speech for this blissymbol
        :return: None
        """
        poses = {pos} if type(pos) == str else set(pos)
        self.current_state = self.transition(self.current_state, blissymbol)
        self.add_success_state(self.current_state, poses)
        self.current_state = 0

    def transition_label(self, state=None):
        """
        Returns the label(s) for this state.
        ~
        If state is None, return all transition labels.

        :param state: Optional[int], state number
        :return: List[str], strings for this state
        """
        labels = self.transitions_labels(state)

        if len(labels) != 0:
            print labels
            return [", ".join([bliss.bliss_name for bliss in label]) for label in labels.values()]
        else:
            return list()

    def blissword_states(self, blissword):
        """
        Returns a list of states for this (English) blissword.
        ~
        Blissword is name of a Blissymbol or one of its
        English translations.

        :param blissword: str, word for a Blissymbol
        :return: List[int], all states with this blissword
        """
        states = list()

        if "," in blissword:
            full_name = True
        else:
            full_name = False

        for transition in self.transitions:
            blissymbol = transition[1]
            if full_name:
                blissname = blissymbol.clean_bliss_name()
                if blissword == blissname:
                    state = transition[0]
                    states.append(state)
            else:
                blissnames = blissymbol.get_translation("English")
                if blissword in blissnames:
                    state = transition[0]
                    states.append(state)

        return states

    def arrow_length(self):
        """
        Returns the width of the largest Blissymbol in self.transitions,
        multiplied by 2.

        :return: int, largest Blissymbol width
        """
        if len(self.transitions) != 0:
            max_transition = max(self.transitions, key=lambda t: self.bliss_image(t[1]).size[0])
            max_blissymbol = max_transition[1]
            max_width = self.bliss_image(max_blissymbol).size[0]
            return max_width * 2
        else:
            return 0

    def visualize_bliss_state(self, blissword):
        """
        Visualizes the (first) state with this blissword.
        ~
        Blissword is name of a Blissymbol or one of its
        English translations.

        :param blissword: str, word for a Blissymbol
        :return: None
        """
        states = self.blissword_states(blissword)
        start_states = filter(self.is_start_state, states)
        length = self.arrow_length()
        if len(start_states) != 0:
            state = start_states[0]  # find first state with this label
            self.visualize_state(state, length)

    def arrow_fan(self, img, num_arrows, vertical=True):
        length = self.RADIUS * 2

        if num_arrows != 0:
            state0 = make_blank_img(0, 0, opacity=0)
            inc = 90 / num_arrows
            apex = (num_arrows - 1) * inc
            angle = apex / 2
            if vertical:
                angle += 90
            branch = state0

            if apex >= 180:
                inc, apex, angle = 0, 0, 0

            for i in range(num_arrows):
                twig = self.connect_states(state0, state0, "", angle=angle, length=length, vertical=vertical)
                if vertical:
                    branch = beside(branch, twig)
                else:
                    branch = above(branch, twig, align='left')
                angle -= inc

            img = self.connect_states(img, branch, length=0, vertical=vertical)

        return img

    def visualize_state(self, state, length):
        """
        Visualizes this state and its transitions as an Image
        and returns the image.

        :param state: int, state to visualize
        :param length: int, length of arrows between states
        :return: Image, image of this state and its transitions
        """
        destinations = self.state_outgoing_states(state)
        dfa = self.state_circle(state)

        if len(destinations) != 0:
            state0 = make_blank_img(0, 0, opacity=0)
            inc = 5
            apex = (len(destinations) - 1) * inc
            angle = apex / 2
            branch = state0

            if apex >= 180:
                inc, apex, angle = 0, 0, 0

            for dest in sorted(destinations):
                blissymbols = destinations[dest]
                circ = self.visualize_state(dest, length)
                twig = self.connect_states(state0, circ, blissymbols, angle=angle, length=length)
                branch = above(branch, twig, align='left')
                angle -= inc

            dfa = self.connect_states(dfa, branch, length=0)

        return dfa

    def bliss_image(self, blissymbol, mini=False):
        """
        Returns an Image for this Blissymbol,
        with a maximum height of self.bliss_height.

        :param blissymbol: Blissymbol, Blissymbol to retrieve image for
        :return: Image, image for Blissymbol
        """
        max_height = self.bliss_height/2 if mini else self.bliss_height
        return blissymbol.bliss_image(max_height=max_height)

    def empty_bliss_image(self):
        """
        Returns a blank image with the height of the Blissymbols.

        :return: Image, empty image for Blissymbols
        """
        return rectangle(0, int(self.bliss_height/2.0), fill=None)

    def state_arrow(self, length, angle, bliss_transitions, vertical=False):
        """
        Returns an arrow image with this length and angle,
        overlaid with an image of all Blissymbols in bliss_transitions.

        :param length: int, length of arrow
        :param angle: int[0,360), angle of arrow
        :param bliss_transitions: Set(Blissymbol), blissymbols to transition with
        :return: Image, arrow with this length, angle, & transition blissymbols
        """
        width = 2 if vertical else length
        height = length if vertical else 2
        bliss_arro = arrow(width=width, height=height, fill="lightgray",
                     angle=angle, label="", font_size=self.FONT_SIZE, lang=self.chart_lang, font=self.font)

        if len(bliss_transitions) != 0:
            transitions = sorted(bliss_transitions)
            if vertical:
                bliss_img = self.above_all(transitions)
            else:
                bliss_img = self.beside_all(transitions)
            bliss_arro = overlay(bliss_img, bliss_arro)

        return bliss_arro

    def above_all(self, blissymbols, mini=False):
        bliss_imgs = [self.bliss_image(bliss, mini) for bliss in blissymbols]
        return above_all(bliss_imgs)

    def beside_all(self, blissymbols, mini=False):
        bliss_imgs = [self.bliss_image(bliss, mini) for bliss in blissymbols]
        return beside_all(bliss_imgs)

    def transition_all(self, state, blissymbols):
        """
        Returns the result of the transition function from this state
        with each Blissymbol in blissymbols.
        ~
        If this state-blissymbols pair already exists, returns their output.
        Otherwise, creates a new transition pair from input state to a new
        state.

        :param state: int, state to transition from
        :param blissymbols: Iterable(Blissymbol), blissymbols to transition with
        :return: int, new state after all blissymbols transitions
        """
        self.add_start_state(state)
        curr_state = state

        for i in range(len(blissymbols)):
            while True:
                blissymbol = blissymbols[i]
                next_bliss = blissymbols[i+1] if i+1 < len(blissymbols) else None
                is_punct = blissymbol.is_punct()
                is_end = False if next_bliss is None else next_bliss.bliss_name[:7] == "period"

                if not is_punct:
                    curr_state = self.transition(curr_state, blissymbol)
                    poses = self.pos_abbrevs(blissymbol.pos)
                    self.add_state_colours(curr_state, poses)
                    if is_end:
                        self.add_success_state(curr_state, set(poses))

                if i == 0:
                    self.add_start_state(curr_state)
                elif blissymbol in self.start_labels:
                    if curr_state not in self.start_states:
                        self.add_start_state(curr_state)
                        curr_state = 0
                        continue

                break  # break if no continue up until end

        return curr_state


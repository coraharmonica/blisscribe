# coding: utf-8
"""
SPEECHARTS:

    Stores classes for charting words as graphs.
    ~
    Designed for (ideally) any language.
"""
from morpheme_parser import MorphemeParser
from images import *


class Chart(MorphemeParser):
    """
    An abstract class for language charts.
    ~
    Contains constants and declares variables without initializing them.
    """
    RADIUS = 24
    FONT_SIZE = RADIUS / 2

    POS_ABBREVS = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS",
                   "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$",
                   "RB", "RBR", "RBS", "RP", "TO", "UH", "VB", "VBD", "VBG",
                   "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"]
    POS_KEY = {u"Noun": "n",
               u"Verb": "v",
               u"Adjective": "a",
               u"Adverb": "r"}
    POS_RGB = {'v': (225,   0,   0, 125),
               'n': (  0, 225,   0, 125),
               'a': (  0,   0, 200, 125),
               's': (  0,   0, 200, 125),
               'r': (175,   0, 175, 125),
               'o': (  0, 175, 175, 125)}
    RGB = {"nouns": POS_RGB['n'],
           "verbs": POS_RGB['v'],
           "adjs.": POS_RGB['a'],
           "advs.": POS_RGB['r'],
           "other": POS_RGB['o']}

    def __init__(self, language):
        MorphemeParser.__init__(self, language)
        self.language = language
        self.chart_lang = self.language
        # dfa states
        self.start_state = int()
        self.current_state = int()
        self.states = None
        self.start_states = None
        self.start_labels = None
        self.success_states = None
        self.state_colours = None
        self.transitions = None
        # fonts
        self.font = None
        self.mini_font = None
        self.title_font = None

    def init_states(self):
        self.alphabet = set()
        self.start_state = 0
        self.current_state = self.start_state
        self.states = {self.start_state}
        self.start_states = self.states.copy()
        self.start_labels = set()
        self.success_states = dict()
        self.state_colours = dict()     # RGBs for each colour combination
        self.transitions = dict()       # transitions functions for all states

    def init_fonts(self):
        self.font = load_default_font(lang_font(self.chart_lang), size=self.FONT_SIZE)
        self.mini_font = load_default_font(lang_font("English"), size=self.FONT_SIZE/2)
        self.title_font = load_default_font(lang_font("English"), size=self.FONT_SIZE*2)

    def clear(self):
        """
        Resets this Speechart's transitions and all states.

        :return: None
        """
        self.init_states()


class Speechart(Chart):
    """
    An instance of a Chart to base all language charts off of.
    """
    def __init__(self, language):
        Chart.__init__(self, language)
        self.init_states()
        self.init_fonts()
        self.init_tokenizers()

    # STATES
    # ------
    def new_state(self):
        """
        Adds one more state to this Speechart's states.
        ~
        Returns the integer representing the new state.

        :return: int, new state's number
        """
        state = len(self.states)
        self.states.add(state)
        return state

    def add_success_state(self, state, poses=set()):
        """
        Adds this state and its part-of-speech as a success state
        to this Speechart's success_states.

        :param state: int, state to add as success state
        :param poses: Set(str), parts of speech to add as key
        :return: None
        """
        self.success_states.setdefault(state, set())
        self.success_states[state].update(poses)
        for pos in poses:
            self.add_state_colour(state, pos)

    def add_state_colour(self, state, pos):
        """
        Adds this state and its part-of-speech colour to state_colours.
        ~
        N.B. Not all success states need to have a colour,
             but many of them will.

        :param state: int, state to add colour to
        :param pos: str, part-of-speech to add to state_colours
        :return: None
        """
        pos_colour = self.pos_rgb(pos)
        self.state_colours.setdefault(state, (0, 0, 0, 0))
        colour = self.state_colours[state]

        if pos_colour is None or colour is None:
            colour = None
        else:
            avg_colour = lambda i: max(100, min(colour[i] + pos_colour[i], 225))
            colour = (avg_colour(0),
                      avg_colour(1),
                      avg_colour(2),
                      avg_colour(3))

        self.state_colours[state] = colour

    def state_destinations(self, state):
        """
        Returns a dictionary of all destination states for the given state.

        :param state: int, state number to return destinations for
        :return: dict[int, Set], all destinations for this state
        """
        state_transitions = [t for t in self.transitions if t[0] == state]
        destinations = dict()

        for statechar in state_transitions:
            dest = self.transitions[statechar]
            destinations.setdefault(dest, set())
            destinations[dest].add(statechar[1])

        return destinations

    def state_labels(self, state):
        """
        Returns all outgoing state labels for this state.

        :param state: int, state in this Speechart
        :return: dict(int, str), where int is state and str is destinations
        """
        destinations = self.state_destinations(state)
        labels = {dest: ", ".join(destinations[dest]) for dest in destinations}
        return labels

    def add_start_label(self, label):
        """
        Adds the given str representing a transition between starting
        states to this Chart's set of state_labels, and returns None.

        :param label: str, transition to add to start_labels
        :return: None
        """
        self.start_labels.add(label)

    def add_start_labels(self, labels):
        """
        Adds the given set of strings representing transitions
        between starting states to this Chart's set of state_labels,
        and returns None.

        :param labels: Set[str], transitions to add to start_labels
        :return: None
        """
        self.start_labels.update(labels)

    def add_start_state(self, state_num):
        """
        Adds the given integer representing a state
        to this Chart's set of start_states, and
        returns None.

        :param state_num: int, state to add
        :return: None
        """
        self.start_states.add(state_num)

    def add_start_states(self, state_nums):
        """
        Adds the given set of integers representing states
        to this Chart's set of start_states, and
        returns None.

        :param state_nums: Set[int], states to add
        :return: None
        """
        self.start_states.update(state_nums)

    # TRANSITIONS
    # -----------
    def transition(self, state, char):
        """
        Returns the result of the transition function from the given state
        and character.
        ~
        If the given state-char pair already exists, returns their output.
        Otherwise, creates a new transition pair from input state to a new
        state and returns new state.

        :param state: int, state to transition from
        :param char: str, character (in alphabet) to transition with
        :return: int, next state
        """
        try:
            new_state = self.transitions[(state, char)]
        except KeyError:
            new_state = self.new_state()
            self.transitions[(state, char)] = new_state
        return new_state

    def transition_all(self, state, chars):
        """
        Returns the result of the transition function from the given state
        and all characters in chars.
        ~
        If the given state-char pair already exists, returns their output.
        Otherwise, creates a new transition pair from input state to a new
        state.

        :param state: int, state to transition from
        :param chars: Iterable(str), characters in alphabet to transition with
        :return: int, new state after all chars transitions
        """
        curr_state = state
        for char in chars:
            curr_state = self.transition(curr_state, self.unicodize(char))
            if curr_state in self.start_states:
                break
        return curr_state

    def transitions_labels(self, state=None):
        """
        Returns the set of all transition labels in this Chart.
        ~
        If more than 1 label belongs to a transition, this method joins all
        labels with commas.

        :return: List[str], new state after all chars transitions
        """
        labels = {}

        for transition in sorted(self.transitions):
            source, label = transition
            if state is None or source == state:
                dest = self.transitions[transition]
                pair = (source, dest)
                labels.setdefault(pair, set())
                labels[pair].add(label)

        return [", ".join(label) for label in labels.values()]

    # AESTHETICS
    # ----------
    def lookup_state_colour(self, state):
        """
        Returns the colour corresponding to the given state.
        ~
        N.B. If given state is a success state, colour is
        based on its part(s) of speech.  Otherwise, colour is
        left blank.

        :param state: int, state to return colour for
        :return: 3-tuple(int,int,int), RGB colour for state
        """
        state_colour = self.state_colours.get(state, None)

        if state_colour is None:
            poses = self.success_states.get(state, list())

            if len(poses) == 0:
                return None
            else:
                return self.state_colours[state]
        else:
            return state_colour

    def pos_rgb(self, pos):
        """
        Returns a 4-tuple representing an additive RGBA value for
        the given pos.

        :param pos: str, part-of-speech to retrieve additive RGBA value for
        :return: 4-tuple(int,int,int,int), additive RBGA value for given pos
        """
        if pos is None:
            return

        try:
            return self.POS_RGB[pos]
        except KeyError:
            try:
                return self.POS_RGB[self.POS_KEY[pos]]
            except KeyError:
                return self.POS_RGB['o']

    def text_size(self, txt):
        """
        Returns this text's pixel size in this Speechart's
        font and FONT_SIZE.

        :param txt: str, text to return
        :return: tuple(int, int), width & height of input text
        """
        return text_size(txt, self.language, self.FONT_SIZE, self.font)

    def get_text_size(self):
        """
        Returns a text size appropriate for the largest transition label
        in this Speechart.

        :return: int, text size
        """
        transitions = self.transitions_labels()
        return self.text_size(max(transitions,
                                  key=lambda txt: self.text_size(txt)[0]))

    # IMAGES
    # ------
    def empty_image(self):
        """
        Returns an invisible image of RADIUS * RADIUS dimensions.
        ~
        Used for holding the place of a future state circle.

        :return: Image, invisible placeholder image
        """
        return rectangle(self.RADIUS/2, self.RADIUS/2, fill=None)

    def state_circle(self, state_num):
        """
        Returns a circle with state_num overlaid.
        ~
        If given state_num is a success state, output circle
        will be outlined.

        :param state_num: int, number for state circle
        :return: Image, circle with state_num overlaid
        """
        is_success = state_num in self.success_states
        state_colour = self.lookup_state_colour(state_num)
        img = circle(self.RADIUS - 8, fill=state_colour, outline='gray')

        if is_success:
            outline = 'gray'
        else:
            outline = 'white'

        img = overlay(circle(self.RADIUS, fill=None, outline=outline), img)
        img = overlay(text(str(state_num),
                           lang=self.language,
                           size=self.FONT_SIZE/2,
                           alpha=0,
                           font=self.mini_font), img)
        return img

    def connect_states(self, state1, state2, transition="", length=0, angle=0):
        """
        Connects state1 and state2 images with an arrow of given
        length and angle, with transition_all overlaid on the arrow.
        ~
        If length is None, set length to the larger of 50 and
        the length of transition_all's text image.

        :param state1: Image, arrow's outgoing state
        :param state2: Image, arrow's incoming state
        :param transition: str, transition_all function from state1 to state2
        :param length: int, length of arrow
        :param angle: int[0,360), angle of arrow between state1 and state2
        :return: Image, state1 connected to state2 with an arrow
        """
        arro = arrow(width=length, height=2, fill="lightgray",
                     angle=angle, label=transition, font_size=self.FONT_SIZE, lang=self.chart_lang, font=self.font)
        diff = length - arro.size[0]
        padding = make_blank_img(int(diff), 1, alpha=0)
        arro = beside(padding, arro)
        state0 = make_blank_img(1, state2.size[1]/2, alpha=0)

        if angle > 0:
            align1, align2 = 'bottom', 'top'
            arro = above(state0, arro)
        elif angle < 0:
            align1, align2 = 'top', 'bottom'
            arro = above(arro, state0)
        else:
            align1, align2 = 'center', 'center'

        s1 = trim(state1)
        s2 = beside(arro, state2, align=align2)
        dfa = beside(s1, s2, align=align1)
        return dfa

    # VISUALIZATION
    # -------------
    def visualize(self):
        """
        Visualizes all this Chart's transitions as an Image
        and returns the image.

        :return: Image, image of this DFA
        """
        start = sorted(self.states)[0]
        length = max(self.FONT_SIZE*2, self.get_text_size()[0])
        dfa = self.visualize_state(start, length)
        dfa.show()
        return dfa

    def visualize_state(self, state, length):
        """
        Visualizes the given state and its transitions as an Image
        and returns the image.

        :param state: int, state to visualize
        :return: Image, image of this state and its transitions
        """
        destinations = self.state_destinations(state)
        dfa = self.state_circle(state)

        if len(destinations) != 0:
            state0 = make_blank_img(0, 0, alpha=0)
            inc = 5
            apex = (len(destinations) - 1) * inc
            angle = apex / 2
            branch = state0
            labels = {dest: ", ".join(destinations[dest]) for dest in destinations}
            #rel_len = length * max(1, int(len(labels)**(1.0/2)))

            if apex >= 180:
                inc, apex, angle = 0, 0, 0

            for label in sorted(labels):
                msg = labels[label]
                circ = self.visualize_state(label, length)
                twig = self.connect_states(state0, circ, msg, angle=angle, length=length)
                branch = above(branch, twig, align='left')
                angle -= inc

            dfa = self.connect_states(dfa, branch, length=0)

        return dfa

    def chart(self, title=None):
        """
        Displays this DFA's states in a chart.  Returns the chart.

        :return: Image, image of chart produced
        """
        dfa = self.visualize()
        if title is None:
            title = self.language + " Language Chart"
        title = text(title, size=self.FONT_SIZE*2, font=self.title_font)
        space = self.empty_image()
        legend = space

        for colour in sorted(self.RGB):
            label = text(colour, size=self.FONT_SIZE, font=self.font)
            rgb = self.RGB[colour]
            state = circle(self.RADIUS/2, fill=rgb, outline='gray')
            line = beside(state, space, align='center')
            line = beside(line, label, align='center')
            legend = above(legend, line, align='left')
            legend = above(legend, space, align='left')

        diagram = venn_diagram(sorted(self.RGB.values()), diameter=self.FONT_SIZE*3)
        diagram = beside(diagram, rectangle(self.FONT_SIZE, self.FONT_SIZE, fill=(255,255,255,0)))
        legend = beside(diagram, legend, align='center')
        legend = above(legend, space)
        legend = above(title, legend)
        img = above(legend, dfa)
        img_x, img_y = img.size
        bg = make_blank_img(img_x, img_y, alpha=255)
        bg = overlay(img, bg)
        bg.show()
        return bg


class LanguageChart(Speechart):
    """
    A class for charting language data as DFAs.
    """
    def __init__(self, language):
        Speechart.__init__(self, language)

    def add_word(self, word):
        """
        Adds the given word's characters as states to this LanguageChart's dfa.
        ~
        Adds the given word to success_states.

        :param word: str, word to add to DFA
        :return: None
        """
        self.current_state = self.transition_all(self.current_state, word)
        self.add_success_state(self.current_state, self.word_poses(word))
        self.current_state = 0

    def add_words(self, words):
        """
        Adds the given space-delimited str words' characters
        as states to this LanguageChart.
        ~
        Adds the given words to success_states.

        :param words: str, space-delimited words to add to DFA
        :return: None
        """
        word_tokens = self.tokenize_words(words)
        for word in sorted(word_tokens):
            if not self.contains_punct(word):
                self.add_word(word)

    def add_sentence(self, sentence):
        """
        Adds the given space-delimited str sentence's words
        as states to this LanguageChart.
        ~
        Adds the given words to success_states.

        :param sentence: List[str], sentence to add to DFA
        :return: None
        """
        for words in sorted(sentence):
            self.add_word(words)

    def add_sentences(self, sentences):
        """
        Adds the given space-delimited str sentences' words
        as states to this LanguageChart.
        ~
        Adds the given words to success_states.

        :param sentences: str, sentences to add to DFA
        :return: None
        """
        sentences = self.unicodize(sentences)
        sentence_tokens = self.tokenize_words_sents(sentences)
        for sentence in sorted(sentence_tokens):
            self.add_sentence(sentence)

    def add_word_pair(self, word_pair):
        """
        Adds the given word-pos pair's characters as states to this Chart's dfa.
        ~
        Adds the given word-pos pair to success_states.

        :param words: tuple(str, Set(str)), word-pos pair to add to DFA
        :return: None
        """
        word, pos = word_pair
        self.current_state = self.transition_all(self.current_state, self.unicodize(word))
        self.add_success_state(self.current_state, {pos})
        self.current_state = 0

    def add_word_pairs(self, word_pairs):
        """
        Adds the given word-pos pairs' characters as states to this Chart's dfa.
        ~
        Adds the given word-pos pairs to success_states.

        :param words: Set(tuple(str, str)), word-pos pairs to add to DFA
        :return: None
        """
        for word_pair in sorted(word_pairs):
            self.add_word_pair(word_pair)
        self.refresh_json()


class WordChart(LanguageChart):
    """
    A class for charting words.
    """
    def __init__(self, language):
        LanguageChart.__init__(self, language)

    def add_word(self, word):
        """
        Adds the given word's characters as states to this Chart's dfa.
        ~
        Adds the given word to success_states.

        :param word: str, word to add to DFA
        :return: None
        """
        self.current_state = self.transition_all(self.current_state, word)
        self.add_success_state(self.current_state, poses=self.word_poses(word, self.language))
        self.current_state = 0

    def add_words(self, words):
        """
        Adds the given space-delimited str words' characters
        as states to this Chart's dfa.
        ~
        Adds the given words to success_states.

        :param words: str, space-delimited words to add to DFA
        :return: None
        """
        word_tokens = self.tokenize_words(words)
        for word in sorted(word_tokens):
            self.add_word(word)

    def add_sentence(self, sentence):
        """
        Adds the given space-delimited str sentence's words
        as states to this Chart's dfa.
        ~
        Adds the given words to success_states.

        :param sentence: List[str], sentence to add to DFA
        :return: None
        """
        for words in sorted(sentence):
            self.add_word(words)

    def add_sentences(self, sentences):
        """
        Adds the given space-delimited str sentences' words
        as states to this Chart's dfa.
        ~
        Adds the given words to success_states.

        :param sentences: str, sentences to add to DFA
        :return: None
        """
        sentence_tokens = self.tokenize_words_sents(sentences)
        for sentence in sorted(sentence_tokens):
            self.add_sentence(sentence)

    def add_word_pair(self, word_pair):
        """
        Adds the given word-pos pair's characters as states to this Chart's dfa.
        ~
        Adds the given word-pos pair to success_states.

        :param words: tuple(str, Set(str)), word-pos pair to add to DFA
        :return: None
        """
        word, pos = word_pair
        self.current_state = self.transition_all(self.current_state, self.unicodize(word))
        self.add_success_state(self.current_state, {pos})
        self.current_state = 0

    def add_word_pairs(self, word_pairs):
        """
        Adds the given word-pos pairs' characters as states to this Chart's dfa.
        ~
        Adds the given word-pos pairs to success_states.

        :param words: Set(tuple(str, str)), word-pos pairs to add to DFA
        :return: None
        """
        for word_pair in sorted(word_pairs):
            self.add_word_pair(word_pair)
        self.refresh_json()

    def transition_all(self, state, word):
        """
        Returns the result of the transition function from this state
        and all characters in word.
        ~
        If this state-word pair already exists, returns their output.
        Otherwise, creates a new transition pair from input state to a new
        state.

        :param state: int, state to transition from
        :param word: str, word to transition with
        :return: int, new state after word transition
        """
        curr_state = state
        for char in word:
            curr_state = self.transition(curr_state, self.unicodize(char))
            if curr_state in self.start_states:
                break
        poses = self.word_poses(word, self.language)
        for pos in poses:
            self.add_state_colour(curr_state, pos)
        return curr_state


class MorphemeChart(LanguageChart):
    """
    A class for constructing DFAs from morphemes in a language.
    """
    def __init__(self, language):
        LanguageChart.__init__(self, language)

    def add_states(self, language=None, lim=50000):
        """
        Adds a number of states up to lim to this DFA.

        :param lim: int, number of common word states to add
        :return: None
        """
        morphemes = self.common_morphemes(language, lim)
        pairs = []
        for morpheme in morphemes:
            poses = self.word_poses(morpheme, language)
            for pos in poses:
                pair = (morpheme, pos)
                pairs.append(pair)
        self.add_word_pairs(pairs)

    def transition_all(self, state, word):
        """
        Returns the result of the transition function from this state
        and all characters in word.
        ~
        If this state-word pair already exists, returns their output.
        Otherwise, creates a new transition pair from input state to a new
        state.

        :param state: int, state to transition from
        :param word: str, word to transition with
        :return: int, new state after word transition
        """
        curr_state = state
        morphemes = self.all_word_morphemes(word, self.language)

        if len(morphemes) != 0:
            self.add_start_state(morphemes[0])
            for morpheme in morphemes:
                curr_state = self.transition(curr_state, self.unicodize(morpheme))
                if curr_state in self.start_states:
                    break
            poses = self.word_poses(word, self.language)
            self.add_success_state(word, poses)
            return curr_state


class PhonemeChart(LanguageChart):
    """
    A class for constructing DFAs from IPA pronunciations in a language.
    """
    def __init__(self, language):
        LanguageChart.__init__(self, language)
        self.chart_lang = "English"

    def add_states(self, language=None, lim=50000, only_top=False):
        """
        Adds a number of states up to lim to this DFA.
        ~
        If only_top is False, states correspond to most common words
        in this DFA's language, up to lim.  Otherwise, states
        correspond to IPA pronunciations of most common words.

        :param lim: int, number of common word states to add
        :param only_top: bool, whether to output only top IPAs or all IPAs
        :return: None
        """
        pairs = self.common_ipa_pairs(language, lim, only_top)
        self.add_word_pairs(pairs)

    def transition_all(self, state, chars):
        """
        Returns the result of the transition function from the given state
        and all IPA characters in chars.
        ~
        If the given state-char pair already exists, returns their output.
        Otherwise, creates a new transition pair from input state to a new
        state.

        :param state: int, state to transition from
        :param chars: Iterable(str), characters in alphabet to transition with
        :return: int, new state after all chars transitions
        """
        try:
            ipas = [self.clean_ipa(ipa, scrub=True) for ipa in self.word_ipas(chars)]
        except AttributeError:
            return

        if len(ipas) != 0:
            self.add_start_state(ipas[0])
            for ipa in ipas[:2]:
                curr_state = Speechart.transition_all(self, state, ipa)
                self.add_success_state(curr_state, self.word_poses(chars))
                self.current_state = 0


class SentenceChart(LanguageChart):

    def __init__(self, language):
        LanguageChart.__init__(self, language)

    def add_sentence(self, sentence, factorial=False):
        """
        Adds this str sentence's words to this SentenceChart's states.

        :param sentence: List[str], words in a sentence to add
        :param factorial: bool, only 1st word as start state or all words
        :return: None
        """
        self.add_start_label(self.entry_word(sentence[0]))

        for i in range(len(sentence)):
            states = sentence[i:]
            self.current_state = self.transition_all(self.current_state, states)
            self.current_state = 0
            if not factorial:
                break

    def add_sentences(self, sentences, factorial=False):
        """
        Adds this str sentences' words to this SentenceChart's states.

        :param sentences: str, string of sentences to add to SentenceChart
        :param factorial: bool, whether to only add sentence beginner words as
            start states, or all words as start states
        :return: None
        """
        sents_tokens = self.tokenize_words_sents(sentences)
        self.add_start_labels({sent_tokens[0] for sent_tokens in sents_tokens
                               if len(sent_tokens) != 0})

        for i in range(len(sents_tokens)):
            sentence = sents_tokens[i]
            sentence = [self.entry_word(word) for word in sentence]
            self.add_sentence(sentence, factorial=factorial)

    def transition_all(self, state, sentence):
        """
        Returns the result of the transition function from the given state
        with all words in sentence.
        ~
        If the given state-word pair already exists, returns their output.
        Otherwise, creates a new transition pair from input state to a new
        state.

        :param state: int, state to transition from
        :param sentence: Iterable(str), words to transition with
        :return: int, new state after all sentence transitions
        """
        curr_state = state

        for i in range(len(sentence)):
            repeat = True

            while repeat:
                word = sentence[i]
                next_word = sentence[i+1] if i+1 < len(sentence) else ""
                is_punct = self.contains_punct(word)
                is_end = u"." in next_word

                if not is_punct:
                    curr_state = self.transition(curr_state, self.entry_word(word))
                    poses = self.word_poses(word)
                    for pos in poses:
                        self.add_state_colour(curr_state, pos)
                    if is_end:
                        self.add_success_state(curr_state, set(poses))

                if i == 0:
                    self.add_start_state(curr_state)
                elif word in self.start_labels:
                    if curr_state not in self.start_states:
                        self.add_start_state(curr_state)
                        curr_state = 0
                        continue

                repeat = False

        return curr_state

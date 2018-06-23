# coding: utf-8
"""
SPEECHARTS:

    Stores classes for charting words as graphs.
    ~
    Designed for (ideally) any language.
    ~
    2 words/meanings are synonymous if they can be substituted for one another,
    i.e. their sentences have a high ratio of similar (especially uncommon) elements.

    Determine word meaning by taking 2 words appearing in similar contexts, and examine
    their differences.  Identify what is predictable and then focus on trying to predict
    what is NOT yet predictable.

    Define word meaning as by use: where do these words occur, which words precede them,
    which words follow them (PREDICTIVELY)?  Extrapolate from there for semantics.
"""
from main.bliss_web.bliss_app.bliss_webapp.blisscribe_py.ordered_set import OrderedSet
from morpheme_parser import MorphemeParser
from images import *
from random import shuffle
from nltk import pos_tag


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
               u"Adverb": "r",
               u"NOUN": "n",
               u"VERB": "v",
               u"ADJ": "a",
               u"ADV": "r"}
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

    def labels(self):
        transition_labels = [k[1] for k in self.transitions.keys()]
        return sorted(set(transition_labels), key=lambda i: transition_labels.count(i), reverse=True)

    def clear(self):
        """
        Resets this Speechart's transitions and all states.

        :return: None
        """
        self.init_states()

    # DFA CLASS METHODS
    # -----------------
    @classmethod
    def new_state(cls):
        return

    @classmethod
    def add_success_state(cls, state):
        return

    @classmethod
    def add_state_colour(cls, state, obj):
        return

    @classmethod
    def state_outgoing_states(cls, state):
        return

    @classmethod
    def add_start_state(cls, state):
        return

    @classmethod
    def transition(cls, state, transition):
        return


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
        self.add_state_colours(state, poses)

    def add_success_states(self, states):
        """
        Adds these states as success states to this Speechart's
        success_states.

        :param states: List[int], states to add to success_states
        :return: None
        """
        for state in states:
            self.add_success_state(state)

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

    def add_state_colours(self, state, poses):
        for pos in poses:
            self.add_state_colour(state, pos)

    def label_incoming_states(self, label):
        """
        Returns a list of all incoming states for all states with
        this label.

        :param label: str, label for states to return incoming states for
        :return: List[int], all incoming states for states with this label
        """
        return [t[0] for t in self.transitions if t[1] == label]

    def label_outgoing_states(self, label):
        """
        Returns a list of all incoming states for all states with
        this label.

        :param label: str, label for states to return outgoing states for
        :return: List[int], all outgoing states for states with this label
        """
        return [self.transitions[t] for t in self.transitions if t[1] == label]

    def label_incoming_labels(self, label):
        """
        Returns a list of all incoming state labels for all states with
        this label.

        :param label: str, label for states to return incoming state labels for
        :return: List[str], all incoming state labels for states with this label
        """
        in_labels = list()
        for t in self.transitions:
            if t[1] == label:
                in_labels.extend(self.state_incoming_labels(t[0]).values())
        return in_labels

    def label_outgoing_labels(self, label):
        """
        Returns a list of all incoming state labels for all states with
        this label.

        :param label: str, label for states to return outgoing state labels for
        :return: List[str], all outgoing state labels for states with this label
        """
        out_labels = list()
        for t in self.transitions:
            if t[1] == label:
                out_labels.extend(self.state_outgoing_labels(self.transitions[t]).values())
        return out_labels

    def state_incoming_states(self, state):
        """
        Returns a dictionary of all incoming states for this state.

        :param state: int, state number to return incoming states for
        :return: dict[int, Set(str)], all incoming states for this state
        """
        state_transitions = [t for t in self.transitions if self.transitions[t] == state]
        incoming = dict()

        for statechar in state_transitions:
            in_state = statechar[0]
            incoming.setdefault(in_state, set())
            incoming[in_state].add(statechar[1])

        return incoming

    def state_outgoing_states(self, state):
        """
        Returns a dictionary of all outgoing states for this state.

        :param state: int, state number to return outgoing for
        :return: dict[int, Set], all outgoing states for this state
        """
        state_transitions = [t for t in self.transitions if t[0] == state]
        outgoing = dict()

        for statechar in state_transitions:
            out_state = self.transitions[statechar]
            outgoing.setdefault(out_state, set())
            outgoing[out_state].add(statechar[1])

        return outgoing

    def state_incoming_labels(self, state):
        """
        Returns a dict of all incoming state labels for this state.

        :param state: int, state in this Speechart
        :return: dict(int, str), where...
            key (int) - incoming state
            val (str) - label for all destinations
        """
        incomings = self.state_incoming_states(state)
        labels = {i: ", ".join(incomings[i]) for i in incomings}
        return labels

    def state_outgoing_labels(self, state):
        """
        Returns a dict of all outgoing state labels for this state.

        :param state: int, state in this Speechart
        :return: dict(int, str), where...
            key (int) - outgoing state
            val (str) - label for all destinations
        """
        outgoings = self.state_outgoing_states(state)
        labels = {out: ", ".join(outgoings[out]) for out in outgoings}
        return labels

    def label_states(self, label):
        """
        Returns a list of all states with this label.

        :param label: Any, label for a state's destination
        :return: List[int], all states with this label
        """
        return [self.transitions[t] for t in self.transitions if t[1] == label]

    def add_start_label(self, label):
        """
        Adds the given str representing a transition between starting
        states to this Chart's set of state_outgoing_labels, and returns None.

        :param label: str, transition to add to start_labels
        :return: None
        """
        self.start_labels.add(label)

    def add_start_labels(self, labels):
        """
        Adds the given set of strings representing transitions
        between starting states to this Chart's set of state_outgoing_labels,
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

        :param state_num: int, state to add to start states
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

    def transition_label(self, state=None):
        labels = self.transitions_labels(state)

        if len(labels) != 0:
            return [", ".join(label) for label in labels.values()]
        else:
            return list()

    def transitions_labels(self, state=None):
        """
        Returns the set of all transition labels in this Chart.
        ~
        If more than 1 label belongs to a transition, this method joins all
        labels with commas.

        :return: dict(tuple, set), where...
            key (tuple(int, int)) - state-transition pair
            val (Set(str)) - transition labels
        """
        labels = {}

        for transition in sorted(self.transitions):
            source, label = transition
            if state is None or source == state:
                dest = self.transitions[transition]
                pair = (source, dest)
                labels.setdefault(pair, set())
                labels[pair].add(label)

        return labels

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
        Returns this text_image's pixel size in this Speechart's
        font and FONT_SIZE.

        :param txt: str, text_image to return
        :return: tuple(int, int), width & height of input text_image
        """
        return text_size(txt, self.language, self.FONT_SIZE, self.font)

    def get_text_size(self):
        """
        Returns a text_image size appropriate for the largest transition label
        in this Speechart.

        :return: int, text_image size
        """
        transitions = self.transition_label()
        if len(transitions) == 0:
            return 0
        else:
            return self.text_size(max(transitions,
                                      key=lambda txt: self.text_size(txt)[0]))

    # IMAGES
    # ------
    def empty_image(self):
        """
        Returns an invisible image with no dimensions.
        ~
        Used for building images off each other.

        :return: Image, invisible placeholder image
        """
        return rectangle(0, 0, fill=None)

    def placeholder_image(self):
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
        ~
        If state_num is -1, returns a circle for an empty state.

        :param state_num: int, number for state circle
        :return: Image, circle with state_num overlaid
        """
        is_success = state_num in self.success_states
        state_colour = self.lookup_state_colour(state_num)
        img = circle(self.RADIUS - 8, fill=state_colour, outline='gray')
        outline = 'gray' if is_success else 'white'
        img = overlay(circle(self.RADIUS, fill=None, outline=outline), img)

        if state_num == -1:
            return img
        else:
            img = overlay(text_image(str(state_num),
                                     lang=self.language,
                                     size=self.FONT_SIZE/2,
                                     opacity=0,
                                     font=self.mini_font), img)
            return img

    def state_arrow(self, length, angle, transition, vertical=False):
        """
        Returns an arrow image with this length and angle,
        overlaid with this transition label.

        :param length: int, length of arrow
        :param angle: int[0,360), angle of arrow
        :param transition: str, transition label
        :return: Image, arrow with this length, angle, & transition label
        """
        width = 2 if vertical else length
        height = length if vertical else 2
        return arrow(width=width, height=height, fill="lightgray",
                     angle=angle, label=transition, font_size=self.FONT_SIZE, lang=self.chart_lang, font=self.font)

    def connect_states(self, state1, state2, transition="", length=0, angle=0, vertical=False):
        """
        Connects state1 and state2 images with an arrow of given
        length and angle, with transition overlaid on the arrow.
        ~
        If length is None, set length to the larger of 50 and
        the length of transition_all's text_image image.

        :param state1: Image, arrow's outgoing state
        :param state2: Image, arrow's incoming state
        :param transition: str, transition_all function from state1 to state2
        :param length: int, length of arrow linking state1 and state2
        :param angle: int[0,360), angle of arrow between state1 and state2
        :return: Image, state1 connected to state2 with an arrow
        """
        fn1, fn2 = (above, beside) if not vertical else (beside, above)
        arro = self.state_arrow(length, angle, transition, vertical=vertical)
        diff = length - (arro.size[1] if vertical else arro.size[0])  # padding to compensate for arrow angle
        pad_w, pad_h = (1, max(1, int(diff))) if vertical else (max(1, int(diff)), 1)
        padding = make_blank_img(pad_w, pad_h, opacity=0)
        arro = fn2(padding, arro)
        state0 = make_blank_img(1, state2.size[1] / 2, opacity=0)

        if angle > 0:
            align1, align2 = 'bottom', 'top'
            arro = fn1(state0, arro)
        elif angle < 0:
            align1, align2 = 'top', 'bottom'
            arro = fn1(arro, state0)
        else:
            align1, align2 = 'center', 'center'

        s1 = trim(state1)
        s2 = fn2(arro, state2, align=align2)
        dfa = fn2(s1, s2, align=align1)
        return dfa

    # VISUALIZATION
    # -------------
    def arrow_length(self):
        return max(self.FONT_SIZE, self.get_text_size()[0])

    def visualize(self):
        """
        Visualizes all this Chart's transitions as an Image
        and returns the image.

        :return: Image, image of this DFA
        """
        start = sorted(self.states)[0]
        length = self.arrow_length()
        dfa = self.visualize_state(start, length)
        dfa.show()
        return dfa

    def visualize_state(self, state, length):
        """
        Visualizes the given state and its transitions as an Image
        and returns the image.

        :param state: int, state to start visualization from
        :param length: int, length of arrows between states
        :return: Image, image of this state and its transitions
        """
        outs = self.state_outgoing_states(state)
        dfa = self.state_circle(state)

        if len(outs) != 0:
            state0 = make_blank_img(0, 0, opacity=0)
            inc = 5
            apex = (len(outs) - 1) * inc
            angle = apex / 2
            branch = state0
            labels = {dest: ", ".join(outs[dest]) for dest in outs}

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

    def visualize_label(self, label):
        """
        Visualizes the state(s) with this label and its transitions
        as an Image and returns the image.

        :param label: int, label of state to visualize
        :return: Image, image of this state and its transitions
        """
        states = self.label_states(label)
        dfa = self.placeholder_image()
        length = self.arrow_length()

        if len(states) != 0:
            for state in states:
                img = self.visualize_state(state, length)
                dfa = above(dfa, img)

        return dfa

    def chart(self, title=None):
        """
        Displays this DFA's states in a chart.  Returns the chart.

        :return: Image, image of chart produced
        """
        if title is None:
            title = self.language + " Language Chart"

        title = text_image(title, size=self.FONT_SIZE * 2, font=self.title_font)
        space = self.placeholder_image()
        legend = space
        dfa = self.visualize()

        for colour in sorted(self.RGB):
            label = text_image(colour, size=self.FONT_SIZE, font=self.font)
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
        bg = make_blank_img(img_x, img_y, opacity=255)
        bg = overlay(img, bg)
        bg.show()
        return bg


class LanguageChart(Speechart):
    """
    A class for charting language data in a DFA.
    """
    def __init__(self, language):
        Speechart.__init__(self, language)

    def before(self, **kwargs):
        """
        Returns the incoming states/labels for given state or label.
        ~
        If labels is True, returns labels. Else, returns states.

        :param kwargs:
            state (int) - state to find incoming states/labels of
            label (str) - label to find incoming states/labels of
            labels (bool) - whether to return labels or states
        :return: List[int/str], incoming states/labels for given state/label
        """
        label = kwargs.get('label', None)
        state = kwargs.get('state', None)
        labels = kwargs.get('labels', label is not None)

        if label is not None:
            return self.label_before(label, labels)
        if state is not None:
            return self.state_before(state, labels)

    def after(self, **kwargs):
        """
        Returns the outgoing states/labels for given state or label.
        ~
        If labels is True, returns labels. Else, returns states.

        :param kwargs:
            state (int) - state to find outgoing states/labels of
            label (str) - label to find outgoing states/labels of
            labels (bool) - whether to return labels or states
        :return: List[int/str], outgoing states/labels for given state/label
        """
        label = kwargs.get('label', None)
        state = kwargs.get('state', None)
        labels = kwargs.get('labels', label is not None)

        if label is not None:
            return self.label_after(label, labels)
        if state is not None:
            return self.state_after(state, labels)

    def label_before(self, label, labels=True):
        """
        Returns the incoming states/labels for this label.
        ~
        If labels is True, returns labels. Else, returns states.

        :param label: str, label for states in this chart
        :param labels: bool, whether to return labels or states
        :return: List[int/str], incoming states/labels for this label
        """
        if labels:
            incomings = self.label_incoming_labels(label)
        else:
            incomings = self.label_incoming_states(label)
        befores = sorted(set(incomings), key=lambda b: incomings.count(b), reverse=True)
        '''
        #print "\n", label, "\n\nincoming:\n\n\t",

        for i in range(len(befores)):
            in_label = befores[i]
            freq = incomings.count(in_label)
            #print "\n{idx:<5}\t{before:<20}... {label}".format(idx=i, before=in_label, label=label)
        '''
        return befores

    def label_after(self, label, labels=True):
        """
        Returns the outgoing states/labels for this label.
        ~
        If labels is True, returns labels. Else, returns states.

        :param label: str, label for states in this chart
        :param labels: bool, whether to return labels or states
        :return: List[int/str], outgoing states/labels for this label
        """
        if labels:
            outgoings = self.label_outgoing_labels(label)
        else:
            outgoings = self.label_outgoing_states(label)
        afters = sorted(set(outgoings), key=lambda a: outgoings.count(a), reverse=True)
        '''
        #print "\n\noutgoing:\n\n\t",

        for i in range(len(afters)):
            out_label = afters[i]
            freq = outgoings.count(out_label)
            #print "\n{idx:<5}\t{label} ...{after:>20}".format(idx=i, after=out_label, label=label)
        '''
        return afters

    def label_before_after(self, label, labels=True):
        """
        Returns a 2-tuple of incoming and outgoing state labels for
        the state with this label.
        ~
        Resulting lists contain no duplicates and are ordered
        by frequency.
        ~
        Incoming states come BEFORE this label.
        Outgoing states come AFTER this label.
        ~
        If labels is True, returns a tuple with strs for state labels.
        Else, returns a tuple with ints for states.

        :param label: str, label to find in/out state labels for
        :param labels: bool, whether to return states or state labels
        :return: tuple(List[str], List[str]), incoming/outgoing states for label
        """
        befores = self.label_before(label, labels)
        afters = self.label_after(label, labels)
        return (befores, afters)

    def state_before(self, state, labels=False):
        if labels:
            incomings = self.state_incoming_labels(state).values()
        else:
            incomings = self.state_incoming_states(state).keys()
        befores = sorted(set(incomings), key=lambda b: incomings.count(b), reverse=True)
        '''
        #print "\n", label, "\n\nincoming:\n\n\t",

        for i in range(len(befores)):
            in_label = befores[i]
            freq = incomings.count(in_label)
            #print "\n{idx:<5}\t{before:<20}... {label}".format(idx=i, before=in_label, label=label)
        '''
        return befores

    def state_after(self, state, labels=False):
        if labels:
            outgoings = self.state_outgoing_labels(state).values()
        else:
            outgoings = self.state_outgoing_states(state).keys()

        afters = sorted(set(outgoings), key=lambda a: outgoings.count(a), reverse=True)
        '''
        #print "\n\noutgoing:\n\n\t",

        for i in range(len(afters)):
            out_label = afters[i]
            freq = outgoings.count(out_label)
            #print "\n{idx:<5}\t{label} ...{after:>20}".format(idx=i, after=out_label, label=label)
        '''
        return afters

    def incoming_labels(self, item):
        if type(item) == int:
            return self.state_incoming_labels(item)
        else:
            return self.label_incoming_labels(item)

    def outgoing_labels(self, item):
        if type(item) == int:
            return self.state_outgoing_labels(item)
        else:
            return self.label_outgoing_labels(item)

    def incoming_states(self, item):
        if type(item) == int:
            return self.state_incoming_states(item)
        else:
            return self.label_incoming_states(item)

    def outgoing_states(self, item):
        if type(item) == int:
            return self.state_outgoing_states(item)
        else:
            return self.label_outgoing_states(item)

    def state_before_after(self, state, labels=False):
        """
        Returns a 2-tuple of incoming and outgoing states for
        the state with this label.
        ~
        Resulting lists contain no duplicates and are ordered
        by frequency.
        ~
        Incoming states come BEFORE this label.
        Outgoing states come AFTER this label.
        ~
        If labels is True, returns a tuple with strs for state labels.
        Else, returns a tuple with ints for states.

        :param state: int, label to find in/out states for
        :param labels: bool, whether to return states or state labels
        :return: tuple(List[int], List[int]), incoming/outgoing states for label
        """
        befores = self.state_before(state, labels)
        afters = self.state_after(state, labels)
        return (befores, afters)

        if labels:
            incomings = self.state_incoming_labels(state).values()
            outgoings = self.state_outgoing_labels(state).values()
        else:
            incomings = self.state_incoming_states(state).keys()
            outgoings = self.state_outgoing_states(state).keys()

        before_set = set(incomings)
        after_set = set(outgoings)

        befores = sorted(before_set, key=lambda b: incomings.count(b), reverse=True)
        afters = sorted(after_set, key=lambda a: outgoings.count(a), reverse=True)

        print "\n", state, "\n\nincoming:\n\n\t",

        for i in range(len(befores)):
            before_state = befores[i]
            freq = incomings.count(before_state)
            print "\n{idx:<5}\t{freq:<5}\t{before:<20}... {label}".format(idx=i, before=before_state, label=state, freq=freq)

        print "\n\noutgoing:\n\n\t",

        for i in range(len(afters)):
            after_state = afters[i]
            freq = outgoings.count(after_state)
            print "\n{idx:<5}\t{freq:<5}\t{label} ...{after:>20}".format(idx=i, after=after_state, label=state, freq=freq)

        return (befores, afters)

    def label_synonym(self, label):
        """
        Returns state label with the most similar incoming and
        outgoing states as that with this label.

        :param label: str, label to find synonyms for
        :return: str, state label with most similar in/out states as label
        """
        label_ins, label_outs = self.label_before_after(label)
        synonym_label = None
        synonym_score = 0
        in_labels_seen = set()
        out_labels_seen = set()

        def calc_crossover(ins, outs):
            """

            :param ins: List[X]
            :param outs: List[X]
            :return: int, number of shared states minus number of non-shared states
            """
            return (len(ins) - (len(ins) - len(ins.intersection(label_ins))) -
                   len(ins.symmetric_difference(label_ins))) + \
                   (len(outs) - (len(outs) - len(outs.intersection(label_outs))) -
                    len(outs.symmetric_difference(label_outs)))

        for label_in in label_ins:
            if label_in not in in_labels_seen:
                in_labels_seen.add(label_in)
                print "INCOMING LABEL:\t", label_in
                print "\toutgoing labels:"
                # check each incoming label's outgoing labels
                outgoings = set(self.label_outgoing_labels(label_in))

                for outgoing_label in outgoings:
                    if outgoing_label != label and outgoing_label != label_in and outgoing_label not in out_labels_seen:
                        print "\t\t", outgoing_label
                        out_labels_seen.add(outgoing_label)
                        # check each outgoing label's incoming labels and
                        # compare them to THIS label's incoming labels
                        out_ins = set(self.label_incoming_labels(outgoing_label))
                        curr_score = calc_crossover(out_ins, outgoings)
                        # if current outgoing label shares more incomings
                        # with THIS label than current max, set it to max
                        if synonym_label is None or curr_score > synonym_score:
                            synonym_label = outgoing_label
                            synonym_ins = out_ins
                            synonym_outs = outgoings
                            synonym_score = calc_crossover(synonym_ins, synonym_outs)
                            print "\t\tNEW SYNONYM:\t", synonym_label, synonym_score
                        else:
                            print "\t\told synonym:\t", synonym_label, synonym_score

        for label_out in label_outs:
            if label_out not in out_labels_seen:
                out_labels_seen.add(label_out)
                print "OUTGOING LABEL:\t", label_out
                print "\tincoming labels:"
                # check each outgoing label's incoming labels
                incomings = set(self.label_incoming_labels(label_out))

                for incoming_label in incomings:
                    if incoming_label != label and incoming_label != label_out and incoming_label not in in_labels_seen:
                        print "\t\t", incoming_label
                        in_labels_seen.add(incoming_label)
                        # check each incoming label's outgoing labels and
                        # compare them to THIS label's outgoing labels
                        in_outs = set(self.label_outgoing_labels(incoming_label))
                        curr_score = calc_crossover(incomings, in_outs)
                        # if current incoming label shares more with
                        # THIS label than current max, set it to max
                        if synonym_label is None or curr_score > synonym_score:
                            synonym_label = incoming_label
                            synonym_ins = incomings
                            synonym_outs = in_outs
                            synonym_score = calc_crossover(synonym_ins, synonym_outs)
                            print "\t\tNEW SYNONYM:\t", synonym_label, synonym_score
                        else:
                            print "\t\told synonym:\t", synonym_label, synonym_score

        return synonym_label

    def label_overlap(self, label1, label2):
        """
        Returns an integer representing the number of
        incoming and outgoing nodes shared by states with
        label1 and label2.

        :param label1: str, label for a state
        :param label2: str, label for another state
        :return: int, difference between label1 and label2's incoming
            and outgoing nodes
        """
        l1_ins, l1_outs = self.label_before_after(label1)
        l2_ins, l2_outs = self.label_before_after(label2)
        return (len(l2_ins) - (len(l2_ins) - len(set(l2_ins).intersection(l1_ins)))) + \
               (len(l2_outs) - (len(l2_outs) - len(set(l2_outs).intersection(l1_outs))))

    def label_synonyms(self, label, threshold=1.0):
        """
        Returns state labels with the most similar incoming and
        outgoing states as that with this label.

        :param label: str, label to find synonyms for
        :param threshold: float, in range[0,1], rate of match between label and result
        :return: List[str], state labels with most similar in/out states as label
        """
        label_ins, label_outs = self.label_before_after(label)

        synonym_labels = list()
        synonym_score = 0
        syn_in_score = 0
        syn_out_score = 0
        syn_labels = self.labels()
        loops = 0  # max # dead loops == syn_labels / 10

        for syn_label in syn_labels[:(len(syn_labels) / 10)]:
            if syn_label != label:
                syn_ins = self.label_before(syn_label)
                in_score = self.calc_in_crossover(syn_ins)

                if in_score >= syn_in_score:
                    syn_outs = self.label_after(syn_label)
                    out_score = self.calc_out_crossover(syn_outs)
                    syn_score = in_score + out_score
                    ins_outs = len(label_ins) + len(label_outs)

                    if ins_outs != 0:
                        syn_meets_threshold = (float(syn_score) / ins_outs) >= threshold
                        syn_equal = (in_score == syn_in_score and out_score == syn_out_score) or syn_score == synonym_score

                        if syn_meets_threshold or syn_equal:
                            synonym_labels.append(syn_label)
                            print "ADDING SYNONYM:\t", syn_label
                            loops = 0
                        elif out_score > syn_out_score or (syn_score > syn_in_score + syn_out_score):
                            synonym_labels = [syn_label]
                            synonym_score = syn_score
                            syn_in_score = in_score
                            syn_out_score = out_score
                            loops = 0
                            print "NEW SYNONYM:\t", syn_label, "\t\tscore:\t", synonym_score

                print "loop #", loops
                loops += 1
                ins_outs = len(label_ins) + len(label_outs)

                if (ins_outs > 0 and (float(synonym_score) / ins_outs) >= threshold) or \
                        loops > (len(syn_labels) / 10.0):
                    print "FINAL SYNONYMS:\t", synonym_labels, "\t\tscore:\t", synonym_score
                    break

        if synonym_score > 20:
            return synonym_labels
        else:
            return

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
        Adds this space-delimited str words' characters
        as states to this LanguageChart.
        ~
        Adds these words to success_states.

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

    def add_word_pair(self, word, pos):
        """
        Adds this word-pos pair's characters as states to this Chart's dfa.
        ~
        Adds this word-pos pair to success_states.

        :param word: str, word to add to DFA with pos
        :param pos: Set(str), parts of speech for this word
        :return: None
        """
        poses = {pos} if type(pos) == str else set(pos)
        self.current_state = self.transition_all(self.current_state, self.unicodize(word))
        self.add_success_state(self.current_state, poses)
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
            word, pos = word_pair
            self.add_word_pair(word, pos)
        self.refresh_data()


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

    def add_word_pair(self, word, pos):
        """
        Adds the given word-pos pair's characters as states to this Chart's dfa.
        ~
        Adds the given word-pos pair to success_states.

        :param word: str, word to add to DFA with pos
        :param pos: Set(str), part-of-speech for this word
        :return: None
        """
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
            word, pos = word_pair
            self.add_word_pair(word, pos)
        self.refresh_data()

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
        self.add_state_colours(curr_state, poses)
        return curr_state


class LetterChart(LanguageChart):
    """
    A class for charting language letters in a DFA.
    """
    def __init__(self, language):
        LanguageChart.__init__(self, language)

    def add_word_pair(self, word, pos):
        """
        Adds this word-pos pair's characters as states to this Chart's dfa.
        ~
        Adds this word-pos pair to success_states.

        :param word: str, word to add to DFA with pos
        :param pos: Set(str), parts of speech for this word
        :return: None
        """
        poses = {pos} if type(pos) == str else set(pos)
        self.current_state = self.transition_all(self.current_state, self.unicodize(word))
        self.add_success_state(self.current_state, poses)
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
            word, pos = word_pair
            self.add_word_pair(word, pos)
        self.refresh_data()


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
            pair = (morpheme, poses)
            pairs.append(pair)
            #for pos in poses:
            #    pair = (morpheme, pos)
            #    pairs.append(pair)
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

    def speak(self, start="", length=None):
        """
        Prints and returns a random sentence which fits
        this LanguageChart's states and begins with start.
        ~
        If length is None, result may be of any length.
        Else, result's number of words will equal length.

        :param start: str, desired beginning of sentence
        :param length: Optional[int], desired length of sentence
        :return: str, sentence starting w/ starts and fitting states
        """
        words = list()
        curr_states = self.start_states

        if len(start) != 0:
            start_words = self.tokenize_words(start)

            for start_word in start_words:
                states = self.label_states(start_word)

                for state in states:
                    if state in curr_states:
                        words.append(start_word)
                        curr_states = self.label_outgoing_states(start_word)

        while len(words) != length or (length is None and words[-1] not in self.success_states):
            curr_states = list(curr_states)
            shuffle(curr_states)  # ensures varying results
            max_states = list()

            for curr_state in curr_states:
                print "current state:\t", curr_state
                state_words = self.state_outgoing_labels(curr_state).values()
                if len(state_words) > len(max_states):
                    max_states = state_words
                    if len(max_states) > length or (length is None and len(max_states) > 0):
                        break

            if len(max_states) != 0:
                if length is None:
                    for max_state in max_states:
                        if max_state in self.success_states and len(words) > 2:
                            state_word = max_state
                            break
                    else:
                        state_word = max_states[0]
                else:
                    if len(words) == length - 1:  # last word should be ending word
                        for max_state in max_states:
                            if max_state in self.success_states:
                                state_word = max_state
                                break
                        else:
                            return self.speak(start, length)
                    else:
                        state_word = max_states[0]

                print "state words:\t", max_states
                print "state word: \t", state_word
                words.append(state_word)
                print "words now:  \t", words
                outgoings = self.state_outgoing_states(curr_state)
                curr_states = outgoings.keys()
            else:
                break

        if length is not None and len(words) < length:
            return self.speak(start, length)
        else:
            if len(words) != 0:
                words[0] = words[0].title()
            sentence = " ".join(words) + "."
            print sentence
            return sentence

    def add_text(self, text, factorial=False):
        """
        Converts this text into words and adds them in punctuation-separated
        chunks to this SentenceChart.

        :param text: str, text to convert to sentences
        :param factorial: bool, whether to only add sentence-initial words as
            start states, or all words as start states
        :return: None
        """
        sents_tokens = self.tokenize_words_punct(text)
        self.add_sentences(sents_tokens, factorial)

    def add_texts(self, texts, factorial=False):
        """
        Converts these texts into words and adds them all in
        punctuation-separated chunks to this SentenceChart.

        :param texts: List[str], texts to convert to sentences
        :param factorial: bool, whether to only add sentence-initial words as
            start states, or all words as start states
        :return: None
        """
        for text in texts:
            self.add_text(text, factorial=factorial)

    def add_sentence(self, sentence, factorial=False):
        """
        Adds this str sentence's words to this SentenceChart's states.

        :param sentence: List[str], words in a sentence to add
        :param factorial: bool, only 1st word as start state or all words
        :return: None
        """
        self.add_start_label(sentence[0])

        for i in range(len(sentence)):
            states = sentence[i:]
            self.transition_all(self.current_state, states)
            self.add_success_states(self.label_states(sentence[-1]))
            self.current_state = 0
            if not factorial:
                break

    def add_sentences(self, sentences, factorial=False):
        """
        Adds this str sentences' words to this SentenceChart's states.

        :param sentences: str, string of sentences to add to SentenceChart
        :param factorial: bool, whether to only add sentence-initial words as
            start states, or all words as start states
        :return: None
        """
        self.add_start_labels({sent[0] for sent in sentences
                               if len(sent) != 0})

        for i in range(len(sentences)):
            sentence = sentences[i]
            print sentence
            # sentence = [self.entry_word(word) for word in sentence]
            self.add_sentence(sentence, factorial=factorial)

    def transition_all(self, state, sentence):
        """
        Returns the result of the transition function from the given state
        with all words in sentence.
        ~
        If the given state-sentence pair already exists, returns their output.
        Otherwise, creates a new transition pair from input state to a new
        state.

        :param state: int, state to transition from
        :param sentence: Iterable(str), words to transition with
        :return: int, new state after all sentence transitions
        """
        curr_state = state
        poses = pos_tag(sentence, lang=self.language[:3].lower(), tagset="universal")

        for i in range(len(sentence)):
            while True:
                word = sentence[i]
                pos = poses[i][1]
                print "\t", word, ":", pos
                next_word = sentence[i+1] if i+1 < len(sentence) else ""
                is_punct = self.contains_punct(word)
                is_end = u"." in next_word or u"!" in next_word or u"?" in next_word or u"," in next_word

                if not is_punct:
                    curr_state = self.transition(curr_state, word)  # self.entry_word(word)
                    self.add_state_colour(curr_state, pos)
                    # poses = self.word_poses(word)
                    # self.add_state_colours(curr_state, poses)
                    if is_end:
                        self.add_success_state(curr_state, {pos})  # set(poses))

                if i == 0:
                    self.add_start_state(curr_state)
                elif word in self.start_labels:
                    if curr_state not in self.start_states:
                        self.add_start_state(curr_state)
                        curr_state = 0
                        continue

                break  # break if no continue up until end

        return curr_state


class StemChart(SentenceChart):
    """
    Used to visualize inputs and outputs for language states.
    ~
    Instead of charting n-grams forwards, charts words with
    inputs and outputs.
    """

    def __init__(self, language):
        SentenceChart.__init__(self, language)

    def visualize_label(self, label):
        ins = self.label_incoming_states(label)
        outs = self.label_outgoing_states(label)

        print "label:", label
        print "\tins:", ins
        print "\touts:", outs

        dfa = self.state_circle(-1)  # empty circle
        state0 = make_blank_img(0, 0, opacity=0)
        angle_inc = 5
        length = 100

        if len(outs) != 0:
            apex = (len(outs) - 1) * angle_inc
            angle = apex / 2
            branch = state0
            #labels = set()
            #for out in outs:
            #    labels.update(self.state_outgoing_labels(out).values())
            #print "OUT LABELS:", labels

            if apex >= 180:
                angle_inc, apex, angle = 0, 0, 0

            for out in outs:
                label = ", ".join(self.state_outgoing_labels(out).values())
                circ = self.state_circle(out)
                #for label in sorted(labels):
                #circ = self.state_circle(-1)
                twig = self.connect_states(state0, circ, label, angle=angle, length=length)
                branch = above(branch, twig, align='left')
                angle -= angle_inc

            dfa.show()
            dfa = self.connect_states(dfa, branch, length=0)

        if len(ins) != 0:
            apex = (len(ins) - 1) * angle_inc
            angle = apex / 2
            branch = state0
            #labels = set()
            #for i in ins:
            #    labels.update(self.state_outgoing_labels(i).values())
            #print "IN LABELS:", labels

            if apex >= 180:
                angle_inc, apex, angle = 0, 0, 0

            for i in sorted(ins):
                label = ", ".join(self.state_outgoing_labels(i).values())
                circ = self.state_circle(i)
                #for label in sorted(labels):
                #    circ = self.state_circle(-1)
                twig = self.connect_states(circ, state0, label, angle=angle, length=length)
                branch = above(branch, twig, align='left')
                angle -= angle_inc

            dfa = beside(branch, dfa, align='right')
            dfa.show()
            #dfa = self.connect_states(branch, dfa, length=0)

        return dfa

    def visualize_state(self, state, length):
        ins = self.state_incoming_states(state)
        outs = self.state_outgoing_states(state)
        print "state", state
        print "ins:", ins
        print "outs:", outs

        dfa = self.state_circle(state)

        if len(outs) != 0:
            state0 = make_blank_img(0, 0, opacity=0)
            inc = 5
            apex = (len(outs) - 1) * inc
            angle = apex / 2
            branch = state0
            labels = {out: ", ".join(outs[out]) for out in outs}

            if apex >= 180:
                inc, apex, angle = 0, 0, 0

            for out in sorted(outs):
                labels = outs[out]

                for label in labels:
                    msg = labels[label]
                    circ = self.state_circle(label)  # self.visualize_state(label, length)
                    twig = self.connect_states(state0, circ, msg, angle=angle, length=length)
                    branch = above(branch, twig, align='left')
                    angle -= inc

            dfa = self.connect_states(dfa, branch, length=0)

        if len(ins) != 0:
            state0 = make_blank_img(0, 0, opacity=0)
            inc = 5
            apex = (len(outs) - 1) * inc
            angle = apex / 2
            branch = state0
            labels = {i: ", ".join(ins[i]) for i in ins}

            if apex >= 180:
                inc, apex, angle = 0, 0, 0

            for label in sorted(labels):
                msg = labels[label]
                circ = self.state_circle(label)  # self.visualize_state(label, length)
                twig = self.connect_states(circ, state0, msg, angle=angle, length=length)
                branch = above(branch, twig, align='left')
                angle -= inc

            dfa = self.connect_states(branch, dfa, length=0)

        return dfa



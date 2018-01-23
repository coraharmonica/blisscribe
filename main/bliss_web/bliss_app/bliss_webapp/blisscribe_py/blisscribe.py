# -*- coding: utf-8 -*-
"""
BLISSCRIBE:

    A Python module for translating text to Blissymbols.

    All relevant parts-of-speech tags (used throughout)
    constitute the Penn Treebank parts of speech, whose
    meanings are enumerated here:
    https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    These can also be found in the top-level docstring of parse_lexica.
"""
import collections
import string
from nltk.tokenize import WordPunctTokenizer
from nltk.tag import pos_tag
from nltk.corpus import wordnet
from pattern import text
from pattern.text import en, es, fr, de, it, nl
from fpdf import FPDF
import blissnet
from fonts import *
from bliss_images import *

try:
    from parse_lexica import LexiconParser, Blissymbol, \
        NEW_BLISSYMBOLS, BLISS_SUPPORTED_LANGUAGES
except ImportError:
    raise ImportError("parse_lexica module could not be imported.\n\
    Please find the local module parse_lexica.py \n\
    and relocate it to the same directory as blisscribe.py.")
else:
    from parse_lexica import LexiconParser, Blissymbol, \
        NEW_BLISSYMBOLS
    from parse_lexica import BLISS_SUPPORTED_LANGUAGES as BLISS_LANGS

try:
    from translation_word import TranslationWord
except ImportError:
    raise ImportError("translation_word module could not be imported.\n\
    Please find the local module translation_word.py \n\
    and relocate it to the same directory as blisscribe.py.")
else:
    from translation_word import TranslationWord


class BlissTranslator:
    """
    A class for translating text in select languages to Blissymbols.
    ~
    Currently supported languages:
        - English (default)
        - Spanish
        - German
        - French
        - Italian
        - Dutch
        - Polish
    ~
    Begin by initializing a BlissTranslator with a supported language.
    Pass a string in your chosen language to translate() for an output
    PDF of the given text with Blissymbols.
    ~
    Use choose_translatables() to set whether to translate nouns,
    verbs, adjectives, and/or other parts of speech.
    ~
    By default, a BlissTranslator will translate all parts of
    speech in CHOSEN_POS, i.e., nouns, verbs, and adjectives.
    To translate all other parts of speech, set self.other to True.
    ~
    Contains methods for:
        1) selecting which parts of speech to translate
           --> choose_translatables()
           --> choose_nouns()
           --> choose_verbs()
           --> choose_adjs()
           --> choose_other_pos()
        2) selecting whether to translate text to Blissymbols
           immediately or gradually
           --> set_fast_translate()
        3) selecting font & font size for output PDF translations
           --> set_font()
        4) selecting whether to subtitle all Blissymbols or only
           new Blissymbols
           --> set_sub_all()
    """
    PATH = os.path.dirname(os.path.realpath(__file__))

    DEFAULT_FONT_SIZE = 30
    IMAGES_SAVED = 0
    DIMS = (816, 1056)

    # LANGUAGE
    # --------
    START_PUNCT = {"(", '"', "-",
                   "\xe2\x80\x9c", "\xe2\x80\x98", "\xe2\x80\x9e"}  # spaces BEFORE
    END_PUNCT = {".", ",", ";", ":", "?", "!", ")", '"', "-",
                 "\xe2\x80\x9d", "\xe2\x80\x99", u"\u201d"}  # spaces AFTER
    PUNCTUATION = START_PUNCT.union(END_PUNCT)
    MID_PUNCT = {u"-", u"\u2013", u"\u2014"}
    CONTRACTIONS = {u"'"}
    PUNCTUATION.update(set(string.punctuation))
    PUNCTUATION = PUNCTUATION.union(MID_PUNCT.union(CONTRACTIONS))
    WHITESPACE = {u"\n", u'', u' ', u'_'}

    # --> Parts of Speech
    # Penn Treebank parts-of-speech set
    PARTS_OF_SPEECH = {"CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS",
                       "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$",
                       "RB", "RBR", "RBS", "RP", "TO", "UH", "VB", "VBD", "VBG",
                       "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"}
    # Penn Treebank parts-of-speech key
    POS_KEY = {"CC": "Coordinating conjunction",
               "CD": "Cardinal number",
               "DT": "Determiner",
               "EX": "Existential there",
               "FW": "Foreign word",
               "IN": "Preposition or subordinating conjunction",
               "JJ": "Adjective",
               "JJR": "Adjective, comparative",
               "JJS": "Adjective, superlative",
               "LS": "List item marker",
               "MD": "Modal",
               "NN": "Noun, singular or mass",
               "NNS": "Noun, plural",
               "NNP": "Proper noun, singular",
               "NNPS": "Proper noun, plural",
               "PDT": "Predeterminer",
               "POS": "Possessive ending",
               "PRP": "Personal pronoun",
               "PRP$": "Possessive pronoun",
               "RB": "Adverb",
               "RBR": "Adverb, comparative",
               "RBS": "Adverb, superlative",
               "RP": "Particle",
               "SYM": "Symbol",
               "TO": "to",
               "UH": "Interjection",
               "VB": "Verb, base form",
               "VBD": "Verb, past tense",
               "VBG": "Verb, gerund or present participle",
               "VBN": "Verb, past participle",
               "VBP": "Verb, non-3rd person singular present",
               "VBZ": "Verb, 3rd person singular present",
               "WDT": "Wh-determiner",
               "WP": "Wh-pronoun",
               "WP$": "Possessive wh-pronoun",
               "WRB": "Wh-adverb"}
    POS_ABBREVS_SORTED = ["n", "v", "a", "s", "r"]  # sorted by likelihood of being Blissymbols
    POS_ABBREVS = {"JJ": "a", "JJS": "s", "NN": "n", "VB": "v", "RB": "r"}
    POS_UNABBREVS = {"a": "JJ", "s": "JJS", "n": "NN", "v": "VB", "r": "RB"}
    POS_NAMES = {"a": "ADJ", "s": "ADJ", "n": "NOUN", "v": "VERB", "r": "ADV"}
    POS_FEATURE_DICT = {"n": 1, "v": 2, "a": 3, "s": 3, "r": 4}
    POS_CODE_DICT = {1: "n", 2: "v", 3: "a", 4: "r"}

    DEFAULT_POS = {"NN", "NNS", "VB", "VBD", "VBG", "VBN", "JJ", "JJR", "JJS"}
    CHOSEN_POS = DEFAULT_POS
    DEFAULT_LANG = "English"
    LANG_CODES = {"Arabic": "arb",
                  "Bulgarian": 'bul',
                  "Catalan": 'cat',
                  "Danish": 'dan',
                  "Dutch": 'nld',
                  "German": 'deu',
                  "Greek": 'ell',
                  "English": 'eng',
                  "Basque": 'eus',
                  "Persian": 'fas',
                  "Finnish": 'fin',
                  "French": 'fra',
                  "Galician": 'glg',
                  "Hebrew": 'heb',
                  "Croatian": 'hrv',
                  "Indonesian": 'ind',
                  "Italian": 'ita',
                  "Japanese": 'jpn',
                  "Norwegian Nyorsk": 'nno',
                  "Norwegian Bokmal": 'nob',
                  "Polish": 'pol',
                  "Portuguese": 'por',
                  "Chinese": "qcn",
                  "Slovenian": 'slv',
                  "Spanish": 'spa',
                  "Swedish": 'swe',
                  "Thai": 'tha',
                  "Malay": 'zsm'}
    WORDNET_LANGS = wordnet.langs()
    WORDNET_LANG_CODES = set(LANG_CODES.values())
    TOKENIZER = WordPunctTokenizer()
    SUPPORTED_LANGS = BLISS_LANGS.intersection(WORDNET_LANGS)
    PATTERN_LANGS = text.LANGUAGES
    SUPPORTED_LANGS.update(PATTERN_LANGS)


    def __init__(self, language=DEFAULT_LANG, font_path=SANS_FONT, font_size=DEFAULT_FONT_SIZE):
        self.lex_parser = LexiconParser(translator=self)

        # Fonts
        self.font_size = font_size
        self.font_path = font_path
        self._font = (self.font_path, self.font_size)
        self.font_fam = FONT_PATHS[self.font_path]

        # Images
        self.sub_all = False
        self.page_nums = True

        # Language
        self.bliss_dict = dict()
        self.eng_bliss_dict = dict()
        self.bliss_to_unicode = self.lex_parser.init_bliss_encoding()
        self.unicode_to_bliss = self.lex_parser.init_bliss_decoding()
        self.lexica = dict()
        self.polish_lexicon = dict()
        self.french_lexicon = dict()
        self.language = str()
        self.lang_code = str()
        self.set_language(language)
        self.all_lemma_names = set(wordnet.all_lemma_names(lang=self.lang_code))
        self.fast_translate = False
        self.safe_translate = False
        self.translate_all = False
        self.machine_translate = False
        self.words_seen = dict()
        self.words_changed = dict()
        self.init_seen_changed()
        self.defns_chosen = {}  # holds user choices for correct word definitions

        # --> parts of speech
        self.nouns = True
        self.verbs = True
        self.adjs = True
        self.other = False

        self.classifier = None

    # GETTERS/SETTERS
    # ===============
    #@property
    def get_lex_parser(self):
        return self.lex_parser

    @property
    def get_wordnet_langs(self):
        return wordnet.langs()

    @property
    def font(self):
        """
        Returns this BlissTranslator's font.

        :return: None
        """
        return self._font

    @font.setter
    def font(self, value):
        """
        Sets this BlissTranslator's default font to an ImageFont
        with given font_path and font_size.
        ~
        If font_path is invalid, uses BlissTranslator's ROMAN_FONT.

        #:param font_path: str, path to font file
        #:param font_size: int, desired font size
        :return: None
        """
        self._font = self.find_font(value[0], value[1])

    def find_font(self, font_path, font_size):
        """
        Returns an ImageFont with given font_path and font_size.
        ~
        If font_path is invalid, returns an ImageFont using this
        BlissTranslator's Arial font and font_size.

        :param font_path: str, path to font file
        :param font_size: int, desired font size
        :return: ImageFont, font with given path and font size
        """
        try:
            ImageFont.truetype(font_path, font_size)
        except IOError:
            font_path = self.FONT_FAMS["Arial"]

        return ImageFont.truetype(font_path, font_size)

    def get_language(self):
        """
        Returns this BlissTranslator's native language.

        :return: str, BlissTranslator's language
        """
        return self.language

    def set_language(self, language):
        """
        Sets this BlissTranslator's native language
        to the input language.
        ~
        If given language is invalid, does not change this
        BlissTranslator's default language.

        :param language: str, language for this BlissTranslator
        :return: None
        """
        if not language.istitle():
            language = language.title()

        if language in BLISS_LANGS:
            if self.language == language:
                return
            self.language = language
        else:
            self.language = "English"

        self.lang_code = self.find_lang_code(self.language)

        if self.lang_code not in self.WORDNET_LANGS:
            self.load_multilingual_lemmas(self.language)

        self.init_lexicon(self.language)
        self.init_bliss_dict()

    def load_multilingual_lemmas(self, language):
        """
        Assumes this BlissTranslator's language isn't part of
        default WordNet, and tries to load a custom tab file
        in the given language to WordNet instead.
        ~
        If no such file can be loaded, raises an Exception.
        ~
        Used to add non-default OMWs to WordNet.

        :param language: str, language to load lemmas for
        :return: None
        """
        assert language not in self.WORDNET_LANGS

        lang_code = self.LANG_CODES[language]
        tab_file = self.lex_parser.get_tab_file(lang_code)

        if tab_file is not None:
            wordnet.custom_lemmas(tab_file, lang_code)
            self.WORDNET_LANGS = wordnet.langs()
        else:
            raise Exception("Blisscribe doesn't support this language yet... oops!")

    def dict_to_blissymbol(self, d):
        """
        Returns the given dict, d, as a Blissymbol and
        adds the Blissymbol to bliss_dict.

        :param d: dict, dictionary to turn into Blissymbol
        :return: Blissymbol, Blissymbol representation of given entry
        """
        blissymbol = self.lex_parser.dict_to_blissymbol(d)
        return blissymbol

    def init_bliss_dict(self):
        """
        Initializes this BlissTranslator's bliss_dict in
        its native language.

        :return: None
        """
        self.bliss_dict = self.lex_parser.init_bliss_lexicon(self.language)

        if self.language != "English":
            self.eng_bliss_dict = self.lex_parser.init_bliss_lexicon("English")
        else:
            self.eng_bliss_dict = self.bliss_dict

    def init_lexicon(self, language):
        """
        Initializes a lexicon in this language
        and adds it to self.lexica.
        ~
        Returns None.
        ~
        N.B. For now, Blisscribe only supports French and Polish
        external lexica.

        :param language: str, language to load lemmas for
        :return: None
        """
        if language == "Polish" or language == "French":
            lexicon = self.lex_parser.parse_lexicon(language)
            self.lexica[language] = lexicon

    def get_bliss_dict(self):
        """
        Returns this BlissTranslator's native language Bliss dictionary.

        :return: dict, where...
            key (str) - word in BlissTranslator's native language
            val (List[Blissymbol]) - corresponding Blissymbols
        """
        return self.bliss_dict

    def get_eng_bliss_dict(self):
        """
        Returns this BlissTranslator's English Bliss dictionary.

        :return: dict, where...
            key (str) - word in English
            val (List[Blissymbol]) - corresponding Blissymbols
        """
        return self.eng_bliss_dict

    def get_blissnet(self):
        """
        Returns the Blissymbols Wordnet, Blissnet.

        :return: dict, where...
            key (str) - Blissymbols unicode symbol
            val (List[Synset]) - corresponding Synsets
        """
        return blissnet.BLISSNET

    def init_seen_changed(self):
        """
        Initializes this BlissTranslator's words_seen
        as a default dict.

        :return: None
        """
        self.words_seen = collections.defaultdict(bool)
        self.words_changed = collections.defaultdict(bool)

    def get_bliss_to_unicode(self):
        """
        Returns the global Blissymbols-to-unicode
        encoding dictionary.

        :return: dict, where...
            key (str) - Blissymbol name
            val (List[str]) - unicode Blissymbol codes (in hexadecimal)
        """
        return self.bliss_to_unicode

    def get_unicode_to_bliss(self):
        """
        Returns the global unicode-to-Blissymbols
        encoding dictionary.

        :return: dict, where...
            key (str) - unicode Blissymbol code (in hexadecimal)
            val (List[str]) - list of Blissymbol names
        """
        return self.unicode_to_bliss

    def lookup_bliss_to_unicode(self, bliss):
        """
        Returns the global Blissymbols-to-unicode
        encoding dictionary.

        :param bliss: str, name of blissymbol to lookup
        :return: List[str], unicode names for given bliss
        """
        try:
            return self.bliss_to_unicode[bliss]
        except KeyError:
            return []

    def lookup_unicode_to_bliss(self, uni):
        """
        Returns the global unicode-to-Blissymbols
        encoding dictionary.

        :param uni: str, unicode name to lookup
        :return: List[str], blissymbol names for given unicode
        """
        try:
            defns = self.unicode_to_bliss[uni]
        except KeyError:
            return []
        else:
            return defns

    def add_bliss_to_unicode(self, bliss, uni):
        """
        Adds the given blissymbol-unicode pair to this
        BlissTranslator's Blissymbols-to-unicode
        encoding dictionary.

        :param bliss: str, name of blissymbol to add
        :param uni: str, unicode name for given bliss
        :return: None
        """
        if bliss not in self.bliss_to_unicode:
            self.bliss_to_unicode[bliss] = []
        if uni not in self.bliss_to_unicode[bliss]:
            self.bliss_to_unicode[bliss].append(uni)

    def add_unicode_to_bliss(self, uni, bliss):
        """
        Adds the given unicode-blissymbol pair to this
        BlissTranslator's unicode-to-Blissymbols
        encoding dictionary.

        :param uni: str, unicode name to add
        :param bliss: str, blissymbol name for given unicode
        :return: None
        """
        if uni not in self.unicode_to_bliss:
            self.unicode_to_bliss[uni] = []
        if bliss not in self.unicode_to_bliss[uni]:
            self.unicode_to_bliss[uni].append(bliss)

    def refresh_bliss_and_unicode(self):
        """
        Overwrites the source Blissymbols encoding and decoding
        dictionaries with this LexiconParser's BlissTranslator's
        bliss_to_unicode and unicode_to_bliss dicts.

        :return: None
        """
        self.lex_parser.refresh_bliss_encoding()
        self.lex_parser.refresh_bliss_decoding()

    def set_sub_all(self, sub_all):
        """
        Sets self.sub_all equal to input sub_all value.
        ~
        Setting sub_all to True will produce subtitles under
        all words translated to Blissymbols.
        Setting sub_all to False will produce subtitles only
        under new words translated to Blissymbols.
        ~
        Sets subtitle settings for this BlissTranslator's
        translate() method.

        :param sub_all: bool, whether to subtitle all words
        :return: None
        """
        self.sub_all = sub_all

    def set_page_nums(self, page_nums):
        """
        Sets self.page_nums to page_nums.
        ~
        Setting page_nums to True will cause this
        BlissTranslator to enumerate the bottom of each
        PDF page from translate().
        Setting page_nums to False will result in no page
        numbers.

        :param page_nums: bool, whether to enumerate
            translated PDF pages
        :return: None
        """
        self.page_nums = page_nums

    def set_fast_translate(self, fast_translate):
        """
        Sets self.fast_translate to fast_translate.
        ~
        Setting fast_translate to True will cause this
        BlissTranslator to translate the first instances of
        every word.
        Setting fast_translate to False will cause it to
        only translate a word after having seen it once.
        ~
        Sets translation speed for this BlissTranslator's
        translate() method.

        :param fast_translate: bool, whether to translate
            words to Blissymbols immediately
        :return: None
        """
        self.fast_translate = fast_translate

    def set_safe_translate(self, safe_translate):
        """
        Sets self.safe_translate to safe_translate.
        ~
        Setting safe_translate to True will cause this
        BlissTranslator to translate to Blissymbols only
        when confident the Blissymbol is appropriate.
        ~
        Setting safe_translate to False will cause it
        to translate all possible Blissymbols.
        ~
        Allows for users to view experimental Blissymbol
        translations.

        :param safe_translate: bool, whether to translate
            only Blissymbols with 100% confidence
        :return: None
        """
        self.safe_translate = safe_translate

    def set_translate_all(self, translate_all):
        """
        Sets self.translate_all to translate_all.
        ~
        Setting translate_all to True will cause this
        BlissTranslator to prompt the user for new
        Blissymbol definitions whenever an unknown word
        is reached.
        ~
        Setting translate_all to False will skip
        translating unknown words without any user input.
        ~
        Allows users to oversee experimental Blissymbol
        translations and set custom Blissymbol translations.

        :param translate_all: bool, whether to try translating
            all input words to Blissymbols
        :return: None
        """
        self.translate_all = translate_all

    def set_machine_translate(self, machine_translate):
        """
        Sets self.machine_translate to machine_translate.
        ~
        Setting machine_translate to True will initialize this
        BlissTranslator with a machine learning classifier
        for translating unknown words.

        :param machine_translate: bool, whether to initialize a
            machine learning classifier
        :return: None
        """
        self.machine_translate = machine_translate

        if self.machine_translate and self.classifier is None:
            try:
                from blisslearn import BlissLearner
            except ImportError:
                print("blisslearn module could not be imported.\n\
                Please find the local module blisslearn.py \n\
                and relocate it to the same directory as blisscribe.py.")
                return
            else:
                self.classifier = BlissLearner(self)

    def set_translatables(self):
        """
        Resets CHOSEN_POS according to this BlissTranslator's translatables
        (i.e., nouns, verbs, adjs, and other).

        :return: None
        """
        if self.other:  # adds all parts of speech
            self.CHOSEN_POS = self.PARTS_OF_SPEECH
        else:
            self.CHOSEN_POS = set()
            if self.nouns:
                self.CHOSEN_POS.add("NN")
                self.CHOSEN_POS.add("NNS")
            if self.verbs:
                self.CHOSEN_POS.add("VB")
                self.CHOSEN_POS.add("VBD")
                self.CHOSEN_POS.add("VBG")
                self.CHOSEN_POS.add("VBN")
            if self.adjs:
                self.CHOSEN_POS.add("JJ")
                self.CHOSEN_POS.add("JJR")
                self.CHOSEN_POS.add("JJS")

    def choose_nouns(self, nouns):
        """
        Allows user to set whether to translate nouns.

        :param nouns: bool, True to translate nouns
        :return: None
        """
        self.nouns = nouns
        self.set_translatables()

    def choose_verbs(self, verbs):
        """
        Allows user to set whether to translate verbs.

        :param verbs: bool, True to translate verbs
        :return: None
        """
        self.verbs = verbs
        self.set_translatables()

    def choose_adjs(self, adjs):
        """
        Allows user to set whether to translate adjectives.

        :param adjs: bool, True to translate adjectives
        :return: None
        """
        self.adjs = adjs
        self.set_translatables()

    def choose_other_pos(self, other):
        """
        Allows user to set whether to translate all other
        parts of speech.

        :param other: bool, True to translate other parts of speech
        :return: None
        """
        self.other = other
        self.set_translatables()

    def choose_translatables(self, nouns, verbs, adjs, other):
        """
        Allows user to set whether to translate nouns, verbs,
        adjectives, and/or all other parts of speech.
        ~
        Changes this BlissTranslator's variables with the same names.

        :param nouns: bool, True to translate nouns
        :param verbs: bool, True to translate verbs
        :param adjs: bool, True to translate adjectives
        :param other: bool, True to translate all other parts of speech
        :return: None
        """
        self.choose_nouns(nouns)
        self.choose_verbs(verbs)
        self.choose_adjs(adjs)
        self.choose_other_pos(other)
        self.set_translatables()

    def is_seen(self, word):
        """
        Returns True if the given word is part of the
        words_seen dict.

        :param word: str, word to check if in words_seen
        :return: bool, whether given word is in words_seen
        """
        return self.words_seen[word]

    def add_seen(self, word):
        """
        Adds word to words_seen dict.

        :param word: str, word to add to words_seen
        :return: None
        """
        self.words_seen[word] = True

    def is_changed(self, word):
        """
        Returns True if the given word is part of the
        words_changed dict.

        :param word: str, word to check if in words_changed
        :return: bool, whether given word is in words_changed
        """
        return self.words_changed[word]

    def add_changed(self, word):
        """
        Adds word to words_changed dict.

        :param word: str, word to add to words_changed
        :return: None
         """
        self.words_changed[word] = True

    def image_heights(self):
        """
        Returns a font size suitable as a subtitle for this
        BlissTranslator's default font_size.

        :return: int, subtitle font size
        """
        return self.font_size * 2

    def subtitle_size(self):
        """
        Returns a font size suitable as a subtitle for this
        BlissTranslator's default font_size.

        :return: int, subtitle font size
        """
        return int(self.font_size * 0.5)

    def get_space_size(self):
        """
        Returns an appropriate space size relative to this
        BT's font_size in pixels.

        :return: int, space size (in pixels)
        """
        return int(self.font_size * 0.75)

    def get_min_space(self):
        """
        Returns the minimum spacing between characters
        in pixels.

        Useful for standardizing punctuation spacing.

        :return: int, minimum space size (in pixels)
        """
        return 2

    def get_bliss_img(self, bliss_name):
        """
        Draws and returns a thumbnail Image of the given word's
        Blissymbol, with width not exceeding self.image_heights().
        ~
        If a word has multiple meanings, then return the Blissymbol
        corresponding to the best meaning in bliss_dict.

        :param bliss_name: str, Blissymbol image filename
        :return: Image, image of input str's Blissymbol
        """
        return get_bliss_img(bliss_name, max_height=self.image_heights())

    def display_images(self, pages):
        """
        Displays each image in pages.
        ~
        Useful for displaying multiple images when debugging.

        :param pages: List[Image], images to display
        :return: None
        """
        for page in pages:
            page.show()

    def save_image(self, img):
        """
        Saves the input Image, img, as a .png file.
        ~
        Names image beginning at this BlissTranslator's
        IMAGES_SAVED variable and incrementing by 1.
        ~
        Returns the filename for the given image.

        :param pages: Image, image to save to file
        :return: str, image's filename
        """
        filename = "bliss_img" + str(self.IMAGES_SAVED) + ".png"
        img.save(filename)
        self.IMAGES_SAVED += 1
        return filename

    def save_images(self, imgs):
        """
        Saves each Image in imgs as a .png file.
        ~
        Names each image beginning at this BlissTranslator's
        IMAGES_SAVED variable and incrementing by 1.
        ~
        After loop terminates, sets IMAGES_SAVED to the
        final accumulated value.
        ~
        Returns a list of the image filenames created.

        :param imgs: List[Image], images to save to file
        :return: List[str], image filenames
        """
        filenames = []

        for img in imgs:
            filename = self.save_image(img)
            filenames.append(filename)

        return filenames

    def delete_image(self, filename):
        """
        Deletes image with given filename.

        :param filename: str, image filename to delete
        :return: None
        """
        #filename = IMG_PATH + filename
        os.remove(filename)

    def delete_images(self, imgs):
        """
        Deletes images with filenames specified in imgs list.

        :param imgs: List[str], image filenames to delete
        :return: None
        """
        for img in imgs:
            self.delete_image(img)

    def make_title_page(self, pdf, title):
        """
        Returns the given PDF with a title page added to it.

        :param pdf: FPDF, pdf to add title page to
        :param title: str, title name
        :return: Image, title page
        """
        pdf.set_title(title)
        pdf.set_font(family=self.font_fam, size=self.font_size)
        pdf.add_page()
        pdf.write(int(pdf.h / 2), txt=title)
        return pdf

    def create_title_page(self, title, x, y):
        """
        Returns a title page of given dimensions x and y with the given
        title.
        :param title: str, title name
        :param x: int, x-dimension of output title page
        :param y: int, y-dimension of output title page
        :return: Image, title page
        """
        img = make_blank_img(x, y)
        title_img = get_word_img(title, self.font_size)

        img_x = x / 2 - title_img.size[0] / 2
        img_y = y / 3

        img.paste(title_img, (img_x, img_y))
        return img

    def get_page_filename(self, page_num):
        return "num" + str(page_num) + ".png"

    def make_page_num(self, page_num):
        """
        Draws and returns an image for a page number.
        ~
        Used for adding page numbers to bottom of PDFs.

        :param page_num: int, number of page
        :return: Image, page_num as a number image
        """
        number = get_word_img(str(page_num), self.font_path, self.font_size, self.image_heights())
        number = trim(number)
        num_fn = self.get_page_filename(page_num)
        number.save(num_fn)
        return number

    def save_pdf(self, filename, pages, margins=0):
        """
        Pastes each image file linked to in pages to a PDF.
        ~
        Saves PDF under given filename in this directory.

        Adapted from:
        https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images

        :param filename: str, filename for output PDF
        :param pages: List[str], image filenames to paste in PDF
        :param margins: int, space in margins (in pixels)
        :return: None
        """
        pdf = self.get_pdf(pages, margins)
        pdf.output(self.PATH + "/out/" + filename + ".pdf", "F")

    def get_pdf(self, filenames, margins=0):
        """
        Pastes each image file linked to in pages to a PDF.
        ~
        Returns PDF file.

        Adapted from:
        https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images

        :param filenames: List[str], image filenames to paste in PDF
        :param margins: int, space in margins (in pixels)
        :return: None
        """
        width, height = Image.open(filenames[0]).size
        new_w, new_h = width + (margins * 2), height + (margins * 2)

        pdf = FPDF(unit="pt", format=[new_w, new_h])
        idx = 0

        for filename in filenames:
            pdf.add_page()
            pdf.image(filename, x=margins, y=margins)

            if idx > 1 and self.page_nums:
                number = self.make_page_num(idx)
                num_fn = self.get_page_filename(idx)
                x = new_w / 2 - number.size[0]
                y = new_h - (margins / 2) - number.size[1]
                pdf.image(num_fn, x=x, y=y)
                os.remove(num_fn)

            self.delete_image(filename)  # deletes images once in PDF
            idx += 1

        return pdf

    def delete_pdf(self, filename):
        """
        Deletes PDF with given filename from out folder.

        :param filename: str, filename with .pdf extension
        :return: None
        """
        os.remove(self.PATH + "/outout/" + filename)

    # LANGUAGE PROCESSING
    # ===================
    def unicodize(self, text):
        """
        Returns the given text in unicode.
        ~
        Ensures all text is in unicode for parsing.

        :param text: str (byte), text to return in unicode
        :return: str (unicode), text in unicode
        """
        if text is not None:
            if not isinstance(text, unicode):
                text = text.decode("utf-8") #, errors='ignore')
        return text

    def deunicodize(self, text):
        """
        Returns the given text decoded from unicode.
        ~
        Ensures all text is in bytes for printing.

        :param text: str (unicode), text to decode from unicode
        :return: str (byte), text in unicode
        """
        if text is not None:
            if isinstance(text, unicode):
                text = text.encode("utf-8")
        return text

    def get_word_tag(self, trans_word):
        """
        Returns the given TranslationWord's part-of-speech tag.

        :param trans_word: TranslationWord, word to tag
        :return: str, given word's pos tag
        """
        if self.language != "English":
            tag = self.get_multilingual_tag(trans_word)

            if tag is not None and tag != "NN":
                # sets trans_word's tag to synset tag if
                # it's a better guess than tokenizer
                trans_word.set_pos(tag)

        return trans_word.get_pos()

    def get_token_phrase(self, phrase):
        """
        Returns a list of word tokens in phrase.

        :param phrase: str, text with >=1 words
        :return: List[str], list of word tokens
        """
        # [word for word in word_tokenize(phrase, language=self.language.lower())]
        return self.TOKENIZER.tokenize(phrase)

    def get_token_phrases(self, phrases):
        """
        Returns a list of word tokens in phrases,
        with a newline in between each phrase.

        :param phrases: List[str], phrases to tokenize
        :return: List[str], list of word tokens
        """
        token_phrases = []
        for phrase in phrases:
            token_phrases.extend(self.get_token_phrase(phrase))
            token_phrases.append("\n")
        return token_phrases

    def tokens_to_tags(self, token_phrase):
        """
        Given a list of strings composing a phrase, returns a list of words'
        part-of-speech tags in that order.

        :param token_phrase: List[str], list of word tokens from a phrase
        :return: List[str], list of word part-to-speech tags
        """
        tagged_phrase = pos_tag([token.lower() for token in token_phrase],
                                lang=self.lang_code)  # tokens tagged according to word type
        tagged_list = []
        for tup in tagged_phrase:
            tagged_list.append(tup[1])
        return tagged_list

    def abbreviate_tag(self, tag):
        """
        Given a full tag name, returns a tag abbreviation
        from "a", "v", "n", "r", "s",

        e.g. abbreviate_tag("RB") -> "r"

        :param tag: str, full tag name from POS_UNABBREVS
        :return: str, 1-character tag abbreviation
        """
        tag = tag[:2]
        if tag in self.POS_ABBREVS:
            return self.POS_ABBREVS[tag]
        else:
            return 'n'

    def unabbreviate_tag(self, tag):
        """
        Given a tag abbreviation from "a", "v", "n", "r", "s",
        returns the full tag name.

        e.g. unabbreviate_tag("r") -> "RB"

        :param tag: str, 1-character tag abbreviation
        :return: str, full tag name from POS_UNABBREVS
        """
        assert tag in self.POS_UNABBREVS
        return self.POS_UNABBREVS[tag]

    def is_word(self, word):
        """
        Returns False if the input is punctuation or whitespace,
        True otherwise.

        :param word: str, word to see if punctuation or whitespace
        :return: bool, whether word is punctuation or whitespace
        """
        return word not in self.PUNCTUATION.union(self.WHITESPACE)

    def is_whitespace(self, word):
        """
        Returns True if the input is whitespace,
        False otherwise.

        :param word: str, word to see if whitespace
        :return: bool, whether word is whitespace
        """
        return word in self.WHITESPACE

    def is_punctuation(self, word):
        """
        Returns True if the input is a punctuation mark.

        :param word: str, word to see if punctuation
        :return: bool, whether word is punctuation
        """
        return word in self.PUNCTUATION

    def is_starting_punct(self, word):
        """
        Returns True if the input is starting punctuation.

        :param word: str, word to see if starting punctuation
        :return: bool, whether word is starting punctuation
        """
        return word in self.START_PUNCT

    def is_ending_punct(self, word):
        """
        Returns True if the input is ending punctuation.

        :param word: str, word to see if ending punctuation
        :return: bool, whether word is ending punctuation
        """
        return word in self.END_PUNCT

    def is_newline(self, word):
        """
        Returns True if the input is a newline.

        :param word: str, word to see if newline
        :return: bool, whether word is newline
        """
        return word == "\n"

    def is_chosen_pos(self, pos):
        """
        Returns True if words with the given part of
        speech should be translated, False otherwise.

        :param pos: str, part-of-speech tag
        :return: bool, whether to translate pos
        """
        if self.lang_code != "eng":
            # FIXME: translate all words in non-English langs until better foreign tagging
            return True
        else:
            return pos in self.CHOSEN_POS

    def get_singular(self, noun):
        """
        Returns the singular form of the given noun
        in this BlissTranslator's set language.
        ~
        If noun cannot be singularized for this
        language, this method returns the input.

        :param noun: str, noun to singularize
        :return: str, singularized input
        """
        if self.language == "English":
            return en.singularize(noun)
        elif self.language == "Spanish":
            return es.singularize(noun)
        elif self.language == "German":
            return de.singularize(noun)
        elif self.language == "French":
            return fr.singularize(noun)
        elif self.language == "Italian":
            return it.singularize(noun)
        elif self.language == "Dutch":
            return nl.singularize(noun)
        else:
            return noun

    def get_infinitive(self, verb):
        """
        Returns the infinitive of the given verb
        in this BlissTranslator's set language.
        ~
        If no infinitive can be found in set language,
        this method returns the input.

        :param verb: str, verb
        :return: str, lemma of verb
        """
        if self.language == "English":
            return en.lemma(verb)
        elif self.language == "Spanish":
            return es.lemma(verb)
        elif self.language == "German":
            return de.lemma(verb)
        elif self.language == "French":
            return fr.lemma(verb)
        elif self.language == "Italian":
            return it.lemma(verb)
        elif self.language == "Dutch":
            return nl.lemma(verb)
        else:
            return verb

    def get_predicative(self, adj):
        """
        Returns the base form of the given adjective
        in this BlissTranslator's set language.
        ~
        If no base form can be found in set language,
        this method returns the input.

        e.g. well   -> good
             belles -> beau

        :param adj: str, adjective
        :return: str, base form of input adj
        """
        if self.language == "English":
            return en.predicative(adj)
        elif self.language == "Spanish":
            return es.predicative(adj)
        elif self.language == "German":
            return de.predicative(adj)
        elif self.language == "French":
            return fr.predicative(adj)
        elif self.language == "Italian":
            return it.predicative(adj)
        elif self.language == "Dutch":
            return nl.predicative(adj)
        else:
            return adj

    def in_bliss_dict(self, word):
        """
        Returns True if word in bliss_dict,
        False otherwise.

        :param word: str, word to check bliss_dict membership
        :return: bool, whether word is in bliss_dict
        """
        try:
            self.bliss_dict[word]
        except KeyError:
            return False
        else:
            return True

    def in_eng_bliss_dict(self, word):
        """
        Returns True if word in eng_bliss_dict,
        False otherwise.

        :param word: str, word to check eng_bliss_dict membership
        :return: bool, whether word is in eng_bliss_dict
        """
        return word in self.eng_bliss_dict

    def is_bliss_word(self, word):
        """
        Returns True if given word is a valid Blissymbol,
        i.e., if it exists in the Bliss dictionary.

        :param word: str, word to check if valid Blissymbol
        :return: bool, whether given word is valid Blissymbol
        """
        return word in self.bliss_to_unicode

    def lookup_bliss_dict(self, word):
        """
        Returns native language word's corresponding Blissymbols
        from this BlissTranslator's bliss_dict.
        ~
        If word is not in bliss_dict, returns None.

        :param word: str, word to lookup in bliss_dict
        :return: List[Blissymbol], word's blissymbols in bliss_dict
        """
        try:
            return self.bliss_dict[word]
        except KeyError:
            return

    def lookup_eng_bliss_dict(self, word):
        """
        Returns English word's corresponding Blissymbols
        from this BlissTranslator's eng_bliss_dict.
        ~
        If word is not in eng_bliss_dict, returns None.

        :param word: str, word to lookup in eng_bliss_dict
        :return: List[Blissymbol], word's blissymbols in eng_bliss_dict
        """
        try:
            return self.eng_bliss_dict[word]
        except KeyError:
            return

    def retrieve_lexicon(self, language):
        """
        Retrieves the lexicon dictionary for the given language
        from this BlissTranslator's self.lexica.
        ~
        If language is not in lexica, returns None.
        ~
        e.g. retrieve_lexicon("French") -> {"suis": "être",
                                            "est": "être"}

        :param language: str, language to retrieve lexicon for
        :return: dict, where...
            key (str) - inflected form of a word
            val (str) - lemma of inflected word
        """
        try:
            return self.lexica[language]
        except KeyError:
            return

    def lookup_blissnet(self, uni):
        """
        Returns this unicode's corresponding synsets
        from this BlissTranslator's blissnet.
        ~
        If unicode is not in blissnet, returns None.

        :param uni: str, Blissymbol unicode to lookup in blissnet
        :return: List[Synset], synsets corresponding to given unicode
        """
        try:
            return blissnet.BLISSNET[uni]
        except KeyError:
            return

    def in_wordnet(self, word, language):
        """
        Returns True if word in WordNet,
        False otherwise.

        :param word: str, word to check WordNet membership
        :return: bool, whether word is in WordNet
        """
        return word in wordnet.all_lemma_names(lang=self.LANG_CODES[language])

    def is_valid_word(self, word):
        """
        Returns True if word is a valid word in this
        BlissTranslator's native language, False otherwise.

        :param word: str, word to check if valid
        :return: bool, whether word is valid
        """
        return self.in_bliss_dict(word) #or self.in_wordnet(word, self.language)

    def is_valid_eng_word(self, word):
        """
        Returns True if word is a valid word in this
        BlissTranslator's native language, False otherwise.

        :param word: str, word to check if valid
        :return: bool, whether word is valid
        """
        return self.in_eng_bliss_dict(word) #or self.in_wordnet(word, "English")

    def remove_parens(self, word):
        """
        Removes parenthetical(s) from the given word and
        returns the result.
        ~
        Parenthetical begins at the first open parenthesis.

        e.g. get_parens("English_(language)") -> "English"

        :param word: str, word to get parenthetical from
        :return: str, given word's parenthetical phrase
        """
        idx = 0
        for char in word:
            if char != "(" and char != "[":
                idx += 1
            else:
                word = word[:idx]
                word = word.strip()
                word = word.strip("_")
                word = word.rstrip("-")
                return word
        return word

    def lemmatize(self, word, pos=None, language="English"):
        """
        Retrieves the given word's lemma,
        i.e., the word in dictionary entry form.
        ~
        e.g. lemmatize("ran") -> "run"
             lemmatize("puppies") -> "puppy"
        ~
        N.B. If a lemma for the given word cannot
        be found, this method returns the input.

        :param word: str, word to convert to lemma
        :param language: str, input word's native language
        :return: str, lemma of input word
        """
        if language != "English":
            bliss_dict = self.bliss_dict
        else:
            bliss_dict = self.eng_bliss_dict

        if word in bliss_dict:
            # check if word in official Blissymbols dict
            return word
        elif word.title() in bliss_dict:
            return word.title()
        elif word.lower() in bliss_dict:
            return word.lower()
        elif language in self.lexica:
            # check if word in Polish/French inflectional dict
            return self.lemmatize_multilingual(word, self.language)
        else:
            # otherwise, lemmatize word based on
            # best guess for its pos
            if pos is not None:
                short_pos = pos[:2]
                if pos == "NNS":
                    return self.get_singular(word)
                elif short_pos == "VB":
                    return self.get_infinitive(word)
                elif short_pos == "NN" and self.is_valid_word(self.get_infinitive(word)):
                    return self.get_infinitive(word)
                elif short_pos == "JJ" or short_pos == "RB":
                    return self.get_predicative(word)
                else:
                    return word.lower()
            else:
                if self.is_valid_word(self.get_singular(word)):
                    return self.get_singular(word)
                elif self.is_valid_word(self.get_infinitive(word)):
                    return self.get_infinitive(word)
                elif self.is_valid_word(self.get_predicative(word)):
                    return self.get_predicative(word)
                else:
                    return word.lower()

    def lemmatize_multilingual(self, word, language):
        """
        Returns the lemma corresponding to this word
        in the given language's lexicon.
        ~
        If language has no external lexicon, returns None.
        If word is not in lexicon, returns word.
        ~
        N.B. As yet Blisscribe only features 2 external
             lexica, French and Polish.

        :param word: str, multilingual word to lemmatize
        :param language: str, input word's native language
        :return: str, lemma of given word
        """
        lexicon = self.retrieve_lexicon(language)
        entry = word

        if lexicon is not None:
            if word in lexicon:
                pass
            elif word.lower() in lexicon:
                entry = entry.lower()
            elif word.title() in lexicon:
                entry = entry.title()
            else:
                return entry

        return lexicon[entry]

    def is_translatable(self, trans_word):
        """
        Returns True if trans_word's lemma or synonym(s)
        can be translated to Blissymbols, False otherwise.

        :param trans_word: TranslationWord, word to test whether translatable
        :return: bool, whether given trans_word is translatable
        """
        lemma = trans_word.get_lemma()
        # check if this word's lemma or synonyms are translatable
        if self.in_bliss_dict(lemma):
            return True
        elif self.is_synonym_translatable(trans_word):
            return True
        # if neither, word is untranslatable
        return False

    def is_synonym_translatable(self, trans_word):
        """
        Given a TranslationWord, returns True if any of its synonyms
        are translatable.

        :param trans_word: TranslationWord, word to generate synonyms
        :return: bool, whether trans_word synonyms are translatable
        """
        synonyms = self.translate_untranslatable(trans_word)

        if synonyms != []:
            trans_word.add_synsets_lemmas(synonyms)
            return True

        return False

    def should_be_translated(self, trans_word):
        """
        Returns True if given TranslationWord should be translated
        (according to this BlissTranslator's language
        preferences), False otherwise.

        :param trans_word: TranslationWord, word whether to translate
        :return: bool, whether this word should be translated
        """
        if trans_word.has_blissymbol():
            return True
        elif self.is_chosen_pos(trans_word.get_pos()):
            return self.is_translatable(trans_word)
        else:
            return False
            # return trans_word.has_blissymbol() or \
            #       self.is_chosen_pos(trans_word.get_pos()) and \
            #       self.is_translatable(trans_word)
            #       #and not self.is_punctuation(trans_word)

    def translate_now(self, trans_word):
        """
        Returns True if words with trans_word's lemma should be
        translated now, False if later/never.

        :param trans_word: TranslationWord, word to test
            whether to translate now
        :return: bool, whether to translate given lemma now
        """
        return self.fast_translate or self.is_seen(trans_word.get_lemma())

    def synsets_similarity(self, synsets):
        """
        Returns the similarity between two Wordnet Synsets
        as a float between 0 and 1.
        ~
        N.B. A similarity score of 1 denotes equality.

        :param synsets: List[Synset], list of synsets to compare
        :return: float, similarity between input synsets
        """
        similarities = []

        for idx in range(0, len(synsets)):
            first = synsets[idx - 1]
            other = synsets[idx]
            sim = self.synset_similarity(first, other)
            similarities.append(sim)

        return similarities

    def synset_similarity(self, synset1, synset2):
        """
        Returns the similarity between two Wordnet Synsets
        as a float between 0 and 1.
        ~
        N.B. A similarity score of 1 denotes equality.

        :param synset1: Synset, first synset to compare
        :param synset2: Synset, second synset to compare
        :return: float, similarity between input synsets
        """
        sim = wordnet.path_similarity(synset1, synset2)
        return sim

    def lookup_word_synsets(self, word, pos, lang="English"):
        """
        Returns a list of Wordnet Synsets corresponding to the
        given word, part-of-speech (pos), and language (lang).
        ~
        If lookup fails with given pos, this method returns
        given word's Wordnet synsets for all parts of speech.

        :param word: str, word to lookup synset for
        :param pos: str, part-of-speech for given word
        :param lang: str, language of given word
        :return: List[Synset], synsets corresponding to
            given word, pos, and lang
        """
        pos = self.abbreviate_tag(pos)

        if lang not in self.LANG_CODES:
            try:
                self.load_multilingual_lemmas(lang)
            except Exception:
                return []

        try:
            lang_code = self.LANG_CODES[lang]
            synsets = wordnet.synsets(word, pos, lang=lang_code)
        except Exception:
            return []
        else:
            if len(synsets) == 0:
                synsets = wordnet.synsets(word, lang=lang_code)
            return synsets

    def lookup_blissymbol_synsets(self, blissymbol):
        """
        Returns a list of Wordnet Synsets corresponding to the
        given Blissymbol.

        :param blissymbol: Blissymbol, blissymbol to lookup synset for
        :return: List[Synset], synsets corresponding to given blissymbol
        """
        if blissymbol.has_unicode():
            uni = blissymbol.get_unicode()
            synsets = self.lookup_blissnet(uni)
            if synsets is not None:
                return synsets
        return []

    def find_lang_code(self, language):
        """
        Returns the abbreviated 3-character language code for
        the given langauge.

        :param language: str, language name
        :return: str, 3-character language code
        """
        return self.LANG_CODES[language]

    def get_multilingual_tag(self, trans_word):
        """
        Given a non-English TranslationWord, find English synsets
        and derive a word tag.
        ~
        If no English synsets exist, return trans_word and NN tag.

        :param trans_word: TranslationWord, non-English word to tag
        :return: List[tuple(str,str)], word tag
        """
        # use_pos=False for foreign languages until tagging improves
        synsets = self.lookup_trans_word_synsets(trans_word, use_pos=False)

        try:
            synsets[0]
        except IndexError:
            pos = trans_word.get_pos()
            return pos
        else:
            pos = synsets[0].pos()
            pos = self.unabbreviate_tag(pos)
            return pos

    def get_multilingual_lemma(self, trans_word):
        """
        Given a non-English TranslationWord, find English synsets
        and derive an English lemma.
        ~
        If no English synsets exist, return trans_word's lemma.

        :param trans_word: TranslationWord, non-English word
        :return: str, English translation of given word
        """
        synsets = trans_word.get_synsets()

        try:
            synsets[0]
        except IndexError:
            return trans_word.get_lemma()
        else:
            synset = synsets[0]
            lemma = synset.lemma_names()[0]
            return lemma

    def lookup_trans_word_synsets(self, trans_word, use_pos=True, eng=False):
        """
        Returns a list of WordNet synsets for given TranslationWord.
        ~
        When use_pos is True, find synsets using trans_word's
        part-of-speech tag.  Else, find synsets in every part of speech.

        WordNet lookup link here:
        http://wordnetweb.princeton.edu/perl/webwn?s=&sub=Search+WordNet

        :param trans_word: TranslationWord, a word to lookup in WordNet
        :param use_pos: bool, whether to lookup trans_word's pos
        :param eng: bool, whether to lookup English synsets
        :return: List[Synset], the word's synsets
        """
        if eng:
            word = trans_word.get_eng_lemma()
            lang = self.LANG_CODES["English"]
        else:
            word = trans_word.get_lemma()  # trans_word.get_word()
            lang = self.lang_code

        if use_pos:
            pos = trans_word.get_pos()
            pos = self.abbreviate_tag(pos)
            synsets = wordnet.synsets(word, pos, lang=lang)

            if not self.safe_translate:
                synsets += wordnet.synsets(word, lang=lang)
        else:
            synsets = wordnet.synsets(word, lang=lang)

        return synsets

    def get_synset_lemmas(self, synset):
        """
        Given a synset, returns a list of its lemma names.

        :param synset: Synset, WordNet synset
        :return: List[str], WordNet lemma names
        """
        return synset.lemma_names(lang=self.lang_code)

    def get_synsets_lemmas(self, synsets):
        """
        Given a list of WordNet synsets, returns a list
        of all of their lemma names.

        :param synsets: List[Synset], synsets
        :return: List[str], lemmas for all synsets
        """
        lemmas = []
        for synset in synsets:
            lemmas.extend(self.get_synset_lemmas(synset))
        return lemmas

    def get_word_synsets_lemmas(self, trans_word):
        """
        Returns all lemma names in all synsets
        associated with given word.

        :param trans_word: TranslationWord, a word to lookup in WordNet
        :return: List[str], all this word's synsets' lemmas
        """
        return self.get_synsets_lemmas(self.lookup_trans_word_synsets(trans_word))

    def translate_synsets_lemmas(self, synsets):
        """
        Given a list of synsets, attempts to translate each
        synset into Blissymbols.
        ~
        If a synonym is translatable to Blissymbols, add that
        synonym to lemmas.
        ~
        At the end, return lemmas.

        :param synsets: List[Synset], a root word and its synonyms
        :return: List[str], word(s) in synset translatable to Blissymbols
        """
        lemmas = []
        for synset in synsets:
            for lemma in self.get_synset_lemmas(synset):
                if self.in_bliss_dict(lemma):
                    lemmas.append(lemma)
        return lemmas

    def get_synset_defn(self, synset):
        """
        Returns this Synset's definition.

        :param synset: Synset, a WordNet synset
        :return: str, the given synset's definition
        """
        return synset.definition()

    def get_synset_id(self, synset):
        """
        Gets the synset ID for this synset.

        :param synset: Synset, synset to find ID for
        :return: int, a 9-digit Wordnet Synset ID
        """
        try:
            offset = synset.offset()
        except AttributeError:
            return
        else:
            pos_code = self.POS_FEATURE_DICT[synset.pos()]
            return self.find_synset_id(offset, pos_code)

    def find_synset_id(self, offset, pos_code):
        """
        Returns a full synset ID for this offset and pos_code.

        :param offset: int, 7-digit offset of synset to find ID for
        :param pos_code: int, 1-digit pos code of synset to find ID for
        :return: int, a full 9-digit Wordnet Synset ID
        """
        full_synset = str(pos_code) + str(offset).zfill(8)
        return int(full_synset)

    def translate_untranslatable(self, trans_word):
        """
        Attempts to translate the given word's synonyms to
        Blissymbols.
        ~
        If a synonym can be translated, this method returns
        that synonym. Otherwise, this method returns the
        input word.

        :param word: str, word to translate to Blissymbols
        :return: List[str], translatable synonym(s) of given word
        """
        return self.translate_synsets_lemmas(self.lookup_trans_word_synsets(trans_word))

    def make_translation_word(self, word_token, pos, debug=False, language="English"):
        """
        Returns a new TranslationWord with...
            given token as its word
            given pos as its pos
            this BlissTranslator as its translator
            given debug as its debug setting

        :param word_token: str, a word token representing the word as found in text
        :param pos: str, the given word token's (Penn Treebank) part-of-speech
        :param debug: bool, whether user will provide new inputs to TranslationWord
        :param language: str, native language of given word token
        :return: TranslationWord, a new TranslationWord with the given fields
        """
        return TranslationWord(word=word_token, pos=pos, translator=self, debug=debug, language=language)

    def make_blissymbol(self, img_filename, pos, derivation, translations=None):
        """
        Returns a new Blissymbol with...
            given img_filename as its English image filename (ending in .png)
            given pos as its part-of-speech
            given derivation as its list of Blissymbol derivations

        :param img_filename: str, the image filename for this Blissymbol
        :param pos: str, the given word token's (Penn Treebank) part-of-speech
        :param derivation: str, this Blissymbol's derivation, of the form:
            "(d(1) + d(2) + ... + d(n))"
            where d(1) to d(n) are derivative bliss names
        :param translations: dict, where...
            key (str) - language of Blissymbol translation
            val (List[str]) - Blissymbol's translations in language
        :return: Blissymbol, a new Blissymbol with the given fields
        """
        if translations is not None:
            translations = translations
        else:
            translations = {}
        translations.setdefault(self.language, [])
        translations["English"] = [name for name in img_filename[:-4].split(",")]
        return Blissymbol(img_filename=img_filename,
                          pos=pos,
                          derivation=derivation,
                          translations=translations,
                          translator=self)

    def fetch_bliss_name(self, word, language="English"):
        """
        Returns the Blissymbol name associated with the
        given word.
        ~
        e.g. fetch_bliss_name("lapin", "French") -> "rabbit,hare"

        :param word: str, word to get Blissymbol name of
        :param language: str, word's native language
        :return: str, Blissymbol name for given word
        """
        bliss = self.word_to_blissymbol(word, language)
        if bliss is not None:
            return bliss.get_bliss_name()
        else:
            return

    def word_to_blissymbol(self, word, language="English"):
        """
        Returns the most likely Blissymbol corresponding to the given word.
        ~
        This method performs a lookup on word in eng_bliss_dict if
        language is English, otherwise in bliss_dict.
        ~
        If the given word cannot be translated to a Blissymbol,
        this method returns None.

        :param word: str, word to lookup Blissymbol for
        :param language: str, word's native language
        :return: Blissymbol, a Blissymbol corresponding to the given word
        """
        word = word.strip()
        new_word = word.replace(" ", "_")
        raw_word = self.remove_parens(new_word)
        raw_words = raw_word.split(",")
        if len(raw_words) > 1:
            raw_word = raw_words[0]

        if language == "English":
            blissymbols = self.lookup_eng_bliss_dict(raw_word)
        else:
            blissymbols = self.lookup_bliss_dict(raw_word)

        blissymbol = None

        if blissymbols is None:
            return blissymbol

        elif len(blissymbols) == 1:
            blissymbol = blissymbols.pop()
            blissymbols.add(blissymbol)
            return blissymbol

        elif raw_word == "indicator" and word != "indicator":
            for blissymbol in blissymbols:
                name = blissymbol.get_bliss_name()
                if name == new_word:
                    return blissymbol
            else:
                return

        elif len(blissymbols) > 1:
            for blissymbol in blissymbols:
                name = blissymbol.get_bliss_name()
                derivs = blissymbol.get_derivations()

                if not blissymbol.is_neutral():
                    continue
                elif new_word == name:
                    return blissymbol
                elif new_word in name.split(","):
                    if word not in derivs:
                        return blissymbol
            else:
                for blissymbol in blissymbols:
                    if blissymbol.get_is_atom() or new_word in blissymbol.get_derivations():
                        return blissymbol
                else:
                    blissymbol = blissymbols.pop()
                    blissymbols.add(blissymbol)
                    return blissymbol

    def add_bliss_entry(self, blissymbol):
        """
        Adds given Blissymbol to this BlissTranslator's bliss_dict.

        :param blissymbol: Blissymbol, entry to add
        :return: None
        """
        languages = ["English", self.language]

        for language in languages:
            translations = blissymbol.get_translation(language)
            for translation in translations:
                if language == "English":
                    self.eng_bliss_dict.setdefault(translation, set())
                    self.eng_bliss_dict[translation].add(blissymbol)
                else:
                    self.bliss_dict.setdefault(translation, set())
                    self.bliss_dict[translation].add(blissymbol)

    def remove_duplicates(self, items):
        """
        Deletes all duplicates from input list of items.
        ~
        Returns refreshed list.

        :param unicodes: List[X], list to delete duplicates from
        :return: List[X], list without duplicates
        """
        seen = set()
        seen_add = seen.add
        return [item for item in items if not (item in seen or seen_add(item))]

    # TRANSLATOR
    # ==========
    def translate(self, phrase, title="translation", title_page=False, img_w=DIMS[0], img_h=DIMS[1]):
        """
        Translates input phrase to Blissymbols according to this
        BlissTranslator's POS and language preferences.
        ~
        Saves translation to a PDF file in this directory's
        outout folder with the given title, or otherwise
        titled after the given phrase's first 20 characters.
        ~
        Default image size is 816x1056px (standard PDF page).

        :param phrase: str, text in BlissTranslator's native language
        :param title: str, desired title for output PDF
        :param title_page: bool, whether to create title page
        :param img_w: int, desired width of PDF pages (in pixels)
        :param img_h: int, desired height of PDF pages (in pixels)
        :return: None
        """
        title, phrase = self.unicodize(title), self.unicodize(phrase)
        images = self.translate_to_images(phrase)
        pages = self.images_to_pages(images, img_w, img_h)
        if title_page:
            title_pg = self.create_title_page(title, img_w, img_h)
            pages.insert(0, title_pg)
        self.pages_to_pdf(pages, title)
        #self.delete_images(NEW_BLISSYMBOLS)
        del NEW_BLISSYMBOLS[:]
        self.lex_parser.refresh_bliss_lexicon()
        self.refresh_bliss_and_unicode()

    def translate_to_transwords(self, phrase):
        """
        Translates the given phrase to a list of TranslationWords
        and returns the list.

        :param phrase: str, phrase to translate to TranslationWords
        :return: List[TranslationWord], TWs for each word/symbol in phrase
        """
        phrases = phrase.split("\n")  # split input by newlines
        token_phrases = self.get_token_phrases(phrases)
        tagged_list = self.tokens_to_tags(token_phrases)
        trans_words = list()

        for idx in range(len(token_phrases)):
            word_token = token_phrases[idx]
            word_tag = tagged_list[idx]
            trans_word = self.make_translation_word(word_token, word_tag, self.translate_all, self.language)
            trans_words.append(trans_word)

        return trans_words

    def translate_to_images(self, phrase):
        """
        Translates the given phrase to a list of Images
        and returns the list.

        :param phrase: str, phrase to translate to TranslationWords
        :return: List[Images], an Image for each word/symbol in phrase
        """
        trans_words = self.translate_to_transwords(phrase)
        imgs = list()

        for trans_word in trans_words:
            lemma = trans_word.get_lemma()
            if lemma == "\n":
                imgs.append(None)
            else:
                subs = (self.should_be_translated(trans_word) or self.translate_now(trans_word)) and \
                       (self.sub_all or not self.is_changed(lemma))
                if subs:
                    self.add_changed(lemma)
                img = get_subbed_bliss_img(trans_word, max_height=self.image_heights(), subs=subs)
                imgs.append(img)

        return imgs

    def images_to_pages(self, images, w=DIMS[0], h=DIMS[1]):
        """
        Pastes each image in images to a list of pages.
        ~
        Returns output list of pages.

        :param images: List[Image], Images to paste to pages (in order)
        :param w: int, desired width of each page (in pixels)
        :param h: int, desired height of each page (in pixels)
        :return: List[Image], pages with images pasted
        """
        space = self.get_space_size()
        indent = self.font_size

        pages = list()
        new_page = lambda: make_blank_img(w, h)
        page = new_page()

        x, y = indent, 0
        inc_x = lambda img: x + img.size[0] + space
        inc_y = lambda: y + int(self.image_heights()*1.5)

        for image in images:
            if image is None:
                # start new paragraph
                x = indent
                y = inc_y()
            else:
                if inc_x(image) > w:
                    x = 0
                    y = inc_y()
                if y > h:
                    pages.append(page)
                    page = new_page()

                page.paste(image, (x, y))
                x = inc_x(image)

        pages.append(page)
        return pages[::-1]

    def pages_to_pdf(self, pages, title):
        """
        Pastes each page in pages to a PDF.
        ~
        Saves the PDF to /out/ under the given title.

        :param pages: List[Image], pages with images pasted (in order)
        :param title: str, desired title for output PDF
        :return: None
        """
        filenames = self.save_images(pages)
        self.save_pdf(title, filenames, margins=50)

    def analyze_concepts(self, phrase):
        """
        Translates the given phrase to Blissymbols and
        returns a frequency dictionary of the most common
        derivative Blissymbols in the output translations.

        :param phrase: str, phrase to analyze concepts of
        :return: dict, where...
            key (str) - name of Blissymbol
            val (int) - number of occurrences in translation
        """
        phrase = self.unicodize(phrase)
        trans_words = self.translate_to_transwords(phrase)
        return self.analyze_trans_word_concepts(trans_words)

    def analyze_trans_word_concepts(self, trans_words):
        """
        Returns a frequency dictionary of the most common
        derivative Blissymbols in given trans_words.

        :return: List[TranslationWord], TWs for each word in a phrase
        :return: dict, where...
            key (str) - name of Blissymbol
            val (int) - number of occurrences in translation
        """
        concept_freqs = dict()

        for trans_word in trans_words:
            if trans_word.has_blissymbol():
                blissymbol = trans_word.get_blissymbol()
                subsymbols = blissymbol.get_subsymbols()

                if len(subsymbols) != 0:
                    for subsymbol in subsymbols:
                        name = subsymbol.get_bliss_name()
                        concept_freqs.setdefault(name, int())
                        concept_freqs[name] += 1

        return concept_freqs
               # {concept: concept_freqs[concept] for concept in concept_freqs
               # if concept_freqs[concept] > 1}

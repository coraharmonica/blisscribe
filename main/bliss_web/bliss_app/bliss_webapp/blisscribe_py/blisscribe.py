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
import os
from nltk.tokenize import WordPunctTokenizer  # word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet
from pattern import text
from pattern.text import en, es, fr, de, it, nl
from PIL import Image, ImageDraw, ImageFont, ImageChops
from fpdf import FPDF
#import bliss_exceptions
import blissnet
from blissnet import BLISSNET as blissnet

try:
    from parse_lexica import LexiconParser, Blissymbol, \
        BLISS_TO_UNICODE, UNICODE_TO_BLISS, \
        NEW_BLISSYMBOLS, BLISS_SUPPORTED_LANGUAGES
except ImportError:
    raise ImportError("parse_lexica module could not be imported.\n\
    Please find the local module parse_lexica.py \n\
    and relocate it to the same directory as blisscribe.py.")
else:
    from parse_lexica import LexiconParser, Blissymbol, \
        BLISS_TO_UNICODE, UNICODE_TO_BLISS, \
        NEW_BLISSYMBOLS
    from parse_lexica import BLISS_SUPPORTED_LANGUAGES as BLISS_LANGS

try:
    import blisslearn
    from blisslearn import BlissLearner
except ImportError:
    raise ImportError
    print("blisslearn module could not be imported.\n\
    Please find the local module blisslearn.py \n\
    and relocate it to the same directory as blisscribe.py.")
else:
    import blisslearn
    from blisslearn import BlissLearner

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
    Use chooseTranslatables() to set whether to translate nouns,
    verbs, adjectives, and/or other parts of speech.
    ~
    By default, a BlissTranslator will translate all parts of
    speech in CHOSEN_POS, i.e., nouns, verbs, and adjectives.
    To translate all other parts of speech, set self.other to True.
    ~
    Contains methods for:
        1) selecting which parts of speech to translate
           --> chooseTranslatables()
           --> chooseNouns()
           --> chooseVerbs()
           --> chooseAdjs()
           --> chooseOtherPOS()
        2) selecting whether to translate text to Blissymbols
           immediately or gradually
           --> setFastTranslate()
        3) selecting font & font size for output PDF translations
           --> setFont()
        4) selecting whether to subtitle all Blissymbols or only
           new Blissymbols
           --> setSubAll()
    """
    PATH = os.path.dirname(os.path.realpath(__file__))
    
    # FONTS
    # -----
    ROMAN_FONT = "/Library/Fonts/Times New Roman.ttf"
    SANS_FONT = "/Library/Fonts/Arial.ttf"
    HIP_FONT = "/Library/Fonts/Helvetica.dfont"
    BLISS_FONT = "/Users/courtney/Library/Fonts/Blissymbolics.ttf"
    FONT_FAMS = {"Times": ROMAN_FONT,
                 "Arial": SANS_FONT,
                 "Helvetica": HIP_FONT,
                 "Blissymbols": BLISS_FONT}
    FONT_PATHS = {ROMAN_FONT: "Times",
                  SANS_FONT: "Arial",
                  HIP_FONT: "Helvetica",
                  BLISS_FONT: "Blissymbols"}
    DEFAULT_FONT_SIZE = 30
    
    # IMAGES
    # ------
    IMG_PATH = PATH + "/symbols/png/full/"
    IMAGES_SAVED = 0
    
    # LANGUAGE
    # --------
    STARTING_PUNCT = set(["(", '"', "-",
                          "\xe2\x80\x9c", "\xe2\x80\x98", "\xe2\x80\x9e"])  # spaces BEFORE
    ENDING_PUNCT = set([".", ",", ";", ":", "?", "!", ")", '"', "-",
                        "\xe2\x80\x9d", "\xe2\x80\x99", u"\u201d"])  # spaces AFTER
    PUNCTUATION = STARTING_PUNCT.union(ENDING_PUNCT)
    MID_PUNCT = set(["-", u"\u2013", u"\u2014"])
    CONTRACTIONS = set("'")
    for punct in string.punctuation:
        PUNCTUATION.add(str(punct))
    PUNCTUATION = PUNCTUATION.union(MID_PUNCT.union(CONTRACTIONS))
    WHITESPACE = set(["\n", '', ' ', '_'])

    # --> Parts of Speech
    # Penn Treebank parts-of-speech set
    PARTS_OF_SPEECH = set(["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS",
                           "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$",
                           "RB", "RBR", "RBS", "RP", "TO", "UH", "VB", "VBD", "VBG",
                           "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"])
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
    POS_UNABBREVS = {"a": "JJ", "s": "JJS", "n": "NN", "v": "VB", "r": "RB"}
    POS_ABBREVS = {"JJ": "a", "JJS": "s", "NN": "n", "VB": "v", "RB": "r"}
    POS_NAMES = {"a": "ADJ", "s": "ADJ", "n": "NOUN", "v": "VERB", "r": "ADV"}
    POS_FEATURE_DICT = {"n": 1, "v": 2, "a": 3, "s": 3, "r": 4}

    DEFAULT_POS = set(["NN", "NNS", "VB", "VBD", "VBG", "VBN", "JJ", "JJR", "JJS"])
    CHOSEN_POS = DEFAULT_POS
    DEFAULT_LANG = "English"
    LANG_CODES = {"Arabic": "arb",
                  "Bulgarian": 'bul',
                  "Catalan": 'cat',
                  "Danish": 'dan',
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
    WORDNET_LANGS = wordnet.langs() #set(LANG_CODES.keys())
    WORDNET_LANG_CODES = set(LANG_CODES.values())
    TOKENIZER = WordPunctTokenizer()
    SUPPORTED_LANGS = BLISS_LANGS.intersection(WORDNET_LANGS)
    PATTERN_LANGS = text.LANGUAGES

    def __init__(self, language="English", font_path=SANS_FONT, font_size=DEFAULT_FONT_SIZE):
        self.lex_parser = LexiconParser(translator=self)
        # Fonts
        self.font_size = font_size
        self.font_path = font_path
        self.font = ImageFont
        self.setFont(self.font_path, self.font_size)
        self.font_fam = self.FONT_PATHS[self.font_path]

        # Images
        self.image_heights = self.font_size*2
        self.pages = []
        self.sub_all = False
        self.page_nums = True

        # Language
        self.bliss_dict = dict
        self.eng_bliss_dict = dict
        self.bliss_lexicon = self.lex_parser.getBlissLexicon()
        print(self.bliss_lexicon)
        self.uni_to_bliss = UNICODE_TO_BLISS
        self.bliss_to_uni = BLISS_TO_UNICODE
        self.polish_lexicon = dict
        self.french_lexicon = dict
        self.language = str #self.DEFAULT_LANG
        self.lang_code = str
        self.setLanguage(language)
        self.fast_translate = False
        self.safe_translate = False
        self.translate_all = False
        self.words_seen = dict
        self.words_changed = dict
        self.initSeenChanged()
        self.defns_chosen = {}  # holds user choices for correct word definitions

        # --> parts of speech
        self.nouns = True
        self.verbs = True
        self.adjs = True
        self.other = False

        self.all_lemma_names = set(wordnet.all_lemma_names(lang=self.lang_code))
        self.classifier = BlissLearner(self)

    # GETTERS/SETTERS
    # ===============
    @property
    def getLexParser(self):
        return self.lex_parser

    def getWordNetLangs(self):
        return wordnet.langs()

    def getFont(self, font_path, font_size):
        """
        Returns an ImageFont with given font_path and font_size.
        ~
        If font_path is invalid, returns an ImageFont using this
        BlissTranslator's ROMAN_FONT and font_size.

        :param font_path: str, path to font file
        :param font_size: int, desired font size
        :return: ImageFont, font with given path and font size
        """
        try:
            ImageFont.truetype(font_path, font_size)
        except IOError:
            self.font_path = self.ROMAN_FONT
            return ImageFont.truetype(self.ROMAN_FONT, font_size)
        else:
            return ImageFont.truetype(font_path, font_size)

    def setFont(self, font_path, font_size):
        """
        Sets this BlissTranslator's default font to an ImageFont
        with given font_path and font_size.
        ~
        If font_path is invalid, uses BlissTranslator's ROMAN_FONT.

        :param font_path: str, path to font file
        :param font_size: int, desired font size
        :return: None
        """
        self.font = self.getFont(font_path, font_size)

    def setLanguage(self, language):
        """
        Sets this BlissTranslator's native language
        to the input language.
        ~
        If given language is invalid, do not change this
        BlissTranslator's default language.

        :param language: str, language to set to default
        :return: None
        """
        if language in BLISS_LANGS:
            self.language = language
        else:
            self.language = "English"

        self.lang_code = self.findLangCode(self.language)

        if self.lang_code not in self.WORDNET_LANGS:
            self.loadMultiLingualLemmas(self.language)

        self.setBlissDict()
        self.bliss_lexicon = self.initBlissLexicon()

    def getLanguage(self):
        """
        Returns this BlissTranslator's native language.

        :return: str, BlissTranslator's language
        """
        return self.language

    def loadMultiLingualLemmas(self, lang):
        """
        Assumes this BlissTranslator's language isn't part of
        default WordNet, and tries to load a custom tab file
        in the given language to WordNet instead.
        ~
        If no such file can be loaded, raises an Exception.
        ~
        Used to add non-default OMWs to WordNet.

        :return: None
        """
        assert lang not in self.WORDNET_LANGS

        lang_code = self.LANG_CODES[lang]
        tab_file = self.lex_parser.getTabFile(lang_code)

        if tab_file is not None:
            wordnet.custom_lemmas(tab_file, lang_code)
            self.WORDNET_LANGS = wordnet.langs()
        else:
            raise Exception("Blisscribe doesn't support this language yet... oops!")

    def entryToBlissymbol(self, entry):
        """
        Returns the given string entry as a Blissymbol.

        :param entry: 4-tuple(str), string to turn to Blissymbol
        :return: Blissymbol, Blissymbol representation of given entry
        """
        blissymbol = self.lex_parser.entryToBlissymbol(entry)
        self.addBlissEntry(blissymbol)
        return blissymbol

    def initBlissLexicon(self):
        """
        Initializes a Bliss dictionary in English corresponding to
        the universal Blissymbol lexicon.

        :return: None
        """
        lexicon = self.lex_parser.bliss_lexicon
        self.lex_parser.bliss_lexicon = self.bliss_lexicon
        self.bliss_lexicon = {entry: self.entryToBlissymbol(lexicon[entry][0])
                              for entry in sorted(lexicon)}

    def initBlissDict(self, language):
        """
        Returns a 2-tuple of 2 Bliss dictionaries, where the
        first dict is in this BlissTranslator's set language
        and the second dict is in English.

        :return: tuple(dict,dict), where...
            key (str) - word in specified language
            val (List[Blissymbol]) - corresponding Blissymbols
        """
        return self.lex_parser.initBlissLexica(self, language)

    def setBlissDict(self):
        """
        Initializes this BlissTranslator's bliss_dict in
        its native language.

        :return: None
        """
        bliss_dicts = self.initBlissDict(self.language)
        self.bliss_dict = bliss_dicts[0]
        
        #if self.language != "English":
        self.eng_bliss_dict = bliss_dicts[1]

        if self.language == "Polish":
            self.polish_lexicon = \
                self.lex_parser.parseLexicon("/resources/lexica/polish.txt")
        elif self.language == "French":
            self.french_lexicon = \
                self.lex_parser.parseFrenchLexicon("/resources/lexica/french.txt")

    def getBlissDict(self):
        """
        Returns this BlissTranslator's native language Bliss dictionary.

        :return: dict, where...
            key (str) - word in BlissTranslator's native language
            val (List[Blissymbol]) - corresponding Blissymbols
        """
        return self.bliss_dict

    def getEngBlissDict(self):
        """
        Returns this BlissTranslator's English Bliss dictionary.

        :return: dict, where...
            key (str) - word in English
            val (List[Blissymbol]) - corresponding Blissymbols
        """
        return self.eng_bliss_dict

    def getBlissLexicon(self):
        """
        Returns this BlissTranslator's Bliss dictionary
        corresponding to the universal Blissymbol lexicon.

        :return: dict, where...
            key (str) - word in English
            val (List[Blissymbol]) - corresponding Blissymbols
        """
        return self.bliss_lexicon

    def getBlissnet(self):
        """
        Returns the Blissymbols Wordnet, Blissnet.

        :return: dict, where...
            key (str) - Blissymbols unicode symbol
            val (List[Synset]) - corresponding Synsets
        """
        return blissnet

    def initSeenChanged(self):
        """
        Initializes this BlissTranslator's words_seen
        as a default dict.

        :return: None
        """
        self.words_seen = collections.defaultdict(bool)
        self.words_changed = collections.defaultdict(bool)

    def getBlissToUnicode(self):
        """
        Returns the global Blissymbols-to-unicode
        encoding dictionary.

        :return: dict, where...
            key (str) - Blissymbol name
            val (List[str]) - unicode Blissymbol codes (in hexadecimal)
        """
        return self.bliss_to_uni

    def getUnicodeToBliss(self):
        """
        Returns the global unicode-to-Blissymbols
        encoding dictionary.

        :return: dict, where...
            key (str) - unicode Blissymbol code (in hexadecimal)
            val (List[str]) - list of Blissymbol names
        """
        return self.uni_to_bliss

    def lookupBlissToUnicode(self, bliss):
        """
        Returns the global Blissymbols-to-unicode
        encoding dictionary.

        :param bliss: str, name of blissymbol to lookup
        :return: List[str], unicode names for given bliss
        """
        try:
            return self.bliss_to_uni[bliss]
        except KeyError:
            return []

    def lookupUnicodeToBliss(self, uni):
        """
        Returns the global unicode-to-Blissymbols
        encoding dictionary.

        :param uni: str, unicode name to lookup
        :return: List[str], blissymbol names for given unicode
        """
        try:
            defns = self.uni_to_bliss[uni]
        except KeyError:
            return []
        else:
            return defns

    def addBlissToUnicode(self, bliss, uni):
        """
        Adds the given blissymbol-unicode pair to this
        BlissTranslator's Blissymbols-to-unicode
        encoding dictionary.

        :param bliss: str, name of blissymbol to add
        :param uni: str, unicode name for given bliss
        :return: None
        """
        if bliss not in self.bliss_to_uni:
            self.bliss_to_uni[bliss] = []
        if uni not in self.bliss_to_uni[bliss]:
            self.bliss_to_uni[bliss].append(uni)

    def addUnicodeToBliss(self, uni, bliss):
        """
        Adds the given unicode-blissymbol pair to this
        BlissTranslator's unicode-to-Blissymbols
        encoding dictionary.

        :param uni: str, unicode name to add
        :param bliss: str, blissymbol name for given unicode
        :return: None
        """
        if uni not in self.uni_to_bliss:
            self.uni_to_bliss[uni] = []
        if bliss not in self.uni_to_bliss[uni]:
            self.uni_to_bliss[uni].append(bliss)

    def setSubAll(self, sub_all):
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

    def setPageNums(self, page_nums):
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

    def setFastTranslate(self, fast_translate):
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

    def setSafeTranslate(self, safe_translate):
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

    def setTranslateAll(self, translate_all):
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

    def setTranslatables(self):
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

    def chooseNouns(self, nouns):
        """
        Allows user to set whether to translate nouns.

        :param nouns: bool, True to translate nouns
        :return: None
        """
        self.nouns = nouns
        self.setTranslatables()

    def chooseVerbs(self, verbs):
        """
        Allows user to set whether to translate verbs.

        :param verbs: bool, True to translate verbs
        :return: None
        """
        self.verbs = verbs
        self.setTranslatables()

    def chooseAdjs(self, adjs):
        """
        Allows user to set whether to translate adjectives.

        :param adjs: bool, True to translate adjectives
        :return: None
        """
        self.adjs = adjs
        self.setTranslatables()

    def chooseOtherPOS(self, other):
        """
        Allows user to set whether to translate all other
        parts of speech.

        :param other: bool, True to translate other parts of speech
        :return: None
        """
        self.other = other
        self.setTranslatables()

    def chooseTranslatables(self, nouns, verbs, adjs, other):
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
        self.chooseNouns(nouns)
        self.chooseVerbs(verbs)
        self.chooseAdjs(adjs)
        self.chooseOtherPOS(other)
        self.setTranslatables()

    def isSeen(self, word):
        """
        Returns True if the given word is part of the
        words_seen dict.

        :param word: str, word to check if in words_seen
        :return: bool, whether given word is in words_seen
        """
        return self.words_seen[word]

    def addSeen(self, word):
        """
        Adds word to words_seen dict.

        :param word: str, word to add to words_seen
        :return: None
        """
        self.words_seen[word] = True

    def isChanged(self, word):
        """
        Returns True if the given word is part of the
        words_changed dict.

        :param word: str, word to check if in words_changed
        :return: bool, whether given word is in words_changed
        """
        return self.words_changed[word]

    def addChanged(self, word):
        """
        Adds word to words_changed dict.

        :param word: str, word to add to words_changed
        :return: None
         """
        self.words_changed[word] = True

    # IMAGES
    # ======
    def getWordWidth(self, word):
        """
        Returns the width of the given string or Image in pixels.

        :param word: str or Image
        :return: int, word width in pixels
        """
        if word == "\n":
            return self.getSpaceSize()
        elif type(word) == str:
            return self.trimHorizontal(self.getWordImg(word, self.font_size)).size[0]
        else:
            try:
                return word.size[0]
            except AttributeError:
                return self.font_size

    def makeBlankImg(self, x, y):
        """
        Returns a blank (white) image of dimensions x and y.

        :param x: int, x-dimension of image
        :param y: int, y-dimension of image
        :return: Image, blank image
        """
        return Image.new("RGBA", (x, y), (255, 255, 255, 255))

    def getWordImg(self, word, font_size=None):
        """
        Draws and returns an Image of given word in given font_size.
        ~
        If font_size is left as None, uses this BlissTranslator's
        font size.

        :param word: str, word to render to Image
        :param font_size: int, desired font size for string
        :return: Image, image of input str
        """
        if font_size is None:
            font_size = self.font_size

        img = self.makeBlankImg(len(word) * font_size,
                                self.image_heights)
        if word == "\n":
            return img
        else:
            word = self.unicodize(word)
            sketch = ImageDraw.Draw(img)
            sketch.text((0, font_size/2),
                        word,
                        font=ImageFont.truetype(font=self.font_path, size=font_size),
                        fill="black")
            return self.trimHorizontal(img)

    def getBlissImg(self, img_filename, max_width, max_height): #trans_word, max_width, max_height):
        """
        Draws and returns a thumbnail Image of the given word's
        Blissymbol, with width not exceeding max_width.
        ~
        If a word has multiple meanings, then return the Blissymbol
        corresponding to the best meaning in bliss_dict.

        :param img_filename: str, Blissymbol image filename
        :param max_width: int, maximum width of Image (in pixels)
        :param max_height: int, maximum height of Image (in pixels)
        :return: Image, image of input str's Blissymbol
        """
        '''
        if trans_word == "indicator plural":
            img_filename = "indicator_(plural).png"
        else:
            img_filename = trans_word.getFilename()
            if img_filename is None:
                raise IOError("Word cannot be translated to Blissymbols...")
        '''
        img = Image.open(self.IMG_PATH + img_filename + ".png")
        img.thumbnail((max_width, max_height))
        return img

    def getTransBlissImg(self, trans_word, max_width, max_height):
        """
        Draws and returns a thumbnail Image of the given word's
        Blissymbol, with width not exceeding max_width.
        ~
        If a word has multiple meanings, then return the Blissymbol
        corresponding to the best meaning in bliss_dict.

        :param trans_word: TranslationWord, word to render to Image
        :param max_width: int, maximum width of Image (in pixels)
        :param max_height: int, maximum height of Image (in pixels)
        :return: Image, image of input str's Blissymbol
        """
        #if trans_word == "indicator plural":
        #    img_filename = "indicator_(plural).png"
        #else:
        img_filename = trans_word.getBlissName()

        if img_filename is None:
            raise IOError("Word cannot be translated to Blissymbols...")
        else:
            return self.getBlissImg(img_filename, max_width, max_height)

        #bliss_word = Image.open(self.IMG_PATH + img_filename)
        #img = bliss_word
        #img.thumbnail((max_width, max_height))
        #return img

    def getSubbedBlissImg(self, trans_word, max_width, max_height, subs=True):
        """
        Returns the given word as a Blissymbol with subtitles
        in this BlissTranslator's chosen language.
        ~
        If subs is set to False, output Image has no subtitles, but
        still offsets as if there were.

        :param trans_word: TranslationWord, word to translate & subtitle
        :param max_width: int, max width of output image
        :param max_height: int, max height of output image
        :param subs: bool, whether to subtitle output image
        :return: Image, subtitled Blissymbol image
        """
        bg = self.makeBlankImg(max_width, max_height)
        word = trans_word.getWord()
        word = self.unicodize(word)

        try:
            # bliss_word = ...
            self.getTransBlissImg(trans_word, max_width, max_height)
        except IOError:
            raise IOError
        else:
            bliss_word = self.getTransBlissImg(trans_word, max_width, max_height)

        start_x = max_width / 2
        start_y = int(max_height * 0.75)
        sub_size = self.getSubtitleSize()
        space = self.getMinSpace() * 2

        text_word = self.getWordImg(word.upper(), font_size=sub_size)
        text_word = self.trimHorizontal(text_word)

        text_width = text_word.size[0]
        bliss_width = bliss_word.size[0]
        bliss_height = bliss_word.size[1]

        start_bliss_word_x = start_x - (bliss_width / 2)
        start_bliss_word_y = start_y - bliss_height + space  # above origin pt
        start_text_word_x = start_x - (text_width / 2)
        start_text_word_y = start_y  # below origin pt

        bg.paste(bliss_word, (start_bliss_word_x, start_bliss_word_y))

        if subs:
            sketch = ImageDraw.Draw(bg)
            sketch.text((start_text_word_x, start_text_word_y),
                        word.upper(),
                        font=ImageFont.truetype(font=self.font_path, size=sub_size),
                        fill="black")

        return self.trimHorizontal(bg)

    def getIndicatorBlissImg(self, indicator, max_width, max_height):
        """
        Returns the Blissymbol image corresponding to the
        given Blissymbol indicator string.

        :param indicator: str, Blissymbol indicator to get image of
        :return: Image, input indicator Blissymbol image
        """
        indicator = indicator.replace(" ", "_(")
        indicator += ")"
        return self.getBlissImg(indicator, max_width, max_height)

    def getPluralImg(self, img):
        """
        Returns the given Blissymbol image with the plural
        Blissymbol at the end.

        :param img: Image, Blissymbol image to pluralize
        :return: Image, input image pluralized
        """
        #plural = self.getBlissImg("indicator plural", img.size[0], img.size[1])
        plural = self.getIndicatorBlissImg("indicator plural", img.size[0], img.size[1])
        max_width = img.size[0] + plural.size[0]
        max_height = self.image_heights

        bg = self.makeBlankImg(max_width, max_height)
        space = self.getMinSpace()*2
        start_y = int(max_height * 0.75)
        start_plural_x = bg.size[0] - plural.size[0] #start_x - (plural_width / 2)
        start_plural_y = start_y - plural.size[1] + space  # above origin pt

        bg.paste(img, (0, 0))
        bg.paste(plural, (start_plural_x, start_plural_y))
        return bg

    def trim(self, img):
        """
        Trims the input image's whitespace.

        :param img: Image, image to be trimmed
        :return: Image, trimmed image

        Taken from http://stackoverflow.com/questions/10615901/trim-whitespace-using-pil/29192070.
        """
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
        diff = ImageChops.difference(img, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()

        if bbox:
            return img.crop(bbox)
        else:
            return img

    def trimHorizontal(self, img):
        """
        Trims the input image's whitespace only
        in the x-dimension.

        :param img: Image, image to be trimmed
        :return: Image, trimmed image

        Adapted from http://stackoverflow.com/questions/10615901/trim-whitespace-using-pil/29192070.
        """
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
        diff = ImageChops.difference(img, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()

        if bbox:
            bbox = (bbox[0], 0, bbox[2], img.height)
            return img.crop(bbox)
        else:
            return img

    def incLine(self, line_no, inc=DEFAULT_FONT_SIZE * 3):
        """
        Returns current line_no multiplied by inc to get the
        y-coordinate for this line in pixels.

        :param line_no: int, the current line number
        :param inc: int, factor to multiply line_no by
        :return: int, y-coordinate for this line (in px)
        """
        return line_no * inc

    def getSubtitleSize(self):
        """
        Returns a font size suitable as a subtitle for this
        BlissTranslator's default font_size.

        :return: int, subtitle font size
        """
        return int(self.font_size * 0.5)

    def getSpaceSize(self):
        """
        Returns an appropriate space size relative to this
        BT's font_size in pixels.

        :return: int, space size (in pixels)
        """
        return int(self.font_size * 0.75)

    def getMinSpace(self):
        """
        Returns the minimum spacing between characters
        in pixels.

        Useful for standardizing punctuation spacing.

        :return: int, minimum space size (in pixels)
        """
        return 2

    def displayImages(self, pages):
        """
        Displays each image in pages.
        ~
        Useful for displaying multiple images when debugging.

        :param pages: List[Image], images to display
        :return: None
        """
        for page in pages:
            page.show()

    def saveImage(self, img):
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

    def saveImages(self, imgs):
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
        :return: None
        """
        filenames = []

        for img in imgs:
            filename = self.saveImage(img)
            filenames.append(filename)

        return filenames

    def deleteImage(self, filename):
        """
        Deletes image with given filename.

        :param filename: str, image filename to delete
        :return: None
        """
        #filename = self.lex_parser.IMG_PATH + filename
        os.remove(filename)

    def deleteImages(self, imgs):
        """
        Deletes images with filenames specified in imgs list.

        :param imgs: List[str], image filenames to delete
        :return: None
        """
        for img in imgs:
            self.deleteImage(img)

    def makeTitlePage(self, pdf, title):
        """
        Returns the given PDF with a title page added to it.

        :param pdf: FPDF, pdf to add title page to
        :param title: str, title name
        :return: Image, title page
        """
        pdf.set_title(title)
        pdf.set_font(family=self.font_fam, size=self.font_size)
        pdf.add_page()
        pdf.write(int(pdf.h/2), txt=title)
        return pdf

    def createTitlePage(self, title, x, y):
        """
        Returns a title page of given dimensions x and y with the given
        title.
        :param title: str, title name
        :param x: int, x-dimension of output title page
        :param y: int, y-dimension of output title page
        :return: Image, title page
        """
        img = self.makeBlankImg(x, y)
        title_img = self.getWordImg(title, self.font_size)

        img_x = x/2 - title_img.size[0]/2
        img_y = y/3

        img.paste(title_img, (img_x, img_y))
        return img

    def getPageFilename(self, page_num):
        return "num" + str(page_num) + ".png"

    def makePageNum(self, page_num):
        """
        Draws and returns an image for a page number.
        ~
        Used for adding page numbers to bottom of PDFs.

        :param page_num: int, number of page
        :return: Image, page_num as a number image
        """
        number = self.getWordImg(str(page_num), self.font_size)
        number = self.trim(number)
        num_fn = self.getPageFilename(page_num)
        number.save(num_fn)
        return number

    def savePdf(self, filename, pages, margins=0):
        """
        Pastes each image file linked to in pages to a PDF.
        ~
        Saves PDF under given filename in this directory.

        Adapted from:
        https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images

        :param filename: str, filename for output PDF
        :param pages: List[str], image filenames to paste in PDF
        :param margins: int, space in margins (in pixels)
        :param delete: bool, whether to delete image files
        :return: None
        """
        pdf = self.getPdf(pages, margins)
        pdf.output(self.PATH + "/bliss pdfs/" + filename + ".pdf", "F")

    def getPdf(self, filenames, margins=0):
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

            if len(filenames) > 2 and idx > 0 and self.page_nums:
                #number = self.getWordImg(str(idx), self.font_size)
                #number = self.trim(number)
                #num_fn = "num" + str(idx) + ".png"
                #number.save(num_fn)
                number = self.makePageNum(idx)
                num_fn = self.getPageFilename(idx)
                x = new_w / 2 - number.size[0]
                y = new_h - (margins / 2) - number.size[1]
                pdf.image(num_fn, x=x, y=y)
                os.remove(num_fn)

            self.deleteImage(filename)  # deletes images once in PDF
            idx += 1

        return pdf

    def deletePdf(self, filename):
        """
        Deletes PDF with given filename from bliss pdfs folder.

        :param filename: str, filename with .pdf extension
        :return: None
        """
        os.remove(self.PATH + "/bliss pdfs/" + filename)


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
                text = text.decode("utf-8")
        return text

    def deUnicodize(self, text):
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

    def cleanPhrase(self, phrase):
        """
        Cleans the given phrase for tokenizing by adding
        whitespace around all punctuation characters.
        ~
        Allows for tokenizing words adjacent to punctuation.

        :param phrase: str, phrase to clean
        :return: str, cleaned phrase
        """
        for punct in self.MID_PUNCT:
            phrase = phrase.replace(punct, " "+punct+" ")
        return phrase

    def getWordTag(self, trans_word):
        """
        Returns the given TranslationWord's part-of-speech tag.

        :param trans_word: TranslationWord, word to tag
        :return: str, given word's pos tag
        """
        if self.language != "English":
            tag = self.getMultilingualTag(trans_word)

            if tag is not None and tag != "NN":
                # sets trans_word's tag to synset tag if
                # it's a better guess than tokenizer
                trans_word.setPos(tag)

        return trans_word.getPos()

    def getTokenPhrase(self, phrase):
        """
        Returns a list of word tokens in phrase.

        :param phrase: str, text with >=1 words
        :return: List[str], list of word tokens
        """
        return self.TOKENIZER.tokenize(phrase) #[word for word in word_tokenize(phrase, language=self.language.lower())]

    def getTokenPhrases(self, phrases):
        """
        Returns a list of word tokens in phrases,
        with a newline in between each phrase.

        :param phrases: List[str], phrases to tokenize
        :return: List[str], list of word tokens
        """
        token_phrases = []
        for phrase in phrases:
            token_phrases.extend(self.getTokenPhrase(phrase))
            token_phrases.append("\n")
        return token_phrases

    def tokensToTags(self, token_phrase):
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

    def abbreviateTag(self, tag):
        """
        Given a full tag name, returns a tag abbreviation
        from "a", "v", "n", "r", "s",

        e.g. abbreviateTag("RB") -> "r"

        :param tag: str, full tag name from POS_UNABBREVS
        :return: str, 1-character tag abbreviation
        """
        tag = tag[:2]
        if tag in self.POS_ABBREVS:
            return self.POS_ABBREVS[tag]
        else:
            return 'n'

    def unabbreviateTag(self, tag):
        """
        Given a tag abbreviation from "a", "v", "n", "r", "s",
        returns the full tag name.

        e.g. unabbreviateTag("r") -> "RB"

        :param tag: str, 1-character tag abbreviation
        :return: str, full tag name from POS_UNABBREVS
        """
        assert tag in self.POS_UNABBREVS
        return self.POS_UNABBREVS[tag]

    def isNoun(self, trans_word):
        """
        Returns True if word is a noun, False otherwise.

        :param trans_word: TranslationWord, word to test whether a noun
        :return: bool, whether given word is a noun
        """
        pos = trans_word.getPos()
        return pos[0:2] == "NN"

    def isPluralNoun(self, trans_word):
        """
        Returns True if word is a plural noun, False otherwise.

        :param trans_word: TranslationWord, word to test whether a plural noun
        :return: bool, whether given word is a plural noun
        """
        return trans_word.getPos() == "NNS"

    def isProperNoun(self, trans_word):
        """
        Returns True if word is a proper noun, False otherwise.

        :param trans_word: TranslationWord, word to test whether a proper noun
        :return: bool, whether given word is a proper noun
        """
        return trans_word.getPos() == "NNP"

    def isVerb(self, trans_word):
        """
        Returns True if word is a verb, False otherwise.

        :param trans_word: TranslationWord, word to test whether a verb
        :return: bool, whether given word is a verb
        """
        pos = trans_word.getPos()
        return pos[0:2] == "VB"

    def isAdj(self, trans_word):
        """
        Returns True if word is an adjective, False otherwise.

        :param trans_word: TranslationWord, word to test whether an adjective
        :return: bool, whether given word is an adjective
        """
        pos = trans_word.getPos()
        return pos[0:2] == "JJ"

    def isAdv(self, trans_word):
        """
        Returns True if word is an adverb, False otherwise.

        :param trans_word: TranslationWord, word to test whether an adverb
        :return: bool, whether given word is an adverb
        """
        pos = trans_word.getPos()
        return pos[0:2] == "RB"

    def isPunctuation(self, word):
        """
        Returns True if the input is a punctuation mark.

        :param word: str, word to see if punctuation
        :return: bool, whether word is punctuation
        """
        return word in self.PUNCTUATION

    def isStartingPunct(self, word):
        """
        Returns True if the input is starting punctuation.

        :param word: str, word to see if starting punctuation
        :return: bool, whether word is starting punctuation
        """
        return word in self.STARTING_PUNCT

    def isEndingPunct(self, word):
        """
        Returns True if the input is ending punctuation.

        :param word: str, word to see if ending punctuation
        :return: bool, whether word is ending punctuation
        """
        return word in self.ENDING_PUNCT

    def isNewline(self, word):
        """
        Returns True if the input is a newline.

        :param word: str, word to see if newline
        :return: bool, whether word is newline
        """
        return word == "\n"

    def isChosenPOS(self, pos):
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

    def getSingular(self, noun):
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

    def getInfinitive(self, verb):
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

    def getPredicative(self, adj):
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

    def inBlissDict(self, word):
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

    def inEngBlissDict(self, word):
        """
        Returns True if word in eng_bliss_dict,
        False otherwise.

        :param word: str, word to check eng_bliss_dict membership
        :return: bool, whether word is in eng_bliss_dict
        """
        return word in self.eng_bliss_dict
        #try:
        #    self.eng_bliss_dict[word]
        #except KeyError:
        #    return False
        #else:
        #    return True

    def inBlissLexicon(self, word):
        """
        Returns True if word in bliss_lexicon,
        False otherwise.

        :param word: str, word to check bliss_lexicon membership
        :return: bool, whether word is in bliss_lexicon
        """
        try:
            self.bliss_lexicon[word]
        except KeyError:
            return False
        else:
            return True

    def isBlissWord(self, word):
        """
        Returns True if given word is a valid Blissymbol,
        i.e., if it exists in the Bliss dictionary.

        :param word: str, word to check if valid Blissymbol
        :return: bool, whether given word is valid Blissymbol
        """
        try:
            self.bliss_to_uni[word]
        except KeyError:
            return False
        else:
            return True

    def lookupBlissDict(self, word):
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

    def lookupEngBlissDict(self, word):
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

    def lookupBlissLexicon(self, word):
        """
        Returns English word's corresponding Blissymbols
        from this BlissTranslator's bliss_lexicon.
        ~
        If word is not in eng_bliss_dict, returns None.

        :param word: str, word to lookup in eng_bliss_dict
        :return: List[Blissymbol], word's blissymbols in bliss_lexicon
        """
        try:
            return self.bliss_lexicon[word]
        except KeyError:
            return

    def lookupBlissnet(self, uni):
        """
        Returns this unicode's corresponding synsets
        from this BlissTranslator's blissnet.
        ~
        If unicode is not in blissnet, returns None.

        :param uni: str, Blissymbol unicode to lookup in blissnet
        :return: List[Synset], synsets corresponding to given unicode
        """
        try:
            return blissnet[uni]
        except KeyError:
            return

    def inWordNet(self, word):
        """
        Returns True if word in WordNet,
        False otherwise.

        :param word: str, word to check WordNet membership
        :return: bool, whether word is in WordNet
        """
        return word in self.all_lemma_names

    def isValidWord(self, word):
        """
        Returns True if word is a valid word in this
        BlissTranslator's native language, False otherwise.

        :param word: str, word to check if valid
        :return: bool, whether word is valid
        """
        return self.inBlissDict(word) or self.inWordNet(word)

    def getLexeme(self, word, pos=None):
        """
        Retrieves the given word's lexeme,
        i.e., the word in dictionary entry form.

        e.g. getLexeme(ran) -> "run"
             getLexeme(puppies) -> "puppy"

        Note: if a lexeme for the given word cannot
        be found, this method returns the input.

        :param word: str, word to convert to lexeme
        :return: str, lexeme of input word
        """
        if self.inBlissDict(word):
            # check if word in official Blissymbols dict
            return word

        elif self.inBlissDict(word.title()):
            return word.title()

        elif self.language == "Polish":
            # check if word in Polish inflectional dict
            try:
                self.polish_lexicon[word]
            except KeyError:
                return word
            else:
                return self.polish_lexicon[word]

        elif self.language == "French":
            # check if word in French inflectional dict
            try:
                self.french_lexicon[word]
            except KeyError:
                return word
            else:
                return self.french_lexicon[word]

        else:
            # otherwise, lemmatize word based on
            # best guess for its pos
            if pos is not None:
                short_pos = pos[:2]
                if pos == "NNS":
                    return self.getSingular(word)
                elif short_pos == "VB":
                    return self.getInfinitive(word)
                elif short_pos == "NN" and self.isValidWord(self.getInfinitive(word)):
                    return self.getInfinitive(word)
                elif short_pos == "JJ" or short_pos == "RB":
                    return self.getPredicative(word)
                else:
                    return word
            else:
                if self.isValidWord(self.getSingular(word)):
                    return self.getSingular(word)
                elif self.isValidWord(self.getInfinitive(word)):
                    return self.getInfinitive(word)
                elif self.isValidWord(self.getPredicative(word)):
                    return self.getPredicative(word)
                else:
                    #print(self.all_lemma_names)
                    return word

    def isTranslatable(self, trans_word):
        """
        Returns True if trans_word's lexeme or synonym(s)
        can be translated to Blissymbols, False otherwise.

        :param trans_word: TranslationWord, word to test whether translatable
        :return: bool, whether given trans_word is translatable
        """
        lexeme = trans_word.getLexeme()
        # check if this word's lexeme or synonyms are translatable
        if self.inBlissDict(lexeme):
            return True
        elif self.isSynonymTranslatable(trans_word):
            return True
        # if neither, word is untranslatable
        return False

    def isSynonymTranslatable(self, trans_word):
        """
        Given a TranslationWord, returns True if any of its synonyms
        are translatable.

        :param trans_word: TranslationWord, word to generate synonyms
        :return: bool, whether trans_word synonyms are translatable
        """
        synonyms = self.translateUntranslatable(trans_word)

        if synonyms != []:
            trans_word.addSynsetsLemmas(synonyms)
            return True

        return False

    def shouldBeTranslated(self, trans_word):
        """
        Returns True if given TranslationWord should be translated
        (according to this BlissTranslator's language
        preferences), False otherwise.

        :param trans_word: TranslationWord, word whether to translate
        :return: bool, whether this word should be translated
        """
        if trans_word.hasBlissymbol():
            return True
        elif self.isChosenPOS(trans_word.getPos()):
            return self.isTranslatable(trans_word)
        else:
            return False
        #return trans_word.hasBlissymbol() or \
        #       self.isChosenPOS(trans_word.getPos()) and \
        #       self.isTranslatable(trans_word)
        #       #and not self.isPunctuation(trans_word)

    def translateNow(self, trans_word):
        """
        Returns True if words with trans_word's lexeme should be
        translated now, False if later/never.

        :param trans_word: TranslationWord, word to test
            whether to translate now
        :return: bool, whether to translate given lexeme now
        """
        return self.fast_translate or self.isSeen(trans_word.getLexeme())

    '''
    def bestWordChoice(self, word, pos=None):
        """
        Determines best guess for correct Bliss translation of given word.
        Returns an integer representing the index of best guess in word's
        list of defns.
        ~
        Returns 0 if no best definition found.

        :param word: str, word to determine best translation of
        :param pos: str, optional parameter for pos of input word
        :return: int, index of best translation of given word
        """
        bliss_words = self.bliss_dict[word]
        if pos is None:
            pos = self.getWordTag(self.getLexeme(word))

        word_idx = 0

        for bliss_word in bliss_words:
            parts_of_speech = bliss_word.getPartsOfSpeech()
            for bliss_pos in parts_of_speech:
                if bliss_pos == pos:
                    return word_idx

        return word_idx
    '''

    def synsetsSimilarity(self, synsets):
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
            first = synsets[idx-1]
            other = synsets[idx]
            sim = self.synsetSimilarity(first,other)
            similarities.append(sim)

        return similarities

    def synsetSimilarity(self, synset1, synset2):
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
        word1 = synset1.lemma_names()[0]
        word2 = synset2.lemma_names()[0]
        #print "\t" + word1 + " vs " + word2 + ":\t" + str(sim)
        return sim

    def lookupWordSynsets(self, word, pos, lang="English"):
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
        pos = self.abbreviateTag(pos)

        if lang not in self.LANG_CODES:
            try:
                self.loadMultiLingualLemmas(lang)
            except Exception:
                #print("The language " + lang + " is not supported for adding lemmas.")
                #print "supported languages: ", self.WORDNET_LANGS
                #raise bliss_exceptions.WordNetError("The language " + lang + " is not supported.")
                return []

        try:
            lang_code = self.LANG_CODES[lang]
            synsets = wordnet.synsets(word, pos, lang=lang_code)
        except Exception:
            #print("The language " + lang + " is not supported by synsets.")
            #print "supported languages: ", self.WORDNET_LANGS
            #raise bliss_exceptions.WordNetError("The language " + lang + " is not supported.")
            return []
            #lang_code = self.LANG_CODES[lang]
            #synsets = wordnet.synsets(word, pos, lang=lang_code)
        else:
            if len(synsets) == 0:
                synsets = wordnet.synsets(word, lang=lang_code)
            return synsets

    def lookupBlissymbolSynsets(self, blissymbol):
        """
        Returns a list of Wordnet Synsets corresponding to the
        given Blissymbol.

        :param blissymbol: Blissymbol, blissymbol to lookup synset for
        :return: List[Synset], synsets corresponding to given blissymbol
        """
        if blissymbol.hasUnicode():
            uni = blissymbol.getUnicode()
            synsets = self.lookupBlissnet(uni)
            if synsets is not None:
                return synsets
        return []

    def findLangCode(self, language):
        """
        Returns the abbreviated 3-character language code for
        the given langauge.

        :param language: str, language name
        :return: str, 3-character language code
        """
        return self.LANG_CODES[language]

    def lookupTWordSynsets(self, trans_word, use_pos=True, eng=False):
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
            word = trans_word.getEngLexeme()
            lang = self.LANG_CODES["English"]
        else:
            word = trans_word.getLexeme() #trans_word.getWord()
            lang = self.lang_code

        if use_pos:
            pos = trans_word.getPos()
            pos = self.abbreviateTag(pos)
            synsets = wordnet.synsets(word, pos, lang=lang)

            if not self.safe_translate:
                synsets += wordnet.synsets(word, lang=lang)
        else:
            synsets = wordnet.synsets(word, lang=lang)

        return synsets

    def getMultilingualTag(self, trans_word):
        """
        Given a non-English TranslationWord, find English synsets
        and derive a word tag.
        ~
        If no English synsets exist, return trans_word and NN tag.

        :param trans_word: TranslationWord, non-English word to tag
        :return: List[tuple(str,str)], word tag
        """
        #if trans_word.getPos() != "NN":
        #    pos = trans_word.getPos()
        #    return pos
        synsets = self.lookupTWordSynsets(trans_word, use_pos=False)

        try:
            synsets[0]
        except IndexError:
            pos = trans_word.getPos()
            return pos
        else:
            pos = synsets[0].pos()
            pos = self.unabbreviateTag(pos)
            return pos

    def getMultilingualLexeme(self, trans_word):
        """
        Given a non-English TranslationWord, find English synsets
        and derive an English lexeme.
        ~
        If no English synsets exist, return trans_word's lexeme.

        :param trans_word: TranslationWord, non-English word
        :return: str, English translation of given word
        """
        synsets = trans_word.getSynsets() #self.lookupTWordSynsets(trans_word, use_pos=False)

        try:
            synsets[0]
        except IndexError:
            return trans_word.getLexeme()
        else:
            synset = synsets[0]
            lexeme = synset.lemma_names()[0]
            return lexeme

    def getSynsetLemmas(self, synset):
        """
        Given a synset, returns a list of its lemma names.

        :param synset: Synset, WordNet synset
        :return: List[str], WordNet lemma names
        """
        return synset.lemma_names(lang=self.lang_code)

    def getSynsetsLemmas(self, synsets):
        """
        Given a list of WordNet synsets, returns a list
        of all of their lemma names.

        :param synsets: List[Synset], synsets
        :return: List[str], lemmas for all synsets
        """
        lemmas = []
        for synset in synsets:
            lemmas.extend(self.getSynsetLemmas(synset))
        return lemmas

    def getWordSynsetsLemmas(self, trans_word):
        """
        Returns all lemma names in all synsets
        associated with given word.

        :param trans_word: TranslationWord, a word to lookup in WordNet
        :return: List[str], all this word's synsets' lemmas
        """
        return self.getSynsetsLemmas(self.lookupTWordSynsets(trans_word))

    def translateSynsetsLemmas(self, synsets):
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
            for lemma in self.getSynsetLemmas(synset):
                if self.inBlissDict(lemma):
                    lemmas.append(lemma)
        return lemmas

    def findSynsetId(self, synset):
        """
        Finds a synset ID for this synset.

        :return: str, a 9-digit Wordnet Synset ID
        """
        try:
            wn_num = synset.offset()
        except AttributeError:
            return
        else:
            pos_code = self.POS_FEATURE_DICT[synset.pos()]
            full_synset = str(pos_code) + str(wn_num).zfill(8)
            return full_synset

    def translateUntranslatable(self, trans_word):
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
        return self.translateSynsetsLemmas(self.lookupTWordSynsets(trans_word))

    def makeTranslationWord(self, word_token, pos, debug=False, language="English"):
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

    def makeBlissymbol(self, img_filename, pos, derivation, translations=None):
        """
        Returns a new Blissymbol with...
            given img_filename as its English image filename (ending in .png)
            given pos as its part-of-speech
            given derivation as its list of Blissymbol derivations

        :param img_filename: str, the image filename for this Blissymbol
        :param pos: str, the given word token's (Penn Treebank) part-of-speech
        :param derivation: str, this Blissymbol's derivation, of the form:
            (d(1) + d(2) + ... + d(n))
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
        #translations["English"].append(img_filename[:-4])
        return Blissymbol(img_filename=img_filename,
                          pos=pos,
                          derivation=derivation,
                          #language=self.language,
                          translations=translations,
                          translator=self)

    def addBlissEntry(self, blissymbol):
        """
        Adds given Blissymbol to this BlissTranslator's bliss_dict.

        :param blissymbol: Blissymbol, entry to add
        :return: None
        """
        translations = blissymbol.getTranslations()
        languages = ["English", self.language]
        idx = 0

        for language in languages:
            defns = translations[language]
            for defn in defns:
                if idx == 0:  # English
                    if self.inEngBlissDict(defn):
                        self.eng_bliss_dict[defn].add(blissymbol)
                    else:
                        self.eng_bliss_dict[defn] = set([blissymbol])
                else:
                    if self.inBlissDict(defn):
                        self.bliss_dict[defn].add(blissymbol)
                    else:
                        self.bliss_dict[defn] = set([blissymbol])
            idx += 1

        self.lex_parser.addBlissEntry(blissymbol)

    def extendBlissEntry(self, blissymbol):
        """
        Refreshes BLISS_LEXICON to reflect this BlissTranslator's
        current eng_bliss_dict.

        :param blissymbol: Blissymbol, blissymbol to extend
        :return: None
        """
        return self.lex_parser.extendBlissEntry(blissymbol)

    def appendBlissEntry(self, blissymbol):
        """
        Modifies BLISS_LEXICON directly by appending
        the given Blissymbol.

        :param blissymbol: Blissymbol, blissymbol to append
        :return: None
        """
        return self.lex_parser.appendBlissEntry(blissymbol)

    def getSynsetDefn(self, synset):
        """
        Returns this Synset's definition.

        :param synset: Synset, a WordNet synset
        :return: str, the given synset's definition
        """
        return synset.definition()

    def getWordAtIndex(self, token_phrase, idx):
        """
        A try-catch block for returning the word
        token in token_phrase at specified idx.
        ~
        If index cannot be reached, this method returns
        the empty string.

        :param token_phrase: List[str], word tokens
        :param idx: int, index to access in token_phrase
        :return: str, word token at specified idx
        """
        try:
            token_phrase[idx]
        except IndexError:
            return ""
        else:
            return token_phrase[idx]

    def removeDuplicates(self, strings):
        """
        Deletes all duplicate items from input list of strings.
        Returns refreshed list.

        :param unicodes: List[str], list to delete duplicates from
        :return: List[str], list without duplicates
        """
        seen = set()
        seen_add = seen.add
        return [string for string in strings if not (string in seen or seen_add(string))]

    # TRANSLATOR
    # ==========
    def translate(self, phrase, title="translation", title_page=False, img_w=816, img_h=1056):
        """
        Translates input phrase to Blissymbols according to this
        BlissTranslator's POS and language preferences.
        ~
        Saves translation to a PDF file in this directory's
        bliss pdfs folder with the given title, or otherwise
        titled after the given phrase's first 20 characters.
        ~
        Default image size is 816x1056px (standard PDF page).

        :param phrase: str, text in BlissTranslator's native language
        :param title: str, desired title for output PDF
        :param title_page: bool, whether to create title page
        :param img_w: int, desired width of PDF images (in pixels)
        :param img_h: int, desired height of PDF images (in pixels)
        :return: None, saves PDF with translation to bliss pdfs folder
        """
        title, phrase = self.unicodize(title), self.unicodize(phrase)
        phrase = self.cleanPhrase(phrase)
        phrases = phrase.split("\n")  # split input by newlines
        token_phrases = self.getTokenPhrases(phrases)
        tagged_list = self.tokensToTags(token_phrases)
        raw_phrase = [word.lower() for word in token_phrases]
        pages = []  # translated images to convert to PDF

        if title_page:
            title_pg = self.createTitlePage(title, img_w, img_h)
            pages.append(title_pg)

        bg = self.makeBlankImg(img_w, img_h)
        indent = self.font_size
        line_no = 0
        idx = 0

        print(self.inBlissDict("juridical"))

        for word in raw_phrase:
            if word in self.WHITESPACE:
                img = self.makeBlankImg(0, 0)
            elif self.isPunctuation(word):
                img = self.getWordImg(word)
            else:
                word_token = token_phrases[idx]
                word_tag = tagged_list[idx]
                trans_word = self.makeTranslationWord(word_token=word,
                                                      pos=word_tag,
                                                      debug=self.translate_all,
                                                      language=self.language)
                #trans_word.initBlissymbol()
                lexeme = trans_word.getLexeme()
                print(trans_word)

                if not self.shouldBeTranslated(trans_word):
                    # if word can't be translated to Blissymbols,
                    # then render text
                    img = self.getWordImg(word_token, self.font_size)

                elif not self.translateNow(trans_word):
                    # if we don't want to translate this word yet,
                    # then render text
                    img = self.getWordImg(word_token, self.font_size)
                    self.addSeen(lexeme)

                else:
                    try:
                        self.getSubbedBlissImg(trans_word, img_w, self.image_heights)
                    except IOError:
                        img = self.getWordImg(word_token, self.font_size)
                    else:
                        if self.isChanged(lexeme) and not self.sub_all:
                            img = self.getSubbedBlissImg(trans_word, img_w, self.image_heights, subs=False)
                        else:
                            # adds subtitles to new words
                            img = self.getSubbedBlissImg(trans_word, img_w, self.image_heights, subs=True)
                            self.addChanged(lexeme)

                        if self.isPluralNoun(trans_word):
                            # affixes plural Blissymbol to plural nouns
                            img = self.getPluralImg(img)

            space = self.getSpaceSize()
            x_inc = indent + self.getWordWidth(img)
            y_inc = self.font_size * 3

            this_word = raw_phrase[idx]
            next_word1 = self.getWordAtIndex(raw_phrase, idx + 1)
            next_word2 = self.getWordAtIndex(raw_phrase, idx + 2)

            # TODO: design a method to handle indentation/linenumbers
            if x_inc > img_w:
                indent = 0
                line_no += 1
            elif self.isEndingPunct(next_word2) or self.isStartingPunct(next_word1):
                if (x_inc + self.getWordWidth(next_word1) + space * 2 + self.getWordWidth(next_word2)) \
                        > img_w:
                    # don't let punctuation trail onto next line alone
                    indent = 0
                    line_no += 1
            elif this_word == "\n":
                indent = self.font_size
                line_no += 1

            if (line_no + 1) * y_inc > img_h:
                # if the next line would go beyond the image,
                # store the current page and create a new one
                pages.insert(0, bg)
                bg = self.makeBlankImg(img_w, img_h)
                line_no = 0

            # TODO: modify paste to work with vector bliss files (for aesthetic resizing)
            bg.paste(img, (indent, self.incLine(line_no, y_inc)))
            indent += self.getWordWidth(img) + space
            idx += 1

        pages.insert(0, bg)
        self.savePdf(title, self.saveImages(pages[::-1]), margins=50)
        self.initSeenChanged()
        self.deleteImages(NEW_BLISSYMBOLS)
        del NEW_BLISSYMBOLS[:]


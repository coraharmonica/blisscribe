"""
BLISSCRIBE:

    A Python module for translating text to Blissymbols.
"""
import os, sys
PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(PATH)
import collections
import nltk
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
from nltk.tag import pos_tag
from nltk.corpus import wordnet
from fpdf import FPDF
from imports import safe_import
safe_import('fonts')
safe_import('punctuation')
safe_import('parts_of_speech')
safe_import('images')
safe_import('lexicon_parser')
safe_import('translation_word')
safe_import('speechart')
safe_import('ordered_set')
safe_import('blisslearn')
from blisslearn import BlissClassifier
from fonts import *
from punctuation import *
from parts_of_speech import *
from images import *
from lexicon_parser import LexiconParser, Blissymbol, NEW_BLISSYMBOLS, BCI_BLISSNET
from translation_word import TranslationWord
from speechart.language_parser import LanguageParser
import speechart.tokenizers as tokenizers
from ordered_set import OrderedSet
# NOTE: deprecating pattern3 until IndentationError patched
# from pattern3 import text
# from pattern3.text import en, es, fr, de, it, nl


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
    Use set_translatables() to set whether to translate nouns,
    verbs, adjectives, and/or other parts of speech.
    ~
    By default, a BlissTranslator will translate nouns, verbs, and adjectives.
    To translate any other parts of speech, use set_translatables().
    ~
    Contains methods for:
        1) selecting which parts of speech to translate
           --> set_translatables()
        2) selecting whether to translate text to Blissymbols
           immediately or gradually
           --> set_fast_translate()
        3) selecting font & font size for output PDF translations
           --> set_font()
        4) selecting whether to subtitle all Blissymbols or only
           new Blissymbols
           --> set_sub_all()
    """
    DEFAULT_LANG = "English"
    WIDTH = 816
    HEIGHT = 1056

    def __init__(self, language=DEFAULT_LANG, font_path=SANS_FONT, font_size=30):
        self.lex_parser = LexiconParser(translator=self)
        self._lang_parser = None
        self._classifier = None

        # Fonts
        self.font_size = font_size
        self.font_path = font_path
        self.font_fam = FONT_PATHS[self.font_path]
        self.font = make_font(self.font_path, self.font_size)
        self.sub_font = make_font(self.font_path, self.subtitle_size())

        # Language
        self.bliss_dicts = {}
        self.lexica = {}
        self.language = "English"
        self.set_language(language)
        self.words_seen = {}
        self.words_changed = {}
        self.init_seen_changed()

    # INITIALIZATIONS
    # ===============
    @property
    def blissnet(self):
        return self.lex_parser.blissnet

    @property
    def blissymbols(self):
        return self.lex_parser.blissymbols

    @property
    def lang_parser(self):
        """
        For Wiktionary lookups on Bliss-unfamiliar words.
        ~
        Initializes this BlissTranslator with a LanguageParser
        if _lang_parser is None, then returns _lang_parser.

        :return: LanguageParser, this BlissTranslator's lang_parser
        """
        if self._lang_parser is None:
            self._lang_parser = LanguageParser(self.language)
        return self._lang_parser

    @property
    def classifier(self):
        """
        For translating uncommon words to Blissymbols.
        ~
        Initializes this BlissTranslator with a BlissClassifier
        if _classifier is None, then returns _classifier.

        :return: BlissClassifier, this BlissTranslator's classifier
        """
        if self._classifier is None:
            self._classifier = BlissClassifier(self)
        return self._classifier

    def add_lexicon(self, lang):
        """
        Initializes a lexicon in this language
        and adds it to lexica.
        ~
        N.B. For now, Blisscribe only supports French and Polish
        external lexica.

        :param lang: str, language to load lemmas for
        :return: None
        """
        if lang == "Polish" or lang == "French":
            lexicon = self.lex_parser.parse_lexicon(lang)
            self.lexica[lang] = lexicon

    def init_bliss_dicts(self):
        """
        Initializes this BlissTranslator's bliss_dicts in
        its native language and in English.
        ~
        N.B. bliss_dicts are initialized empty but will be
             filled with Blissymbols in lex_parser.init_blissymbols.

        :return: None
        """
        self.bliss_dicts.setdefault(self.language, {})
        self.bliss_dicts.setdefault("English", {})
        self.bliss_dicts[self.language] = self.lex_parser.init_bliss_lexicon(self.language)
        if self.language != "English":
            self.bliss_dicts["English"] = self.lex_parser.init_bliss_lexicon("English")
            self.load_multilingual_lemmas(self.lang_code())

    def init_seen_changed(self):
        """
        Initializes this BlissTranslator's words_seen
        as a default dict.

        :return: None
        """
        self.words_seen = collections.defaultdict(bool)
        self.words_changed = collections.defaultdict(bool)

    def init_language(self, language):
        """
        Sets this BlissTranslator's native language
        to the input language.
        ~
        If given language is invalid, does not change this
        BlissTranslator's default language.

        :param language: str, language for this BlissTranslator
        :return: None
        """
        language = language.title()

        if language in self.lex_parser.BLISS_LANGS:
            self.language = language

        if self.language[:3] != "Eng":  # add OMW data to non-English wordnets
            self.load_multilingual_lemmas(self.lang_code())

    def lang_code(self, lang=None):
        return LANG_CODES.get(self.language if lang is None else lang, None)

    @property
    def bliss_unicode(self):
        """
        Returns a blissname-to-unicode dictionary.

        :return: dict, where...
            key (str) - name of a Blissymbol
            val (str) - corresponding unicode
        """
        return self.lex_parser.load_bliss_unicode()

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
        self.init_language(language)
        self.add_lexicon(self.language)
        self.init_bliss_dicts()

    def set_font(self, font_path, font_size):
        """
        Sets this BlissTranslator's default font to an ImageFont
        with a 2-tuple of font_path and font_size.
        ~
        If font_path is invalid, uses BlissTranslator's ROMAN_FONT.

        :param value: 2-tuple, font path and font size
        :return: None
        """
        self.font = make_font(font_path, font_size)

    # BLISS CONVERSIONS
    # -----------------
    def lookup_bliss_unicode(self, **kwargs):
        """
        Returns this unicode ID's corresponding Blissymbol name.

         kwargs:
        :param uni: str, unicode name to lookup
        :param bliss: str, name of blissymbol to lookup

        :return: str, Blissymbol name for uni / unicode for bliss name
        """
        bliss_unicode = self.bliss_unicode
        uni = kwargs.get('uni', None)
        if uni is not None:
            return bliss_unicode.get(uni, None)
        bliss = kwargs.get('bliss', None)
        if bliss is not None:
            uni_bliss = {bliss_unicode[b]: b for b in bliss_unicode}
            return uni_bliss.get(bliss, None)

    # SEEN/CHANGED
    # ------------
    def is_seen(self, word):
        """
        Returns True if this word is part of the
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
        Returns True if this word is part of the
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

    # DATA REFRESHING
    # ---------------
    def refresh_data(self):
        """
        Overwrites the source Wiktionary JSON data with this
        BlissTranslator's lang_parser's wiktionary_entries.

        :return: None
        """
        self.clear_new_blissymbols()
        self.refresh_blissymbols()
        self.lang_parser.refresh_data()

    def refresh_blissymbols(self):
        return

    def clear_new_blissymbols(self):
        """
        Deletes all contents of NEW_BLISSYMBOLS.
        ~
        Refreshes naming cycle for new images.

        :return: None
        """
        del NEW_BLISSYMBOLS[:]

    # IMAGES
    # ------
    def image_heights(self):
        """
        Returns the appropriate height of Bliss-images
        relative to font_size.

        :return: int, height of Bliss-images relative to font
        """
        return self.font_size * 2

    def sub_heights(self):
        """
        Returns the height of subtitles in pixels.

        :return: int, height of subtitles
        """
        return self.sub_font.getsize("ÉÇ")[1]

    def subtitle_size(self):
        """
        Returns a font size suitable as a subtitle for this
        BlissTranslator's default font_size.

        :return: int, subtitle font size
        """
        return int(self.font_size * 0.5)

    def trim(self, *args, **kwargs):
        return trim(*args, **kwargs)

    def blank_image(self, *args, **kwargs):
        return blank_image(*args, **kwargs)

    def above(self, *args, **kwargs):
        return above(*args, **kwargs)

    def beside(self, *args, **kwargs):
        return beside(*args, **kwargs)

    def word_image(self, word, subs=False):
        """
        Returns an Image of this TranslationWord's word.
        ~
        If subs is False, creates word Image from word with
        translator's font_size.  Otherwise, creates word image
        from uppercase word and translator's subtitle_size().
        ~
        Used to draw full-sized text as well as subtitles.

        :param word: str, word to render to Image
        :param subs: bool, whether to subtitle image
        :return: Image, image of input str
        """
        if subs:
            word = word.upper()
        font_path = self.font_path
        font_size = self.subtitle_size() if subs else self.font_size
        height = self.image_heights()
        img = word_image(word, height, font_path=font_path, font_size=font_size)
        return img

    def bliss_image(self, bliss_name, **kwargs):
        """
        Draws and returns a thumbnail Image for the Blissymbol with
        this bliss_name, with width not exceeding max_width.

        :param bliss_name: str, name of a Blissymbol with an image filename

        keyword args:
            :param width: int, maximum width of Image (in pixels)
            :param height: int, maximum height of Image (in pixels)

        :return: Image, image of input str's Blissymbol
        """
        width = kwargs.get('width', None)
        height = kwargs.get('height', None)
        whitebg = kwargs.get('whitebg', False)

        img = Image.open(IMG_PATH + bliss_name + ".png")
        if width is not None or height is not None:
            if width is None:
                width = img.size[0]
            if height is None:
                height = img.size[1]
            img.thumbnail((width, height))
        if whitebg:
            bg = blank_image(img.size[0], img.size[1], opacity=255)
            img = overlay(img, bg)
        return img

    def space_size(self):
        """
        Returns an appropriate space size relative to this
        BT's font_size in pixels.

        :return: int, space size (in pixels)
        """
        return int(self.font_size * 0.75)

    def delete_image(self, filename):
        """
        Deletes image with given filename.

        :param filename: str or Set[str], image filename(s) to delete
        :return: None
        """
        if type(filename) == str:
            os.remove(filename)
        else:
            for img_fn in filename:
                self.delete_image(img_fn)

    def title_page(self, title, x, y):
        """
        Returns a title page of dimensions x and y with this title.

        :param title: str, title name
        :param x: int, x-dimension of output title page
        :param y: int, y-dimension of output title page
        :return: Image, title page
        """
        img = blank_image(x, y)
        title_img = word_image(title, self.image_heights(), font_path=self.font_path, font_size=self.font_size)
        img_x = x // 2 - title_img.size[0] // 2
        img_y = y // 3
        img.paste(title_img, (img_x, img_y))
        return img

    def get_pdf(self, title, pages, margins=50, page_nums=False):
        """
        Pastes each image file linked to in pages to a PDF with this title.
        ~
        Returns PDF file.

        Adapted from:
        https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images

        :param title: str, title for output PDF
        :param pages: List[Image], images to paste to PDF
        :param margins: int, space in margins (in pixels)
        :param page_nums: bool, whether to include numbers on pages
        :return: FPDF, pdf document named title with pages
        """
        filenames = []
        for i in range(len(pages)):
            filename = 'bliss_img' + str(i) + '.png'
            pages[i].save(filename)
            filenames.append(filename)
        width, height = Image.open(filenames[0]).size
        new_w, new_h = width + (margins * 2), height + (margins * 2)

        pdf = FPDF(unit="pt", format=[new_w, new_h])

        for idx in range(len(filenames)):
            filename = filenames[idx]
            pdf.add_page()
            pdf.image(filename, x=margins, y=margins)

            if idx > 1 and page_nums:
                number = trim(word_image(str(idx), self.image_heights(),
                                         font_path=self.font_path, font_size=self.font_size))
                num_filename = str(idx) + ".png"
                number.save(num_filename)
                x = new_w // 2 - number.size[0]
                y = new_h - (margins // 2) - number.size[1]
                pdf.image(num_filename, x=x, y=y)
                os.remove(num_filename)

            os.remove(filename)  # deletes images once in PDF

        pdf.output(PATH + "/out/" + title + ".pdf", "F")
        return pdf

    def delete_pdf(self, filename):
        """
        Deletes PDF with given filename from out folder.

        :param filename: str, filename with .pdf extension
        :return: None
        """
        os.remove(PATH + "/out/" + filename)

    # LANGUAGE SUPPORT
    # ----------------
    @staticmethod
    def wordnet_langs():
        """
        Returns a list of all languages supported by WordNet.
        ~
        N.B. Language list is hardcoded because wordnet.langs() loads slowly.

        :return: Set[str], languages supported by WordNet
        """
        return WORDNET_SUPPORTED_LANGS

    @staticmethod
    def find_lang_code(language):
        """
        Returns the abbreviated 3-character language code for
        this language.  If none exists, returns None.

        :param language: str, language name
        :return: Optional[str], 3-character language code
        """
        try:
            return LANG_CODES[language]
        except KeyError:
            if language in LANG_CODES.values():
                for lang in LANG_CODES:
                    if LANG_CODES[lang] == language:
                        return lang
        return None

    @staticmethod
    def supported_langs():
        """
        Returns a set of the languages currently supported by Blisscribe.

        :return: Set(str), languages supported in Blissymbols and WordNet
        """
        return WORDNET_SUPPORTED_LANGS.intersection({LANG_CODES.get(b, None) for b in BLISS_SUPPORTED_LANGS})
        #supported_langs = self.lex_parser.BLISS_LANGS.intersection(self.wordnet_langs())
        #pattern_langs = text.LANGUAGES
        #supported_langs.update(pattern_langs)
        #return supported_langs

    def load_multilingual_lemmas(self, lang_code):
        """
        Loads a custom tab file for this lang_code's language to WordNet.
        ~
        If no such file can be loaded, raises a ValueError.
        ~
        Used to add non-default OMWs to WordNet.

        :param lang_code: str, language code for language to load lemmas for
        :return: None
        """
        if lang_code is not None:
            tab_file = self.lex_parser.get_tab_file(lang_code)

            if tab_file is not None:
                wordnet.custom_lemmas(tab_file, lang_code)
            #else:
            #    raise ValueError("Blisscribe doesn't support this language yet... oops!")

    # LANGUAGE PROCESSING
    # -------------------
    def underscore(self, word):
        """
        Returns this word with spaces replaced by underscores.

        :param word: str, word with spaces to underscore
        :return: str, word with underscores instead of spaces
        """
        return word.strip().replace(" ", "_")

    def deunderscore(self, word):
        """
        Returns this word with underscores replaced by spaces.

        :param word: str, word with underscores to replace
        :return: str, word with spaces instead of underscores
        """
        return word.replace("_", " ").strip()

    def get_token_phrase(self, phrase):
        """
        Returns a list of word tokens in phrase.

        :param phrase: str, text with >=1 words
        :return: List[str], list of word tokens
        """
        return tokenizers.wordpunct_tokenize(phrase)

    def get_token_phrases(self, text):
        """
        Returns a list of word tokens in text,
        with a newline in between each phrase.

        :param phrases: List[str], phrases to tokenize
        :return: List[str], list of word tokens
        """
        phrases = text.split("\n")  # split text by newlines
        token_phrases = []
        for phrase in phrases:
            token_phrases.extend(self.get_token_phrase(phrase))
            token_phrases.append("\n")
        return token_phrases

    def convert_pos(self, pos):
        """
        Converts parts of speech between Penn Treebank and
        Wiktionary.
        ~
        If pos is in PTB, returns the corresponding Wikt part of speech.
        If pos is in Wikt, returns the corresponding PTB part of speech.
        Otherwise, returns None.

        :param pos: str or Iterable[str], PTB or Wikt part(s) of speech
        :return: str or Iterable[str], converted Wikt or PTB part(s) of speech
        """
        if type(pos) == str:
            if pos in PARTS_OF_SPEECH:
                return POS_WIKT_KEY.get(pos, None)
            elif pos in WIKTIONARY_POS_KEY:
                return WIKTIONARY_POS_KEY.get(pos, None)
            else:
                return None
        else:
            poses = OrderedSet([])
            for p in pos:
                conv = self.convert_pos(p)
                if conv is not None:
                    poses.update(conv)
            return poses.intersections()

    def convert_pos_to_wikt(self, pos):
        """
        Returns this Penn Treebank part of speech converted
        to its Wiktionary part of speech.
        ~
        e.g. convert_wikt_to_pos("NN") -> "Noun"

        :param pos: str or Iterable, Penn Treebank part of speech
        :return: str or List, Wiktionary part(s) of speech
        """
        if type(pos) == str:
            return POS_WIKT_KEY.get(pos, None)
        else:  # assume pos is an iterable
            poses = OrderedSet([])
            for p in pos:
                wikt_pos = self.convert_pos_to_wikt(p)
                if wikt_pos is not None:
                    poses.add(wikt_pos)
            return poses.intersections()

    def convert_wikt_to_pos(self, wikt_pos):
        """
        Returns this Wiktionary part of speech converted
        to its Penn Treebank parts of speech.
        ~
        e.g. convert_wikt_to_pos("Noun") -> ["NN", "NNS"]

        :param wikt_pos: str or Iterable, Wiktionary part(s) of speech
        :return: List[str], Penn Treebank part(s) of speech
        """
        if type(wikt_pos) == str:
            return WIKTIONARY_POS_KEY.get(wikt_pos, None)
        else:  # assume pos is an iterable
            poses = OrderedSet([])
            for pos in wikt_pos:
                p = self.convert_wikt_to_pos(pos)
                if p is not None:
                    poses.update(p)
            return poses.intersections()

    def token_pos(self, token, language):
        """
        Returns the Penn Treebank part of speech for this token.
        ~
        e.g. token_pos("dogs") -> "NNS"

        :param token: str, word token
        :return: str, token's part of speech
        """
        tups = pos_tag([token.lower()], lang=self.find_lang_code(language))
        tup = tups[0]
        pos = tup[1]
        return pos

    def abbreviate_pos(self, pos):
        """
        Returns an abbreviation for this Penn Treebank
        part of speech, pos, from "a", "v", "n", "r", "s".
        ~
        e.g. abbreviate_pos("RB") -> "r"
             abbreviate_pos(["JJ", "JJR", "NN"]) -> ["a", "n"]

        :param pos: str or Iterable, Penn Treebank part(s) of speech
        :return: str or List, 1-character abbreviated part of speech
        """
        if type(pos) == str:
            if self.is_noun(pos):
                return 'n'
            elif self.is_verb(pos):
                return 'v'
            elif self.is_adj(pos):
                return 'a'
            elif self.is_adv(pos):
                return 'r'
            else:
                return
        elif len(pos) != 0:
            poses = OrderedSet([])
            for p in pos:
                abbrev = self.abbreviate_pos(p)
                if abbrev is not None:
                    poses.add(abbrev)
            return poses.intersections()

    def unabbreviate_pos(self, pos):
        """
        Given an abbreviated part of speech from "n", "v", "a", "s", "r",
        returns the corresponding Penn Treebank part of speech.
        ~
        e.g. unabbreviate_pos("r") -> "RB"

        :param pos: str, abbreviated part of speech
        :return: str, Penn Treebank part of speech
        """
        if pos == "n":
            return "NN"
        elif pos == "v":
            return "VB"
        elif pos == "a":
            return "JJ"
        elif pos == "s":
            return "JJS"
        elif pos == "r":
            return "RB"
        else:
            return

    def singularize(self, noun, lang, pos="NNS"):
        """
        Returns the singular form of this noun
        in this BlissTranslator's set language.
        ~
        If noun cannot be singularized for this
        language, this method returns the input.

        :param noun: str, noun to singularize
        :param lang: str, language of adj
        :param pos: str, noun's part of speech
        :return: str, plural noun singularized
        """
        if pos == "NNS":
            return self.lang_parser.find_custom_lemma(noun, lang, 'Noun', 'plural', add_new=True)
        elif pos == "NNPS":
            return self.lang_parser.find_custom_lemma(noun, lang, 'Proper noun', 'plural', add_new=True)

    def infinitive(self, verb, lang, pos):
        """
        Returns the infinitive of this verb
        in this language.
        ~
        If no infinitive can be found in set language,
        returns None.

        :param verb: str, verb
        :param lang: str, language of adj
        :param pos: str, verb's part of speech
        :return: str, lemma of verb
        """
        if pos == "VB":
            return verb
        elif pos == "VBD":
            return self.lang_parser.find_custom_lemma(verb, lang, 'Verb', 'past tense', add_new=True)
        elif pos == "VBG":
            return self.lang_parser.find_custom_lemma(verb, lang, 'Verb', 'present participle', add_new=True)
        elif pos == "VBN":
            return self.lang_parser.find_custom_lemma(verb, lang, 'Verb', 'past participle', add_new=True)
        elif pos == "VBP":
            person1 = self.lang_parser.find_custom_lemma(verb, lang, 'Verb', ['singular present', 'first-person'],
                                                         add_new=True)
            if person1 is not None:
                return person1
            else:
                return self.lang_parser.find_custom_lemma(verb, lang, 'Verb', ['singular present', 'second-person'],
                                                          add_new=True)
        elif pos == "VBZ":
            return self.lang_parser.find_custom_lemma(verb, lang, 'Verb', ['singular present', 'third-person'],
                                                         add_new=True)
        else:
            return

    def predicative(self, adjv, lang, pos):
        """
        Returns the base form of this adjective/adverb
        in this BlissTranslator's language.
        ~
        If no base form can be found in set language,
        this method returns the input.
        ~
        e.g. well, English, JJ  -> good
             belles, French, JJ -> beau

        :param adjv: str, adjective to find predicative form of
        :param lang: str, language of adj
        :param pos: str, adj's part of speech
        :return: str, predicative form of adj
        """
        if pos == "JJ":
            return adjv
        elif pos == "JJR":
            return self.lang_parser.find_custom_lemma(adjv, lang, pos='Adjective', defn_phrase="comparative")
        elif pos == "JJS":
            return self.lang_parser.find_custom_lemma(adjv, lang, pos='Adjective', defn_phrase="superlative")
        elif pos == "RB":
            return self.lang_parser.find_custom_lemma(adjv, lang, pos='Adverb')
        elif pos == "RBR":
            return self.lang_parser.find_custom_lemma(adjv, lang, pos='Adverb', defn_phrase="comparative")
        elif pos == "RBS":
            return self.lang_parser.find_custom_lemma(adjv, lang, pos='Adverb', defn_phrase="superlative")

    def is_noun(self, pos):
        """
        Returns True if pos is a noun, False otherwise.

        :param pos: str or Iterable[str], part(s) of speech to check
        :return: bool, whether pos is a noun
        """
        if type(pos) == str:
            return pos[:2] == "NN"
        else:
            return any(self.is_noun(p) for p in pos)

    def is_plural_noun(self, pos):
        """
        Returns True if pos is a plural noun, False otherwise.

        :param pos: str or Iterable[str], part(s) of speech to check
        :return: bool, whether pos is a plural noun
        """
        if type(pos) == str:
            return pos == "NNS"
        else:
            return any(self.is_plural_noun(p) for p in pos)

    def is_proper_noun(self, pos):
        """
        Returns True if pos is a proper noun, False otherwise.

        :param pos: str or Iterable[str], part(s) of speech to check
        :return: bool, whether pos is a proper noun
        """
        if type(pos) == str:
            return pos == "NNP"
        else:
            return any(self.is_proper_noun(p) for p in pos)

    def is_verb(self, pos):
        """
        Returns True if pos is a verb, False otherwise.

        :param pos: str or Iterable[str], part(s) of speech to check
        :return: bool, whether pos is a verb
        """
        if type(pos) == str:
            return pos[:2] == "VB"
        else:
            return any(self.is_verb(p) for p in pos)

    def is_adj(self, pos):
        """
        Returns True if pos is an adjective, False otherwise.

        :param pos: str or Iterable[str], part(s) of speech to check
        :return: bool, whether pos is an adjective
        """
        if type(pos) == str:
            return pos[:2] == "JJ"
        else:
            return any(self.is_adj(p) for p in pos)

    def is_adv(self, pos):
        """
        Returns True if pos is an adverb, False otherwise.

        :param pos: str or Iterable[str], part(s) of speech to check
        :return: bool, whether pos is an adverb
        """
        if type(pos) == str:
            return pos[:2] == "RB"
        else:
            return any(self.is_adv(p) for p in pos)

    '''
    def get_singular(self, noun):
        """
        Returns the singular form of this noun
        in this BlissTranslator's set language.
        ~
        If noun cannot be singularized for this
        language, this method returns the input.

        :param noun: str, noun to singularize
        :return: str, singularized input
        """
        return self.lang_parser.lemmatize(noun)

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
        Returns the infinitive of this verb
        in this BlissTranslator's set language.
        ~
        If no infinitive can be found in set language,
        this method returns the input.

        :param verb: str, verb
        :return: str, lemma of verb
        """
        return self.lang_parser.lemmatize(verb)

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
        Returns the base form of this adjective
        in this BlissTranslator's set language.
        ~
        If no base form can be found in set language,
        this method returns the input.

        e.g. well   -> good
             belles -> beau

        :param adj: str, adjective
        :return: str, base form of input adj
        """
        return self.lang_parser.lemmatize(adj)

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
    '''

    def is_whitespace(self, word):
        """
        Returns True if the input is whitespace,
        False otherwise.

        :param word: str, word to see if whitespace
        :return: bool, whether word is whitespace
        """
        return word in WHITESPACE

    def is_punctuation(self, word):
        """
        Returns True if the input is a punctuation mark.

        :param word: str, word to see if punctuation
        :return: bool, whether word is punctuation
        """
        return all(char in PUNCTUATION for char in word)

    def is_alpha(self, word):
        return all(char.isalpha() for char in word)

    def is_nonalpha(self, word):
        return all(not char.isalpha() for char in word)

    def is_word(self, word):
        """
        Returns False if the input is punctuation or whitespace,
        True otherwise.

        :param word: str, word to see if punctuation or whitespace
        :return: bool, whether word is punctuation or whitespace
        """
        return not (self.is_whitespace(word) or self.is_punctuation(word)) and len(word) != 0

    def is_bliss_word(self, word):
        """
        Returns True if given word is a valid Blissymbol,
        i.e., if it exists in the Bliss dictionary.

        :param word: str, word to check if valid Blissymbol
        :return: bool, whether given word is valid Blissymbol
        """
        return word in self.lex_parser.bliss_derivations

    def in_bliss_dict(self, word, language):
        """
        Returns True if word in eng_bliss_dict,
        False otherwise.

        :param word: str, word to check eng_bliss_dict membership
        :param language: str, language of Blissymbols dict
        :return: bool, whether word is in eng_bliss_dict
        """
        bliss_dict = self.bliss_dict(language)
        return word in bliss_dict

    def in_blissnet(self, **kwargs):
        """
        Returns True if synset, bci_num, or blissymbol's bci_num
        is in this BlissTranslator's blissnet, False otherwise.

        :return: bool, whether word is in eng_bliss_dict
        """
        synset = kwargs.get('synset', None)
        if synset is not None:
            return any(synset.name() in v for v in self.blissnet.values())
        bci_num = kwargs.get('bci_num', None)
        if bci_num is None:
            blissymbol = kwargs.get('blissymbol', None)
            if blissymbol is not None:
                bci_num = blissymbol.bci_num
            else:
                return False
        return bci_num in self.blissnet

    def lookup_blissnet(self, **kwargs):
        """
        Returns this Blissymbol's corresponding synset strings
        from this BlissTranslator's blissnet.
        ~
        If blissymbol is not in blissnet, returns None.

        :keyword synset: Synset, WordNet Synset to lookup in blissnet
        :keyword bci_num: int, BCI-AV# to lookup in blissnet
        :keyword blissymbol: Blissymbol, symbol to lookup in blissnet
        :return: List[str], synset strings corresponding to given Blissymbol
        """
        synset = kwargs.get("synset", None)
        if synset is not None:
            bliss_num, match = None, 0
            for bci_num in BCI_BLISSNET:
                synsets = BCI_BLISSNET[bci_num]
                if synset.name() in synsets:
                    curr_match = 1/len(synsets)
                    if curr_match > match:
                        bliss_num, match = bci_num, curr_match
            return self.bci_num_to_blissymbol(int(bliss_num)) if bliss_num is not None else None
        else:
            bci_num = kwargs.get("bci_num", None)
            if bci_num is None:
                bci_num = kwargs.get("blissymbol").bci_num
            return BCI_BLISSNET.get(bci_num, None)

    def lookup_bliss_dict(self, word, language):
        """
        Returns the Blissymbols for this word in this language.
        ~
        If word is not in this language's Blissymbols dictionary, returns None.

        :param word: str, word to lookup in bliss_dict
        :param language: str, language of Blissymbols dict
        :return: List[Blissymbol], word's blissymbols in bliss_dict
        """
        bliss_dict = self.bliss_dict(language)
        return bliss_dict.get(word, None)

    def bliss_dict(self, language):
        """
        Returns the Blissymbols dictionary for this language.

        :param language: str, language of desired Blissymbols dict
        :return: dict, where...
            key (str) - words in this language
            val (Set(Blissymbol)) - corresponding Blissymbols with
                translations in language and English
        """
        bliss_dict = self.bliss_dicts.get(language, None)
        if bliss_dict is None:
            bliss_dict = self.lex_parser.init_bliss_lexicon(language)
            self.bliss_dicts.setdefault(language, bliss_dict)
        return bliss_dict

    def detect_language(self, word):
        return self.lang_parser.detect_language(word)

    def common_hypernym(self, synsets):
        """
        Returns a synset which is the most common
        hypernym of these synsets.

        :param synsets: List[Synset]
        :return: Synset
        """
        if len(synsets) != 0:
            hypernyms = OrderedSet([])
            for synset in synsets:
                hypernyms.update(synset.hypernyms())
            if len(hypernyms) != 0:
                return hypernyms.intersections()[0]

    def pos_match(self, pos1, pos2):
        if pos1 is None or pos2 is None:
            return True
        if type(pos1) == str:
            if type(pos2) == str:
                return pos1 == pos2
            else:
                return pos1 in pos2
        else:
            if type(pos2) == str:
                return pos2 in pos1
            else:
                return len(set(pos1).intersection(pos2)) != 0

    @staticmethod
    def remove_parens(word, starts={"(", "["}, ends={")", "]"}):
        """
        Removes parenthetical(s) from this word and
        returns the result.
        ~
        Parenthetical begins at the first open parenthesis.

        e.g. remove_parens("English_(language)") -> "English"

        :param word: str, word to remove parenthetical from
        :param starts: Set[str], starts of parentheticals
        :param ends: Set[str], ends of parentheticals
        :return: str, word without parenthetical phrase
        """
        idx = 0
        num_starts, start_idx = 0, 0

        for char in word:
            if char in starts:
                num_starts += 1
                start_idx = idx
            elif char in ends:
                num_starts -= 1
                if num_starts == 0:
                    if idx+2 < len(word):
                        stripped = word[:start_idx] + word[idx+1:]
                    else:
                        stripped = word[:start_idx]
                    stripped = stripped.strip()
                    stripped = stripped.strip("_")
                    stripped = stripped.rstrip("-")
                    return stripped
            idx += 1

        return word

    def lemmatize(self, word, pos=None, lang="English"):
        """
        Retrieves this word's lemma,
        i.e., the word in dictionary entry form.
        ~
        e.g. lemmatize("ran") -> "run"
             lemmatize("puppies") -> "puppy"
        ~
        N.B. If a lemma for this word cannot
        be found, this method returns the input.

        :param word: str, word to lemmatize
        :param pos: Optional[str/Set], word's part(s) of speech
        :param lang: str, word's native language
        :return: str, word's lemma
        """
        bliss_dict = self.bliss_dict(lang)

        if type(pos) == str:
            pos = {pos}
        elif pos is None:
            pos = set(PARTS_OF_SPEECH)

        def in_bliss_dict(w):
            if w in bliss_dict and any(self.pos_match(pos, b.pos) for b in bliss_dict[w]):
                return w
            else:
                return None

        if self.is_punctuation(word):
            return word

        # check if variations of word are in official Blissymbols dict
        word_entry = in_bliss_dict(word)
        if word_entry is not None:
            return word_entry

        word_entry = in_bliss_dict(word.title())
        if word_entry is not None:
            return word_entry

        word_entry = in_bliss_dict(word.lower())
        if word_entry is not None:
            return word_entry
        else:
            del word_entry

        del bliss_dict
        '''
        if pos is None or self.is_noun(pos):
            singular = self.singularize(word, lang)
            if singular is not None:
                return singular
            else:
                del singular

        if pos is None or self.is_verb(pos):
            infinitive = self.infinitive(word, lang, pos)
            if infinitive is not None:
                return infinitive
            else:
                del infinitive

        if pos is None or any(self.is_noun(p) for p in pos):
            predicative = self.predicative(word, lang)
            if predicative is not None:
                return predicative
            else:
                del predicative
        '''

        if lang[:3] == "Eng":
            pos_abbrev = self.abbreviate_pos(pos)
            if len(pos_abbrev) != 0:
                return tokenizers.lemmatize(word, pos_abbrev[0])

        if lang in self.lexica:
            # check if word in Polish/French inflectional dict
            return self.lemmatize_multilingual(word, lang, pos=pos)
        else:
            if pos is not None:
                wikt_pos = self.convert_pos_to_wikt(pos)
            else:
                wikt_pos = None
            return self.lang_parser.lemmatize(word, lang=lang, pos=wikt_pos, add_new=True)

    def lemmatize_multilingual(self, word, lang, pos=None):
        """
        Returns the lemma corresponding to this word
        in this language's lexicon.
        ~
        If language has no external lexicon, returns None.
        If word is not in lexicon, returns word.
        ~
        N.B. As yet Blisscribe only features 2 external
             lexica, French and Polish.

        :param word: str, multilingual word to lemmatize
        :param lang: str, input word's native language
        :param pos: Optional[str or Set], this word's part(s) of speech
        :return: str, lemma of given word
        """
        lexicon = self.lexica.get(lang, None)

        if lexicon is not None:
            if word in lexicon:
                return lexicon[word]
            entry = lexicon.get(word.title(), None)
            if entry is not None:
                return entry
            if word != word.lower():
                return lexicon.get(word.lower(), None)
            else:
                return word

            try:
                entry = lexicon[word]
            except KeyError:
                try:
                    entry = lexicon[word.lower()]
                except KeyError:
                    try:
                        entry = lexicon[word.title()]
                    except KeyError:
                        return word

            if len(entry) != 0:
                if len(entry) == 1:
                    return entry[0]
                else:
                    poses = self.convert_pos_to_wikt(pos) if pos is not None else None
                    multilemmas = [self.lang_parser.lemmatize_multilingual(lemma, lang, poses,
                                                                           add_new=lemma not in self.words_seen)
                                   for lemma in entry]
                    lemmas = OrderedSet(multilemmas).intersections()
                    if len(lemmas) != 0:
                        entry = lemmas
                    return word if word in entry else entry[0]

        return word

    def translation_word(self, word_token, pos, lang="English"):
        """
        Returns a new TranslationWord with...
            word_token as its word
            pos as its part(s)-of-speech
            language as its language
            this BlissTranslator as its translator

        :param word_token: str, a word token representing the word as found in text
        :param pos: Set(str), this word token's (Penn Treebank) part(s)-of-speech
        :param lang: str, native language of given word token
        :return: TranslationWord, a new TranslationWord with the given fields
        """
        return TranslationWord(word=word_token, pos=pos, translator=self, lang=lang)

    def blissymbol(self, bliss_name, pos, derivation, translations=None, num=0):
        """
        Returns a new Blissymbol with...
            bliss_name as its English lookup name
            pos as its part(s) of speech
            derivation as its list of Blissymbol derivations
            num as its BCI-AV#

        :param bliss_name: str, this Blissymbol's official name
        :param pos: str or Iterable, this Blissymbol's (Penn Treebank) part(s) of speech
        :param derivation: str, this Blissymbol's derivation, of the form:
            "(d(1) + d(2) + ... + d(n))"
            where d(1) to d(n) are derivative bliss names
        :param translations: dict, where...
            key (str) - language of Blissymbol translation
            val (List[str]) - Blissymbol's translations in language
        :param num: int, this Blissymbol's BCI-AV#
        :return: Blissymbol, a new Blissymbol with the this fields
        """
        if translations is not None:
            translations = translations
        else:
            translations = {}
        translations.setdefault(self.language, [])
        translations["English"] = [name for name in bliss_name[:-4].split(",")]
        return Blissymbol(bliss_name=bliss_name,
                          pos=pos,
                          derivation=derivation,
                          translations=translations,
                          translator=self,
                          num=num)

    def word_bliss_name(self, word, language="English"):
        """
        Returns the Blissymbol name associated with
        this word.
        ~
        e.g. word_bliss_name("lapin", "French") -> "rabbit,hare"

        :param word: str, word to get Blissymbol name of
        :param language: str, word's native language
        :return: str, Blissymbol name for this word
        """
        bliss = self.word_to_blissymbol(word, lang=language)
        if bliss is not None:
            return bliss.bliss_name
        else:
            return

    def word_to_blissymbol(self, word, pos=None, lang="English", return_none=True):
        """
        Returns the Blissymbol for this word in this language
        with this part of speech.
        ~
        If this word cannot be translated to a Blissymbol,
        this method returns None, if return_none is True.
        Otherwise, returns the Blissymbol for question_mark.

        :param word: str, word to lookup Blissymbol for
        :param lang: str, word's native language
        :param pos: str or Iterable, word's part of speech
        :return: Optional[Blissymbol], a Blissymbol for this word
        """
        if word is not None:
            blissymbols = self.lookup_bliss_dict(word, lang)

            if pos is not None and blissymbols is not None:
                pos_match = lambda p, b: p in b.pos if type(p) == str else any(s in b.pos for s in pos)
                filtered_bliss = [bliss for bliss in blissymbols if pos_match(pos, bliss)]
                if len(filtered_bliss) != 0:
                    blissymbols = filtered_bliss

            if blissymbols is not None and len(blissymbols) != 0:
                if len(blissymbols) == 1:
                    return list(blissymbols)[0]
                elif len(blissymbols) > 1:
                    nonneutral = None

                    for blissymbol in blissymbols:
                        if not blissymbol.is_neutral():
                            nonneutral = blissymbol
                            continue
                        elif word == blissymbol.bliss_name:
                            return blissymbol
                    else:
                        for blissymbol in blissymbols:
                            translations = blissymbol.get_translation(lang)

                            if word in translations or word in translations:
                                return blissymbol

                        return nonneutral

        if not return_none:
            return self.blissword_to_blissymbol("question_mark")

    def words_to_blissymbol(self, words, lang="English", pos=None):
        """
        Returns the Blissymbol common to all these words.
        ~
        If words have no Blissymbol, returns None.

        :param words: List[str], words to lookup Blissymbol for
        :param lang: str, word's native language
        :param pos: str or Iterable, words' part(s) of speech
        :return: Blissymbol, a Blissymbol corresponding to this word
        """
        blissymbols = OrderedSet([])

        for word in words:
            entry = self.lookup_bliss_dict(word, lang)
            if entry is not None:
                if pos is not None:
                    matches_pos = lambda p, b: (p in b.pos) or (p[:2] in b.pos) if type(p) == str else \
                        any((p_ in b.pos) or (p_[:2] in b.pos) for p_ in p)
                    entry = {bliss for bliss in entry if matches_pos(pos, bliss)}
                blissymbols.update(entry)

        blissymbols = blissymbols.intersections()
        return blissymbols[0] if len(blissymbols) != 0 else None

    def synset_to_blissymbol(self, synset, language):
        """
        Returns the Blissymbol common to all this synset's lemma names.
        ~
        If synset has no Blissymbol, returns None.

        :param synset: Synset, synset to lookup Blissymbol for
        :return: Blissymbol, a Blissymbol for this synset
        """
        lemmas = self.synset_lemmas(synset, eng=False)
        return self.words_to_blissymbol(lemmas, lang=language, pos=self.synset_pos(synset))

    def synsets_to_blissymbol(self, synsets):
        """
        Returns the Blissymbol common to all these synsets.
        ~
        If words have no Blissymbol, returns None.

        :param synsets: List[Synset], synsets to lookup Blissymbol for
        :return: Blissymbol, a Blissymbol for these synsets
        """
        blissymbols = OrderedSet([])

        for synset in synsets:
            blissymbols.update(self.lookup_blissnet(synset=synset))

        if len(blissymbols) != 0:
            return blissymbols.intersections()[0]
        else:
            hypernym = self.common_hypernym(synsets)
            return None if hypernym is None else self.lookup_blissnet(synset=hypernym)

    def blissymbol_to_bci_num(self, blissymbol):
        """
        Returns the BCI-AV# for a Blissymbol with the same
        bliss_name as this blissymbol.  If none exist,
        returns None.

        :param blissymbol: Blissymbol, to find BCI-AV# for
        :return: Optional[int], Blissymbol's BCI-AV# (None if nonexistent)
        """
        if blissymbol.bci_num is None:
            for bs in self.lex_parser.blissymbols:
                if bs.bliss_name == blissymbol.bliss_name:
                    return int(bs.bci_num)

    def bci_num_to_blissymbol(self, bci_num):
        """
        Returns the Blissymbol with this bci_num as its
        BCI-AV#.  If none exists, returns None.

        :param bci_num: int, BCI-AV# corresponding to a Blissymbol
        :return: Optional[Blissymbol], Blissymbol with this bci_num (None if nonexistent)
        """
        for bs in self.lex_parser.blissymbols:
            if bci_num == bs.bci_num:
                return bs

    def blissymbol_to_synsets(self, blissymbol):
        """
        Return a list of PWN Synsets for this Blissymbol.

        :param blissymbol: Blissymbol, to find Synsets for
        :return: List[Synset], Synsets for blissymbol
        """
        synsets = OrderedSet([])
        bliss_translations = blissymbol.translations

        if len(bliss_translations) > 1:
            for language in bliss_translations:
                translations = bliss_translations[language]
                lang_code = self.find_lang_code(language)
                if len(translations) != 0:
                    word_synsets = self.words_synsets(translations, lang_code=lang_code, pos=blissymbol.get_pos())
                    synsets.update(word_synsets)

        return synsets.intersections()

    def blissymbols_to_synsets(self, blissymbols):
        """
        Return a list of PWN Synsets for these Blissymbols.

        :param blissymbols: List[Blissymbol], to find Synsets for
        :return: List[Synset], Synsets for blissymbols
        """
        synsets = OrderedSet([])

        for blissymbol in blissymbols:
            synsets.update(self.blissymbol_to_synsets(blissymbol))

        return synsets.intersections()

    def blissword_to_blissymbol(self, blissword):
        """
        Returns the Blissymbol for to this (English) blissword.
        ~
        If blissword has no Blissymbol, returns None.

        :param blissword: str, comma-separated English word(s) for a Blissymbol
        :return: Blissymbol, Blissymbol for this blissword
        """
        blissword = self.underscore(blissword)
        bliss_dict = self.bliss_dict(self.language)

        for entry in bliss_dict:
            blissymbols = bliss_dict[entry]
            for blissymbol in blissymbols:
                if blissymbol.bliss_name == blissword:
                    return blissymbol

    def add_bliss_entry(self, blissymbol):
        """
        Adds this Blissymbol to this BlissTranslator's
        Blissymbol dictionaries.

        :param blissymbol: Blissymbol, entry to add
        :return: None
        """
        languages = {self.language, "English"}.union(self.bliss_dicts.keys())
        all_translations = blissymbol.translations
        for language in languages:
            translations = all_translations.get(language, None)
            if translations is not None:
                bliss_dict = self.bliss_dict(language)
                for translation in translations:
                    bliss_dict.setdefault(translation, set())
                    bliss_dict[translation].add(blissymbol)
        '''
        for language in self.bliss_dicts:
            bliss_dict = self.bliss_dicts[language]
            translations = blissymbol.get_translation(language)
            for translation in translations:
                bliss_dict.setdefault(translation, set())
                bliss_dict[translation].add(blissymbol)
        '''

    @staticmethod
    def ordered_set(items):
        return OrderedSet(items)

    @staticmethod
    def remove_duplicates(items):
        """
        Removes all duplicates from items list and returns new list.

        :param unicodes: List[X], list to delete duplicates from
        :return: List[X], list without duplicates
        """
        return OrderedSet(items).items()

    # SYNSETS
    # -------
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

    def multilingual_word_synsets(self, word, pos=None, lang_code="eng"):
        """
        Returns a list of Wordnet Synsets corresponding to this
        word, part of speech (pos), and language.
        ~
        If lookup fails with this pos, returns this
        word's Wordnet synsets for all parts of speech
        (assuming an incorrect pos label).

        :param word: str, word to lookup synset for
        :param pos: str, part-of-speech for given word
        :param lang_code: str, language code for word
        :return: List[Synset], synsets corresponding to
            given word, pos, and lang
        """
        if lang_code not in WORDNET_SUPPORTED_LANGS:
            try:
                self.load_multilingual_lemmas(self.lang_code())
            except ValueError:
                return []
            else:
                WORDNET_SUPPORTED_LANGS.add(lang_code)
                return self.word_synsets(word, pos, lang_code)
        else:
            return []

    def word_synsets(self, word, pos=None, lang_code="eng"):
        """
        Returns a list of Wordnet Synsets corresponding to this
        word, part of speech (pos), and language.
        ~
        If lookup fails with this pos, returns this
        word's Wordnet synsets for all parts of speech
        (assuming an incorrect pos label).

        :param word: str, word to lookup synset for
        :param pos: str or Iterable, word's part(s) of speech
        :param lang_code: str, word's language
        :return: List[Synset], synsets under this word, pos, and lang
        """
        pos_abbrev = self.abbreviate_pos(pos) if pos is not None else None

        try:
            synsets = wordnet.synsets(word, pos_abbrev, lang=lang_code)
        except Exception:
            return self.multilingual_word_synsets(word, pos, lang_code)

        if len(synsets) == 0:
            if lang_code != "eng":
                synsets = wordnet.synsets(word, lang=lang_code)

        return synsets

    def words_synsets(self, words, pos=None, lang_code="eng"):
        """
        Returns a list of Wordnet Synsets corresponding to this
        word, part of speech (pos), and language.
        ~
        If lookup fails with this pos, returns this
        word's Wordnet synsets for all parts of speech.

        :param words: List[str], words to lookup synsets for
        :param pos: str, part-of-speech for given word
        :param lang_code: str, language of word
        :return: List[Synset], synsets for words, pos, and language
        """
        if len(words) != 0:
            synsets = OrderedSet([])

            for word in words:
                word_synsets = self.word_synsets(word, pos=pos, lang_code=lang_code)
                if len(word_synsets) != 0:
                    synsets.update(word_synsets)

            return synsets.intersections()
        else:
            return []

    def str_synset(self, s):
        """
        Returns a Wordnet Synset for this string s, where s
        follows the regex "\w+\.[nvas]\.d{2}", i.e.,
        "[word].[pos code].[sense number]".

        :param s: str, string for Wordnet Synset
        :return: Synset, synset for this s
        """
        return wordnet.synset(s)

    def strs_synsets(self, strs):
        """
        Returns a Wordnet Synset for this string s, where s
        follows the regex "\w+\.[nvas]\.d{2}", or
        "[word].[pos code].[sense number]".

        :param strs: List[str], strings for Wordnet Synsets
        :return: List[Synset], synsets for strs
        """
        return [self.str_synset(s) for s in strs]

    def synset_pos(self, synset):
        """
        Returns this synset's Penn Treebank part of speech.

        :param synset: Synset, WordNet synset
        :return: str, synset's Penn Treebank part of speech
        """
        pos = synset.pos()
        return self.unabbreviate_pos(pos)

    def synset_lemmas(self, synset, eng=False):
        """
        Returns a list of this synset's lemma names.

        :param synset: Synset, WordNet synset
        :return: List[str], WordNet lemma names
        """
        lang_code = "eng" if eng else self.lang_code()
        return [self.deunderscore(ln) for ln in synset.lemma_names(lang=lang_code)]

    def synsets_lemmas(self, synsets, eng=False):
        """
        Returns a list of all these synsets' lemmas.

        :param synsets: List[Synset], synsets
        :return: List[str], lemmas for all synsets
        """
        lemmas = OrderedSet([])
        for synset in synsets:
            lemmas.update(self.synset_lemmas(synset, eng=eng))
        return lemmas.items()

    def translatable_synsets(self, synsets):
        """
        Returns a list of all these synsets with any lemmas
        appearing in bliss_dict.

        :param synsets: List[Synset], a root word and its synonyms
        :return: List[Synset], synsets in bliss_dict
        """
        translatable_synsets = []

        for synset in synsets:
            if any([self.in_bliss_dict(lemma, self.language) for lemma in self.synset_lemmas(synset)]):
                translatable_synsets.append(synset)

        return translatable_synsets

    def synset_definition(self, synset):
        """
        Returns this Synset's definition.

        :param synset: Synset, a WordNet synset
        :return: str, this synset's definition
        """
        return synset.definition()

    def id_synset(self, id):
        """
        Returns the WordNet Synset for this 9-digit synset id.

        :param id: int, 9-digit WordNet Synset ID
        :return: Synset, synset for this id
        """
        pos_code = id[0]
        offset = id[1:]
        pos = POS_CODE_DICT[pos_code]
        return wordnet.synset_from_pos_and_offset(pos, offset)

    def synset_id(self, synset):
        """
        Returns the 9-digit synset ID for this Synset,
        consisting of its part-of-speech number followed by
        its sense-key.

        :param synset: Synset, synset to find ID for
        :return: int, a 9-digit WordNet Synset ID
        """
        if synset is not None:
            pos_code = POS_FEATURE_DICT[synset.pos()]
            full_synset = str(pos_code) + self.synset_sensekey(synset)
            return int(full_synset)
        else:
            return

    def synset_sensekey(self, synset):
        """
        Returns the 8-digit sense-key string for this Synset.

        :param synset: Synset, synset to find ID for
        :return: str, a 8-digit WordNet Synset sense-key
        """
        if synset is not None:
            return str(synset.offset()).zfill(8)
        else:
            return

    def str_synset_id(self, str_synset):
        """
        Returns the WordNet 3.0 synset ID for this synset string str_synset.

        :param str_synset: str, for a Synset in WordNet
        :return: str, WordNet synset ID for this str's synset
        """
        return self.synset_id(self.str_synset(str_synset))

    # TRANSLATOR
    # ==========
    def translate(self, phrase, **kwargs):
        """
        Translates input phrase to Blissymbols according to this
        BlissTranslator's part-of-speech and language preferences.
        ~
        Saves translation to a PDF file in this directory's
        out folder with this title, or otherwise
        titled after this phrase's first 20 characters.
        ~
        Default image size is 816x1056px (standard PDF page).

        :param phrase: str, text in BlissTranslator's native language
        :keyword lang: str, phrase's language
        :keyword width: int, desired width of PDF pages (in pixels)
        :keyword height: int, desired height of PDF pages (in pixels)
        :keyword title: str, desired title for output PDF
        :keyword title_pg: bool, whether to create title page
        :keyword pos: Iterable[str], Penn Treebank parts of speech to translate
        :keyword page_nums: bool, whether to add numbers to PDF pages
        :return: FPDF, pdf document named title with pages of phrase in Blissymbols
        """
        kwargs = self._setdefault_kwargs(**kwargs)
        pages = self.translate_to_pages(phrase, **kwargs)
        pdf = self.get_pdf(kwargs['title'], pages, margins=50, page_nums=kwargs['page_nums'])
        self.refresh_data()
        return pdf

    def translate_to_pages(self, phrase, **kwargs):
        """
        Translates input phrase to Blissymbols according to this
        BlissTranslator's part-of-speech and language preferences.
        ~
        Returns a list of Images of pages translated to Blissymbols.
        ~
        Default image size is 816x1056px (standard PDF page).

        :param phrase: str, text to translate to pages of Blissymbols

        keyword args:
        :param lang: str, phrase's native language
        :param title: str, desired title for output PDF
        :param title_pg: bool, whether to create title page
        :param width: int, desired width of PDF pages (in pixels)
        :param height: int, desired height of PDF pages (in pixels)

        :return: List[Image], pages of phrase translated to Blissymbols
        """
        kwargs = self._setdefault_kwargs(**kwargs)
        img_w, img_h = kwargs['width'], kwargs['height']
        images = self.translate_to_images(phrase, **kwargs)
        pages = self.images_to_pages(images, img_w, img_h)

        if kwargs['title_pg']:
            title_pg = self.title_page(kwargs['title'], img_w, img_h)
            pages.insert(0, title_pg)

        return pages

    def translate_to_transwords(self, phrase, **kwargs):
        """
        Translates this phrase to a list of TranslationWords
        and returns the list.

        :param phrase: str, phrase to translate to TranslationWords
        :return: List[TranslationWord], TWs for each word in phrase
        """
        kwargs = self._setdefault_kwargs(**kwargs)
        lang = kwargs['lang']
        word_tags = self.tokenize_pos_tag(phrase, lang)
        return [self.translation_word(word_tag[0].lower() if self.in_bliss_dict(word_tag[0].lower(), lang)
                                      else word_tag[0], word_tag[1], lang) if self.is_word(word_tag[0])
                else word_tag[0] for word_tag in word_tags]

    def find_lemmas(self, word, pos, lang):
        wikt_pos = self.convert_pos_to_wikt(pos)
        return self.lang_parser.find_lemmas(word, wikt_pos[0] if wikt_pos is not None and len(wikt_pos) != 0 else None,
                                            lang)

    def find_english_translations(self, word, pos, lang):
        wikt_pos = self.convert_pos_to_wikt(pos) if pos is not None else None
        add_new = word not in self.words_seen
        return self.lang_parser.find_english_translations(word, wikt_pos, lang, add_new)

    def word_poses(self, word, lang):
        add_new = word not in self.words_seen
        poses = self.lang_parser.word_poses(word, lang, add_new=add_new)
        return self.convert_wikt_to_pos(poses)

    def word_pos(self, word, lang):
        add_new = word not in self.words_seen
        pos = self.lang_parser.word_pos(word, lang, add_new=add_new)
        return self.convert_wikt_to_pos(pos)

    def tokenize_pos_tag(self, phrase, lang=None):
        token_pos_tags = tokenizers.tokenize_pos_tag(phrase)

        if lang[:3] == "Eng":
            return token_pos_tags
        else:
            return [(w, max(self.word_poses(w, lang), [p], key=len)) for w, p in token_pos_tags]

    def translate_to_images(self, phrase, **kwargs):
        """
        Translates this phrase to a list of Images
        and returns the list.

        :param phrase: str, phrase to translate to TranslationWords
        :return: List[Images], an Image for each word/symbol in phrase
        """
        kwargs = self._setdefault_kwargs(**kwargs)
        trans_words = self.translate_to_transwords(phrase, **kwargs)
        imgs = []

        for trans_word in trans_words:
            if type(trans_word) == str:
                if trans_word == "\n":
                    imgs.append(None)
                else:
                    imgs.append(self.word_image(trans_word))
            else:
                lemma = trans_word.lemma
                if lemma == "\n":
                    imgs.append(None)
                else:
                    subs = kwargs['sub_all'] or not self.is_changed(lemma)
                    self.add_changed(lemma) if subs else self.add_seen(lemma)
                    img = trans_word.image(subs=subs)
                    imgs.append(img)

        self.init_seen_changed()
        return imgs

    def images_to_lines(self, images, w=WIDTH, init_indent=True):
        space = self.space_size()
        indent = self.font_size

        lines = []
        blank_line = blank_image(x=w, y=self.image_heights())
        add_line = lambda l: lines.append(overlay(l, blank_line))
        new_line = lambda: blank_line.copy()
        line = new_line()

        x = indent if init_indent else 2  # 2 is minimum space (1 pixel on each side)
        inc_x = lambda img: x + img.size[0] + space
        y = 0

        for image in images:
            if image is None:
                # start new paragraph
                add_line(line)
                line = new_line()
                x = indent
            else:
                # continue on current line until...
                if inc_x(image) > w:
                    # x > pdf width
                    x = 0
                    add_line(line)
                    line = new_line()

                line.paste(image, (x, y))
                x = inc_x(image)

        if line != blank_line:
            add_line(line)

        return lines

    def lines_to_pages(self, lines, h=HEIGHT):
        """
        Pastes each line Image in lines to a list of pages and
        returns the list.

        :param lines: List[Image], lines on pages (in order)
        :param h: int, desired height of each page (in pixels)
        :return: List[Image], pages with images pasted
        """
        if len(lines) != 0:
            pages = []
            new_page = lambda: blank_image(0, 0)
            line1 = lines[0]
            fill_page = lambda p: above(p, blank_image(line1.size[0], h - line1.size[1]))
            page = new_page()

            y = 0
            inc_y = lambda: y + int(self.image_heights()*1.5)

            for line in lines:
                if line is None:
                    continue
                else:
                    # continue on current page until...
                    if inc_y() > h:
                        # y > pdf height
                        page = fill_page(page)
                        pages.append(page)
                        page = new_page()
                        y = 0
                    else:
                        page = above(page, line)

            if page != new_page():
                page = fill_page(page)
                pages.append(page)

            blank_page = blank_image(page.size[0], h)
            return [overlay(page, blank_page) for page in pages]

    def images_to_pages(self, images, w=WIDTH, h=HEIGHT):
        """
        Pastes each image in images to a list of pages.
        ~
        Returns output list of pages.

        :param images: List[Image], Images to paste to pages (in order)
        :param w: int, desired width of each page (in pixels)
        :param h: int, desired height of each page (in pixels)
        :return: List[Image], pages with images pasted
        """
        space = self.space_size()
        indent = self.font_size

        pages = []
        new_page = lambda: blank_image(w, h)
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
                # continue on current line until...
                if inc_x(image) > w:
                    # x > pdf width
                    x = 0
                    y = inc_y()
                if inc_y() > h:
                    # y > pdf height
                    x, y = 0, 0
                    pages.append(page)
                    page = new_page()

                page.paste(image, (x, y))
                x = inc_x(image)

        pages.append(page)
        return pages

    def analyze_concepts(self, phrase):
        """
        Translates this phrase to Blissymbols and
        returns a frequency dictionary of the most common
        derivative Blissymbols in the output translations.

        :param phrase: str, phrase to analyze concepts of
        :return: dict, where...
            key (str) - name of Blissymbol
            val (int) - number of occurrences in translation
        """
        phrase = str(phrase)
        trans_words = self.translate_to_transwords(phrase)
        return self.analyze_trans_word_concepts(trans_words)

    def analyze_trans_word_concepts(self, trans_words):
        """
        Returns a frequency dictionary of the most common
        derivative Blissymbols in these trans_words.

        :return: List[TranslationWord], TWs for each word in a phrase
        :return: dict, where...
            key (str) - name of Blissymbol
            val (int) - number of occurrences in translation
        """
        concept_freqs = {}

        for trans_word in trans_words:
            if trans_word.has_blissymbol():
                blissymbol = trans_word.blissymbol
                subsymbols = blissymbol.get_subsymbols()

                if len(subsymbols) != 0:
                    for subsymbol in subsymbols:
                        name = subsymbol.bliss_name
                        concept_freqs.setdefault(name, int())
                        concept_freqs[name] += 1

        return concept_freqs

    def _setdefault_kwargs(self, **kwargs):
        kwargs.setdefault('title', 'translation')
        kwargs.setdefault('title_pg', False)
        kwargs.setdefault('page_nums', False)
        kwargs.setdefault('width', self.WIDTH)
        kwargs.setdefault('height', self.HEIGHT)
        kwargs.setdefault('sub_all', True)
        kwargs.setdefault('machine_learn', False)
        kwargs.setdefault('fast', True)
        kwargs.setdefault('lang', self.language)
        kwargs.setdefault('pos', PARTS_OF_SPEECH)  # set of desired parts of speech to translate
        return kwargs


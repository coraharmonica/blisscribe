"""
BLISSCRIBE:

    A Python module for translating text_image to Blissymbols.

    All relevant parts-of-speech tags (used throughout)
    constitute the Penn Treebank parts of speech, whose
    meanings are enumerated here:
    https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    These can also be found in the top-level docstring of parse_lexica.
"""
import os
import sys
import collections

from nltk.tag import pos_tag
from nltk.corpus import wordnet
from pattern3 import text
from pattern3.text import en, es, fr, de, it, nl
from fpdf import FPDF

PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(PATH)

from imports import safe_import

safe_import("fonts")
safe_import("punctuation")
safe_import("parts_of_speech")
safe_import("images")
safe_import("lexicon_parser")
safe_import("translation_word")
safe_import("speechart")
safe_import("ordered_set")

from fonts import *
from punctuation import *
from parts_of_speech import *
from images import make_font, make_blank_img, get_word_img, trim, above, beside, overlay, Image
from lexicon_parser import LexiconParser, Blissymbol, NEW_BLISSYMBOLS
from translation_word import TranslationWord
from speechart.language_parser import LanguageParser
import speechart.tokenizers as tokenizers
from ordered_set import OrderedSet


class BlissTranslator:
    """
    A class for translating text_image in select languages to Blissymbols.
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
    PDF of the given text_image with Blissymbols.
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
        2) selecting whether to translate text_image to Blissymbols
           immediately or gradually
           --> set_fast_translate()
        3) selecting font & font size for output PDF translations
           --> set_font()
        4) selecting whether to subtitle all Blissymbols or only
           new Blissymbols
           --> set_sub_all()
    """
    DEFAULT_LANG = "English"
    DIMS = (816, 1056)

    def __init__(self, language=DEFAULT_LANG, font_path=SANS_FONT, font_size=30):
        self.lex_parser = LexiconParser(translator=self)
        self.lang_parser = None
        self.classifier = None
        self.images_saved = 0

        # Fonts
        self.font_size = font_size
        self.font_path = font_path
        self.font_fam = FONT_PATHS[self.font_path]
        self.font = make_font(self.font_path, self.font_size)

        # Language
        self.bliss_dicts = {}
        self.blissnet = None
        self.lexica = {}
        self.language = ""
        self.lang_code = ""
        self.set_language(language)
        self.words_seen = {}
        self.words_changed = {}
        self.init_seen_changed()
        self.defns_chosen = {}  # holds user choices for correct word definitions

        # Settings
        self.sub_all = False
        self.page_nums = True
        self.fast_translate = False
        self.safe_translate = False
        self.translate_all = False
        self.machine_translate = False

        self.chosen_pos = set()
        self.set_translatables()

    # INITIALIZATIONS
    # ===============
    def init_lang_parser(self):
        """
        Initializes this BlissTranslator with a LanguageParser
        for Wiktionary lookups on words if it does not exist yet.

        :return: None
        """
        if self.lang_parser is None:
            self.lang_parser = LanguageParser(self.language)

    def init_classifier(self):
        """
        Initializes this BlissTranslator with a classifier
        for translating uncommon words to Blissymbols
        if classifier does not exist yet.
        ~
        Returns this BlissTranslator's classifier.

        :return: BlissClassifier, a text_image-to-Blissymbols classifier
        """
        if self.classifier is None:
            # import blisslearn HERE since django can't handle sklearn
            try:
                from blisslearn import BlissClassifier
            except ImportError:
                print("blisslearn module could not be imported.\n\
                    Please find the local module blisslearn.py \n\
                    and relocate it to the same directory as blisscribe.py.")
                return
            else:
                self.classifier = BlissClassifier(self)
        return self.classifier

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

    def init_blissnet(self):
        """
        Initializes this BlissTranslator with a Blissymbols WordNet
        if one does not exist yet.
        ~
        Returns this BlissTranslator's blissnet.

        :return: dict, where...
            key (str) - unicode for Blissymbol with Synsets
            val (List[Synset]) - PWN Synsets for given Blissymbol
        """
        if self.blissnet is None:
            blissnet = self.lex_parser.load_blissnet()
            self.blissnet = {uni: self.strs_synsets(blissnet[uni]) for uni in blissnet}
        return self.blissnet

    def init_bci_blissnet(self):
        """
        Initializes this BlissTranslator with a Blissymbols WordNet
        if one does not exist yet.
        ~
        Returns this BlissTranslator's blissnet.

        :return: dict, where...
            key (str) - Blissymbol's BCI-AV number
            val (List[str]) - PWN synset strings for given Blissymbol
        """
        if self.blissnet is None:
            self.blissnet = self.lex_parser.load_bci_blissnet()
            #
            #
        return self.blissnet

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
        self.lex_parser.init_blissymbols()
        lang_bliss_dict = self.lex_parser.init_bliss_lexicon(self.language)
        eng_bliss_dict = lang_bliss_dict if self.lang_code == "eng" \
            else self.lex_parser.init_bliss_lexicon("English")
        self.add_bliss_dict(bliss_dict=lang_bliss_dict, language=self.language, sub=True)
        self.add_bliss_dict(bliss_dict=eng_bliss_dict, language="English", sub=True)

    def init_tokenizer(self):
        """
        Initializes this BlissTranslator's lang_code according to
        its native language.
        ~
        If lang_code is not in WordNet, this method loads custom
        lemmas for this BlissTranslator's language.

        :param language: str, language for this BlissTranslator
        :return: None
        """
        tokenizers.init_word_tokenizer()

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
            if self.language == language:
                return
            self.language = language
        else:
            if len(self.language) == 0:
                self.language = "English"
            else:
                return

    def init_lang_code(self):
        """
        Initializes this BlissTranslator's lang_code according to
        its native language.
        ~
        If lang_code is not in WordNet, this method loads custom
        lemmas for this BlissTranslator's language.

        :param language: str, language for this BlissTranslator
        :return: None
        """
        self.lang_code = self.find_lang_code(self.language)
        if self.lang_code != "eng":  # add OMW data to non-English wordnets
            self.load_multilingual_lemmas(self.lang_code)

    def init_bliss_to_unicode(self):
        """
        Initializes this BlissTranslator's Blissymbols-to-unicode
        encoding dictionary.

        :return: dict, where...
            key (str) - Blissymbol name
            val (List[str]) - unicode Blissymbol codes (in hexadecimal)
        """
        if self.bliss_to_unicode is None:
            self.bliss_to_unicode = self.lex_parser.load_bliss_encoding()
        return self.bliss_to_unicode

    def init_unicode_to_bliss(self):
        """
        Initializes this BlissTranslator's unicode-to-Blissymbols
        encoding dictionary.

        :return: dict, where...
            key (str) - unicode Blissymbol code (in hexadecimal)
            val (List[str]) - list of Blissymbol names
        """
        if self.unicode_to_bliss is None:
            self.unicode_to_bliss = self.lex_parser.load_bliss_decoding()
        return self.unicode_to_bliss

    def init_bliss_unicode(self):
        """
        Initializes this BlissTranslator's Blissymbols-to-unicode
        encoding dictionary.

        :return: dict, where...
            key (str) - unicode for Blissymbol
            val (str) - name of Blissymbol
        """
        if self.bliss_unicode is None:
            self.bliss_unicode = self.lex_parser.load_bliss_unicode()
        return self.bliss_unicode

    # SETTERS
    # -------
    def set_lang_parser(self, lang_parser):
        """
        Sets this BlissTranslator's language parser to this lang_parser.

        :param lang_parser: LanguageParser, parser to set as lang_parser
        :return: None
        """
        self.lang_parser = lang_parser

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
        self.init_lang_code()
        self.init_lexicon(self.language)
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

    def set_sub_all(self, sub_all):
        """
        Sets self.sub_all equal to input sub_all value.
        ~
        Setting sub_all to True will produce subtitles under
        all words translated to Blissymbols.
        Setting sub_all to False will produce subtitles only
        under new words translated to Blissymbols.
        ~
        Sets subtitle setting for this BlissTranslator's
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
        for translating unknown words to Blissymbols.

        :param machine_translate: bool, whether to initialize a
            machine learning classifier
        :return: None
        """
        self.machine_translate = machine_translate

        if self.machine_translate:
            self.init_classifier()

    def set_translatables(self, nouns=True, verbs=True, adjs=True, other=False, all=False):
        """
        Allows user to set whether to translate nouns, verbs,
        adjectives, all other parts of speech, OR all parts of speech.
        ~
        Changes this BlissTranslator's variables with the same names.

        :param nouns: bool, True to translate nouns
        :param verbs: bool, True to translate verbs
        :param adjs: bool, True to translate adjectives
        :param other: bool, True to translate all other parts of speech
        :param all: bool, True to translate all parts of speech
        :return: None
        """
        self.chosen_pos = set()

        if all:
            self.chosen_pos.update(PARTS_OF_SPEECH)
        else:
            noun_codes = set(WIKTIONARY_POS_KEY["Noun"])
            verb_codes = set(WIKTIONARY_POS_KEY["Verb"])
            adj_codes = set(WIKTIONARY_POS_KEY["Adjective"] + WIKTIONARY_POS_KEY["Adverb"])
            other_codes = PARTS_OF_SPEECH.difference(noun_codes.union(verb_codes.union(adj_codes)))

            if nouns:
                self.chosen_pos.update(noun_codes)
            if verbs:
                self.chosen_pos.update(verb_codes)
            if adjs:
                self.chosen_pos.update(adj_codes)
            if other:
                self.chosen_pos.update(other_codes)

    # BLISS CONVERSIONS
    # -----------------
    def get_bliss_to_unicode(self):
        """
        Returns the global Blissymbols-to-unicode
        encoding dictionary.

        :return: dict, where...
            key (str) - Blissymbol name
            val (List[str]) - unicode Blissymbol codes (in hexadecimal)
        """
        return self.init_bliss_to_unicode()

    def get_unicode_to_bliss(self):
        """
        Returns the global unicode-to-Blissymbols
        encoding dictionary.

        :return: dict, where...
            key (str) - unicode Blissymbol code (in hexadecimal)
            val (List[str]) - list of Blissymbol names
        """
        return self.init_unicode_to_bliss()

    def unicode_to_blissymbol(self, uni):
        """
        Returns this unicode string's corresponding Blissymbol.

        :param uni: str, 4-character unicode for a Blissymbol
        :return: Blissymbol, Blissymbol corresponding to uni
        """
        blissword = self.lookup_bliss_unicode(uni)
        if blissword is not None:
            blissymbol = self.blissword_to_blissymbol(blissword)
            return blissymbol

    def lookup_bliss_to_unicode(self, blissword):
        """
        Returns this blissword's unicode ID.

        :param blissword: str, word for Blissymbol to lookup
        :return: List[str], unicode names for blissword
        """
        return self.init_bliss_to_unicode().get(blissword, [])

    def lookup_unicode_to_bliss(self, uni):
        """
        Returns this unicode ID's corresponding Blissymbol word(s).

        :param uni: str, unicode name to lookup
        :return: List[str], Blissymbol words for uni
        """
        return self.init_unicode_to_bliss().get(uni, [])

    def lookup_bliss_unicode(self, uni):
        """
        Returns this unicode ID's corresponding Blissymbol name.

        :param uni: str, unicode name to lookup
        :return: str, Blissymbol name for uni
        """
        return self.init_bliss_unicode().get(uni, None)

    def add_bliss_to_unicode(self, bliss, uni):
        """
        Adds this blissymbol-unicode pair to this
        BlissTranslator's Blissymbols-to-unicode
        encoding dictionary.

        :param bliss: str, name of blissymbol to add
        :param uni: str, unicode name for given bliss
        :return: None
        """
        self.init_bliss_to_unicode()
        if bliss not in self.bliss_to_unicode:
            self.bliss_to_unicode[bliss] = []
        if uni not in self.bliss_to_unicode[bliss]:
            self.bliss_to_unicode[bliss].append(uni)

    def add_unicode_to_bliss(self, uni, bliss):
        """
        Adds this unicode-blissymbol pair to this
        BlissTranslator's unicode-to-Blissymbols
        encoding dictionary.

        :param uni: str, unicode name to add
        :param bliss: str, blissymbol name for given unicode
        :return: None
        """
        self.init_unicode_to_bliss()
        if uni not in self.unicode_to_bliss:
            self.unicode_to_bliss[uni] = []
        if bliss not in self.unicode_to_bliss[uni]:
            self.unicode_to_bliss[uni].append(bliss)

    def add_bliss_unicode(self, uni, bliss):
        """
        Adds this unicode key to this Blissymbol's
        BlissTranslator's unicode-to-Blissymbol dict,
        with blissymbol name bliss as its value.

        :param uni: str, unicode name to add
        :param bliss: str, name of blissymbol for this unicode
        :return: None
        """
        self.init_bliss_unicode()
        if uni not in self.bliss_unicode:
            self.bliss_unicode[uni] = bliss

    def add_bliss_dict(self, language, bliss_dict, sub=False):
        """
        Adds this language as a key with this bliss_dict as
        its value to this BlissTranslator's bliss_dicts.
        ~
        If sub is True, substitutes existing dictionary with bliss_dict.

        :param language: str, language of bliss_dict
        :param bliss_dict: dict, word-to-Blissymbol dictionary
        :param sub: bool, whether to substitute bliss_dict for existing dict
        :return: None
        """
        if sub:
            self.bliss_dicts[language] = bliss_dict
        else:
            self.bliss_dicts.setdefault(language, bliss_dict)

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
    def refresh_bliss_dicts(self):
        """
        Overwrites the source Blissymbols lexicon, encoding, and
        decoding dictionaries with this BlissTranslator's
        eng_bliss_dict, bliss_to_unicode, and unicode_to_bliss dicts.

        :return: None
        """
        #self.lex_parser.refresh_bliss_encoding()
        #self.lex_parser.refresh_bliss_decoding()
        #self.lex_parser.refresh_bliss_unicode()
        self.lex_parser.refresh_bliss_lexicon()

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

    def subtitle_size(self):
        """
        Returns a font size suitable as a subtitle for this
        BlissTranslator's default font_size.

        :return: int, subtitle font size
        """
        return int(self.font_size * 0.5)

    def bliss_image(self, trans_word):
        """
        Returns a thumbnail Image of this TranslationWord's
        Blissymbol, with height as its translator's image_heights.
        ~
        If this TranslationWord's Blissymbol is None,
        returns an Image with its word as text_image instead.

        :param trans_word: TranslationWord, word to render to Image
        :return: Image, image of input str's Blissymbol
        """
        return trans_word.image()

        height = self.image_heights()

        if not trans_word.has_blissymbol():
            return self.trans_word_image(trans_word, height)
        else:
            blissymbol = trans_word.blissymbol
            img = blissymbol.image(max_height=height)
            if trans_word.is_plural_noun():
                img = blissymbol.pluralize_image(img)
            return img

    def subbed_bliss_image(self, trans_word, subs=False):
        """
        Returns this TranslationWord's Blissymbol subtitled with its word.
        ~
        If subs is set to False, output Image has no subtitles, but
        still offsets as if there were.

        :param trans_word: TranslationWord, word to translate & subtitle
        :param subs: bool, whether to subtitle output image
        :return: Image, subtitled Blissymbol image
        """
        if trans_word.has_blissymbol():
            img = self.bliss_image(trans_word)
        else:
            subs = False
            img = self.trans_word_image(trans_word, subs=False)

        subtitle = self.trans_word_image(trans_word, subs)
        subtitle = trim(subtitle)
        if not subs:
            subtitle = make_blank_img(1, subtitle.size[1])
        img = above(img, subtitle)
        return img

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
        return get_word_img(word, font_path, font_size, height)

    def trans_word_image(self, trans_word, subs=False):
        """
        Returns an Image of this TranslationWord's word.
        ~
        If subs is False, creates word Image from word with
        translator's font_size.  Otherwise, creates word image
        from uppercase word and translator's subtitle_size().

        :param trans_word: TranslationWord, word to render to Image
        :param subs: bool, whether to subtitle image
        :return: Image, image of input trans_word
        """
        return self.word_image(trans_word.word, subs)

    def get_space_size(self):
        """
        Returns an appropriate space size relative to this
        BT's font_size in pixels.

        :return: int, space size (in pixels)
        """
        return int(self.font_size * 0.75)

    def save_image(self, img):
        """
        Saves the input Image, img, as a .png file.
        ~
        Names image beginning at this BlissTranslator's
        images_saved variable and incrementing by 1.
        ~
        Returns the filename for this image.

        :param pages: Image, image to save to file
        :return: str, image's filename
        """
        filename = "bliss_img" + str(self.images_saved) + ".png"
        img.save(filename)
        self.images_saved += 1
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
        Returns this PDF with a title page added to it.

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
        Returns a title page of dimensions x and y with this title.

        :param title: str, title name
        :param x: int, x-dimension of output title page
        :param y: int, y-dimension of output title page
        :return: Image, title page
        """
        img = make_blank_img(x, y)
        title_img = get_word_img(title, self.font_path, self.font_size, self.image_heights())

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
        :return: FPDF, pdf document named filename with pages
        """
        pdf = self.get_pdf(pages, margins)
        pdf.output(PATH + "/out/" + filename + ".pdf", "F")
        return pdf

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
        return LANG_CODES.get(language, None)

    def supported_languages(self):
        """
        Returns a set of the languages currently supported by Blisscribe.

        :return: Set(str), languages supported by Blisscribe
        """
        supported_langs = self.lex_parser.BLISS_LANGS.intersection(self.wordnet_langs())
        pattern_langs = text.LANGUAGES
        supported_langs.update(pattern_langs)
        return supported_langs

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
            else:
                raise ValueError("Blisscribe doesn't support this language yet... oops!")

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

    def get_word_tag(self, trans_word):
        """
        Returns this TranslationWord's part-of-speech tag.

        :param trans_word: TranslationWord, word to tag
        :return: str, given word's pos tag
        """
        if self.language != "English":
            self.init_lang_parser()
            add_new = not (trans_word.word in self.words_seen and trans_word.word not in self.words_changed)
            wikt_poses = self.lang_parser.find_word_poses(trans_word.lemma, trans_word.language, add_new=add_new)
            if add_new:
                self.add_seen(trans_word.word)
            wikt_poses = self.convert_wikt_poses(wikt_poses) if wikt_poses is not None else []
            synset_poses = self.multilingual_poses(trans_word)
            poses = OrderedSet(wikt_poses + synset_poses).items()
            if len(poses) != 0:
                pos = poses[0]
                trans_word.set_pos(pos)

        return trans_word.pos

    def get_token_phrase(self, phrase):
        """
        Returns a list of word tokens in phrase.

        :param phrase: str, text_image with >=1 words
        :return: List[str], list of word tokens
        """
        self.init_tokenizer()
        return tokenizers.word_tokenizer.tokenize(phrase)

    def get_token_phrases(self, text):
        """
        Returns a list of word tokens in text_image,
        with a newline in between each phrase.

        :param phrases: List[str], phrases to tokenize
        :return: List[str], list of word tokens
        """
        phrases = text.split("\n")  # split text_image by newlines
        token_phrases = []
        for phrase in phrases:
            token_phrases.extend(self.get_token_phrase(phrase))
            token_phrases.append("\n")
        return token_phrases

    def convert_pos_to_wikt(self, pos):
        """
        Returns this Penn Treebank part of speech converted
        to its Wiktionary part of speech.
        ~
        e.g. convert_wikt_pos("NN") -> "Noun"

        :param pos: str, Penn Treebank part of speech
        :return: str, Wiktionary part of speech
        """
        return POS_WIKT_KEY.get(pos, None)

    def convert_wikt_pos(self, wikt_pos):
        """
        Returns this Wiktionary part of speech converted
        to its Penn Treebank parts of speech.
        ~
        e.g. convert_wikt_pos("Noun") -> ["NN", "NNS"]

        :param wikt_pos: str, Wiktionary part of speech
        :return: List[str], Penn Treebank part(s) of speech
        """
        return WIKTIONARY_POS_KEY.get(wikt_pos, None)

    def convert_wikt_poses(self, wikt_poses):
        """
        Returns this list of Wiktionary parts of speech converted
        to a set of Penn Treebank parts of speech.
        ~
        e.g. convert_wikt_pos(["Article", "Proper noun"]) -> {"DT", "NNP", "NNPS"}

        :param wikt_pos: List[str], Wiktionary parts of speech
        :return: Set(str), Penn Treebank parts of speech
        """
        poses = OrderedSet([])
        for wikt_pos in wikt_poses:
            converted_pos = self.convert_wikt_pos(wikt_pos)
            if converted_pos is not None:
                poses.update(converted_pos)
        return poses.items()

    def token_pos(self, token):
        """
        Returns the Penn Treebank part of speech for this token.
        ~
        e.g. token_pos("dogs") -> "NNS"

        :param token: str, word token
        :return: str, token's part of speech
        """
        tups = pos_tag([token.lower()], lang=self.lang_code)
        tup = tups[0]
        pos = tup[1]
        return pos

    def tokens_poses(self, token_phrase):
        """
        Returns a list of Penn Treebank parts of speech
        for each token in token_phrase.

        :param token_phrase: List[str], word tokens
        :return: List[str], parts of speech for tokens in token_phrase
        """
        tagged_phrase = pos_tag([token.lower() for token in token_phrase],
                                lang=self.lang_code)  # tokens tagged according to word type
        tagged_list = []
        for tup in tagged_phrase:
            tagged_list.append(tup[1])
        return tagged_list

    def abbreviate_pos(self, pos):
        """
        Returns an abbreviation for this Penn Treebank
        part of speech, pos, from "a", "v", "n", "r", "s".
        ~
        e.g. abbreviate_pos("RB") -> "r"

        :param pos: str, Penn Treebank part of speech
        :return: str, 1-character abbreviated part of speech
        """
        pos_letter = pos[0].lower()
        if pos_letter == "j":
            pos_letter = "a"

        if pos_letter not in POS_ABBREVS_SORTED:
            return
        else:
            return pos_letter

    def unabbreviate_pos(self, pos):
        """
        Given an abbreviated part of speech from "a", "v", "n", "r", "s",
        returns the corresponding Penn Treebank part of speech.
        ~
        e.g. unabbreviate_pos("r") -> "RB"

        :param pos: str, abbreviated part of speech
        :return: str, Penn Treebank part of speech
        """
        assert pos in POS_UNABBREVS
        return POS_UNABBREVS[pos]

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

    def is_chosen_pos(self, pos):
        """
        Returns True if words with this part of
        speech should be translated, False otherwise.

        :param pos: str, part-of-speech tag
        :return: bool, whether to translate pos
        """
        #if self.lang_code != "eng":
        #    # FIXME: translate all words in non-English langs until better foreign tagging
        #    return True
        return pos in self.chosen_pos

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
        return word in self.init_bliss_to_unicode()

    def in_bliss_dict(self, word, language):
        """
        Returns True if word in eng_bliss_dict,
        False otherwise.

        :param word: str, word to check eng_bliss_dict membership
        :param language: str, language of Blissymbols dict
        :return: bool, whether word is in eng_bliss_dict
        """
        bliss_dict = self.find_bliss_dict(language)
        return word in bliss_dict

    def lookup_bliss_dict(self, word, language):
        """
        Returns the Blissymbols for this word in this language.
        ~
        If word is not in this language's Blissymbols dictionary, returns None.

        :param word: str, word to lookup in bliss_dict
        :param language: str, language of Blissymbols dict
        :return: List[Blissymbol], word's blissymbols in bliss_dict
        """
        bliss_dict = self.find_bliss_dict(language)
        return bliss_dict.get(word, None)

    def find_bliss_dict(self, language):
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
            self.add_bliss_dict(language, bliss_dict)
        return bliss_dict

    def lookup_blissnet(self, blissymbol):
        """
        Returns this Blissymbol's corresponding synset strings
        from this BlissTranslator's blissnet.
        ~
        If blissymbol is not in blissnet, returns None.

        :param blissymbol: Blissymbol, symbol to lookup in blissnet
        :return: List[str], synset strings corresponding to given Blissymbol
        """
        return self.init_bci_blissnet().get(blissymbol.bci_num, None)

    def retrieve_lexicon(self, language):
        """
        Retrieves the lexicon dictionary for this language
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
        return self.lexica.get(language, None)

    def all_synsets(self):
        return wordnet.all_synsets()

    def in_wordnet(self, word, language):
        """
        Returns True if word in WordNet,
        False otherwise.

        :param word: str, word to check WordNet membership
        :return: bool, whether word is in WordNet
        """
        return word in wordnet.all_lemma_names(lang=self.find_lang_code(language))

    def is_valid_word(self, word):
        """
        Returns True if word is a valid word in this
        BlissTranslator's native language, False otherwise.

        :param word: str, word to check if valid
        :return: bool, whether word is valid
        """
        return self.in_bliss_dict(word, self.language)

    def is_valid_eng_word(self, word):
        """
        Returns True if word is a valid word in this
        BlissTranslator's native language, False otherwise.

        :param word: str, word to check if valid
        :return: bool, whether word is valid
        """
        return self.in_multi_bliss_dict(word, "English")

    @staticmethod
    def remove_parens(word, starts={"(", "["}, ends={")", "]"}):
        """
        Removes parenthetical(s) from this word and
        returns the result.
        ~
        Parenthetical begins at the first open parenthesis.

        e.g. remove_parens("English_(language)") -> "English"

        :param word: str, word to remove parenthetical from
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

    @staticmethod
    def extract_parens(word, starts={"(", "["}, ends={")", "]"}):
        """
        Extracts first parenthetical from this word and
        returns its contents.
        ~
        Parenthetical begins at the first open parenthesis.

        e.g. extract_parens("English_(language)") -> "language"

        :param word: str, word to extract parenthetical from
        :return: str, word's parenthetical phrase
        """
        idx = 0
        num_starts, start_idx = 0, 0

        for char in word:
            if char in starts:
                if num_starts == 0:
                    start_idx = idx
                num_starts += 1
            elif char in ends:
                num_starts -= 1
                if num_starts == 0:
                    stripped = word[start_idx+1:idx]
                    stripped = stripped.strip()
                    stripped = stripped.strip("_")
                    stripped = stripped.rstrip("-")
                    return stripped
            idx += 1
        else:
            if num_starts == 0:
                return word
            else:
                return word[start_idx+1:]

    def lemmatize(self, word, pos=None, language="English"):
        """
        Retrieves this word's lemma,
        i.e., the word in dictionary entry form.
        ~
        e.g. lemmatize("ran") -> "run"
             lemmatize("puppies") -> "puppy"
        ~
        N.B. If a lemma for this word cannot
        be found, this method returns the input.

        :param word: str, word to convert to lemma
        :param language: str, input word's native language
        :return: str, lemma of input word
        """
        bliss_dict = self.find_bliss_dict(language)

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
        in this language's lexicon.
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

    def multilingual_poses(self, trans_word):
        """
        Returns a part of speech for this (non-English) TranslationWord
        from its synsets.
        ~
        If trans_word has no synsets, returns trans_word's current pos.

        :param trans_word: TranslationWord, non-English word to find pos for
        :return: List[str], Penn Treebank part of speech for this trans_word
        """
        synsets = trans_word.synsets
        poses = OrderedSet([])
        for synset in synsets:
            poses.add(self.unabbreviate_pos(synset.pos()))
        return poses.items()

    def multilingual_lemma(self, trans_word):
        """
        Returns an English lemma for this (non-English) TranslationWord
        from its synsets.
        ~
        If trans_word has no synsets, returns trans_word's current lemma.

        :param trans_word: TranslationWord, word to find lemma for
        :return: str, English lemma for trans_word
        """
        synsets = trans_word.synsets

        try:
            synsets[0]
        except IndexError:
            return trans_word.lemma
        else:
            synset = synsets[0]
            lemma = synset.lemma_names()[0]
            return lemma

    def is_translatable(self, trans_word):
        """
        Returns True if trans_word's lemma or synonym(s)
        can be translated to Blissymbols, False otherwise.

        :param trans_word: TranslationWord, word to test whether translatable
        :return: bool, whether given trans_word is translatable
        """
        lemma = trans_word.lemma
        # check if this word's lemma or synonyms are translatable
        if self.in_bliss_dict(lemma, trans_word.language):
            return True
        elif self.is_synset_translatable(trans_word):
            return True
        # if neither, word is untranslatable
        return False

    def is_synset_translatable(self, trans_word):
        """
        Given a TranslationWord, returns True if any of its synonyms
        are translatable.

        :param trans_word: TranslationWord, word to generate synonyms
        :return: bool, whether trans_word synonyms are translatable
        """
        synsets = self.translate_untranslatable(trans_word)

        if len(synsets) != 0:
            trans_word.set_synsets(synsets)
            return True

        return False

    def should_translate(self, trans_word):
        """
        Returns True if given TranslationWord should be translated
        according to this BlissTranslator's language
        preferences, False otherwise.

        :param trans_word: TranslationWord, word whether to translate
        :return: bool, whether trans_word should be translated
        """
        is_chosen_pos = self.is_chosen_pos(trans_word.pos)

        if is_chosen_pos:
            if trans_word.has_blissymbol():
                return True
            else:
                return self.is_translatable(trans_word)
        else:
            return False

    def should_translate_now(self, trans_word):
        """
        Returns True if words with trans_word's lemma should be
        translated now, False if later/never.

        :param trans_word: TranslationWord, word to test
            whether to translate now
        :return: bool, whether to translate given lemma now
        """
        return self.fast_translate or self.is_seen(trans_word.lemma)

    def translate_untranslatable(self, trans_word):
        """
        Returns a list of this word's synsets that can be
        translated to Blissymbols.

        :param word: str, word to translate to Blissymbols
        :return: List[str], translatable synset(s) of this word
        """
        return self.translatable_synsets(trans_word.synsets)

    def make_translation_word(self, word_token, pos, language="English", debug=False):
        """
        Returns a new TranslationWord with...
            word_token as its word
            pos as its part-of-speech
            this BlissTranslator as its translator
            language as its language
            debug as its debug setting

        :param word_token: str, a word token representing the word as found in text_image
        :param pos: str, this word token's (Penn Treebank) part-of-speech
        :param language: str, native language of given word token
        :param debug: bool, whether user will provide new inputs to TranslationWord
        :return: TranslationWord, a new TranslationWord with the given fields
        """
        return TranslationWord(word=word_token, pos=pos, translator=self, language=language, debug=debug)

    def make_blissymbol(self, bliss_name, pos, derivation, translations=None, num=0):
        """
        Returns a new Blissymbol with...
            bliss_name as its English lookup name
            pos as its part-of-speech
            derivation as its list of Blissymbol derivations
            num as its BCI-AV#

        :param bliss_name: str, this Blissymbol's official name
        :param pos: str, this Blissymbol's (Penn Treebank) part-of-speech
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

    def fetch_bliss_name(self, word, language="English"):
        """
        Returns the Blissymbol name associated with
        this word.
        ~
        e.g. fetch_bliss_name("lapin", "French") -> "rabbit,hare"

        :param word: str, word to get Blissymbol name of
        :param language: str, word's native language
        :return: str, Blissymbol name for this word
        """
        bliss = self.word_to_blissymbol(word, language)
        if bliss is not None:
            return bliss.bliss_name
        else:
            return

    def word_to_blissymbol(self, word, language="English", pos=None):
        """
        Returns the Blissymbol for this word in this language
        with this part of speech.
        ~
        If this word cannot be translated to a Blissymbol,
        this method returns None.

        :param word: str, word to lookup Blissymbol for
        :param language: str, word's native language
        :param pos: str, word's part of speech
        :return: Blissymbol, a Blissymbol for this word
        """
        if word is not None:
            if "," in word or "(" in word:
                return self.blissword_to_blissymbol(word)
            else:
                clean_word = self.deunderscore(word)
                blissymbols = self.lookup_bliss_dict(clean_word, language)

                if pos is not None and blissymbols is not None:
                    blissymbols = {bliss for bliss in blissymbols if pos in bliss.pos}

                if blissymbols is None or len(blissymbols) == 0:
                    return
                elif len(blissymbols) == 1:
                    blissymbol = blissymbols.pop()
                    blissymbols.add(blissymbol)
                    return blissymbol
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
                            translations = blissymbol.get_translation(language)

                            if clean_word in translations or clean_word in translations:
                                return blissymbol

                        return nonneutral
                else:
                    return

    def words_to_blissymbol(self, words, language="English", pos=None):
        """
        Returns the Blissymbol common to all these words.
        ~
        If words have no Blissymbol, returns None.

        :param words: List[str], words to lookup Blissymbol for
        :param language: str, word's native language
        :param pos: str, words' part of speech
        :return: Blissymbol, a Blissymbol corresponding to this word
        """
        blissymbols = OrderedSet([])

        for word in words:
            entry = self.lookup_bliss_dict(word, language)
            if entry is not None:
                if pos is not None:
                    entry = {bliss for bliss in entry if pos in bliss.pos}
                blissymbols.update(entry)

        blissymbols = blissymbols.intersections()
        blissymbol = blissymbols[0] if len(blissymbols) != 0 else None
        return blissymbol

    def synset_to_blissymbol(self, synset):
        """
        Returns the Blissymbol common to all this synset's lemma names.
        ~
        If synset has no Blissymbol, returns None.

        :param synset: Synset, synset to lookup Blissymbol for
        :return: Blissymbol, a Blissymbol for this synset
        """
        lemmas = self.synset_lemmas(synset, eng=True)
        return self.words_to_blissymbol(lemmas, language="English", pos=self.synset_pos(synset))

    def synsets_to_blissymbol(self, synsets):
        """
        Returns the Blissymbol common to all these synsets.
        ~
        If words have no Blissymbol, returns None.

        :param synsets: List[Synset], synsets to lookup Blissymbol for
        :return: Blissymbol, a Blissymbol for these synsets
        """
        if len(synsets) != 0:
            lemmas = self.synsets_lemmas(synsets, eng=True)
            return self.words_to_blissymbol(lemmas, language="English", pos=self.synset_pos(synsets[0]))

    def find_blissymbol_bci_num(self, blissymbol):
        """
        Returns the BCI-AV# for a Blissymbol with the same
        bliss_name as given blissymbol.  If none exist,
        returns None.

        :param blissymbol: Blissymbol, to find BCI-AV# for
        :return: Optional[int], Blissymbol's BCI-AV# (None if nonexistent)
        """
        if blissymbol.bci_num is None:
            self.lex_parser.init_blissymbols()
            for bs in self.lex_parser.blissymbols:
                if bs.bliss_name == blissymbol.bliss_name:
                    return int(bs.bci_num)

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
                    word_synsets = self.lookup_words_synsets(translations, lang_code=lang_code, pos=blissymbol.get_pos())
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
        bliss_dict = self.find_bliss_dict(self.language)

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
                bliss_dict = self.find_bliss_dict(language)
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

    def lookup_multilingual_word_synsets(self, word, pos=None, lang_code="eng"):
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
                self.load_multilingual_lemmas(self.lang_code)
            except ValueError:
                return []
            else:
                WORDNET_SUPPORTED_LANGS.add(lang_code)
                return self.lookup_word_synsets(word, pos, lang_code) #language)
        else:
            return []

    def lookup_word_synsets(self, word, pos=None, lang_code="eng"):
        """
        Returns a list of Wordnet Synsets corresponding to this
        word, part of speech (pos), and language.
        ~
        If lookup fails with this pos, returns this
        word's Wordnet synsets for all parts of speech
        (assuming an incorrect pos label).

        :param word: str, word to lookup synset for
        :param pos: str, part-of-speech for given word
        :param lang_code: str, language of word
        :return: List[Synset], synsets corresponding to
            this word, pos, and lang
        """
        if pos is not None:
            pos = self.abbreviate_pos(pos)

        if lang_code is None:
            return []
        else:
            try:
                synsets = wordnet.synsets(word, pos, lang=lang_code)
            except wordnet.WordNetError:
                return self.lookup_multilingual_word_synsets(word, pos, lang_code)

            if len(synsets) == 0:
                synsets = wordnet.synsets(word, lang=lang_code)
            return synsets

    def lookup_words_synsets(self, words, pos=None, lang_code="English"):
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
        synsets = OrderedSet([])

        for word in words:
            word_synsets = self.lookup_word_synsets(word, pos=pos, lang_code=lang_code)
            if len(word_synsets) != 0:
                synsets.update(word_synsets)

        return synsets.intersections()

    def str_synset(self, s):
        """
        Returns a Wordnet Synset for this string s, where s
        follows the regex "\w+\.[nvas]\.d{2}", or
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
        if eng:
            lang_code = "eng"
        else:
            lang_code = self.lang_code
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
    def translate(self, phrase, title="translation", title_page=False, img_w=DIMS[0], img_h=DIMS[1]):
        """
        Translates input phrase to Blissymbols according to this
        BlissTranslator's part-of-speech and language preferences.
        ~
        Saves translation to a PDF file in this directory's
        out folder with this title, or otherwise
        titled after this phrase's first 20 characters.
        ~
        Default image size is 816x1056px (standard PDF page).

        :param phrase: str, text_image in BlissTranslator's native language
        :param title: str, desired title for output PDF
        :param title_page: bool, whether to create title page
        :param img_w: int, desired width of PDF pages (in pixels)
        :param img_h: int, desired height of PDF pages (in pixels)
        :return: FPDF, pdf document named title with pages of phrase in Blissymbols
        """
        pages = self.translate_to_pages(phrase, title, title_page, img_w, img_h)
        pdf = self.pages_to_pdf(pages, title)
        self.clear_new_blissymbols()
        self.refresh_bliss_dicts()
        return pdf

    def translate_to_pages(self, phrase, title="translation", title_page=False, img_w=DIMS[0], img_h=DIMS[1]):
        """
        Translates input phrase to Blissymbols according to this
        BlissTranslator's part-of-speech and language preferences.
        ~
        Returns a list of Images of pages translated to Blissymbols.
        ~
        Default image size is 816x1056px (standard PDF page).

        :param phrase: str, text_image in BlissTranslator's native language
        :param title: str, desired title for output PDF
        :param title_page: bool, whether to create title page
        :param img_w: int, desired width of PDF pages (in pixels)
        :param img_h: int, desired height of PDF pages (in pixels)
        :return: List[Image], pages of phrase translated to Blissymbols
        """
        title, phrase = str(title), str(phrase)
        images = self.translate_to_images(phrase)
        pages = self.images_to_pages(images, img_w, img_h)

        if title_page:
            title_pg = self.create_title_page(title, img_w, img_h)
            pages.insert(0, title_pg)

        return pages

    def translate_to_transwords(self, phrase):
        """
        Translates this phrase to a list of TranslationWords
        and returns the list.

        :param phrase: str, phrase to translate to TranslationWords
        :return: List[TranslationWord], TWs for each word in phrase
        """
        token_phrases = self.get_token_phrases(phrase)
        tagged_list = self.tokens_poses(token_phrases)
        trans_words = []

        for idx in range(len(token_phrases)):
            word_token = token_phrases[idx]
            word_tag = tagged_list[idx]
            trans_word = self.make_translation_word(word_token, word_tag, self.language, self.translate_all)
            trans_words.append(trans_word)

        return trans_words

    def translate_to_images(self, phrase):
        """
        Translates this phrase to a list of Images
        and returns the list.

        :param phrase: str, phrase to translate to TranslationWords
        :return: List[Images], an Image for each word/symbol in phrase
        """
        trans_words = self.translate_to_transwords(phrase)
        imgs = []

        for trans_word in trans_words:
            lemma = trans_word.lemma

            if lemma == "\n":
                imgs.append(None)
            else:
                can_translate = self.should_translate(trans_word) and self.should_translate_now(trans_word)
                if can_translate:
                    subs = self.sub_all or not self.is_changed(lemma)
                    self.add_changed(lemma) if subs else self.add_seen(lemma)
                    img = self.subbed_bliss_image(trans_word, subs=subs)
                else:
                    img = self.trans_word_image(trans_word, subs=False)
                imgs.append(img)

        self.init_seen_changed()
        return imgs

    def images_to_lines(self, images, w=DIMS[0], init_indent=True):
        space = self.get_space_size()
        indent = self.font_size

        lines = []
        blank_line = make_blank_img(x=w, y=self.image_heights())
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

    def lines_to_pages(self, lines, h=DIMS[1]):
        """
        Pastes each line Image in lines to a list of pages and
        returns the list.

        :param lines: List[Image], lines on pages (in order)
        :param h: int, desired height of each page (in pixels)
        :return: List[Image], pages with images pasted
        """
        if len(lines) != 0:
            pages = []
            new_page = lambda: make_blank_img(0, 0)
            line1 = lines[0]
            fill_page = lambda p: above(p, make_blank_img(line1.size[0], h-line1.size[1]))
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

            blank_page = make_blank_img(page.size[0], h)
            return [overlay(page, blank_page) for page in pages]

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

        pages = []
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

    def pages_to_pdf(self, pages, title):
        """
        Pastes each page in pages to a PDF and
        saves the PDF to /out/ under this title.

        :param pages: List[Image], pages with images pasted (in order)
        :param title: str, desired title for output PDF
        :return: FPDF, pdf document named title with pages
        """
        filenames = self.save_images(pages)
        return self.save_pdf(title, filenames, margins=50)

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

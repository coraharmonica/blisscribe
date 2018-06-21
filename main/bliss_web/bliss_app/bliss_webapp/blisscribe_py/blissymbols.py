# -*- coding: utf-8 -*-
"""
BLISSYMBOLS:

    Contains a class for representing a Blissymbol, either
    created from a language-to-Blissymbols dictionary file or
    by a user.
"""
from bliss_images import *
import re

NEW_BLISSYMBOLS = []    # stores new Blissymbols from Blissymbol.make_new_blissymbol() for deletion


class Blissymbol:
    """
    A class representing a Blissymbol, each with...
    - img filename
    - part of speech
    - a derivation
    - translation(s) in each language
    """
    PARTS_OF_SPEECH = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS",
                       "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$",
                       "RB", "RBR", "RBS", "RP", "TO", "UH", "VB", "VBD", "VBG",
                       "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"]
    POS_COLOUR_CODE = {"GRAY": ["INDICATOR"],
                       "WHITE": PARTS_OF_SPEECH,  # WHITE is catch-all for other parts of speech
                       "YELLOW": ["NN",
                                  "NNS",
                                  "NNP",
                                  "NNPS",
                                  ],
                       "RED": ["VB",
                               "VBD",
                               "VBG",
                               "VBN",
                               "VBP",
                               "VBZ",
                               ],
                       "BLUE": ["NN",  # personal (pro-)nouns
                                "NNS",
                                "NNP",
                                "NNPS",
                                "PRP",
                                "PRP$",
                                ],
                       "GREEN": ["JJ",
                                 "JJR",
                                 "JJS",
                                 "RB",
                                 "RBR",
                                 "RBS",
                                 ]}
    PUNCT_MAP = {",": u"comma",
                 ".": u"period,point,full_stop,decimal_point",
                 "?": u"question_mark",
                 "!": u"exclamation_mark"}

    def __init__(self, img_filename=None, pos=None, derivation="", translations=None, translator=None):
        self.translator = translator
        self.last_encoding = int(self.calc_last_unicode()[2:], 16)
        self.img_filename = img_filename
        self.bliss_name = self.img_filename[:-4]
        self.pos_code = pos
        self.init_pos_code(pos)
        self.pos = self.init_pos(pos)
        self.paren_phrase = self.get_parens(self.bliss_name)
        self.derivation = derivation
        self.is_atom = self.find_is_atom()
        self.derivations = self.find_derivations()
        self.check_img_filename()  # creates new blissymbol image from derivations if none exists
        self.translations = self.clean_translations(translations)  # hold translations in different languages
        self.bliss_glyph = None
        self.unicode = str()
        self.unicode = self.init_unicode()
        self.synset = None
        self.synsets = self.init_blissymbol_synsets()
        if self.valid_filename():
            self.translator.add_bliss_entry(self)

    def calc_last_unicode(self):
        """
        Returns the last unicode symbol in the official Blissymbols decoding.

        :return: str, unicode for last Blissymbol decoded
        """
        return sorted(self.translator.get_unicode_to_bliss())[-1]

    def set_pos(self, pos):
        """
        Sets this Blissymbol's parts of speech to pos.

        :param pos: List[str], list of Penn Treebank parts of speech
        :return: None
        """
        self.pos = pos

    def bliss_image(self, max_width=None, max_height=None):
        """
        Returns the Image for this Blissymbol, with a
        maximum width of max_width and maximum height of max_height.

        :param max_width: Optional[int], maximum width of output image
        :param max_height: Optional[int], maximum height of output image
        :return: Image, image of this Blissymbol with given dimensions
        """
        return get_bliss_img(self.bliss_name, max_width=max_width, max_height=max_height)

    def pluralize_image(self, img):
        """
        Returns this Blissymbol img with a plural indicator.

        :param img: Image, Blissymbol image to pluralize
        :param max_width: Optional[int], maximum width of output image
        :param max_height: Optional[int], maximum height of output image
        :return: Image, input image pluralized
        """
        plural = get_bliss_img("indicator_(plural)", img.size[0], img.size[1])
        return overlay(img, plural)

    def is_punct(self):
        """
        Returns True if this Blissymbol is a punctuation symbol.

        :return: bool, whether this Blissymbol is punctuation
        """
        return self.bliss_name in self.PUNCT_MAP.values()

    def valid_filename(self):
        """
        Returns True if this Blissymbol's img_filename can be opened,
        False otherwise.

        :return: bool, whether img_filename can be opened
        """
        try:
            open(IMG_PATH + self.img_filename)
        except IOError:
            return False
        else:
            return True

    def check_img_filename(self):
        """
        If this Blissymbol's img_filename cannot be opened,
        attempts to create a new image from this Blissymbol's derivations.
        If successful, saves this new image as img_filename.

        :return: None
        """
        if not self.valid_filename():
            for name in self.bliss_name.split(","):
                filename = name + ".png"
                try:
                    open(IMG_PATH + filename)
                except IOError:
                    continue
                else:
                    self.img_filename = filename
                    break
            else:
                print("couldn't open file: " + self.img_filename + str(self.derivations))

            if len(self.derivations) != 0:
                self.make_new_blissymbol(self.derivations, self.img_filename)

    def count_indicators(self):
        count = 0
        for deriv in self.derivations:
            if self.is_indicator(deriv):
                count += 1
        return count

    def derivation_blissymbols(self, blissymbol, atomic=True):
        """
        Returns a list of Blissymbols for this Blissymbol's derivation.
        ~
        If atomic is True, returns all atomic Blissymbols part of this
        Blissymbol's derivation.  Otherwise, returns only this Blissymbol's
        immediate derivations as Blissymbols.
        ~
        e.g. bs = Blissymbol("rabbit,hare.png", derivation="(rodent + ear)"])

             derivation_blissymbols(bs, False) -> [Blissymbol("rodent"), Blissymbol("ear")]
             derivation_blissymbols(bs, True) -> [Blissymbol("animal"), Blissymbol("teeth"), Blissymbol("ear")]

        :param blissymbol: Blissymbol, to find derivative Blissymbols for
        :param atomic: bool, whether to return only atomic Blissymbol derivations
        :return: List[Blissymbol], this Blissymbol's derivative Blissymbols
        """
        bliss_derivatives = list()

        if blissymbol.is_atom or len(blissymbol.derivations) == 1:
            bliss_derivatives.append(blissymbol)
            return bliss_derivatives
        else:
            for derivation in blissymbol.derivations:
                deriv_bliss = self.translator.word_to_blissymbol(derivation)

                if deriv_bliss is None:  # if derivation has no characters, return this Blissymbol
                    bliss_derivatives.append(deriv_bliss)
                    return bliss_derivatives
                elif blissymbol == deriv_bliss or deriv_bliss in bliss_derivatives:
                    continue
                else:
                    if atomic:
                        bliss_derivatives += self.derivation_blissymbols(deriv_bliss, atomic)
                    else:
                        bliss_derivatives.append(blissymbol)

            if len(bliss_derivatives) == 0:
                bliss_derivatives.append(blissymbol)

            return bliss_derivatives

    def make_new_blissymbol(self, derivations, filename):
        """
        Given a list of derivations for a Blissymbol,
        combines derivations to make a new Blissymbol image
        and returns the result.
        ~
        Saves the resulting image under this filename.

        :param derivations: List[str], derivative Blissymbol(s)
        :param filename: str, filename to save Blissymbol under
        :return: Image, new Blissymbol image from derivations
        """
        if filename is None:
            filename = self.img_filename

        bliss_imgs = []
        indicators = []
        width = 0
        space = 2

        for derivation in self.derivations:
            blissymbol = self.translator.word_to_blissymbol(derivation)

            if blissymbol is not None:
                bliss_name = blissymbol.bliss_name
                bliss_img = get_bliss_img(bliss_name)
            else:
                print("couldn't find Blissymbol derivation for " + derivation + "...")
                continue

            if blissymbol.is_indicator(blissymbol.bliss_name):
                indicators.append(bliss_img)
            else:
                bliss_imgs.append(bliss_img)
                width += bliss_img.size[0] + space

        if len(bliss_imgs) != 0:
            width -= space  # remove trailing whitespace
            height = max(bliss_imgs, key=lambda bw: bw.size[1]).size[1]

            img = Image.new("RGBA", (width, height))
            curr_width = 0

            for bliss_img in bliss_imgs:
                img.paste(bliss_img, (curr_width, 0))
                curr_width += space + bliss_img.size[0]

            if len(indicators) != 0:
                all_indicators = indicators[0]

                for i in range(1, len(indicators)):
                    indicator = indicators[i]
                    all_indicators = beside(all_indicators, indicator)

                img = overlay(all_indicators, img)

            filename = self.translator.deunicodize(filename)
            img_path = str(IMG_PATH + filename)
            img.save(img_path)
            print("made new Blissymbol: " + filename)
            print("with the derivations " + " ".join([d for d in derivations]))
            NEW_BLISSYMBOLS.append(img_path)
            return img

    def add_translation(self, language, translation):
        """
        Adds this translation to self.translations
        under this language.

        e.g. add_translation("Polish", "kot") ->
             self.translations == {"Polish": ["kot"]}

             add_translation("French", "chat") ->
             self.translations == {"Polish": ["kot"],
                                   "French": ["chat"]}

        :param language: str, language of this translation
        :param translation: str, Blissymbol translation in language
        :return: None
        """
        self.translations.setdefault(language, [])
        self.translations[language].append(translation)
        self.translations[language] = self.translator.remove_duplicates(self.translations[language])

    def add_translations(self, language, translations):
        """
        Adds these translations to self.translations
        under this language.

        e.g. add_translation("Polish", ["kot", "kotka"]) ->
             self.translations == {"Polish": ["kot", "kotka"]}

             add_translation("French", ["chat", "chatton"]) ->
             self.translations == {"Polish": ["kot", "kotka"],
                                   "French": ["chat", "chatton"]}

        :param language: str, language of this translation
        :param translation: List[str], Blissymbol translations in language
        :return: None
        """
        if len(translations) != 0:
            self.translations.setdefault(language, list())
            for translation in translations:
                self.add_translation(language, translation)

    def get_derivation(self):
        """
        Returns this Blissymbol's source derivation as a string.

        :return: str, this Blissymbol's source derivation
        """
        return unicode(self.derivation)

    def set_derivation(self, derivation):
        """
        Sets this Blissymbol's derivation to this derivation.

        :param derivation: str, derivation of Blissymbol
        :return: None
        """
        self.derivation = derivation

    def find_derivations(self):
        """
        Returns a list of the Blissymbols from which this
        Blissymbol is derived.

        :return: List[str], list of this Blissymbol's derivations
        """
        if self.bliss_name in self.translator.lex_parser.init_derivations():
            return self.translator.lex_parser.init_derivations()[self.bliss_name]
        elif self.is_atom:
            return [self.bliss_name]
        elif self.derivation == "":
            return []
        else:
            deriv = self.translator.extract_parens(self.derivation, starts={"("}, ends={")"})
            if ":" in deriv:
                deriv = deriv.split(":")[0]
            deriv = self.translator.remove_parens(deriv, starts={"["}, ends={"]"})
            derivations = [d.split(", ")[0].strip() for d in deriv.split(" + ")]
            print "\t", self, "has derivations:\t", derivations
            return derivations

    def set_derivations(self, derivations):
        """
        Sets this Blissymbol's derivations to derivations.

        :param derivation: List[str], derivations of Blissymbol
        :return: None
        """
        self.derivations = derivations

    def is_derivation(self, word):
        """
        Returns True if this word is in this Blissymbol's derivations,
        False otherwise.

        :return: List[str], derivations of Blissymbol
        """
        return word in self.derivations

    def get_subsymbols(self):
        """
        Returns this Blissymbol's constituent atomic Blissymbols.
        ~
        Differs from derivations in that this method
        returns a list of the bottommost derivations.
        ~
        e.g. rabbit == rodent + ear == (animal + teeth) + ear

        :return: List[Blissymbol], derivations of Blissymbol
        """
        subderivations = []

        for derivation in self.derivations:
            subderivation = self.find_subsymbols(derivation)
            subderivations += subderivation

        return subderivations

    def find_subsymbols(self, derivation):
        """
        Returns this Blissymbol's atomic derivations.
        ~
        Differs from derivations in that this method
        returns a list of the bottommost derivations.

        :param derivation: str, derivation to derive subderivations from
        :return: List[Blissymbol], derivations of Blissymbol
        """
        atoms = []
        blissymbol = self.translator.word_to_blissymbol(derivation)

        if blissymbol is None:
            return atoms
        else:
            if blissymbol.get_is_atom():
                atoms.append(blissymbol)
                return atoms
            else:
                derivs = blissymbol.derivations

                if len(derivs) == 1:
                    atoms.append(blissymbol)
                    return atoms
                else:
                    for deriv in derivs:
                        if deriv not in blissymbol.derivations:
                            atoms += blissymbol.find_subsymbols(deriv)
                        else:
                            break
                    return atoms

    def clean_defn(self, defn):
        """
        Replaces input defn's underscores with spaces and
        strips whitespace from ends.  Returns result.

        :param defn: str, word definition to clean
        :return: str, cleaned word definition
        """
        new_defn = defn.replace("_", " ")
        new_defn = new_defn.strip()
        return new_defn

    def clean_translation(self, translation):
        """
        Returns this list of translation definitions
        with spaces instead of underscores and no parenthesis
        phrase.
        ~
        Allows for more direct comparisons between input and
        Blissymbol translations.

        :param translation: List[str], input translations to clean
        :return: List[str], cleaned translations
        """
        clean_translation = []
        for t in translation:
            cleaned = self.clean_defn(t.split("(")[0])
            if len(cleaned) != 0 and cleaned not in clean_translation:
                clean_translation.append(cleaned)
        return clean_translation

    def clean_translations(self, translations):
        """
        Returns this dictionary of translations with
        each translation cleaned, i.e. with spaces instead
        of underscores and no parenthesis phrase.

        :param translations: dict, where...
            key (str) - language of translations
            val (List[str]) - uncleaned Blissymbol translations in language
        :return: dict, where...
            key (str) - language of translations
            val (List[str]) - cleaned Blissymbol translations in language
        """
        languages = translations
        translations = {language: self.clean_translation(translations[language]) for language in languages}
        return translations

    def get_img_filename(self):
        """
        Returns image filename associated with this Blissymbol.

        :return: str, this Blissymbol's image filename
        """
        return self.img_filename

    def get_pos_code(self):
        """
        Return this Blissymbol's part-of-speech colour code.

        :return: str, Blissymbol's part-of-speech colour code
        """
        return self.pos_code

    def get_pos(self):
        """
        Return first part-of-speech in this Blissymbol's
        parts-of-speech list.

        :return: str, Blissymbol's part-of-speech
        """
        if self.pos is not None:
            return self.pos[0]

    def get_parts_of_speech(self):
        """
        Return this Blissymbol's parts-of-speech list.

        :return: List[str], Blissymbol's parts-of-speech
        """
        return self.pos

    def get_parens(self, word):
        """
        Returns parenthetical(s) from this word.
        ~
        Parenthetical begins at the first open parenthesis.

        e.g. get_parens("English_(language)") -> "(language)"

        :param word: str, word to get parenthetical from
        :return: str, this word's parenthetical phrase
        """
        idx = 0
        for char in word:
            if char != "(" and char != "[":
                idx += 1
            else:
                return word[idx:]
        return None

    def is_neutral(self):
        """
        Returns True if this Blissymbol neutral, i.e.
        if it does not have gender (feminine or masculine) and isn't plural.

        :return: bool, whether this Blissymbol is neutral
        """
        if self.paren_phrase is None:
            return True
        else:
            start = self.paren_phrase[1:5]
            return not (start == "femi" or start == "masc" or start == "plur")

    def remove_parens(self, word):
        """
        Removes parenthetical(s) from this word and
        returns the result.
        ~
        Parenthetical begins at the first open parenthesis.

        e.g. get_parens("English_(language)") -> "English"

        :param word: str, word to get parenthetical from
        :return: str, this word's parenthetical phrase
        """
        return self.translator.remove_parens(word)

    def get_translation(self, language=None):
        """
        If self.translations contains a translation in
        this language, returns translations in that language.
        ~
        Otherwise, returns translations in this Blissymbol's
        native language.

        :param language: str, language to get translations in
        :return: List[str], Blissymbol translations in this language
        """
        try:
            return self.translations[language]
        except KeyError:
            return []

    def get_translations(self):
        """
        Returns this Blissymbol's translations dict.

        :return: dict, where...
            key (str) - language name (in English)
            val (List[str]) - Blissymbol translations in English
        """
        return self.translations

    def set_img_filename(self, img_filename):
        """
        Sets this Blissymbol's img_filename to this img_filename.
        ~
        Assumes img_filename includes appropriate extension (.png).

        :param img_filename: str, image filename (ending in .png)
        :return: None
        """
        self.img_filename = img_filename

    def set_paren_phrase(self, paren_phrase):
        """
        Sets this Blissymbol's parenthesis phrase to
        this paren_phrase.

        :param paren_phrase: str, phrase in parentheses
        :return: None
        """
        self.paren_phrase = paren_phrase

    def init_pos(self, pos):
        """
        Sets this Blissymbol's pos to this pos,
        unless Blissymbol appears to be a different
        part of speech.

        :param pos: str, this Blissymbol's part of speech
        :return: List[str], this Blissymbol's parts of speech
        """
        poses = list()

        if self.get_parens(self.bliss_name) == "(to)":
            # all verbs have (to) indicator
            poses = self.POS_COLOUR_CODE["RED"]
        elif pos is not None:
            try:
                poses = self.POS_COLOUR_CODE[pos]
            except KeyError:
                if pos in self.PARTS_OF_SPEECH:
                    poses = [pos]
                if len(pos) > 2:
                    poses = [pos[:2]]

        return poses

    def init_pos_code(self, pos_code):
        """
        Sets this Blissymbol's pos_code to this pos_code,
        unless pos_code is not in POS_COLOUR_CODE.

        :param pos_code: str, this Blissymbol's part of speech colour code
        :return: None
        """
        if self.get_parens(self.bliss_name) == "(to)":
            # all verbs have (to) indicator
            self.pos_code = "RED"
        elif pos_code is not None:
            try:
                self.POS_COLOUR_CODE[pos_code]
            except KeyError:
                self.pos_code = self.find_pos_colour(pos=pos_code)
            else:
                self.pos_code = pos_code

    def find_pos_colour(self, pos):
        """
        Given a pos, returns the corresponding pos colour code.

        :param pos: str, this Blissymbol's part of speech
        :return: str, pos_code
        """
        assert pos not in self.POS_COLOUR_CODE
        for colour in self.POS_COLOUR_CODE:
            if pos in self.POS_COLOUR_CODE[colour]:
                return colour

    @staticmethod
    def find_colour_pos(colour):
        """
        Given a colour, returns the corresponding pos.

        :param colour: str, a Blissymbol's part of speech colour
        :return: List[str], parts of speech for the given colour
        """
        return Blissymbol.POS_COLOUR_CODE[colour]

    def get_is_atom(self):
        """
        Returns whether this Blissymbol is atomic.
        ~
        is_atom is True when a Blissymbol is atomic, False otherwise.

        :return: bool, whether this Blissymbol is atomic
        """
        return self.is_atom

    def find_is_atom(self):
        """
        Identifies whether this Blissymbol is atomic or not.
        ~
        is_atom is True when a Blissymbol is atomic, False otherwise.
        ~
        N.B. Only specified Blissymbols are atomic, all others are non-atomic.
             All characters with derivations ending in "Character" are atomic.

        :return: bool, whether this Blissymbol is atomic
        """
        derivations = self.derivation.lstrip("(").rstrip(")").split(":")

        if len(derivations) == 1 and derivations[0] == self.bliss_name:
            return True
        elif derivations[0][:10] == "pictograph":
            return True

        derivation = derivations[-1]
        derivation = derivation.strip()
        is_character = (derivation[:9] == "Character")

        if is_character:
            derivation = "".join(derivations[:-1])
            derivation = derivation.strip()
            self.set_derivation(derivation)

        return is_character

    def set_is_atom(self, is_atom):
        """
        Sets this Blissymbol's is_atom value to is_atom.

        :param is_atom: bool, whether this Blissymbol is atomic
        :return: None
        """
        self.is_atom = is_atom

    def get_unicode(self):
        """
        Returns this Blissymbol's unique unicode identifier.

        :return: str, this Blissymbol's unicode ID
        """
        return self.unicode

    def get_deriv_unicode(self, atomic=True):
        """
        Returns a list of this Blissymbol's derivations' unicode
        identifiers.

        :return: List[str], this Blissymbol's derivations' unicode IDs
        """
        return [self.unicode] if self.is_atom else self.find_deriv_unicode(atomic=atomic)

    def add_unicode_to_bliss(self, uni, bliss):
        """
        Adds this unicode key to this Blissymbol's
        BlissTranslator's unicode-to-Blissymbol dict,
        with blissymbol name bliss as its value.

        :param uni: str, unicode name to add
        :param bliss: str, name of blissymbol for this unicode
        :return: None
        """
        self.translator.add_unicode_to_bliss(uni, bliss)

    def add_bliss_to_unicode(self, bliss, uni):
        """
        Adds this blissymbol key bliss to this Blissymbol's
        BlissTranslator's Blissymbol-to-unicode dict,
        with unicode as its value.

        :param bliss: str, name of blissymbol to add
        :param unicode: str, unicode name for this bliss
        :return: None
        """
        self.translator.add_bliss_to_unicode(bliss, uni)

    def add_bliss_unicode(self, uni, bliss):
        """
        Adds this unicode key to this Blissymbol's
        BlissTranslator's unicode-to-Blissymbol dict,
        with blissymbol name bliss as its value.

        :param uni: str, unicode name to add
        :param bliss: str, name of blissymbol for this unicode
        :return: None
        """
        self.translator.add_bliss_unicode(uni, bliss)

    def add_bliss_and_unicode(self, bliss="", uni=""):
        """
        Adds this Blissymbol string bliss and its corresponding
        unicode symbol unicode to bliss_to_unicode dict as well as
        unicode_to_bliss dict.
        ~
        If bliss or unicodes are left empty, this method sets bliss to
        this Blissymbol's name and unicode to the next unicode character
        in the series.

        :param bliss: str, name of blissymbol to add
        :param uni: str, unicode name for this bliss
        :return: None
        """
        if bliss == "":
            bliss = self.bliss_name
        if uni == "":
            uni = self.unicode

        self.add_bliss_to_unicode(bliss, uni)
        self.add_unicode_to_bliss(uni, bliss)

    def add_blissymbol_unicodes(self, blissymbol):
        """
        Adds all translations for this Blissymbol to the
        Blissymbol encoding and decoding dictionaries.

        :param blissymbol: Blissymbol, entry to encoding/decoding dicts
        :return: None
        """
        uni = blissymbol.unicode
        self.add_bliss_unicode(uni, blissymbol.bliss_name)

        for bliss in blissymbol.get_translation("English"):
            self.add_bliss_and_unicode(bliss, uni)

    def new_unicode(self):
        """
        Returns a new unicode name for a Blissymbol and
        adds to encoding dicts accordingly.

        :return: str, new unicode name
        """
        print "\tlast unicode:", hex(self.last_encoding)[2:]
        self.last_encoding += 1
        print "\tnew unicode:", hex(self.last_encoding)[2:]
        uni = hex(self.last_encoding)
        uni = "U+" + uni[2:]
        return uni

    def derivations_synonyms(self, derivations):
        """
        Returns a list of all Blissymbol derivations split by commas.

        :param derivations: List[str], derivations for a Blissymbol
        :return: List[str], derivations split by commas
        """
        synonyms = []
        for derivation in derivations:
            synonyms += derivation.split(",")
        return synonyms

    def is_indicator(self, blissname):
        return blissname[:9] == "indicator"

    def clean_derivation_synonym(self, deriv_synonym):
        """
        Returns this Blissymbol's deriv_synonym cleaned.

        :param deriv_synonym: str, synonym for a Blissymbol's derivation
        :return: str, derivation synonym cleaned
        """
        if self.is_indicator(deriv_synonym):
            deriv_synonym = deriv_synonym.replace("(", "")
            deriv_synonym = deriv_synonym.replace(")", "")
        deriv_synonym = deriv_synonym.replace("_", " ")
        deriv_synonym = self.remove_parens(deriv_synonym)
        return deriv_synonym

    def find_deriv_unicode(self, atomic=True):
        """
        Returns a list of unicode strings corresponding to
        the Blissymbol translations of this Blissymbol's
        derivations.
        ~
        N.B. If this Blissymbol is atomic, then its
        deriv_unicodes will be equivalent to its unicode.

        :return: List[str], unicodes for this Blissymbol's
            derivations
        """
        return [db.unicode for db in self.derivation_blissymbols(atomic=atomic)]

    def get_unicode_pos(self):
        """
        If this Blissymbol is not atomic, returns unicode name
        for this Blissymbol's part of speech.

        :return: str, unicode representation of part of speech
        """
        if not self.is_atom:
            try:
                indicator = self.translator.bliss_to_uni[self.pos_to_indicator(self.get_pos())]
            except KeyError:
                return ""
            else:
                return indicator

    def pos_to_indicator(self, pos):
        """
        Returns unicode name for this part of speech.

        :return: str, part-of-speech to get indicator name for
        :return: str, Blissymbol indicator name for this pos
        """
        if pos in self.POS_COLOUR_CODE["BLUE"]:
            return "indicator thing"
        elif pos in self.POS_COLOUR_CODE["GREEN"]:
            return "indicator description"
        elif pos in self.POS_COLOUR_CODE["RED"]:
            return "indicator action"

    def has_unicode(self):
        """
        Returns True if this Blissymbol has a corresponding
        unicode value, False otherwise.

        :return: bool, whether this Blissymbol has a unicode
        """
        return self.unicode is not None

    def init_unicode(self):
        """
        Initializes this Blissymbol's unicode to
        its definition's unicode.

        :return: str, unicode for this Blissymbol
        """
        unicodes = self.translator.init_bliss_unicode()

        for u in unicodes:
            blissname = unicodes[u]
            if self.bliss_name == blissname:
                uni = u
                break
        else:
            uni = self.new_unicode()

        self.set_unicode(uni)
        self.add_blissymbol_unicodes(self)
        return uni

    def add_synset(self, synset):
        """
        Adds this synset to this Blissymbol's synsets.

        :param synset: Synset, synset to add to synsets
        :return: None
        """
        self.synsets.add(synset)

    def add_synsets(self, synsets):
        """
        Updates this Blissymbol's synsets with this synsets.

        :param synsets: List[Synset], synsets to add to synsets
        :return: None
        """
        self.synsets.update(synsets)

    def init_blissymbol_synsets(self):
        """
        Returns a list of English Wordnet synsets corresponding
        to this Blissymbol.

        :return: Set(Synset), this Blissymbol's Wordnet synsets
        """
        synsets = self.lookup_blissymbol_synsets(self)
        try:
            self.synset = synsets[0]
        except IndexError:
            pass
        return set(synsets)

    def lookup_blissymbol_synsets(self, blissymbol):
        """
        Returns a list of Wordnet Synsets corresponding to
        this Blissymbol.

        :param blissymbol: Blissymbol, blissymbol to lookup synset for
        :return: List[Synset], synsets corresponding to blissymbol
        """
        if blissymbol.has_unicode():
            uni = blissymbol.unicode
            synsets = self.translator.lookup_blissnet(uni)
            if synsets is not None:
                return synsets
        return []

    def find_blissymbol_synsets(self):
        """
        Returns a list of English Wordnet synsets corresponding
        to this Blissymbol.

        :return: Set[Synset], this Blissymbol's Wordnet synsets
        """
        synsets = set()
        translations = self.get_translations()
        word = self.bliss_name
        word = word.replace("_", " ")
        words = word.split(",")
        pos = self.get_pos()

        if len(words) > 0:
            word_synsets = set()
            lang_synsets = set()

            for word in words:
                word = self.remove_parens(word)
                word = word.rstrip("_")
                word_synset = self.translator.lookup_word_synsets(word, pos)
                word_synsets.update(word_synset)

            for lang in translations:
                if lang != "English":
                    translation = translations[lang]
                    lang_synset = set()

                    for defn in translation:
                        synset = self.translator.lookup_word_synsets(defn, pos, language=lang)
                        if synset is None:
                            lang = False
                            break
                        else:
                            lang_synset.update(synset)
                    if not lang:
                        continue

                    if len(lang_synset) != 0:
                        if len(lang_synsets) != 0:
                            lang_synsets.intersection_update(lang_synset)
                        else:
                            lang_synsets.update(lang_synset)

            synset = lang_synsets.intersection(word_synsets)

            if len(synsets) == 0:
                synsets = synset
            else:
                synsets.update(synset)

            if len(synsets) == 0:
                synsets.update(word_synsets.union(lang_synsets))

        if self.synset is None and len(synsets) != 0:
            self.synset = list(synsets)[0]
        if self.synset is not None:
            pos = self.synset.pos()
            self.set_pos(self.init_pos(pos))

        return synsets

    def clean_bliss_name(self):
        return self.bliss_name.replace("_", " ")

    def set_unicode(self, unicode):
        """
        Sets this Blissymbol's unicode to unicodes.
        ~
        Each unicode str in unicodes follow the regex:
            U+[A-F|0-9]{4}

        :param unicodes: str, list of unicodes
        :return: None
        """
        self.unicode = unicode

    def set_bliss_glyph(self):
        """
        Creates a BlissGlyph for this Blissymbol according to
        its part of speech and derivations.
        ~
        If Blissymbol is atomic, BlissGlyph is 1 atomic bliss unit.
        ~
        Sets this Blissymbol's bliss_glyph to created BlissGlyph.

        :return: None
        """
        glyph = BlissGlyph()
        pos = self.get_pos()

        if self.is_atom:
            glyph.set_bliss_unit(self.bliss_name)
            return
        else:
            for derivn in self.derivations:
                glyph.add_bliss_unit(derivn)

        if pos == 'NN':
            glyph.add_ultra_zone("indicator thing")
        elif pos == 'VB':
            glyph.add_ultra_zone("indicator action")
        elif pos == 'RB' or pos == 'JJ':
            glyph.add_ultra_zone("indicator description")

    def __eq__(self, other):
        return self.bliss_name == other.bliss_name

    def __hash__(self):
        return hash(self.bliss_name)

    def __str__(self):
        return self.bliss_name

    __repr__ = __str__


class BlissAlphabet:
    """
    A class for holding BlissGlyph elements.
    """
    def __init__(self):
        pass
        #self.lex_parser = LexiconParser()
        #self.bliss_atoms = self.lex_parser.init_blissymbols()
    
    
class BlissIndicator:
    INDICATORS = {
        # PARTS OF SPEECH
        "verb": "indicator_(action)",
        "noun": "indicator_(thing)",
        "plural noun": "indicator_(things)",
        "adverb": "indicator_(adverb)",
        "plural": "indicator_(plural)",

        # NOUNS
        # --> definiteness
        "definite": "indicator_(definite_form)",
        "indefinite": "indicator_(indefinite_form)",
        # --> possession
        "possessive": "indicator_(possessive_form)",

        # VERBS
        # --> grammatical forms
        "imperative": "indicator_(imperative_form)",
        "imperfective": "indicator_(continuous_form)",
        "imperfect": ["indicator_(past_action)", "indicator_(continuous_form)"],
        # --> tense
        "past": "indicator_(past_action)",
        "present": "indicator_(present_action)",
        "future": "indicator_(future_action)",
        # --> conditional
        "past conditional": "indicator_(past_conditional)",
        "conditional": "indicator_(conditional)",
        "future conditional": "indicator_(future_conditional)",
        # --> active/passive
        "active": "indicator_(active)",
        "past passive": "indicator_(past_passive)",
        "passive": "indicator_(passive)",
        "future passive": "indicator_(future_passive)",
        # --> passive conditional
        "past passive conditional": "indicator_(past_passive_conditional)",
        "present passive conditional": "indicator_(present_passive_conditional)",
        "future passive conditional": "indicator_(future_passive_conditional)",
        # --> participles
        "past participle": "indicator_(past_participle_1)",
        "present participle": "indicator_(present_participle)",

        # ADJECTIVES
        # "": "indicator_(description_before_fact)",
        "adjective": "indicator_(description)",
        # "": "indicator_(description_after_fact)",

        # ASPECTS
        # --> person
        "first person": "indicator_(first_person)",
        "second person": "indicator_(second_person)",
        "third person": "indicator_(third_person)",
        # --> gender
        "diminutive": "indicator_(diminutive_form)",
        "feminine": "indicator_(female)",
        "neutral": "indicator_(neutral_form)",
        "object": "indicator_(object_form)",

        # BLISS-SPECIFIC
        "combination": "indicator_(combine)"
    }


class BlissGlyph:
    """
    A class for representing Bliss glyphs in a grid.
    ~
    Each BlissGlyph contains list attributes corresponding to the
    following grid layout:

    http://tecfa.unige.ch/guides/3dprinting/bliss/blisssym-grid.html
    ~
    The first element of middle_zones defines the main BLISS_UNIT.
    """
    HEIGHTS = {0: "descender limit",
               1: "earthline",
               2: "middle earth line",
               3: "midline",
               4: "middle sky line",
               5: "skyline",
               6: "indicator limit",
               7: "tall indicator limit"}
    GLYPH_HEIGHT = len(HEIGHTS)
    ZONE_HEIGHTS = 2    # each zone takes up 2x2 blocks
    UNIT_WIDTH = 4      # each atomic Blissymbol takes up 4 width units

    def __init__(self, bliss_unit=list(), sky_zones=list(),
                 middle_zones=list(), earth_zones=list(),
                 ultra_zones=list(), infra_zones=list()):
        self.bliss_unit = bliss_unit        # takes up sky/middle/earth zone
        self.ultra_zones = ultra_zones      # holds indicators
        self.sky_zones = sky_zones
        self.middle_zones = middle_zones
        self.earth_zones = earth_zones
        self.infra_zones = infra_zones      # holds descenders

    def set_bliss_unit(self, bliss_unit):
        self.bliss_unit = bliss_unit

    def set_sky_zones(self, sky_zones):
        self.sky_zones = sky_zones

    def set_middle_zones(self, middle_zones):
        self.middle_zones = middle_zones

    def set_earth_zones(self, earth_zones):
        self.earth_zones = earth_zones

    def set_ultra_zones(self, ultra_zones):
        self.ultra_zones = ultra_zones

    def set_infra_zones(self, infra_zones):
        self.infra_zones = infra_zones

    def add_bliss_unit(self, bliss_unit):
        self.bliss_unit.append(bliss_unit)

    def add_sky_zone(self, sky_zones):
        self.sky_zones.append(sky_zones)

    def add_middle_zone(self, middle_zone):
        self.middle_zones.append(middle_zone)

    def add_earth_zone(self, earth_zone):
        self.earth_zones.append(earth_zone)

    def add_ultra_zone(self, ultra_zone):
        self.ultra_zones.append(ultra_zone)

    def add_infra_zone(self, infra_zone):
        self.infra_zones.append(infra_zone)

    def get_bliss_unit(self):
        return self.bliss_unit

    def get_sky_zones(self):
        return self.sky_zones

    def get_middle_zones(self):
        return self.middle_zones

    def get_earth_zones(self):
        return self.earth_zones

    def get_ultra_zones(self):
        return self.ultra_zones

    def get_infra_zones(self):
        return self.infra_zones
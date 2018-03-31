# -*- coding: utf-8 -*-
"""
BLISSYMBOLS:

    Contains a class for representing a Blissymbol, either
    created from a language-to-Blissymbols dictionary file or
    by a user.
"""
from bliss_images import *

LAST_BLISS_ENCODING = int("3576", 16)
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

    def __init__(self, img_filename=None, pos=None, derivation="", translations=None, translator=None):
        self.translator = translator
        self.img_filename = img_filename
        self.bliss_name = self.img_filename[:-4]
        self.pos_code = pos
        self.init_pos_code(pos)
        self.pos = pos
        self.init_pos(pos)
        self.paren_phrase = self.get_parens(self.bliss_name)
        self.derivation = derivation
        self.is_atom = bool
        self.init_is_atom()
        self.derivations = self.find_derivations()
        self.check_img_filename()  # creates new blissymbol image from derivations if none exists
        self.translations = self.clean_translations(translations)  # hold translations in different languages
        self.bliss_glyph = None
        self.unicode = str()
        self.deriv_unicode = list()
        self.init_unicode()
        self.init_deriv_unicode()
        self.synset = None
        self.synsets = self.init_blissymbol_synsets()
        if self.valid_filename():
            self.translator.add_bliss_entry(self)

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
                print("couldn't open file: " + self.img_filename)

            if len(self.derivations) != 0:
                self.make_new_blissymbol(self.derivations, self.img_filename, self.get_pos())

    def make_new_blissymbol(self, derivations, filename, pos=""):
        """
        Given a list of derivations for a Blissymbol,
        combines derivations to make a new Blissymbol image
        and returns the result.
        ~
        Saves the resulting image under this filename.

        :param derivations: List[str], derivative Blissymbol(s)
        :param filename: str, filename to save Blissymbol under
        :param pos: str, indicator Blissymbol to append at end of image
        :return: Image, new Blissymbol image from derivations
        """
        if filename is None:
            filename = self.img_filename

        bliss_imgs = []
        width = 0
        space = 2

        for derivation in derivations:
            blissymbol = self.translator.word_to_blissymbol(derivation)
            if blissymbol is not None:
                bliss_name = blissymbol.bliss_name
                bliss_img = get_bliss_img(bliss_name)
            else:
                print("couldn't find Blissymbol derivation for " + derivation + "...")
                continue
            bliss_imgs.append(bliss_img)
            width += bliss_img.size[0] + space

        if len(bliss_imgs) != 0:
            width -= space  # remove trailing whitespace
            height = max(bliss_imgs, key=lambda bw: bw.size[1]).size[1]

            if len(pos) != 0:
                indicator = self.pos_to_indicator(pos)
                bliss_img = get_indicator_bliss_img(indicator)
                width += space + bliss_img.size[0]
                bliss_imgs.append(bliss_img)

            img = Image.new("RGBA", (width, height))
            curr_width = 0

            for bliss_img in bliss_imgs:
                img.paste(bliss_img, (curr_width, 0))
                curr_width += space + bliss_img.size[0]

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
        return str(self.derivation)

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
        if self.is_atom:
            return [self.bliss_name]
        elif self.derivation == "":
            return []
        else:
            # TODO: clean this up, a lot
            deriv = self.derivation
            deriv = deriv.replace("\n", "")
            deriv = deriv.replace(";", ":")
            deriv = deriv.replace("+", " + ")
            deriv = deriv.replace("  ", " ")
            derivs = deriv.split(":")
            deriv = derivs[0]

            if deriv[0] == "(":
                deriv = deriv[1:]
            else:
                start = 0
                in_parens = False
                while deriv[start] != "(" or in_parens:
                    try:
                        deriv[start+1]
                    except IndexError:
                        start = None
                        break
                    else:
                        if deriv[start] == "(" or deriv[start] == "[":
                            in_parens = True
                        elif in_parens and (deriv[start] == ")" or deriv[start] == "]"):
                            in_parens = False
                        elif in_parens and deriv[start] == ",":
                            deriv = deriv[:start] + "@" + deriv[start+1:]
                        start += 1
                deriv = deriv[start:]

            end = 0
            in_parens = False
            while (deriv[end] != ")" or in_parens) and deriv[end] != ":":
                try:
                    deriv[end+1]
                except IndexError:
                    end = None
                    break
                else:
                    if deriv[end] == "(" or deriv[end] == "[":
                        in_parens = True
                    elif in_parens and (deriv[end] == ")" or deriv[end] == "]"):
                        in_parens = False
                    elif in_parens and deriv[end] == ",":
                        deriv = deriv[:end] + "@" + deriv[end+1:]
                    end += 1

            deriv = deriv[:end]
            deriv = deriv.replace("@", "")

            derivs_itn = deriv.split(" ")
            derivs = derivs_itn

            derivations = []
            start = 0
            end = 1

            for d in derivs_itn:
                if d == ":" or d == "-":
                    break
                elif d == "":
                    continue
                else:
                    d = d.strip()
                    if d == "indicator":
                        derivations.append(d + " (" + " ".join(derivs[start:end-1]) + ")")
                        start = end
                    elif d == "+":
                        blissymbol = " ".join(derivs[start:end-1])
                        derivations.append(blissymbol)
                        start = end
                    elif (end+1)>len(derivs):
                        derivs[end-1] = self.clean_defn(derivs[end - 1])
                        blissymbol = " ".join(derivs[start:])
                        if blissymbol[-2:] == "))":
                            blissymbol = blissymbol[:-1]
                        derivations.append(blissymbol)
                    elif d != "":
                        derivs[end-1] = self.clean_defn(derivs[end - 1])
                    end += 1

            return [d.strip() for d in derivations]

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
        translation = [self.remove_parens(self.clean_defn(t)) for t in translation]
        return self.translator.remove_duplicates(translation)

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

    '''
    GET/SET LANGUAGE FUNCTIONS
    --------------------------
    Intended for (future) Blissymbol creation solely in 1 language
    (e.g. for "untranslatable" words).
    
    def get_language(self):
        """
        Returns this Blissymbol's language.
        ~
        N.B. Every Blissymbol's native language is English.

        :return: str, this Blissymbol's language (English)
        """
        return str(self.language)

    def set_language(self, language):
        """
        Sets this Blissymbol's default language to this language.
        ~
        Default language should be set to whichever language the
        Blissymbol names are being entered in.
        ~
        N.B. Default language should always be English for now.

        :param language: str, this Blissymbol's working language
        :return: None
        """
        self.language = language
    '''

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
        :return: None
        """
        if self.get_parens(self.bliss_name) == "(to)":
            # all verbs have (to) indicator
            self.pos = self.POS_COLOUR_CODE["RED"]
        elif pos is not None:
            try:
                self.pos = self.POS_COLOUR_CODE[pos]
            except KeyError:
                if pos in self.PARTS_OF_SPEECH:
                    self.pos = [pos]
                if len(pos) > 2:
                    self.pos = [pos[:2]]

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
                self.pos_code = self.find_pos_code(pos=pos_code)
            else:
                self.pos_code = pos_code

    def find_pos_code(self, pos):
        """
        Given a pos, returns the corresponding pos colour code.

        :param pos: str, this Blissymbol's part of speech
        :return: str, pos_code
        """
        assert pos not in self.POS_COLOUR_CODE
        for colour in self.POS_COLOUR_CODE:
            if pos in self.POS_COLOUR_CODE[colour]:
                return colour

    def get_is_atom(self):
        """
        Returns whether this Blissymbol is atomic.
        ~
        is_atom is True when a Blissymbol is atomic, False otherwise.

        :return: bool, whether this Blissymbol is atomic
        """
        return self.is_atom

    def init_is_atom(self):
        """
        Initializes this Blissymbol as atomic or not.
        ~
        is_atom is True when a Blissymbol is atomic, False otherwise.
        ~
        N.B. Only specified Blissymbols are atomic, all others are non-atomic.
             All characters with derivations ending in "Character" are atomic.

        :return: None
        """
        self.is_atom = self.find_is_atom()

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
        derivations = self.derivation.lstrip("(").rstrip(")").split(":")  #self.derivation.split("-")

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

    def get_deriv_unicode(self):
        """
        Returns a list of this Blissymbol's derivations' unicode
        identifiers.

        :return: List[str], this Blissymbol's derivations' unicode IDs
        """
        return self.deriv_unicode

    def add_deriv_unicode(self, unicode):
        """
        Adds this unicode str to self.deriv_unicode.

        :param unicode: str, unicode string
        :return: None
        """
        self.deriv_unicode.append(unicode)

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
        uni = blissymbol.get_unicode()

        for bliss in blissymbol.get_translation("English"):
            self.add_bliss_and_unicode(bliss, uni)

    def find_unicode(self, defn, lang="English"):
        """
        Given a word defn, finds and adds unicode names for defn
        to this Blissymbol's unicode.
        ~
        If no unicode name for this defn or its derivations exists,
        creates new unicode name and adds to encoding dicts accordingly.

        :param defn: str, word to find/add unicode
        :param lang: str, this word's language
        :return: str, word's corresponding unicode name
        """
        if defn in self.translator.get_bliss_to_unicode():
            uni = self.translator.lookup_bliss_to_unicode(defn)[0]
        else:
            if lang != "English":
                # only add English translations as lemmas to bliss dict,
                # since Blissymbols default language is English
                synonyms = self.translations["English"]
                unis = []
                # add the same unicode definition for each synonym
                for synonym in synonyms:
                    if len(unis) == 0:
                        unis = self.translator.lookup_bliss_to_unicode(synonym)

                    if len(unis) != 0:
                        uni = unis[0]
                        return uni

            global LAST_BLISS_ENCODING
            LAST_BLISS_ENCODING += 1

            uni = hex(LAST_BLISS_ENCODING)
            uni = uni[2:]
            uni = "U+" + uni
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

    def clean_derivation_synonym(self, deriv_synonym):
        """
        Returns this Blissymbol's deriv_synonym cleaned.

        :param deriv_synonym: str, synonym for a Blissymbol's derivation
        :return: str, derivation synonym cleaned
        """
        if deriv_synonym[:9] == "indicator":
            deriv_synonym = deriv_synonym.replace("(", "")
            deriv_synonym = deriv_synonym.replace(")", "")
        deriv_synonym = deriv_synonym.replace("_", " ")
        deriv_synonym = self.remove_parens(deriv_synonym)
        return deriv_synonym

    def find_deriv_unicode(self):
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
        deriv_unicode = set()
        deriv_synonyms = self.derivations_synonyms(self.derivations)
        unicodes = set()

        for deriv_synonym in deriv_synonyms:
            synonym = self.clean_derivation_synonym(deriv_synonym)
            if synonym in self.translator.get_bliss_to_unicode():
                unis = self.translator.lookup_bliss_to_unicode(synonym)
                unis = self.translator.remove_duplicates(unis)

                if len(unis) == 1:
                    uni = unis[0]
                    unicodes.add(uni)
                    self.add_bliss_and_unicode(synonym, uni)
                    break
                else:
                    unis = set(unis)
                    if len(unicodes) == 0:
                        unicodes.update(unis)
                    else:
                        unicodes.intersection_update(unis)
                        for uni in unis:
                            self.add_bliss_and_unicode(synonym, uni)
            else:
                uni = self.find_unicode(synonym)
                unicodes.add(uni)
                self.add_bliss_and_unicode(synonym, uni)

            if len(deriv_unicode.intersection(unicodes)) > 0:
                deriv_unicode.intersection_update(unicodes)
            else:
                deriv_unicode.update(unicodes)

        return list(deriv_unicode)

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

        :return: None
        """
        translations = self.translations["English"]

        if len(translations) != 0:
            translation = translations[0]
            self.unicode = self.find_unicode(translation)
            self.add_blissymbol_unicodes(self)
        else:
            print("could not find unicode defn for " + self.bliss_name)
            self.unicode = None

    def init_deriv_unicode(self):
        """
        Automatically sets this Blissymbol's deriv_unicode to
        its derivations' unicodes.

        :return: None
        """
        self.deriv_unicode = [self.unicode] if self.is_atom else self.find_deriv_unicode()

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
        synsets = self.translator.lookup_blissymbol_synsets(self)
        if len(synsets) == 0:
            synsets = list(self.find_blissymbol_synsets())
        try:
            self.synset = synsets[0]
        except IndexError:
            pass
        return set(synsets)

    def init_blissymbol_synset(self):
        """
        Initializes the English Wordnet synset corresponding
        to this Blissymbol.

        :return: Synset, this Blissymbol's Wordnet synset
        """
        try:
            self.synset = self.synsets[0]
        except IndexError:
            return None

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
                        synset = self.translator.lookup_word_synsets(defn, pos, lang=lang)
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
            self.init_pos(pos)

        return synsets

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
        #self.bliss_atoms = self.lex_parser.init_blissnet()
    
    
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
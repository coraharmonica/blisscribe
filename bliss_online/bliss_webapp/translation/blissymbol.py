# -*- coding: utf-8 -*-
"""
BLISSYMBOLS:

    Contains a class for representing a Blissymbol, either
    created from a language-to-Blissymbols dictionary file or
    by a user.
"""
import os, sys
PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(PATH)
from imports import safe_import
safe_import("images")
safe_import("parts_of_speech")
safe_import("resources")
from images import *
from parts_of_speech import *
from resources.data.bci_blissnet import BCI_BLISSNET

NEW_BLISSYMBOLS = []    # stores new Blissymbols from Blissymbol.new_blissymbol() for deletion


class Blissymbol:
    """
    A class representing a Blissymbol, each with...
    - img filename
    - part of speech
    :param derivation: str, this Blissymbol's derivative Blissymbols
    :param translations: Optional[dict], translation(s) in each language
    :param blisstranslator: BlissTranslator, for translating this Blissymbol to target languages
    :param bci_num: int, this Blissymbol's BCI-AV#, i.e. its official BCI numeric ID
                         -> N.B. initialize as 0 if creating a new Blissymbol
    """
    def __init__(self, bliss_name=None, pos=None, derivation=list(), translations=None, translator=None, num=None):
        if bliss_name[-5:] != "(OLD)" and bliss_name[-7:] != "ercase)":
            self.translator = translator
            self.bliss_name = bliss_name
            self.bci_num = self.init_bci_num(num)
            self.pos = self.init_pos(pos)
            self.derivation = derivation
            self.check_img_filename()  # creates new blissymbol image from derivation if none exists
            self.translations = self.clean_translations(translations)  # holds translations in different languages
            self.synsets = None
            self.init_synsets()
        else:
            self.bliss_name = bliss_name
            self.pos = POS_COLOURS.get(pos, pos)
            self.derivation = []
            self.translations = {}
            self.translator = translator
            self.bci_num = 0
            self.synsets = None

    @property
    def is_atomic(self):
        return len(self.derivation) == 1

    @property
    def image_filename(self):
        return self.bliss_name + ".png"

    @property
    def unicode(self):
        return self.translator.lex_parser.load_bliss_unicode().get(self.bliss_name, " ".join(self.find_deriv_unicode()))

    def set_pos(self, pos):
        """
        Sets this Blissymbol's parts of speech to pos.

        :param pos: List[str], list of Penn Treebank parts of speech
        :return: None
        """
        self.pos = pos

    def image(self, **kwargs):
        """
        Returns the Image for this Blissymbol, with a
        maximum width of max_width and maximum height of max_height.

        keyword args:
            :param width: Optional[int], maximum width of output image
            :param height: Optional[int], maximum height of output image
            :param whitebg: bool, whether to output white or transparent background
            :param text_img: bool, whether to return word or Blissymbol image

        :return: Image, image of this Blissymbol with given dimensions
        """
        kwargs.setdefault('width', None)
        height = kwargs.setdefault('height', self.translator.image_heights())
        kwargs.setdefault('whitebg', False)
        is_text = kwargs.setdefault('text_img', False)
        subs = kwargs.setdefault('subs', False)
        if is_text:
            return word_image(self.bliss_name, img_h=height, subs=subs)
        else:
            return self.translator.bliss_image(self.bliss_name, **kwargs)

    @property
    def indicators(self):
        return [d for d in self.derivation if self.is_indicator(d)]

    def overlay_indicators(self, img, indicators):
        if len(indicators) == 0:
            return img
        #elif len(indicators) == 1:
        #    return self.indicator_image(img, indicators.pop())
        else:
            deriv_inds = self.indicators
            indicators = sorted(deriv_inds + indicators, key=lambda i: INDICATORS.get(i[11:-1],
                                                                                      max(INDICATORS.values())+1))
            ind_imgs = [self.translator.bliss_image(ind, width=img.size[0], height=img.size[1], whitebg=False)
                        for ind in indicators]
            ind_banner = blank_image(0, 0, 0)
            for ind_img in ind_imgs:
                ind_banner = beside(ind_banner, ind_img)
            if len(deriv_inds) != 0:
                # cover up indicator area (up to 350y)
                cover = self.translator.blank_image(x=img.size[0], y=img.size[1]//3, opacity=255)
                img.paste(cover, (0, 0))
            return overlay(ind_banner, img)

    def indicator_image(self, img, indicator):
        """
        Returns this Blissymbol img with this indicator.

        :param img: Image, Blissymbol image to pluralize
        :param indicator: str, name of indicator
        :return: Image, input image pluralized
        """
        bliss_indicators = self.indicators
        ind = self.translator.bliss_image(indicator, width=img.size[0], height=img.size[1], whitebg=True)
        if len(bliss_indicators) != 0:
            # indicator width = 158
            blank_img = self.translator.blank_image(x=int(158*1.5*len(bliss_indicators)), y=img.size[1], opacity=0)
            ind = self.translator.beside(blank_img, ind)
        return overlay(ind, img)

    def is_punct(self):
        """
        Returns True if this Blissymbol is a punctuation symbol.

        :return: bool, whether this Blissymbol is punctuation
        """
        return self.bliss_name in PUNCT_MAP.values()

    def valid_filename(self):
        """
        Returns True if this Blissymbol's img_filename can be opened,
        False otherwise.

        :return: bool, whether img_filename can be opened
        """
        try:
            open(IMG_PATH + self.bliss_name + ".png")
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
                    self.bliss_name = name
                    break
            else:
                print("couldn't open file: " + self.bliss_name + str(self.derivation))

            if len(self.derivation) != 0:
                self.new_blissymbol(self.derivation, self.bliss_name)

    def count_indicators(self):
        count = 0
        for deriv in self.derivation:
            if self.is_indicator(deriv):
                count += 1
        return count

    def derivation_blissymbols(self, atomic=True):
        """
        Returns a list of Blissymbols for this Blissymbol's derivation.
        ~
        If atomic is True, returns all atomic Blissymbols part of this
        Blissymbol's derivation.  Otherwise, returns only this Blissymbol's
        immediate derivations as Blissymbols.
        ~
        e.g. bs = Blissymbol("rabbit,hare", derivation="(rodent + ear)"])

             bs.derivation_blissymbols(False) -> [Blissymbol("rodent"), Blissymbol("ear")]
             bs.derivation_blissymbols(True) -> [Blissymbol("animal"), Blissymbol("teeth"), Blissymbol("ear")]

        :param atomic: bool, whether to return only atomic Blissymbol derivations
        :return: List[Blissymbol], this Blissymbol's derivative Blissymbols
        """
        bliss_derivatives = list()

        if self.is_atomic:
            bliss_derivatives.append(self)
            return bliss_derivatives
        else:
            for derivation in self.derivation:
                deriv_bliss = self.translator.blissword_to_blissymbol(derivation)

                if deriv_bliss is None:  # if derivation has no characters, return this Blissymbol
                    bliss_derivatives.append(deriv_bliss)
                    return bliss_derivatives
                elif self == deriv_bliss or deriv_bliss in bliss_derivatives:
                    continue
                else:
                    if atomic:
                        bliss_derivatives += deriv_bliss.derivation_blissymbols(atomic)
                    else:
                        bliss_derivatives.append(self)

            if len(bliss_derivatives) == 0:
                bliss_derivatives.append(self)

            return bliss_derivatives

    def new_blissymbol(self, derivations, bliss_name):
        """
        Given a list of derivations for a Blissymbol,
        combines derivations to make a new Blissymbol image
        and returns the result.
        ~
        Saves the resulting image under this filename.

        :param derivations: List[str], derivative Blissymbol(s)
        :param bliss_name: str, name of new Blissymbol
        :return: Image, new Blissymbol image from derivations
        """
        if bliss_name is None:
            bliss_name = self.bliss_name

        bliss_imgs = []
        indicators = []
        width = 0
        space = 2

        for derivation in self.derivation:
            blissymbol = self.translator.blissword_to_blissymbol(derivation)

            if blissymbol is not None:
                bliss_name = blissymbol.bliss_name
                bliss_img = self.translator.bliss_image(bliss_name)
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

            img_path = str(IMG_PATH + bliss_name)
            img.save(img_path)
            print("made new Blissymbol: " + bliss_name)
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

    def is_derivation(self, word):
        """
        Returns True if this word is in this Blissymbol's derivations,
        False otherwise.

        :return: bool, whether this word is a derivation of this Blissymbol
        """
        return word in self.derivation

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

        for derivation in self.derivation:
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
        blissymbol = self.translator.blissword_to_blissymbol(derivation)

        if blissymbol is None:
            return atoms
        else:
            if blissymbol.is_atom:
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
            cleaned = self.clean_defn(t.split("(")[0]).rstrip("-")
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

    def get_pos(self):
        """
        Return first part-of-speech in this Blissymbol's
        parts-of-speech list.

        :return: str, Blissymbol's part-of-speech
        """
        if self.pos is not None and len(self.pos) != 0:
            return self.pos[0]

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
        paren_phrase = self.get_parens(self.bliss_name)
        if paren_phrase is None:
            return True
        else:
            start = paren_phrase[1:5]
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
        return self.translations.get(language, list())

    def init_pos(self, pos):
        """
        Sets this Blissymbol's pos to this pos,
        unless Blissymbol appears to be a different
        part of speech.

        :param pos: str, this Blissymbol's part of speech
        :return: List[str], this Blissymbol's parts of speech
        """
        return list(pos) if type(pos) != str else [pos]

    @staticmethod
    def find_colour_pos(colour):
        """
        Given a colour, returns the corresponding pos.

        :param colour: str, a Blissymbol's part of speech colour
        :return: List[str], parts of speech for the given colour
        """
        return POS_COLOURS[colour]

    def derivation_unicodes(self, atomic=True):
        """
        Returns a list of this Blissymbol's derivations' unicode
        identifiers.

        :return: List[str], this Blissymbol's derivations' unicode IDs
        """
        return [self.unicode] if self.is_atomic else self.find_deriv_unicode(atomic=atomic)

    def derivation_bci_nums(self, atomic=True):
        """
        Returns a list of this Blissymbol's derivations' BCI-AV#s.

        :return: List[int], this Blissymbol's derivations' BCI-AV#s
        """
        return [self.bci_num] if self.is_atomic else self.find_deriv_bci_nums(atomic=atomic)

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

    def find_deriv_bci_nums(self, atomic=True):
        """
        Returns a list of BCI-AV#s corresponding to
        the Blissymbol translations of this Blissymbol's
        derivations.
        ~
        N.B. If this Blissymbol is atomic, then its
        deriv_bci_num will be equivalent to its bci_num.

        :return: List[int], BCI-AV#s for this Blissymbol's
            derivations
        """
        return [db.bci_num for db in self.derivation_blissymbols(atomic=atomic)]

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

    def init_bci_num(self, bci_num):
        """
        Returns the appropriate BCI-AV# for this Blissymbol.
        ~
        If this bci_num is not None, returns bci_num.
        Otherwise, returns the BCI-AV# for a Blissymbol with the
        same bliss_name as this Blissymbol.  If none exist,
        returns None.

        :return: Optional[int], this Blissymbol's BCI-AV# (None if nonexistent)
        """
        return int(bci_num) if bci_num is not None else None

    def init_synsets(self):
        """
        Sets this Blissymbol's synsets as a corresponding list of
        English Wordnet Synsets.

        :return: None
        """
        self.synsets = [self.translator.str_synset(s) for s in self.lookup_blissnet()]

    def lookup_blissnet(self):
        """
        Returns a list of WordNet synset strings corresponding
        to this Blissymbol's bci_num.

        :return: List[str], synset strings
        """
        return BCI_BLISSNET.get(self.bci_num, [])

    def find_synsets(self):
        """
        Returns a list of English Wordnet synsets corresponding
        to this Blissymbol.

        :return: Set[Synset], this Blissymbol's Wordnet synsets
        """
        synsets = self.translator.ordered_set([])
        translations = self.translations
        word = self.bliss_name
        word = word.replace("_", " ")
        words = word.split(",")
        pos = self.get_pos()

        if len(words) > 0:
            word_synsets = self.translator.ordered_set([])
            lang_synsets = self.translator.ordered_set([])

            for word in words:
                word = self.remove_parens(word)
                word = word.rstrip("_")
                word_synset = self.translator.word_synsets(word, pos)
                word_synsets.update(word_synset)

            for lang in translations:
                if lang != "English":
                    translation = translations[lang]
                    lang_synset = set()
                    lang_code = self.translator.find_lang_code(lang)

                    for defn in translation:
                        synset = self.translator.word_synsets(defn, pos, lang_code=lang_code)
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

        if len(self.synsets) == 0 and len(synsets) != 0:
            self.synsets = synsets.items()
        if len(self.synsets) != 0:
            pos = self.synsets[0].pos()
            self.pos = self.init_pos(pos)

        return synsets

    def clean_bliss_name(self):
        return self.bliss_name.replace("_", " ")

    def __eq__(self, other):
        return self.bliss_name == other.bliss_name

    def __hash__(self):
        return hash(self.bliss_name)

    def __str__(self):
        return 'Blissymbol("{0}", {1}, {2}, {3}, {4}, {5})'.format(self.bliss_name,
                                                                   self.pos,
                                                                   self.derivation,
                                                                   self.translations,
                                                                   "self.translator",
                                                                   self.bci_num)

    def __int__(self):
        return int(self.bci_num)

    def __dict__(self):
        return {"name": self.bliss_name,
                "pos": self.get_pos(),
                "BCI-AV": self.bci_num,
                "derivation": self.derivation,
                "translations": self.translations}

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
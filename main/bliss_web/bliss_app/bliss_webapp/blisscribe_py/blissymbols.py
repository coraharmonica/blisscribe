# -*- coding: utf-8 -*-
"""
BLISSYMBOLS:

    Contains a class for representing a Blissymbol, either
    created from a language-to-Blissymbols dictionary file or
    by a user.
"""
import os
from PIL import Image
from bliss_encoding import BLISS_TO_UNICODE, UNICODE_TO_BLISS

BLISS_TO_UNICODE = BLISS_TO_UNICODE
UNICODE_TO_BLISS = UNICODE_TO_BLISS
LAST_BLISS_ENCODING = int("3576", 16)
NEW_BLISSYMBOLS = [] # stores Blissymbols created with Blissymbol.makeNewBlissymbol() for later deletion
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
IMG_LOCN = "/symbols/png/full/"
IMG_PATH = FILE_PATH + IMG_LOCN


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
    POS_COLOURS = ["RED", "YELLOW", "BLUE", "GREEN", "GRAY", "WHITE"]
    POS_COLOUR_CODE = {"GRAY": ["INDICATOR"],
                       #"WHITE": ["CC", "CD", "DT", "EX", "IN", "JJ", "PRP", "RP", "UH", "WDT"],
                       # WHITE also includes colours & relations
                       "WHITE": PARTS_OF_SPEECH,  # WHITE is catch-all other parts of speech
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

    def __init__(self, img_filename=None, pos=None, derivation="", translations=None, translator=None): # language="English"
        self.translator = translator
        self.img_filename = img_filename
        self.pos_code = pos
        self.initPosCode(pos)
        self.pos = pos
        self.initPos(pos)
        self.paren_phrase = self.getParens(self.getBlissName())
        self.derivation = derivation
        self.is_atom = bool
        self.initIsAtom()
        self.derivations = self.findDerivations()
        self.checkImgFilename()  # creates new blissymbol image from derivations if none exists
        self.bliss_name = self.getBlissName()
        #self.language = language
        self.translations = self.cleanTranslations(translations)  # hold translations in different languages
        self.bliss_glyph = None
        self.unicode = str
        self.deriv_unicode = []
        self.initUnicode()
        self.initDerivUnicode()
        #self.changed = False  # whether this Blissymbol's translations, etc. have changed at all
        self.synset = None
        self.synsets = self.initBlissymbolSynsets()
        #print("\nHi!  I'm the Blissymbol " + self.bliss_name + ", with the " +
        #      "synsets: ")
        #print(self.synsets)
        #for synset in self.synsets:
        #    print synset, ": " + self.translator.getSynsetDefn(synset)
        #print("and the unicode: " + self.unicode)
        #print("Hope this is okay... Bye!\n")

    def checkImgFilename(self):
        """
        Checks to see if this Blissymbol's img_filename
        can be opened.
        ~
        If img_filename cannot be opened, attempts to create
        a new image from this Blissymbol's derivations, and
        saves this new image under img_filename.

        :return: None
        """
        try:
            open(IMG_PATH + self.img_filename)
        except IOError:
            bliss_name = self.getBlissName()
            for name in bliss_name.split(","):
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
            derivs = self.derivations
            self.makeNewBlissymbol(derivs, self.img_filename)

    def makeNewBlissymbol(self, derivations, filename=None, pos=False):
        """
        Given a list of derivations for a Blissymbol,
        combines derivations in order to make a new Bliss image.
        ~
        Saves the result under given filename, or otherwise
        this Blissymbol's img_filename.

        :param derivations: List[str], derivative Blissymbol(s)
        :param filename: str, filename to save Blissymbol under
        :param pos: bool, whether to automatically include POS Blissymbol
        :return: None
        """
        if filename is None:
            filename = self.img_filename

        bliss_words = []
        width = 0
        height = 0
        space = 0

        idx = 0

        for derivation in derivations:
            #print(derivation)
            derivation = derivation.replace(" ", "_")

            try:
                Image.open(str(IMG_PATH + derivation + ".png"))
            except IOError:
                try:
                    Image.open(str(IMG_PATH + derivation[:-1] + ".png"))
                except IOError:
                    for deriv in derivation.split(","):
                        deriv = deriv.replace(" ", "_")
                        try:
                            Image.open(str(IMG_PATH + deriv + ".png"))
                        except IOError:
                            print("couldn't find Blissymbol derivation for " + deriv + "...")
                            continue
                        else:
                            bliss_word = Image.open(str(IMG_PATH + deriv + ".png"))
                            bliss_words.append(bliss_word)
                            break
                    else:
                        print("couldn't find Blissymbol derivation for " + derivation + "...")
                        return
                else:
                    if derivation[-1:] == ")":
                        derivation = derivation[:-1]
                        bliss_word = Image.open(str(IMG_PATH + derivation + ".png"))
                        bliss_words.append(bliss_word)
                        self.derivations[idx] = derivation
            else:
                bliss_word = Image.open(str(IMG_PATH + derivation + ".png"))
                bliss_words.append(bliss_word)

            if bliss_word is not None:
                if height == 0:
                    height = bliss_word.size[1]
                    space = height/25
                width += space + bliss_word.size[0]

            idx += 1

        if pos:
            indicator = self.getPosIndicator()
            if indicator is not None:
                indicator = self.translator.getIndicatorBlissImg(indicator)
                width += space + indicator.size[0]
                bliss_words.append(indicator)

        bs = Image.new("RGBA", (width, height))

        curr_width = space

        for bliss_word in bliss_words:
            bs.paste(bliss_word, (curr_width, 0))
            curr_width += space + bliss_word.size[0]

        filename = filename.encode('utf-8')
        img_path = str(IMG_PATH + filename)
        bs.save(img_path)
        print("made new Blissymbol: " + filename)
        NEW_BLISSYMBOLS.append(img_path)

    def addTranslation(self, language, translation):
        """
        Adds given translation to self.translations
        under given language.

        e.g. addTranslation("Polish", "kot") ->
             self.translations == {"Polish": ["kot"]}

             addTranslation("French", "chat") ->
             self.translations == {"Polish": ["kot"],
                                   "French": ["chat"]}

        :param language: str, language of given translation
        :param translation: str, Blissymbol translation in language
        :return: None
        """
        self.translations.setdefault(language, [])
        self.translations[language].append(translation)
        self.translations[language] = self.translator.removeDuplicates(self.translations[language])

    def addTranslations(self, language, translations):
        """
        Adds given translations to self.translations
        under given language.

        e.g. addTranslation("Polish", ["kot", "kotka"]) ->
             self.translations == {"Polish": ["kot", "kotka"]}

             addTranslation("French", ["chat", "chatton"]) ->
             self.translations == {"Polish": ["kot", "kotka"],
                                   "French": ["chat", "chatton"]}

        :param language: str, language of given translation
        :param translation: List[str], Blissymbol translations in language
        :return: None
        """
        self.translations.setdefault(language, [])
        for translation in translations:
            self.addTranslation(language, translation)

    def getDerivation(self):
        return str(self.derivation)

    def setDerivation(self, derivation):
        """
        Sets this Blissymbol's derivation to given derivation.

        :param derivation: str, derivation of Blissymbol
        :return: None
        """
        self.derivation = derivation

    def findDerivations(self):
        """
        Returns a list of the Blissymbols from which this
        Blissymbol is derived.

        :return: List[str], list of this Blissymbol's derivations
        """
        if self.is_atom:
            return [self.getBlissName()]
        elif self.derivation == "":
            return []
        else:
            deriv = self.derivation
            deriv = deriv.replace("\n", "")
            deriv = deriv.replace(";", ":")
            deriv = deriv.replace("+", " + ")
            deriv = deriv.replace("  ", " ")
            derivs = deriv.split(":")
            deriv = derivs[0]
            #deriv = self.getParens(deriv)


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
                        derivs[end-1] = self.cleanDefn(derivs[end-1])
                        blissymbol = " ".join(derivs[start:])
                        if blissymbol[-2:] == "))":
                            blissymbol = blissymbol[:-1]
                        derivations.append(blissymbol)
                    elif d != "":
                        derivs[end-1] = self.cleanDefn(derivs[end-1])
                    end += 1

            return derivations #[self.removeParens(d) for d in derivations]

    def setDerivations(self, derivations):
        """
        Sets this Blissymbol's derivations to given derivations.

        :param derivation: List[str], derivations of Blissymbol
        :return: None
        """
        self.derivations = derivations

    def getDerivations(self):
        """
        Returns this Blissymbol's derivations.

        :return: List[str], derivations of Blissymbol
        """
        return self.derivations

    def cleanDefn(self, defn):
        """
        Replaces input defn's underscores with spaces and
        strips whitespace from ends.  Returns result.

        :param defn: str, word definition to clean
        :return: str, cleaned word definition
        """
        new_defn = defn.replace("_", " ")
        new_defn = new_defn.strip()
        return new_defn

    def cleanTranslation(self, translation):
        """
        Returns the given list of translation definitions
        with spaces instead of underscores and no parenthesis
        phrase.
        ~
        Allows for more direct comparisons between input and
        Blissymbol translations.

        :param translation: List[str], input translations to clean
        :return: List[str], cleaned translations
        """
        translation = [self.removeParens(self.cleanDefn(t)) for t in translation]
        return self.translator.removeDuplicates(translation)

    def cleanTranslations(self, translations):
        """
        Returns the given dictionary of translations with
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
        translations = {language: self.cleanTranslation(translations[language]) for language in languages}
        return translations

    def getBlissName(self):
        """
        Return name of this Blissymbol's bliss image
        file, without the filename extension.

        :return: str, Blissymbol's image filename
        """
        return self.img_filename[:-4]

    def getImgFilename(self):
        """
        Returns image filename associated with this Blissymbol.

        :return: str, this Blissymbol's image filename
        """
        return self.img_filename

    def getPosCode(self):
        """
        Return this Blissymbol's part-of-speech colour code.

        :return: str, Blissymbol's part-of-speech colour code
        """
        return self.pos_code

    def getPos(self):
        """
        Return first part-of-speech in this Blissymbol's
        parts-of-speech list.

        :return: str, Blissymbol's part-of-speech
        """
        if self.pos is not None:
            return self.pos[0]

    def getPartsOfSpeech(self):
        """
        Return this Blissymbol's parts-of-speech list.

        :return: List[str], Blissymbol's parts-of-speech
        """
        if self.pos is not None:
            return self.pos

    def getParenPhrase(self):
        """
        Returns parenthetical(s) of this Blissymbol.

        :return: str, given word's parenthetical phrase
        """
        return self.paren_phrase

    def getParens(self, word):
        """
        Returns parenthetical(s) from the given word.
        ~
        Parenthetical begins at the first open parenthesis.

        e.g. getParens("English_(language)") -> "(language)"

        :param word: str, word to get parenthetical from
        :return: str, given word's parenthetical phrase
        """
        idx = 0
        for char in word:
            if char != "(" and char != "[":
                idx += 1
            else:
                return word[idx:]
        return None

    def isNeutral(self):
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

    def removeParens(self, word):
        """
        Removes parenthetical(s) from the given word and
        returns the result.
        ~
        Parenthetical begins at the first open parenthesis.

        e.g. getParens("English_(language)") -> "English"

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
                word = word.rstrip("-")
                return word
        return word

    '''
    GET/SET LANGUAGE FUNCTIONS
    --------------------------
    Intended for (future) Blissymbol creation solely in 1 language.
    
    def getLanguage(self):
        """
        Returns this Blissymbol's language.
        ~
        N.B. Every Blissymbol's native language is English.

        :return: str, this Blissymbol's language (English)
        """
        return str(self.language)

    def setLanguage(self, language):
        """
        Sets this Blissymbol's default language to given language.
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

    def getTranslation(self, language=None):
        """
        If self.translations contains a translation in
        given language, returns translations in that language.
        ~
        Otherwise, returns translations in this Blissymbol's
        native language.

        :param language: str, language to get translations in
        :return: List[str], Blissymbol translations in given language
        """
        try:
            self.translations[language]
        except KeyError:
            return []
        else:
            return self.translations[language]

    def getTranslations(self):
        """
        Returns this Blissymbol's translations dict.

        :return: dict, where...
            key (str) - language name (in English)
            val (List[str]) - Blissymbol translations in key language
        """
        return self.translations

    def setImgFilename(self, img_filename):
        """
        Sets this Blissymbol's img_filename to given img_filename.
        ~
        Assumes img_filename includes appropriate extension (.png).

        :param img_filename: str, image filename (ending in .png)
        :return: None
        """
        self.img_filename = img_filename

    def setParenPhrase(self, paren_phrase):
        """
        Sets this Blissymbol's parenthesis phrase to
        the given paren_phrase.

        :param paren_phrase: str, phrase in parentheses
        :return: None
        """
        self.paren_phrase = paren_phrase

    def initPos(self, pos):
        """
        Sets this Blissymbol's pos to given pos,
        unless Blissymbol appears to be a different
        part of speech.

        :param pos: str, this Blissymbol's part of speech
        :return: None
        """
        if self.getParens(self.getBlissName()) == "(to)":
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

    def initPosCode(self, pos_code):
        """
        Sets this Blissymbol's pos_code to given pos_code,
        unless pos_code is not in POS_COLOUR_CODE.

        :param pos_code: str, this Blissymbol's part of speech colour code
        :return: None
        """
        if self.getParens(self.getBlissName()) == "(to)":
            # all verbs have (to) indicator
            self.pos_code = self.POS_COLOUR_CODE["RED"]
        elif pos_code is not None:
            try:
                self.POS_COLOUR_CODE[pos_code]
            except KeyError:
                if pos_code in self.PARTS_OF_SPEECH:
                    self.pos_code = self.findPosCode(pos=pos_code)
            else:
                self.pos_code = pos_code

    def findPosCode(self, pos):
        """
        Given a pos, returns the corresponding pos colour code.

        :param pos: str, this Blissymbol's part of speech
        :return: str, pos_code
        """
        assert pos not in self.POS_COLOURS
        for colour in self.POS_COLOURS:
            if pos in self.POS_COLOUR_CODE[colour]:
                return colour

    def getIsAtom(self):
        """
        Returns whether this Blissymbol is atomic.
        ~
        is_atom is True when a Blissymbol is atomic, False otherwise.

        :return: bool, whether this Blissymbol is atomic
        """
        return self.is_atom

    def initIsAtom(self):
        self.is_atom = self.findIsAtom()

    def findIsAtom(self):
        """
        Identifies whether this Blissymbol is atomic or not.
        ~
        is_atom is True when a Blissymbol is atomic, False otherwise.
        ~
        N.B. Only specified Blissymbols are atomic, all others are non-atomic.
             All characters with derivations ending in "Character" are atomic.

        :return: bool, whether this Blissymbol is atomic
        """
        derivations = self.derivation.split("-")
        if len(derivations) == 1 and derivations[0] == self.getBlissName():
            return True
        derivation = derivations[-1]
        derivation = derivation.strip()
        is_character = (derivation[:9] == "Character")
        if is_character:
            derivation = "".join(derivations[:-1])
            derivation = derivation.strip()
            self.setDerivation(derivation)
        return is_character

    def setIsAtom(self, is_atom):
        """
        Sets this Blissymbol's is_atom value to is_atom.

        :param is_atom: bool, whether this Blissymbol is atomic
        :return: None
        """
        self.is_atom = is_atom

    def getUnicode(self):
        """
        Returns this Blissymbol's unique unicode identifier.

        :return: str, this Blissymbol's unicode ID
        """
        return self.unicode

    def getDerivUnicode(self):
        """
        Returns a list of this Blissymbol's derivations' unicode
        identifiers.

        :return: List[str], this Blissymbol's derivations' unicode IDs
        """
        return self.deriv_unicode

    def addDerivUnicode(self, unicode):
        """
        Adds given unicode str to self.deriv_unicode.

        :param unicode: str, unicode string
        :return: None
        """
        self.deriv_unicode.append(unicode)

    def addUnicodeToBliss(self, uni, bliss):
        """
        Adds the given unicode key to this Blissymbol's
        BlissTranslator's unicode-to-Blissymbol dict,
        with blissymbol name bliss as its value.

        :param uni: str, unicode name to add
        :param bliss: str, name of blissymbol for given unicode
        :return: None
        """
        self.translator.addUnicodeToBliss(uni, bliss)

    def addBlissToUnicode(self, bliss, uni):
        """
        Adds the given blissymbol key bliss to this Blissymbol's
        BlissTranslator's Blissymbol-to-unicode dict,
        with unicode as its value.

        :param bliss: str, name of blissymbol to add
        :param unicode: str, unicode name for given bliss
        :return: None
        """
        self.translator.addBlissToUnicode(bliss, uni)

    def addBlissAndUnicode(self, bliss="", uni=""):
        """
        Adds the given Blissymbol string bliss and its corresponding
        unicode symbol unicode to BLISS_TO_UNICODE dict as well as
        UNICODE_TO_BLISS dict.
        ~
        If bliss or unicodes are left empty, this method sets bliss to
        this Blissymbol's name and unicode to the next unicode character
        in the series.

        :param bliss: str, name of blissymbol to add
        :param uni: str, unicode name for given bliss
        :return: None
        """
        if bliss == "":
            bliss = self.getBlissName()
        if uni == "":
            uni = self.unicode

        #self.writeBlissAndUnicode(bliss, uni)
        self.addBlissToUnicode(bliss, uni)
        self.addUnicodeToBliss(uni, bliss)

    def writeBlissymbolEncoding(self, blissymbol):
        """
        Creates a new entry to BLISS_TO_UNICODE and UNICODE_TO_BLISS based on
        given blissymbol.

        :param blissymbol: Blissymbol, blissymbol to add to Bliss-to-uni encoding dicts
        :return: None
        """
        uni = blissymbol.getUnicode()

        for bliss in blissymbol.getTranslation("English"):
            self.writeBlissAndUnicode(bliss, uni)

    def writeBlissAndUnicode(self, bliss, uni):
        """
        Creates a new entry to BLISS_TO_UNICODE and UNICODE_TO_BLISS based on
        given Bliss word bliss and its unicode representation.
        ~
        If Bliss word is already in dict and translations are not, appends new
        translations appropriately.  If translations are already in dict, does
        nothing.  Otherwise, adds a new lexical entry for this Bliss word.

        :param bliss: str, Bliss word to add to Bliss-to-uni encoding dicts
        :param uni: str, unicode name for given bliss
        :return: None
        """
        path = FILE_PATH + "/bliss_encoding.py"
        if len(bliss) == 0:
            return

        if bliss not in BLISS_TO_UNICODE:
            bliss_line = '\nBLISS_TO_UNICODE["' + bliss + '"] = ["' + uni + '"]'
        elif uni not in BLISS_TO_UNICODE[bliss]:
            bliss_line = '\nBLISS_TO_UNICODE["' + bliss + '"].append("' + uni + '")'
        else:
            return
        bliss_line = self.translator.deUnicodize(bliss_line)

        if uni not in UNICODE_TO_BLISS:
            uni_line = '\nUNICODE_TO_BLISS["' + uni + '"] = ["' + bliss + '"]'
        elif bliss not in UNICODE_TO_BLISS[uni]:
            uni_line = '\nUNICODE_TO_BLISS["' + uni + '"].append("' + bliss + '")'
        else:
            return
        uni_line = self.translator.deUnicodize(uni_line)

        with open(path, "a") as encoding:
            print("writing to file...")
            encoding.write(bliss_line)
            encoding.write(uni_line)
            encoding.close()

        self.addBlissAndUnicode(bliss, uni)

    def findUnicode(self, defn, lang="English"):
        """
        Given a word defn, finds and adds unicode names for defn
        to this Blissymbol's unicode.
        ~
        If no unicode name for this defn or its derivations exists,
        creates new unicode name and adds to encoding dicts accordingly.

        :param defn: str, word to find/add unicode
        :param lang: str, given word's language
        :return: str, word's corresponding unicode name
        """
        if defn in self.translator.getBlissToUnicode():
            uni = self.translator.lookupBlissToUnicode(defn)[0]
        else:
            if lang != "English":
                # only add English translations as lemmas to bliss dict,
                # since Blissymbols default language is English
                synonyms = self.translations["English"]
                unis = []
                # add the same unicode definition for each synonym
                for synonym in synonyms:
                    if len(unis) == 0:
                        unis = self.translator.lookupBlissToUnicode(synonym)

                    if len(unis) != 0:
                        uni = unis[0]
                        return uni

            global LAST_BLISS_ENCODING
            LAST_BLISS_ENCODING += 1

            uni = hex(LAST_BLISS_ENCODING)
            uni = uni[2:]
            uni = "U+" + uni
            #self.addBlissAndUnicode(bliss=defn, uni=uni)
            #self.writeBlissAndUnicode(bliss=defn, uni=uni)

        return uni

    def findDerivUnicode(self):
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
        derivations = self.derivations
        deriv_unicode = set()

        for derivation in derivations:
            unicodes = set()
            for synonym in derivation.split(","):
                if synonym[:9] == "indicator":
                    synonym = synonym.replace("(", "")
                    synonym = synonym.replace(")", "")
                synonym = synonym.replace("_", " ")
                synonym = self.removeParens(synonym)

                if synonym in self.translator.getBlissToUnicode():
                    unis = self.translator.lookupBlissToUnicode(synonym)
                    unis = self.translator.removeDuplicates(unis)
                    if len(unis) == 1:
                        uni = unis[0]
                        unicodes.add(uni)
                        self.writeBlissAndUnicode(synonym, uni)
                        break
                    else:
                        unis = set(unis)
                        if len(unicodes) == 0:
                            unicodes.update(unis)
                        else:
                            unicodes.intersection_update(unis)
                            for uni in unis:
                                self.writeBlissAndUnicode(synonym, uni)
                else:
                    uni = self.findUnicode(synonym)
                    unicodes.add(uni)
                    #self.addBlissAndUnicode(bliss=synonym, uni=uni)
                    self.writeBlissAndUnicode(bliss=synonym, uni=uni)

            if len(deriv_unicode.intersection(unicodes)) > 0:
                deriv_unicode.intersection_update(unicodes)
            else:
                deriv_unicode.update(unicodes)

        return list(deriv_unicode)

    def getUnicodePos(self):
        """
        If this Blissymbol is not atomic, returns unicode name
        for this Blissymbol's part of speech.

        :return: str, unicode representation of part of speech
        """
        if not self.is_atom:
            try:
                indicator = self.translator.bliss_to_uni[self.getPosIndicator()]
            except KeyError:
                return ""
            else:
                return indicator

    def getPosIndicator(self):
        """
        If this Blissymbol is not atomic, returns unicode name
        for this Blissymbol's part of speech.

        :return: str, Blissymbol indicator name for pos
        """
        #if not self.is_atom:
        if self.getPos() == "NN":
            return "indicator thing"
        elif self.getPos() == "JJ" or self.getPos() == "RB":
            return "indicator description"
        elif self.getPos() == "VB":
            return "indicator action"

    def hasUnicode(self):
        """
        Returns True if this Blissymbol has a corresponding
        unicode value, False otherwise.

        :return: bool, whether this Blissymbol has a unicode
        """
        return self.unicode is not None

    def initUnicode(self):
        """
        Initializes this Blissymbol's unicode to
        its definition's unicode.

        :return: None
        """
        #translations = self.translations(language=self.language)
        translations = self.translations["English"]  #self.language?
        print translations

        if len(translations) != 0:
            translation = translations[0]
            self.unicode = self.findUnicode(translation)
            print translation, self.unicode
            self.writeBlissymbolEncoding(self)
            #self.writeBlissAndUnicode(bliss=translation, uni=self.unicode)

            '''
            if self.unicode is None:
                for translation in translations:
                    self.unicode = self.findUnicode(translation)
                    if self.unicode is not None:
                        self.writeBlissAndUnicode(bliss=translation, uni=self.unicode)
                        #self.addBlissAndUnicode(bliss=translation, uni=self.unicode)
                        return
            '''
        else:
            print("could not find unicode defn for " + self.bliss_name)
            self.unicode = None

    def initDerivUnicode(self):
        """
        Automatically sets this Blissymbol's deriv_unicode to
        its derivations' unicodes.

        :return: None
        """
        self.deriv_unicode = [self.unicode] if self.is_atom else self.findDerivUnicode()

    def getSynset(self):
        return self.synset

    def getSynsets(self):
        return self.synsets

    def addSynset(self, synset):
        """
        Adds given synset to this Blissymbol's synsets.

        :param synset: Synset, synset to add to synsets
        :return: None
        """
        self.synsets.add(synset)

    def addSynsets(self, synsets):
        """
        Updates this Blissymbol's synsets with given synsets.

        :param synsets: List[Synset], synsets to add to synsets
        :return: None
        """
        self.synsets.update(synsets)

    def initBlissymbolSynsets(self):
        """
        Returns a list of English Wordnet synsets corresponding
        to this Blissymbol.

        :return: Set[Synset], this Blissymbol's Wordnet synsets
        """
        synsets = self.translator.lookupBlissymbolSynsets(self)
        if len(synsets) == 0:
            synsets = list(self.findBlissymbolSynsets())
        try:
            self.synset = synsets[0]
        except IndexError:
            pass
        #else:
        #    self.synset = synsets[0]
        return set(synsets)

    def initBlissymbolSynset(self):
        """
        Initializes the English Wordnet synset corresponding
        to this Blissymbol.

        :return: Synset, this Blissymbol's Wordnet synset
        """
        try:
            self.synset = self.synsets[0]
        except IndexError:
            return None

    def findBlissymbolSynsets(self):
        """
        Returns a list of English Wordnet synsets corresponding
        to this Blissymbol.

        :return: Set[Synset], this Blissymbol's Wordnet synsets
        """
        synsets = set([])
        translations = self.getTranslations()
        word = self.getBlissName()
        word = word.replace("_", " ")
        words = word.split(",")
        pos = self.getPos()

        if len(words) > 0:
            word_synsets = set([])
            lang_synsets = set([])

            for word in words:
                word = self.removeParens(word)
                word = word.rstrip("_")
                word_synset = self.translator.lookupWordSynsets(word, pos)
                #word_synsets.intersection_update(word_synset)
                word_synsets.update(word_synset)
                #if self.synset is None and len(word_synset) != 0:
                #    self.synset = word_synset[0]

            for lang in translations:
                if lang != "English":
                    translation = translations[lang]
                    lang_synset = set([])

                    for defn in translation:
                        synset = self.translator.lookupWordSynsets(defn, pos, lang=lang)
                        if synset is None:
                            lang = False
                            break
                        else:
                            lang_synset.update(synset)
                    if not lang:
                        continue

                    if len(lang_synset) != 0:
                        #print "synset in " + lang[:7] + ":\t", lang_synset
                        if len(lang_synsets) != 0:
                            lang_synsets.intersection_update(lang_synset)
                        else:
                            lang_synsets.update(lang_synset)

            #print("intersecting multilingual synsets:\t", lang_synsets)
            synset = lang_synsets.intersection(word_synsets)

            if len(synsets) == 0:
                synsets = synset
            else:
                synsets.update(synset)

            if len(synsets) == 0:
                synsets.update(word_synsets.union(lang_synsets))
        #else:
        #    word_synset = set(self.translator.lookupWordSynsets(word, pos))
        #    synsets = word_synset

        if self.synset is None and len(synsets) != 0:
            self.synset = list(synsets)[0]
        if self.synset is not None:
            pos = self.synset.pos()
            self.initPos(pos)

        return synsets

    def setUnicode(self, unicode):
        """
        Sets this Blissymbol's unicode to unicodes.
        ~
        Each unicode str in unicodes follow the regex:
            U+[A-F|0-9]{4}

        :param unicodes: str, list of unicodes
        :return: None
        """
        self.unicode = unicode

    def setBlissGlyph(self):
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
        pos = self.getPos()

        if self.is_atom:
            glyph.setBlissUnit(self.getBlissName())
            return
        else:
            for derivn in self.derivations:
                glyph.addBlissUnit(derivn)

        if pos == 'NN':
            glyph.addUltraZone("indicator thing")
        elif pos == 'VB':
            glyph.addUltraZone("indicator action")
        elif pos == 'RB' or pos == 'JJ':
            glyph.addUltraZone("indicator description")

    def __eq__(self, other):
        return self.bliss_name == other.bliss_name

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return self.bliss_name

    __repr__ = __str__


class BlissAlphabet:
    """
    A class for holding BlissGlyph elements.
    """
    def __init__(self):
        self.lex_parser = LexiconParser()
        self.bliss_atoms = self.lex_parser.getBlissAtomsDict(self.lex_parser.LEXICA_PATH +
                                                         "blissymbol encoding.txt")


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
    GLYPH_HEIGHT = 8
    HEIGHTS = {1: "descender limit",
               2: "earthline",
               3: "middle earth line",
               4: "midline",
               5: "middle sky line",
               6: "skyline",
               7: "indicator limit",
               8: "tall indicator limit"}
    ZONE_HEIGHTS = 2  # each zone takes up 2 blocks
    UNIT_WIDTH = 4  # each atomic Blissymbol takes up 4 width units

    def __init__(self, bliss_unit=[], sky_zones=[], middle_zones=[], earth_zones=[], ultra_zones=[], infra_zones=[]):
        self.bliss_unit = bliss_unit
        self.ultra_zones = ultra_zones # ultra zone(s) holds indicators
        self.sky_zones = sky_zones
        self.middle_zones = middle_zones
        self.earth_zones = earth_zones
        self.infra_zones = infra_zones

    def setBlissUnit(self, bliss_unit):
        self.bliss_unit = bliss_unit

    def setSkyZones(self, sky_zones):
        self.sky_zones = sky_zones

    def setMiddleZones(self, middle_zones):
        self.middle_zones = middle_zones

    def setEarthZones(self, earth_zones):
        self.earth_zones = earth_zones

    def setUltraZones(self, ultra_zones):
        self.ultra_zones = ultra_zones

    def setInfraZones(self, infra_zones):
        self.infra_zones = infra_zones

    def addBlissUnit(self, bliss_unit):
        self.bliss_unit.append(bliss_unit)

    def addSkyZone(self, sky_zones):
        self.sky_zones.append(sky_zones)

    def addMiddleZone(self, middle_zone):
        self.middle_zones.append(middle_zone)

    def addEarthZone(self, earth_zone):
        self.earth_zones.append(earth_zone)

    def addUltraZone(self, ultra_zone):
        self.ultra_zones.append(ultra_zone)

    def addInfraZone(self, infra_zone):
        self.infra_zones.append(infra_zone)

    def getBlissUnit(self):
        return self.bliss_unit

    def getSkyZones(self):
        return self.sky_zones

    def getMiddleZones(self):
        return self.middle_zones

    def getEarthZones(self):
        return self.earth_zones

    def getUltraZones(self):
        return self.ultra_zones

    def getInfraZones(self):
        return self.infra_zones
# -*- coding: utf-8 -*-
"""
TRANSLATION_WORD:

    A class for representing a word-in-translation as
    part of a BlissTranslator.
"""
from parts_of_speech import INDICATORS_MAP


class TranslationWord:
    """
    Represents a word-in-translation, including:
     - word token
        i.e. word as it appears in text
        e.g. kept, mice, funnest, Alice
     - Penn Treebank part(s) of speech
     - associated BlissTranslator

     Upon initialization, uses kwargs to generate:
     - word lemma
        i.e. word as it appears in the dictionary
        e.g. keep, mouse, fun, Alice
     - synonyms
     - native language
    """
    def __init__(self, word, pos, translator, lang=None):
        self.word = word
        self.pos = set(pos) if type(pos) != str else {pos}  # Set of 1 or more parts of speech
        self.translator = translator
        self.language = self.translator.language if lang is None else lang
        self.lemmas = self.lemmatize()
        self.blissymbol = None
        self.eng_lemmas = self.find_eng_lemmas()
        self.synsets = self.find_synsets()
        self.init_blissymbol()
        if self.blissymbol is not None:
            self.synsets.extend(self.blissymbol.synsets)
            self.blissymbol.add_translations(self.language, self.lemmas)
            if self.language != "English":
                self.blissymbol.add_translations("English", self.eng_lemmas)
            self.translator.add_bliss_entry(self.blissymbol)

    def lemmatize(self):
        lemma = self.translator.lemmatize(self.word, self.pos, self.language)
        if lemma is None or len(lemma) == 0:
            prev_pos = self.pos.copy()
            self.init_pos()
            if self.pos != prev_pos:
                lemma = self.translator.lemmatize(self.word, self.pos, self.language)
        lemmas = [lemma] if type(lemma) == str or len(lemma) == 0 \
            else self.translator.ordered_set(lemma).items()
        for lemma in lemmas:
            self.init_pos(lemma)
        return lemmas

    @property
    def lemma(self):
        return self.lemmas[0]

    def init_lemmas(self):
        lemmas = self.translator.find_lemmas(self.word, self.pos, self.language)
        return [self.word] if lemmas is None else lemmas

    def init_pos(self, word=None):
        """
        If language is not English, this method cross-references
        this TranslationWord's pos with other likely parts of speech
        to determine the most likely part of speech.

        :return: None
        """
        word = self.word if word is None else word
        if self.translator.language != "English" and not self.translator.is_nonalpha(word):
            pos = self.translator.word_poses(word, self.language)
            self.pos.update(pos)

    def find_eng_lemmas(self):
        """
        Returns a list of English words synonymous with this
        TranslationWord's lemma.

        :return: List[str], this TranslationWord's English lemmas
        """
        if not self.translator.is_word(self.word):
            return []
        elif self.language == "English":
            return self.lemmas
        else:
            eng_lemmas = self.translator.ordered_set([])
            eng_lemmas += self.find_english_translations(self.lemma, self.pos)
            eng_lemmas += self.find_english_translations(self.word, self.pos)
            eng_lemmas += self.find_english_translations(self.lemma)
            eng_lemmas += self.find_english_translations(self.word)
            return eng_lemmas.items()

    def image(self, subs=False):
        return self.subbed_bliss_image(subs=subs)

    def word_image(self):
        """
        Returns a thumbnail Image of this TranslationWord's
        Blissymbol, with height as its translator's image_heights.
        ~
        If this TranslationWord's Blissymbol is None,
        returns an Image with its word as text instead.

        :return: Image, image of this TW's Blissymbol
        """
        return self.translator.word_image(self.word, subs=False)

    def subtitle(self):
        """
        Returns a thumbnail Image of this TranslationWord's
        Blissymbol, with height as its translator's image_heights.
        ~
        If this TranslationWord's Blissymbol is None,
        returns an Image with its word as text instead.

        :return: Image, image of this TW's Blissymbol
        """
        return self.translator.trim(image=self.translator.word_image(self.word, subs=True))

    def overlay_indicators(self, img):
        wikt_pos = self.translator.convert_pos_to_wikt(self.pos)
        terms = self.translator.lang_parser.find_terms(self.word, wikt_pos, self.language, add_new=False)
        if 'plural' in terms:
            if 'singular' in terms:
                # if can be plural or singular, remove plural
                if 'NNS' not in self.pos:
                    terms.remove('plural')
            else:
                self.pos.add('NNS')
        if len(terms) != 0:
            if len({'neutral', 'feminine', 'masculine'}.intersection(terms)) >= 2:
                if 'neutral' in terms:
                    terms.remove('neutral')
                if 'feminine' in terms:
                    terms.remove('feminine')
                if 'masculine' in terms:
                    terms.remove('masculine')
            if len({'past', 'present', 'future'}.intersection(terms)) >= 2:
                if 'past' in terms:
                    terms.remove('past')
                if 'present' in terms:
                    terms.remove('present')
                if 'future' in terms:
                    terms.remove('future')
            if len({'first-person', 'second-person', 'third-person'}.intersection(terms)) >= 2:
                if 'first-person' in terms:
                    terms.remove('first-person')
                if 'second-person' in terms:
                    terms.remove('second-person')
                if 'third-person' in terms:
                    terms.remove('third-person')
            indicators = ["indicator_(" + INDICATORS_MAP[t] + ")" for t in terms if t in INDICATORS_MAP]
            if len(indicators) != 0:
                return self.blissymbol.overlay_indicators(img, indicators)
        return img

    def subbed_bliss_image(self, subs=False):
        """
        Returns this TranslationWord's Blissymbol subtitled with its word.
        ~
        If subs is set to False, output Image has no subtitles, but
        still offsets as if there were.

        :param subs: bool, whether to subtitle output image
        :return: Image, subtitled Blissymbol image
        """
        if self.has_blissymbol():
            img = self.overlay_indicators(self.blissymbol.image())
        else:
            subs = False  # never subtitle a word with itself
            img = self.word_image()

        subtitle = self.subtitle()
        if not subs:
            subtitle = self.translator.blank_image(1, subtitle.size[1])
        subtitle_h = self.translator.sub_heights()

        if subtitle.size[1] != subtitle_h:
            subtitle_fill = self.translator.blank_image(subtitle.size[0], max(0, subtitle_h - subtitle.size[1]))
            subtitle = self.translator.above(subtitle_fill, subtitle)

        img = self.translator.above(img, subtitle)
        return img

    def set_pos(self, pos):
        """
        Sets this TranslationWord's part-of-speech
        tag to given pos.

        :param pos: str or Iterable, TW's part(s) of speech
        :return: None
        """
        self.pos = set(pos) if type(pos) != str else {pos}

    def has_blissymbol(self):
        """
        Returns whether this TranslationWord has a blissymbol.

        :return: bool, whether TW has Bliss translation
        """
        return (self.blissymbol is not None) and self.blissymbol.valid_filename()

    @property
    def bliss_name(self):
        """
        Returns this TranslationWord's blissymbol's name.

        :return: str, TW's Blissymbol's name
        """
        if self.blissymbol is not None:
            return self.blissymbol.bliss_name
        else:
            return ""

    def get_blissymbol_derivations(self):
        """
        Returns a list of this TranslationWord's blissymbol's
        derivations.

        :return: List[str], TW's blissymbol's derivations
        """
        if self.blissymbol is not None:
            return self.blissymbol.derivations
        else:
            return []

    def add_new_derivations(self):
        """
        Prompts user for a list of Blissymbol derivations approximating
        the meaning of this TranslationWord.
        ~
        Returns a list of Blissymbol names as strings.

        :param trans_word: TranslationWord, word to enter derivations for
        :return: List[str], list of Blissymbol names for entered derivations
        """
        keep_going = True
        derivations = []
        eng_lemma = self.eng_lemmas[0]

        print("\n")
        print(eng_lemma)
        print("-" * len(eng_lemma))

        while keep_going:
            print("Please enter the correct Blissymbol derivation(s) for " +
                  eng_lemma + ", each separated by a comma and a space. ")
            user_deriv = str(input(""))

            if len(user_deriv) == 0:
                print(eng_lemma + " will not be translated.\n")
                return derivations
            else:
                keep_going = False
                user_derivs = user_deriv.split(", ")

                for deriv in user_derivs:
                    blissword = self.word_to_blissword(deriv)

                    if blissword is not None:
                        print(deriv + " is ... a valid bliss word :)")
                        derivations.append(blissword)
                    else:
                        print(deriv + " is ... an invalid bliss word :(")

                    keep_going = keep_going or blissword is None

                    if keep_going:
                        print("\nI'm sorry, one of the Blissymbol derivations you entered is invalid. " +
                              "Please try using a different synonym.\n")
                        continue

        derivation = self.words_to_derivation(derivations)
        blissymbol = self.translator.blissymbol(eng_lemma, pos=self.pos, derivation=derivation)
        self.reset_blissymbol(blissymbol)
        return self.blissymbol.derivations

    def words_to_derivation(self, words):
        """
        Returns this list of words as a Blissymbols derivation.
        ~
        A Blissymbols derivation begins and ends with parentheses
        and contains a list of names of Blissymbols inside,
        separated by addition signs.
        ~
        e.g. words_to_derivation(["rodent", "ear"]) -> "(rodent + ear)"

        :param words: List[str], words for a Blissymbol derivation
        :return: str, words joined as a Blissymbol derivation
        """
        return "(" + " + ".join([self.translator.underscore(w) for w in words]) + ")"

    def word_to_blissword(self, word):
        """
        Returns the name of the Blissymbol for this word.

        :param word: str, word to find Blissymbol name for
        :return: str, name of Blissymbol for word
        """
        blissymbol = self.translator.word_to_blissymbol(word)

        if blissymbol is not None:
            return blissymbol.bliss_name
        else:
            return

    def reset_blissymbol(self, blissymbol):
        """
        Resets this TranslationWord's blissymbol to
        this blissymbol.

        :param blissymbol: Blissymbol, TW's Bliss translation
        :return: None
        """
        self.blissymbol = blissymbol

    def set_blissymbol(self, blissymbol):
        """
        Sets this TranslationWord's blissymbol to
        given blissymbol if it meets certain criteria.

        :param blissymbol: Blissymbol, TW's Bliss translation
        :return: None
        """
        if self.blissymbol is None:
            if any(p in blissymbol.pos for p in self.pos):
                self.blissymbol = blissymbol

    def init_blissymbol(self):
        """
        Initializes this TranslationWord's Blissymbol.
        ~
        If Blissymbol exists for this TranslationWord, returns
        a best guess definition from a BlissClassifier.

        :return: None
        """
        blissymbol = self.translator.word_to_blissymbol(self.lemma, pos=self.pos, lang=self.language)

        if blissymbol is not None:
            self.blissymbol = blissymbol
            return

        if len(self.lemmas) != 1:
            blissymbol = self.translator.words_to_blissymbol(self.lemmas, pos=self.pos, lang=self.language)
            if blissymbol is None:
                blissymbol = self.translator.words_to_blissymbol(self.lemmas, lang=self.language)
            if blissymbol is not None:
                self.blissymbol = blissymbol
                return

        if self.word != self.lemma:
            blissymbol = self.translator.word_to_blissymbol(self.word, pos=self.pos, lang=self.language)
            if blissymbol is not None:
                self.blissymbol = blissymbol
                self.lemmas = [self.word] + self.lemmas
                return

        if len(self.eng_lemmas) != 0:
            blissymbol = self.translator.words_to_blissymbol(self.eng_lemmas, pos=self.pos)
            if blissymbol is not None:
                self.blissymbol = blissymbol
                return

        if len(self.synsets) != 0:
            for synset in self.synsets:
                blissymbol = self.translator.lookup_blissnet(synset=synset)
                if blissymbol is not None:
                    self.blissymbol = blissymbol
                    return
            else:
                hypernym = self.translator.common_hypernym(self.synsets)
                if hypernym is not None:
                    self.blissymbol = self.translator.lookup_blissnet(synset=hypernym)
                    return
        else:
            blissymbol = self.translator.synsets_to_blissymbol(self.synsets)
            if blissymbol is not None:
                self.blissymbol = blissymbol
            else:
                self.find_blissymbol(machine_learn=False)
                self.add_blissymbol_translations()

    def find_blissymbol(self, machine_learn=False):
        """
        Finds this TranslationWord's Blissymbol
        according to whichever Blissymbol can be found.
        ~
        If self.blissymbol is not None, returns self.blissymbol.
        ~
        Else, if self.blissymbols is not None, returns
        first element of self.blissymbols.
        ~
        Otherwise, attempts to identify Blissymbol(s) for
        synonyms of this word.  If no synonyms with Blissymbol
        definitions exist, return a best guess definition from
        a BlissClassifier.

        :param machine_learn: bool, whether to predict Blissymbol with classifier
        :return: None
        """
        if self.blissymbol is None:
            self.blissymbol = self.translator.words_to_blissymbol(self.eng_lemmas, "English", self.pos)

            if self.blissymbol is None:
                self.blissymbol = self.translator.words_to_blissymbol(self.eng_lemmas, "English")

            if self.blissymbol is None:
                if machine_learn and self.translator.is_word(self.word):
                    self.predict_blissymbol()

    def add_blissymbol_translations(self):
        """
        Adds this TranslationWord's lemma and eng_lemma as translations
        to its Blissymbol.

        :return: None
        """
        if self.blissymbol is not None:
            self.blissymbol.add_translations("English", self.eng_lemmas)
            self.blissymbol.add_translation(self.language, self.lemma)
            self.translator.add_bliss_entry(self.blissymbol)

    def find_bliss_etymologies(self, word):
        """
        Returns the names of Blissymbols for all this word's etymologies.

        :param etym: str, a word's etymology
        :return: List[str], Blissymbol names for word's etymologies
        """
        etyms = self.translator.lang_parser.find_word_etymology(word)
        bliss_etyms = []

        if etyms is not None:
            for etym in etyms:
                bliss_etym = self.find_bliss_etymology(etym)
                if bliss_etym is not None:
                    bliss_etyms.append(bliss_etym)

        return bliss_etyms

    def find_bliss_etymology(self, etym):
        """
        Returns the name of a Blissymbol for this etymology, if one exists.
        Otherwise, returns None.

        :param etym: str, a word's etymology
        :return: str, name of Blissymbol for etym
        """
        if self.translator.in_bliss_dict(etym, self.language):
            return etym
        else:
            etym_stemwords = self.translator.lang_parser.find_stemwords(etym, self.language)

            if len(etym_stemwords) == 0 and etym[0] == u"-":
                clean_etym = etym[1:]
                return self.find_bliss_etymology(clean_etym)
            if len(etym_stemwords) != 0:
                return etym_stemwords[0]

    def debug_lemma(self):
        """
        Prompts the user to verify this TranslationWord's lemma
        and change it manually if needed.

        :return: None
        """
        print(self.language + u": " + self.lemma)
        print("If the above is the true lemma for", self.word, ", press enter.\n",
              "Otherwise, enter", self.word, "'s true lemma(s), separated by commas if necessary.")
        ans = str(input(""))

        if ans != "":
            self.lemmas = ans.split(",")

    def predict_blissymbol(self):
        """
        Returns a BlissClassifier's best guess definition for
        this TranslationWord's Blissymbol.

        :return: Blissymbol, this word's Blissymbol
        """
        classifier = self.translator.classifier
        bliss_words = classifier.predict_word(self)
        lemma = self.translator.underscore(self.lemma)
        eng_lemma = self.translator.underscore(self.eng_lemmas[0])

        if len(bliss_words) == 0:
            return
        if len(bliss_words) == 1:
            bliss_name = bliss_words[0]
        else:
            bliss_name = eng_lemma

        if len(bliss_words) > 0:
            derivation = self.words_to_derivation(bliss_words)
            print("making Blissymbol with " + bliss_name)
            translations = dict()
            translations["English"] = self.eng_lemmas
            translations[self.language] = [lemma]
            blissymbol = self.translator.blissymbol(bliss_name=bliss_name,
                                                    pos=self.pos,
                                                    derivation=derivation,
                                                    translations=translations,
                                                    num=0)
            blissymbol.add_synsets(self.synsets)
            self.reset_blissymbol(blissymbol)
            self.translator.add_bliss_entry(self.blissymbol)
            return self.blissymbol

    def find_english_translations(self, word, pos=None):
        """
        Returns all English translations of this word from its synsets.
        ~
        If no synsets can be found and wikt is True, searches Wiktionary
        for English translations.
        ~
        If no English translations are found, returns None.

        :param word: str, word to translate to English
        :param pos: str or Iterable, word's Penn Treebank part(s) of speech
        :return: List[str], word's English translations
        """
        '''
        synsets = self.translator.word_synsets(word, pos, self.translator.lang_code(self.language))
        # check synsets for English translations first
        if len(synsets) != 0:
            eng_lemmas = self.translator.ordered_set([])
            for synset in synsets:
                eng_lemmas.update(synset.lemma_names())
            eng_lemmas = eng_lemmas.intersections()  # most common lemmas
            if len(eng_lemmas) != 0:
                return eng_lemmas
        '''
        # if synsets provide no lemmas, check Wiktionary
        return self.translator.find_english_translations(word, pos, self.language)

    def add_eng_lemma(self, eng_lemma):
        """
        Adds eng_lemma to this TranslationWord's find_eng_lemmas.

        :param eng_lemma: str, English lemma synonymous with this TW's lemma
        :return: None
        """
        self.eng_lemmas.append(eng_lemma)

    def find_synsets(self):
        """
        Returns a list of WordNet synsets for this TranslationWord.
        ~
        When this TranslationWord is English, find synsets using trans_word's
        part-of-speech tag.  Else, find synsets in every part of speech.

        WordNet lookup link here:
        http://wordnetweb.princeton.edu/perl/webwn?s=&sub=Search+WordNet

        :return: List[Synset], the word's synsets
        """
        synsets = self.translator.words_synsets(self.lemmas, pos=self.pos, lang_code=self.translator.lang_code)

        if len(synsets) == 0 and self.language != "English":
            synsets += self.translator.word_synsets(self.lemma, lang_code=self.translator.lang_code)
            synsets += self.translator.words_synsets(self.eng_lemmas, pos=self.pos, lang_code="eng")

        return synsets

    def __str__(self):
        """
        Returns a string representation to print to a user.

        :return: str, string representation of this Blissymbol
        """
        return "word:\t\t" + str(self.word) + "\n" + \
               "pos:\t\t" + str(self.pos) + "\n" + \
               "lemma:\t\t" + str(self.lemma) + "\n" + \
               "eng lemmas:\t\t" + str("    ".join(self.eng_lemmas) if self.eng_lemmas is not None else "") + "\n" + \
               "bliss:\t\t" + str(self.bliss_name) + "\n"

    __repr__ = __str__


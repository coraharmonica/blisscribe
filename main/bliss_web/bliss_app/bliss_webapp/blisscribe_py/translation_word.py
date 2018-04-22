# -*- coding: utf-8 -*-
"""
TRANSLATION_WORD:

    A class for representing a word-in-translation as
    part of a BlissTranslator.
"""
from bliss_images import *


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
    def __init__(self, word, pos, translator, language=None, debug=False):
        self.translator = translator
        self.language = self.translator.language if language is None else language
        self.debug = debug
        self.word = self.translator.unicodize(word)
        self.pos = pos
        self.lemma = self.find_lemma(self.word, self.language, self.pos)
        self.blissymbol = None
        self.synsets = self.find_synsets()
        self.synset_idx = 0
        self.synset = self.find_synset()
        self.init_pos()
        self.eng_lemmas = None
        self.init_blissymbol()

    def init_pos(self):
        """
        If language is not English, this method cross-references
        this TranslationWord's pos with other likely parts of speech
        to determine most likely part of speech.

        :return: None
        """
        if self.translator.language != "English":
            self.get_multilingual_pos()

    def init_lang_parser(self):
        """
        Returns this TranslationWord's translator's LanguageParser.

        :return: LanguageParser, a parser for Wiktionary lookups
        """
        return self.translator.init_lang_parser()

    def find_pos_abbrev(self):
        """
        Returns this TranslationWord's abbreviated part-of-speech tag.

        :return: str, TW's pos tag
        """
        return self.translator.abbreviate_pos(self.pos)

    def set_pos(self, pos):
        """
        Sets this TranslationWord's part-of-speech
        tag to given pos.

        :param pos: str, TW's pos tag
        :return: None
        """
        self.pos = pos

    def get_multilingual_pos(self):
        """
        Only invoked when language is not English.
        ~
        Returns part-of-speech tag for this
        non-English TranslationWord.

        :return: str, TW's pos tag
        """
        return self.translator.get_word_tag(self)

    def is_noun(self):
        """
        Returns True if word is a noun, False otherwise.

        :param trans_word: TranslationWord, word to test whether a noun
        :return: bool, whether given word is a noun
        """
        return self.pos[0:2] == "NN"

    def is_plural_noun(self):
        """
        Returns True if word is a plural noun, False otherwise.

        :param trans_word: TranslationWord, word to test whether a plural noun
        :return: bool, whether given word is a plural noun
        """
        return self.pos == "NNS"

    def is_proper_noun(self):
        """
        Returns True if word is a proper noun, False otherwise.

        :param trans_word: TranslationWord, word to test whether a proper noun
        :return: bool, whether given word is a proper noun
        """
        return self.pos == "NNP"

    def is_verb(self):
        """
        Returns True if word is a verb, False otherwise.

        :param trans_word: TranslationWord, word to test whether a verb
        :return: bool, whether given word is a verb
        """
        return self.pos[0:2] == "VB"

    def is_adj(self):
        """
        Returns True if word is an adjective, False otherwise.

        :param trans_word: TranslationWord, word to test whether an adjective
        :return: bool, whether given word is an adjective
        """
        return self.pos[0:2] == "JJ"

    def is_adv(self):
        """
        Returns True if word is an adverb, False otherwise.

        :param trans_word: TranslationWord, word to test whether an adverb
        :return: bool, whether given word is an adverb
        """
        return self.pos[0:2] == "RB"

    def get_lemma(self):
        """
        Returns this TranslationWord's lemma.

        :return: str, TW's lemma
        """
        return self.lemma

    def has_blissymbol(self):
        """
        Returns whether this TranslationWord has a blissymbol.

        :return: bool, whether TW has Bliss translation
        """
        return (self.blissymbol is not None) and self.blissymbol.valid_filename()

    def get_bliss_name(self):
        """
        Returns this TranslationWord's blissymbol's name.

        :return: str, TW's Blissymbol's name
        """
        if self.blissymbol is not None:
            return self.blissymbol.get_bliss_name()
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
            return list()

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
        derivations = list()
        self.init_eng_lemmas()
        eng_lemma = self.eng_lemmas[0]

        print("\n")
        print(eng_lemma)
        print("-" * len(eng_lemma))

        while keep_going:
            print("Please enter the correct Blissymbol derivation(s) for " +
                  eng_lemma + ", each separated by a comma and a space. ")
            user_deriv = str(raw_input(""))

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
        blissymbol = self.translator.make_blissymbol(eng_lemma + ".png", pos=self.pos, derivation=derivation)
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
        return "(" + " + ".join([self.translator.underscore_word(w) for w in words]) + ")"

    def word_to_blissword(self, word):
        """
        Returns the name of the Blissymbol for this word.

        :param word: str, word to find Blissymbol name for
        :return: str, name of Blissymbol for word
        """
        blissymbol = self.translator.word_to_blissymbol(word)

        if blissymbol is not None:
            return blissymbol.get_bliss_name()
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
            if self.pos in blissymbol.get_parts_of_speech():
                self.blissymbol = blissymbol

    def init_blissymbol(self):
        """
        Initializes this TranslationWord's Blissymbol.
        ~
        If Blissymbol exists for this TranslationWord, returns
        a best guess definition from a BlissClassifier.

        :return: None
        """
        blissymbol = self.translator.word_to_blissymbol(self.lemma, self.language)
        if blissymbol is not None:
            self.blissymbol = blissymbol

        blissymbol = self.translator.word_to_blissymbol(self.word, self.language)
        if blissymbol is not None:
            self.blissymbol = blissymbol
            self.lemma = self.word
        else:
            self.init_eng_lemmas()
            print self.word, "ENGLISH LEMMAS:", self.eng_lemmas
            if self.eng_lemmas is not None:
                self.blissymbol = self.translator.words_to_blissymbol(self.eng_lemmas, "English", self.pos)
                print "   BLISSYMBOL:", self.blissymbol

            self.add_blissymbol_translations()

    def find_blissymbol(self):
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

        :return: None
        """
        if self.blissymbol is None:
            self.init_eng_lemmas()
            if self.eng_lemmas is not None:
                self.blissymbol = self.translator.words_to_blissymbol(self.eng_lemmas, "English", self.pos)
            elif self.translator.is_word(self.word) and self.translator.classifier is not None:
                self.predict_blissymbol()

    def add_blissymbol_translations(self):
        """
        Adds this TranslationWord's lemma and eng_lemma as translations
        to its Blissymbol.

        :return: None
        """
        if self.blissymbol is not None:
            self.init_eng_lemmas()
            self.blissymbol.add_translations("English", self.eng_lemmas)
            self.blissymbol.add_translation(self.language, self.lemma)
            self.translator.add_bliss_entry(self.blissymbol)

    def find_bliss_etymologies(self, word):
        """
        Returns the names of Blissymbols for all this word's etymologies.

        :param etym: str, a word's etymology
        :return: List[str], Blissymbol names for word's etymologies
        """
        lang_parser = self.init_lang_parser()
        etyms = lang_parser.find_word_etymology(word)
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
        if self.in_bliss_dict(etym, self.language):
            return etym
        else:
            lang_parser = self.init_lang_parser()
            etym_stemwords = lang_parser.find_stemwords(etym, self.language)

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
        print("If the above is the true lemma for " + self.word + ", press enter." +
              "\nOtherwise, enter " + self.word + "'s true lemma.")
        ans = str(raw_input(""))

        if ans != "":
            self.lemma = ans

    def predict_blissymbol(self):
        """
        Returns a BlissClassifier's best guess definition for
        this TranslationWord's Blissymbol.

        :return: Blissymbol, this word's Blissymbol
        """
        '''
        if self.translator.safe_translate:
            self.debug_lemma()
            self.add_eng_lemma(self.find_eng_lemma(debug=self.translator.translate_all))
            entry = self.translator.words_to_blissymbol(self.eng_lemmas, "English")

            if entry is not None:
                print("Success: " + self.eng_lemmas[0] + " in English bliss dict!")
                return entry

            entry = self.translator.word_to_blissymbol(self.lemma, self.language)
            if entry is not None:
                print(u"Success: " + self.lemma + u" in bliss dict!")
                return entry
        '''
        self.init_eng_lemmas()
        classifier = self.translator.classifier
        bliss_words = classifier.predict_word(self, debug=self.debug)
        lemma = self.translator.underscore_word(self.lemma)
        eng_lemma = self.translator.underscore_word(self.eng_lemmas[0])

        if len(bliss_words) == 0:
            return
        if len(bliss_words) == 1:
            img_filename = bliss_words[0]
        else:
            img_filename = eng_lemma

        if len(bliss_words) > 0:
            derivation = self.words_to_derivation(bliss_words)
            print("making Blissymbol with " + img_filename)
            translations = dict()
            translations["English"] = self.eng_lemmas
            translations[self.language] = [lemma]
            blissymbol = self.translator.make_blissymbol(img_filename=img_filename + ".png",
                                                         pos=self.pos,
                                                         derivation=derivation,
                                                         translations=translations)
            blissymbol.add_synsets(self.synsets)
            self.reset_blissymbol(blissymbol)
            self.translator.add_bliss_entry(self.blissymbol)
            return self.blissymbol

    def get_filename(self):
        """
        If this Blissymbol has an associated image file,
        return the image filename including extension.
        ~
        If this Blissymbol has no associated image file,
        return None.

        :return: str, this Blissymbol's image filename
        """
        if self.blissymbol:
            return self.translator.unicodize(self.blissymbol.img_filename)

    def init_eng_lemmas(self):
        if self.eng_lemmas is None:
            self.eng_lemmas = self.find_english_translations(self.word, self.pos)

    def find_lemma(self, word, language, pos):
        """
        Retrieves this Blissymbol's lemma,
        i.e., its "dictionary entry" form.
        ~
        Determines lemma from this Blissymbol's word and pos.

        :return: str, this Blissymbol's lemma
        """
        if self.language != "English":
            lemma = self.translator.lemmatize(word, language)
        else:
            lemma = self.translator.lemmatize(word, pos)
        return lemma

    def find_english_translation(self, word, pos=None):
        """
        Returns the English translation of this word from Wiktionary.
        ~
        If no English translation is found, returns None.

        :param word: str, word to translate to English
        :param pos: str, word's part-of-speech
        :return: str, word's English translation
        """
        eng_lemmas = self.find_english_translations(word, pos)
        blissymbol = self.translator.words_to_blissymbol(eng_lemmas, "English", pos)
        return blissymbol.get_translation("English")[0]

    def find_english_translations(self, word, pos=None):
        """
        Returns all English translations of this word from Wiktionary.
        ~
        If no English translations are found, returns None.

        :param word: str, word to translate to English
        :param pos: str, word's Penn Treebank part-of-speech
        :return: Set(str), word's English translations
        """
        lang_parser = self.init_lang_parser()
        wikt_pos = self.translator.convert_pos_to_wikt(pos)
        eng_lemmas = lang_parser.find_english_translations(word, language=self.language, pos=wikt_pos)
        if len(eng_lemmas) == 0:
            lemma = self.translator.lemmatize(word, language=self.language, pos=pos)
            eng_lemmas = lang_parser.find_english_translations(lemma, language=self.language, pos=wikt_pos)
        return eng_lemmas

    def find_synset_synonyms(self, lemma, synsets, debug=False):
        """
        Returns the appropriate English lemma from synsets for this lemma.
        ~
        If debug is True, prompts user for input on best synset.
        Otherwise, chooses automatically.

        :param lemma: str, lemma to translate using synsets
        :param synsets: List[Synset], synsets to translate lemma with
        :param debug: bool, whether to take user input
        :return: str, lemma's synonym
        """
        if debug:
            self.debug_lemma()

        try:
            synsets[0]
        except IndexError:  # no English lemma exists thus far
            if debug:
                print(lemma)
                print("This word appears to have no English translation.  " +
                      "If you can provide one, enter it here. Otherwise, press enter.")
                answer = str(raw_input(""))
                print("")
                if answer != "":
                    eng_lemma = answer
                else:
                    return
            else:
                return
        else:
            if debug and len(synsets) > 1:
                # allows user to select which synset corresponds with this word
                # if multiple synsets apply
                print(lemma)
                print("This word matches the following English synsets:")
                idx = 1
                for synset in synsets:
                    print idx, synset.lemma_names(), synset.definition()
                    idx += 1
                while not (0 <= idx < len(synsets)):
                    print("Which index does this match?  If none is appropriate, enter 0.")
                    idx = int(input(""))
                    if idx == 0:
                        return
                    else:
                        idx -= 1
            elif len(synsets) != 0:
                idx = 0
            else:
                print("No English synsets found.")
                return

            synset = synsets[idx]
            self.set_synset_idx(idx)
            synonyms = synset.lemma_names()
            eng_lemma = synonyms[0]

        eng_lemma = self.translator.unicodize(eng_lemma)
        return eng_lemma

    def find_eng_lemmas(self):
        """
        Returns a list of English lemmas for this TranslationWord's lemma.

        :return: List[str], English lemmas
        """
        if self.language == "English":
            eng_lemmas = [self.lemma]
        else:
            if not self.translator.is_word(self.lemma):
                return
            else:
                eng_lemmas = self.find_english_translations(self.lemma, self.pos)

        return eng_lemmas

    def add_eng_lemma(self, eng_lemma):
        self.init_eng_lemmas()
        self.eng_lemmas.append(eng_lemma)

    def in_bliss_dict(self, word, language):
        """
        Returns True if this word is in this TranslationWord's
        BlissTranslator's Blissymbols dictionary for this language.
        Otherwise, returns False.

        :param word: str, word to lookup in bliss_dict
        :param language: str, language of Blissymbols dict
        :return: bool, whether word found in bliss_dict
        """
        return self.translator.in_bliss_dict(word, language)

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
        word = self.lemma
        use_pos = (self.language == "English")  # use_pos False for non-English languages until better tagging

        if use_pos:
            pos = self.pos
            pos = self.translator.abbreviate_pos(pos)
            synsets = self.translator.lookup_word_synsets(word, pos=pos, language=self.translator.language)

            if not self.translator.safe_translate:
                synsets += self.translator.lookup_word_synsets(word, language=self.translator.language)
        else:
            synsets = self.translator.lookup_word_synsets(word, language=self.translator.language)

        return synsets

    def set_synset(self, synset):
        """
        Sets this TranslationWord's synset to this synset.

        :param synset: Synset, synset to set as self.synset
        :return: None
        """
        self.synset = synset

    def set_synsets(self, synsets):
        """
        Sets this TranslationWord's synsets list to given synsets.

        :param synsets: List[Synset], synsets
        :return: None
        """
        self.synsets = synsets

    def set_synset_idx(self, idx):
        """
        Sets this TranslationWord's synset_idx to given idx.
        ~
        Reconfigures self.synset and self.synset_id according
        to new synset_idx.
        ~
        N.B. 0 <= self.synset_idx <= len(self.synsets)

        :param idx: int, index to set as synset_idx
        :return: None
        """
        if len(self.synsets) > 0:
            assert 0 <= idx < len(self.synsets)
            self.synset_idx = idx
            self.synset = self.find_synset()

    def find_synset(self):
        """
        Returns the synset in this TranslationWord's synsets
        at synset_idx.

        :return: Synset, this TW's WN synset
        """
        try:
            return self.synsets[self.synset_idx]
        except IndexError:
            return

    def get_synset(self):
        """
        Returns this TranslationWord's corresponding Wordnet Synset.

        :return: Synset, this TW's WN synset
        """
        return self.synset

    def __str__(self):
        """
        Returns a string representation to print to a user.

        :return: str, string representation of this Blissymbol
        """
        return "word:\t\t" + (self.word).encode('ascii', 'replace') + "\n" + \
               "pos:\t\t" + self.pos + "\n" + \
               "lemma:\t\t" + (self.lemma).encode('ascii', 'replace') + "\n" + \
               "bliss:\t\t" + (self.get_bliss_name()).encode('ascii', 'replace') + "\n"

    __repr__ = __str__


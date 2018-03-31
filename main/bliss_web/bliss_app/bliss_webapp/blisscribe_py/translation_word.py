# -*- coding: utf-8 -*-
"""
TRANSLATION_WORD:

    A class for representing a word-in-translation as
    part of a BlissTranslator.
"""


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
        self.lang_parser = None
        self.language = self.translator.language if (language is None) else language
        self.debug = debug
        self.word = self.translator.unicodize(word)
        self.pos = pos
        self.pos_abbrev = self.find_pos_abbrev()
        self.lemma = self.find_lemma()
        self.init_pos()
        self.bliss_dict = self.translator.bliss_dict
        self.eng_bliss_dict = self.translator.eng_bliss_dict
        self.blissymbols = None
        self.blissymbol = None
        self.synonyms = list()
        self.synsets_lemmas = list()
        self.synsets = self.find_synsets()
        self.synset_idx = 0
        self.synset = self.find_synset()
        self.synset_id = self.init_synset_id()
        self.eng_lemma = self.find_eng_lemma(debug)
        self.init_blissymbols()
        self.init_blissymbol()
        self.wn_defn = None
        self.wn_idx = None

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
        Initializes this TranslationWord's lang_parser as its
        translator's LanguageParser and returns None.

        :return: None
        """
        self.lang_parser = self.translator.init_lang_parser()

    def find_pos_abbrev(self):
        """
        Returns this TranslationWord's abbreviated part-of-speech tag.

        :return: str, TW's pos tag
        """
        return self.translator.abbreviate_tag(self.pos)

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
        Returns the result as a set of strings.

        :param trans_word: TranslationWord, word to enter derivations for
        :return: List[str], list of entered derivations
        """
        keep_going = True
        derivations = list()
        eng_lexeme = self.eng_lemma
        print("\n")
        print(eng_lexeme)
        print("-" * len(eng_lexeme))

        while keep_going:
            print("Please enter the correct Blissymbol derivation(s) for " +
                  eng_lexeme + ", each separated by a comma and a space. ")
            user_derivs = raw_input("")

            if len(user_derivs) == 0:
                print(eng_lexeme + " will not be translated.\n")
                return derivations
            else:
                user_derivs = str(user_derivs)
                user_derivs = user_derivs.split(", ")
                keep_going = False
                for user_deriv in user_derivs:
                    blissymbol = self.translator.word_to_blissymbol(user_deriv)
                    blissymbols = self.translator.lookup_eng_bliss_dict(user_deriv)
                    is_bliss_word = blissymbol is not None
                    in_bliss_dict = is_bliss_word and len(blissymbols) > 0
                    if in_bliss_dict:
                        print(user_deriv + " is ... a valid bliss word :)")
                        derivations.append(blissymbols.pop().get_bliss_name())
                    elif is_bliss_word:
                        print(user_deriv + " is ... a valid bliss word :)")
                        derivations.append(blissymbol.get_bliss_name())
                    else:
                        print(user_deriv + " is ... an invalid bliss word :(")
                    keep_going = keep_going or not (is_bliss_word or in_bliss_dict)
                    if keep_going:
                        print("\nI'm sorry, one of the Blissymbol derivations you entered is invalid. " +
                              "Please try using a different synonym.\n")
                        continue

        return self.translator.remove_duplicates(derivations)

    def overwrite_blissymbol(self, blissymbol):
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

    def set_blissymbols(self, blissymbols):
        """
        Sets this TranslationWord's blissymbols to
        given blissymbols.

        :param blissymbols: List[Blissymbol], TW's Bliss translation
        :return: None
        """
        neutrals = [bs for bs in blissymbols if bs.is_neutral()]

        if len(neutrals) != 0:
            self.blissymbols = neutrals
        else:
            self.blissymbols = blissymbols

    def caps_in_bliss_dict(self, word):
        """
        If this word with the first letter capitalized
        is in the Bliss dictionary, return that word.
        Otherwise, return None.

        :param word: str, word to check whether capitalized
            in Bliss dict
        :return: str, word capitalized if in Bliss dict
        """
        caps = word.title()

        if self.in_bliss_dict(caps):
            return caps

    def find_synonyms(self):
        """
        Browses this TranslationWord's synsets to see if
        any synset synonyms are in bliss_dict and have
        the same part of speech.
        ~
        If so, sets TranslationWord image to first match
        and adds synset synonyms to self.synonyms.
        ~
        If no matches found with same part of speech,
        lookup synset synonyms with any part of speech
        in bliss_dict. Once a match found, sets this
        TranslationWord's image to match and halts.

        :return: None
        """
        for synset in self.synsets_lemmas:
            if self.in_bliss_dict(synset):
                self.set_blissymbols(self.bliss_dict[synset])
                for blissymbol in self.blissymbols:
                    if self.pos in blissymbol.get_parts_of_speech():
                        self.synonyms += blissymbol.get_translation(self.language)
                        self.overwrite_blissymbol(blissymbol)
                break

        if self.blissymbol is None:
            for synset in self.synsets_lemmas:
                if self.in_bliss_dict(synset):
                    self.set_blissymbols(self.bliss_dict[synset])
                    for blissymbol in self.blissymbols:
                        if self.blissymbol is None:
                            self.blissymbol = blissymbol
                    break

    def init_blissymbol(self):
        """
        Initializes this TranslationWord's corresponding Blissymbol
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
        a BlissLearner.

        :return: None
        """
        blissymbol = self.translator.word_to_blissymbol(self.lemma, self.language)

        if blissymbol is not None:
            self.blissymbol = blissymbol
        else:
            self.find_synonyms()

            if self.blissymbol is None:
                if self.blissymbols is not None and len(self.blissymbols) != 0:
                    self.blissymbol = next(iter(self.blissymbols))
                elif self.translator.is_word(self.word) and self.translator.classifier is not None:
                    self.find_blissymbol()

            if self.blissymbol is None:
                self.init_lang_parser()
                if len(self.word) != 0 and not self.lang_parser.contains_punct(self.word):
                    filename = self.word + ".png"
                    pos = self.pos
                    derivs = self.find_bliss_etymologies(self.word)
                    if derivs is not None:
                        derivation = "(" + " + ".join(derivs) + ")"
                        blissymbol = self.translator.make_blissymbol(filename, pos, derivation)
                        if blissymbol.valid_filename():
                            self.blissymbol = blissymbol

            if self.blissymbol is not None:
                self.blissymbol.add_translation("English", self.eng_lemma)
                self.blissymbol.add_translation(self.language, self.lemma)

    def find_bliss_etymologies(self, word):
        """
        Returns the names of Blissymbols for all this word's etymologies.

        :param etym: str, a word's etymology
        :return: List[str], Blissymbol names for word's etymologies
        """
        etyms = self.lang_parser.find_word_etymology(word)
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
        if self.in_bliss_dict(etym):
            return etym
        else:
            etym_stemwords = self.lang_parser.find_stemwords(etym, self.language)
            if len(etym_stemwords) == 0 and etym[0] == u"-":
                clean_etym = etym[1:]
                return self.find_bliss_etymology(clean_etym)
            if len(etym_stemwords) != 0:
                return etym_stemwords[0]

    def init_blissymbols(self):
        """
        If this TranslationWord's lemma is in bliss_dict,
        sets self.blissymbol to the first match in self.blissymbols.

        :return: None
        """
        bliss_dict = self.bliss_dict

        if self.in_bliss_dict(self.lemma):
            lemma = self.lemma

        elif self.in_bliss_dict(self.word):
            self.lemma = self.word
            lemma = self.lemma

        elif self.in_eng_bliss_dict(self.eng_lemma):
            lemma = self.eng_lemma
            bliss_dict = self.translator.eng_bliss_dict

        else:
            lemma_title = self.lemma.title()
            caps = self.in_bliss_dict(lemma_title)

            if caps:
                lemma = lemma_title
            else:
                if len(self.eng_lemma) != 0:
                    lemma = self.eng_lemma
                else:
                    lemma = ""

        if len(lemma) != 0 and self.in_bliss_dict(lemma):
            self.set_blissymbols(bliss_dict[lemma])

            for blissymbol in self.blissymbols:
                translations = [self.translator.unicodize(translation)
                                for translation in blissymbol.get_translation("English")]
                self.synonyms += translations
                self.set_blissymbol(blissymbol)

    def verify_lemma(self):
        print(self.language + u": " + self.lemma)
        print("If the above is the true lemma for " + self.word + ", press enter." +
              "\nOtherwise, enter " + self.word + "'s true lemma.")
        ans = str(raw_input(""))

        if ans != "":
            self.lemma = ans

        return self.lemma

    def find_blissymbol(self):
        """
        Returns a BlissLearner's best guess definition for
        this TranslationWord's Blissymbol.

        :return: Blissymbol, this word's Blissymbol
        """
        if self.translator.safe_translate:
            self.verify_lemma()
            self.eng_lemma = self.find_eng_lemma(debug=self.translator.translate_all)

            if self.eng_lemma in self.eng_bliss_dict:
                print("Success: " + self.eng_lemma + " in English bliss dict!")
                return self.translator.word_to_blissymbol(self.eng_lemma)
            elif self.lemma in self.bliss_dict:
                print(u"Success: " + self.lemma + u" in bliss dict!")
                return self.translator.word_to_blissymbol(self.lemma, self.language)

        classifier = self.translator.classifier
        bliss_words = classifier.predict_word(self, debug=self.debug)
        lemma = self.lemma.replace(" ", "_")
        eng_lemma = self.eng_lemma.replace(" ", "_")

        if len(bliss_words) == 1:
            img_filename = bliss_words[0]
        elif len(bliss_words) == 0:
            return None
        else:
            img_filename = eng_lemma

        if len(bliss_words) > 0:
            derivation = ["("]
            idx = 0
            for bliss_word in bliss_words:
                derivation.append(bliss_word.replace(" ", "_"))
                idx += 1
                if idx < len(bliss_words):
                    derivation.append(" + ")
            derivation.append(")")
            derivation = "".join(derivation)
            print("making Blissymbol with " + img_filename)
            translations = dict()
            translations["English"] = [eng_lemma]
            translations.setdefault(self.language, [])
            translations[self.language].append(lemma)
            blissymbol = self.translator.make_blissymbol(img_filename=img_filename + ".png",
                                                         pos=self.pos,
                                                         derivation=derivation,
                                                         translations=translations)
            blissymbol.add_synsets(self.synsets)
            self.overwrite_blissymbol(blissymbol)
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

    def get_wordnet_defn(self):
        """
        Returns this TranslationWord's synset description.

        :return: str, this TranslationWord's synset description
        """
        if self.wn_defn is None:
            self.set_wordnet_defn(self.find_wordnet_defn())
        return self.wn_defn

    def set_wordnet_defn(self, wn_defn):
        """
        Sets this TranslationWord's synset description to given
        wn_defn.

        :param wn_defn: str, this TranslationWord's synset description
        :return: None
        """
        self.wn_defn = wn_defn

    def find_wordnet_defn(self):
        """
        Finds and returns this TranslationWord's synset description
        from WordNet.

        :return: str, this TranslationWord's synset description
        """
        synsets = self.translator.lookup_trans_word_synsets(trans_word=self)
        try:
            synset = synsets[0]
        except IndexError:
            return
        else:
            return self.translator.get_synset_defn(synset)

    def find_lemma(self):
        """
        Retrieves this Blissymbol's lemma,
        i.e., its "dictionary entry" form.
        ~
        Determines lemma from this Blissymbol's word and pos.

        :return: str, this Blissymbol's lemma
        """
        if self.language != "English":
            lemma = self.translator.lemmatize(self.word, language=self.language)
        else:
            lemma = self.translator.lemmatize(self.word, pos=self.pos)

        return lemma

    def init_eng_lemma(self):
        """
        Initializes this TranslationWord's English lemma by
        setting self.eng_lemma to whichever English lemma it
        can find.
        ~
        If debug is True, then the user will be prompted to
        identify the correct English lemma from a set of
        synsets.

        :return: None
        """
        self.eng_lemma = self.find_eng_lemma(self.debug)

    def find_eng_lemma(self, debug):
        """
        Returns this TranslationWord's corresponding English lemma.

        :return: str, English lemma
        """
        if self.language == "English":
            eng_lemma = self.lemma

        elif self.lemma in self.bliss_dict:
            blissymbols = self.bliss_dict[self.lemma]
            for bs in blissymbols:
                if bs.get_pos() == self.pos[:2] and bs.is_neutral():
                    blissymbol = bs
                    break
            else:
                blissymbol = next(iter(blissymbols))
            translations = blissymbol.get_translation("English")
            eng_lemma = translations[0]

        else:
            if len(self.lemma) == 0 or not self.translator.is_word(self.lemma):
                return self.lemma

            if self.translator.safe_translate:
                self.verify_lemma()

            synsets = self.translator.lookup_trans_word_synsets(self, use_pos=False)
            lemma = self.lemma

            try:
                synsets[0]
            except IndexError:  # no English lemma exists thus far
                if debug:
                    print(lemma)
                    print("This word appears to have no English translation.  " +
                          "If you can provide one, enter it here. Otherwise, press enter.")
                    answer = str(raw_input(""))
                    if answer != "":
                        lemma = answer
                    print
                else:
                    lemma = ""
            else:
                if debug and len(synsets) > 1:
                    # allows user to select which synset corresponds with this word
                    # if multiple synsets apply
                    print(lemma)
                    print("This word matches the following synsets:")
                    idx = 1
                    for synset in synsets:
                        print idx, synset.lemma_names(), synset.definition()
                        idx += 1
                    while not (0 <= idx < len(synsets)):
                        print("Which index does this match?  If none is appropriate, enter 0.")
                        idx = int(input(""))
                        if idx == 0:
                            return ""
                        else:
                            idx -= 1
                elif len(synsets) != 0:
                    idx = 0
                else:
                    print("No English synsets found.")
                    return ""

                synset = synsets[idx]
                self.set_synset_idx(idx)
                synonyms = synset.lemma_names()
                lemma = synonyms[0]

            eng_lemma = self.translator.unicodize(lemma)

        self.set_synset_id(self.init_synset_id())
        return eng_lemma

    def set_eng_lemma(self, eng_lemma):
        """
        Sets self.eng_lemma to given eng_lemma.

        :param eng_lemma: str, English lemma
        :return: None
        """
        self.eng_lemma = eng_lemma

    def in_bliss_dict(self, word):
        """
        Returns True if given word is in this TranslationWord's
        BlissTranslator's bliss_dict.  Otherwise, returns False.

        :param word: str, word to lookup in bliss_dict
        :return: bool, whether word found in bliss_dict
        """
        return self.translator.in_bliss_dict(word)

    def in_eng_bliss_dict(self, word):
        """
        Returns True if given word is in this TranslationWord's
        BlissTranslator's eng_bliss_dict.  Otherwise, returns False.

        :param word: str, word to lookup in eng_bliss_dict
        :return: bool, whether word found in eng_bliss_dict
        """
        return self.translator.in_eng_bliss_dict(word)

    def has_synonyms(self):
        """
        Returns True if any of this TranslationWord's synonyms
        are translatable to Blissymbols.  Else, returns False.

        :return: bool, whether this TranslationWord has synonyms
        """
        return self.translator.is_synonym_translatable(self)

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
            pos = self.translator.abbreviate_tag(pos)
            synsets = self.translator.lookup_word_synsets(word, pos=pos, lang=self.translator.language)

            if not self.translator.safe_translate:
                synsets += self.translator.lookup_word_synsets(word, lang=self.translator.language)
        else:
            synsets = self.translator.lookup_word_synsets(word, lang=self.translator.language)

        self.add_synsets_lemmas(self.translator.get_synsets_lemmas(synsets))
        return synsets

    def set_synsets(self, synsets):
        """
        Sets this TranslationWord's synsets list to given synsets.

        :param synsets: List[Synset], synsets
        :return: None
        """
        self.synsets = synsets
        for synset in synsets:
            self.add_synsets_lemmas(synset.lemma_names(lang=self.translator.lang_code))

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
            self.set_synset_id(self.find_synset_id(self.synset))

    def get_synset_id(self):
        """
        Returns this TranslationWord's synset_id.
        ~
        N.B. TranslationWord's synset_id allows this word to be considered
        synonymous with any other TranslationWord possessing the same synset_id.

        :return: str, a 9-digit Wordnet Synset ID
        """
        return self.synset_id

    def init_synset_id(self):
        """
        Finds a synset ID for this TranslationWord based on its synset.
        ~
        N.B. TranslationWord's synset_id corresponds to Synset.offset()
        in NLTK's Wordnet module, i.e., a 9-digit numerical identifier.

        :return: str, a 9-digit Wordnet Synset ID
        """
        return self.find_synset_id(self.synset)

    def find_synset_id(self, synset):
        """
        Finds a synset ID for this TranslationWord based on its synset.
        ~
        N.B. TranslationWord's synset_id corresponds to Synset.offset()
        in NLTK's Wordnet module, i.e., a 9-digit numerical identifier.

        :return: int, a 9-digit Wordnet Synset ID
        """
        return self.translator.get_synset_id(synset)

    def set_synset_id(self, id):
        """
        Sets this TranslationWord's synset_id to given id.
        ~
        N.B. TranslationWord's synset_id corresponds to Synset.offset()
        in NLTK's Wordnet module, i.e., a 9-digit numerical identifier.

        :param id: int, a 9-digit Wordnet Synset ID
        :return: None
        """
        self.synset_id = id

    def find_synset(self):
        """
        Returns the synset in this TranslationWord's synsets
        at synset_idx.

        :return: Synset, this TW's WN synset
        """
        try:
            self.synsets[self.synset_idx]
        except IndexError:
            return
        else:
            return self.synsets[self.synset_idx]

    def get_synset(self):
        """
        Returns this TranslationWord's corresponding Wordnet Synset.

        :return: Synset, this TW's WN synset
        """
        return self.synset

    def add_synsets_lemmas(self, lemmas):
        """
        Adds items from lemmas to this TranslationWord's
        synsets_lemmas list.
        ~
        N.B. Param lemmas only contains strings which
        are synonyms derived from Synset objects.  It
        contains no Synset objects itself.

        :param lemmas: List[str], synset lemmas
        :return: None
        """
        self.synsets_lemmas += lemmas
        self.synsets_lemmas = self.translator.remove_duplicates(self.synsets_lemmas)

    def __str__(self):
        """
        Returns a string representation to print to a user.

        :return: str, string representation of this Blissymbol
        """
        return "word:\t\t" + (self.word).encode('ascii', 'replace') + "\n" + \
               "pos:\t\t" + self.pos + "\n" + \
               "lemma:\t\t" + (self.lemma).encode('ascii', 'replace') + "\n" + \
               "bliss:\t\t" + (self.get_bliss_name()).encode('ascii', 'replace') + "\n" + \
               "synonyms:\t" + (str(self.synsets_lemmas)).encode('ascii', 'replace')

    __repr__ = __str__


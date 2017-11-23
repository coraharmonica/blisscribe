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
        e.g. kept, mice, funnest
     - Penn Treebank part(s) of speech
     - associated BlissTranslator

     Upon initialization, uses kwargs to generate:
     - word lexeme
        i.e. word as it appears in the dictionary
        e.g. keep, mouse, fun
     - synonyms
     - native language
    """
    def __init__(self, word, pos, translator, debug=False, language=None):
        self.debug = debug
        self.translator = translator
        self.language = self.translator.language if (language is None) else language
        self.word = self.translator.unicodize(word)
        self.pos = pos
        self.pos_abbrev = self.findPosAbbrev()
        self.lexeme = self.findLexeme()
        self.initPos()
        self.bliss_dict = self.translator.getBlissDict()
        self.eng_bliss_dict = self.translator.getEngBlissDict()
        self.blissymbols = None
        self.blissymbol = None
        self.synonyms = []
        self.synsets_lemmas = []
        self.synsets = self.findSynsets()
        self.synset_idx = 0
        self.synset = self.findSynset()
        self.synset_id = self.initSynsetId()
        self.eng_lexeme = self.findEngLexeme(debug)
        self.initBlissymbols()
        self.initBlissymbol()
        self.wn_defn = None
        self.wn_idx = None

    def getWord(self):
        """
        Returns this TranslationWord's word.
        ~
        Word should be the word token as it
        appeared in the original text.

        :return: str, this TW's word token
        """
        return self.word

    def initPos(self):
        """
        If language is not English, this method cross-references
        this TranslationWord's pos with other likely parts of speech
        to determine most likely part of speech.

        :return: None
        """
        if self.translator.language != "English":
            self.getMultilingualPos()

    def getPos(self):
        """
        Returns this TranslationWord's part-of-speech tag.

        :return: str, TW's pos tag
        """
        return self.pos

    def getPosAbbrev(self):
        """
        Returns this TranslationWord's abbreviated part-of-speech tag.

        :return: str, TW's pos tag
        """
        return self.pos_abbrev

    def findPosAbbrev(self):
        """
        Returns this TranslationWord's abbreviated part-of-speech tag.

        :return: str, TW's pos tag
        """
        return self.translator.abbreviateTag(self.pos)

    def setPos(self, pos):
        """
        Sets this TranslationWord's part-of-speech
        tag to given pos.

        :param pos: str, TW's pos tag
        :return: None
        """
        self.pos = pos

    def getMultilingualPos(self):
        """
        Only invoked when language is not English.
        ~
        Returns part-of-speech tag for this
        non-English TranslationWord.

        :return: str, TW's pos tag
        """
        return self.translator.getWordTag(self)

    def getLexeme(self):
        """
        Returns this TranslationWord's lexeme.

        :return: str, TW's lexeme
        """
        return self.lexeme

    def hasBlissymbol(self):
        """
        Returns whether this TranslationWord has a blissymbol.

        :return: bool, whether TW has Bliss translation
        """
        return self.blissymbol is not None

    def getBlissymbol(self):
        """
        Returns this TranslationWord's blissymbol.

        :return: Blissymbol, TW's Bliss translation
        """
        return self.blissymbol

    def getBlissName(self):
        """
        Returns this TranslationWord's blissymbol's name.

        :return: str, TW's Blissymbol's name
        """
        if self.blissymbol is not None:
            return self.blissymbol.getBlissName()
        else:
            return ""

    def resetBlissymbol(self, blissymbol):
        """
        Resets this TranslationWord's blissymbol to
        given blissymbol.

        :param blissymbol: Blissymbol, TW's Bliss translation
        :return: None
        """
        self.blissymbol = blissymbol

    def setBlissymbol(self, blissymbol):
        """
        Sets this TranslationWord's blissymbol to
        given blissymbol if it meets certain criteria.

        :param blissymbol: Blissymbol, TW's Bliss translation
        :return: None
        """
        if self.blissymbol is None:
            if self.pos in blissymbol.getPartsOfSpeech():
                #if blissymbol.isNeutral():
                self.blissymbol = blissymbol

    def setBlissymbols(self, blissymbols):
        """
        Sets this TranslationWord's blissymbols to
        given blissymbols.

        :param blissymbols: List[Blissymbol], TW's Bliss translation
        :return: None
        """
        neutrals = [bs for bs in blissymbols if bs.isNeutral()]

        if len(neutrals) != 0:
            self.blissymbols = neutrals
        else:
            self.blissymbols = blissymbols

    def capsInBlissDict(self, word):
        """
        If the given word with the first letter capitalized
        is in the Bliss dictionary, return that word.
        Otherwise, return None.

        :param word: str, word to check whether capitalized
            in Bliss dict
        :return: str, word capitalized if in Bliss dict
        """
        caps = word.title()

        if self.inBlissDict(caps):
            return caps

    def initBlissymbols(self):
        """
        If this TranslationWord's lexeme is in bliss_dict,
        sets self.blissymbol to the first match in self.blissymbols.

        :return: None
        """
        '''
        if self.translator.translate_all:
            print("Can this word be translated to English/Blissymbols?" +
                  "\nEnter y for yes, n for no.")
            ans = str(raw_input(""))
        else:
            ans = "y"

        if ans == "y":
        '''
        bliss_dict = self.translator.getBlissDict()
        #eng_bliss_dict = self.translator.getEngBlissDict()
        #print(bliss_dict)
        #print(eng_bliss_dict)
        #print(self.language + " lexeme: " + self.lexeme)
        #print("English lexeme: " + self.eng_lexeme)

        if self.inBlissDict(self.lexeme):
            lexeme = self.lexeme

        elif self.inBlissDict(self.word):
            self.lexeme = self.word
            lexeme = self.lexeme

        elif self.inEngBlissDict(self.eng_lexeme):
            lexeme = self.eng_lexeme
            bliss_dict = self.translator.getEngBlissDict()

        else:
            caps = self.capsInBlissDict(self.lexeme)
            if caps is not None:
                lexeme = caps
            else:
                if len(self.eng_lexeme) > 0:
                    lexeme = self.eng_lexeme
                else:
                    lexeme = ""

        if len(lexeme) != 0 and lexeme in bliss_dict:
            self.setBlissymbols(bliss_dict[lexeme])

            for blissymbol in self.blissymbols:
                translations = [self.translator.unicodize(translation)
                                for translation in blissymbol.getTranslation("English")]  #self.language?
                self.synonyms += translations
                self.setBlissymbol(blissymbol)

        '''
        if self.blissymbol is None and self.blissymbols is not None:
            print(lexeme)
            print("This word appears to have no Blissymbol.")
            print("I could set this word's blissymbol to " + self.blissymbols[0] +
                  ".\nWould you like that?  Enter y for yes, n for no.\n")
            ans = str(raw_input(""))
            if ans == "y":
                self.blissymbol = self.blissymbols[0]
        '''

    def findSynonyms(self):
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
            if self.inBlissDict(synset):
                self.setBlissymbols(self.bliss_dict[synset])
                for blissymbol in self.blissymbols:
                    if self.pos in blissymbol.getPartsOfSpeech():
                        self.synonyms += blissymbol.getTranslation(self.language)  #self.language?
                        self.resetBlissymbol(blissymbol)
                break

        if self.blissymbol is None:
            for synset in self.synsets_lemmas:
                if self.inBlissDict(synset):
                    self.setBlissymbols(self.bliss_dict[synset])
                    for blissymbol in self.blissymbols:
                        if self.blissymbol is None:
                            self.blissymbol = blissymbol
                    break

    def initBlissymbol(self):
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
        self.findSynonyms()
        if self.blissymbol is not None:
            self.blissymbol = self.blissymbol
        elif self.blissymbols is not None:
            self.blissymbol = next(iter(self.blissymbols))
        elif self.translator.translate_all:
            self.blissymbol = self.findBlissymbol()

        '''
        if self.blissymbol is not None:
            bliss_name = self.getBlissName()
            bliss_names = bliss_name.split(",")
            untranslated = any(bn not in self.eng_bliss_dict for bn in bliss_names)
            if untranslated:
                self.blissymbol.addTranslation(self.language, self.lexeme)
                self.blissymbol.addTranslation("English", self.eng_lexeme)
                self.translator.addBlissEntry(self.blissymbol)
        '''

    def findBlissymbol(self):
        """
        Returns a BlissLearner's best guess definition for
        this TranslationWord's Blissymbol.

        :return: Blissymbol, this word's Blissymbol
        """
        print(self.language + u": " + self.lexeme + u"\nEnglish: " + self.eng_lexeme)
        ans = str(raw_input("Enter y to translate this word to Blissymbols yourself, " +
                            "or n to choose not to translate it to Blissymbols.\n"))

        if ans == "y":
            print("Is the above lexeme the real lexeme for " + self.word + " in " + self.language + "?" +
                  "\nIf so, enter y.  Else, enter n to modify the lexeme.")

            ans = str(raw_input(""))

            if ans == "n":
                print("Enter the true lexeme for " + self.word + ".")
                lexeme = str(raw_input(""))
                self.lexeme = lexeme
                self.eng_lexeme = self.findEngLexeme(self.translator.translate_all)

            if self.eng_lexeme in self.eng_bliss_dict:
                print("Success: " + self.eng_lexeme + " in English bliss dict!")
                blissymbols = self.eng_bliss_dict[self.eng_lexeme]
                self.blissymbol = blissymbols[0]
                self.translator.lex_parser.addBlissEntry(self.blissymbol)
                return self.blissymbol
            elif self.lexeme in self.bliss_dict:
                blissymbols = self.bliss_dict[self.lexeme]
                self.blissymbol = blissymbols[0]
                return self.blissymbol
            else:
                print(self.eng_bliss_dict)

            classifier = self.translator.classifier
            bliss_words = classifier.predictWord(self)
            lang_code = self.translator.findLangCode(self.language)
            lexeme = self.lexeme.replace(" ", "_")
            eng_lexeme = self.eng_lexeme.replace(" ", "_")
            #eng_lexeme = eng_lexeme.replace(" ", "_")
            print(eng_lexeme)

            if len(bliss_words) == 1:
                img_filename = bliss_words[0]
            elif len(bliss_words) == 0:
                return None
            else:
                img_filename = eng_lexeme

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
                # TODO: change filename to be the same as the bliss image
                translations = {}
                print("adding to English translations:")
                print(self.synsets_lemmas)
                print(self.eng_lexeme)
                translations["English"] = self.synsets_lemmas
                translations["English"] = [eng_lexeme]
                print("adding to " + self.language + " translations:")
                #print(self.synonyms)
                #print(self.synset.lemma_names(lang_code))
                print(self.lexeme)
                translations.setdefault(self.language, [])
                #translations[self.language] = self.synset.lemma_names(lang_code)
                translations[self.language].append(lexeme)
                print(translations)
                blissymbol = self.translator.makeBlissymbol(img_filename=img_filename + ".png",
                                                            pos=self.getPos(),
                                                            derivation=derivation,
                                                            translations=translations)
                #print blissymbol
                blissymbol.addSynsets(self.synsets)
                self.resetBlissymbol(blissymbol)
                self.translator.addBlissEntry(self.blissymbol)
                return self.blissymbol

    def getFilename(self):
        """
        If this Blissymbol has an associated image file,
        return the image filename including extension.
        ~
        If this Blissymbol has no associated image file,
        return None.

        :return: str, this Blissymbol's image filename
        """
        if self.blissymbol:
            return self.translator.unicodize(self.blissymbol.getImgFilename())

    def getWNDefn(self):
        """
        Returns this TranslationWord's synset description.

        :return: str, this TranslationWord's synset description
        """
        if self.wn_defn is None:
            self.setWNDefn(self.findWNDefn())
        return self.wn_defn

    def setWNDefn(self, wn_defn):
        """
        Sets this TranslationWord's synset description to given
        wn_defn.

        :param wn_defn: str, this TranslationWord's synset description
        :return: None
        """
        self.wn_defn = wn_defn

    def findWNDefn(self):
        """
        Finds and returns this TranslationWord's synset description
        from WordNet.

        :return: str, this TranslationWord's synset description
        """
        synsets = self.translator.lookupTWordSynsets(trans_word=self)
        try:
            synset = synsets[0]
        except IndexError:
            return
        else:
            return self.translator.getSynsetDefn(synset)

    def findLexeme(self):
        """
        Retrieves this Blissymbol's lexeme,
        i.e., its "dictionary entry" form.
        ~
        Determines lexeme from this Blissymbol's word and pos.

        :return: str, this Blissymbol's lexeme
        """
        try:
            if self.language != "English":
                lexeme = self.translator.getLexeme(self.word)
            else:
                lexeme = self.translator.getLexeme(self.word, self.pos)
        except KeyError:
            try:
                lexeme = self.translator.getLexeme(self.word.lower(), self.pos)
            except KeyError:
                try:
                    lexeme = self.translator.getLexeme(self.word.title(), self.pos)
                except KeyError:
                    return self.word  # no lexeme found
                else:
                    self.word = self.word.title()
                    self.lexeme = self.lexeme.title()
            else:
                self.word = self.word.lower()
                #lexeme = self.translator.getLexeme(self.word, self.pos)

        return self.translator.unicodize(lexeme)

    def initEngLexeme(self, debug=True):
        """
        Initializes this TranslationWord's English lexeme by
        setting self.eng_lexeme to whichever English lexeme it
        can find.
        ~
        If debug is True, then the user will be prompted to
        identify the correct English lexeme from a set of
        synsets.

        :param debug: bool, whether user should identify correct
            English lexeme
        :return: None
        """
        self.eng_lexeme = self.findEngLexeme(debug)

    def findEngLexeme(self, debug):
        """
        Returns this TranslationWord's corresponding English lexeme.

        :return: str, English lexeme
        """
        #lexeme = self.lexeme #self.findLexeme()
        if self.language == "English":
            eng_lexeme = self.lexeme

        elif self.lexeme in self.bliss_dict:
            blissymbols = self.bliss_dict[self.lexeme]
            blissymbol = next(iter(blissymbols))  #blissymbols[0]
            if debug:
                for bs in blissymbols:
                    if bs.getPos() == self.pos[:2] and bs.isNeutral():
                        blissymbol = bs
                        break
            translations = blissymbol.getTranslation("English")
            eng_lexeme = translations[0]

        else:
            synsets = self.translator.lookupTWordSynsets(self, use_pos=False)
            print(synsets)
            lexeme = self.lexeme

            try:
                synsets[0]
            except IndexError:  # no English lexeme exists thus far
                if debug:
                    print("\n")
                    print(lexeme)
                    print("This word appears to have no English translation.  " +
                          "Could you provide one?  Enter y for yes, n for no.")
                    answer = str(raw_input(""))
                    if answer == "y":
                        lexeme = str(raw_input("Enter your English translation:\n"))
                else:
                    lexeme = ""
            else:
                if debug and len(synsets) > 1:
                    # allows user to select which synset corresponds with this word
                    # if multiple synsets apply
                    print(lexeme)
                    print("This word matches the following synsets:")
                    idx = 1
                    for synset in synsets:
                        print idx, synset.lemma_names(), synset.definition()
                        idx += 1
                    while idx < 0 or idx >= len(synsets):
                        print("Which index does this match?  If none is appropriate, enter 0.")
                        idx = int(input(""))
                        if idx == 0:
                            return ""
                        else:
                            idx -= 1
                            #assert 0 <= idx < len(synsets)
                elif len(synsets) != 0:
                    idx = 0
                else:
                    print("No English synsets found.")  #Enter y to choose your own, or n to continue.\n")
                    return ""
                    #ans = str(raw_input(""))
                #for synset in synsets:
                #    print(synset.lemma_names())
                synset = synsets[idx]
                self.setSynsetIdx(idx)
                synonyms = synset.lemma_names()
                lexeme = synonyms[0]

            eng_lexeme = self.translator.unicodize(lexeme)

        return eng_lexeme

    def getEngLexeme(self):
        """
        Returns self.eng_lexeme, this TranslationWord's
        corresponding WordNet English lexeme.

        :return: str, English lexeme
        """
        return self.eng_lexeme

    def setEngLexeme(self, eng_lexeme):
        """
        Sets self.eng_lexeme to given eng_lexeme.

        :param eng_lexeme: str, English lexeme
        :return: None
        """
        self.eng_lexeme = eng_lexeme

    def inBlissDict(self, word):
        """
        Returns True if given word is in this TranslationWord's
        BlissTranslator's bliss_dict.  Otherwise, returns False.

        :param word: str, word to lookup in bliss_dict
        :return: bool, whether word found in bliss_dict
        """
        return self.translator.inBlissDict(word)

    def inEngBlissDict(self, word):
        """
        Returns True if given word is in this TranslationWord's
        BlissTranslator's eng_bliss_dict.  Otherwise, returns False.

        :param word: str, word to lookup in eng_bliss_dict
        :return: bool, whether word found in eng_bliss_dict
        """
        return self.translator.inEngBlissDict(word)

    def hasSynonyms(self):
        """
        Returns True if any of this TranslationWord's synonyms
        are translatable to Blissymbols.  Else, returns False.

        :return: bool, whether this TranslationWord has synonyms
        """
        return self.translator.isSynonymTranslatable(self)

    def findSynsets(self):
        """
        Finds and returns this TranslationWord's synsets.

        :return: List[Synset], synset synonyms
        """
        use_pos = (self.language == "English")
        synsets = self.translator.lookupTWordSynsets(self, use_pos)
        self.addSynsetsLemmas(self.translator.getSynsetsLemmas(synsets))
        return synsets

    def setSynsets(self, synsets):
        """
        Sets this TranslationWord's synsets list to given synsets.

        :param synsets: List[Synset], synsets
        :return: None
        """
        self.synsets = synsets
        for synset in synsets:
            self.addSynsetsLemmas(synset.lemma_names(lang=self.translator.lang_code))

    def getSynsets(self):
        """
        Returns this TranslationWord's synsets list.

        :return:  List[Synset], synsets
        """
        return self.synsets

    def setSynsetIdx(self, idx):
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
        assert 0 <= idx < len(self.synsets)
        self.synset_idx = idx
        self.synset = self.findSynset()
        self.setSynsetId(self.findSynsetId())

    def getSynsetIdx(self):
        """
        Returns this TranslationWord's synset_idx, the best
        guess for which Synset this TranslationWord corresponds to.
        ~
        N.B. Unless manually set otherwise, synset_idx will be 0.

        :return: int, the index of this TW's correct Synset,
            0 <= self.synset_idx < len(self.synsets)
        """
        return self.synset_idx

    def getSynsetId(self):
        """
        Returns this TranslationWord's synset_id.
        ~
        N.B. TranslationWord's synset_id allows this word to be considered
        synonymous with any other TranslationWord possessing the same synset_id.

        :return: str, a 9-digit Wordnet Synset ID
        """
        return self.synset_id

    def initSynsetId(self):
        """
        Finds a synset ID for this TranslationWord based on its synset.
        ~
        N.B. TranslationWord's synset_id corresponds to Synset.offset()
        in NLTK's Wordnet module, i.e., a 9-digit numerical identifier.

        :return: str, a 9-digit Wordnet Synset ID
        """
        return self.findSynsetId(self.synset)

    def findSynsetId(self, synset):
        """
        Finds a synset ID for this TranslationWord based on its synset.
        ~
        N.B. TranslationWord's synset_id corresponds to Synset.offset()
        in NLTK's Wordnet module, i.e., a 9-digit numerical identifier.

        :return: str, a 9-digit Wordnet Synset ID
        """
        return self.translator.findSynsetId(synset)

    def setSynsetId(self, id):
        """
        Sets this TranslationWord's synset_id to given id.
        ~
        N.B. TranslationWord's synset_id corresponds to Synset.offset()
        in NLTK's Wordnet module, i.e., a 9-digit numerical identifier.

        :param id: str, a 9-digit Wordnet Synset ID
        :return: None
        """
        self.synset_id = id

    def findSynset(self):
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

    def getSynset(self):
        """
        Returns this TranslationWord's corresponding Wordnet Synset.

        :return: Synset, this TW's WN synset
        """
        return self.synset

    def addSynsetsLemmas(self, lemmas):
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
        self.synsets_lemmas = self.translator.removeDuplicates(self.synsets_lemmas)

    def __str__(self):
        """
        Returns a string representation to print to a user.

        :return: str, string representation of this Blissymbol
        """
        return "word:\t\t" + (self.word).encode('ascii', 'replace') + "\n" + \
               "pos:\t\t" + self.pos + "\n" + \
               "lexeme:\t\t" + (self.lexeme).encode('ascii', 'replace') + "\n" + \
               "bliss:\t\t" + (self.getBlissName()).encode('ascii', 'replace') + "\n" + \
               "synonyms:\t" + (str(self.synsets_lemmas)).encode('ascii', 'replace')

    __repr__ = __str__
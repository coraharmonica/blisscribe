# -*- coding: utf-8 -*-
"""
BLISSLEARN:

    A machine learning module for Blisscribe.

    Features to feed:
        - locn of Blissymbols on grid
            1) ultra
            2) sky
            3) mid
            4) earth
            5) infra
        - Blissymbol derivations/meanings

    Labels to feed:
        - Bliss atoms
        - official Blissymbol derived vocabulary
"""
import os
from string import zfill
from sklearn.tree import DecisionTreeClassifier
#from nltk.classify import accuracy, DecisionTreeClassifier
#from sklearn.metrics import accuracy_score
from random import shuffle
import blissnet
from blissnet import BLISSNET
import bliss_lex

class BlissLearner:
    """
    A machine learning classifier for Blissymbols.
    """
    PATH = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, bliss_translator):
        self.translator = bliss_translator
        self.bliss_lexicon = bliss_lex.BLISS_LEXICON #self.translator.getBlissLexicon()
        #print(self.bliss_lexicon)
        self.classifier = DecisionTreeClassifier() #(label="")
        self.questions = []
        self.answers = []
        #self.qa_pairs = []   # List[2-tuple]
        self.wordnet_indices = self.getWordnetIndices()  # dict
        self.wordnet_entries = self.getWordnetEntries()  # dict
        self.wordnet_descriptions = self.getWordnetDescriptions()  # dict
        self.initClassifier()

    def initClassifier(self):
        """
        Fits data to this BlissClassifier's classifier for future predicting.

        :return: None
        """
        samples = self.wordnet_indices
        questions = []
        answers = []
        test_questions = []
        test_answers = []
        common_words = self.readCommonWords()
        print("initializing Bliss classifier...")

        '''
        for entry in BLISSNET:
            uni = self.unicodeToStr(entry)
            synsets = BLISSNET[entry]
            synset = synsets[0]
            pos = synset.pos()
            pos_code = self.posToInt(pos)
            pair = (synset.offset(), pos_code)
            wn_num = self.findFullSynsetId(pair)
            word_features = [wn_num, pos_code]

            if len(synsets) == 1:
                answers.append(uni)
                questions.append(word_features)
        '''
        # percent on-target: 0.0%
        # percent on-target: 2.64700321422%
        # percent on-target: 9.88755331524%
        # percent on-target: 95.6051873199%

        for lex in self.bliss_lexicon:
            blissymbols = self.translator.lookupEngBlissDict(lex)
            if blissymbols is not None:
                for blissymbol in blissymbols:
                    synsets = blissymbol.getSynsets()
                    if synsets is not None:
                        unis = blissymbol.getDerivUnicode()
                        uni = self.unicodesToStr(unis)
                        name = blissymbol.getBlissName()
                        for synset in synsets:
                            pos = synset.pos()
                            pos_code = self.posToInt(pos)
                            wn_num = self.findFullSynsetId((synset.offset(), pos_code))
                            word_features = [wn_num, pos_code]

                            print("ADDED " + name)
                            answers.append(uni)
                            questions.append(word_features)

        for wn_num in samples:  # iterate thru (unordered) dict
            # convert human-readable data to machine-readable numbers
            defns = samples[wn_num]
            shuffle(defns)

            for defn in defns:  # iterate thru list
                name = defn[0]
                pos = defn[1]
                pos_unabbrev = self.translator.unabbreviateTag(pos)

                trans_word = self.translator.makeTranslationWord(name, pos_unabbrev, debug=False, language="English")

                if trans_word.hasBlissymbol():
                    trans_word.getBlissName() + " has a blissymbol"
                    blissymbol = trans_word.getBlissymbol()
                    unis = blissymbol.getDerivUnicode()
                    uni = self.unicodesToStr(unis)
                    pos_code = self.posToInt(pos)
                    word_features = [wn_num, pos_code]

                    synsets = blissymbol.getSynsets()

                    #if word_features not in questions and word_features not in test_questions:
                    if len(synsets) != 0:
                        for synset in synsets:
                            if self.findSynsetId(synset) == wn_num:
                                if self.translator.inBlissDict(name) and name in self.bliss_lexicon \
                                 and name in common_words:
                                    print("ADDED " + name)
                                    answers.append(uni)
                                    questions.append(word_features)
                                else:
                                    print("SKIPPED " + name)
                                    test_answers.append(uni)
                                    test_questions.append(word_features)


        self.questions = questions
        self.answers = answers
        test_questions.append([302835329, 3])
        test_answers.append("34d1 3353 4478 3b5c")
        test_questions.append([103990025, 1])
        test_answers.append("34d1 3353 4478")
        train_questions, train_answers = self.questions, self.answers #self.questions[100:], self.answers[100:]
        test_questions, test_answers = test_questions, test_answers #self.questions[0:100], self.answers[0:100]

        print("\ntraining classifier...")
        self.classifier.fit(train_questions, train_answers)
        print("training complete.\n")

        print("\ntesting classifier...")
        hits = []
        misses = []
        unicode_hits = 0
        all_unicodes = 0
        for (q, ans) in zip(test_questions, test_answers):
            guess = self.classifier.predict([q])[0]
            word_id = q[0]
            pos_code = q[1]
            if guess != ans:
                misses.append((ans, guess, q))
                guess_lst = set(guess.split(" "))
                ans_lst = set(ans.split(" "))
                unicode_hits += len(guess_lst.intersection(ans_lst))
                all_unicodes += len(guess_lst) + len(ans_lst)
            else:
                hits.append((ans, guess, q))
            print word_id, pos_code, ans
            self.fitWordToClassifier(word_id=word_id, pos_code=pos_code, derivations=ans)
        all = sorted(hits) + sorted(misses)

        for (ans, guess, q) in all:
            print

            # format answer from unicode to Bliss words
            ans = ans.split(" ")
            new_ans = []
            for uni in ans:
                defns = self.translator.lookupUnicodeToBliss(self.strToUnicode(uni))
                if len(defns) != 0:
                    defn = defns[0]
                    new_ans.append(defn.replace(" ", "_"))
            ans = " ".join(new_ans)

            # format guess from unicode to Bliss words
            guess = guess.split(" ")
            new_guess = []
            for uni in guess:
                defns = self.translator.lookupUnicodeToBliss(self.strToUnicode(uni))
                if len(defns) != 0:
                    defn = defns[0]
                    new_guess.append(defn.replace(" ", "_"))
            guess = " ".join(new_guess)

            q = self.wordnet_indices[q[0]]
            q = q[0][0]
            print('question: {:<30}\nanswer: {:<40s}\nguess: {:<40}'.format(q, ans, guess))
            print

        print("testing complete.")
        print("number on-target: " + str(len(test_questions) - len(misses)) + " out of " + str(len(test_questions)))
        print("percent on-target: " + str(float(len(test_questions) - len(misses))/len(test_questions) * 100) + "%")
        print("partly on-target: " + str(unicode_hits) + " out of " + str(all_unicodes))
        print()
        print("trained with " + str(len(questions)) + " question-answer sets")
        print("word coverage: " + str(len(questions)/float(len(samples))))

        self.writeExamples()

    def writeExamples(self):
        path = self.translator.PATH + "/examples.txt"
        #q_desc = [(self.findIdSynsets(q[0])[0], self.intToPos(q[1])) for q in self.questions]
        #a_desc = [[self.translator.lookupUnicodeToBliss(self.strToUnicode(ans)) for ans in answer.split(" ")]
        #           for answer in self.answers]

        with open(path, "w") as examples:
            for qa in zip(self.questions, self.answers):
                q_word = self.findIdSynsets(qa[0][0])[0]
                q_pos = self.intToPos(qa[0][1])
                a_desc = ("/".join(self.translator.lookupUnicodeToBliss(self.strToUnicode(ans)))
                          for ans in qa[1].split(" "))
                a_desc = " + ".join(a_desc)
                examples.write("# " + str(q_word[0]) + ", " + str(q_pos) + " -> " + str(a_desc) + "\n")
                examples.write(str(qa) + "\n\n")
            examples.close()

    def readCommonWords(self):
        """
        Returns a set of the most common words in English.
        ~
        Used to train BlissLearner with proper examples.

        :return: set(str), most common words in English
        """
        path = self.translator.PATH + "/common_words.txt"
        with open(path, "r") as words:
            common_words = {word.rstrip("\n") for word in words}
        return common_words

    def refitClassifier(self):
        """
        Refits this BlissLearner's classifier according to
        its current questions and answers fields.
        ~
        Allows updated learning with more examples.

        :return: None
        """
        self.classifier.fit(self.questions, self.answers)

    def trainClassifier(self, questions, answers):
        """
        Refits this BlissLearner's classifier according to
        given questions and answers.
        ~
        Allows updated learning with more examples.

        :param questions: List[List[int,int]], list with lists of
            wordnet IDs and their pos codes
        :param answers: str, unicode responses (without U+ prefix)
        :return: None
        """
        self.questions += questions
        self.answers += answers
        self.classifier.fit(self.questions, self.answers)

    def fitWordToClassifier(self, word_id, pos_code, derivations):
        """
        Fits a word with given synset ID, pos, and derivations
        to this BlissClassifier's machine learning classifier.
        ~
        Allows for classifier to learn from successes/mistakes.
        ~
        e.g. fitWordToClassifier(107739125, 1, '3fa1') ->
            fits the synset for apple to this classifier

        :param word_id: int, a synset's full (9-digit) numeric ID
        :param pos: int, the synset's part-of-speech code
        :param derivations: str, a list of 4-character unicodes corresponding
            to the synset's Blissymbol translation
        :return: None
        """
        sample = [word_id, pos_code]
        self.questions.append(sample)
        self.answers.append(derivations)
        #self.qa_pairs.append((sample, derivations))
        #self.classifier.train(self.qa_pairs)
        self.classifier.fit(self.questions, self.answers)

    def posToInt(self, pos):
        """
        Takes in a part-of-speech (from n, v, a, s, r) and
        returns its corresponding WordNet integer.

        :param pos: str, single-character part-of-speech
        :return: int, pos's corresponding WordNet integer
        """
        return self.translator.POS_FEATURE_DICT[pos]

    def intToPos(self, code):
        """
        Takes in a WordNet integer (in range(0,4)) and
        returns its corresponding WordNet part-of-speech.
        ~
        N.B. Since adjectives ("a") and adjective sattelites ("s")
        are both indexed at 3, this method returns "a" if given 3.

        :param pos: int, code corresponding to WordNet part-of-speech
        :return: str, given code's single-character part-of-speech
        """
        return self.translator.POS_CODE_DICT[code]

    def findSynsetId(self, synset):
        """
        Finds a synset ID for this synset.

        :param synset: Synset, synset to find ID for
        :return: int, a 9-digit Wordnet Synset ID
        """
        return self.translator.findSynsetId(synset)

    def findFullSynsetId(self, synset):
        """
        Finds a synset ID for this synset, represented as a 2-tuple
        with a WordNet integer ID and its corresponding part-of-speech.

        :param synset: tuple(int,int), synset to find ID for
        :return: int, a 9-digit Wordnet Synset ID
        """
        return self.translator.findFullSynsetId(synset)

    def findIdSynsets(self, id):
        """
        Returns a list of 2-tuples of synsets and their
        parts of speech for the given synset ID.

        :param id: int, a 9-digit Wordnet Synset ID
        :return: List[(str,str)], list of synsets
        """
        synset = self.wordnet_indices[id]
        return synset

    def getWordnetIndices(self):
        """
        Returns dictionary of Wordnet word indices.

        :return: dict, where...
            key (int) - Wordnet synset entry index
            val (List[str,str]) - list of synset name(s) & part(s) of speech
        """
        sample_path = self.PATH + "/resources/wordnet/"
        entries = sample_path + "wn_s.txt"

        index_dict = {}

        with open(entries, "r") as synsets:
            for synset in synsets:
                synset = synset[2:-3]
                info = synset.split(",")
                id = int(info[0])
                gloss = info[2]
                gloss = gloss[1:-1]
                pos = info[3]

                if id not in index_dict:
                    index_dict[id] = []
                index_dict[id].append([gloss,pos])

        return index_dict

    def getWordnetEntries(self):
        """
        Returns dictionary of Wordnet synset names.

        :return: dict, where...
            key (tuple(str,str)) - Wordnet synset name and pos
            val (List[int]) - Wordnet synset id(s)
        """
        samples_path = self.PATH + "/resources/wordnet/"
        entries = samples_path + "wn_s.txt"

        entry_dict = {}

        with open(entries, "r") as synsets:
            for synset in synsets:
                synset = synset[2:-3]
                info = synset.split(",")
                id = info[0]
                #id = id[2:]
                name = info[2]
                name = name[1:-1]
                pos = info[3]
                entry = (name, pos)

                if entry not in entry_dict:
                    entry_dict[entry] = []
                entry_dict[entry].append(id)

        return entry_dict

    def getWordnetDescriptions(self):
        """
        Returns dictionary of Wordnet word entry descriptions.

        :return: dict, where...
            key (int) - Wordnet synset entry index
            val (List[str,str]) - list of synset descriptions
        """
        sample_path = self.PATH + "/resources/wordnet/"
        path = sample_path + "wn_g.txt"

        descriptions = {}

        with open(path, "r") as synsets:
            for synset in synsets:
                synset = synset[2:-3]
                info = synset.split(",")
                id = info[0]
                description = info[1]
                description = description[1:-1]

                if id not in descriptions:
                    descriptions[id] = []
                descriptions[id].append(description)

        return descriptions

    def getBlissToUnicode(self):
        return self.translator.getBlissToUnicode()

    def getUnicodeToBliss(self):
        return self.translator.getUnicodeToBliss()

    def strToUnicode(self, string):
        """
        Prefixes given string with "U+".
        ~
        Used to convert classifier's unicode outputs to
        Blissymbol unicode keys.

        :param string: str, string to prefix
        :return: str, string unicode
        """
        return "U+" + string

    def strToUnicodes(self, string):
        """
        Converts the given string to a list of unicodes.

        :param string: str, string to convert to list of unicodes
        :return: List[str], unicode strings
        """
        unis = [self.strToUnicode(uni) for uni in string.split(" ")]
        return unis

    def unicodeToStr(self, uni):
        """
        Converts the given string to unicode by prepending "U+".

        :param string: str, string to convert to unicode
        :return: str, string unicode
        """
        return uni[2:]

    def unicodesToStr(self, unis):
        """
        Converts the given list of unicodes to a string.

        :param string: List[str], list of unicodes to convert to string
        :return: str, string of all unicode names
        """
        unis = [self.unicodeToStr(uni) for uni in unis]
        return " ".join(unis)

    def cleanDefn(self, defn):
        """
        Replaces input defn's underscores with spaces and
        strips whitespace from ends.  Returns result.

        :param defn: str, word definition to clean
        :return: str, cleaned word definition
        """
        new_defn = self.translator.lex_parser.parseAlphabetic(defn)
        new_defn = self.translator.lex_parser.stripParens(new_defn)
        return new_defn

    def getNewDerivations(self, trans_word):
        """
        Prompts user for a list of Blissymbol derivations approximating
        the meaning of the given trans_word.
        ~
        Returns the result as a set of strings.

        :param trans_word: TranslationWord, word to enter derivations for
        :return: Set(str), set of entered derivations
        """
        keep_going = True
        derivations = []
        eng_lexeme = trans_word.getEngLexeme()
        print("\n")
        print(eng_lexeme)
        print("-" * len(eng_lexeme))

        while keep_going:
            print("Please enter the correct Blissymbol derivation(s) for " +
                  eng_lexeme + ", each separated by a comma and a space. ")
            derivations = raw_input("")

            if len(derivations) == 0:
                print("Please try again.\n")
                continue
            else:
                derivations = str(derivations)
                derivations = derivations.split(", ")
                keep_going = False
                for derivation in derivations:
                    is_bliss_word = self.translator.inEngBlissDict(derivation)
                    if is_bliss_word:
                        print(derivation + " is ... a valid bliss word :)")
                    else:
                        print(derivation + " is ... an invalid bliss word :(")
                    keep_going = keep_going or not is_bliss_word
                    if keep_going:
                        print("\nI'm sorry, one of the Blissymbol derivations you entered is invalid. " +
                              "Please try using a different synonym.\n")
                        continue

        derivations = set([(next(iter(trans_word.eng_bliss_dict[derivation]))).getBlissName()
                           for derivation in derivations])
        return derivations

    def lookupWNEntry(self, lexeme, pos):
        """
        Performs and returns a lookup in self.wordnet_entries
        for the given (lexeme, pos) pair, where lexeme is
        the WordNet dictionary entry name and pos is the
        abbreviated part-of-speech tag.
        ~
        N.B. An abbreviated pos tag is one of the following:
            n, v, a, s, r

            n - Noun
            v - Verb
            a - Adjective
            s - Adjective (satellite)
            r - Adverb

        :param lexeme: str, a lexeme to lookup in WordNet
        :param pos: str, the given lexeme's pos tag
        :return: tuple(int, str), the given word's
        """

    def predictWord(self, trans_word, debug=True):
        """
        Returns a list of derivations for the given trans_word.

        :param trans_word: TranslationWord, word to get derivations of
        :return: List[str], derivations for given trans_word
        """
        if trans_word.getEngLexeme() is None:
            trans_word.initEngLexeme(debug=True)
        trans_word.setSynsetId(trans_word.initSynsetId())
        lexeme = trans_word.getEngLexeme()
        pos = trans_word.getPos()
        pos_abbrev = self.translator.abbreviateTag(pos)
        pos_code = self.translator.POS_FEATURE_DICT[pos_abbrev]
        blissymbols = set([])

        pair = self.lookupWNEntry(lexeme, pos_abbrev)

        try:
            self.wordnet_entries[(lexeme, pos_abbrev)]
        except KeyError:
            for pt_of_speech in self.translator.POS_ABBREVS_SORTED:
                try:
                    self.wordnet_entries[(lexeme, pt_of_speech)]
                except KeyError:
                    print("word " + self.translator.deUnicodize(lexeme) + ", " + str(pt_of_speech) + " not in dict")
                    continue
                else:
                    pos_abbrev = pt_of_speech
                    pos_code = self.translator.POS_FEATURE_DICT[pos_abbrev]
                    word_id = self.wordnet_entries[(lexeme, pt_of_speech)][0]
                    new_pos = self.translator.unabbreviateTag(pt_of_speech)
                    trans_word.setPos(new_pos)
                    trans_word.setSynsetId(word_id)
                    print(word_id)
                    break
            else:
                ans = input("Enter y to translate this word to Blissymbols yourself, " +
                            "or n to choose not to translate it to Blissymbols.\n")
                if ans == "y":
                    blissymbols = self.getNewDerivations(trans_word)
                    return blissymbols
                else:
                    return []

                    #if pos_abbrev is None:
                    #    return blissymbols
        else:
            #word_ids = self.wordnet_entries[(lexeme, pos_abbrev)][0]
            word_id = trans_word.getSynsetId()

        if word_id is None:
            return blissymbols

        pair = [int(word_id), pos_code]
        print(pair)
        prediction = self.classifier.predict([pair])
        prediction = prediction[0]
        print("prediction: ", prediction)
        unicodes = str(prediction).split(" ")
        unicodes = ["U+" + uni for uni in unicodes if uni != ""]

        for uni in unicodes:
            symbols = self.getUnicodeToBliss()[uni]
            try:
                bs = trans_word.eng_bliss_dict[symbols[0]]
            except KeyError:
                symbols = symbols[1:]
            else:
                blissymbol = next(iter(bs))
                blissymbol = blissymbol.getBlissName()
                blissymbols.add(blissymbol)
                continue

            for symbol in symbols:
                symbol = self.cleanDefn(symbol)
                if symbol in trans_word.eng_bliss_dict:
                    blissymbol = trans_word.eng_bliss_dict[symbol][0]
                    blissymbol = blissymbol.getBlissName()
                    if debug:
                        print("I'm about to translate the word " + lexeme +
                              ", " + pos_abbrev + " with the Blissymbol " + str(blissymbol) + ".  Is that ok?")
                        answer = raw_input("Enter y for yes, n for no.  Enter s to skip to the next Blissymbol.\n")
                        if answer == "n":
                            ans = raw_input("Enter y to translate this word to Blissymbols yourself, " +
                                            "or n to choose not to translate it to Blissymbols.\n")
                            if ans == "y":
                                blissymbols = self.getNewDerivations(trans_word)
                                break
                            else:
                                return []
                        elif answer == "s":
                            continue
                        else:
                            blissymbols.add(blissymbol)
                    break
                    #else:
                    #    print trans_word.eng_bliss_dict

        if debug:
            print("I'm about to translate the word " + lexeme +
                  " with the Blissymbols " + str(blissymbols) + ".  Is that ok?")
            answer = raw_input("Enter y for yes, n for no.\n")
            if answer == "n":
                blissymbols = self.getNewDerivations(trans_word)
                unicodes = []
                for symbol in blissymbols:
                    symbols = symbol.split(",")
                    for symbol in symbols:
                        try:
                            unicode = (self.getBlissToUnicode()[symbol])[0]
                        except KeyError:
                            continue
                        else:
                            unicodes.append(self.unicodeToStr(unicode))
                            break
                #print unicodes
                prediction = " ".join(unicodes)
            print("synset: ", pair)
            print("prediction: ", prediction)
            self.fitWordToClassifier(word_id, pos_code, prediction)

        return blissymbols
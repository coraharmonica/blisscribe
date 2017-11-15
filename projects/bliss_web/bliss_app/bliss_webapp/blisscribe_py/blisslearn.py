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
from sklearn import tree


class BlissymbolClassifier:
    """
    A machine learning classifier for Blissymbols.
    """
    PATH = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, bliss_translator):
        self.translator = bliss_translator
        self.classifier = tree.DecisionTreeClassifier()
        self.questions = []
        self.answers = []
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
        new_samples = []
        features = []

        pos_features = []

        for wn_num in samples:  # iterate thru dict
            # convert human-readable data to machine-readable numbers
            defns = samples[wn_num]

            for defn in defns:  # iterate thru list
                name = defn[0]
                pos = defn[1]
                pos_unabbrev = self.translator.unabbreviateTag(pos)
                trans_word = self.translator.makeTranslationWord(name, pos_unabbrev, debug=False, language="English")
                #print(trans_word)

                if trans_word.hasBlissymbol():
                    blissymbol = trans_word.getBlissymbol()
                    new_samples.append(samples[wn_num])
                    unicodes = blissymbol.getDerivUnicode()
                    #print(blissymbol, unicodes)
                    unicode = " ".join([uni[2:] for uni in unicodes])
                    features.append(unicode)
                    pos_code = self.translator.POS_FEATURE_DICT[pos]
                    pos_feature = [int(wn_num), pos_code]
                    pos_features.append(pos_feature)
                    #bliss_words = [" ".join(UNICODE_TO_BLISS[uni]) for uni in unicodes]
                    #print(name + ": ")
                    #print("\t" + " + ".join(bliss_words))
                    #print("\n")
        self.questions = pos_features
        self.answers = features
        self.classifier.fit(self.questions, self.answers)

    def fitWordToClassifier(self, word_id, pos_code, derivations):
        """
        Fits a word with given lexeme, pos, and derivations
        to this BlissClassifier's machine learning classifier.
        ~
        Allows for classifier to learn from successes/mistakes.

        :param word_id: str
        :param pos: str
        :param derivations: str
        :return: None
        """
        sample = [int(word_id), pos_code]
        self.questions.append(sample)
        self.answers.append(derivations)
        self.classifier.fit(self.questions, self.answers)

    def getWordnetIndices(self):
        """
        Returns dictionary of Wordnet word indices.

        :return: dict, where...
            key (int) - Wordnet synset entry index
            val (List[str,str]) - list of synset name(s) & part(s) of speech
        """
        sample_path = self.PATH + "/resources/samples/"
        entries = sample_path + "wn_s.txt"

        index_dict = {}

        with open(entries, "r") as synsets:
            for synset in synsets:
                synset = synset[2:-3]
                info = synset.split(",")
                id = info[0]
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
        samples_path = self.PATH + "/resources/samples/"
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
        sample_path = self.PATH + "/resources/samples/"
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

    def cleanDefn(self, defn):
        """
        Replaces input defn's underscores with spaces and
        strips whitespace from ends.  Returns result.

        :param defn: str, word definition to clean
        :return: str, cleaned word definition
        """
        new_defn = self.translator.LEX_PARSER.parseAlphabetic(defn)
        new_defn = self.translator.LEX_PARSER.stripParens(new_defn)
        return new_defn

    def getNewDerivations(self, trans_word):
        """
        Prompts user for a list of Blissymbol derivations approximating
        the meaning of the given trans_word.
        ~
        Returns the result as a list of strings.

        :param trans_word: TranslationWord, word to enter derivations for
        :return: List[str], list of entered derivations
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
                        #print(self.getBlissToUnicode())
                        #print(self.getUnicodeToBliss())
                        print(self.translator.eng_bliss_dict)
                    keep_going = keep_going or not is_bliss_word
                    if keep_going:
                        print("\nI'm sorry, one of the Blissymbol derivations you entered is invalid. " +
                              "Please try using a different synonym.\n")
                        continue

        derivations = [(trans_word.eng_bliss_dict[derivation][0]).getBlissName() for derivation in derivations]
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
        trans_word.initEngLexeme(debug=True)
        trans_word.setSynsetId(trans_word.findSynsetId())
        lexeme = trans_word.getEngLexeme()
        pos = trans_word.getPos()
        pos_abbrev = self.translator.abbreviateTag(pos)
        pos_code = self.translator.POS_FEATURE_DICT[pos_abbrev]
        blissymbols = []

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
                ans = raw_input("Enter y to translate this word to Blissymbols yourself, " +
                                "or n to choose not to translate it to Blissymbols.\n")
                if ans == "y":
                    blissymbols = self.getNewDerivations(trans_word)
                    return blissymbols
                else:
                    return []

            if pos_abbrev is None:
                return blissymbols
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
                blissymbol = trans_word.eng_bliss_dict[symbols[0]][0]
            except KeyError:
                symbols = symbols[1:]
            else:
                blissymbol = blissymbol.getBlissName()
                blissymbols.append(blissymbol)
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
                            blissymbols.append(blissymbol)
                    break
                else:
                    print trans_word.eng_bliss_dict

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
                            unicodes.append(unicode[2:])
                            break
                print unicodes
                prediction = " ".join(unicodes)
            print("synset: ", pair)
            print("prediction: ", prediction)
            self.fitWordToClassifier(word_id, pos_code, prediction)

        return blissymbols
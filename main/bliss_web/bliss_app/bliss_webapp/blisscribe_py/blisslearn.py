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
from sklearn.tree import DecisionTreeClassifier
from random import shuffle
from parts_of_speech import POS_FEATURE_DICT, POS_CODE_DICT, POS_ABBREVS_SORTED


class BlissLearner:
    """
    A machine learning classifier for Blissymbols.
    """
    PATH = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, bliss_translator):
        self.translator = bliss_translator
        self.bliss_lexicon = self.translator.eng_bliss_dict
        self.classifier = DecisionTreeClassifier()
        self.questions = list()
        self.answers = list()
        self.wordnet_indices = self.get_wordnet_indices()  # dict
        self.wordnet_entries = self.get_wordnet_entries()  # dict
        self.wordnet_words = {entry[0] for entry in self.wordnet_entries}
        self.wordnet_descriptions = self.get_wordnet_descriptions()  # dict
        self.init_classifier()

    def init_classifier(self):
        """
        Fits data to this BlissClassifier's classifier for future predicting.

        :return: None
        """
        samples = self.wordnet_indices
        test_questions, test_answers = list(), list()
        common_words = self.read_common_words()
        print("initializing Bliss classifier...")

        # percent on-target: 0.0%
        # percent on-target: 2.64700321422%
        # percent on-target: 9.88755331524%
        # percent on-target: 95.6051873199%
        # percent on-target: 79.5349488724% -> whyyy
        # percent on-target: 85.8133669609% -> ok better...
        # percent on-target: 87.3926796204%
        # percent on-target: 34.1225626741% -> nooooo but ok it's still getting better
        # percent on-target: 40.9489916963%
        # percent on-target: 44.6297700278%
        # percent on-target: 45.0088450847%

        for entry in self.bliss_lexicon:
            bliss_set = self.bliss_lexicon[entry]
            if bliss_set is not None:
                print entry, bliss_set
                bs = self.translator.word_to_blissymbol(entry)
                blissymbols = sorted(bliss_set, key=lambda bs: len(bs.derivations), reverse=True)
                if bs in bliss_set:
                    blissymbols.remove(bs)
                if bs is not None:
                    blissymbols.insert(0, bs)

                print entry, "has the Blissymbols", blissymbols

                for blissymbol in blissymbols:
                    synsets = blissymbol.synsets
                    if len(synsets) > 0:
                        ss = blissymbol.synset
                        synsets = list(synsets)
                        synsets.insert(0, ss)
                        unis = blissymbol.get_deriv_unicode()
                        uni = self.unicodes_to_str(unis)
                        for synset in synsets:
                            pos = synset.pos()
                            pos_code = self.pos_to_int(pos)
                            wn_num = self.find_synset_id(synset.offset(), pos_code)
                            word_features = [wn_num, pos_code]
                            if entry.lower() in common_words:
                                if entry in synset.lemma_names():
                                    self.add_question_answer(word_features, uni)
                                elif word_features not in self.questions and word_features not in test_questions:
                                    test_answers.append(uni)
                                    test_questions.append(word_features)
                print

        for wn_num in samples:
            # convert human-readable data to machine-readable numbers
            defns = samples[wn_num]
            shuffle(defns)  # shuffle defns for random order

            for defn in defns:  # iterate thru each Wordnet definition
                name = defn[0]
                pos = defn[1]
                pos_unabbrev = self.translator.unabbreviate_tag(pos)
                trans_word = self.translator.make_translation_word(name, pos_unabbrev)

                if trans_word.has_blissymbol():
                    blissymbol = trans_word.blissymbol
                    unis = blissymbol.get_deriv_unicode()
                    uni = self.unicodes_to_str(unis)
                    pos_code = self.pos_to_int(pos)
                    word_features = [wn_num, pos_code]
                    synsets = blissymbol.synsets

                    if word_features not in self.questions and len(synsets) > 0:
                        synset = blissymbol.synset
                        synsets = list(synsets)
                        synsets.insert(0, synset)
                        for synset in synsets:
                            if self.find_synset_id(synset.offset(), pos_code) == wn_num:
                                if name.lower() in common_words and word_features not in test_questions:
                                    # and name in synset.lemma_names():
                                    # self.add_question_answer(word_features, uni)
                                    test_answers.append(uni)
                                    test_questions.append(word_features)

        train_questions, train_answers = self.questions, self.answers
        test_questions, test_answers = test_questions, test_answers

        print("\ntraining classifier...")
        self.classifier.fit(train_questions, train_answers)
        print("training complete.\n")

        print("\ntesting classifier...")
        self.test_classifier(test_questions, test_answers)
        print("testing complete.")

        print("")
        print("trained with " + str(len(self.questions)) + " question-answer sets")
        print("tested with " + str(len(test_questions)) + " question-answer sets")
        print("word coverage: " + str(len(self.questions)/float(len(samples))))
        print("")

        self.train_classifier(test_questions, test_answers)

    def write_examples(self):
        """
        Writes this BlissLearner's question-answer sets to
        a wordnet_to_bliss.txt file.
        ~
        Used for overseeing this BlissLearner's learning.

        :return: None
        """
        path = self.translator.PATH + "/wordnet_to_bliss.txt"

        with open(path, "w") as examples:
            for qa in zip(self.questions, self.answers):
                q_word = self.find_id_synsets(qa[0][0])[0]
                q_pos = self.int_to_pos(qa[0][1])
                a_desc = ("/".join(self.translator.lookup_unicode_to_bliss(self.str_to_unicode(ans)))
                          for ans in qa[1].split(" "))
                a_desc = " + ".join(a_desc)
                examples.write("# " + str(q_word[0]) + ", " + str(q_pos) + " -> " + str(a_desc) + "\n")
                examples.write(str(qa) + "\n\n")
            examples.close()

    def read_common_words(self, cap=50000):
        """
        Returns a set of the most common words in English, up to cap.
        ~
        Used to train BlissLearner with proper examples.

        :param cap: int, maximum number of common words to output
        :return: Set(str), most common words in English
        """
        path = self.translator.PATH + "/resources/frequency_words/content/2016/en/en_50k.txt"
        with open(path, "r") as words:
            common_words = set()
            idx = 0
            for word in words:
                if idx >= cap:
                    break
                common_words.add(word.rsplit(" ", 1)[0])
                idx += 1
        return common_words

    def add_question_answer(self, question, answer):
        """
        Adds this question and answer to this BlissClassifier's
        questions and answers respectively.

        :param question: tuple(int, int), synset's 9-digit ID and part-of-speech code
        :param answer: str, a list of 4-character unicodes corresponding
            to the synset's Blissymbol translation
        :return: None
        """
        if question[0] in [q[0] for q in self.questions]:
            return
        else:
            self.questions.append(question)
            self.answers.append(answer)

    def refit_classifier(self):
        """
        Refits this BlissLearner's classifier according to
        its current questions and answers fields.
        ~
        Allows updated learning with more examples.

        :return: None
        """
        self.classifier.fit(self.questions, self.answers)

    def train_classifier(self, questions, answers):
        """
        Refits this BlissLearner's classifier according to
        these questions and answers.
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

    def test_classifier(self, test_questions, test_answers):
        """
        Tests this BlissLearner's classifier according to
        these questions and answers.

        :param test_questions: List[List[int,int]], list with lists of
            wordnet IDs and their pos codes
        :param test_answers: str, unicode responses (without U+ prefix)
        :return: None
        """
        hits = []
        misses = []
        unicode_hits = 0
        all_unicodes = 0

        for (q, ans) in zip(test_questions, test_answers):
            guess = self.classifier.predict([q])[0]
            if guess != ans:
                misses.append((ans, guess, q))
                guess_lst = set(guess.split(" "))
                ans_lst = set(ans.split(" "))
                unicode_hits += len(guess_lst.intersection(ans_lst))
                all_unicodes += len(guess_lst) + len(ans_lst)
            else:
                hits.append((ans, guess, q))
            self.add_question_answer(q, ans)

        all = sorted(hits) + sorted(misses)
        self.test_results(all)

        print("")
        print("number on-target: " + str(len(test_questions) - len(misses)) + " out of " + str(len(test_questions)))
        print("percent on-target: " + str(float(len(test_questions) - len(misses))/len(test_questions) * 100) + "%")
        print("")
        print("partly on-target: " + str(unicode_hits) + " out of " + str(all_unicodes))
        print("percent pt on-target: " + str(float(unicode_hits)/all_unicodes * 100) + "%")
        print("")

    def test_results(self, all):
        """
        For each answer-guess-question 3-tuple in all,
        print the question, answer, and guess in this format:

            question: rabbit
            answer:   rodent teeth ear
            guess:    animal ear

        :param all: List[3-tuple], where each 3-tuple has an...
            [0] answer: str, correct unicode Blissymbol characters
            [1] guess: str, machine classified unicode Blissymbol characters
            [2] question: List[int, int], synset number and pos code
        :return: None
        """
        for (ans, guess, q) in all:
            print("")

            # format answer from unicode to Bliss words
            ans = ans.split(" ")
            new_ans = []
            for uni in ans:
                defns = self.translator.lookup_unicode_to_bliss(self.str_to_unicode(uni))
                if len(defns) != 0:
                    defn = defns[0]
                    new_ans.append(defn.replace(" ", "_"))
            ans = " ".join(new_ans)

            # format guess from unicode to Bliss words
            guess = guess.split(" ")
            new_guess = []
            for uni in guess:
                defns = self.translator.lookup_unicode_to_bliss(self.str_to_unicode(uni))
                if len(defns) != 0:
                    defn = defns[0]
                    new_guess.append(defn.replace(" ", "_"))
            guess = " ".join(new_guess)

            q = self.wordnet_indices[q[0]]
            q = q[0][0]
            print('question:\t{:<30s}\nanswer:  \t{:<40s}\nguess:   \t{:<40s}'.format(q, ans, guess))
            print("")

    def pos_to_int(self, pos):
        """
        Takes in a part-of-speech (from n, v, a, s, r) and
        returns its corresponding WordNet integer.

        :param pos: str, single-character part-of-speech
        :return: int, pos's corresponding WordNet integer
        """
        return POS_FEATURE_DICT[pos]

    def int_to_pos(self, code):
        """
        Takes in a WordNet integer (in range(0,4)) and
        returns its corresponding WordNet part-of-speech.
        ~
        N.B. Since adjectives ("a") and adjective sattelites ("s")
        are both indexed at 3, this method returns "a" if given 3.

        :param pos: int, code corresponding to WordNet part-of-speech
        :return: str, this code's single-character part-of-speech
        """
        return POS_CODE_DICT[code]

    def get_synset_id(self, synset):
        """
        Finds a synset ID for this synset.

        :param synset: Synset, synset to find ID for
        :return: int, a 9-digit Wordnet Synset ID
        """
        return self.translator.get_synset_id(synset)

    def find_synset_id(self, offset, pos_code):
        """
        Finds a synset ID for a synset with this offset
        and pos_code (in range(0,4)).

        :param offset: int, 7-digit offset of synset to find ID for
        :param pos_code: int, 1-digit pos code of synset to find ID for
        :return: int, a 9-digit Wordnet Synset ID
        """
        return self.translator.find_synset_id(offset, pos_code)

    def find_id_synsets(self, id):
        """
        Returns a list of 2-tuples of synsets and their
        parts of speech for this synset ID.

        :param id: int, a 9-digit Wordnet Synset ID
        :return: List[(str,str)], list of synsets
        """
        synset = self.wordnet_indices[id]
        return synset

    def get_wordnet_indices(self):
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

    def get_wordnet_entries(self):
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

    def get_wordnet_descriptions(self):
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

    def get_bliss_to_unicode(self):
        return self.translator.get_bliss_to_unicode()

    def get_unicode_to_bliss(self):
        return self.translator.get_unicode_to_bliss()

    def str_to_unicode(self, string):
        """
        Prefixes this string with "U+".
        ~
        Used to convert classifier's unicode outputs to
        Blissymbol unicode keys.

        :param string: str, string to prefix
        :return: str, string unicode
        """
        return "U+" + string

    def str_to_unicodes(self, string):
        """
        Converts this string to a list of unicodes.
        ~
        e.g. str_to_unicodes("2573 3652") -> ["U+2573", "U+3652"]

        :param string: str, string to convert to list of unicodes
        :return: List[str], unicode strings
        """
        unis = [self.str_to_unicode(uni) for uni in string.split(" ")]
        return unis

    def unicode_to_str(self, uni):
        """
        Converts this unicode to a string by removing "U+"
        from the beginning.
        ~
        e.g. unicode_to_str("U+2573") -> "2573"

        :param uni: str, unicode to convert to string
        :return: str, unicode as string
        """
        return uni[2:]

    def unicodes_to_str(self, unis):
        """
        Converts this list of unicodes to a string.
        ~
        e.g. unicode_to_str(["U+2573", "U+3652"]) -> "2573 3652"

        :param string: List[str], list of unicodes to convert to string
        :return: str, string of all unicode names
        """
        unis = [self.unicode_to_str(uni) for uni in unis]
        return " ".join(unis)

    def lookup_wordnet_entry(self, trans_word):
        """
        Performs and returns a lookup in self.wordnet_entries
        for this (lemma, pos) pair, where lemma is
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

        :param lexeme: str, a lemma to lookup in WordNet
        :param pos: str, this lemma's pos tag
        :return: List[int, str], this word's WordNet word ID
            and pos code
        """
        if trans_word.eng_lemma is None:
            trans_word.init_eng_lemma(debug=True)

        lexeme = trans_word.eng_lemma

        if lexeme not in self.wordnet_words:
            lexeme = lexeme.title()
            if lexeme not in self.wordnet_words:
                return []

        pos = trans_word.pos
        pos_abbrev = self.translator.abbreviate_tag(pos)
        pos_code = POS_FEATURE_DICT[pos_abbrev]

        try:
            self.wordnet_entries[(lexeme, pos_abbrev)]
        except KeyError:
            for pt_of_speech in POS_ABBREVS_SORTED:
                try:
                    self.wordnet_entries[(lexeme, pt_of_speech)]
                except KeyError:
                    print("word " + self.translator.deunicodize(lexeme) + ", " + str(pt_of_speech) + " not in dict")
                    continue
                else:
                    pos_abbrev = pt_of_speech
                    pos_code = POS_FEATURE_DICT[pos_abbrev]
                    word_id = self.wordnet_entries[(lexeme, pt_of_speech)][0]
                    new_pos = self.translator.unabbreviate_tag(pt_of_speech)
                    trans_word.set_pos(new_pos)
                    trans_word.set_synset_id(word_id)
                    break
            else:
                ans = raw_input("Enter y to translate this word to Blissymbols yourself, " +
                                "or n to choose not to translate it to Blissymbols.\n")
                if ans == "y":
                    blissymbols = trans_word.add_new_derivations()
                    return blissymbols
                else:
                    return []
        else:
            word_id = trans_word.synset_id

        if word_id is None:
            return []
        else:
            pair = [int(word_id), pos_code]
            return pair

    def predict(self, pair):
        """
        Returns a string of Blissymbol unicodes predicted from
        this BlissLearner's classifier with this Wordnet number
        and word pair.

        :param pair: List[int, str], WordNet number and word
        :return: List[str], strings of Blissymbol unicodes
        """
        return self.classifier.predict([pair])

    def predict_word(self, trans_word, debug=True):
        """
        Returns a list of Blissymbol derivations predicted to correspond
        with this trans_word.

        :param trans_word: TranslationWord, word to get derivations of
        :return: List[str], Blissymbols for this trans_word
        """
        pair = self.lookup_wordnet_entry(trans_word)

        if len(pair) == 0:
            return pair
        else:
            print(pair)
            blissymbols = list()
            prediction = self.predict(pair)
            prediction = prediction[0]
            unicodes = str(prediction).split(" ")
            unicodes = ["U+" + uni for uni in unicodes if uni != ""]

            for uni in unicodes:
                symbols = self.get_unicode_to_bliss()[uni]
                try:
                    bs = trans_word.eng_bliss_dict[symbols[0]]
                except KeyError:
                    symbols = symbols[1:]
                else:
                    print symbols[0]
                    print bs
                    blissymbol = next(iter(bs))
                    blissymbol = blissymbol.get_bliss_name()
                    blissymbols.append(blissymbol)
                    continue

                for symbol in symbols:
                    if symbol in trans_word.eng_bliss_dict:
                        blissymbol = trans_word.eng_bliss_dict[symbol][0]
                        blissymbol = blissymbol.get_bliss_name()

                        if debug:
                            print("I'm about to translate the word " + trans_word.eng_lemma +
                                  ", " + trans_word.pos + " with the Blissymbol " + str(blissymbol) + ".  Is that ok?")
                            answer = raw_input("Enter y for yes, n for no.  Enter s to skip to the next Blissymbol.\n")

                            if answer == "n":
                                ans = raw_input("Enter y to translate this word to Blissymbols yourself, " +
                                                "or n to choose not to translate it to Blissymbols.\n")
                                if ans == "y":
                                    blissymbols = trans_word.add_new_derivations() #self.add_new_derivations(trans_word)
                                    break
                                else:
                                    return []

                            elif answer == "s":
                                continue

                            else:
                                blissymbols.add(blissymbol)

                        break

            if debug:
                print("I'm about to translate the word " + trans_word.eng_lemma +
                      " with the Blissymbols " + str(blissymbols) + ".  Is that ok?")
                answer = raw_input("Enter y for yes, n for no.\n")

                if answer == "n":
                    blissymbols = trans_word.add_new_derivations() #self.add_new_derivations(trans_word)
                    unicodes = []
                    symbols = []
                    for symbol in blissymbols:
                        symbols += symbol.split(",")

                    for symbol in symbols:
                        try:
                            unis = self.get_bliss_to_unicode()[symbol]
                        except KeyError:
                            continue
                        else:
                            uni = unis[0]
                            unicodes.append(self.unicode_to_str(uni))
                            break

                    prediction = " ".join(unicodes)

                self.add_question_answer(pair, prediction)

            return blissymbols
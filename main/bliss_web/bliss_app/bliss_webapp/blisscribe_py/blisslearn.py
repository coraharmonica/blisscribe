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


class BlissClassifier:
    """
    A machine learning classifier for Blissymbols.
    """
    PATH = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, bliss_translator):
        self.translator = bliss_translator
        self.blissymbols = self.translator.lex_parser.blissymbols
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
        all_blissymbols = self.blissymbols
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
        # percent on-target: 62.2127313402%

        for blissymbol in all_blissymbols:
            if not blissymbol.is_atom:
                synsets = blissymbol.synsets
                unis = blissymbol.get_deriv_unicode()
                uni = self.unicodes_to_str(unis)
                eng_lemmas = set(blissymbol.get_translation("English"))

                for synset in synsets:
                    pos_code = self.pos_to_int(synset.pos())
                    wn_num = self.synset_id(synset)
                    word_features = [wn_num, pos_code]
                    intersection = eng_lemmas.intersection(synset.lemma_names())

                    if len(intersection) != 0:
                        self.add_question_answer(word_features, uni)
                    elif word_features not in test_questions and word_features not in self.questions:
                        test_questions.append(word_features)
                        test_answers.append(uni)

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
        Writes this BlissClassifier's question-answer sets to
        a wordnet_to_bliss.txt file.
        ~
        Used for overseeing this BlissClassifier's learning.

        :return: None
        """
        path = self.translator.PATH + "/wordnet_to_bliss.txt"

        with open(path, "w") as examples:
            for qa in zip(self.questions, self.answers):
                q_word = self.find_id_synsets(qa[0][0])[0]
                q_pos = self.int_to_pos(qa[0][1])

                ans_desc = ("/".join(self.translator.lookup_unicode_to_bliss(self.hex_to_unicode(ans)))
                            for ans in qa[1].split(" "))
                ans_desc = " + ".join(ans_desc)

                examples.write("# " + str(q_word[0]) + ", " + str(q_pos) + " -> " + str(ans_desc) + "\n")
                examples.write(str(qa) + "\n\n")

            examples.close()

    def read_common_words(self, cap=50000):
        """
        Returns a set of the most common words in English, up to cap.
        ~
        Used to train BlissClassifier with proper examples.

        :param cap: int, maximum number of common words to output
        :return: Set(str), most common words in English
        """
        path = self.translator.PATH + "/speechart/resources/frequency_words/content/2016/en/en_50k.txt"
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
        Refits this BlissClassifier's classifier according to
        its current questions and answers fields.
        ~
        Allows updated learning with more examples.

        :return: None
        """
        self.classifier.fit(self.questions, self.answers)

    def train_classifier(self, questions, answers):
        """
        Refits this BlissClassifier's classifier according to
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
        Tests this BlissClassifier's classifier according to
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

            # format answers & guesses from unicode to Bliss words
            answers = ans.split(" ")
            ans_unis = self.hexes_unicodes(answers)
            new_ans = self.unicodes_blisswords(ans_unis)
            ans = " + ".join(new_ans)

            guesses = guess.split(" ")
            guess_unis = self.hexes_unicodes(guesses)
            new_guess = self.unicodes_blisswords(guess_unis)
            guess = " + ".join(new_guess)

            q = self.wordnet_indices[q[0]]
            q = q[0][0]
            print('question:\t{:<30s}\nanswer:  \t{:<40s}\nguess:   \t{:<40s}\n'.format(q, ans, guess))

    def unicode_blissword(self, uni):
        """
        Returns the name of the Blissymbol corresponding to
        this unicode str.

        :param uni: str, unicode string for a Blissymbol
        :return: str, name of Blissymbol for uni
        """
        defns = self.translator.lookup_unicode_to_bliss(uni)

        if len(defns) != 0:
            defn = defns[0]
            clean_defn = self.translator.underscore(defn)
            return clean_defn
        else:
            return

    def hexes_unicodes(self, hexes):
        """
        Returns the names of the Blissymbols corresponding to
        each unicode str in unis.

        :param hexes: List[str], list of hexadecimal strings
        :return: List[str], list of unicode strings
        """
        return [self.hex_to_unicode(h) for h in hexes]

    def unicodes_blisswords(self, unis):
        """
        Returns the names of the Blissymbols corresponding to
        each unicode str in unis.

        :param unis: List[str], list of unicode strings
        :return: List[str], Blissymbol names for unicodes in unis
        """
        blisswords = list()

        for uni in unis:
            blissword = self.unicode_blissword(uni)
            if blissword is not None:
                blisswords.append(blissword)

        return blisswords

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

    def synset_id(self, synset):
        """
        Finds a synset ID for this synset.

        :param synset: Synset, synset to find ID for
        :return: int, a 9-digit Wordnet Synset ID
        """
        return self.translator.synset_id(synset)

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

    def hex_to_unicode(self, string):
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
        unis = [self.hex_to_unicode(uni) for uni in string.split(" ")]
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

    def lemma_in_wordnet(self, word):
        """
        Returns True if this word is in (English) WordNet,
        False otherwise.

        :param word: str, word to check whether in WordNet
        :return: bool, whether word is in WordNet
        """
        return word in self.wordnet_words

    def pair_in_wordnet(self, lemma, pos):
        """
        Returns True if this (lemma, pos) pair is in (English) WordNet,
        False otherwise.

        :param lemma: str, word to check whether in WordNet with pos
        :param pos: str, pos to check whether in WordNet with lemma
        :return: bool, whether (lemma, pos) is in WordNet
        """
        try:
            self.wordnet_entries[(lemma, pos)]
        except KeyError:
            return False
        else:
            return True

    def trans_word_in_wordnet(self, trans_word):
        """
        Returns True if this TranslationWord's (eng_lemma, pos) pair
        is in (English) WordNet, False otherwise.

        :param trans_word: TranslationWord, word to check whether in WordNet
        :return: bool, whether trans_word is in WordNet
        """
        lemma = trans_word.eng_lemma
        pos = self.abbreviate_pos(trans_word.pos)
        return self.pair_in_wordnet(lemma, pos)

    def abbreviate_pos(self, pos):
        """
        Returns an abbreviation for this Penn Treebank
        part of speech from "a", "v", "n", "r", "s".
        ~
        e.g. abbreviate_pos("RB") -> "r"

        :param pos: str, Penn Treebank part of speech
        :return: str, 1-character abbreviated part of speech
        """
        return self.translator.abbreviate_pos(pos)

    def trans_word_wordnet_lemma(self, trans_word):
        """
        Returns a lemma for this trans_word that is in WordNet.
        ~
        If no lemma for this trans_word is in WordNet, returns None.

        :param trans_word: TranslationWord, word to find WordNet lemma for
        :return: str, TranslationWord lemma in WordNet
        """
        if trans_word.eng_lemma is None:
            return
            #trans_word.init_eng_lemma(debug=True)

        lemma = trans_word.eng_lemma

        if not self.lemma_in_wordnet(lemma):
            lemma = lemma.title()
            if not self.lemma_in_wordnet(lemma):
                return

        return lemma

    def lemma_wordnet_pos(self, lemma):
        """
        Returns the first part of speech for this lemma
        in WordNet.
        ~
        If no WordNet entry exists for this lemma and any part of speech,
        returns None.

        :param lemma: str, WordNet lemma to find part of speech for
        :return: str, part of speech in WordNet with this lemma
        """
        if self.lemma_in_wordnet(lemma):
            for pos in POS_ABBREVS_SORTED:
                try:
                    self.wordnet_entries[(lemma, pos)]
                except KeyError:
                    print("word " + self.translator.deunicodize(lemma) + ", " + str(pos) + " not in dict")
                    continue
                else:
                    return pos

    def wordnet_trans_word(self, trans_word):
        """
        Returns this TranslationWord such that its
        synset_id, eng_lemma, and pos are all in WordNet.
        ~
        If no synset_id can be found for this TranslationWord's
        lemma and pos, returns None.

        :param trans_word: TranslationWord, word to modify for WordNet
        :return: TranslationWord, trans_word modified for WordNet
        """
        lemma = self.trans_word_wordnet_lemma(trans_word)
        pos = self.lemma_wordnet_pos(lemma)

        if self.pair_in_wordnet(lemma, pos):
            word_id = self.wordnet_entries[(lemma, pos)][0]
            new_pos = self.translator.unabbreviate_pos(pos)
            synset = self.translator.id_synset(word_id)
            trans_word.set_pos(new_pos)
            trans_word.add_eng_lemma(lemma)
            trans_word.set_synset(synset)
            return trans_word

    def lookup_wordnet_entry(self, trans_word):
        """
        Performs and returns a lookup in self.wordnet_entries
        for this trans_word's lemma and part of speech.
        ~
        N.B. An abbreviated pos tag is one of the following:
            n, v, a, s, r

            n - Noun
            v - Verb
            a - Adjective
            s - Adjective (satellite)
            r - Adverb

        :param trans_word: TranslationWord, word to lookup in WordNet
        :return: List[int, str], this word's WordNet word ID
            and pos code
        """
        trans_word = self.wordnet_trans_word(trans_word)

        if trans_word is None:
            return
        else:
            word_id = int(trans_word.synset_id)
            pos_code = self.pos_to_int(trans_word.pos)
            pair = (word_id, pos_code)
            return pair

    def predict(self, pair):
        """
        Returns a string of Blissymbol unicodes predicted from
        this BlissClassifier's classifier with this Wordnet number
        and word pair.

        :param pair: List[int, str], WordNet number and word
        :return: List[str], strings of Blissymbol unicodes
        """
        return self.classifier.predict([pair])

    def prediction_to_unicodes(self, prediction):
        """
        Returns a list of Blissymbol unicodes from this prediction.

        :param prediction: List[str], classifier's predicted unicodes
        :return: List[str], Blissymbol unicodes
        """
        prediction = prediction[0]
        unicodes = str(prediction).split(" ")
        return ["U+" + uni for uni in unicodes if uni != ""]

    def choose_translation(self, trans_word):
        ans = raw_input("Enter y to translate " + trans_word.eng_lemma + " to Blissymbols yourself, " +
                        "or n to choose not to translate it to Blissymbols.\n")
        if ans == "y":
            trans_word.add_new_derivations()

    def verify_translation(self, trans_word, blissymbol):
        print("I'm about to translate the word " + trans_word.eng_lemma +
              ", " + trans_word.pos + " with the Blissymbol " + str(blissymbol) + ".  Is that ok?")
        answer = raw_input("Enter y for yes, n for no.  Enter s to skip to the next Blissymbol.\n")

        if answer == "n":
            self.choose_translation(trans_word)

        return trans_word.blissymbol

    def verify_translations(self, trans_word, blissymbols):
        print("I'm about to translate the word " + trans_word.eng_lemma +
              ", " + trans_word.pos + " with the Blissymbols " + str(blissymbols) + ".  Is that ok?")
        answer = raw_input("Enter y for yes, n for no.\n")

        if answer == "n":
            self.choose_translation(trans_word)
            unicodes = [self.unicode_to_str(bs.unicode) for bs in trans_word.blissymbol.derivation_blissymbols()]
            prediction = " ".join(unicodes)
            return prediction

    def predict_word(self, trans_word, debug=True):
        """
        Returns a list of Blissymbol derivations predicted to correspond
        with this trans_word.

        :param trans_word: TranslationWord, word to get derivations of
        :return: List[str], Blissymbols for this trans_word
        """
        pair = self.lookup_wordnet_entry(trans_word)
        blissymbols = list()

        if pair is not None:
            print(pair)

            prediction = self.predict(list(pair))
            unicodes = self.prediction_to_unicodes(prediction)

            for uni in unicodes:
                blisswords = self.translator.lookup_unicode_to_bliss(uni)

                for blissword in blisswords:
                    entries = self.translator.lookup_bliss_dict(blissword, "English")

                    if entries is not None:
                        blissymbol = next(iter(entries))

                        if debug:
                            blissymbol = self.verify_translation(trans_word, blissymbol)
                            if blissymbol is None:
                                continue

                        blissymbols.append(blissymbol.bliss_name)
                        break

            if debug:
                prediction = self.verify_translations(trans_word, blissymbols)
                if prediction is not None:
                    self.add_question_answer(pair, prediction)

        return blissymbols
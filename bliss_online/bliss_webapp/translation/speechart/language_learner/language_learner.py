# coding: utf-8
"""
LANGUAGE LEARNER:

    Used to teach language.

    TODO: Create a semantic framework that translates to all languages.
    - Every word/sentence expresses something.
    - Sentences are linked to each other in meaning.
        > there are meanings that span the entire text (global)
            e.g. Alice, the White Rabbit, Wonderland
        > there are meanings that span >=1 sentences at a time (local)
        > there are words with meanings not in the text but in culture
            e.g. Humpty Dumpty
"""
import re
import os
import string
from nltk.tokenize import WordPunctTokenizer, PunktSentenceTokenizer
from main.bliss_web.bliss_app.bliss_webapp.blisscribe_py.ordered_set import OrderedSet
from main.bliss_web.bliss_app.bliss_webapp.blisscribe_py.ordered_dict import OrderedDict


class LanguageLearner:
    PATH = os.path.dirname(os.path.realpath(__file__))
    LANG_CODES = {"Afrikaans": "af",
                  "Albanian": "sq",
                  "Arabic": "ar",
                  "Armenian": "hy",
                  "Basque": "eu",
                  "Bengali": "bn",
                  "Bosnian": "bs",
                  "Breton": "br",
                  "Bulgarian": "bg",
                  "Catalan": "ca",
                  "Chinese": "zh",
                  "Croatian": "hr",
                  "Danish": "da",
                  "Dutch": "nl",
                  "English": "en",
                  "Esperanto": "eo",
                  "Georgian": "ka",
                  "German": "de",
                  "Greek": "el",
                  "Finnish": "fi",
                  "French": "fr",
                  "Galician": "gl",
                  "Hebrew": "he",
                  "Hindi": "hi",
                  "Hungarian": "hu",
                  "Icelandic": "is",
                  "Indonesian": "id",
                  "Italian": "it",
                  "Japanese": "ja",
                  "Kazakh": "kk",
                  "Korean": "ko",
                  "Latvian": "lv",
                  "Lithuanian": "lt",
                  "Macedonian": "mk",
                  "Malayan": "ml",
                  "Malay": "ms",
                  "Norwegian": "no",
                  "Persian": "fa",
                  "Polish": "pl",
                  "Portuguese": "pt",
                  "Romanian": "ro",
                  "Russian": "ru",
                  "Serbian": "sr",
                  "Sinhala": "si",
                  "Slovak": "sk",
                  "Slovenian": "sl",
                  "Spanish": "es",
                  "Swedish": "sv",
                  "Tamil": "ta",
                  "Telugu": "te",
                  "Thai": "th",
                  "Tagalog": "tl",
                  "Turkish": "tr",
                  "Ukrainian": "uk",
                  "Vietnamese": "vi"}

    def __init__(self):
        self.connections = dict()
        self.word_tokenizer = None

    def init_tokenizer(self):
        if self.word_tokenizer is None:
            self.word_tokenizer = WordPunctTokenizer()

    def get_lang_code(self, language):
        """
        Returns the language code associated with this language.
        ~
        e.g. get_lang_code("Polish") -> "pl"

        :param language: str, language to retrieve language code for
        :return: str, language code for given language
        """
        return self.LANG_CODES.get(language, None)

    def is_punct(self, char):
        """
        Returns True if the first character in char is punctuation.

        :param char: str, character to check whether punctuation
        :return: bool, whether char is punctuation or not
        """
        return char[0] in string.punctuation

    def contains_punct(self, word):
        """
        Returns True if any punctuation characters are in this word.

        :param word: str, word to check whether containing punctuation
        :return: bool, whether punctuation in this word or not
        """
        return any(char in word for char in "\n\t "+string.punctuation)

    def common_words(self, language=None, lim=50000):
        """
        Returns the most common words in this language up to lim.

        :param lim: int, lim <= 50000, number of words to retrieve
        :param language: Optional[str], language of common words
        :return: List[str], 50k most common words in language
        """
        lang_code = self.get_lang_code(language)

        if lang_code is None:
            return

        words = list()
        path = self.PATH.strip("language_learner") + \
               "resources/frequency_words/content/2016/%s/%s_50k.txt" % (lang_code, lang_code)

        with open(path, 'r') as fifty_k:
            line_no = 0
            for line in fifty_k:
                word = line.split(" ", 1)[0]
                #word = self.unicodize(word)
                words.append(word)
                if line_no > lim:
                    break
                line_no += 1

        return words

    def teach_from_source(self, language, filename):
        """
        Teaches this LanguageLearner in this language with the
        file for this filename.

        :param language: str, language of text in filename
        :param filename: str, filename to open for text in language
        :return: None
        """
        txt = open(filename)
        self.teach(txt, language)

    def crossteach_from_sources(self, **kwargs):
        """
        Crossteaches each file in different languages so that they
        translate back to the same thing.
        ~
        Each parameter name in kwargs should be the name of a language,
        assigned to a string filename in that language.

        :param kwargs: str, string for filename in parameter name's language
        :return: None
        """
        texts = list()
        for lang in kwargs:
            filename = kwargs[lang]
            texts.append(open(filename))
        self.crossteach(texts=texts, langs=kwargs.keys())

    def teach(self, text, language):
        """
        Teaches this text in this language to this LanguageLearner.

        :param text: str, text to teach
        :param language: str, language of text
        :return: None
        """
        pass

    def crossteach(self, texts, langs):
        """
        Teaches these texts in these languages to this LanguageLearner,
        cross-referencing each with the other so as to construct a multilingual
        dictionary.

        :param texts: List[str], texts to teach
        :param langs: List[str], languages paired to texts
        :return: None
        """
        breakpts = []
        for text in texts:
            breakpt = self.text_breakpoints(text)
            breakpts.append(breakpt)

        if len(breakpts) != 0:
            for i in range(len(breakpts[0])):
                matches = [breakpt[i] for breakpt in breakpts]
                self.crossmatch(matches, langs)

        return

    def remove_punct(self, text):
        """
        Removes all punctuation from text.

        :param text: str, text to remove punctuation from
        :return: str, text with all punctuation removed
        """
        return re.sub("[^ \w\-']+", "", text)

    def crossmatch(self, matches, langs):
        """
        Crossmatches each match in matches with each other
        such that they translate to each other.
        ~
        All matches should be translations of the same text
        in different languages.
        ~
        e.g. crossmatch(["The cat is on the mat", "Le chat est sur le tapis"], ["English", "French"]) ->
             {"the": {"fr": ["le"]}, "cat": {"fr": ["chat"]}, "is": {"fr": ["est"]},
              "on": {"fr": ["sur"]}, "mat": {"fr": ["tapis"]}}

        :param matches: List[str], translation of same text in different languages
        :param langs: List[str], languages paired to matches
        :return: dict, where...
            key (str) - language
            val (dict) - words in language with translations in other languages
        """
        # first treat it as if there's only 2 matches!  go slowly cora : )
        matches_sentences = [self.tokenize_sentences(self.tokenize_words(m)) for m in matches]
        all_matches = dict()

        for i in range(len(matches_sentences)):
            lang = langs[i]
            match_sentences = sorted(matches_sentences[i], key=len)
            lang_matches = OrderedDict([])

            for match_sentence in match_sentences:
                if len(match_sentence) != 0:
                    match_sentence = [ms for ms in match_sentence if not self.is_punct(ms)]
                    before_after = self.words_before_after(match_sentence)
                    lang_matches.update(before_after)

            all_matches[lang] = lang_matches

        print(all_matches)
        input("NOT GOING ON UNTIL YOU SAY SO")
        translation_dicts = dict()
        lang_words = dict()
        print("MATCHES BEFORE:", matches)

        '''
        for i in range(len(matches)):
            lang = langs[i]
            sentence = matches[i]
            trans_dict = self.translation_dict(sentence)
            translation_dicts.setdefault(lang, trans_dict)

        for i in range(len(matches)):
            lang = langs[i]
            sentence = matches[i]
            words = [w for w in self.tokenize_words(sentence) if not self.is_punct(w)]
            lang_words[lang] = words

        for i in range(len(lang_words.get(langs[0]))):
            synonyms = [lang_words[l][i] for l in langs]
            print "SYNONYMS:", synonyms

            for l in range(len(langs)):  # lang in langs:
                lang = langs[l]
                lang_synonym = synonyms[l]
                translation_dicts[lang].setdefault(lang_synonym, dict())

                for s in range(len(synonyms)):
                    if s != l:
                        trans_lang = unicode(langs[s][:2].lower())
                        synonym = unicode(synonyms[s])
                        translation_dicts[lang][lang_synonym].setdefault(trans_lang, list())
                        translation_dicts[lang][lang_synonym][trans_lang].append(synonym)
        '''
        print("MATCHES AFTER:", matches)
        return translation_dicts

    def tokenize_words(self, text):
        """
        Returns a list of all words and punctuation marks in text, in order.
        ~
        N.B. If a word appears in text as uppercase and
        lowercase, returns the lowercase version of the word.

        :param text: str, text to return words for
        :return: List[str], words in text
        """
        self.init_tokenizer()
        #text = self.unicodize(text)
        words = self.word_tokenizer.tokenize(text)
        return self.recapitalize_words(words)

    def tokenize_sentences(self, words, incl_punct=True):
        """
        Returns a list of all sentences from tokens in words, in order.

        :param words: List[str], word tokens to turn to sentences
        :param incl_punct: bool, whether to return punctuation from words
        :return: List[list], sentences from words
        """
        sentences = list()
        sentence = list()

        for word in words:
            if word[0] in ".!?":  # ending punctuation:
                sentences.append(sentence)
                sentence = list()
            else:
                if incl_punct or not self.is_punct(word):
                    sentence.append(word)

        return sentences

    def text_words(self, text):
        """
        Returns a list of all words in text, in order.
        ~
        N.B. If a word appears in text as uppercase and
        lowercase, returns the lowercase version of the word.

        :param text: str, text to return words for
        :return: List[str], words in text
        """
        if type(text) != list:
            words = list()
            #text = self.unicodize(text)

            while len(text) != 0:
                word = ""
                idx = 0

                for char in text:
                    is_clitic = char == "'" and (text[idx - 1] not in string.punctuation + " ") \
                                and (text[idx + 1] not in string.punctuation + " ")

                    if char in " \n\t" or (char in string.punctuation and not is_clitic):
                        if idx == 0:
                            idx += 1
                            continue
                        else:
                            break
                    else:
                        word += char
                        idx += 1

                if len(word) != 0:
                    #print "new word:", word
                    words.append(word.strip("'"))

                text = text[idx + 1:]  # skip to next word

            return [w if not (w.istitle() and w.lower() in words) else w.lower() for w in words]
        else:
            return text

    def text_before_after(self, text, n_gram=1):
        """
        Returns a dict with the words in this text as keys and a 2-tuple of
        words occurring (1) before and (2) after this word for vals.
        ~
        Used for figuring out which words come before others.
        ~
        e.g. text_before_after("Hi, I love you!") ->
             {"Hi": ([], ["I"]), "I": (["Hi"], ["love"]), "love": (["I"], ["you"]), "you": (["love"], [])}

        :param text: str, text in a language with words
        :param n_gram: int, number of words to check before
        :return: dict(str, tuple(list, list)), where...
            key (str) - word from text
            val (tuple(list, list)) - words coming before and after key word
        """
        words = self.tokenize_words(text)
        return self.words_before_after(words, n_gram=n_gram)

    def texts_before_after(self, texts, n_gram=1):
        """
        Returns a dict with the words in these texts as keys and a 2-tuple of
        words occurring (1) before and (2) after this word for vals.
        ~
        Used for figuring out which words come before others.
        ~
        e.g. texts_before_after(["Hi"], ["I love you!"]) ->
             {"Hi": ([], []), "I": ([], ["love"]), "love": (["I"], ["you"]), "you": (["love"], [])}

        :param text: str, text in a language with words
        :param n_gram: int, number of words to check before
        :return: dict(str, tuple(list, list)), where...
            key (str) - word from text
            val (tuple(list, list)) - words coming before and after key word
        """
        words = self.tokenize_words("\n\n".join(texts))
        return self.words_before_after(words, n_gram=n_gram)

    def recapitalize_words(self, words):
        """
        Returns this list of words with uppercase occurrences
        replaced by lowercase occurrences.  If an uppercase token
        has no lowercase token in words, keeps uppercase token.
        ~
        e.g. recapitalize_words(["The", "girl", "Alice", "likes", "the", "tea"]) ->
             ["the", "girl", "Alice", "likes", "the", "tea"]

        :param words: List[str], tokenized words from a text
        :return: List[str], words with uppercases as lowercases
        """
        return [word.lower() if not word.islower() and word.lower() in words else word for word in words]

    def words_before(self, words, n_gram=1):
        """
        Returns a dict with these words as keys and a list of
        words occurring before this word for vals.
        ~
        Used for figuring out which words come before others.
        ~
        e.g. words_before(["Hi", "I", "love", "you"]) ->
             {"I": ["Hi"], "love": ["I"], "you": ["love"]}

        :param words: List[str], word tokens in order of occurrence in text
        :param n_gram: int, number of words to check before
        :return: dict(str, list), where...
            key (str) - word from words
            val (tuple(List[str])) - words coming after key word
        """
        befores = dict()

        for i in range(len(words)):
            word = words[i]

            if not self.is_punct(word):
                prev_idx = i-1
                n_grams = n_gram

                while n_grams > 0 and prev_idx >= 0:
                    prev_word = words[prev_idx]

                    if self.is_punct(prev_word):
                        break
                    else:
                        befores.setdefault(word, list())
                        befores[word].append(prev_word)

                    n_grams -= 1
                    prev_idx -= 1

        res = dict()
        for word in befores:
            before = befores[word]
            print(word, before)
            entry = sorted(set(before), key=lambda b: before.count(b), reverse=True)
            res[word] = entry #[e for e in entry if before.count(e) > 1]

        return res

    def words_after(self, words, n_gram=1):
        """
        Returns a dict with these words as keys and a list of
        words occurring after this word for vals.
        ~
        Used for figuring out which words come after others.
        ~
        e.g. words_after(["Hi", "I", "love", "you"]) ->
             {"Hi": ["I"], "I": ["love"], "love": ["you"]}

        :param words: List[str], word tokens in order of occurrence in text
        :param n_gram: int, number of words to check after
        :return: dict(str, list), where...
            key (str) - word from words
            val (tuple(List[str])) - words coming after key word
        """
        afters = dict()

        for i in range(len(words)):
            word = words[i]

            if not self.is_punct(word):
                next_idx = i+1
                n_grams = n_gram

                while n_grams > 0:
                    try:
                        next_word = words[next_idx]
                    except IndexError:
                        break
                    else:
                        if self.is_punct(next_word):
                            break
                        else:
                            afters.setdefault(word, list())
                            afters[word].append(next_word)

                    n_grams -= 1
                    next_idx += 1

        res = dict()
        for word in afters:
            after = afters[word]
            print(word, after)
            entry = (sorted(set(after), key=lambda a: afters[word].count(a), reverse=True))
            res[word] = entry #[e for e in entry if after.count(e) > 1]

        return res

    def words_before_after(self, words, n_gram=1):
        """
        Returns a dict with these words as keys and a 2-tuple of
        words occurring (1) before and (2) after this word for vals.
        ~
        Used for figuring out which words come before others.
        ~
        e.g. words_before_after(["Hi", "I", "love", "you"]) ->
             {"Hi": ([], ["I"]), "I": (["Hi"], ["love"]), "love": (["I"], ["you"]), "you": (["love"], [])}

        :param words: List[str], word tokens in order of occurrence in text
        :param n_gram: int, number of words to check before and after
        :return: dict(str, tuple(list, list)), where...
            key (str) - word from words
            val (tuple(list, list)) - words coming before and after key word
        """
        befores = self.words_before(words, n_gram=n_gram)
        afters = self.words_after(words, n_gram=n_gram)
        befores_afters = {word: (befores.get(word, list()), afters.get(word, list())) for word in words}
        return befores_afters

    def words_shared_in_sentences(self, word, text):
        """
        Returns the most common words shared in each sentence with
        word in it.

        :param word: str, word in sentences
        :param text: str, sentences from a text
        :return: List[str], words shared by word in words
        """
        shared_words = OrderedSet([])
        words = self.tokenize_words(text)
        sentences = self.tokenize_sentences(words)
        word_sentences = [sent for sent in sentences if word in sent]

        for word_sent in word_sentences:
            shared_words.update(word_sent)

        freqs = shared_words.frequency_counts()
        print("WORD FREQUENCIES", freqs)
        for word_freq in freqs:
            freq = freqs[word_freq]
            # does word occur more in these sentences than all sentences?
            if (float(freq) / len(word_sentences)) > (float(words.count(word_freq)) / len(sentences)):
                # if so, include in final
                pass
            else:
                # else, remove from items
                shared_words.remove(word_freq)

        items = shared_words.items(min_ct=int((len(word_sentences)-1)/2.0))
        return items #[items.index(word)+1:]

    def text_synonyms(self, text, language=None, lim=1000):
        """
        Returns a dictionary of likely "synonyms" in text, where
        synonyms really means words occuring in the same context.
        (For now, that means that they have the same word(s) in front of
        and after them.)

        :param text: str, text to find synonyms for
        :param language: str, language of text
        :param lim: int, number of common words synonyms can consist of
        :return: dict(str, list), where...
            key (str) - word from text
            val (List[str]) - word(s) from text with same context as key word
        """
        words = self.tokenize_words(text)
        return self.words_synonyms(words, language=language, lim=lim)

    def classify_text(self, text, language=None, lim=1000):
        """
        Returns a dictionary of the different types of words in this text
        (e.g. nouns, verbs, etc.) according to where in the text they occur.

        :param text: str, text to find synonyms for
        :param language: str, language of text
        :param lim: int, number of common words synonyms can consist of
        :return: dict(int, list), where...
            key (int) - number
            val (List[str]) - words from text with same context
        """
        synonyms_dict = self.text_synonyms(text, language=language, lim=lim)
        synonyms_lst = sorted(list(synonyms_dict), key=lambda k: len(synonyms_dict[k]), reverse=True)
        categories = dict()
        synonyms_left = synonyms_lst[:]
        loops = 0
        max_loop = len(max(synonyms_dict.values(), key=len))

        while len(synonyms_left) > 0 and loops <= max_loop:
            for i1 in range(len(synonyms_lst)):
                synonym1 = synonyms_lst[i1]

                if synonym1 in synonyms_left:
                    print("FINDING CATEGORY FOR", synonym1.upper())
                    synonyms1 = synonyms_dict[synonym1]
                    category_syns = OrderedSet([])

                    for i2 in range(len(synonyms_left)):
                        synonym2 = synonyms_lst[i2]
                        if synonym2 != synonym1:
                            synonyms2 = synonyms_dict[synonym2]

                            if len(set(synonyms2).intersection(synonyms1)) == max(1, len(synonyms2)-loops) or \
                                len(set(synonyms1).intersection(synonyms2)) == max(1, len(synonyms1)-loops):
                                category_syns.add(synonym1)
                                category_syns.update(synonyms1)
                                category_syns.add(synonym2)
                                category_syns.update(synonyms2)

                    synonyms_left = [s for s in synonyms_left if s not in category_syns]
                    category = [c for c in category_syns.items(min_ct=1)
                                if not any([c in v for v in categories.values()])]

                    print("\t", synonym1, "appears synonymous with", category)

                    if len(category) != 0:
                        loops = 0
                        categories[len(categories)] = category

                    print("\n", len(synonyms_left), "words left to categorize\n\n")

            loops += 1

        if len(synonyms_left) != 0:
            categories[len(categories)] = synonyms_left

        return categories

    def find_ngrams(self, text, length=None, words=True):
        """
        Finds ngrams of words or chars if words is False.
        ~
        If length is None, finds longest ngrams with highest frequencoes.

        :param text: str, text to find ngrams in
        :param length: int, length of ngrams
        :param words: bool, whether to find ngrams of words or chars
        :return: List[str], ngrams in text of given length
        """
        #text = self.unicodize(text)
        iter_text = filter(lambda w: not self.is_punct(w), self.tokenize_words(text)) if words else text
        ngrams = dict()

        for i in range(len(iter_text)):
            curr_freq = None

            if length is None:
                curr_len = 2
            else:
                curr_len = length

            loops = 0

            while loops < 100:
                try:
                    w = iter_text[i:i+curr_len]
                except IndexError:
                    break
                else:
                    ngram = " ".join(w) if words else w
                    print(ngram)

                    if ngram not in ngrams:
                        nfreq = text.count(ngram)
                        prev_ngram = " ".join(iter_text[i:i+curr_len-1])

                        if nfreq > 1 and nfreq >= text.count(prev_ngram) * 0.75:  #(length is not None or nfreq > curr_freq):
                            curr_freq = nfreq
                            print("HERE!", ngram, prev_ngram, length)
                            if length is not None:
                                ngrams[ngram] = curr_freq
                            curr_len += 1
                        else:
                            print("THERE!", ngram, prev_ngram, length, curr_freq)
                            if len(prev_ngram) > 1 and curr_freq is not None:
                                ngrams[ngram] = curr_freq
                            break

                if length is not None:
                    break
                else:
                    loops += 1

        return ngrams

    def learn_sentences(self, text):
        """
        Sorts the sentences in text from smallest to largest
        and replaces equivalent entity tokens.

        :param text: str, text with sentences
        :return: None
        """
        sentences = self.tokenize_sentences(self.tokenize_words(text), incl_punct=False)
        sorted_sents = filter(lambda l: len(l) != 0, sorted(sentences, key=lambda s: len(s)))
        token_sentences = dict()

        for i in range(1, len(sorted_sents[-1])+1):
            sents = filter(lambda s: len(s) == i, sorted_sents)
            if len(sents) != 0:
                for sent in sents:
                    print(sent)
                token_sentences[i] = sents

        return token_sentences

    def speak(self, text, start_word=None, length=3):
        """
        Returns a sentence of this length based on words in text.

        :param text: str, text with words
        :param start_word: Optional[str], word(s) starting sentence
        :param length: int, length of desired output sentence
        :return: str, a sentence of desired length
        """
        words = self.tokenize_words(text)
        befores_afters = self.words_before_after(words)

        if start_word is None:
            common_words = sorted(befores_afters, key=lambda b: words.count(b), reverse=True)
            start = common_words[0]
            word = start
            sentence = [word.title()]
        else:
            sentence = start_word.split(" ")
            word = sentence[-1]

        try_idx = 0

        while len(sentence) < length:
            before, after = befores_afters[word]
            try:
                word = after[try_idx]
            except IndexError:
                if try_idx > 5:
                    break
                else:
                    try_idx += 1

                    if start_word is None:
                        word = common_words[try_idx]
                        sentence = [word.title()]
                    else:
                        sentence = start_word.split(" ")
                        word = sentence[-1]
            else:
                sentence.append(word)
                print(sentence)

        return " ".join(sentence) + "."

    def texts_synonyms(self, texts, language=None, lim=1000):
        """
        Returns a dictionary of likely "synonyms" in text, where
        synonyms really means words occuring in the same context.
        (For now, that means that they have the same word(s) in front of
        and after them.)

        :param text: str, text to find synonyms for
        :param language: str, language of text
        :param lim: int, number of common words synonyms can consist of
        :return: dict(str, list), where...
            key (str) - word from text
            val (List[str]) - word(s) from text with same context as key word
        """
        words = self.tokenize_words("\n\n".join(texts))
        print("calculating word synonyms...")
        return self.words_synonyms(words, language=language, lim=lim)

    def word_synonyms(self, word, before_after):
        """
        Returns a list of synonyms for this word from before_after,
        i.e., words sharing this word's before/after words.
        ~
        e.g. word_synonyms("love", {"I": ([], ["love"]), "love": (["I"], ["you"]),
                                        "you": (["love"], []), "hate": (["I"], ["you"])}) ->
             ["hate"]

        :param word: str, word in before_after
        :param before_after: dict(str, tuple(list, list)), where...
            key (str) - word from words
            val (tuple(list, list)) - words coming before and after key word
        :return: List[str], words with same context as word in before_after
        """
        befores, afters = before_after[word]
        best_fits = list()

        if len(befores) != 0 and len(afters) != 0:
            max_in_crossover = 0.15  # >15% match
            max_out_crossover = 0.15
            print("\n\nFINDING SYNONYMS FOR", word.upper())

            for word2 in before_after:
                if word2 != word:
                    befores2, afters2 = before_after[word2]
                    if len(befores2) != 0 and len(afters2) != 0:
                        in_crossover = self.calc_crossover(befores, befores2) * \
                                       min(1, len(befores2) / float(len(befores)))
                        out_crossover = self.calc_crossover(afters, afters2) * \
                                        min(1, len(afters2) / float(len(afters)))

                        if in_crossover > max_in_crossover and out_crossover > max_out_crossover:
                            best_fits = [word2]
                            max_in_crossover = in_crossover
                            max_out_crossover = out_crossover
                        elif in_crossover >= max_in_crossover or out_crossover >= max_out_crossover and \
                                (in_crossover/2.0) + (out_crossover/2.0) >= (max_in_crossover/2.0) + (max_out_crossover/2.0):
                            best_fits.append(word2)
                        else:
                            continue

            print("\t", word.upper(), "is synonymous with:", best_fits)
            print("\t", "with crossover scores:", max_in_crossover, max_out_crossover)
        else:
            print("\t", word.upper(), "is not synonymous with anything")

        return best_fits

    def words_synonyms(self, words, language=None, lim=20000):
        """
        Returns a list of synonyms for this word from before_after,
        i.e., words sharing this word's before/after words.
        ~
        e.g. word_synonyms("love", {"I": ([], ["love"]), "love": (["I"], ["you"]),
                                        "you": (["love"], []), "hate": (["I"], ["you"])}) ->
             ["hate"]

        :param words: List[str], word tokens in order of occurrence in text
        :param lim: int, number of common words synonyms can consist of
        :return: dict(str, tuple(list, list)), where...
            key (str) - word from words
            val (tuple(list, list)) - words coming before and after key word
        """
        before_after = self.words_before_after(words)
        print("BEFORE/AFTER:", before_after)
        return self.before_after_synonyms(before_after, language, lim)

    def before_after_synonyms(self, before_after, language=None, lim=20000):
        """
        Returns a dict with these words as keys and a 2-tuple of
        words occurring (1) before and (2) after this word for vals.
        ~
        Used for figuring out which words come before others.
        ~
        e.g. before_after_synonyms({"Hi": ([], ["I"]), "I": (["Hi"], ["love"]),
                "love": (["I"], ["you"]), "you": (["love"], []), language="English"} ->
             {"Hi": [], "I": [], "love": [], "you": []}
             before_after_synonyms({"hate": (["I", "you"], ["you", "me"]), "I": (["Hi"], ["love"]),
                "love": (["I"], ["you"]), "you": (["love"], []), language="English"} ->
             {"I": ["you"], "love": ["hate"], "hate": ["love"], "you": ["I", "me"]}

        :param before_after: dict(str, tuple(list, list)), where...
            key (str) - word in language
            val (tuple(list, list)) - words coming before and after key word
        :param language: str, language of before_after dict
        :param lim: int, number of common words synonyms can consist of
        :return: dict(str, list), where...
            key (str) - word from a text
            val (List[str]) - word(s) with same context as key word
        """
        synonyms = dict()
        common_words = self.common_words(language=language, lim=lim)
        empty_tup = ([], [])
        before_after = {word: ([i for i in before_after[word][0] if word in before_after.get(i, empty_tup)[1]],
                               [o for o in before_after[word][1] if word in before_after.get(o, empty_tup)[0]])
                        for word in before_after}

        if language is not None:
            iter_lst = common_words[:lim]
        else:
            iter_lst = list(before_after)

        # TODO: find synonyms by going over all words, finding top synonyms 1st then filling in rest
        # TODO: create language of meaning (phenomenological semantics)

        for word in iter_lst:
            if word in before_after:
                print("FINDING SYNONYMS FOR", word.upper())
                best_fits = self.word_synonyms(word, before_after)

                if len(best_fits) != 0:
                    synonyms[word] = best_fits
                    print("\tsynonyms:", best_fits)
                print("\n")

        cross_synonyms = dict()

        for word in synonyms:
            synonym = synonyms[word]
            cross_synonym = [s for s in synonym if word in synonyms.get(s, [])]
            cross_synonyms[word] = cross_synonym

        return cross_synonyms

    def calc_crossover(self, lst1, lst2):
        """
        Returns ratio of crossover between lst1 and lst2 by
        dividing length of their intersection by length of their union.

        :param lst1: Iterable(X), first list to crossover
        :param lst2: Iterable(X), second list to crossover
        :return: float, in range[0,1], ratio of crossover between lst1 and lst2
        """
        # maximize intersection, minimize difference
        return len(set(lst1).intersection(lst2)) / max(1, float(len(set(lst1).union(lst2))))

    def word_clusters(self, text, threshold=1.0):
        """
        Returns a list of words clustered by their common incoming
        and outgoing states.
        ~
        threshold specifies what ratio incoming/outgoing states
        must be shared.
        ~
        Designed to parse pronouns vs verbs vs nouns, etc.  Categorizes
        parts of speech without syntax trees or pre-identified parts of speech.

        :param text: str, text to cluster by words
        :param threshold: float, in range[0,1], ratio of states shared by words
        :return: List[List[str]], words clustered by incoming/outgoing
        """
        tokens = self.tokenize_words(text)
        words = filter(lambda i: not self.is_punct(i), tokens)
        top_words = sorted(set(words), key=lambda t: words.count(t), reverse=True)
        synonyms_dict = dict()

        for i in range(0, len(top_words)/20):
            top_word = top_words[i]
            print("\n\n\n\nTOP WORD #", i+1, ":\t", top_word)
            synonyms = self.label_synonyms(top_word, threshold=threshold)
            if synonyms is not None:
                print(synonyms)
                synonyms_dict.setdefault(top_word, list())
                synonyms_dict[top_word].extend(synonyms)
                for synonym in synonyms:
                    synonyms_dict.setdefault(synonym, list())
                    synonyms_dict[synonym].append(top_word)

        return synonyms_dict

    def word_difference(self, word1, word2, text1, text2, contains1=False, contains2=False):
        """
        Returns a float for the sum of squared differences between locations of
        word1 and word2 in their corresponding texts, text1 and text2.
        ~
        If contains1 or contains2 is True, word1/word2 are the "same" as words
        in text1/text2 if they have the same *starting* characters. Otherwise,
        words in text1/text2 are only the "same" if *exactly* the same.

        e.g. word_difference("Alice", "Alicj", "Alice in Wonderland", "Alicja w Kranie Czarów") ->
                "Alicja" matches with "Alicja"
             word_difference("Alice", "Alicj", "Alice in Wonderland", "Alicja w Kranie Czarów", contains2=True) ->
                "Alicj" matches with "Alicja", "Alicji", ... "Alicj".*

        :param word1: str, first word to compare differences with
        :param word2: str, second word to compare differences with
        :param text1: List[str], text in which word1 appears
        :param text2: List[str], text in which word2 appears
        :param contains1: bool, whether words in text1[:len(word1)] == word1
        :param contains2: bool, whether words in text2[:len(word2)] == word2
        :return: float, sum of squared differences between word1 and word2 in texts
        """
        text1, text2 = self.tokenize_words(text1), self.tokenize_words(text2)
        num_matches = 0

        def match(w1, w2, txt1, txt2, c1, c2):
            sum_squares = 0
            num_matches = 0

            for w1_idx in range(len(txt1)):
                txt1_word = txt1[w1_idx]
                same_words = (txt1_word[:len(w1)] == w1) if c1 else (txt1_word == w1)

                if same_words:
                    ratio = float(w1_idx) / len(txt1)
                    w2_idx = int(len(txt2) * ratio)
                    txt2_word = txt2[w2_idx]

                    addn = 0
                    addn_idx = 0
                    is_neg = False

                    while (txt2_word[:len(w2)] != w2) if c2 else (txt2_word != w2):

                        addn = addn_idx

                        if is_neg:
                            addn *= -1
                        else:
                            addn_idx += 1

                        if (w1_idx + addn) >= 0:
                            try:
                                txt2_word = txt2[w2_idx + addn]
                            except IndexError:
                                break

                        is_neg = not is_neg

                    num_matches += 1
                    w2_idx += addn

                    try:
                        txt2[w2_idx]
                    except IndexError:
                        continue
                    else:
                        #print "\nMatch number", num_matches, "for", w1, "\n\tlanguage 1:", w1_idx, "\n\tlanguage 2:", w2_idx
                        sum_squares += (w1_idx - w2_idx)**2

            return sum_squares  # / num_matches

        match1 = match(word1, word2, text1, text2, contains1, contains2)
        match2 = match(word2, word1, text2, text1, contains2, contains1)
        #print "DIFFERENCES:", match1, match2
        return (match1 + match2) / (max(text1.count(word1), text2.count(word2)) - num_matches)

    def word_translation(self, word1, text1, text2, contains1=False, intervene=False):
        """
        Returns the most likely word from text2 which matches word1 from text1.
        ~
        If contains1 is True, identifies words from text1 with words from text2
        if they have the same starting characters.  Otherwise, requires
        words to be exactly the same.
        ~
        e.g. word_translation("Alice", "", "", contains2=True)

        :param word1: str, first word to compare differences with
        :param text1: List[str], text in which word1 appears
        :param text2: List[str], text in which word2 appears
        :param contains1: bool, whether words in text1[:len(word1)] == word1
        :param intervene: bool, whether to enable user intervention for translations
        :return: str, word in text2 matching word1
        """
        text1, text2 = self.tokenize_words(text1), self.tokenize_words(text2)
        translation = None
        min_match = None
        seen = set()

        for word2 in text2:
            if word2 in seen or len(word2) == 0:
                continue
            else:
                seen.add(word2)

            print("\ncomparing", word1, "to", word2, "...")
            match = self.word_difference(word1, word2, text1, text2, contains1)

            if min_match is None or match < min_match:
                min_match = match
                translation = word2
                print(word2, "is best match so far")
                if min_match == 0:
                    break

        if intervene:
            print(translation, "means", word1)
            ans = input("If this is untrue, enter the true translation. Otherwise, press enter. "
                            "If this word is untranslatable, enter 'u'.")
            if len(ans) != 0:
                if ans == 'u':
                    return ""
                else:
                    return ans

        return translation

    def triangulate_translation(self, word1, text1, text2, translations):
        """
        Uses words from existing translations to triangulate the translation of
        word1 from text1 to text2.
        ~
        Translations is a dictionary of words from text1 leading to words in text2.
        ~
        Better method of comparing texts than by ratio of words covered.
        ~
        This method asks, if word1 is X steps away from a known word in text1, how many
        steps away is a potential translation compared to a known translation in text2?
        ~
        e.g. triangulate_translation("cat", "The cat is on the mat", "Le chat est sur le tapis",
                        {"is": ["est"], "the": ["le"]})

             The cat is on the mat          Le chat est sur le tapis
             XXX     XX    XXX              XX      XXX     XX
              |      |      |_______________|________|______|
              |______|______________________|        |
                     |_______________________________|

             If "cat" appears between "the" and "is", then the word which appears
             (in French) between "le" and "est" ("chat") is its translation.

        :param word1: str, word in text1 to translate to word in text2
        :param text1: List[str], text in which word1 appears
        :param text2: List[str], text to translate word1 to
        :param translations: dict[str, list], of words from text1 to words from text2
        :return: List[str], word1 translated to word from text2
        """
        text1, text2 = self.tokenize_words(text1), self.tokenize_words(text2)
        commonalities = OrderedSet([])
        last_end = 0
        print("\nTriangulating translation for...", word1)

        for i in range(len(text1)):
            word = text1[i]

            if word == word1:
                minus = 1
                plus = 1

                prev_word = text1[i-minus] if i-minus >= 0 else ""
                next_word = text1[i+plus] if i+plus < len(text1) else ""

                while prev_word not in translations and i-minus >= 0:
                    minus += 1
                    prev_word = text1[i-minus] if i-minus >= 0 else ""

                while next_word not in translations and i+plus < len(text1):
                    plus += 1
                    next_word = text1[i+plus] if i+plus < len(text1) else ""

                prev_translations = translations[prev_word] if prev_word != "" else ""
                next_translations = translations[next_word] if next_word != "" else ""

                start_idx = None
                end_idx = None

                for i2 in range(last_end, len(text2)):
                    word2 = text2[i2]
                    if word2 in prev_translations:
                        if start_idx is None:
                            start_idx = i2 + 1
                    elif word2 in next_translations:
                        if start_idx is not None:
                            end_idx = i2
                            last_end = end_idx + 1
                            break

                section = text2[start_idx:end_idx]
                print("section containing translation:", section)
                commonalities.update(section)

        min_ct = text1.count(word1)
        res = commonalities.items(min_ct=min_ct)
        # print "min count:", min_ct
        min_ct -= 1

        while len(res) == 0 and min_ct >= 1:
            res = commonalities.items(min_ct=min_ct)
            min_ct -= 1
            if len(res) == 0:
                break
        else:
            res = commonalities.items()

        print("   result:", res)
        return res

    def words_translations(self, text1, text2):
        """
        Returns a dictionary of translations from text1 to text2.
        ~
        e.g. words_translations("The cat is on the mat", "Le chat est sur le tapis") ->
             {"the": ["le"], "cat": ["chat"], "is": ["est"], "on": ["sur"], "mat": ["tapis"]}

        :param text1: List[str], text to translate from
        :param text2: List[str], text to translate to
        :return: dict, where...
            key (str) - word from text1
            val (List[str]) - matching word(s) from text2
        """
        curr_text1, curr_text2 = self.tokenize_words(text1), self.tokenize_words(text2)
        freqs1 = self.word_freqs(curr_text1)
        freqs2 = self.word_freqs(curr_text2)
        freq_words1 = sorted(freqs1, key=lambda k: freqs1[k], reverse=True)
        freq_words2 = sorted(freqs2, key=lambda k: freqs2[k], reverse=True)
        ranked_translations = dict()

        for word1 in freq_words1:
            ranked_translations.setdefault(word1, dict())
            for word2 in freq_words2:
                word_diff = self.word_difference(word1, word2, curr_text1, curr_text2)
                ranked_translations[word1].setdefault(word_diff, list())
                ranked_translations[word1][word_diff].append(word2)

        #print "ALL TRANSLATIONS:", ranked_translations

        all_translations = {r: [ranked_translations[r][v] for v in ranked_translations[r]]
                            for r in ranked_translations}
        translations = dict()
        words_translated = set()
        min_match = 0
        match_sum = 0

        while len(translations) != len(ranked_translations) and min_match < 1000:
            for word in ranked_translations:
                if word not in translations:
                    matches = ranked_translations[word]
                    if min_match in sorted(matches)[:15]:
                        new_translations = all_translations.copy()
                        new_translations.update(translations)
                        triangulation = self.triangulate_translation(word, text1, text2, new_translations)
                        match = matches[min_match]
                        translation = list()
                        print("\ntriangulation for", word, ":\t", triangulation)
                        print("       lookup for", word, ":\t", match)

                        if len(triangulation) > 5:
                            translation = match
                        else:
                            both_matches = triangulation + match

                            for t in both_matches:
                                if t in triangulation and t in match and t not in translation:
                                    translation.append(t)

                        print("  translation for", word, ":\t", translation)

                        if len(translation) != 0:
                            translations.setdefault(word, list())
                            translations[word] += translation
                            match_sum += min_match
                            words_translated.update(translation)
            min_match += 1

        print("\nFINAL TRANSLATION:", translations)
        print("\nMATCH SUM:", match_sum)
        print()
        return translations

    def word_freqs(self, words):
        """
        Returns a dictionary of each word in this list of words and
        its frequency in words.
        ~
        e.g. word_freqs(["I", "want", "you", "I", "need", "you"]) ->
             {"I": 2, "want": 1, "you": 2, "need": 1}

        :param words: List[str], list of words (e.g. from a text)
        :return: dict(), where...
            key (str) - word from words
            val (int) - number of occurrences of word in words
        """
        freqs = dict()
        for word in words:
            freqs.setdefault(word, int())
            freqs[word] += 1
        return freqs

    def translation_dict(self, text):
        """
        Returns an empty dictionary for this text so that
        its translations in other languages can be added.

        :param text: str, string of text (sentences) in a language
        :return: dict, where...
            key (str) - word in this text
            val (dict) - empty dict for translations in other languages
        """
        words = self.remove_punct(text).split(" ")
        return {word: dict() for word in words}

    def text_breakpoints(self, text):
        breakpoints = re.split(pattern="[!?]", string=text)
        return [b.strip() for b in breakpoints if len(b) != 0]


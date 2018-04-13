# coding: utf-8
"""
LANGUAGE_PARSER:

    Contains LanguageParser class for parsing data in
    a particular language from Wiktionary.
"""
from wiktionary_parser import *
from nltk.tokenize import WordPunctTokenizer, PunktSentenceTokenizer


class LanguageParser(WiktionaryParser):
    ALPHABETS = {}
    LEXICA = {}

    def __init__(self, language):
        WiktionaryParser.__init__(self)
        self.language = language
        self.url = self.url % self.language
        # --> alphabets
        self.alphabets = self.load_alphabets()
        self.alphabet = self.find_alphabet(self.language)
        # --> tokenizers
        self.word_tokenizer = None
        self.sent_tokenizer = None

    def reset_language(self, language):
        """
        Sets this LanguageParser's language to the given language.

        :param language: str, language to change to
        :return: None
        """
        if self.language != language:
            self.refresh_data()
            self.__init__(language)

    # LEXICA
    # ------
    def in_lexicon(self, word, language=None):
        """
        Returns True if this word is in this language's lexicon
        or if this language's lexicon is empty (undetermined),
        False otherwise.

        :param word: str, word to check if in lexicon
        :param language: str, language of lexicon
        :return: bool, True if word in lexicon or empty lexicon
        """
        lexicon = self.find_lexicon(language)
        return word in lexicon or len(lexicon) == 0

    def parse_lexicon(self, language):
        """
        Parses plaintext lexicon in given language.
        Returns a dict with all words in lexicon
        as keys and corresponding lemma forms as values.
        ~
        Each new lexical entry should be separated by "\n",
        while inflected forms should be separated by ",".
        ~
        Assumes first word on every line is the lemma form
        of all subsequent words on the same line.
        ~
        N.B. The same lemma value will often belong to multiple keys.

        e.g. "kota, kocie, kot" -> {"kota":"kota", "kocie":"kota", "kot":"kota"}

        :param language: str, language of .txt file for lexicon
        :return: dict, where...
            key (str) - inflected form of a word
            val (str) - lemma form of inflected word
        """
        return self.all_inflections(language)

    def parse_custom_lexicon(self, language):
        """
        Parses a custom lexicon for this language, if one exists.
        ~
        Currently only supports French and Polish.

        :param language: str, language to parse lexicon for
        :return: dict, where...
            key (str) - word lemma
            val (List[str]) - all lexical forms of word lemma
        """
        if language == "Polish":
            fn = self.parse_polish_lexicon
        elif language == "French":
            fn = self.parse_french_lexicon
        else:
            return

        filename = "/resources/lexica/" + language + ".txt"

        with open(self.PATH + filename, "rb") as lex:
            lexicon = fn(lex)

        return lexicon

    def parse_french_lexicon(self, lex):
        """
        Parses plaintext file for French lexicon with
        given filename.  Returns a dict with all lexemes
        in French lexicon as keys and corresponding
        lemma forms as values.
        ~
        Each new lexical entry should be separated by "\n",
        while inflected forms should be separated by ",".
        ~
        Assumes second word on every line is the lemma form
        of previous words on the same line.
        ~
        N.B. The same lemma value will often belong to
        multiple lexemes.

        e.g. "grande, grand" -> {"grand": ["grand", "grande"]}

        :param lex: List[str], entries in French lexicon
        :return: dict, where...
            key (str) - word lemma
            val (List[str]) - all lexical forms of word lemma
        """
        lexicon = dict()

        for line in lex:
            line = line.strip("\n")
            line = self.unicodize(line)
            if line[-1] == "=":
                lemma = line[:-2]
                lexicon.setdefault(lemma, list())
                lexicon[lemma].append(lemma)
            else:
                entry = line.split("\t")
                lemma = entry[1]
                lexeme = entry[0]
                lexicon.setdefault(lexeme, list())
                lexicon[lexeme].append(lemma)

        return lexicon

    def parse_polish_lexicon(self, lex):
        """
        Parses plaintext file for Polish lexicon with
        given filename.  Returns a dict with all lexemes
        in Polish lexicon as keys and corresponding
        lemma forms as values.
        ~
        Inflected forms in each lexical entry should be
        separated by ",".
        ~
        Assumes first word on every line is the lemma form
        of following words on the same line.
        ~
        N.B. The same lemma value will often belong to
        multiple lexemes.

        e.g. "kot, kota, kocie" -> {"kot": ["kot", "kota", "kocie"]}

        :param lex: List[str], entries in Polish lexicon
        :return: dict, where...
            key (str) - word lemma
            val (List[str]) - all lexical forms of word lemma
        """
        lexicon = dict()

        for line in lex:
            line = line.strip("\n")
            line = line.strip("\r")
            line = self.unicodize(line)
            lexemes = line.split(",")
            lexemes = [l.strip() for l in lexemes]
            lemma = lexemes[0]
            lexicon[lemma] = lexemes

        return lexicon

    # ALPHABET
    # --------
    def init_alphabet(self, language=None):
        """
        Returns a sorted list of all alphabet letters in this language.

        :param language: str, language of alphabet to retrieve
        :return: List[str], alphabet letters in this language
        """
        language = self.verify_language(language)
        page = self.url_page(self.lemma_url(language))
        return self.page_alphabet(page)

    def page_alphabet(self, page):
        """
        Returns a sorted list of all alphabet letters on this page's
        alphabet table.

        :param page: (BeautifulSoup) Tag, page with alphabet table
        :return: List[str], alphabet letters in this language
        """
        alphabet = set()
        table = page.find("table", attrs={"id": "toc"})
        cells = self.alphabet_cells(table)

        letters = []
        for cell in cells:
            cell_text = cell.getText()
            if cell_text != "Top":
                letters.extend(self.unicodize(cell_text).split(" "))

        for letter in letters:
            if self.valid_letter(letter):
                alphabet.add(letter)
                alphabet.add(letter.lower())
                alphabet.add(letter.upper())

        return sorted(alphabet)

    def find_alphabet(self, language=None):
        """
        Returns the alphabet for the given language.
        ~
        If no alphabet for this language exists, creates new
        alphabet for language, adds to ALPHABETS, and returns the result.

        :param language: str, language of alphabet
        :return: List[str], all letters in given language's alphabet
        """
        language = self.verify_language(language)
        alphabet = self.load_alphabet(language)

        if len(alphabet) == 0:
            alphabet = self.init_alphabet(language)
            self.alphabets[language] = alphabet

        self.refresh_alphabets()
        return sorted(alphabet)

    def valid_letter(self, letter):
        """
        Returns True if this alphabet letter has at least 1 character
        and no parentheses (which indicate a non-native letter).
        Otherwise, returns False.

        :param letter: str, alphabet letter to check whether valid
        :return: bool, True if letter is valid, False otherwise
        """
        return len(letter) != 0 and "(" not in letter

    def alphabet_cells(self, alphabet_table):
        """
        Returns this alphabet table's letter cells.

        :param page: (BeautifulSoup) Tag, page with alphabet table
        :return: List[str], alphabet letters in this language
        """
        cells = []
        rows = alphabet_table.findAll("tr")
        if len(rows) > 1:
            rows = rows[1:]
        for row in rows:
            cells.extend(row.findAll("td")[-1].findAll("a"))
        return cells

    def word_in_alphabet(self, word, language=None):
        """
        Returns True if this word contains only characters from
        this language's alphabet, False otherwise.

        :param word: str, word to verify whether in language alphabet
        :param language: str, language of alphabet
        :return: bool, whether word contains only characters from language
        """
        language = self.verify_language(language)
        word_chars = set(word)
        alphabet = self.find_alphabet(language)
        return len(word_chars.difference(alphabet)) == 0

    # TOKENIZERS
    # ----------
    def init_tokenizers(self):
        """
        Initializes this LanguageParser's tokenizers if they
        are None.

        :return: None
        """
        self.init_word_tokenizer()
        self.init_sent_tokenizer()

    def init_word_tokenizer(self):
        """
        Initializes this LanguageParser's word_tokenizer if it
        is None.

        :return: None
        """
        if self.word_tokenizer is None:
            self.word_tokenizer = WordPunctTokenizer()

    def init_sent_tokenizer(self):
        """
        Initializes this LanguageParser's sent_tokenizer if it
        is None.

        :return: None
        """
        if self.sent_tokenizer is None:
            self.sent_tokenizer = PunktSentenceTokenizer()

    def tokenize_words(self, words):
        """
        Returns a list of words in this str words.

        :param words: str, string to tokenize by word
        :return: List[str], phrase tokenized by word
        """
        self.init_word_tokenizer()
        words = self.unicodize(words)
        words = self.word_tokenizer.tokenize(words)
        return words

    def tokenize_sents(self, sents):
        """
        Returns a list of the sentences in this str sents.

        :param sents: str, string to tokenize by sentence
        :return: List[str], phrase tokenized by sentence
        """
        self.init_sent_tokenizer()
        sents = self.unicodize(sents)
        sentences = self.sent_tokenizer.tokenize(sents)
        return sentences

    def tokenize_words_sents(self, phrase):
        """
        Returns a list of the words in the sentences in the given str phrase.

        :param phrase: str, string to tokenize by sentence and word
        :return: List[str], phrase tokenized by sentence and word
        """
        self.init_tokenizers()
        phrases = self.unicodize(phrase)
        sentences = self.tokenize_sents(phrases)
        phrases_tokens = [self.tokenize_words(sentence) for sentence in sentences]
        return phrases_tokens

    # JSON
    # ----
    def load_alphabets(self):
        """
        Returns a memoized dictionary of alphabets in every language.

        :return: dict(str, list), where str is language and list is alphabet
        """
        return self.load_json("alphabets")

    def load_alphabet(self, language=None):
        """
        Returns the memoized alphabet for this language.

        :return: dict(str, list), where str is language and list is alphabet
        """
        language = self.verify_language(language)
        return self.alphabets.setdefault(language, list())

    def refresh_data(self):
        """
        Dumps this LanguageParser's data from...
            alphabets to alphabets.json, and
            wiktionary_entries to wiktionary_entries.json.

        :return: None
        """
        self.refresh_alphabets()
        self.refresh_wiktionary_entries()

    def refresh_dict(self, dict_name):
        """
        Refreshes the LanguageParser's language dictionary with dict_name.
        ~
        Dict_name should be one of:
            alphabets, or
            wiktionary_entries.

        :param dict_name: str, name of language dictionary to refresh
        :return: None
        """
        dict_obj = getattr(self, dict_name, None)

        if dict_obj is not None:
            entry = getattr(self, dict_name[:-1], None)
            if entry is not None:
                dict_obj[self.language] = sorted(entry)
            self.dump_json(dict_obj, dict_name)

    def refresh_alphabets(self):
        """
        Dumps this LanguageParser's alphabets data to alphabets.json.

        :return: None
        """
        self.refresh_dict("alphabets")

    # LEMMAS
    # ------
    def lemmatize(self, word, language=None, pos=None):
        """
        Returns the lemma for this word in this language.
        ~
        If word has no lemma, this method returns the given word.
        ~
        e.g. lemmatize("drove", "English", "Verb") -> "drive"
             lemmatize("yeux", "French", "Noun") -> "œil"

        :param word: str, word to find lemma for
        :param language: str, language of given word
        :param poses: Set[str], parts-of-speech for output lemma
        :return: str, lemma for given word
        """
        word = self.entry_word(word, language)
        lemmas = self.word_lemmas(word, language, pos)
        if len(lemmas) != 0:
            return lemmas[0]
        else:
            return word

    def word_lemmas(self, word, language=None, poses=None):
        """
        Returns the lemmas for this word in this language.
        ~
        e.g. word_lemmas("driven", "English") -> ["drive", "driven"]

        :param word: str, word to find lemmas for
        :param language: str, language of given word
        :param poses: Set[str], parts-of-speech for output lemmas
        :return: List[str], lemmas for given word
        """
        lemmas = OrderedSet([])

        if len(word) == 0:
            return lemmas.items()
        if poses is None:
            poses = self.PARTS_OF_SPEECH

        language = self.verify_language(language)
        word = self.unicodize(word)
        inflections = self.find_word_inflections(word, language)

        if inflections is not None:
            lemmas.add(word)
        else:
            stemwords = self.find_stemwords(word, language, poses)
            stemwords = self.filter_language_words(stemwords, language)
            lemmas.update(stemwords)

            if len(lemmas) == 0:
                headwords = self.find_headwords(word, language, poses)
                headwords = self.filter_language_words(headwords, language)
                lemmas.update(headwords)

        return lemmas.items()

    def is_word_in_language(self, word, language=None):
        """
        Returns True if this word is in this language,
        False otherwise.
        ~
        e.g. is_word_in_language("balloon", "English") -> True
             is_word_in_language("ballon", "English") -> False
             is_word_in_language("ballon", "French") -> True

        :param word: str, word to check whether in language
        :param language: str, language to check
        :return: bool, whether word is in language
        """
        language = self.verify_language(language)
        word_page = self.word_page(word)

        if word_page is None:
            lang_lexicon = self.find_lexicon(language)
            return word in lang_lexicon
        else:
            return self.valid_page(word_page, language)

    def filter_language_words(self, words, language=None):
        """
        Returns this list of words filtered to only include
        words in this language's lexicon.
        ~
        e.g. filter_language_words(["balloon", "ballon"], "English") -> ["balloon"]
             filter_language_words(["balloon", "ballon"], "French") -> ["ballon"]

        :param words: List[str], list of words to filter by language
        :param language: str, desired language of output words
        :return: List[str], words only in this language
        """
        return [word for word in words if self.is_word_in_language(word, language)]

    def uninflect(self, word, language=None):
        """
        Returns the uninflected form of this word in this language.

        :param word: str, word to uninflect
        :param language: str, language of word
        :return: str, word uninflected
        """
        language = self.verify_language(language)
        for word_entry in self.wiktionary_entries:
            inflections = self.lookup_word_inflections(word_entry, language)
            if inflections is not None:
                for inflection in inflections:
                    if inflection == word:
                        return word_entry
        else:
            return self.lemmatize(word, language=language)

    # IPAS
    # ----
    def word_ipa(self, word, language=None):
        """
        Transcribes the given word to IPA.  Returns this word's
        IPA pronunciation and adds its transcription to the given
        language's IPA dictionary.

        :param word: str, word to transcribe to IPA
        :param language: str, word's language
        :return: unicode, IPA transcription of word
        """
        ipas = self.word_ipas(word, language)
        if len(ipas) != 0:
            return ipas[0]
        else:
            return

    def word_ipas(self, word, language=None):
        """
        Transcribes the given word to IPAs.

        :param word: str, word to transcribe to IPA
        :param language: str, word's language
        :return: List[unicode], IPA transcriptions of word
        """
        language = self.verify_language(language)
        entry = self.find_wiktionary_subentry(word, language, u"Pronunciation")
        if len(entry) == 0:
            ipa = self.etymology_ipa(word, language)
            if ipa is not None:
                entry.insert(0, ipa)
                self.edit_wiktionary_entry(word, language, u"Pronunciation", entry)
        return entry

    def words_ipa(self, words):
        """
        Transcribes the given words to IPA.

        :param word: List[str], words to transcribe to IPA
        :return: List[unicode], IPA transcriptions of words
        """
        ipas = list()

        for word in words:
            ipa = self.word_ipa(word)
            if ipa is not None:
                ipas.append(ipa)

        return ipas

    def find_headwords(self, word, language=None, poses=None):
        """
        Returns this word's head word from its Wiktionary entry
        in this language for each part of speech in poses.
        ~
        N.B. A "head word" is the first item in the first sublist
        under a word's part-of-speech heading:

            e.g. "Noun": [["miles", None], ["plural of mile", "mile"]]
                            ^^^^^
                          head word

        Part-of-speech entries contain only 1 head word but may
        contain >=1 stem words.

        :param word: str, word of Wiktionary entry to lookup
        :param language: Optional[str], language of entry to lookup
        :param poses: Optional[List], parts of speech to lookup
        :return: List[str], given word's head words for this language
        """
        pos_entries = self.find_pos_entries(word, language, poses)
        headwords = list()

        for pos in pos_entries:
            pos_entry = pos_entries[pos]
            try:
                headword = pos_entry[0][0]
            except IndexError:
                continue
            else:
                if headword is not None and headword in self.find_lexicon(language):
                    headwords.append(headword)

        return headwords

    def find_stemwords(self, word, language=None, poses=None):
        """
        Returns this word's stem words from its Wiktionary entry
        in this language.
        ~
        N.B. A "stem word" is the second item in all but the first sublist
        under a word's part-of-speech heading:

            e.g. "Noun": [["miles", None], ["plural of mile", "mile"]]
                                                               ^^^^
                                                             stem word

        Entries may contain >=1 stem words but will only contain 1 head word.

        :param word: str, word of Wiktionary entry to lookup
        :param language: Optional[str], language of entry to lookup
        :param poses: Optional[List], parts of speech to lookup
        :return: List[str], given word's stem words for this language
        """
        pos_entries = self.find_pos_entries(word, language, poses)
        stemwords = list()

        for pos in pos_entries:
            pos_entry = pos_entries[pos]
            try:
                stems = [entry[1] for entry in pos_entry[1:]
                         if entry[1] is not None]
            except IndexError:
                continue
            else:
                stemwords += stems

        return OrderedSet(stemwords).rank_items()

    def find_english_translation(self, word, language=None):
        """
        Returns this word's translation from this language to English,
        according to Wiktionary.

        :param word: str, word to translate
        :param language: str, language of word
        :return: str, word's translation in English
        """
        language = self.verify_language(language)
        word = self.unicodize(word)

        if language != "English":
            print "IN FINDING ENGLISH TRANSLATION"
            translations = set()
            pos_entries = self.find_pos_entries(word, language)
            eng_entries = set()

            print "\t", pos_entries
            for pos in pos_entries:
                entry = pos_entries[pos]
                eng_entry = entry[1:]
                eng_entries.update([e[0] for e in eng_entry])

            for translation in translations:
                translation = translation.replace(u"to", u"").strip()
                if self.word_in_wiktionary(translation, "English"):
                    return self.clean_parentheticals(translation)
        else:
            return word

    def find_english_translations(self, word, language=None, pos=None):
        """
        Returns this word's translations from this language to English,
        according to Wiktionary.

        :param word: str, word to translate
        :param language: str, language of word
        :return: Set(str), word's translations in English
        """
        language = self.verify_language(language)
        word = self.unicodize(word)
        eng_translations = set()

        if language != "English":
            translations = set()
            print "finding pos entries for", word
            pos_entries = self.find_pos_entries(word, language, poses={pos})
            if len(pos_entries) == 0:
                pos_entries = self.find_pos_entries(word, language)
            print "found pos entries for", word

            print "\t", pos_entries
            for pos_entry in pos_entries:
                entry = pos_entries[pos_entry]
                eng_entry = entry[1:]
                translations.update([e[1] for e in eng_entry if e[1] is not None and e[1] != word])

            print "\t", translations

            for translation in translations:
                translation = self.clean_parentheticals(translation.strip())
                if self.word_in_wiktionary(translation, "English"):
                    print "\t", translation, "is an English word"
                    eng_translations.add(translation)

            print
        return eng_translations

    def find_word_ipas(self, word, language=None):
        """
        Transcribes the given word to IPAs.

        :param word: str, word to transcribe to IPA
        :param language: str, word's language
        :return: List[unicode], IPA transcriptions of word
        """
        language = self.verify_language(language)
        try:
            return self.wiktionary_entries[word][language][u"Pronunciation"]
        except KeyError:
            return list()

    def etymology_ipa(self, word, language=None):
        """
        Returns this word's IPA constructed from its etymology.

        :param word: str, word to return etymology's IPA of
        :param language: str, language of word
        :return: (unicode) str, this word's etymology's IPA
        """
        language = self.verify_language(language)
        etyms = self.find_word_etymology(word, language)
        ipas = []
        if etyms is not None and len(etyms) != 0:
            for etym in etyms:
                etym_ipa = self.word_ipa(etym)
                if etym_ipa is None:
                    return
                else:
                    ipas += etym_ipa
        return "".join(ipas)

    # PARTS-OF-SPEECH
    # ---------------
    def word_pos(self, word, language=None):
        """
        Returns the given word's part of speech.

        :param word: str, word to get part of speech of
        :param language: str, word's language
        :return: str, word's part of speech
        """
        poses = self.word_poses(word, language)
        if len(poses) != 0:
            return poses[0]

    def word_poses(self, word, language=None):
        """
        Returns the given word's parts of speech.

        :param word: str, word to get parts of speech of
        :param language: str, word's language
        :return: List[str], word's parts of speech
        """
        language = self.verify_language(language)
        word_entry = self.find_wiktionary_entry(word, language)

        if word_entry is not None:
            poses = [sect for sect in word_entry
                     if sect in self.PARTS_OF_SPEECH]
            pos_set = OrderedSet(poses)
            return pos_set.items()
        else:
            return list()

    def words_pos(self, words, language=None):
        """
        Returns a list of the given words' parts of speech.

        :param word: List[str], words to get parts of speech of
        :param language: str, words' language
        :return: List[str], words' parts of speech
        """
        pos = list()
        for word in words:
            pos.append(self.word_pos(word, language))
        return pos

    def words_poses(self, words, language=None):
        """
        Returns a list of the given words' parts of speech.

        :param word: List[str], words to get parts of speech of
        :param language: str, words' language
        :return: List[Set(str)], words' parts of speech
        """
        poses = list()
        for word in words:
            poses.append(self.word_poses(word, language))
        return poses

    # MORPHEMES
    # ---------
    def word_morphemes(self, word, language=None):
        """
        Returns a set of morphemes in this word.

        :param word: str, word to find morphemes of
        :param language: str, language of morpehemes
        :return: List[str], word's morphemes
        """
        word = self.entry_word(word, language)
        return self.lookup_word_etymology(word, language)

    def recursive_all_word_morphemes(self, word, language=None):
        """
        Returns a set of morphemes in this word, including the
        morphemes for all its sub-morphemes.
        ~
        e.g. all_word_morphemes("undeniable", "English") -> ["un-", "deny", "-able"]

        :param word: str, word to find morphemes of
        :param language: str, language of morpehemes
        :return: List[str], word's morphemes
        """
        language = self.verify_language(language)
        word_morphemes = self.word_morphemes(word, language)
        if word_morphemes is not None:
            submorphemes = OrderedSet(word_morphemes)
            for morpheme in word_morphemes:
                print morpheme
                submorphemes.update(self.recursive_all_word_morphemes(morpheme))
        else:
            submorphemes = OrderedSet([])
        return submorphemes

    def all_word_morphemes(self, word, language=None):
        """
        Returns a set of morphemes in this word, including the
        morphemes for all its sub-morphemes.
        ~
        e.g. all_word_morphemes("undeniable", "English") -> ["un-", "deny", "-able"]

        :param word: str, word to find morphemes of
        :param language: str, language of morpehemes
        :return: List[str], word's morphemes
        """
        language = self.verify_language(language)
        morphemes = OrderedSet([])
        todo = {word}

        while len(todo) != 0:
            curr_word = todo.pop()
            if len(curr_word) != 0 and curr_word not in morphemes.items_set and not self.contains_punct(curr_word):
                morphemes.add(curr_word)
                word_morphemes = self.word_morphemes(curr_word, language)
                if word_morphemes is not None:
                    morphemes.update(word_morphemes)
                    todo.update(word_morphemes)

        return morphemes.order_items()

    def words_morphemes(self, words, language=None):
        """
        Returns a list of morphemes in these words.

        :param word: str, word to find morphemes of
        :param language: str, language of morpehemes
        :return: List[str], words' morphemes
        """
        language = self.verify_language(language)
        morphemes = list()
        for word in words:
            word_morphemes = self.all_word_morphemes(word, language)
            morphemes += word_morphemes
        return morphemes

    def sentences_morphemes(self, sentences, language=None):
        """
        Returns a list of morphemes in these sentences.

        :param sentences: str, sentences to find morphemes of
        :param language: str, language of sentences
        :return: List[str], sentences's morphemes
        """
        language = self.verify_language(language)
        sents_tokens = self.tokenize_words(self.unicodize(sentences))
        return self.words_morphemes(sents_tokens, language)

    # LOOKUPS & FINDS
    # ---------------
    # Use lookup to "look up" existing entries,
    # use find to "find" new entries if none exist.
    # ---------------
    def lookup_word_inflections(self, word, language):
        """
        Returns all inflected forms of this word in wiktionary_entries.

        :param word: str, word to get inflections of
        :return: List[str], all inflected forms of word
        """
        try:
            return self.wiktionary_entries[word][language][u"Inflections"]
        except KeyError:
            return

    def find_word_inflections(self, word, language):
        """
        Returns all inflected forms of this word from Wiktionary.

        :param word: str, word for inflections to get inflections of
        :return: List[str], all inflected forms of word
        """
        return self.find_wiktionary_subentry(word, language, u"Inflections")

    def lookup_word_etymology(self, word, language=None):
        """
        Returns the etymology of the given word in this
        language (according to Wiktionary).

        :param word: str, word to find etymology of
        :param language: str, language of etymology
        :return: List[str], etymological roots of this word
        """
        language = self.verify_language(language)
        return self.lookup_wiktionary_subentry(word, language, u"Etymology")

    def find_word_etymology(self, word, language=None):
        """
        Returns the etymology of this word from Wiktionary.

        :param word: str, word to lookup etymology of
        :param language: str, language of etymology
        :return: List[str], etymological roots of this word
        """
        language = self.verify_language(language)
        return self.find_wiktionary_subentry(word, language, u"Etymology")

    # ALL ENTRIES
    # -----------
    def all_inflections(self, language=None):
        """
        Returns a dictionary of all words in this language's inflections.

        :param language: str, language of inflections dicts
        :return: dict(str, Set(str)), inflection-lemma pairs in this language
        """
        language = self.verify_language(language)
        all_inflections = dict()

        for word in self.wiktionary_entries:
            inflections = self.lookup_word_inflections(word, language)
            if inflections is not None:
                for inflection in inflections:
                    all_inflections.setdefault(inflection, set())
                    all_inflections[inflection].add(word)

        return all_inflections

    def all_morphemes(self, language=None):
        """
        Returns all words in this language's inflections.

        :param language: str, language of inflection dict
        :return: List[str], all morphemes in this language
        """
        language = self.verify_language(language)
        morphemes = list()

        for word in self.wiktionary_entries:
            etyms = self.word_morphemes(word, language)
            if etyms is not None:
                morphemes += etyms

        return morphemes

    def all_ipas(self, language=None):
        """
        Returns all IPAs in this language's pronunciations.

        :param language: str, language of pronunciations
        :return: dict(str, str), inflection-lemma pairs in this language
        """
        language = self.verify_language(language)
        ipas = dict()

        for word in self.wiktionary_entries:
            word_ipas = self.find_word_ipas(word, language)
            if word_ipas is not None:
                ipas.setdefault(word, list())
                ipas[word] = OrderedSet(ipas[word] + word_ipas).items()

        return ipas

    # WORDNET
    # -------
    def get_wordnet_words(self):
        """
        Returns a set of all words in Wordnet.

        :return: Set(str), Wordnet word
        """
        if self.language == "English":
            entries = set()
            path = self.PATH + "/resources/wordnet/wn_s.txt"

            with open(path, "r") as synsets:
                for synset in synsets:
                    synset = synset[2:-3]
                    info = synset.split(",")
                    name = info[2]
                    name = name[1:-1]
                    if " " not in name:
                        entries.add(name)

            return entries
        else:
            lexicon = self.parse_lexicon(self.language)
            return set(lexicon.keys())

    def get_wordnet_word_pairs(self):
        """
        Returns a list of 2-tuples consisting of a Wordnet word and
        its corresponding parts of speech.

        :return: Set(tuple(str,str)), Wordnet word and pos
        """
        path = self.PATH + "/resources/wordnet/wn_s.txt"
        entries = set()

        with open(path, "r") as synsets:
            for synset in synsets:
                synset = synset[2:-3]
                info = synset.split(",")
                name = info[2]
                name = name[1:-1]
                pos = info[3]
                if " " not in name:
                    pair = (self.unicodize(name), self.unicodize(pos))
                    entries.add(pair)

        return entries

    # COMMON WORDS
    # ------------
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
        path = self.PATH + "/resources/frequency_words/content/2016/%s/%s_50k.txt" % (lang_code, lang_code)

        with open(path, 'r') as fifty_k:
            line_no = 0
            for line in fifty_k:
                word = line.split(" ", 1)[0]
                word = self.unicodize(word)
                words.append(word)
                if line_no > lim:
                    break
                line_no += 1

        return words

    def common_word_pairs(self, language=None, lim=50000):
        """
        Returns the most common word-pos pairs in this language
        up to lim.

        :param lim: int, number of common words to return
        :param language: Optional[str], language of common words
        :return: List[tuple(str, str)], Wordnet word and pos
        """
        language = self.verify_language(language)
        common_words = self.common_words(language, lim)

        if language == "English":
            word_pairs = self.get_wordnet_word_pairs()
            return [word_pair for word_pair in word_pairs if word_pair[0] in common_words]
        else:
            poses = self.words_poses(common_words)
            word_pairs = list()

            for i in range(len(common_words)):
                word = common_words[i]
                pos = poses[i]
                if len(pos) == 0:
                    pos.append(None)
                for p in pos:
                    pair = (self.unicodize(word), self.unicodize(p))
                    word_pairs.append(pair)

            return word_pairs

    def common_morphemes(self, language=None, lim=50000):
        """
        Returns the most common words in this language up to lim,
        including their constituent words.

        :param lim: int, lim <= 50000, number of words to retrieve
        :param language: Optional[str], language of common morpemes
        :return: List[str], up to 50k most common words in LanguageParser's language
        """
        language = self.verify_language(language)
        lexicon = self.find_lexicon(language, lim)
        common_words = lexicon[:lim]
        morphemes = self.words_morphemes(common_words, language)
        return morphemes

    def add_common_wiktionary_entries(self, language=None, lim=50000):
        """
        Adds Wiktionary entries for the most common words in
        this language to this WiktionaryParser's wiktionary_entries.

        :param words: List[str], words of Wiktionary entries to add
        :param language: Optional[str], language of entries to add
        :return: dict(str, dict), where str is language and dict is...
            key (str) - title of subentry heading (e.g. Etymology)
            val (list) - value(s) associated with subentry
        """
        language = self.verify_language(language)
        return self.add_wiktionary_entries(self.common_words(language, lim), language)

    # URLS
    # ----
    def lemma_url(self, language=None):
        """
        Returns the Wiktionary URL for lemmas in this language.

        :param language: str, language of URL
        :return: str, Wiktionary URL for this parser's lemmas
        """
        language = self.verify_language(language)
        return (self.WIKI_URL + self.END_URL + self.LEMMA_PATH) % language

    def ipa_url(self, language=None):
        """
        Returns the Wiktionary URL for IPAs in this language.

        :param language: str, language of IPA URL
        :return: str, Wiktionary URL for this parser's IPAs
        """
        language = self.verify_language(language)
        return (self.WIKI_URL + self.END_URL + self.IPA_PATH) % (language, language)
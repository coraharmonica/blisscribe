# coding: utf-8
"""
LANGUAGE_PARSER:

    Contains LanguageParser class for parsing data in
    a particular language from Wiktionary.
"""
import os, sys
sys.path.append(os.path.realpath(__file__))
try:
    import tokenizers as tokenizers
except ImportError:
    from . import tokenizers as tokenizers
from .wiktionary_parser import *


class LanguageParser(WiktionaryParser):
    ALPHABETS = {}
    LEXICA = {}

    def __init__(self, lang):
        WiktionaryParser.__init__(self)
        self.language = lang
        # --> alphabets
        self.alphabets = self.load_alphabets()
        self.alphabet = self.find_alphabet(self.language)

    def reset_language(self, lang):
        """
        Sets this LanguageParser's language to the given language.

        :param lang: str, language to change to
        :return: None
        """
        if self.language != lang:
            self.refresh_data()
            self.__init__(lang)

    # LEXICA
    # ------
    def in_lexicon(self, word, lang=None):
        """
        Returns True if this word is in this language's lexicon
        or if this language's lexicon is empty (undetermined),
        False otherwise.

        :param word: str, word to check if in lexicon
        :param lang: str, language of lexicon
        :return: bool, True if word in lexicon or empty lexicon
        """
        lexicon = self.find_lexicon(lang)
        return word in lexicon or len(lexicon) == 0

    def parse_lexicon(self, lang):
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

        :param lang: str, language of .txt file for lexicon
        :return: dict, where...
            key (str) - inflected form of a word
            val (str) - lemma form of inflected word
        """
        return self.all_inflections(lang)

    def parse_custom_lexicon(self, lang):
        """
        Parses a custom lexicon for this language, if one exists.
        ~
        Currently only supports French and Polish.

        :param lang: str, language to parse lexicon for
        :return: dict, where...
            key (str) - word lemma
            val (List[str]) - all lexical forms of word lemma
        """
        if lang == "Polish":
            fn = self.parse_polish_lexicon
        elif lang == "French":
            fn = self.parse_french_lexicon
        else:
            return

        filename = "/resources/lexica/" + lang + ".txt"

        with open(PATH + filename, "rb") as lex:
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

        :param lex: List[str], entry in French lexicon
        :return: dict, where...
            key (str) - word lemma
            val (List[str]) - all lexical forms of word lemma
        """
        lexicon = {}

        for line in lex:
            line = str(line).strip("\n")
            if line[-1] == "=":
                lemma = line[:-2]
                lexicon.setdefault(lemma, [])
                lexicon[lemma].append(lemma)
            else:
                entry = line.split("\t")
                lemma = entry[1]
                lexeme = entry[0]
                lexicon.setdefault(lexeme, [])
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

        :param lex: List[str], entry in Polish lexicon
        :return: dict, where...
            key (str) - word lemma
            val (List[str]) - all lexical forms of word lemma
        """
        lexicon = {}

        for line in lex:
            line = str(line).strip("\n")
            line = line.strip("\r")
            lexemes = line.split(",")
            lexemes = [l.strip() for l in lexemes]
            lemma = lexemes[0]
            lexicon[lemma] = lexemes

        return lexicon

    # ALPHABET
    # --------
    def init_alphabet(self, lang=None):
        """
        Returns a sorted list of all alphabet letters in this language.

        :param lang: str, language of alphabet to retrieve
        :return: List[str], alphabet letters in this language
        """
        lang = self.verify_language(lang)
        page = self.url_page(self.lemma_url(lang))
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
                letters.extend(str(cell_text).split(" "))

        for letter in letters:
            if self.valid_letter(letter):
                alphabet.add(letter)
                alphabet.add(letter.lower())
                alphabet.add(letter.upper())

        return sorted(alphabet)

    def find_alphabet(self, lang=None):
        """
        Returns the alphabet for the given language.
        ~
        If no alphabet for this language exists, creates new
        alphabet for language, adds to ALPHABETS, and returns the result.

        :param lang: str, language of alphabet
        :return: List[str], all letters in given language's alphabet
        """
        lang = self.verify_language(lang)
        alphabet = self.load_alphabet(lang)

        if len(alphabet) == 0:
            alphabet = self.init_alphabet(lang)
            self.alphabets[lang] = alphabet
            self.refresh_alphabets()

        return sorted(alphabet)

    def valid_letter(self, letter):
        """
        Returns True if this alphabet letter has 1 character,
        no digits, and no parentheses (for non-native letters).
        Otherwise, returns False.

        :param letter: str, alphabet letter to check whether valid
        :return: bool, True if letter is valid, False otherwise
        """
        return len(letter) == 1 and not letter.isdigit() and "(" not in letter

    def alphabet_cells(self, alphabet_table):
        """
        Returns this alphabet table's letter cells.

        :param page: (BeautifulSoup) Tag, page with alphabet table
        :return: List[str], alphabet letters in this language
        """
        cells = []
        rows = alphabet_table.find_all("tr")
        if len(rows) > 1:
            rows = rows[1:]
        for row in rows:
            cells.extend(row.find_all("td")[-1].find_all("a"))
        return cells

    def word_in_alphabet(self, word, lang=None):
        """
        Returns True if this word contains only characters from
        this language's alphabet, False otherwise.

        :param word: str, word to verify whether in language alphabet
        :param lang: str, language of alphabet
        :return: bool, whether word contains only characters from language
        """
        lang = self.verify_language(lang)
        word_chars = set(word)
        alphabet = self.find_alphabet(lang)
        return len(word_chars.difference(alphabet)) == 0

    def detect_language(self, word):
        """
        Returns the language most likely for this word.

        :param word: str, word in an unknown language
        :return: str, this word's language
        """
        langs = self.LANG_CODES
        print("LANGS:", langs)
        word_lang = None
        delta = 10

        while delta <= 50000 and word_lang is None:
            common_dicts = {lang: self.common_words(lang, lim=delta) for lang in langs}
            min_idx = float('inf')

            for lang in langs:
                try:
                    idx = common_dicts[lang].index(word)
                except ValueError:
                    continue
                else:
                    if idx < min_idx:
                        min_idx = idx
                        word_lang = lang

            delta *= 10

        return word_lang

    # TOKENIZERS
    # ----------
    def tokenize_words(self, words):
        """
        Returns a list of words in this str words.

        :param words: str, string to tokenize by word
        :return: List[str], phrase tokenized by word
        """
        return tokenizers.wordpunct_tokenize(str(words))

    def tokenize_sents(self, sents):
        """
        Returns a list of the sentences in this str sents.

        :param sents: str, string to tokenize by sentence
        :return: List[str], phrase tokenized by sentence
        """
        return tokenizers.sent_tokenizer.tokenize(str(sents))

    def tokenize_punct(self, text):
        """
        Returns a list of tokenized words from text separated
        by punctuation.
        ~
        e.g. tokenize_punct("Hello, this is my friend, Molly") ->
             [["Hello"], ["this", "is", "my", "friend"], ["Molly"]]

        :param text: str, string to tokenize by word and split by punctuation
        :return: List[List[str]], phrase separated by punctuation
        """
        text = str(text)
        words = self.tokenize_words(text)
        sentences = []
        curr_sentence = []

        for word in words:
            if self.is_punct(word) and word != u"'":
                if len(curr_sentence) != 0:
                    sentences.append(curr_sentence)
                    curr_sentence = []
            else:
                curr_sentence.append(word)

        if len(curr_sentence) != 0:
            sentences.append(curr_sentence)

        return sentences

    def tokenize_words_sents(self, phrase):
        """
        Returns a list of the words in the sentences in phrase.

        :param phrase: str, string to tokenize by sentence and word
        :return: List[str], phrase tokenized by sentence and word
        """
        sentences = self.tokenize_sents(str(phrase))
        phrases_tokens = [self.tokenize_words(sentence) for sentence in sentences]
        return phrases_tokens

    def tokenize_words_punct(self, phrase):
        """
        Returns a list of the words separated by punctuation in phrase.

        :param phrase: str, string to tokenize by sentence and word
        :return: List[str], phrase tokenized by punctuation and word
        """
        return self.tokenize_punct(str(phrase))

    # JSON
    # ----
    def load_alphabets(self):
        """
        Returns a memoized dictionary of alphabets in every language.

        :return: dict(str, list), where str is language and list is alphabet
        """
        return self.load_json("alphabets")

    def load_alphabet(self, lang=None):
        """
        Returns a list of alphabetic characters in this language,
        or for this LanguageParser's language if lang is None.

        :param lang: str, language of alphabet
        :return: List[str], lang's alphabet letters
        """
        return self.alphabets.setdefault(self.verify_language(lang), [])

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
    def lemmatize(self, word, lang=None, pos=None, add_new=False):
        """
        Returns the lemma for this word in this language.
        ~
        If word has no lemma, this method returns the given word.
        ~
        e.g. lemmatize("drove", "English", {"Verb"}) -> "drive"
             lemmatize("yeux", "French", {"Noun"}) -> "œil"

        :param word: str, word to find lemma for
        :param lang: str, language of given word
        :param pos: Set[str], parts-of-speech for output lemma
        :param add_new: bool, whether to add new Wiktionary entry
        :return: str, lemma for given word
        """
        lang = self.verify_language(lang)
        self.find_wiktionary_entry(word, lang, add_new=add_new)
        lemmas = self.find_lemmas(word, lang=lang, pos=pos, add_new=add_new)
        if lemmas is not None and len(lemmas) != 0:
            return lemmas[0]
        elif lang != "English":
            return self.lemmatize_multilingual(word, lang, pos, add_new=add_new)
        else:
            return word

    def lemmatize_multilingual(self, word, lang=None, pos=None, add_new=False):
        lang = self.verify_language(lang)
        lemmas = self.find_lemmas(word, lang, pos, add_new=add_new)

        if lemmas is not None and len(lemmas) != 0:
            return lemmas[0]
        elif pos is not None:
            lemmas = self.find_lemmas(word, lang, pos=None, add_new=add_new)
            if lemmas is not None and len(lemmas) != 0:
                return lemmas[0]

        if self.in_wiktionary(word, lang=lang, eng=False):
            sublemmas = self.find_sublemmas(word, lang, pos)
            if len(sublemmas) != 0:
                for sublemma in sublemmas:
                    if self.in_wiktionary(sublemma, lang=lang):
                        return sublemma
                else:
                    return sublemmas[0]

        return word

    def find_custom_lemma(self, word, lang, pos=None, defn_phrase="", add_new=False):
        entry = self.find_wiktionary_subentry(word, lang, pos, add_new=add_new)
        if type(defn_phrase) == str:
            defn_phrase = [defn_phrase]

        def search_subentry(subentry):
            for defn in subentry['definitions']:
                if all(d in defn for d in defn_phrase):
                    defn_words = tokenizers.wordpunct_tokenize(defn)
                    for lemma in subentry['lemmas'][lang]:
                        if lemma in defn_words:
                            print("LEMMA OF", word, "IS", lemma)
                            return lemma

        if entry is not None and len(entry) != 0:
            if pos is None:
                for pos in entry:
                    lemma = search_subentry(entry[pos])
                    if lemma is not None:
                        return lemma
            else:
                return search_subentry(entry)

    def find_lemmas(self, word, lang, pos=None, add_new=False):
        pos_entries = self.find_pos_entries(word, lang=lang, pos=pos, add_new=add_new)
        if len(pos_entries) != 0:
            lemmas = OrderedSet([])
            for pos_entry in pos_entries:
                entry = pos_entries[pos_entry]
                entry_lemmas = entry.get("lemmas", None)
                if entry_lemmas is not None:
                    lemmas.update(entry_lemmas[lang])
            return lemmas.items()
        else:
            return None

    def find_sublemmas(self, word, lang, pos=None):
        word_page = self.find_page_language(self.word_page(word, eng=False), lang, eng=False)
        page_sibs = word_page.find_next_siblings()
        sublemmas = OrderedSet([])
        for sib in page_sibs:
            if sib.name == 'h2' and sib.find('span', attrs={'id': self.LANG_CODES[lang]}) is None:
                break
            sibtxt = sib.get_text()
            if any(str(dig) in sibtxt for dig in range(1, 9)):  # check digits for definition numbers
                links = sib.find_all('a')
                lemmas = [link.get('title') for link in links
                            if link.get('href') == '/wiki/' + link.get('title',' ')]
                for lemma in lemmas:
                    if pos is None or any(p in pos for p in self.word_poses(lemma, lang=lang, add_new=False)):
                        sublemmas.add(lemma)

            return sublemmas.items()

        return [word]

    def word_lemmas(self, word, lang=None, pos=None):
        """
        Returns the lemmas for this word in this language.
        ~
        e.g. word_lemmas("driven", "English") -> ["drive", "driven"]

        :param word: str, word to find lemmas for
        :param lang: str, language of given word
        :param pos: Set[str], parts-of-speech for output lemmas
        :return: List[str], lemmas for given word
        """
        if len(word) == 0:
            return []
        if pos is None:
            pos = self.PARTS_OF_SPEECH
        if type(pos) == str:
            pos = set(pos)

        lang = self.verify_language(lang)
        inflections = self.find_word_inflections(word, lang)
        lemmas = OrderedSet([])

        if inflections is not None:
            lemmas.add(word)
        else:
            stemwords = self.find_stemwords(word, lang, pos)
            stemwords = self.filter_language_words(stemwords, lang)
            lemmas.update(stemwords)

            if len(lemmas) == 0:
                headwords = self.find_headwords(word, lang, pos)
                headwords = self.filter_language_words(headwords, lang)
                lemmas.update(headwords)

        return lemmas.items()

    def is_word_in_language(self, word, lang=None):
        """
        Returns True if this word is in this language,
        False otherwise.
        ~
        e.g. is_word_in_language("balloon", "English") -> True
             is_word_in_language("ballon", "English") -> False
             is_word_in_language("ballon", "French") -> True

        :param word: str, word to check whether in language
        :param lang: str, language to check
        :return: bool, whether word is in language
        """
        lang = self.verify_language(lang)
        word_page = self.word_page(word)

        if word_page is None:
            lang_lexicon = self.find_lexicon(lang)
            return word in lang_lexicon
        else:
            return self.valid_page(word_page, lang)

    def filter_language_words(self, words, lang=None):
        """
        Returns this list of words filtered to only include
        words in this language's lexicon.
        ~
        e.g. filter_language_words(["balloon", "ballon"], "English") -> ["balloon"]
             filter_language_words(["balloon", "ballon"], "French") -> ["ballon"]

        :param words: List[str], list of words to filter by language
        :param lang: str, desired language of output words
        :return: List[str], words only in this language
        """
        return [word for word in words if self.is_word_in_language(word, lang)]

    def uninflect(self, word, lang=None):
        """
        Returns the uninflected form of this word in this language.

        :param word: str, word to uninflect
        :param lang: str, language of word
        :return: str, word uninflected
        """
        lang = self.verify_language(lang)
        for word_entry in self.wiktionary_entries:
            inflections = self.lookup_word_inflections(word_entry, lang)
            if inflections is not None:
                for inflection in inflections:
                    if inflection == word:
                        return word_entry
        else:
            return self.lemmatize(word, lang=lang)

    # IPAS
    # ----
    def word_ipa(self, word, lang=None):
        """
        Transcribes the given word to IPA.  Returns this word's
        IPA pronunciation and adds its transcription to the given
        language's IPA dictionary.

        :param word: str, word to transcribe to IPA
        :param lang: str, word's language
        :return: unicode, IPA transcription of word
        """
        ipas = self.word_ipas(word, lang)
        if len(ipas) != 0:
            return ipas[0]
        else:
            return

    def word_ipas(self, word, lang=None):
        """
        Transcribes the given word to IPAs.

        :param word: str, word to transcribe to IPA
        :param lang: str, word's language
        :return: List[unicode], IPA transcriptions of word
        """
        lang = self.verify_language(lang)
        entry = self.find_wiktionary_subentry(word, lang, u"Pronunciation", add_new=True)
        if entry is None:
            entry = []
        if len(entry) == 0:
            ipa = self.etymology_ipa(word, lang)
            if ipa is not None:
                entry.insert(0, ipa)
                self.edit_wiktionary_entry(word, lang, u"Pronunciation", entry)
        return entry

    def words_ipa(self, words):
        """
        Transcribes the given words to IPA.

        :param word: List[str], words to transcribe to IPA
        :return: List[unicode], IPA transcriptions of words
        """
        ipas = []

        for word in words:
            ipa = self.word_ipa(word)
            if ipa is not None:
                ipas.append(ipa)

        return ipas

    def find_headwords(self, word, lang=None, pos=None):
        """
        Returns this word's head word from its Wiktionary entry
        in this language for each part of speech in poses.
        ~
        N.B. A "head word" is the first item in the first sublist
        under a word's part-of-speech heading:

            e.g. "Noun": [["miles", None], ["plural of mile", "mile"]]
                            ^^^^^
                          head word

        Part-of-speech entry contain only 1 head word but may
        contain >=1 stem words.

        :param word: str, word of Wiktionary entry to lookup
        :param lang: Optional[str], language of entry to lookup
        :param pos: Optional[List], parts of speech to lookup
        :return: List[str], given word's head words for this language
        """
        pos_entries = self.find_pos_entries(word, lang, pos)
        headwords = []

        for pos_entry in pos_entries:
            entry = pos_entries[pos_entry]
            try:
                headword = entry[0][0]
            except IndexError:
                continue
            else:
                if headword is not None and headword in self.find_lexicon(lang):
                    headwords.append(headword)

        return headwords

    def find_stemwords(self, word, lang=None, pos=None):
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
        :param lang: Optional[str], language of entry to lookup
        :param pos: Optional[List], parts of speech to lookup
        :return: List[str], given word's stem words for this language
        """
        pos_entries = self.find_pos_entries(word, lang, pos)
        stemwords = []

        for pos_entry in pos_entries:
            entry = pos_entries[pos_entry]
            print("\t", pos_entry, "has entry", entry)
            try:
                stems = [e[1] for e in entry[1:] if e[1] is not None]
            except IndexError:
                continue
            else:
                stemwords += stems

        return OrderedSet(stemwords).rank_items()

    def find_word_ipas(self, word, lang=None):
        """
        Transcribes the given word to IPAs.

        :param word: str, word to transcribe to IPA
        :param lang: str, word's language
        :return: List[unicode], IPA transcriptions of word
        """
        lang = self.verify_language(lang)
        try:
            return self.wiktionary_entries[word][lang][u"Pronunciation"]
        except KeyError:
            return []

    def etymology_ipa(self, word, lang=None):
        """
        Returns this word's IPA constructed from its etymology.

        :param word: str, word to return etymology's IPA of
        :param lang: str, language of word
        :return: (unicode) str, this word's etymology's IPA
        """
        lang = self.verify_language(lang)
        etyms = self.find_word_etymology(word, lang)
        ipas = []
        if etyms is not None and len(etyms) != 0:
            for etym in etyms:
                etym_ipa = self.word_ipa(etym)
                if etym_ipa is None:
                    return
                else:
                    ipas += etym_ipa
        return "".join(ipas)

    # MORPHEMES
    # ---------
    def word_morphemes(self, word, lang=None):
        """
        Returns a set of morphemes in this word.

        :param word: str, word to find morphemes of
        :param lang: str, language of morpehemes
        :return: List[str], word's morphemes
        """
        word = self.entry_word(word, lang)
        return self.lookup_word_etymology(word, lang)

    def recursive_all_word_morphemes(self, word, lang=None):
        """
        Returns a set of morphemes in this word, including the
        morphemes for all its sub-morphemes.
        ~
        e.g. all_word_morphemes("undeniable", "English") -> ["un-", "deny", "-able"]

        :param word: str, word to find morphemes of
        :param lang: str, language of morpehemes
        :return: List[str], word's morphemes
        """
        lang = self.verify_language(lang)
        word_morphemes = self.word_morphemes(word, lang)
        if word_morphemes is not None:
            submorphemes = OrderedSet(word_morphemes)
            for morpheme in word_morphemes:
                submorphemes.update(self.recursive_all_word_morphemes(morpheme))
        else:
            submorphemes = OrderedSet([])
        return submorphemes

    def all_word_morphemes(self, word, lang=None):
        """
        Returns a set of morphemes in this word, including the
        morphemes for all its sub-morphemes.
        ~
        e.g. all_word_morphemes("undeniable", "English") -> ["un-", "deny", "-able"]

        :param word: str, word to find morphemes of
        :param lang: str, language of morpehemes
        :return: List[str], word's morphemes
        """
        lang = self.verify_language(lang)
        morphemes = OrderedSet([])
        todo = {word}

        while len(todo) != 0:
            curr_word = todo.pop()
            if len(curr_word) != 0 and curr_word not in morphemes.items_set and not self.contains_punct(curr_word):
                morphemes.add(curr_word)
                word_morphemes = self.word_morphemes(curr_word, lang)
                if word_morphemes is not None:
                    morphemes.update(word_morphemes)
                    todo.update(word_morphemes)

        return morphemes.order_items()

    def words_morphemes(self, words, lang=None):
        """
        Returns a list of morphemes in these words.

        :param word: str, word to find morphemes of
        :param lang: str, language of morpehemes
        :return: List[str], words' morphemes
        """
        lang = self.verify_language(lang)
        morphemes = []
        for word in words:
            if not self.is_punct(word):
                word = self.entry_word(word, lang)
                word_morphemes = self.all_word_morphemes(word, lang)
                print("adding", word, "morphemes:", word_morphemes)
                morphemes += word_morphemes
        return morphemes

    def sentences_morphemes(self, sentences, lang=None):
        """
        Returns a list of morphemes in these sentences.

        :param sentences: str, sentences to find morphemes of
        :param lang: str, language of sentences
        :return: List[str], sentences's morphemes
        """
        lang = self.verify_language(lang)
        sents_tokens = self.tokenize_words(str(sentences))
        return self.words_morphemes(sents_tokens, lang)

    # MINIMAL PAIRS
    # -------------
    # Find "minimal pairs" in a language of words
    # which differ by only 1 IPA, or sentences which
    # differ by only 1 word.
    # -------------

    # LOOKUPS & FINDS
    # ---------------
    # Use lookup to "look up" existing entry,
    # use find to "find" new entry if none exist.
    # ---------------
    def lookup_word_inflections(self, word, lang):
        """
        Returns all inflected forms of this word in wiktionary_entries.

        :param word: str, word to get inflections of
        :return: List[str], all inflected forms of word
        """
        try:
            return self.wiktionary_entries[word][lang][u"Inflections"]
        except KeyError:
            return

    def find_word_inflections(self, word, language, add_new=False):
        """
        Returns all inflected forms of this word from Wiktionary.

        :param word: str, word for inflections to get inflections of
        :return: List[str], all inflected forms of word
        """
        return self.find_wiktionary_subentry(word, language, u"Inflections", add_new=add_new)

    def lookup_word_etymology(self, word, lang=None):
        """
        Returns the etymology of the given word in this
        language (according to Wiktionary).

        :param word: str, word to find etymology of
        :param lang: str, language of etymology
        :return: List[str], etymological roots of this word
        """
        lang = self.verify_language(lang)
        return self.lookup_wiktionary_subentry(word, lang, u"Etymology")

    def find_word_etymology(self, word, lang=None, add_new=False):
        """
        Returns the etymology of this word from Wiktionary.

        :param word: str, word to lookup etymology of
        :param lang: str, language of etymology
        :return: List[str], etymological roots of this word
        """
        lang = self.verify_language(lang)
        return self.find_wiktionary_subentry(word, lang, u"Etymology", add_new=add_new)

    # ALL ENTRIES
    # -----------
    def all_inflections(self, lang=None):
        """
        Returns a dictionary of all words in this language's inflections.

        :param lang: str, language of inflections dicts
        :return: dict(str, Set(str)), inflection-lemma pairs in this language
        """
        lang = self.verify_language(lang)
        all_inflections = {}

        for word in self.wiktionary_entries:
            inflections = self.lookup_word_inflections(word, lang)
            if inflections is not None:
                for inflection in inflections:
                    all_inflections.setdefault(inflection, set())
                    all_inflections[inflection].add(word)

        return all_inflections

    def all_morphemes(self, lang=None):
        """
        Returns all words in this language's inflections.

        :param lang: str, language of inflection dict
        :return: List[str], all morphemes in this language
        """
        lang = self.verify_language(lang)
        morphemes = []

        for word in self.wiktionary_entries:
            etyms = self.word_morphemes(word, lang)
            if etyms is not None:
                morphemes += etyms

        return morphemes

    def all_ipas(self, lang=None):
        """
        Returns all IPAs in this language's pronunciations.

        :param lang: str, language of pronunciations
        :return: dict(str, str), inflection-lemma pairs in this language
        """
        lang = self.verify_language(lang)
        ipas = {}

        for word in self.wiktionary_entries:
            word_ipas = self.find_word_ipas(word, lang)
            if word_ipas is not None:
                ipas.setdefault(word, [])
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
            path = PATH + "/resources/wordnet/wn_s.txt"

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
        path = PATH + "/resources/wordnet/wn_s.txt"
        entries = set()

        with open(path, "r") as synsets:
            for synset in synsets:
                synset = synset[2:-3]
                info = synset.split(",")
                name = info[2]
                name = str(name[1:-1])
                pos = str(info[3])
                if " " not in name:
                    pair = (name, pos)
                    entries.add(pair)

        return entries

    # COMMON WORDS
    # ------------
    def common_words(self, lang=None, lim=50000):
        """
        Returns the most common words in this language up to lim.

        :param lim: int, lim <= 50000, number of words to retrieve
        :param lang: Optional[str], language of common words
        :return: List[str], 50k most common words in language
        """
        lang_code = self.lang_code(lang)

        if lang_code is None:
            return

        words = []
        path = PATH + "/resources/frequency_words/content/2016/%s/%s_50k.txt" % (lang_code, lang_code)

        with open(path, 'r') as fifty_k:
            line_no = 0
            for line in fifty_k:
                word = str(line).split(" ", 1)[0]
                words.append(word)
                if line_no > lim:
                    break
                line_no += 1

        return words

    def common_word(self, idx, lang):
        assert -50000 < idx <= 50000
        lang_code = self.lang_code(lang)
        if lang_code is None:
            return
        path = PATH + "/resources/frequency_words/content/2016/%s/%s_50k.txt" % (lang_code, lang_code)

        with open(path, 'r') as common_words:
            idx_line = common_words.readlines()[idx]
            idx_word = str(idx_line).split(" ", 1)[0]
            return idx_word

    def common_word_pairs(self, lang=None, lim=50000):
        """
        Returns the most common word-pos pairs in this language
        up to lim.

        :param lim: int, number of common words to return
        :param lang: Optional[str], language of common words
        :return: List[tuple(str, str)], Wordnet word and pos
        """
        lang = self.verify_language(lang)
        common_words = self.common_words(lang, lim)

        if lang == "English":
            word_pairs = self.get_wordnet_word_pairs()
            return [word_pair for word_pair in word_pairs if word_pair[0] in common_words]
        else:
            poses = [self.word_poses(word, lang) for word in common_words]
            word_pairs = []

            for i in range(len(common_words)):
                word = common_words[i]
                pos = poses[i]
                if len(pos) == 0:
                    pos.append(None)
                for p in pos:
                    pair = (word, p)
                    word_pairs.append(pair)

            return word_pairs

    def common_morphemes(self, lang=None, lim=50000):
        """
        Returns the most common words in this language up to lim,
        including their constituent words.

        :param lim: int, lim <= 50000, number of words to retrieve
        :param lang: Optional[str], language of common morpemes
        :return: List[str], up to 50k most common words in LanguageParser's language
        """
        lang = self.verify_language(lang)
        lexicon = self.find_lexicon(lang, lim)
        common_words = lexicon[:lim]
        morphemes = self.words_morphemes(common_words, lang)
        return morphemes

    def add_common_wiktionary_entries(self, lang=None, lim=50000):
        """
        Adds Wiktionary entry for the most common words in
        this language to this WiktionaryParser's wiktionary_entries.

        :param words: List[str], words of Wiktionary entry to add
        :param lang: Optional[str], language of entry to add
        :return: dict(str, dict), where str is language and dict is...
            key (str) - title of subentry heading (e.g. Etymology)
            val (list) - value(s) associated with subentry
        """
        lang = self.verify_language(lang)
        self.find_wiktionary_entries(self.common_words(lang, lim), lang)
        return self.wiktionary_entries

    # URLS
    # ----
    def lemma_url(self, lang=None):
        """
        Returns the Wiktionary URL for lemmas in this language.

        :param lang: str, language of URL
        :return: str, Wiktionary URL for this parser's lemmas
        """
        lang = self.verify_language(lang)
        return (self.WIKI_URL + self.END_URL + self.LEMMA_PATH).format(lang_code="en",  #self.get_lang_code(language),
                                                                       lang=lang)

    def ipa_url(self, lang=None):
        """
        Returns the Wiktionary URL for IPAs in this language.

        :param lang: str, language of IPA URL
        :return: str, Wiktionary URL for this parser's IPAs
        """
        lang = self.verify_language(lang)
        return (self.WIKI_URL + self.END_URL + self.IPA_PATH).format(lang_code="en",  #self.get_lang_code(language),
                                                                     lang=lang)


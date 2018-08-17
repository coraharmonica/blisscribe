# coding: utf-8
"""
WIKTIONARY_PARSER:

    Contains WiktionaryParser class for parsing Wiktionary entry in any language.
"""
import os, sys
PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(PATH)
import re
import string
import json
import requests
from bs4 import BeautifulSoup
try:
    from bliss_online.bliss_webapp.translation.ordered_set import OrderedSet
except (ModuleNotFoundError, ImportError):
    from translation.ordered_set import OrderedSet
from .ipa_symbols import *


class WiktionaryParser:
    """
    A class for parsing Wiktionary pages.
    """
    LEXICA = {}
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
                  "Telug": "te",
                  "Thai": "th",
                  "Tagalog": "tl",
                  "Turkish": "tr",
                  "Ukrainian": "uk",
                  "Vietnamese": "vi"}
    PARTS_OF_SPEECH = {"Noun", "Verb", "Adjective", "Adverb",
                       "Conjunction", "Interjection", "Determiner",
                       "Preposition", "Postposition",
                       "Morpheme", "Pronoun", "Proper noun",
                       "Phrase", "Numeral", "Particle", "Article", "Participle",
                       "Prefix", "Suffix", "Circumfix", "Interfix", "Infix"}
    WIKI_URL = "https://{lang_code}.wiktionary.org"
    ENG_URL = WIKI_URL.format(lang_code="en")
    END_URL = "/w/index.php?title=Category:{lang}"
    BASE_URL = WIKI_URL + "/wiki/{word}#{lang}"
    IPA_PATH = "_terms_with_IPA_pronunciation&from="
    LEMMA_PATH = "_lemmas"
    HEADER_NAMES = PARTS_OF_SPEECH.union({"Pronunciation",
                                          "Etymology",
                                          "Declension",
                                          "Conjugation",
                                          "Inflections"})

    def __init__(self):
        self._session = requests.session()
        self.language = None
        self.wiktionary_entries = self.load_wiktionary_entries()
        self._quote_pattern = None
        self._paren_pattern = None
        self._space_pattern = None

    @property
    def quote_pattern(self):
        if self._quote_pattern is None:
            self._quote_pattern = re.compile("\"[^\+]*?\"")
        return self._quote_pattern

    @property
    def paren_pattern(self):
        if self._paren_pattern is None:
            self._paren_pattern = re.compile("\([^\(]*?\)")
        return self._paren_pattern

    @property
    def space_pattern(self):
        if self._space_pattern is None:
            self._space_pattern = re.compile("( )+")
        return self._space_pattern

    def add_lexicon(self, lang, lexicon):
        """
        Adds the given lexicon to LEXICA under the given language.

        :param lang: str, language of lexicon
        :param lexicon: List[str], all words in given language
        :return: None
        """
        self.LEXICA[lang] = lexicon

    def find_lexicon(self, lang=None, lim=100000):
        """
        Returns the lexicon for the given language.
        ~
        If no lexicon for this language exists, creates new
        lexicon for language, adds to LEXICA, and returns the result.

        :param lang: str, language of lexicon
        :return: List[str], all words in given language
        """
        lang = self.verify_language(lang)

        try:
            return self.LEXICA[lang]
        except KeyError:
            lexicon = self.init_lexicon(lang, lim)
            self.add_lexicon(lang, lexicon)
            return lexicon

    def verify_language(self, language):
        """
        If this language is None, returns self.language if
        not None or otherwise "English".
        Otherwise, returns this language.

        :param language: str, language to verify
        :return: str, verified language
        """
        if language is None:
            return self.language if self.language is not None else "English"
        else:
            return language

    def valid_ipa(self, ipa):
        """
        Returns True if this IPA pronunciation contains only
        valid IPA symbols.
        ~
        Used for rooting out invalid IPA symbols.

        :param ipa: unicode, IPA pronunciation to verify
        :return: bool, whether given IPA is valid
        """
        return ipa[0] != "-" and self.ipaize(ipa) == ipa

    def lang_code(self, lang=None):
        """
        Returns the language code associated with the given language.
        ~
        e.g. get_lang_code("Polish") -> "pl"

        :param lang: str, language to retrieve language code for
        :return: str, language code for given language
        """
        lang = self.verify_language(lang)
        return self.LANG_CODES.get(lang, None)

    def init_lexicon(self, lang=None, lim=None):
        """
        Returns a set of all words in this language, up to lim.
        ~
        If lim is None, returns all words.

        :param lang: str, language of lexicon to retrieve
        :param lim: int, number of words in lexicon to retrieve
        :return: List[str], words in LanguageParser's language
        """
        lang_code = self.lang_code(lang)
        words = list()

        if lang_code is not None:
            path = PATH + "/resources/frequency_words/content/2016/{0}/{0}_full.txt".format(lang_code)
            with open(path, 'r', encoding='utf-8') as lexicon:
                line_no = 0
                for line in lexicon:
                    word = line.split(" ", 1)[0]
                    words.append(str(word))
                    if lim:
                        if line_no > lim:
                            break
                        line_no += 1
        return words

    # JSON
    # ----
    def dump_json(self, data, filename):
        """
        Dumps data (prettily) to filename.json.

        :param data: X, data to dump to JSON
        :param filename: str, name of .json file to dump to
        :return: None
        """
        path = PATH + "/resources/data/" + filename + ".json"
        json.dump(data, open(path, 'w', encoding='utf-8'), indent=1, sort_keys=True, ensure_ascii=False)

    def load_json(self, filename):
        """
        Returns a dictionary corresponding to the given JSON file.

        :param filename: str, name of .json file to load
        :return: X, content of given .json file
        """
        path = PATH + "/resources/data/" + filename + ".json"
        return json.load(open(path, encoding='utf-8'))

    def load_wiktionary_entries(self):
        """
        Returns a dictionary of memoized Wiktionary pages.

        :return: dict(str, dict), where str is a word and dict is...
            key (str) - language of word entry
            val (dict) - language's entry under word
        """
        return self.load_json("wiktionary_entries")

    def refresh_wiktionary_entries(self):
        """
        Dumps this WiktionaryParser's wiktionary_entries data to
        wiktionary_entries.json.

        :return: None
        """
        self.dump_json(self.wiktionary_entries, "wiktionary_entries")

    # WIKTIONARY PAGES
    # ----------------
    def entry_word(self, word, lang=None):
        """
        Returns the correctly capitalized version of this word
        which has an entry in wiktionary_entries.

        :param word: str, word to find entry word for
        :param lang: str, language of given word
        :return: str, entry word for given word
        """
        lang = self.verify_language(lang)
        nuwords = [word, word.lower(), word.title()]

        for nuword in nuwords:
            if self.in_wiktionary(nuword, lang):
                return nuword

        return word

    def find_wiktionary_entries(self, words, lang=None):
        """
        Adds Wiktionary entry for these words to this
        WiktionaryParser's wiktionary_entries.

        :param words: List[str], words of Wiktionary entry to add
        :param lang: str, language of entry to add
        :return: List[dict]
        """
        lang = self.verify_language(lang)
        return [self.find_wiktionary_entry(word, lang) for word in words]

    def edit_wiktionary_entry(self, word, lang=None, heading=None, content=None):
        """
        Edits the Wiktionary entry for this word by adding this content
        under this language and heading.

        :param word: str, word of Wiktionary entry to edit
        :param lang: str, language of entry to edit
        :param heading: str, heading of entry to edit
        :param content: List[str], content to add to entry
        :return: None
        """
        word = str(word)
        lang = self.verify_language(lang)
        entry = self.lookup_wiktionary_subentry(word, lang)
        if entry is None:
            entry = dict()
        entry.setdefault(heading, list())

        try:
            self.wiktionary_entries[word][lang].setdefault(heading, list())
        except KeyError:
            return
        else:
            entry = self.wiktionary_entries[word][lang][heading]
            self.wiktionary_entries[word][lang][heading] = OrderedSet(entry + content).items()

    def contains_punct(self, word):
        """
        Returns True if any punctuation characters are in this word.

        :param word: str, word to check whether containing punctuation
        :return: bool, whether punctuation in this word or not
        """
        return any(char in word for char in "\n\t "+string.punctuation)

    def is_punct(self, word):
        """
        Returns True if this word contains only punctuation characters.

        :param word: str, word to check whether containing punctuation
        :return: bool, whether punctuation in this word or not
        """
        return all(not char.isalpha() for char in word) #all(char in string.punctuation for char in word)

    # LOOKUPS & FINDS
    # ---------------
    # Use lookup to "look up" existing entry,
    # use find to "find" new entry if none exist.
    # ---------------
    def find_wiktionary_entry(self, word, lang=None, add_new=False):
        """
        If a Wiktionary page corresponding to this word already
        exists, returns the memoized page.  Otherwise, retrieves new
        Wiktionary page data for word and adds new entry to this
        WiktionaryParser's wiktionary_entries.

        :param word: str, word of Wiktionary page to lookup
        :param lang: str, language of entry to lookup
        :param add_new: bool, whether to add new entries
        :return: dict(str, dict), where str is language and dict is...
            key (str) - title of subentry heading (e.g. Etymology)
            val (list) - value(s) associated with subentry
        """
        if word is None:
            return
        else:
            entry = self.lookup_wiktionary_entry(word, lang)
            if entry is not None:
                return entry
            else:
                entry = self.wiktionary_entries.get(word, dict())
                entry = entry.get(lang, None)
                if add_new and entry is None and not self.is_punct(word):
                    entry = self.word_wikt_page(word, lang).entry
                    if lang is not None:
                        entry = entry.get(lang, None)
                return entry

    def lookup_wiktionary_entry(self, word, lang=None):
        """
        If a Wiktionary page corresponding to this word already
        exists, returns the memoized page.  Otherwise, returns None.

        :param word: str, word of Wiktionary page to lookup
        :param lang: str, language of entry to lookup
        :return: dict(str, dict), where str is language and dict is...
            key (str) - title of subentry heading (e.g. Etymology)
            val (list) - value(s) associated with subentry
        """
        lang = self.verify_language(lang)
        try:
            return self.wiktionary_entries[word][lang]
        except KeyError:
            return

    def find_wiktionary_subentry(self, word, lang=None, heading=None, add_new=False):
        """
        Returns the Wiktionary subentry for the given word, language and/or heading.
        ~
        If language is None, this method returns the sub-entry for this
        word.
        ~
        If language is not None, this method returns the sub-entry
        for this language.
        ~
        If heading is not None, this method returns all sub-entry with
        this heading for this word in this language.
        ~
        If no entry contains the parameters given, returns an empty dict.
        ~
        e.g. find_wiktionary_subentry("is", "Afrikaans", "Pronunciation") -> ["əs"]
             find_wiktionary_subentry("is", heading="Pronunciation") ->
                ["əs", "i\u02d0s", "s", ""a\u026az", ...]
             find_wiktionary_subentry("is", "Afrikaans") ->
                {"Pronunciation": ["əs"],
                 "Verb": [["is", null],
                          ["am , are , is ( present tense, all persons, plural and singular of wees , to be )", null],
                          ["Forms the perfect passive voice when followed by a past participle", null]]}

        :param word: str, word of Wiktionary page to lookup
        :param lang: Optional[str], language of entry to lookup
        :param heading: Optional[str], heading of subentry to lookup
        :param add_new: bool, whether to add new Wiktionary entry
        :return: Any, subentry corresponding to given word, language, &/or heading
        """
        if word is None:
            return self.wiktionary_entries
        elif self.contains_punct(word):
            return

        if lang is None:
            return self.find_wiktionary_entry(word, add_new=add_new)
        else:
            entry = self.find_wiktionary_entry(word, lang, add_new=add_new)
            if heading is None or entry is None:
                return entry
            else:
                section = entry.get(heading, None)
                if section is not None:
                    return section
                else:
                    for section in entry:
                        if section[:len(heading)] == heading:
                            return entry[section]
        return

    def lookup_wiktionary_subentry(self, word, lang=None, heading=None):
        """
        Looks up this word's subentry in wiktionary_entries with this language
        and heading.

        :param word: str, word of Wiktionary page to lookup
        :param lang: Optional[str], language of entry to lookup
        :param heading: Optional[str], heading of subentry to lookup
        :return: Any, subentry corresponding to given word, language, &/or heading
        """
        try:
            entry = self.wiktionary_entries[word]
            if lang is not None:
                entry = entry[lang]
                if heading is not None:
                    entry = entry[heading]
        except KeyError:
            return
        else:
            return entry

    def find_pos_entries(self, word, lang, pos=None, add_new=False):
        """
        Returns this word's parts of speech in poses from its
        Wiktionary entry in this language.
        ~
        If pos is None, finds entries for all parts of speech.

        :param word: str, word of Wiktionary entry to lookup
        :param lang: str, language of entry to lookup
        :param pos: Optional[str or Iterable], part(s) of speech to lookup
        :param add_new: bool, whether to add new Wiktionary entry
        :return: List[str], word's parts of speech entry in this language
        """
        if pos is None:
            pos = self.PARTS_OF_SPEECH
        if type(pos) == str:
            pos = {pos}

        lang = self.verify_language(lang)
        lang_entries = self.find_wiktionary_entry(word, lang, add_new=add_new)
        pos_entries = dict()

        if lang_entries is not None:
            for heading in lang_entries:
                if heading in pos:
                    pos_entries[heading] = lang_entries[heading]

        return pos_entries

    # PARTS-OF-SPEECH
    # ---------------
    def word_pos(self, word, lang=None, add_new=False):
        """
        Returns this word's part of speech.

        :param word: str, word to get part of speech of
        :param lang: str, word's language
        :return: str, word's part of speech
        """
        poses = self.word_poses(word, lang, add_new=add_new)
        if len(poses) != 0:
            return poses[0]

    def word_poses(self, word, lang, add_new=False):
        """
        Returns a list of this word's parts of speech from its
        Wiktionary entry in this language.

        :param word: str, word of Wiktionary entry to lookup
        :param lang: str, language of entry to lookup
        :param add_new: bool, whether to add new Wiktionary entry
        :return: List[str], word's parts of speech in this language
        """
        lang = self.verify_language(lang)
        word_entry = self.find_wiktionary_entry(word, lang, add_new=add_new)

        if word_entry is not None:
            poses = [sect for sect in word_entry
                     if sect in self.PARTS_OF_SPEECH]
            pos_set = OrderedSet(poses)
            return pos_set.items()
        else:
            return []

    def find_english_translation(self, word, lang=None, pos=None):
        """
        Returns this word's translation from this language to English,
        according to Wiktionary.

        :param word: str, word to translate
        :param lang: str, language of word
        :param pos: str, part-of-speech of word
        :return: str, word's translation in English
        """
        translations = self.find_english_translations(word, pos, lang)
        try:
            return translations[0]
        except IndexError:
            return

    def find_english_translations(self, word, pos, lang=None, add_new=False):
        """
        Returns this word's translations from this language to English,
        according to Wiktionary.

        :param word: str, word to translate
        :param pos: str or Iterable, word's part(s)-of-speech
        :param lang: str, language of word
        :param add_new: bool, whether to add new Wiktionary entry
        :return: List[str], word's translations in English
        """
        lang = self.verify_language(lang)

        if type(pos) != str:
            if pos is None:
                pos = self.PARTS_OF_SPEECH

            if len(pos) == 1:
                pos = pos.pop()
            else:
                word_entries = OrderedSet([])
                for p in pos:
                    word_entries.update(self.find_english_translations(word, p, lang))
                return word_entries.intersections()

        word_entry = self.find_wiktionary_subentry(word, lang, heading=pos, add_new=add_new)
        if word_entry is None:
            return []
        else:
            try:
                return word_entry["lemmas"]["English"]
            except KeyError:
                return []

    def find_terms(self, word, pos, lang=None, add_new=False):
        """
        Returns this word's terms (e.g. genitive, plural, etc.)
        according to Wiktionary.

        :param word: str, word to find terms for
        :param pos: str or Iterable, word's part(s)-of-speech
        :param lang: str, language of word
        :param add_new: bool, whether to add new Wiktionary entry
        :return: List[str], word's terms
        """
        if type(pos) == str:
            return self.find_wiktionary_subentry(word, lang, pos, add_new)['terms']
        else:
            terms = OrderedSet([])
            for p in pos:
                subentry = self.find_wiktionary_subentry(word, lang, p, add_new)
                if subentry is not None:
                    terms.update(subentry.get('terms', []))
            return terms.intersections()

    # PAGES
    # -----
    def word_url(self, word, eng=True):
        """
        Returns a Wiktionary URL for this word.
        ~
        If eng is True, URL is from en.wiktionary.org.
        Else, URL is from this parser's language's Wiktionary.

        :param word: str, word to retrieve URL for
        :param eng: bool, whether Wiktionary is in English
        :return: str, URL matching this word
        """
        lang_code = "en" if eng else self.LANG_CODES[self.language]
        return self.BASE_URL.format(word=word, lang=self.language, lang_code=lang_code)

    def url_page(self, url):
        """
        Parses given URL string to a BeautifulSoup Tag.

        :param url: str, URL to parse to tags
        :return: Tag, parsed URL
        """
        response = self._session.get(url)
        html = response.text
        parsed = BeautifulSoup(html, "lxml")
        return parsed

    def word_page(self, word, eng=True):
        """
        Returns a BeautifulSoup Tag corresponding to the Wiktionary
        page for this word.
        ~
        If eng is True, Wiktionary page is from en.wiktionary.org.
        Otherwise, page is from this parser's language's Wiktionary.

        :param word: str, word to retrieve page for
        :param eng: bool, whether Wiktionary is in English
        :return: Tag, BeautifulSoup tag matching this word's page
        """
        return self.url_page(self.word_url(word, eng=eng))

    def word_wikt_page(self, word, lang=None):
        """
        Returns a WiktionaryPage for this word in this language.

        :param word: str, word to create WP for
        :param lang: str, language of this word
        :return: WiktionaryPage, Wiktionary page for this word
        """
        lang = self.verify_language(lang)
        return WiktionaryPage(word=word, lang=lang, parser=self)

    def in_wiktionary(self, word, lang=None, eng=True):
        """
        Returns True if this word has a Wiktionary page,
        False otherwise.
        ~
        If eng is True, Wiktionary page is from en.wiktionary.org.
        Otherwise, page is from this parser's language's Wiktionary.

        :param word: str, word for a Wiktionary page entry
        :param lang: str, language to find in Wiktionary
        :param eng: bool, whether Wiktionary is in English
        :return: bool, whether page is valid
        """
        return self.valid_page(self.word_page(word, eng=eng), lang, eng=eng)

    def find_page_language(self, page, lang, eng=True):
        """
        Returns the first span on this page in this language.
        ~
        If eng is True, checks page with English Wiktionary conventions.
        Otherwise, checks page according to multilingual conventions.

        :param page: Tag, HTML Wiktionary page in BeautifulSoup
        :param lang: str, language to find on page
        :param eng: bool, whether Wiktionary is in English
        :return: Tag, first HTML span from page in language
        """
        header = page.find("span", attrs={"class": "mw-headline", "id": lang})
        if not eng and header is None:
            # Any Wiktionary's top entry is in its own language.
            # i.e. English wikt's top entry for "cent" is English,
            #      French wikt's for "cent" is French, etc.
            nuheader = page.find("span", attrs={"class": "mw-headline"})
            if nuheader is not None and nuheader.find("span", attrs={"id": self.LANG_CODES[lang]}) is not None:
                return nuheader.find_parent("h2")
        return header

    def valid_page(self, page, lang=None, eng=True):
        """
        Returns True if this Wiktionary page contains an
        entry under this language, False otherwise.
        ~
        If eng is True, checks Wiktionary at en.wiktionary.org.
        Otherwise, checks parser's language's Wiktionary.

        :param page: Tag, HTML Wiktionary page for an entry
        :param lang: str, language to check whether on page
        :param eng: bool, whether Wiktionary is in English
        :return: bool, whether this page has an entry in this language
        """
        if lang is None:
            return page.find("h2").get_text()[:10] != "Navigation"
        else:
            return self.find_page_language(page, lang, eng=eng) is not None

    def word_languages(self, word):
        """
        Returns a list of the given word's Wiktionary entry's languages.

        :param word: str, word of Wiktionary entry to retrieve languages for
        :return: List[str], all languages for this word's Wiktionary entry
        """
        entry = self.find_wiktionary_entry(word)
        if entry is not None:
            return sorted(entry.keys())

    # PAGE PARSING
    # ------------
    def page_ipas(self, page):
        """
        Returns a list of strings of all IPAs from this Wiktionary page
        in BeautifulSoup.

        :param page: BeautifulSoup.Tag, Wiktionary page to fetch IPAs from
        :return: List[unicode], IPAs from this page
        """
        ipa_tags = [ipa for ipa in page.find_all("span", attrs={"class": "IPA"})
                    if ipa.find_parent("li") is not None]
        ipas = [self.clean_tag_ipa(ipa_tag) for ipa_tag in ipa_tags]
        ipas = OrderedSet(ipas).items()
        valid_ipas = [ipa for ipa in ipas if self.valid_ipa(ipa)]
        return valid_ipas

    def page_etymologies(self, page, lang=None):
        """
        Returns a list of etymological roots on this Wiktionary page
        in this language.

        :param page: BeautifulSoup.Tag, page to find etymology from
        :param lang: str, language of etymology
        :return: List[str], etymological roots on this page in this language
        """
        lang = self.verify_language(lang)
        num_roots = page.get_text().count("+") + 1
        etym_tags = page.find_all("i", attrs={"xml:lang": self.lang_code(lang)}, limit=num_roots)
        if len(etym_tags) == 0:
            etym_tags = page.find_all("i", attrs={"lang": self.lang_code(lang)}, limit=num_roots)
        if len(etym_tags) != num_roots or num_roots == 1:  # corrects for errors
            return list()
        etyms = [self.clean_text(self.remove_superscripts(etym_tag).get_text(" ")) for etym_tag in etym_tags]
        return etyms

    def page_siblings(self, page, start_headers=set(), end_headers=set(), lang=None):
        """
        Returns this tag's siblings between start_headers and end_headers.
        ~
        If lang is not None, ensures that start_header(s) text begins with
        this language.
        ~
        e.g. tag_siblings(Tag("<h1>Hi</h1><h2>my</h2><h3>good</h3><h1>friend</h1>"), {"h1"}, {"h1"}) ->
             [Tag("<h2>my</h2>"), Tag("<h3>good</h3>")]

        :param tag: Tag, BeautifulSoup Tag to retrieve children from
        :param start_headers: Set(str), header name(s) to start at
        :param end_headers: Set(str), header name(s) to stop at
        :param lang: Optional[str], language of entry to subtag
        :return: List[Tag], Tag's children between start_headers and stop_headers
        """
        head_tag = page.find(start_headers)
        if head_tag is not None:
            return self.tag_siblings(head_tag, end_headers=end_headers, lang=lang)
        else:
            return []

    def page_content(self, page):
        """
        Returns this Wiktionary page Tag's div bodyContent.

        :param page: Tag, HTML for Wiktionary page
        :return: Tag, page's div content
        """
        return page.find('div', attrs={'id': 'bodyContent', 'class': 'mw-body-content'})

    # TAG PARSING
    # -----------
    def tag_siblings(self, tag, start_headers=set(), end_headers=set(), lang=None):
        """
        Returns this tag's siblings between start_headers and stop_headers.
        ~
        If language is not None, ensures that start_header(s) text begins with
        given language.
        ~
        e.g. tag_siblings(Tag("<h1>Hi</h1><h2>my</h2><h3>good</h3><h1>friend</h1>"), {"h1"}, {"h1"}) ->
             [Tag("<h2>my</h2>"), Tag("<h3>good</h3>")]

        :param tag: Tag, BeautifulSoup Tag to retrieve children from
        :param start_headers: Set(str), header name(s) to start at
        :param end_headers: Set(str), header name(s) to stop at
        :param lang: Optional[str], language of entry to subtag
        :return: List[Tag], Tag's children between start_headers and stop_headers
        """
        curr_tag = tag
        next_sibling = curr_tag.nextSiblingGenerator()
        children = []
        matches_lang = lambda t: lang is None or t.find_child('span', attrs={'class': 'mw-headline',
                                                                                 'id': lang}) is not None

        if len(start_headers) != 0:
            while not (getattr(curr_tag, 'name', '') in start_headers and matches_lang(curr_tag)):
                try:
                    curr_tag = next(next_sibling)
                except StopIteration:
                    return children

        try:
            curr_tag = next(next_sibling)
        except StopIteration:
            return children

        end_header = lambda t: getattr(t, 'id', '') == "mw-navigation"

        if len(end_headers) != 0:
            while not (getattr(curr_tag, 'name', '') in end_headers or end_header(curr_tag)):
                if curr_tag is not None:
                    if str(curr_tag)[:4] == "<!--":
                        break
                    children.append(curr_tag)
                try:
                    curr_tag = next(next_sibling)
                except StopIteration:
                    break

        return children

    def soupify(self, tags):
        """
        Returns a BeautifulSoup page joining each Tag in tags, in rank.

        :param tags: List[Tag], BeautifulSoup Tags to join
        :return: Tag, tags joined into 1 page
        """
        return BeautifulSoup("\n".join([str(tag) for tag in tags]), "lxml")

    def soupify_siblings(self, tag, start_headers=set(), end_headers=set(), lang=None):
        """
        Returns the given tag's siblings as a new tag containing only
        its siblings from (any of) start_headers up to (any of) stop_headers.

        :param tag: Tag, BeautifulSoup Tag to retrieve children from
        :param start_headers: Set(str), header name(s) to start at
        :param end_headers: Set(str), header name(s) to stop at
        :param lang: Optional[str], language of entry to subtag
        :return: Tag, BeautifulSoup Tag with only this tag's children
        """
        return self.soupify(self.tag_siblings(tag, start_headers, end_headers, lang=lang))

    # TEXT CLEANUP / HELPERS
    # ----------------------
    def clean_text(self, text):
        """
        Returns the given text in unicode without HTML characters
        and with regular spacing.
        ~
        e.g. clean_text(" hi , how  are you ? ") -> "hi, how are you?"

        :param text: str, string to clean
        :return: unicode, cleaned unicode string
        """
        return self.clean_spaces(re.sub("&\S{3,10};", " ", str(text.replace(" ", ""))))

    def clean_punct(self, text):
        """
        Cleans the spacing around punctuation in the given text.

        :param text: str, text to clean punctuation spacing for
        :return: str, text with clean punctuation spacing
        """
        return text.replace(" ,", ",").replace("( ", "(").replace(" )", ")")

    def clean_ipa(self, ipa, scrub=False):
        """
        Returns the given IPA pronunciation with stress marks,
        syllable markers, and parentheses removed.
        ~
        If scrub is True, clean_ipa() also removes given ipa's diacritics.

        :param ipa: unicode, IPA to remove stress/syllable marks from
        :param scrub: bool, whether to also remove diacritics
        :return: unicode, given ipa with stress/syllable marks removed
        """
        cleaned = re.sub("[ˈˌ./›\"]", "", self.clean_word(ipa))
        if scrub:
            cleaned = self.remove_diacritics(cleaned)
        return cleaned

    def clean_tag_ipa(self, tag):
        tag_ipa = self.clean_text(self.remove_superscripts(tag).get_text()).replace(" ", "")
        return self.clean_ipa(self.remove_digits(tag_ipa.split("→")[0]))

    def clean_word(self, word):
        """
        Returns the given word in lowercase and with punctuation and
        whitespace removed.

        :param word: unicode, word to tag_text
        :return: unicode, cleaned word
        """
        return re.sub("[" + string.punctuation.replace("-", "") + "]", "", word.lower())

    def clean_header(self, header):
        """
        Returns this Wiktionary header title with [edit]
        stripped from the end.

        :param header: str, Wiktionary header to clean
        :return: str, cleaned Wiktionary header
        """
        return self.clean_text(header).split("[", 1)[0].strip()

    def clean_spaces(self, s):
        """
        Returns s with no more than 1 consecutive space and with
        whitespace stripped from ends.
        ~
        e.g. clean_spaces("  how  are   you  ") -> "how are you"

        :param s: str, string with spaces to tag_text
        :return: str, s cleaned
        """
        return self.clean_punct(self.space_pattern.sub(" ", s)).strip()

    def clean_parentheticals(self, s):
        """
        Returns s with all parentheticals removed.
        ~
        e.g. clean_parentheticals("cat (noun) - animal") -> "cat - animal"

        :param s: str, string to remove parentheticals frosm
        :return: str, s without parentheticals
        """
        last = s
        new = self.paren_pattern.sub("", s)
        while last != new:
            last = new
            new = self.paren_pattern.sub("", new)
        return new

    def clean_quotes(self, s):
        """
        Returns s with all quotes removed.
        ~
        e.g. clean_parentheticals("cat ("cat")") -> "cat ()"

        :param s: str, string to remove parentheticals from
        :return: str, s without parentheticals
        """
        return self.quote_pattern.sub("", s)

    def ipaize(self, s):
        return "".join([char for char in s if char in ALLSYMBOLS or char in ", "])

    def remove_digits(self, s):
        return "".join([char for char in s if not char.isdigit() and char not in "⁻⁽⁾ˀ"])

    def remove_parens(self, word):
        """
        Returns the given word with parentheses removed.

        :param word: unicode, word to remove parentheses from
        :return: unicode, word with parentheses removed
        """
        return re.sub("\(|\)", "", word)

    def remove_superscripts(self, tag):
        """
        Removes all superscript tags from the given BeautifulSoup Tag.

        :param tag: Tag, BeautifulSoup tag to remove superscripts from
        :return: Tag, tag with superscripts removed
        """
        try:
            tag.sup.decompose()
        except AttributeError:
            pass
        return tag

    def remove_sublists(self, tag):
        """
        Removes all sublist tags (i.e., ul and dl) from the given BeautifulSoup Tag.

        :param tag: Tag, BeautifulSoup tag to remove sublists from
        :return: Tag, tag with sublists removed
        """
        self.remove_superscripts(tag)
        try:
            tag.dl.decompose()
        except AttributeError:
            pass
        try:
            tag.ul.decompose()
        except AttributeError:
            pass
        try:
            tag.abbr.decompose()
        except AttributeError:
            pass
        return tag

    def remove_diacritics(self, ipa):
        """
        Returns the given IPA pronunciation with diacritics removed.

        :param ipa: unicode, IPA to remove stress/syllable marks from
        :return: unicode, given ipa with stress/syllable marks removed
        """
        return "".join([c for c in ipa if c not in IPADIACRITICS])

    def fill_list(self, lst, limit, item=None):
        """
        Adds item to given list until it reaches length limit.

        :param lst: List[X], list to fill with item
        :param limit: int, desired length of list
        :param item: X, item to fill list with
        :return: List[X], original list with item added until limit
        """
        return self.add_item(lst, limit - len(lst), item)

    def add_item(self, lst, times, item=None):
        """
        Adds the given item to the given list the given number of times.
        ~
        e.g. add_item([1,2,3], 2) -> [1,2,3,None,None]

        :param lst: List[X], list to add item to repeatedly
        :param times: int, number of times to add item
        :param item: X, item to add to given lst
        :return: List[X], lst with item added up to times
        """
        lst += [item] * times
        return lst

    def safe_execute(self, default, exception, function, *args):
        """
        Returns the result of the given function with the given arguments.
        If exception is raised, return default.

        :param default: Any, default value to return if exception
        :param exception: Exception, exception to catch
        :param function: function, function to safely execute
        :param args: Any, arguments of given function to execute
        :return: Any, output of given function or default if exception
        """
        try:
            return function(*args)
        except exception:
            return default

    def add_wikt_entry(self, word, lang, heading, content):
        try:
            entry = self.wiktionary_entries[word][lang][heading]
        except KeyError:
            self.wiktionary_entries.setdefault(word, dict())
            self.wiktionary_entries[word].setdefault(lang, dict())
            self.wiktionary_entries[word][lang].setdefault(heading, type(content)())
            entry = self.wiktionary_entries[word][lang][heading]

        if entry == content:
            return
        elif type(content) == str:
            if type(entry) == str:
                entry = [entry]
            entry.append(content)
        elif type(content) == list:
            entry += content
        else:
            if len(entry) == 0:
                entry.update(content)
            else:
                for header in content:
                    wikt_content = entry[header]
                    new_content = content[header]

                    if type(new_content) == str:
                        if type(wikt_content) == str:
                            wikt_content = list(wikt_content)
                        wikt_content.append(new_content)
                    elif type(new_content) == list:
                        wikt_content.extend(new_content)

                    entry[header] = wikt_content

        self.wiktionary_entries[word][lang][heading] = entry

    def add_wikt_entries(self, word, lang, headings, contents):
        for i in range(len(headings)):
            self.add_wikt_entry(word, lang, headings[i], contents[i])


class WiktionaryPage:
    """
    A class for parsing Wiktionary pages into language data.
    ~
    Automatically adds data from all WiktionaryPages to its parent
    WiktionaryParser's wiktionary_entries.
    """
    def __init__(self, word, lang=None, parser=None):
        if parser is None:
            self.parser = WiktionaryParser()
        else:
            self.parser = parser
        self.word = word
        self.page = self.word_page(word, lang)
        self.entry = self.page_entry(self.page, lang)
        self.add_wikt_entry(self.word, self.entry)

    def add_wikt_entry(self, word, entry):
        print("adding", word, "to wikt with entry", entry)
        langs = list(entry.keys())
        for lang in langs:
            lang_contents = entry[lang]
            headings = list(lang_contents.keys())
            contents = list(lang_contents.values())
            self.parser.add_wikt_entries(word, lang, headings, contents)

    def word_page(self, word, language):
        """
        Returns a BeautifulSoup Tag corresponding to the Wiktionary
        page for this word in this language.

        :param word: str, word to retrieve page for
        :return: Tag, BeautifulSoup tag matching given word's page
        """
        language = self.parser.verify_language(language)
        nuwords = [word, word.lower(), word.title()]

        # check eng wikt 1st
        for nuword in nuwords:
            page = self.parser.word_page(nuword, eng=True)
            if self.parser.valid_page(page, language, eng=True):
                return page

        # if word not in eng wikt, check native wikt
        for nuword in nuwords:
            page = self.parser.word_page(nuword, eng=False)
            # if in native wikt, iterate over sublemmas until finding sublemma in eng wikt
            if self.parser.valid_page(page, language, eng=False):
                return page

    def desired_header(self, header):
        return header.split("_", 1)[0] in self.parser.HEADER_NAMES

    def page_entry(self, page, lang=None):
        """
        Returns a dict for the word entry for this Wiktionary page.
        If lang is None, returns entry for all languages on this page.
        Otherwise, returns entry in given language.

        :param page: Tag, HTML Wiktionary page to extract entry from
        :param lang: str, language of page entry to retrieve
        :return: dict(str, dict), where...
            key (str) - entry language
            val (dict) - entry content
        """
        entries = dict()

        if page is not None:
            entry_headers = {"h3", "h4", "h5"}
            tags = page.find_all("span", attrs={"class": "mw-headline", "id": self.desired_header})

            for tag in tags:
                header_lang = self.header_lang(tag)
                if lang is None or lang == header_lang:
                    tag = tag.find_parent(entry_headers)
                    if tag is not None:
                        heading = self.subtag(tag, stop_headers=entry_headers)

                        if heading is not None:
                            header_name = self.header_text(tag)
                            heading_entry = self.heading_entry(heading, header_name, header_lang)

                            if heading_entry is not None and len(heading_entry) != 0:
                                entries.setdefault(header_lang, dict())
                                if header_name in self.parser.PARTS_OF_SPEECH:
                                    entries[header_lang].setdefault(header_name, dict())
                                    entries[header_lang][header_name].update(heading_entry)
                                elif self.is_header_declension(header_name):
                                    entries[header_lang][header_name] = heading_entry
                                else:
                                    entries[header_lang].setdefault(header_name, list())
                                    subentry = entries[header_lang][header_name] + heading_entry
                                    new_entry = OrderedSet(subentry).order_items()
                                    entries[header_lang][header_name] = new_entry
                elif header_lang == "":
                    continue
                elif header_lang[:10] == "Navigation":
                    break

        return entries

    def is_header_declension(self, header):
        return header[:6] == "Inflec" or header[:6] == "Declen" or header[:6] == "Conjug"

    def header_text(self, header):
        """
        Returns the given Wiktionary header's text, with
        [edit] stripped from the end.

        :param header: Tag, HTML header to extract text from
        :return: str, Wiktionary header's text
        """
        text = getattr(header, 'text', '')
        return self.parser.clean_header(text)

    def header_lang(self, heading):
        """
        Finds and returns the given Wiktionary heading's
        language.

        :param heading: Tag, HTML tag to find language for
        :return: str, name of heading's language header
        """
        return self.header_text(heading.find_previous("h2"))

    def subpage(self, page, start_headers=set(), stop_headers=set(), lang=None):
        """
        Returns the given Wiktionary HTML Tag page as a new Tag
        with contents between start_headers and stop_headers.
        ~
        If language is None, returns first subtag between start_headers
        and stop_headers.  Otherwise, extracts language from tag first and then
        performs subtag on that language's Wiktionary entry.

        :param page: Tag, HTML to extract new Tag from
        :param start_headers: Set(str), headers to begin new tag at
        :param stop_headers: Set(str), headers to end new tag at
        :param lang: Optional[str], language of entry to subtag
        :return: Tag, this Tag's contents from start_headers up to stop_headers
        """
        page = self.parser.page_content(page)
        tags = [t for t in page.find_all(start_headers) if t.find('span', attrs={'id': lang}) is not None or
                (lang is None and t.find('span', attrs={'id': self.parser.LANG_CODES}))]
        if len(tags) != 0:
            return self.parser.soupify_siblings(tags[0], end_headers=stop_headers, lang=lang)

    def subtag(self, tag, start_headers=set(), stop_headers=set(), lang=None):
        """
        Returns the given Wiktionary HTML Tag as a new Tag
        with contents between start_headers and stop_headers.
        ~
        If language is None, returns first subtag between start_headers
        and stop_headers.  Otherwise, extracts language from tag first and then
        performs subtag on that language's Wiktionary entry.

        :param tag: Tag, HTML to extract new Tag from
        :param start_headers: Set(str), headers to begin new tag at
        :param stop_headers: Set(str), headers to end new tag at
        :param lang: Optional[str], language of entry to subtag
        :return: Tag, this Tag's contents from start_headers up to stop_headers
        """
        return self.parser.soupify_siblings(tag, start_headers, stop_headers, lang=lang)

    def tag_text(self, tag):
        """
        Returns the given Wiktionary HTML tag's text.

        :param tag: Tag, BeautifulSoup tag in HTML containing text
        :return: str, this Tag's text
        """
        if tag is None:
            return
        else:
            return self.parser.clean_text(self.parser.remove_sublists(tag).get_text(" "))

    def tag_comparables(self, tag):
        comparables = dict()
        if tag is not None:
            has_link = tag.find('a', attrs={'title': 'Appendix:Glossary'})
            if has_link is not None:
                curr_tag = tag
                while curr_tag is not None:
                    curr_tag = curr_tag.find_next_sibling('i')
                    comp_text = self.tag_text(curr_tag)
                    if curr_tag is None:
                        break
                    curr_tag = curr_tag.find_next_sibling('b')
                    val_text = self.tag_text(curr_tag)
                    curr_comp = comparables.setdefault(comp_text, list())
                    if val_text not in curr_comp:
                        curr_comp.append(val_text)
        return comparables

    def tag_sentences(self, tag):
        sentences = list()
        if tag.find('dl') is not None:
            tag_sents = tag.find_all('dd')
            if tag_sents is not None:
                for tag_sent in tag_sents:
                    sent_text = self.tag_text(tag_sent)
                    if len(sent_text) != 0 and sent_text not in sentences:
                        sentences.append(sent_text)
                        ital_tag = tag_sent.find('i')
                        if ital_tag is not None:
                            ital_text = self.tag_text(ital_tag)
                            if sent_text != ital_text and ital_text not in sentences and len(ital_text) != 0:
                                sentences.append(ital_text)
        return sentences

    def tag_lemma(self, tag):
        """
        Returns this HTML tag's first lemma, i.e. text
        from span with class=mention or class=form-of-definition-link.
        ~
        Used for retrieving lemmas from parts-of-speech definitions.

        :param tag: Tag, BeautifulSoup HTML to extract lemma from
        :return: str, lemma from given tag
        """
        lemma = tag.find("span", attrs={"class": ["mention", "form-of-definition-link"]})
        lemma_text = self.tag_text(lemma)
        return lemma_text

    def english_tag_lemmas(self, tag):
        """
        Returns a list of all English lemmas linked to in this Tag.

        :param tag: Tag, HTML containing English lemma links
        :return: List[str], English lemmas linked in tag
        """
        english_lexicon = self.parser.find_lexicon("English")
        links = tag.find_all("a", attrs={"title": english_lexicon})
        lemmas = [link.get("title") for link in links
                  if "#" not in link.get("href") and link.parent.name == "li"]
        return lemmas

    def tags_texts(self, tags):
        return [self.tag_text(tag) for tag in tags]

    def tag_glossary_terms(self, tag):
        gloss_terms = tag.find_all('a', attrs={'title': 'Appendix:Glossary'})
        paren_tag = tag.find('span', attrs={'class': 'ib-content'})
        if paren_tag is not None:
            gloss_terms += paren_tag.find_all('a')
        return self.tags_texts(gloss_terms)

    def tag_lemmas(self, tag, lang=None):
        """
        Returns all this HTML tag's lemmas, i.e. text
        from span with class=mention or class=form-of-definition-link.
        ~
        Used for retrieving lemmas from parts-of-speech definitions.

        :param tag: Tag, BeautifulSoup HTML to extract lemma from
        :param lang: str, language of lemmas
        :return: List[str], lemmas from given tag
        """
        lang = self.parser.verify_language(lang)

        if tag is not None:
            lemmas = tag.find_all("span", attrs={"class": ["mention", "form-of-definition-link"]})

            if lang == "English":
                is_en = lambda h: h is not None and h[:6] == '/wiki/' and '#' not in h
                lang_tags = tag.find_all('a', attrs={'href': is_en})
                lang_tags = [l for l in lang_tags if l.find_parent("span", attrs={"class": "ib-content"}) is None]
            else:
                lang_tags = tag.find_all(attrs={"lang": self.parser.LANG_CODES.get(lang, None)})
                is_lang = lambda h: h[-len(lang):] == lang
                lang_tags += tag.find_all('a', attrs={'href': is_lang})

            lemmas += lang_tags

            if len(lemmas) != 0:
                lemmas_text = OrderedSet(self.tags_texts(lemmas)).items()
                return lemmas_text

        return []

    def text_lemmas(self, text):
        """
        Returns all lemmas in this text from an HTML tag.
        ~
        Used for retrieving lemmas from parts-of-speech definitions.

        :param text: str, BeautifulSoup HTML to extract lemma from
        :return: List[str], lemmas from text
        """
        split_text = re.split("[;,]", text)
        lemmas = list()
        for st in split_text:
            lemma = st.strip()
            if " " not in lemma:
                lemmas.append(lemma)
        return lemmas

    def word_tag_definitions(self, word_tag, lang=None):
        """
        Returns a dict for this word_tag's head word, definitions,
        and each definition's lemmas in this language and English.

        with head word as the first item in the list and
        definitions following.
        ~
        e.g. -> [("driven (comparative more driven, superlative most driven)", "driven"),
                 ("Obsessed; passionately motivated to achieve goals.", None),
                 ("(of snow) Formed into snowdrifts by wind.", None)]

                 {'head': 'driven',
                 'definitions': ["driven (comparative more driven, superlative most driven)",
                                 "Obsessed; passionately motivated to achieve goals.",
                                 "(of snow) Formed into snowdrifts by wind."],
                 'lemmas': {'English': ['driven',
                                        'obsessed']},
                 'terms': []}

             -> [("is", None),
                 ("plural of i", "i"),
                 ("third-person singular present of be", "be")]

        :param word_tag: Tag, HTML to retrieve word definitions from
        :param lang: str, language of definitions
        :return: dict(str, list/dict), where...
            key (str) - name of definition part; one of:
                'head' - the key word given by Wiktionary
                'definitions' - each meaning of the head word
                'lemmas' - lemmas extracted from definitions
                'terms' - glossary terms relevant to this word
        """
        lang = self.parser.verify_language(lang)
        word_tag = self.parser.remove_sublists(word_tag)
        subdefns = word_tag.find_all("li")
        head = self.tag_text(word_tag.find("strong"))
        defns = {'head': head, 'definitions': list(), 'lemmas': {lang: OrderedSet([]),
                                                                 'English': OrderedSet([])},
                 'terms': list()}
        comparables = self.tag_comparables(word_tag.find('p'))
        if len(comparables) != 0:
            defns['comparables'] = comparables
        sentences = self.tag_sentences(word_tag)
        if len(sentences) != 0:
            defns['sentences'] = sentences

        if head is not None:
            self.word = head

        for subdefn in subdefns:
            defn = self.tag_text(subdefn)
            if len(defn) != 0:
                defns['definitions'].append(defn)

            lemmas = self.tag_lemmas(subdefn, lang)

            if len(lemmas) == 0:
                lemmas = self.tag_lemmas(subdefn, 'English')
                if len(lemmas) != 0:
                    language = 'English'
                else:
                    continue
            else:
                language = lang

            lemmas = [self.parser.clean_parentheticals(l) for l in lemmas if l is not None and l != ""]
            defns['lemmas'][language].update(lemmas)
            defns['terms'].extend(self.tag_glossary_terms(subdefn))

        defns['lemmas'][lang] = defns['lemmas'][lang].items()
        if type(defns['lemmas']['English']) == OrderedSet:
            defns['lemmas']['English'] = defns['lemmas']['English'].items()
        defns['terms'] = OrderedSet.remove_duplicates(defns['terms'])

        return defns

    def pos_tag_definitions(self, pos_tag, lang=None):
        """
        Returns this part-of-speech tag's definition-lemma pairs,
        with head word as the first item in the list and
        definitions following.
        ~
        e.g. -> [("driven (comparative more driven, superlative most driven)", "driven"),
                 ("Obsessed; passionately motivated to achieve goals.", None),
                 ("(of snow) Formed into snowdrifts by wind.", None)]

             -> [("is", None),
                 ("plural of i", "i"),
                 ("third-person singular present of be", "be")]

        :param pos_tag: Tag, HTML to retrieve pos definitions from
        :param lang: str, language of definitions
        :return: List[2-tuple], pos_tag's definition-lemma pairs
        """
        pairs = list()
        pos_tag = self.parser.remove_sublists(pos_tag)
        subtags = pos_tag.find_all(["strong", "li"])

        for subtag in subtags:
            print("SUBTAG'S NAME IS", subtag.get('name'))
            if subtag.get('name') == 'strong':
                print("FOUND A HEADWORD")
                descriptors = subtag.find_next_siblings("i")
                lexemes = subtag.find_next_siblings("b")
                print([self.tag_text(d) for d in descriptors])
                print([self.tag_text(l) for l in lexemes])
            defn = self.tag_text(subtag)
            lemmas = self.tag_lemmas(subtag, lang)
            if defn != "" and len(lemmas) != 0:
                for lemma in lemmas:
                    lemma = None if lemma is None or lemma == "" else self.parser.clean_parentheticals(lemma)
                    pair = (defn, lemma)
                    pairs.append(pair)

        return pairs

    def tag_declension(self, tag, lang, simple=False, root_only=True):
        """
        Returns the declension of the word for this tag
        in this language.
        ~
        If simple is True, returns a list of words. Otherwise,
        returns a dict including column and row names.
        ~
        If root_only is True, returns declension only if this tag's
        word is the root for all inflections.  Otherwise, returns
        declension if this tag's word occurs as any inflection.

        :param tag: Tag, HTML tag containing inflections table
        :param lang: str, language of tag content
        :param simple: bool, whether tag inflections are simple
        :param root_only: bool, whether to return declension only for root words
        :return: dict(str, dict), where str is column name and dict is...
            key (str) - row name
            val (list) - cell values for given column and row
        """
        if tag is not None:
            wikt_table = WiktionaryTable(tag, lang, self)
            simple_inflections = wikt_table.get_simple_inflections()
            if len(simple_inflections) != 0:
                is_root = simple_inflections[0] == self.word

                if simple:
                    if root_only:
                        if is_root:
                            return simple_inflections
                        else:
                            return list()
                    else:
                        return simple_inflections
                else:
                    inflections = wikt_table.inflections
                    if root_only:
                        if is_root:
                            return inflections
                        else:
                            return dict()
                    else:
                        return inflections

    def heading_entry(self, content, header, language):
        """
        Parses a Wiktionary entry from this HTML content
        with this header name and language.

        :param content: Tag, HTML containing entry content
        :param header: str, header name of entry
        :param language: str, language of heading content
        :return: list, parsed entry content
        """
        if header[:4] == "Etym":
            entry = self.parser.page_etymologies(content, language)
        elif header[:6] == "Pronun":
            entry = self.parser.page_ipas(content)
        elif self.is_header_declension(header):
            entry = self.tag_declension(content, language, simple=False)
        elif header.replace("_", " ") in self.parser.PARTS_OF_SPEECH:
            entry = self.word_tag_definitions(content, language)
        else:
            entry = list()

        return entry


class WiktionaryTable:
    """
    A class for parsing Wiktionary pages into language data.
    """
    def __init__(self, table, lang, wikt_page):
        self.language = lang
        self.wikt_page = wikt_page
        self.table = self.tag_table(table, self.language)
        if self.table is not None:
            self.rows = self.table_rows(self.table)
            self.num_rows = len(self.rows)
            self.num_cols = self.count_cols(self.table)
        self.inflections = None

    def get_simple_inflections(self):
        """
        Returns a list of all words in this WiktionaryTable's table.

        :return: List[str], words in this WT's table
        """
        contents = list()
        table_cells = self.table_content(self.table)

        for cell in table_cells:
            cell = self.wikt_page.parser.remove_sublists(cell)
            cell_txt = cell.get_text("").rstrip("\n")
            if len(cell_txt) != 0 and not self.wikt_page.parser.is_punct(cell_txt):
                contents += self.split_cell_text(cell_txt)
        return contents

    def inflections(self):
        if self.inflections is None:
            self.inflections = self.parse_inflections(self.table, self.language)
        return self.inflections

    def is_header(self, cell):
        """
        Returns True if the given cell is a (row or column) header,
        False otherwise.

        :param cell: Tag, BeautifulSoup cell in table to check if header
        :return: bool, whether given cell is a (row or column) header
        """
        return cell.name == 'th' if cell is not None else False

    def is_content(self, cell):
        """
        Returns True if the given cell is a cell containing content,
        False otherwise.

        :param cell: Tag, BeautifulSoup cell in table to check if content
        :return: bool, whether given cell contains content
        """
        if cell is not None:
            if cell.name == "td":
                return self.valid_content(cell)
            elif cell.name == "th":
                return self.contains_content(cell)

        return False

    def valid_content(self, cell):
        """
        Returns True if the content in the given cell is valid,
        i.e., not empty, beginning with a superscript, or containing a
        paragraph.

        :param cell: Tag, HTML cell in table to check whether containing valid content
        :return: bool, whether given cell contains valid content
        """
        try:
            first_item = cell.contents[0]
        except (AttributeError, IndexError):
            first_item = cell
        # cell not valid if empty, begins w/ superscript, or has paragraph
        return (not self.is_cell_empty(cell)) and getattr(first_item, 'name', None) != "sup" and cell.find("p") is None

    def contains_content(self, tag):
        """
        Returns True if the given HTML tag contains language content,
        False otherwise.

        :param tag: Tag, BeautifulSoup Tag to ask if it contains content
        :return: bool, True if tag contains content and False otherwise
        """
        matches_href = lambda t: t[-len(self.language):] == self.language
        tag_link = tag.find("a", attrs={'href': matches_href})
        return tag_link is not None

    def is_cell_empty(self, cell):
        """
        Returns True if this cell contains no inflections data,
        False otherwise.

        :param cell: Tag, BeautifulSoup tag for cell in HTML table
        :return: bool, whether this cell is empty
        """
        if cell is None:
            return True
        else:
            cell_text = cell.get_text()
            return cell_text is None or cell_text == "—"

    def is_col_empty(self, col):
        """
        Returns True if this HTML column is empty and takes up
        a whole row, False otherwise.

        :param col: Tag, BeautifulSoup Tag for column in table
        :return: bool, whether this column is empty
        """
        return self.cell_rowspan(col) >= self.num_rows and col.get("text") is None

    def cell_rowspan(self, cell):
        """
        Returns this BeautifulSoup Tag cell's rowspan.
        ~
        If cell has no rowspan, returns 1.

        :param cell: Tag, BeautifulSoup tag to get rowspan of
        :return: int, rowspan of given cell
        """
        return int(cell.get("rowspan", 1))

    def cell_colspan(self, cell):
        """
        Returns this BeautifulSoup Tag cell's colspan.
        ~
        If cell has no colspan, returns 1.

        :param cell: Tag, BeautifulSoup tag to get colspan of
        :return: int, colspan of this cell
        """
        return int(cell.get("colspan", 1))

    def content_text(self, spans):
        """
        Returns a newline-joined str of text for all content in spans.

        :param spans: List[Tag], HTML tags for content in a cell
        :return: str, text from content in spans
        """
        spans_text = [self.wikt_page.tag_text(span) for span in spans]
        text = "\n".join(spans_text)
        return text

    def cell_contents(self, cell, language):
        """
        Returns the given cell (from a table)'s text contents.

        :param cell: Tag, BeautifulSoup tag for cell in HTML table
        :return: List[str], given cell's text contents
        """
        try:
            cell = self.wikt_page.parser.remove_sublists(cell)
            spans = cell.find_all("span", lang=self.wikt_page.parser.LANG_CODES[language])
            if len(spans) != 0:
                return [self.wikt_page.tag_text(span) for span in spans]
        except (AttributeError, KeyError):
            pass
        return []

    def cell_text(self, cell, language):
        """
        Returns the given cell (from a table)'s text.

        :param cell: Tag, BeautifulSoup tag for cell in HTML table
        :return: str, given cell's text
        """
        try:
            cell = self.wikt_page.parser.remove_sublists(cell)
            spans = cell.find_all("span", lang=self.wikt_page.parser.LANG_CODES[language])
            text = self.wikt_page.tag_text(cell) if len(spans) == 0 else self.content_text(spans)
            return self.wikt_page.parser.clean_text(text)
        except AttributeError:
            return ""

    def header_text(self, cell):
        """
        Returns this header cell (from a table)'s text.

        :param cell: Tag, BeautifulSoup tag for cell in HTML table
        :return: str, given cell's text
        """
        return self.wikt_page.parser.clean_text(cell.get_text(" "))

    def cell_content(self, cell, language):
        if self.is_content(cell):
            return self.cell_entry(cell, language)

    def split_cell_text(self, text):
        delimiters = re.compile("[,/\n]")
        entry = [e.strip() for e in delimiters.split(text)]
        return entry

    def cell_entry(self, cell, language):
        """
        Returns a list of the words in this cell.

        :param cell: Tag, BeautifulSoup tag for cell in HTML table
        :return: List[str], list of words in this cell
        """
        text = self.cell_text(cell, language)

        if len(text) != 0:
            return self.split_cell_text(text)
        else:
            return list()

    def cell_rows(self, coord, table_dict):
        """
        Returns a tuple of the given coordinate
        from the given table_dict's row names.

        :param coord: Tuple(int, int), coordinate to get row names for
        :param table_dict: dict[tuple, Tag], where...
            key (Tuple[int, int]) - table_dict's row and column number
            val (Tag) - cell for row and column
        :return: Tuple(str), given cell's row names
        """
        row_num, col_num = coord
        sorted_dict = sorted(table_dict)
        prev_rows = [c for c in sorted_dict if c[0] == row_num
                     and c[1] < col_num]
        num_rows, num_cols = sorted_dict[-1]
        rows = []
        header_yet = False

        # iterate over previous rows to find closest set of headers
        for row_coord in reversed(prev_rows):
            cell = table_dict[row_coord]
            if self.is_header(cell):
                text = self.header_text(cell)
                if self.cell_rowspan(cell) <= num_rows and len(text) != 0:
                    if text not in rows:
                        header_yet = True
                        rows.insert(0, text)
            elif header_yet:
                break

        return tuple(rows)

    def cell_cols(self, coord, table_dict):
        """
        Returns a tuple of the given coordinate
        from the given table_dict's column names.

        :param coord: Tuple(int, int), coordinate to get row names for
        :param table_dict: dict[tuple, Tag], where...
            key (Tuple[int, int]) - given table's row and column number
            val (Tag) - cell for given row and column
        :return: Tuple(str), given cell's column names
        """
        row_num, col_num = coord
        sorted_dict = sorted(table_dict)
        prev_cols = [c for c in sorted_dict if c[1] == col_num
                     and c[0] < row_num]
        cols = []
        header_yet = False

        # iterate over previous columns to find closest set of headers
        for col_coord in reversed(prev_cols):
            cell = table_dict[col_coord]
            if self.is_header(cell):
                text = self.header_text(cell)
                if self.cell_colspan(cell) < self.num_cols and len(text) != 0:
                    header_yet = True
                    cols.insert(0, text)
            elif header_yet:
                break

        return tuple(cols)

    def is_table_inflection(self, table, language):
        """
        Returns True if this table is an inflection in the given language,
        False otherwise.

        :param table: Tag, Tag, BeautifulSoup tag for HTML table
        :param language: str, language of table
        :return: bool, whether given table is inflection
        """
        cells = self.table_content(table)
        links = [cell.find("a") for cell in cells if cell.find("a") is not None]
        hrefs = [link.get("href") for link in links if link.get("href") is not None]
        all_langs = all([href[-len(language):] == language.replace(" ", "_") or
                         href[-9:] == "redlink=1" for href in hrefs])
        return all_langs

    def table_cells(self, table):
        """
        Returns all cells from the given HTML table.

        :param table: Tag, BeautifulSoup tag for an HTML table
        :return: List[Tag], tags for all cells in given table
        """
        return table.find_all(["td", "th"])

    def table_content(self, table):
        """
        Returns all content cells from the given table.

        :param table: Tag, BeautifulSoup tag for an HTML table
        :return: List[Tag], tags for content cells in given table
        """
        if table is not None:
            cells = table.find_all("td")
            if cells is not None:
                return [cell for cell in cells if self.is_content(cell)]
        return []

    def table_rows(self, table):
        """
        Returns the given table separated into rows.

        :param table: Tag, BeautifulSoup tag to get rows of
        :return: List[Tag], rows of given table
        """
        try:
            # find hidden rows first
            rows = table.find_all("tr", attrs={"class": "vsHide"})
            if len(rows) != 0:
                return rows
            else:  # if no hidden rows, return all rows
                return table.find_all("tr")
        except AttributeError:
            return list()

    def tag_table(self, tag, language):
        """
        Returns the inflectional table for the word
        for this HTML tag in this language.

        :param tag: Tag, HTML tag containing inflection table
        :param language: str, language of inflectional table
        :return: Tag, inflection table from tag in language
        """
        infl_tables = tag.find_all('table', attrs={'class': 'wikitable inflection-table'})

        if len(infl_tables) != 0:
            return infl_tables[0]
        else:
            tables = tag.find_all('table')
            for table in tables:
                prev_header = tag.find_previous_sibling('h4')
                lang_header = tag.find_previous_sibling('h2')  # if None, assume table already in language
                is_in_language = lang_header is None or lang_header[:len(language)] == language
                if prev_header is not None and is_in_language:
                    if self.wikt_page.is_header_declension(prev_header.get_text()):
                        return table
            else:
                if len(tables) != 0:
                    return tables[0]
                else:
                    return

    def count_cols(self, table):
        """
        Returns the number of columns in this HTML table.

        :param table: Tag, BeautifulSoup table in HTML from webpage
        :return: int, number of columns in given table
        """
        num_cols = 0

        try:
            row1 = table.find("tr")
            cells = row1.find_all(["th", "td"])  # all headers/cells in 1st row
        except AttributeError:
            return 0

        for cell in cells:
            colspan = self.cell_colspan(cell)
            num_cols += colspan

        return num_cols

    def num_col_headers(self, table):
        """
        Returns the number of header columns in this HTML table.

        :param table: Tag, BeautifulSoup table in HTML from webpage
        :return: int, number of header columns in table
        """
        num_cols = 0
        row1 = table.find("tr")

        try:
            headers = row1.find_all("th")  # all headers in 1st row
        except AttributeError:
            return 0

        if headers is None:
            return 0

        for header in headers:
            colspan = self.cell_colspan(header)
            num_cols += colspan

        return num_cols

    def parse_table(self, table):
        """
        Returns a dictionary representing the given table.

        :param table: Tag, BeautifulSoup tag for an HTML table
        :return: dict[tuple, Tag], where...
            key (tuple[int, int]) - given table's row and column number
            val (Tag) - cell for given row and column
        """
        table_dict = dict()

        if table is not None:
            num_cols = self.num_cols
            row_range = range(self.num_rows)
            row_iter = iter(row_range)

            for r in row_iter:
                row = self.rows[r]
                cells = self.table_cells(row)
                cells_iter = iter(cells)
                col_range = range(num_cols)
                col_iter = iter(col_range)

                for c in col_iter:
                    coord = r, c

                    try:
                        cell = next(cells_iter)
                    except StopIteration:
                        continue
                    else:
                        # skip empty columns
                        while self.is_col_empty(cell):
                            try:
                                cell = next(cells_iter)
                            except StopIteration:
                                break

                        if self.is_col_empty(cell):
                            col_range = col_range[:-1]
                            num_cols -= 1
                            continue

                    while coord in table_dict:
                        try:
                            next(col_iter)
                            c += 1
                        except StopIteration:
                            try:
                                next(row_iter) #row_iter.__next__()
                                r += 1
                            except StopIteration:
                                break

                        coord = r, c
                    else:
                        rowspan = self.cell_rowspan(cell)
                        colspan = self.cell_colspan(cell)
                        rowspan = min(rowspan, self.num_rows)
                        colspan = min(colspan, num_cols)

                        if colspan != 1 or rowspan != 1:
                            rs = 0

                            while rs < rowspan:
                                coord = r + rs, c
                                table_dict[coord] = cell
                                cs = 1

                                while cs < colspan:
                                    coord = r + rs, c + cs
                                    table_dict[coord] = cell
                                    cs += 1
                                rs += 1

                            for i in range(1, colspan):
                                try:
                                    next(col_iter)
                                    #col_iter.next()
                                except StopIteration:
                                    break

                            continue
                        else:
                            table_dict[coord] = cell

        return table_dict

    def parse_inflections(self, table, language):
        """
        Returns an inflection dictionary for the given table.
        ~
        If table has multiple columns or rows, this method adds
        all column/row names in a tuple.

        :param table: Tag, BeautifulSoup table
        :return: dict(str, dict), where...
            key (str) - inflection column (i.e., plural or sing.)
            val (dict[str, list]) - inflection row (e.g., nominative) &
                list of words for given row & column
        """
        coords = self.parse_table(table)
        #self.visualize_inflections(coords)
        sorted_coords = sorted(coords)
        inflections = dict()
        line_names = lambda line: [l for l in line
                                  if len(line) > 0 and "—" not in l and
                                  not self.wikt_page.parser.is_punct(l)]

        for coord in sorted_coords:
            cell = coords[coord]
            if self.is_content(cell) and self.cell_colspan(cell) <= self.num_cols:
                rows_lst = self.cell_rows(coord, coords)
                cols_lst = self.cell_cols(coord, coords)
                row_names = line_names(rows_lst)
                col_names = line_names(cols_lst)
                entry = self.cell_entry(cell, language)

                if len(entry) > 0:
                    if (len(row_names) > 0 or len(col_names) > 0) or self.num_rows-self.num_cols == 1:
                        cols_rows = col_names + row_names  # nest dicts w/ columns on outside, rows on inside
                        curr_dict_loc = inflections

                        for i in range(len(cols_rows)):
                            cr = cols_rows[i]
                            if i < len(cols_rows) - 1:
                                init_type = dict
                            else:
                                init_type = list  # list @ bottom of nest
                            if init_type == list and type(curr_dict_loc) == list:
                                return self.get_simple_inflections()
                            else:
                                curr_dict_loc = curr_dict_loc.setdefault(cr, init_type())

                        try:
                            curr_dict_loc += OrderedSet(entry).items()
                        except TypeError:
                            return self.get_simple_inflections()

        return inflections

    def visualize_inflections(self, inflections):
        """
        Prints the given inflections to the user as a table.

        :param inflections: dict[tuple], row-col int keys with cell values
        :return: None
        """
        if len(inflections) != 0:
            bold = '\033[1m'
            end_bold = '\033[0m'

            inflections_len = len(max(inflections.values(), key=lambda v: len(v.text)).text)
            max_row, max_col = sorted(inflections)[-1]
            row_digits = len(str(max_row))
            width_padding = 5
            col_width = inflections_len + width_padding
            col_intro = " " * int(col_width * 1.25)  # begin just after 1 for centred spacing
            col_space = " " * col_width

            print("Inflections:\n", bold + col_intro + col_space.join([str(i) for i in range(max_col + 1)]) + end_bold)

            for coord in sorted(inflections):
                x, y = coord
                val = inflections[coord]
                text = self.wikt_page.parser.clean_text(val.get_text(" "))
                offset = col_width - len(text)
                if y == 0:
                    print("\n", bold + str(coord[0]).zfill(row_digits) + end_bold + col_space, end="")

                is_header = self.is_header(val)
                if is_header:
                    text = bold + text + end_bold
                print(text + (" " * offset), end="")
            print()


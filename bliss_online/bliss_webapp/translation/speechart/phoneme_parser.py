# coding: utf-8
"""
IPA_PARSER:

    Contains PhonemeParser class for parsing IPA pronunciation data.
"""
from main.bliss_web.bliss_app.bliss_webapp.blisscribe_py.speechart.language_parser import *


class PhonemeParser(LanguageParser):
    """
    A class for parsing IPA data from Wiktionary in a given language.
    """
    def __init__(self, language):
        LanguageParser.__init__(self, language)
        self.ipas = set()        # this language's IPA symbols
        self.vowels = OrderedSet([])
        self.consonants = OrderedSet([])
        self.phoneme_dict = {}

    def merge_dicts(self, first, other):
        """
        Merges the first dict with the other dict.

        :param first: dict, to merge with other, where...
            key (X)
            val (OrderedSet(X))
        :param other: dict, to merge with first, where...
            key (X)
            val (OrderedSet(X))
        :return: dict, first merged with other, where...
            key (X)
            val (OrderedSet(X))
        """
        first = {phoneme: first[phoneme].union(other.pop(phoneme).pop(phoneme))
                 for phoneme in first if phoneme in other}
        first.update(other)
        return first

    # HOMOPHONES
    # ----------
    def nearest_homophones(self, word, language):
        """
        Returns the nearest homophones in the given language
        to the given word in this PhonemeParser's native language.

        :param word: str, word in PhonemeParser's native language
        :param language: str, language of desired output homophones
        :return: List[str], homophones for word in given language
        """
        word_ipas = self.word_ipas(word, self.language)
        word_ipas = [self.clean_ipa(word_ipa, scrub=True) for word_ipa in word_ipas]
        homophones = list()

        if len(word_ipas) != 0:
            foreign = self.all_ipas(language)

            for word_ipa in word_ipas:
                homophone = None

                for fw in foreign:
                    ipas = foreign[fw]

                    if len(ipas) != 0:
                        ipa = self.clean_ipa(ipas[0], scrub=True)
                        if homophone is None:
                            homophone = IPAWord(fw, language, parser=self)
                            continue
                        homo = self.nearer_homophone(word_ipa, homophone.get_cleaned_ipa(), ipa)
                        if homo == ipa:
                            homophone = IPAWord(fw, language, parser=self)
                        if word_ipa == ipa:
                            break

                if homophone is not None:
                    homophones.append(homophone.word)

        if len(homophones) == 0:
            homophones.append(None)

        return homophones

    def nearest_homophone(self, word, language):
        """
        Returns the nearest homophone in the given language
        to the given word in this PhonemeParser's native language.
        ~
        e.g. nearest_homophone("droit", "English") -> "draw"

        :param word: str, word in PhonemeParser's native language
        :param language: str, language of desired output homophone
        :return: str, homophone for word in given language
        """
        word_ipa = self.word_ipa(word)
        homophone = None

        if word_ipa is not None:
            word_ipa = self.clean_ipa(word_ipa, scrub=True)
            foreign = self.all_ipas(language)

            for fw in foreign:
                ipas = foreign[fw]

                if len(ipas) != 0:
                    ipa = self.clean_ipa(ipas[0], scrub=True)
                    if homophone is None:
                        homophone = IPAWord(fw, language, parser=self)
                        continue
                    elif word_ipa == ipa:
                        return fw
                    else:
                        homo = self.nearer_homophone(word_ipa, homophone.get_cleaned_ipa(), ipa)
                        if homo == ipa:
                            homophone = IPAWord(fw, language, parser=self)

            if homophone is not None:
                return homophone.word

        return homophone

    def nearer_homophone(self, ipa, ipa1, ipa2):
        """
        If ipa1 is closer to ipa than ipa2,
        return ipa1.  Otherwise, return ipa2.

        :param ipa: str, IPA homophones are trying to be like
        :param ipa1: str, first IPA to compare to ipa
        :param ipa2: str, second IPA to compare to ipa
        :return: str, closest homophone to IPA from ipa1 and ipa2
        """
        if ipa == ipa1 or ipa == ipa2:
            return ipa
        else:
            sim1, sim2 = 20, 20
            ipa_chars = set(ipa)
            elt_diffs = lambda i: len(ipa_chars.symmetric_difference(i))/2.0
            sim1 -= elt_diffs(ipa1)
            sim2 -= elt_diffs(ipa2)
            elt_sims = lambda i: len(ipa_chars.intersection(i))/2.0
            sim1 += elt_sims(ipa1)
            sim2 += elt_sims(ipa2)
            sim1 += self.same_ipas(ipa, ipa1)
            sim2 += self.same_ipas(ipa, ipa2)

            print(ipa, "vs", ipa1, ":\t", sim1)
            print(ipa, "vs", ipa2, ":\t", sim2)

            if sim1 >= sim2:
                print("winner:", ipa1)
                return ipa1
            else:
                print("winner:", ipa2)
                return ipa2

    def same_ipas(self, ipa1, ipa2):
        """
        Returns an integer representing the number of IPA characters
        shared at the same indices by ipa1 and ipa2.

        :param ipa1: str, first string to compare
        :param ipa2: str, second string to compare
        :return: int, number of IPA characters shared by ipa1 and ipa2
        """
        sims = 0
        i = 0

        try:
            while True:
                char1 = ipa1[i]
                char2 = ipa2[i]

                letter1 = self.ipa_to_ipaletter(char1)
                letter2 = self.ipa_to_ipaletter(char2)

                if letter1 is None or letter2 is None:
                    sims += (ipa1[i] == ipa2[i])
                else:
                    add = letter1.compare(letter2)
                    sims += add

                i += 1
        except IndexError:
            pass

        sims -= abs(len(ipa1) - len(ipa2))
        return sims

    # COMMON IPAS/PHONEMES
    # --------------------
    def common_ipas(self, lim=50000):
        """
        Returns a list of the 50,000 most common morphemes
        in this PhonemeParser's language transcribed to IPA.

        :param lim: int, lim <= 50000, number of IPAs to retreive
        :return: Set(str), most common IPAs in PhonemeParser's language
        """
        morphemes = self.common_morphemes(lim)
        ipas = set()

        for morpheme in morphemes:
            ipa = self.word_ipa(morpheme)
            if ipa is not None:
                ipas.add(ipa)

        self.refresh_data()
        return ipas

    def common_ipa_words(self, lim=50000):
        """
        Returns a set of IPAWords corresponding to the
        Wiktionary entry of this PhonemeParser's language's most
        common words (up to 50,000).

        :param lim: int, lim <= 50000, number of words to retrieve
        :return: Set(IPAWord), common IPAWords in this PhonemeParser's language
        """
        words = self.common_words(language=self.language, lim=lim)
        transcriptions = self.words_ipawords(words)
        return transcriptions

    def common_phonemes(self, lim=50000):
        """
        Returns a dictionary representing ipa_phonemes
        for up to the 50,000 most common words in this language
        and each of the forms they take.

        :param lim: int, lim <= 50000, number of words to retreive
        :return: dict, where...
            key (str) - phoneme (i.e., short sequence of characters)
            val (List[str]) - IPA translations of this language's phoneme
        """
        transcriptions = self.common_ipa_words(lim=lim)
        phoneme_dict = self.ipa_words_phonemes(transcriptions)
        return phoneme_dict

    def common_ipa_pairs(self, language=None, lim=50000, only_top=False):
        """
        Returns a set of common IPA-pos pairs from Wordnet up to lim.
        ~
        If top is True, this method only adds the top IPA pronunciation
        for each word to the list.  Otherwise, adds all IPA pronunciations.

        :param language: str, language of ipa pairs
        :param lim: int, lim <= 50000, number of ipa pairs to retrieve
        :param only_top: bool, whether to output only top IPAs or all IPAs
        :return: Set(tuple(str,str)), common ipa pairs in MorphemeParser's language
        """
        language = self.verify_language(language)
        word_pairs = self.common_word_pairs(language, lim)
        ipa_pairs = set()

        for word, pos in word_pairs:
            ipas = self.word_ipas(word, self.language)
            if ipas is not None:
                for ipa in ipas:
                    pair = (ipa, pos)
                    ipa_pairs.add(pair)
                    if only_top:
                        break

        self.refresh_data()
        return ipa_pairs

    # IPA/PHONEME MANIPULATION
    # ------------------------
    def word_ipaword(self, word, language=None):
        """
        Returns the given word as an IPAWord.

        :param word: str, word to turn into IPAWord
        :param language: str, language of word
        :return: IPAWord, IPAWord corresponding to given word
        """
        language = self.verify_language(language)
        ipa = self.word_ipa(word)
        if ipa is not None:
            return IPAWord(word, language, parser=self)

    def words_ipawords(self, words, language=None):
        """
        Transcribes the words in the given set of words to IPAWords.

        :param words: Set(str), set of word definitions
        :param language: str, language of words
        :return: Set(IPAWord), IPAWords corresponding to given definitions
        """
        language = self.verify_language(language)
        ipa_words = set()

        for word in words:
            ipa_word = self.word_ipaword(word, language)
            if ipa_word is not None:
                ipa_words.add(ipa_word)

        return ipa_words

    def word_declension(self, word, language=None):
        """
        Returns the declension for the word in the given language.
        ~
        A declension is a dictionary of word inflections, with the
        word lemma as the head and each type of inflection as a
        different key-value pair.

        :param word: str, word to find declension for
        :param language: str, language of declension
        :return: dict[], where...
            key (str) - declension type (e.g. nominative)
            val (List[str]) - all word's inflections for given type
        """
        language = self.verify_language(language)
        declension = self.find_wiktionary_subentry(word, language, u"Declension")
        return declension

    def words_declensions(self, words, language=None):
        """
        Returns a list of declension dictionaries for each
        word (in the given language) in words.

        :param words: List[str], words to retrieve declensions for
        :param language: str, language of given words
        :return: List[dict], declension dictionaries for all words
        """
        declensions = []
        for word in words:
            declension = self.word_declension(word, language)
            if declension is not None:
                declensions.append(declension)
        return declensions

    def ipa_to_ipaletter(self, ipa):
        """
        Returns this ipa symbol's corresponding IPALetter,
        if one exists.  Otherwise, return None.

        :param ipa: str, ipa symbol
        :return: IPALetter, IPALetter for this ipa symbol
        """
        try:
            return IPALETTERS[ipa]
        except KeyError:
            return

    def ipa_words_phonemes(self, ipa_words):
        """
        Returns a dictionary representing all phonemes in ipa_words.
        ~
        N.B. Phonemes are in a language's native lettering system,
        while their forms are in IPA.

        :param ipa_words: Set(IPAWord), IPAWords to return phonemes of
        :return: dict, where...
            key (str) - phoneme (i.e., short sequence of >=1 characters)
            val (List[str]) - IPA translations of this language's phoneme
        """
        ipa_words = sorted(ipa_words, key=lambda iw: iw.get_difficulty())

        for ipa_word in ipa_words:
            phoneme_dict = ipa_word.find_phoneme_dict()
            self.phoneme_dict = self.merge_dicts(self.phoneme_dict, phoneme_dict)

        return self.phoneme_dict

    def next_phoneme(self, ipa, remove=True, use_syllables=True):
        """
        Returns the given ipa's next phoneme.
        ~
        If remove is set to True, this method finds and
        removes ipa's first phoneme, returning a 2-tuple of
        1) the phoneme and 2) given ipa with phoneme removed.
        ~
        e.g. next_phoneme("ɔˈba.lat͡ɕ") -> ("ɔ", "balat͡ɕ")

        :param ipa: str, IPA word to return next phoneme of
        :param remove: bool, whether to return ipa with vowels removed
        :param use_syllables: bool, whether to calculate next phoneme with ipa's syllables
        :return: tuple(str, str), IPA's first phoneme and rest of IPA
        """
        phoneme = str()  # next phoneme so far

        if len(ipa) == 0:
            next_phoneme = (phoneme, ipa) if remove else phoneme
            return next_phoneme

        if use_syllables:
            # ensure uniform stress marks
            new_ipa = self.restress(ipa)
            # end ipa @ 1st syllable marker
            new_ipa = new_ipa.split(u".", 1)[0]
        else:
            new_ipa = self.clean_ipa(ipa)

        # search for polyphonemes first
        end = 1
        # TODO: change to end <= min([longest IPA phoneme in phoneme_dict], len(new_ipa))
        while end <= 3:
            new_sym = new_ipa[:end]
            filtered_sym = "".join(filter((lambda x: x if x not in SEMIVOWELS else ""), new_sym))
            # check to make sure phonemes are all vowels xor all consonants
            are_vowels = self.is_ipa_vowel(filtered_sym)
            if are_vowels is None:
                end -= 1
                break
            elif self.is_ipa_phoneme(new_sym):
                phoneme = new_sym
            end += 1

        # if no polyphonemes found,
        # set phoneme to first IPA character
        if len(phoneme) == 0:
            phoneme = new_ipa[0]
            end = 1

        next_phoneme = (phoneme, ipa[end:]) if remove else phoneme
        return next_phoneme

    # VOWELS, CONSONANTS, & PHONEMES
    # ------------------------------
    def is_letter_vowel(self, chars):
        """
        Returns True if the given chars is a vowel in this
        IPAWord's native language, False if a consonant.
        ~
        Returns None if chars is not in this PhonemeParser's phoneme_dict.
        ~
        N.B. chars can be multiple letters long.

        :param chars: str, character(s) to determine whether vowel
        :return: bool, whether given character(s) are a vowel
        """
        if chars in self.phoneme_dict:
            return chars in self.vowels.items_set

    def is_letter_consonant(self, chars):
        """
        Returns True if the given chars is a consonant in this
        IPAWord's native language, False if a vowel.
        ~
        Returns None if this chars is not in this PhonemeParser's phoneme_dict.
        ~
        N.B. chars can be multiple letters long.

        :param chars: str, character(s) to determine whether consonant
        :return: bool, whether given character(s) are a consonant
        """
        if chars in self.phoneme_dict:
            return chars in self.consonants.items_set

    def is_letter_phoneme(self, chars):
        """
        Returns True if the given chars is a phoneme in this
        IPAWord's native language, False otherwise.
        ~
        Returns None if this chars is not in this PhonemeParser's phoneme_dict.
        ~
        N.B. chars can be multiple letters long.

        :param chars: str, character(s) to determine whether phoneme
        :return: bool, whether given character(s) are a phoneme
        """
        return chars in self.phoneme_dict

    def is_ipa_vowel(self, ipa):
        """
        Returns True if the given IPA symbol is a vowel
        according to the IPA, False if a consonant.
        ~
        Returns None if this symbol is not an IPA letter.

        :param ipa: str, IPA symbol to determine whether vowel
        :return: bool, whether given IPA symbol is a vowel
        """
        try:
            ipa_sym = IPALETTERS[ipa]
        except KeyError:
            if len(ipa) > 1:
                ipa_phonemes = self.phoneme_dict.keys()
                if len(ipa_phonemes) == 0:
                    return
                elif ipa in ipa_phonemes:
                    return any(self.is_ipa_vowel(sym) for sym in ipa if sym in IPALETTERS)
            else:
                return
        else:
            return ipa_sym.is_vowel

    def is_ipa_semivowel(self, ipa):
        """
        Returns True if the given IPA symbol is a semivowel
        according to the IPA, False otherwise.
        ~
        Returns None if this symbol is not an IPA letter.

        :param ipa: str, IPA symbol to determine whether vowel
        :return: bool, whether given IPA symbol is a vowel
        """
        try:
            IPALETTERS[ipa]
        except KeyError:
            return None
        else:
            return ipa in SEMIVOWELS

    def is_ipa_phoneme(self, ipa):
        """
        Returns True if the given IPA symbol is a phoneme in the
        IPA or in this PhonemeParser's language, False otherwise.

        :param ipa: str, IPA symbol to determine whether phoneme
        :return: bool, whether given IPA symbol is a phoneme
        """
        for phoneme in self.phoneme_dict:
            items = self.phoneme_dict[phoneme]
            for item in iter(items):
                if ipa == item:
                    return True
        else:
            if self.is_ipa_vowel(ipa) is not None:
                return True
            else:
                return False

    def add_vowel(self, chars):
        """
        Adds the given chars to this PhonemeParser's
        list of vowels.

        :param chars: str, phoneme (i.e., short sequence of characters)
        :return: None
        """
        self.vowels.add(chars)

    def add_consonant(self, chars):
        """
        Adds the given chars to this PhonemeParser's
        list of consonants.

        :param chars: str, phoneme (i.e., short sequence of characters)
        :return: None
        """
        self.consonants.add(chars)

    def add_phoneme_entry(self, chars, ipas):
        """
        Adds the given chars-ipas pair to this PhonemeParser's
        phoneme_dict.

        :param chars: str, phoneme (i.e., short sequence of characters)
        :param ipas: str, IPA translation of this language's phoneme
        :return: None
        """
        self.phoneme_dict.setdefault(chars, OrderedSet([]))
        self.phoneme_dict[chars].add(ipas)

    def destress(self, ipa):
        """
        Returns the given IPA pronunciation with stress marks removed.

        :param ipa: str, IPA to remove stress marks from
        :return: str, ipa with stress marks removed
        """
        return re.sub(u"[" + self.STRESS_MARKS + u"]", u"", ipa)

    def restress(self, ipa):
        """
        Returns the given IPA pronunciation with all stress marks
        replaced with periods.

        :param ipa: str, IPA to replace stress marks with periods
        :return: str, ipa with stress marks replaced with periods
        """
        restressed = re.sub(u"[" + self.STRESS_MARKS + u"]", u".", ipa)
        return restressed.strip(u".")


class IPAWord:
    """
    A class for operating on words and their IPA pronunciations.
    """
    def __init__(self, word, language, pos=None, parser=None):
        self.language = language
        if parser is None:
            self.parser = PhonemeParser(self.language)
        else:
            self.parser = parser
        self.word = word
        self.pos = pos
        self.vowels = OrderedSet([])
        self.consonants = OrderedSet([])
        self.ipa = None
        self.phoneme_dict = {}

    def get_word(self):
        """
        Returns this IPAWord's word, in its native language's alphabet.

        :return: str, this IPAWord's word
        """
        return self.parser.clean_word(self.word)

    def get_pos(self):
        """
        Returns this IPAWord's part-of-speech, pos.

        :return: str, this IPAWord's part-of-speech
        """
        return self.pos

    def get_ipa(self):
        """
        Returns this IPAWord's pronunciation in IPA.

        :return: str, this IPAWord's IPA pronunciation
        """
        if self.ipa is None:
            self.init_ipa()
        return self.ipa

    def init_ipa(self):
        """
        Initializes this IPAWord's IPA according to its word and language.

        :return:
        """
        self.ipa = self.parser.word_ipa(self.word, self.language)

    def get_cleaned_ipa(self, scrub=True):
        """
        Returns this IPAWord's pronunciation in IPA,
        with no stress symbols.

        :param scrub: bool, whether to also remove diacritics
        :return: str, this IPAWord's IPA pronunciation
        """
        return self.parser.clean_ipa(self.get_ipa(), scrub=scrub)

    def get_phoneme_dict(self):
        """
        Returns this IPAWord's phoneme dictionary.

        :return: dict, where...
            key (str) - >=1 letters in a native language alphabet
            val (Set(str)) - list of >=1 IPA symbols corresponding to key
        """
        return self.phoneme_dict

    def get_difficulty(self):
        """
        Returns this IPAWord's difficulty score, calculated from
        the predictable differences between its word and IPA.
        ~
        More predictable differences have a lower difficulty score.
        Less predictable differences have a higher difficulty score.

        :return: float, difficulty score for this ipa
        """
        return self.difficulty_score()

    def init_phoneme_dict(self):
        """
        Initializes this IPAWord's phoneme dictionary.

        :return: dict, where...
            key (str) - >=1 letters in a native language alphabet
            val (Set(str)) - list of >=1 IPA symbols corresponding to key
        """
        self.phoneme_dict = self.find_phoneme_dict()

    def set_pos(self, pos):
        """
        Sets given pos to this IPAWord's part-of-speech.

        :param pos: str, this IPAWord's part-of-speech
        :return: None
        """
        self.pos = pos

    def add_phoneme_entry(self, chars, ipas):
        """
        Adds the given chars-ipas pair to this IPAWord and PhonemeParser's
        phoneme_dict.

        :param chars: str, phoneme (i.e., short sequence of characters)
        :param ipas: str, IPA translation of this language's phoneme
        :return: None
        """
        self.phoneme_dict.setdefault(chars, OrderedSet([]))
        self.phoneme_dict[chars].add(ipas)
        if self.parser.is_ipa_vowel(ipas):
            self.add_vowel(chars)
        if self.parser.is_ipa_vowel(ipas) is False or any(self.parser.is_ipa_vowel(ipa) is False for ipa in ipas):
            self.add_consonant(chars)
        self.parser.add_phoneme_entry(chars, ipas)

    def add_vowel(self, chars):
        """
        Adds the given chars to this IPAWord and PhonemeParser's
        list of vowels.

        :param chars: str, phoneme (i.e., short sequence of characters)
        :return: None
        """
        self.vowels.add(chars)
        self.parser.add_vowel(chars)

    def add_consonant(self, chars):
        """
        Adds the given chars to this IPAWord and PhonemeParser's
        list of consonants.

        :param chars: str, phoneme (i.e., short sequence of characters)
        :return: None
        """
        self.consonants.add(chars)
        self.parser.add_consonant(chars)

    def find_vowels(self, phrase, remove=True):
        """
        Returns the first continuous string of vowels in
        the given phrase.
        ~
        If remove is set to True, this method finds and removes
        the first string of vowels, returning a tuple of the
        vowels and the given phrase after the vowels.
        ~
        e.g. find_vowels("stroop", remove=False) -> "oo"
             find_vowels("stroop", remove=True) -> ("oo", "p")

        :param phrase: str, phrase to extract vowels from
        :param remove: bool, whether to return phrase with vowels removed
        :return: str, first string of vowels in phrase
        """
        pre_vowels = True
        vowels = ""
        char_idx = 0

        for char in phrase:
            if pre_vowels:
                if self.parser.is_letter_vowel(char) is True:
                    pre_vowels = False
                    vowels += char
            else:
                if self.parser.is_letter_vowel(char) is not False:
                    vowels += char
                else:
                    break

            char_idx += 1

        if remove:
            remainder = phrase[char_idx:]
            return (vowels, remainder)
        else:
            return vowels

    def find_consonants(self, phrase, remove=True):
        """
        Returns the first continuous string of consonants in
        the given phrase.
        ~
        If remove is set to True, this method finds and removes
        the first string of consonants, returning a tuple.
        ~
        e.g. find_consonants("stroop", remove=False) -> "str"
             find_consonants("stroop", remove=True) -> ("str", "oop")

        :param phrase: str, phrase to extract consonants from
        :param remove: bool, whether to return phrase with consonants removed
        :return: str, first string of consonants in phrase
              or tuple(str, str), first string of consonants in phrase and
              phrase with consonants removed
        """
        pre_consonants = True
        consonants = ""
        char_idx = 0

        for char in phrase:
            if pre_consonants:
                if self.parser.is_letter_vowel(char) is False:
                    pre_consonants = False
                    consonants += char
            else:
                if self.parser.is_letter_vowel(char) is True:
                    phoneme2 = consonants[-2:]
                    if self.parser.is_letter_consonant(phoneme2):
                        consonants = consonants[:-2]
                        char_idx -= 2
                    else:
                        consonants = consonants[:-1]
                        char_idx -= 1
                    break
                else:
                    consonants += char

            char_idx += 1

        if remove:
            remainder = phrase[char_idx:]
            return (consonants, remainder)
        else:
            return consonants

    def find_ipa_vowels(self, ipa, remove=True):
        """
        Returns the first continuous string of vowels in
        the given IPA.
        ~
        If remove is set to True, this method finds and removes
        the first string of vowels, returning a tuple of the
        vowels and the given IPA after the vowels.
        ~
        e.g. find_vowels("twɔk", remove=False) -> "ɔ"
             find_vowels("twɔk", remove=True) -> ("ɔ", "k")

        :param ipa: str, IPA to extract vowels from
        :param remove: bool, whether to return phrase with vowels removed
        :return: str, first string of vowels in IPA
        """
        ipa = self.parser.restress(ipa)
        pre_vowels = True
        vowels = ""
        sym_idx = 0

        for sym in ipa:
            if pre_vowels:
                if self.parser.is_ipa_vowel(sym):
                    pre_vowels = False
                    vowels += sym
            else:
                if self.parser.is_ipa_vowel(sym):
                    vowels += sym
                else:
                    if sym == u".":
                        sym_idx += 1
                    break

            sym_idx += 1

        if remove:
            remainder = ipa[sym_idx:]
            return (vowels, remainder)
        else:
            return vowels

    def find_ipa_consonants(self, ipa, remove=True):
        """
        Returns the first continuous string of consonants in
        the given IPA.
        ~
        If remove is set to True, this method finds and removes
        the first string of consonants, returning a tuple of the
        consonants and the given IPA after the consonants.
        ~
        e.g. find_consonants("twɔk", remove=False) -> "tw"
             find_consonants("twɔk", remove=True) -> ("tw", "ɔk")

        :param ipa: str, IPA to extract consonants from
        :param remove: bool, whether to return phrase with consonants removed
        :return: str, first string of consonants in IPA
        """
        ipa = self.parser.restress(ipa)
        pre_consonants = True
        consonants = ""
        sym_idx = 0

        for sym in ipa:
            is_vowel = self.parser.is_ipa_vowel(sym)

            if pre_consonants:
                if is_vowel is False:
                    pre_consonants = False
                    consonants += sym
            else:
                if is_vowel:
                    sym_idx -= 1
                    consonants = consonants[:sym_idx]
                    sym_idx += 1
                    break
                else:
                    if sym == u".":
                        sym_idx += 1
                        break
                    else:
                        consonants += sym

            sym_idx += 1

        if remove:
            remainder = ipa[sym_idx:]
            return (consonants, remainder)
        else:
            return consonants

    def find_letter_phonemes(self):
        """
        Returns this IPAWord's letter phonemes as a list of
        character strings.
        ~
        Phonemes are calculated from this IPAWord's word as well as ipa.
        ~
        e.g. cat = IPAWord("cat", "Noun", "kæt", PhonemeParser("English"))
             cat.find_letter_phonemes() -> ["c", "a", "t"]

             text = IPAWord("text", "Noun", "tɛkst", PhonemeParser("English"))
             text.find_letter_phonemes() -> ["t", "e", "x", "t"]

        :return: List[(str) str], this IPAWord's letter phonemes
        """
        cleaned_ipa = self.get_cleaned_ipa()
        phonemes = []

        size = len(cleaned_ipa)
        start = 0   # inclusive
        end = 1     # exclusive

        while end <= size:
            if end != size and cleaned_ipa[end] in SYMBOLS:
                if cleaned_ipa[end] in AFFRICATES:
                    end += 1  # skip 2 for affricates
                end += 1      # skip 1 for diacritics
            else:
                phoneme = cleaned_ipa[start:end]
                phonemes.append(phoneme)
                start = end
                end = start + 1

        return phonemes

    def extract_vowels(self, ipas):
        """
        Breaks the given ipas into a list of IPA vowels.
        ~
        Assumes ipas contains no consonants.

        :param ipas: str, IPA to break into a list of vowels
        :return: List[(str) str], IPA broken into vowels
        """
        phonemes = []
        ipas_iter = iter(range(len(ipas)))

        for i in ipas_iter:
            try:
                ipas[i+2]
            except IndexError:
                pass
            else:
                phone_2 = ipas[i:i+2]
                if self.parser.is_ipa_vowel(phone_2):
                    phonemes.append(phone_2)
                    next(ipas_iter)
                    continue

            phone_1 = ipas[i]

            if self.parser.is_ipa_vowel(phone_1):
                phonemes.append(phone_1)
                continue

            try:
                ipas[i+3]
            except IndexError:
                pass
            else:
                phone_3 = ipas[i:i+3]
                if self.parser.is_ipa_vowel(phone_3):
                    phonemes.append(phone_3)
                    next(ipas_iter)
                    next(ipas_iter)
                    continue

            phonemes.append(phone_1)

        return phonemes

    def extract_consonants(self, ipas):
        """
        Breaks the given ipas into a list of IPA consonants.
        ~
        Assumes ipas contains no vowels.

        :param ipas: str, IPA to break into a list of consonants
        :return: List[(str) str], IPA broken into consonants
        """
        phonemes = []
        ipas_iter = iter(range(len(ipas)))

        for i in ipas_iter:
            try:
                phone_1 = ipas[i:i+1]
            except IndexError:
                pass
            else:
                if self.parser.is_ipa_vowel(phone_1) is False:
                    phonemes.append(phone_1)
                    next(ipas_iter)
                    continue

            phone_0 = ipas[i]

            if self.parser.is_ipa_vowel(phone_0) is False:
                phonemes.append(phone_0)
                continue

            try:
                phone_2 = ipas[i:i+2]
            except IndexError:
                pass
            else:
                if self.parser.is_ipa_vowel(phone_2) is False:
                    phonemes.append(phone_2)
                    next(ipas_iter)
                    next(ipas_iter)
                    continue

            phonemes.append(phone_0)

        return phonemes

    def find_ipa_phonemes(self, ipa, use_syllables=True):
        """
        Returns this IPAWord's phonemes as a list of IPA strings.
        ~
        Phonemes are calculated from this IPAWord's self.ipa.
        ~
        e.g. cat = IPAWord("cat", "Noun", "kæt", PhonemeParser("English"))
             cat.find_ipa_phonemes() -> ["k", "æ", "t"]

             text = IPAWord("text", "Noun", "tɛkst", PhonemeParser("English"))
             text.find_ipa_phonemes() -> ["t", "ɛ", "ks", "t"]

        :param ipa: str, IPA to find phonemes of
        :param use_syllables: bool, whether to calculate phonemes with ipa's syllables
        :return: List[(str) str], this IPAWord's phonemes in IPA
        """
        if len(ipa) == 0:
            return []
        else:
            phonemes = []
            next_ipa = ipa

            while len(next_ipa) != 0:
                next_phoneme, next_ipa = self.parser.next_phoneme(next_ipa, use_syllables)
                phonemes.append(next_phoneme)

            return phonemes

    def find_word_phonemes(self, word, ipa):
        """
        Finds this word-IPA pair's phonemes and
        adds them to this IPAWord's phoneme_dict.
        ~
        Returns None.
        ~
        N.B. For now, this method only works with 1-syllable words.

        :param word: str, word to add phonemes of
        :param ipa: str, IPA corresponding to word
        :return: None
        """
        parts = self.parser.break_syllable(ipa)
        onset, rhyme, coda = parts
        vowel_start, vowel_end = 0, None
        clean_ipa = self.parser.clean_ipa(ipa)

        if all(len(part) == 1 for part in parts) and len(word) == len(clean_ipa):
            self.add_phoneme_entry(word[0], onset)
            self.add_phoneme_entry(word[1], rhyme)
            self.add_phoneme_entry(word[2], coda)
            return

        if len(onset) != 0:
            # there MUST be consonant letter(s) @ beginning of word
            # at least 1st letter is consonant
            vowel_start += 1
            while all(self.parser.is_letter_vowel(c) is False for c in word[:vowel_start+1]) \
                    and vowel_start+1 < len(word):
                vowel_start += 1
            char = word[:vowel_start]
            self.add_phoneme_entry(char, onset)
            self.add_consonant(char)

        if len(coda) != 0:
            # there MUST be consonant letter(s) @ end of word
            # at least last letter is consonant
            vowel_end = -1
            while all(self.parser.is_letter_vowel(c) is not True for c in word[vowel_end-1:]) \
                    and vowel_end-1 > vowel_start:
                vowel_end -= 1
            char = word[vowel_end:]
            self.add_phoneme_entry(char, coda)
            self.add_consonant(char)

        if len(rhyme) != 0:
            # there MUST be vowel letter(s) @ middle of word
            char = word[vowel_start:vowel_end]
            self.add_phoneme_entry(char, rhyme)
            self.add_vowel(char)

    def find_hard_word_phonemes(self, word, ipa):
        """
        Finds this hard word-IPA pair's phonemes and
        adds them to this IPAWord's phoneme_dict.
        ~
        Returns None.
        ~
        N.B. This method is for words with >1 syllable.

        :param word: str, word to add phonemes of
        :param ipa: str, IPA corresponding to word
        :return: None
        """
        broken_syllables = self.parser.break_syllables(ipa, use_syllables=True)
        rest_word = word

        for i in range(len(broken_syllables)):
            syllable = broken_syllables[i]
            onset, rhyme, coda = syllable

            if len(onset) != 0:
                consonants, rest_word = self.find_consonants(rest_word)
                if len(consonants) != 0:
                    self.add_phoneme_entry(consonants, onset)

            if len(rhyme) != 0:
                vowels, rest_word = self.find_vowels(rest_word)
                if len(vowels) != 0:
                    self.add_phoneme_entry(vowels, rhyme)

            if len(coda) != 0:
                consonants, rest_word = self.find_consonants(rest_word)
                if len(consonants) != 0:
                    self.add_phoneme_entry(consonants, coda)

    def find_phoneme_dict(self, word=None, ipa=None):
        """
        Returns a dictionary representing this IPAWord's ipa_phonemes,
        with native alphabet letters as keys and IPA symbols as values.
        ~
        Phonemes are calculated from this IPAWord's self.ipa_phonemes.

        :param word: str, word to return phoneme dictionary for
        :param ipa: str, IPA corresponding to word
        :return: dict, where...
            key (str) - >=1 letters in a native language alphabet
            val (OrderedSet(str)) - list of >=1 IPA symbols corresponding to key
        """
        word = self.word if word is None else word
        ipa = self.ipa if ipa is None else ipa
        ipa_phonemes = self.find_ipa_phonemes(ipa)

        if self.equal_word_ipa_syllables(word, ipa) == 1:
            # 1 syllable therefore only 1 set of onset/rhyme/coda
            if len(ipa_phonemes) == 1:
                self.add_phoneme_entry(word, ipa_phonemes[0])
            else:
                self.find_word_phonemes(word, ipa)

        elif not self.is_difficult(word, ipa_phonemes):
            for i in range(len(word)):
                char = word[i]
                phoneme = ipa_phonemes[i]
                self.add_phoneme_entry(char, phoneme)

        else:
            self.find_hard_word_phonemes(word, ipa)

        return self.phoneme_dict

    def is_difficult(self, word, ipas):
        """
        Returns True if the given word-ipas pair is
        difficult to phonemize, False otherwise.
        ~
        Used to sort easy from difficult words.

        :param word: str, word to determine whether difficult
        :param ipas: List[(str) str], IPAs of word to determine whether difficult
        :return: bool, whether given word-ipas pair is difficult to phonemize
        """
        return len(word) != len(ipas) or any(len(sym) > 1 for sym in ipas)

    def difficulty_score(self, word=None, ipas=None):
        """
        Returns an integer representing the difficulty of
        translating this word-ipas pair.
        ~
        Calculates difficulty score by subtracting the
        length of the word from the length of its IPAs.
        ~
        If word and/or ipas is None, this method replaces
        them with self.word and/or self.ipa respectively.
        ~
        Used to determine the difficulty of translating
        this word-ipas pair for sorting.

        :param word: str, word to determine difficulty of
        :param ipas: List[(str) str], word's IPA pronunciations to score
        :return: int, number representing differences between word and ipas
        """
        word = self.word if word is None else word
        ipas = self.find_ipa_phonemes(self.ipa) if ipas is None else ipas
        score = (abs(len(word) - len(ipas)) + (max(0, len(word) - 2)))**2 + sum((len(sym)-1)**2 for sym in ipas)
        return score

    def add_syllables(self, ipa):
        """
        Adds most likely syllable marks to this IPA.
        ~
        Assumes given IPA has no syllable marks.
        ~
        This method does not account for primary/secondary stresses
        and thus only adds a period (".") to show stress.

        :param ipa: str, IPA to add syllable marks to
        :return: str, IPA with syllable marks added
        """
        syllables = []
        next_ipa = ipa

        while len(next_ipa) != 0:
            syllable, next_ipa = self.parser.next_syllable(next_ipa)
            syllables.append(syllable)

        return u".".join(syllables)

    def equal_word_ipa_syllables(self, word, ipa):
        """
        If this word and its corresponding IPA pronunciation ipa share an equal
        number of syllables, this method returns their number of syllables.
        If they share an inequal number of syllables, this method returns False.
        ~
        False converts to integer 0 which ensures no overlap between bool vs int outputs.

        :param word: str, word to count whether syllables equal to IPA
        :param ipa: str, IPA to count whether syllables equal to word
        :return: int or bool, syllables in word and ipa if equal, False otherwise
        """
        word_syllables = self.count_word_syllables(word)
        ipa_syllables = self.count_ipa_syllables(ipa)

        if word_syllables == ipa_syllables:
            return word_syllables
        else:
            return False

    def equate_word_ipa_syllables(self, word, ipa):
        """
        If this word and its corresponding IPA pronunciation ipa share an equal
        number of syllables, this method returns the input ipa.
        ~
        Otherwise, if word and ipa share an inequal number of syllables, this method
        returns the input ipa modified to contain with the same number of syllables as
        the input word.
        ~
        This method was designed to correct Wiktionary IPA entry which have no
        syllable marks added as yet.

        :param word: str, word to check whether syllables equal to IPA
        :param ipa: str, IPA to check whether syllables equal to word
        :return: str, input ipa containing same number of syllables as word
        """
        num_syllables = self.equal_word_ipa_syllables(word, ipa)

        if num_syllables != 0:
            return ipa
        else:
            ipa = self.parser.clean_ipa(ipa)
            return self.add_syllables(ipa)

    def equate_ipa_syllables(self, ipa):
        """
        If this IPA pronunciation's stress marks appear not to match its
        number of syllables, this method returns the input ipa with stress marks added.
        ~
        Otherwise, if word and ipa share an inequal number of syllables, this method
        returns the input ipa modified to contain with the same number of syllables as
        the input word.
        ~
        This method was designed to correct Wiktionary IPA entry which have no
        syllable marks added as yet.

        :param word: str, word to check whether syllables equal to IPA
        :param ipa: str, IPA to check whether syllables equal to word
        :return: str, input ipa containing same number of syllables as word
        """
        ipa = self.parser.clean_ipa(ipa)
        return self.add_syllables(ipa)

    def count_ipa_stresses(self, ipa):
        """
        Returns number of stress marks in the given IPA.
        ~
        N.B. More precisely, this method returns the number of
        syllables implied by the number of stress marks in the given ipa.

        :param ipa: str, IPA to count stress marks of
        :return: int, number of stress marks in word with given IPA
        """
        periods = ipa.count(u".")
        primary_stress = ipa.count(u"ˈ")
        secondary_stress = ipa.count(u"ˌ")
        addn = 0 if ipa[0] in u"ˈˌ" else 1  # accounts for missing initial stress mark
        return periods + primary_stress + secondary_stress + addn

    def count_ipa_syllables(self, ipa):
        """
        Returns number of syllables in the given IPA.

        :param ipa: str, IPA to count syllables of
        :return: int, number of syllables in word with given IPA
        """
        syllables = 0
        ipa_iter = iter(range(len(ipa)))

        for i in ipa_iter:
            sym = ipa[i]

            if self.parser.is_ipa_vowel(sym):
                while i < len(ipa)-1 and self.parser.is_ipa_vowel(sym) is not False:
                    i = next(ipa_iter)
                    sym = ipa[i]

                syllables += 1

        if syllables is 0:
            syllables = 1

        return syllables

    def count_word_syllables(self, word):
        """
        Returns the number of vowel clusters in this word.

        :param word: str, word to count syllables of
        :return: int, number of syllables in word
        """
        syllables = 0
        new_word = word

        while len(new_word) != 0:
            vowels, new_word = self.find_vowels(new_word)
            syllables += 1
        # if word has no vowels, it has 1 syllable
        syllables = 1 if syllables == 0 else syllables

        return syllables

    def count_word_vowels(self, word):
        """
        Returns number of vowels in the given word.

        :param word: str, word to count vowels of
        :return: int, number of vowels in word
        """
        count = 0
        for char in word:
            if self.parser.is_letter_vowel(char):
                count += 1
        return count

    def count_word_consonants(self, word):
        """
        Returns number of consonants in the given word.

        :param word: str, word to count consonants of
        :return: int, number of consonants in word
        """
        count = 0
        for char in word:
            if self.parser.is_letter_vowel(char) is False:
                count += 1
        return count

    def count_ipa_vowels(self):
        """
        Returns number of vowels in this IPAWord's IPA.

        :return: int, number of vowels in IPA
        """
        count = 0
        for char in self.ipa:
            if char in IPAVOWELS:
                count += 1
        return count

    def count_ipa_consonants(self):
        """
        Returns number of consonants in this IPAWord's IPA.

        :return: int, number of consonants in IPA
        """
        count = 0
        for char in self.ipa:
            if char in IPACONSONANTS:
                count += 1
        return count

    def no_diacritics(self):
        """
        Returns True if this IPAWord's IPA pronunciation contains no
        diacritical or affricate symbols.

        :return: bool, whether this IPAWord's IPA contains no symbols
        """
        symbols = set(SYMBOLS)
        ipas = set(self.ipa)
        sims = symbols.intersection(ipas)
        return len(sims) == 0

    def has_diacritics(self):
        """
        Returns True if this IPAWord's IPA pronunciation contains
        diacritical or affricate symbols.

        :return: bool, whether this IPAWord's IPA contains symbols
        """
        symbols = set(SYMBOLS)
        ipas = set(self.ipa)
        sims = symbols.intersection(ipas)
        return len(sims) != 0

    def strip_syllables(self, ipa):
        """
        Removes syllable markers (i.e., '.', a period) from given IPA.

        :param ipa: str, IPA pronunciation to remove syllable markers from
        :return: str, IPA pronunciation with syllable markers removed
        """
        return re.sub(u"\.", u"", ipa)

    def __len__(self):
        """
        Returns the length of this IPAWord's cleaned word.

        :return: int, length of this IPAWord's word
        """
        return len(self.get_word())


# coding: utf-8
"""
MORPHEME_PARSER:

    Contains MorphemeParser class for parsing morpheme data
    in a given language from Wiktionary.
"""
from phoneme_parser import *


class MorphemeParser(PhonemeParser):
    """
    A class for extracting and analyzing morphemes in a
    given language.
    """
    def __init__(self, language):
        PhonemeParser.__init__(self, language)
        self.affixes = set()
        self.morphemes = set()

    # MORPHEMES
    # ---------
    def add_word_morphemes(self, word):
        """
        Adds all morphemes in this word to this MorphemeParser's
        morphemes.

        :param word: str, word to add morphemes of to morphemes
        :return: None
        """
        self.morphemes.add(word)
        word_morphemes = self.strip_affixes(word)
        self.morphemes.update(word_morphemes)

    def add_words_morphemes(self, words):
        """
        Adds all morphemes in this list of words to this MorphemeParser's
        morphemes.

        :param words: List[str], list of words to add morphemes of
        :return: None
        """
        for word in words:
            self.add_word_morphemes(word)

    def morpheme_freqs(self, morphemes=None, language=None):
        """
        Returns a frequency dictionary of morphemes in this
        MorphemeParser's language.

        :param morphemes: List[str], list of morphemes
        :param language: str, language of morphemes
        :return: dict, where...
            key (str) - morpheme in this MP's language
            val (int) - given morpheme's frequency
        """
        language = self.verify_language(language)
        if morphemes is None:
            morphemes = self.all_morphemes(language)
        morphemes = [morpheme.lower() for morpheme in morphemes]
        keys = set(morphemes)
        return {key.lower(): morphemes.count(key.lower()) for key in keys}

    def weighted_morpheme_freqs(self, morphemes=None, language=None, lim=10000):
        """
        Returns a frequency dictionary of morphemes in this
        MorphemeParser's language.

        :return: dict, where...
            key (str) - morpheme in this MP's language
            val (int) - given morpheme's frequency
        """
        common_morphemes = self.common_morphemes(language, lim=lim)
        freqs = self.morpheme_freqs(morphemes, language)
        weighted_freqs = {}

        for morpheme in freqs:
            try:
                weighting = common_morphemes.index(morpheme) * 100
                weight_ratio = weighting / float(lim)
            except ValueError:
                weight_ratio = 1

            freq = freqs[morpheme]
            weighted_freq = int(freq * weight_ratio)
            weighted_freqs[morpheme] = weighted_freq

        return weighted_freqs

    def strip_affixes(self, word):
        """
        Removes all morphemes from this word until none are left,
        then returns a list of all morphemes in this word.
        ~
        A different method to obtain a word's morphemes than
        finding its Wiktionary etymologies.

        :param word: str, word to find morphemes of
        :return: List[str], all morphemes in this word
        """
        words = self.morphemes.union(self.common_words(self.language, lim=10000))
        morphemes = []
        new_word = word
        last_morpheme = str()

        while len(new_word) != 0:
            for morpheme in sorted(words, key=lambda m: len(m), reverse=True):
                if morpheme != word and len(morpheme) > 1:
                    if morpheme == new_word[:len(morpheme)] and len(last_morpheme) > 1 and last_morpheme in words:
                        morphemes.append(last_morpheme)
                        morphemes.append(morpheme)
                        new_word = new_word[len(morpheme):]
                        last_morpheme = str()
                        break
            else:
                last_morpheme += new_word[0]
                new_word = new_word[1:]
                if len(new_word) == 0:
                    morphemes.append(last_morpheme)

        return filter(lambda m: m != "", morphemes)

    # SYLLABIFICATION
    # ---------------
    def break_word_syllable(self, syllable):
        """
        Breaks the given word syllable into its constituent
        consonants and vowels.
        ~
        N.B. In a syllable...
            1) The first set of consonants is called the ONSET.
            2) The set of vowels is called the RHYME.
            3) The second set of consonants is called the CODA.
        ~
        e.g. break_syllable("wszech") -> ("wsz", "e", "ch")

        :param syllable: (unicode) str, syllable to break
        :return: tuple((all unicode) str, str, str), the given
            syllable's onset, rhyme, and coda, respectively
        """
        onset = ""
        rhyme = ""
        coda = ""

        pre_rhyme = True

        for i in range(len(syllable)):
            char = syllable[i]

            if self.is_letter_vowel(char) is None:
                return ("", "", "")
            elif self.is_letter_vowel(char):
                pre_rhyme = False
                rhyme += char
            else:
                if pre_rhyme:
                    onset += char
                else:
                    coda += char

        return (onset, rhyme, coda)

    def break_word_syllables(self, word):
        """
        Breaks the given word into its constituent syllables'
        consonants and vowels.
        ~
        N.B. In a syllable...
            1) The first set of consonants is called the ONSET.
            2) The set of vowels is called the RHYME.
            3) The second set of consonants is called the CODA.
        ~
        e.g. break_word_syllables("wszechmocny") -> [("wsz", "e", "ch"),
                                                     ("m", "o", "c"),
                                                     ("n", "y", "")]

        :param syllable: (unicode) str, syllable to break
        :return: List[tuple((all unicode)] str, str, str), the given
            word's syllables' onsets, rhymes, and codas, respectively
        """
        return [self.break_word_syllable(syllable) for syllable in self.split_word_syllables(word)]

    def split_word_syllables(self, word):
        """
        Splits the given word into its constituent
        syllables.
        ~
        e.g. split_word_syllables("wszechmocny") -> ["wszech", "moc", "ny"]

        :param word: (unicode) str, word to break into syllables
        :return: List[(unicode) str], list of given word's syllables
        """
        syllables = []
        onset, rhyme, coda = "", "", ""
        pre_rhyme = True

        for i in range(len(word)):
            letter = word[i]

            if self.is_letter_vowel(letter):
                pre_rhyme = False
                rhyme += letter
            else:
                if pre_rhyme:
                    onset += letter
                else:
                    if not any(self.is_letter_vowel(char) for char in word[i:]):
                        coda += word[i:]
                        break
                    elif i+1 < len(word) and self.is_letter_vowel(word[i+1]):
                        coda += word[i]
                    triplet = (onset, rhyme, coda)
                    syllables.append(triplet)
                    onset, rhyme, coda = "", "", ""
                    pre_rhyme = True

        return syllables

    def break_syllable(self, syllable):
        """
        Breaks the given IPA syllable into its constituent
        consonants and vowels.
        ~
        N.B. In a syllable...
            1) The first set of consonants is called the ONSET.
            2) The set of vowels is called the RHYME.
            3) The second set of consonants is called the CODA.
        ~
        e.g. break_syllable(u"lat͡ɕ") -> (u"l", u"a", u"t͡ɕ")

        :param syllable: (unicode) str, syllable to break
        :return: tuple((all unicode) str, str, str), the given
            syllable's onset, rhyme, and coda, respectively
        """
        onset = ""
        rhyme = ""
        coda = ""
        pre_rhyme = True
        next_syllable = syllable

        while len(next_syllable) != 0:
            next_phoneme, next_syllable = self.next_phoneme(next_syllable)
            is_vowel = self.is_ipa_vowel(next_phoneme)

            if pre_rhyme:
                if is_vowel:
                    pre_rhyme = False
                    rhyme += next_phoneme
                else:
                    onset += next_phoneme
            else:
                if is_vowel or self.is_ipa_semivowel(next_phoneme):
                    rhyme += next_phoneme
                else:
                    coda += next_phoneme + next_syllable
                    break

        return (onset, rhyme, coda)

    def break_syllables(self, ipa, use_syllables=True):
        """
        Breaks the given IPA word into its syllables' constituent
        consonants and vowels.
        ~
        N.B. In a syllable...
            1) The first set of consonants is called the ONSET.
            2) The set of vowels is called the RHYME.
            3) The second set of consonants is called the CODA.
        ~
        e.g. break_syllables("ɔˈba.lat͡ɕ") -> [("", "ɔ", ""),
                                              ("b", "a", ""),
                                              ("l", "a", "t͡ɕ")]

        :param ipa: (unicode) str, IPA word to break into constituents
        :param use_syllables: bool, whether to break syllables with IPA markers
        :return: List[tuple((all unicode) str, str, str)], the given
            syllables' onsets, rhymes, and codas, respectively
        """
        return [self.break_syllable(syllable)
                for syllable in self.split_syllables(ipa, use_syllables)]

    def extract_syllable(self, ipa, idx=0, use_syllables=True):
        """
        Returns the given ipa's syllable at the given idx.
        ~
        If the index is out of bounds, this method returns a
        3-tuple of all empty strings.
        ~
        If use_syllables is True, uses built-in syllable identifiers
        (e.g. "ˈ", ".") in this ipa to guide syllable demarcation.
        Else, uses vowel and consonant clusters.
        ~
        e.g. extract_syllable("ɔˈba.lat͡ɕ", 2) -> ("l", "a", "t͡ɕ")
             extract_syllable("ɔbalat͡ɕ", 2, use_syllables=False) -> ("l", "a", "t͡ɕ")

        :param ipa: (unicode) str, IPA word to retrieve syllable of at idx
        :param idx: int, index of syllable to retrieve from IPA word's syllables
        :param use_syllables: bool, whether to calculate phonemes with ipa's syllables
        :return: tuple((all unicode) str, str, str), this ipa
            syllable's onset, rhyme, and coda, respectively
        """
        syllables = self.split_syllables(ipa, use_syllables)
        print ipa, "'s syllables:", syllables
        try:
            syllable = syllables[idx]
        except IndexError:
            return "", "", ""
        else:
            return self.break_syllable(syllable)

    def remove_syllable(self, ipa, idx=0):
        """
        Returns given ipa with the syllable at given index idx removed.
        ~
        If the index is out of bounds, this method returns the input ipa.
        ~
        e.g. remove_syllable("ɔˈba.lat͡ɕ", 2) -> "ɔ.lat͡ɕ"

        :param ipa: (unicode) str, IPA word to remove syllable at idx
        :param idx: int, syllable to remove from IPA word
        :return: (unicode) str, given ipa without syllable at idx
        """
        syllables = self.split_syllables(ipa)
        syllables.pop(idx)
        return ".".join(syllables)

    def split_syllables(self, ipa, use_syllables=True):
        """
        Splits the given IPA word into its constituent
        syllables.
        ~
        e.g. split_syllables("ɔˈba.lat͡ɕ") -> ["ɔ", "ba", "lat͡ɕ"]
             split_syllables("ɔˈba.lat͡ɕ", use_syllables=False) -> ["ɔ", "ba", "lat͡ɕ"]

        :param ipa: (unicode) str, IPA word to break into syllables
        :param use_syllables: bool, whether to calculate phonemes with ipa's syllables
        :return: List[(unicode) str], list of given ipa's syllables
        """
        if len(ipa) == 0:
            return
        else:
            if use_syllables:
                subbed_ipa = re.sub(u"[ˈˌ]", u".", ipa)
                subbed_ipa = subbed_ipa.strip(u".")
                syllables = subbed_ipa.split(u".")
                return syllables
            else:
                ipa = self.clean_ipa(ipa)
                syllables = []

                while len(ipa) != 0:
                    syllable, ipa = self.next_syllable(ipa, remove=True)
                    syllables.append(syllable)

                return syllables

    def next_syllable(self, ipa, remove=True):
        """
        Returns the given ipa's next syllable.
        ~
        Assumes given ipa does not contain syllabic markers.
        ~
        If remove is set to True, this method finds and
        removes ipa's first syllable, returning a 2-tuple of
        1) the syllable and 2) given ipa with syllable removed.
        ~
        e.g. next_syllable("ɔˈba.lat͡ɕ") -> ("ɔ", "ba.lat͡ɕ")
             next_syllable("ɔˈba.lat͡ɕ", remove=False) -> "ɔ"

        :param ipa: (unicode) str, IPA word to return next syllable of
        :param remove: bool, whether to return ipa with syllable removed
        :return: tuple((both unicode) str, str), ipa's next syllable and rest of IPA
        """
        ipa = self.clean_ipa(ipa)
        syllable = []
        pre_vowel = True

        while len(ipa) != 0:
            phoneme, ipa = self.next_phoneme(ipa, remove=True, use_syllables=False)
            is_vowel = self.is_ipa_vowel(phoneme)

            if pre_vowel:
                if is_vowel:
                    pre_vowel = False
                syllable.append(phoneme)
            else:
                if is_vowel:
                    syllable.append(phoneme)
                else:
                    if len(ipa) == 0:
                        syllable.append(phoneme)
                    else:
                        new_phoneme, new_ipa = self.next_phoneme(ipa, remove=True, use_syllables=False)
                        if self.is_ipa_vowel(new_phoneme) is False:
                            syllable.append(phoneme)
                        else:
                            ipa = phoneme + ipa
                        break

        syllable = "".join(syllable)
        syllable = (syllable, ipa) if remove else syllable
        return syllable


class Morpheme:
    """
    A class for distinguishing morphemes.

    1) free (roots)
        PARTS OF SPEECH:
        1) noun - "NN"
        2) verb - "VB"
        3) adj  - "JJ"
        4) adv  - "RB"

    2) bound (affixes)
        AFFIXES:
        1) prefix    (*XXX)
        2) suffix    (XXX*)
        3) infix     (X**X)
        4) circumfix (*XX*)
        5) interfix  (XX*X)
    """
    AFFIXES = {"prefix",
               "suffix",
               "infix",
               "circumfix",
               "interfix"}

    def __init__(self, word, language, is_free, type):
        self.word = word
        self.language = language.title()
        self._is_free = is_free
        self._type = type      # root part-of-speech or affix type

    @property
    def is_free(self):
        return self._is_free

    @is_free.setter
    def is_free(self, value):
        self._is_free = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def __hash__(self):
        return hash(self.word + self.language[:3] + str(self.type))


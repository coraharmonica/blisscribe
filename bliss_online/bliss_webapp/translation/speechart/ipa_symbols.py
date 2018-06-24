# coding: utf-8
"""
IPA_SYMBOLS:

    Stores classes for categorizing IPA symbols.
"""
from .ipas import *


class IPASymbol:

    def __init__(self, symbol):
        self.symbol = symbol

    def is_vowel(self):
        return False

    def is_affricate(self):
        return False


class IPACompound(IPASymbol):

    def __init__(self, symbols):
        IPASymbol.__init__(self, symbols)
        self.num_symbols = len(symbols)

    def get_dict(self):
        res = dict()
        res["symbol"] = self.symbol
        return res

    def get_diacritics(self):
        diacritics = "".join([sym for sym in self.symbol if sym in DIACRITICS])
        return diacritics

    def get_letters(self):
        letters = "".join([sym for sym in self.symbol if sym in IPASYMBOLS])
        return letters


class IPADiacritic(IPASymbol):

    def __init__(self, symbol, is_affricate=False):
        IPASymbol.__init__(self, symbol)
        self.is_affricate = is_affricate

    def get_dict(self):
        res = dict()
        res["symbol"] = self.symbol
        res["affricate"] = self.is_affricate
        return res

    def __int__(self):
        first = 3
        second = int(self.is_affricate)
        third = sorted(SYMBOLS).index(self.symbol)
        return int(str(first) + str(second) + str(third))


class IPALetter(IPASymbol):
    def __init__(self, symbol, is_vowel=None):
        IPASymbol.__init__(self, symbol)
        self.is_vowel = is_vowel
        self.comparisons = dict()

    def get_symbol(self):
        return self.symbol

    def is_vowel(self):
        return self.is_vowel

    def compare(self, other):
        """
        Compares this IPALetter to other IPALetter's features and
        returns an integer representing the number of similarities.
        ~
        N.B. A higher score denotes greater similarity,
             while a lower score denotes lower similarity.

        :param other: IPALetter, other IPALetter to compare with
        :return: int, number of common features between self and other
        """
        pair = (self.symbol, other.symbol)
        try:
            return self.comparisons[pair]
        except KeyError:
            score = 0

            if self.is_vowel == other.is_vowel:
                if self.is_vowel:
                    score = self.compare_vowels(other)
                elif self.is_vowel is False:
                    score = self.compare_consonants(other)

            self.comparisons[pair] = score
            return score

    def compare_vowels(self, other):
        return

    def compare_consonants(self, other):
        return

    def compare_place(self, other):
        return

    def compare_manner(self, other):
        return

    def compare_voiced(self, other):
        return

    def compare_velarized(self, other):
        return

    def compare_openness(self, other):
        return

    def compare_backness(self, other):
        return

    def compare_roundness(self, other):
        return

    def compare_lax(self, other):
        return

    def compare_rhotacized(self, other):
        return


class IPAVowel(IPALetter):
    OPENNESS = {"close": 1,
                "near close": 2,
                "close mid": 3,
                "mid": 4,
                "open mid": 5,
                "near open": 6,
                "open": 7}
    BACKNESS = {"front": 1,
                "near front": 2,
                "central front": 3,
                "central": 4,
                "central back": 5,
                "near back": 6,
                "back": 7}
    ROUNDNESS = {"unrounded": 1,
                 "rounded": 2,
                 "neither": 3}

    def __init__(self, symbol, openness, backness, roundness, lax=False, rhotacized=False, nasalized=False):
        """
        Initializes this IPAVowel as a vowel with the
        given symbol, with the given openness, backness, and roundness.
        ~
        If lax is True then this vowel is lax,
        otherwise it is not.
        ~
        If rhotacized is True then this vowel is rhotacized,
        otherwise it is regular.

        :param symbol: (unicode) str, vowel symbol(s)
        :param openness: str, openness of vowel
        :param backness: str, backness of vowel
        :param roundness: str, roundness of vowel
        :param lax: bool, whether this vowel is lax
        :param rhotacized: bool, whether this vowel is rhotacized
        :param nasalized: bool, whether this vowel is nasalized
        """
        IPALetter.__init__(self, symbol, True)
        self.openness = openness
        self.backness = backness
        self.roundness = roundness
        self.lax = lax
        self.rhotacized = rhotacized
        self.nasalized = nasalized

    def get_openness(self):
        return self.OPENNESS[self.openness]

    def get_backness(self):
        return self.BACKNESS[self.backness]

    def get_roundness(self):
        return self.ROUNDNESS[self.roundness]

    def lax(self):
        return self.lax

    def rhotacized(self):
        return self.rhotacized

    def compare_vowels(self, other):
        o = self.compare_openness(other)
        b = self.compare_backness(other)
        r = self.compare_roundness(other)
        lax = self.compare_lax(other)/2.0
        rho = self.compare_rhotacized(other)/2.0
        total = len(self.OPENNESS) + len(self.BACKNESS) + len(self.ROUNDNESS) + 1.0
        score = (o + b + r + lax + rho)/total
        score = (score - 0.9) * 10
        return score

    def compare_openness(self, other):
        total = float(len(self.OPENNESS))
        return (total - (abs(self.get_openness() - other.get_openness())/total)) #/total

    def compare_backness(self, other):
        total = float(len(self.BACKNESS))
        return (total - (abs(self.get_backness() - other.get_backness())/total)) #/total

    def compare_roundness(self, other):
        total = float(len(self.ROUNDNESS))
        return (total - (abs(self.get_roundness() - other.get_roundness())/total)) #/total

    def compare_lax(self, other):
        return self.lax == other.lax

    def compare_rhotacized(self, other):
        return self.rhotacized == other.rhotacized


class IPAConsonant(IPALetter):
    PLACE = {"bilabial": 1,
             "labiodental": 2,
             "dental": 3,
             "alveolar": 4,
             "post alveolar": 5,
             "alveolopalatal": 6,
             "retroflex": 7,
             "palatal": 8,
             "velar": 9,
             "uvular": 10,
             "pharyngeal": 11,
             "glottal": 12}
    MANNER = {"plosive": 1,
              "nasal": 2,
              "trill": 3,
              "flap tap": 4,
              "lateral flap tap": 5,
              "fricative": 6,
              "lateral fricative": 7,
              "approximant": 8,
              "lateral approximant": 9}

    def __init__(self, symbol, place, manner, voiced=False, velarized=False):
        """
        Initializes this IPAConsonant as a consonant with the
        given symbol and linguistic place and manner of articulation.
        ~
        If voiced is True then this consonant is voiced,
        otherwise it is voiceless.

        :param symbol: (unicode) str, consonant symbol(s)
        :param place: str, place of articulation
        :param manner: str, manner of articulation
        :param voiced: bool, whether this consonant is voiced
        :param velarized: bool, whether this consonant is velarized
        """
        IPALetter.__init__(self, symbol, False)
        self.symbol = symbol
        self.place = place #self.parse_part("Place", place)
        self.manner = manner #self.parse_part("Manner", manner)
        self.voiced = voiced
        self.velarized = velarized

    def get_place(self):
        return self.PLACE[self.place]

    def get_manner(self):
        return self.MANNER[self.manner]

    def voiced(self):
        return self.voiced

    def velarized(self):
        return self.velarized

    def compare_consonants(self, other):
        p = self.compare_place(other)
        m = self.compare_manner(other) * 1.5
        voiced = self.compare_voiced(other) / 2.0
        velar = self.compare_velarized(other) / 2.0
        total = len(self.PLACE) + (len(self.MANNER) * 1.5) + 1.0
        score = (p + m + voiced + velar)/total
        score = (score - 0.9) * 10
        return score

    def compare_place(self, other):
        total = float(len(self.PLACE))
        return (total - (abs(self.get_place() - other.get_place())/total)) #/total

    def compare_manner(self, other):
        total = float(len(self.MANNER))
        return (total - (abs(self.get_manner() - other.get_manner())/total)) #/total

    def compare_voiced(self, other):
        return self.voiced == other.voiced

    def compare_velarized(self, other):
        return self.velarized == other.velarized


VOWEL_KEYS = VOWELS.keys()

IPAVOWELS = {
    # FRONT VOWELS
    u"i": IPAVowel(u"i", "close", "front", "unrounded"),
    u"í": IPAVowel(u"í", "close", "front", "unrounded"),
    u"ì": IPAVowel(u"ì", "close", "front", "unrounded"),
    u"î": IPAVowel(u"î", "close", "front", "unrounded"),
    u"y": IPAVowel(u"y", "close", "front", "rounded"),
    u"ý": IPAVowel(u"ý", "close", "front", "rounded"),

    u"ɪ": IPAVowel(u"ɪ", "near close", "near front", "unrounded", lax=True),
    u"ʏ": IPAVowel(u"ʏ", "near close", "near front", "rounded", lax=True),

    u"e": IPAVowel(u"e", "close mid", "front", "unrounded"),
    u"ë": IPAVowel(u"ë", "close mid", "front", "unrounded"),
    u"é": IPAVowel(u"é", "close mid", "front", "unrounded"),
    u"ê": IPAVowel(u"ê", "close mid", "front", "unrounded"),
    u"ẽ": IPAVowel(u"ẽ", "close mid", "front", "unrounded"),
    u"ø": IPAVowel(u"ø", "close mid", "front", "rounded"),
    u"ǿ": IPAVowel(u"ǿ", "close mid", "front", "rounded"),

    u"ɛ": IPAVowel(u"ɛ", "open mid", "front", "unrounded"),
    u"œ": IPAVowel(u"œ", "open mid", "front", "rounded"),

    u"æ": IPAVowel(u"æ", "near open", "front", "unrounded"),

    u"a": IPAVowel(u"a", "open", "front", "unrounded"),
    u"ä": IPAVowel(u"a", "open", "front", "unrounded"),
    u"ã": IPAVowel(u"ã", "open", "front", "unrounded", nasalized=True),
    u"å": IPAVowel(u"ã", "open", "front", "unrounded"),
    u"â": IPAVowel(u"â", "open", "front", "unrounded"),
    u"à": IPAVowel(u"â", "open", "front", "unrounded"),
    u"ɶ": IPAVowel(u"ɶ", "open", "front", "rounded"),

    # CENTRAL VOWELS
    u"ɨ": IPAVowel(u"ɨ", "close", "central", "unrounded"),
    u"ʉ": IPAVowel(u"ʉ", "close", "central", "rounded"),

    u"ɘ": IPAVowel(u"ɘ", "close mid", "central", "unrounded"),
    u"ɵ": IPAVowel(u"ɵ", "close mid", "central", "rounded"),

    u"ə": IPAVowel(u"ə", "mid", "central", "unrounded"),
    u"ɚ": IPAVowel(u"ɚ", "mid", "central", "unrounded", rhotacized=True),

    u"ɜ": IPAVowel(u"ɜ", "open mid", "central", "unrounded"),
    u"ɝ": IPAVowel(u"ɝ", "open mid", "central", "unrounded", rhotacized=True),
    u"ɞ": IPAVowel(u"ɞ", "open mid", "central", "rounded"),

    u"ɐ": IPAVowel(u"ɐ", "near open", "central", "unrounded"),

    # BACK VOWELS
    u"ɯ": IPAVowel(u"ɯ", "close", "back", "unrounded"),
    u"u": IPAVowel(u"u", "close", "back", "rounded"),
    u"ǔ": IPAVowel(u"ǔ", "close", "back", "rounded"),
    u"ú": IPAVowel(u"ú", "close", "back", "rounded"),
    u"ù": IPAVowel(u"ù", "close", "back", "rounded"),

    u"ʊ": IPAVowel(u"ʊ", "near close", "near back", "rounded"),

    u"ɤ": IPAVowel(u"ɤ", "close mid", "back", "unrounded"),
    u"o": IPAVowel(u"o", "close mid", "back", "rounded"),
    u"õ": IPAVowel(u"õ", "close mid", "back", "rounded", nasalized=True),
    u"ó": IPAVowel(u"õ", "close mid", "back", "rounded"),
    u"ò": IPAVowel(u"ò", "close mid", "back", "rounded"),
    u"ǒ": IPAVowel(u"ǒ", "close mid", "back", "rounded"),
    u"ô": IPAVowel(u"ô", "close mid", "back", "rounded"),

    u"ʌ": IPAVowel(u"ʌ", "open mid", "back", "unrounded"),
    u"ɔ": IPAVowel(u"ɔ", "open mid", "back", "rounded"),

    u"ɑ": IPAVowel(u"ɑ", "open", "back", "unrounded"),
    u"ɒ": IPAVowel(u"ɒ", "open", "back", "rounded"),
}

SEMIVOWELS = {
    #u"j": IPAVowel(u"j", "close", "front", "unrounded"),   # semivowel approximating "i:"
    u"w": IPAVowel(u"w", "close", "back", "rounded"),      # semivowel approximating "u:"
}

IPACONSONANTS = {
    # PLOSIVES
    u"p": IPAConsonant(u"p", "bilabial", "plosive", voiced=False),  # vl bilabial plosive
    u"b": IPAConsonant(u"b", "bilabial", "plosive", voiced=True),   # vd bilabial plosive

    u"t": IPAConsonant(u"t", "alveolar", "plosive", voiced=False),  # vl alveolar plosive
    u"d": IPAConsonant(u"d", "alveolar", "plosive", voiced=True),   # vd alveolar plosive

    u"ʈ": IPAConsonant(u"ʈ", "retroflex", "plosive", voiced=False), # vl retroflex plosive
    u"ɖ": IPAConsonant(u"ɖ", "retroflex", "plosive", voiced=True),  # vd retroflex plosive

    u"c": IPAConsonant(u"c", "palatal", "plosive", voiced=False),   # vl palatal plosive
    u"ɟ": IPAConsonant(u"ɟ", "palatal", "plosive", voiced=True),    # vd palatal plosive

    u"k": IPAConsonant(u"k", "velar", "plosive", voiced=False),     # vl velar plosive
    u"ɡ": IPAConsonant(u"ɡ", "velar", "plosive", voiced=True),      # vd velar plosive
    u"g": IPAConsonant(u"g", "velar", "plosive", voiced=True),      # vd velar plosive

    u"q": IPAConsonant(u"q", "uvular", "plosive", voiced=False),    # vl uvular plosive
    u"ɢ": IPAConsonant(u"ɢ", "uvular", "plosive", voiced=True),     # vd uvular plosive

    u"ʔ": IPAConsonant(u"ʔ", "glottal", "plosive", voiced=True),    # vd glottal plosive

    # NASALS
    u"m": IPAConsonant(u"m", "labiodental", "nasal", voiced=True),  # vd bilabial nasal

    u"ɱ": IPAConsonant(u"ɱ", "labiodental", "nasal", voiced=True),  # vd labiodental nasal

    u"n": IPAConsonant(u"n", "alveolar", "nasal", voiced=True),     # vd alveolar nasal

    u"ɳ": IPAConsonant(u"ɳ", "retroflex", "nasal", voiced=True),    # vd retroflex nasal

    u"ɲ": IPAConsonant(u"ɲ", "palatal", "nasal", voiced=True),      # vd palatal nasal

    u"ŋ": IPAConsonant(u"ŋ", "velar", "nasal", voiced=True),        # vd velar nasal

    u"ɴ": IPAConsonant(u"ɴ", "uvular", "nasal", voiced=True),       # vd uvular nasal

    # TRILL
    u"ʙ": IPAConsonant(u"ʙ", "bilabial", "trill", voiced=True),    # vd bilabial trill

    u"r": IPAConsonant(u"r", "alveolar", "trill", voiced=True),    # vd alveolar trill

    u"ʀ": IPAConsonant(u"ʀ", "uvular", "trill", voiced=True),    # vd uvular trill

    # FLAP/TAP
    u"ⱱ": IPAConsonant(u"ⱱ", "labiodental", "flap tap", voiced=True),    # voiced labiodental flap

    u"ɾ": IPAConsonant(u"ɾ", "alveolar", "flap tap", voiced=True),    # vd alveolar tap

    u"ɽ": IPAConsonant(u"ɽ", "retroflex", "flap tap", voiced=True),    # vd retroflex flap

    # FRICATIVE
    u"ɸ": IPAConsonant(u"ɸ", "bilabial", "fricative", voiced=False),   # vl bilabial fricative
    u"β": IPAConsonant(u"β", "bilabial", "fricative", voiced=True),    # vd bilabial fricative

    u"f": IPAConsonant(u"f", "labiodental", "fricative", voiced=False),   # vl labiodental fricative
    u"v": IPAConsonant(u"v", "labiodental", "fricative", voiced=True),    # vd labiodental fricative

    u"θ": IPAConsonant(u"θ", "dental", "fricative", voiced=False),   # vl dental fricative
    u"ð": IPAConsonant(u"ð", "dental", "fricative", voiced=True),    # vd dental fricative

    u"s": IPAConsonant(u"s", "alveolar", "fricative", voiced=False),   # vl alveolar fricative
    u"š": IPAConsonant(u"š", "alveolar", "fricative", voiced=False),   # vl alveolar fricative
    u"z": IPAConsonant(u"z", "alveolar", "fricative", voiced=True),    # vd alveolar fricative

    u"ʃ": IPAConsonant(u"ʃ", "post alveolar", "fricative", voiced=False),   # vl postalveolar fricative
    u"ʒ": IPAConsonant(u"ʒ", "post alveolar", "fricative", voiced=True),    # vd postalveolar fricative

    u"ʂ": IPAConsonant(u"ʂ", "retroflex", "fricative", voiced=False),   # vl retroflex fricative
    u"ʐ": IPAConsonant(u"ʐ", "retroflex", "fricative", voiced=True),    # vd retroflex fricative

    u"ç": IPAConsonant(u"ç", "palatal", "fricative", voiced=False),   # vl palatal fricative
    u"ʝ": IPAConsonant(u"ʝ", "palatal", "fricative", voiced=True),    # vd palatal fricative

    u"x": IPAConsonant(u"x", "velar", "fricative", voiced=False),   # vl velar fricative
    u"ɣ": IPAConsonant(u"ɣ", "velar", "fricative", voiced=True),    # vd velar fricative

    u"χ": IPAConsonant(u"χ", "uvular", "fricative", voiced=False),   # vl uvular fricative
    u"ʁ": IPAConsonant(u"ʁ", "uvular", "fricative", voiced=True),    # vd uvular fricative

    u"ħ": IPAConsonant(u"ħ", "pharyngeal", "fricative", voiced=False),   # vl pharyngeal fricative
    u"ʕ": IPAConsonant(u"ʕ", "pharyngeal", "fricative", voiced=True),    # vd pharyngeal fricative

    u"h": IPAConsonant(u"h", "glottal", "fricative", voiced=False),   # vl glottal fricative
    u"ɦ": IPAConsonant(u"ɦ", "glottal", "fricative", voiced=True),    # vd glottal fricative

    # APPROXIMANT
    #u"w": IPAConsonant(u"w", "bilabial", "approximant", voiced=True),       # vd bilabial approximant

    u"ʋ": IPAConsonant(u"ʋ", "labiodental", "approximant", voiced=True),    # vd labiodental approximant

    u"ɹ": IPAConsonant(u"ɹ", "post alveolar", "approximant", voiced=True),  # vd (post)alveolar approximant

    u"ɻ": IPAConsonant(u"ɻ", "retroflex", "approximant", voiced=True),      # vd retroflex approximant

    u"j": IPAConsonant(u"j", "palatal", "approximant", voiced=True),        # vd palatal approximant

    u"ɰ": IPAConsonant(u"ɰ", "velar", "approximant", voiced=True),          # vd velar approximant

    # LATERAL FRICATIVE
    u"ɬ": IPAConsonant(u"ɬ", "alveolar", "lateral fricative", voiced=False),  # vl alveolar lateral fricative
    u"ɮ": IPAConsonant(u"ɮ", "alveolar", "lateral fricative", voiced=True),   # vd alveolar lateral fricative
    u"ɫ": IPAConsonant(u"ɫ", "alveolar", "lateral fricative",                 # vd alveolar lateral (velarized) [dark l]
                       voiced=True, velarized=True),

    # LATERAL APPROXIMANT
    u"l": IPAConsonant(u"l", "alveolar", "lateral approximant", voiced=True),   # vd alveolar lateral approximant
    u"ɭ": IPAConsonant(u"ɭ", "retroflex", "lateral approximant", voiced=True),  # vd retroflex lateral approximant
    u"ʟ": IPAConsonant(u"ʟ", "velar", "lateral approximant", voiced=True),      # vd velar lateral approximant

    # LATERAL FLAP/TAP
    u"ɺ": IPAConsonant(u"ɺ", "alveolar", "lateral flap tap", voiced=True),    # vd alveolar lateral flap

    # ALVEOLOPALATAL
    u"ɕ": IPAConsonant(u"ɕ", "alveolopalatal", "fricative", voiced=False),   # vl alveolopalatal fricative
    u"ʑ": IPAConsonant(u"ʑ", "alveolopalatal", "fricative", voiced=True),    # vd alveolopalatal fricative

    # MISC (TBD)
    #u"ɓ": IPAConsonant(u"ɓ", "bilabial", "plosive", voiced=True),          # vd bilabial implosive
    #u"ɗ": IPAConsonant(u"ɗ", "alveolar", "plosive", voiced=True),          # vd alveolar implosive
    #u"ħ": IPAConsonant(u"ɧ", "multi-place", "fricative", voiced=False),    # vl multiple-place fricative
    #u"ʜ": IPAConsonant(u"ʜ", "epiglottal", "fricative", voiced=False),     # vl epiglottal fricative
    #u"ʤ": IPAConsonant(u"ʤ", "post-alveolar", "affricate", voiced=True),   # vd postalveolar affricate
    #u"ʄ": IPAConsonant(u"ʄ", "palatal", "plosive", voiced=True),           # vd palatal implosive
    #u"ɠ": IPAConsonant(u"ɠ", "velar", "plosive", voiced=True),             # vd velar implosive
    #u"ʛ": IPAConsonant(u"ʛ", "uvular", "plosive", voiced=True),            # vd uvular implosive
    #u"ɥ": IPAConsonant(u"ɥ", "labial-palatal", "approximant"),             # labial-palatal approximant
    #u"ʘ": IPAConsonant(u"ʘ", "bilabial", "click"),                         # bilabial click
    #u"ʧ": IPAConsonant(u"ʧ", "postalveolar", "affricate", voiced=False),   # vl postalveolar affricate
    #u"ʍ": IPAConsonant(u"ʍ", "labial-velar", "fricative", voiced=False),   # vl labial-velar fricative
    #u"ʎ": IPAConsonant(u"ʎ", "palatal", "lateral", voiced=True),           # vd palatal lateral
    #u"ʡ": IPAConsonant(u"ʡ", "epiglottal", "plosive", voiced=True),        # vd epiglottal plosive
    #u"ʢ": IPAConsonant(u"ʢ", "epiglottal", "fricative", voiced=True)       # vd epiglottal fricative
}

IPADIACRITICS = {
    # AFFRICATES
    u"͡": IPADiacritic(u"͡", is_affricate=True),     # combining double inverted breve
    u"͜": IPADiacritic(u"͜", is_affricate=True),     # combining double breve below

    # DIACRITICS
    u"ˈ": IPADiacritic(u"ˈ", is_affricate=False),    # (primary) stress mark
    u"ˌ": IPADiacritic(u"ˌ", is_affricate=False),    # secondary stress
    u"ː": IPADiacritic(u"ː", is_affricate=False),    # length mark (alt: colon)
    u"ˑ": IPADiacritic(u"ˑ", is_affricate=False),    # half-length
    u"̞": IPADiacritic(u"̞", is_affricate=False),      # lowered articulation
    u"ʼ": IPADiacritic(u"ʼ", is_affricate=False),    # ejective
    u"ʴ": IPADiacritic(u"ʴ", is_affricate=False),    # rhotacized
    u"ʰ": IPADiacritic(u"ʰ", is_affricate=False),    # aspirated
    u"ʱ": IPADiacritic(u"ʱ", is_affricate=False),    # breathy-voice-aspirated
    u"ʲ": IPADiacritic(u"ʲ", is_affricate=False),    # palatalized
    u"ʷ": IPADiacritic(u"ʷ", is_affricate=False),    # labialized
    u"ˠ": IPADiacritic(u"ˠ", is_affricate=False),    # velarized
    u"ˤ": IPADiacritic(u"ˤ", is_affricate=False),    # pharyngealized
    u"˞": IPADiacritic(u"˞", is_affricate=False),    # rhotacized
    u"¨": IPADiacritic(u"¨", is_affricate=False),    # diaresis
    u"̥": IPADiacritic(u"̥", is_affricate=False),     # voiceless
    u"̊": IPADiacritic(u"̊", is_affricate=False),     # voiceless (use if character has descender)
    u"̤": IPADiacritic(u"̤", is_affricate=False),     # breathy voiced
    u"̪": IPADiacritic(u"̪", is_affricate=False),     # dental
    u"̬": IPADiacritic(u"̬", is_affricate=False),     # voiced
    u"̰": IPADiacritic(u"̰", is_affricate=False),     # creaky voiced
    u"̺": IPADiacritic(u"̺", is_affricate=False),     # apical
    u"̼": IPADiacritic(u"̼", is_affricate=False),     # linguolabial
    u"̻": IPADiacritic(u"̻", is_affricate=False),     # laminal
    u"̚": IPADiacritic(u"̚", is_affricate=False),     # not audibly released
    u"̹": IPADiacritic(u"̹", is_affricate=False),     # more rounded
    u"̃": IPADiacritic(u"̃", is_affricate=False),     # nasalized
    u"̜": IPADiacritic(u"̜", is_affricate=False),     # less rounded
    u"̟": IPADiacritic(u"̟", is_affricate=False),     # advanced
    u"̠": IPADiacritic(u"̠", is_affricate=False),     # retracted
    u"̈": IPADiacritic(u"̈", is_affricate=False),     # centralized
    u"̴": IPADiacritic(u"̴", is_affricate=False),     # velarized or pharyngealized
    u"̽": IPADiacritic(u"̽", is_affricate=False),     # mid-centralized
    u"̝": IPADiacritic(u"̝", is_affricate=False),     # raised
    u"̩": IPADiacritic(u"̩", is_affricate=False),     # syllabic consonant
    u"̞̞": IPADiacritic(u"̞", is_affricate=False),     # lowered
    u"̯": IPADiacritic(u"̯", is_affricate=False),     # non-syllabic
    u"̘": IPADiacritic(u"̘", is_affricate=False),     # advanced tongue root
    u"̙": IPADiacritic(u"̙", is_affricate=False),     # retracted tongue root
    u"̆": IPADiacritic(u"̆", is_affricate=False),     # extra-short
    u"̋": IPADiacritic(u"̋", is_affricate=False),     # extra high tone
    u"́": IPADiacritic(u"́", is_affricate=False),     # high tone
    u"̄": IPADiacritic(u"̄", is_affricate=False),     # mid tone
    u"¯": IPADiacritic(u"̄", is_affricate=False),    # mid tone
    u"̀": IPADiacritic(u"̀", is_affricate=False),     # low tone
    u"̏": IPADiacritic(u"̏", is_affricate=False),     # extra low tone
    u"˥": IPADiacritic(u"˥", is_affricate=False),   # extra high tone
    u"˦": IPADiacritic(u"˦", is_affricate=False),   # high tone
    u"˧": IPADiacritic(u"˧", is_affricate=False),   # mid tone
    u"˨": IPADiacritic(u"˨", is_affricate=False),   # low tone
    u"˩": IPADiacritic(u"˩", is_affricate=False),   # extra low tone
    u"ˣ": IPADiacritic(u"ˣ", is_affricate=False),   # geminate following consonant
    u"ˢ": IPADiacritic(u"ˢ", is_affricate=False),   # geminate following consonant
}

IPALETTERS = IPACONSONANTS.copy()
IPALETTERS.update(IPAVOWELS)
IPALETTERS.update(SEMIVOWELS)

IPASYMBOLS = IPALETTERS.copy()
IPASYMBOLS.update(IPADIACRITICS)

ALLSYMBOLS = IPASYMBOLS.copy()
ALLSYMBOLS.update(ALL_SYMBOLS)

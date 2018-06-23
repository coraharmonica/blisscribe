# coding: utf-8
"""
IPAS:

    Stores all IPA symbols, including diacritics and letters.
    Letters include place, manner, and other linguistic information.
"""


AFFRICATES = {
    u"͡": u"\u0361",     # combining double inverted breve
    u"͜": u"\u035c",     # combining double breve below
}

DIACRITICS = {
    u"ˈ": u"\u02c8",    # (primary) stress mark
    u"ˌ": u"\u02cc",    # secondary stress
    u"ː": u"\u02d0",    # length mark (alt: colon)
    u"ˑ": u"\u02d1",    # half-length
    u"ʼ": u"\u02bc",    # ejective
    u"ʴ": u"\u02b4",    # rhotacized
    u"ʰ": u"\u02b0",    # aspirated
    u"ʱ": u"\u02b1",    # breathy-voice-aspirated
    u"ʲ": u"\u02b2",    # palatalized
    u"ʷ": u"\u02b7",    # labialized
    u"ˠ": u"\u02e0",    # velarized
    u"ˤ": u"\u02e4",    # pharyngealized
    u"˞": u"\u02de",    # rhotacized
    u"̥": u"\u0325",     # voiceless
    u"̊": u"\u030a",     # voiceless (use if character has descender)
    u"̤": u"\u0324",     # breathy voiced
    u"̪": u"\u032a",     # dental
    u"̬": u"\u032c",     # voiced
    u"̰": u"\u0330",     # creaky voiced
    u"̺": u"\u033a",     # apical
    u"̼": u"\u033c",     # linguolabial
    u"̻": u"\u033b",     # laminal
    u"̚": u"\u031a",     # not audibly released
    u"̹": u"\u0339",     # more rounded
    u"̃": u"\u0303",     # nasalized
    u"̜": u"\u031c",     # less rounded
    u"̟": u"\u031f",     # advanced
    u"̠": u"\u0320",     # retracted
    u"̈": u"\u0308",     # centralized
    u"̴": u"\u0334",     # velarized or pharyngealized
    u"̽": u"\u033d",     # mid-centralized
    u"̝": u"\u031d",     # raised
    u"̩": u"\u0329",     # syllabic consonant
    u"̞̞": u"\u031e",     # lowered
    u"̯": u"\u032f",     # non-syllabic
    u"̘": u"\u0318",     # advanced tongue root
    u"̙": u"\u0319",     # retracted tongue root
    u"̆": u"\u0306",     # extra-short
    u"̋": u"\u030b",     # extra high tone
    u"́": u"\u0301",     # high tone
    u"̄": u"\u0304",     # mid tone
    u"̀": u"\u0300",     # low tone
    u"̏": u"\u030f"}     # extra low tone

SYMBOLS = DIACRITICS.copy()
SYMBOLS.update(AFFRICATES) #dict(DIACRITICS.items() + AFFRICATES.items())

VOWELS = {
    # FRONT VOWELS
    u"i": u"i",         # close front unrounded
    u"y": u"y",         # close front rounded

    u"ɪ": u"\u026a",    # near-close near-front unrounded (lax)
    u"ʏ": u"\u028f",    # near-close near-front rounded (lax)

    u"e": "e",          # close-mid front unrounded
    u"ø": u"\u00f8",    # close-mid front rounded

    u"ɛ": u"\u025b",    # open-mid front unrounded
    u"œ": u"\u0153",    # open-mid front rounded

    u"æ": u"\u00e6",    # near-open front unrounded (raised)

    u"a": "a",          # open front unrounded
    u"ɶ": u"\u0276",    # front open rounded

    # CENTRAL VOWELS
    u"ɨ": u"\u0268",    # close central unrounded
    u"ʉ": u"\u0289",    # close central rounded

    u"ɘ": u"\u0258",    # close-mid central unrounded [schwa]
    u"ɵ": u"\u0275",    # close-mid central rounded [schwa]

    u"ə": u"\u0259",    # mid central unrounded [schwa]
    u"ɚ": u"\u025a",    # mid central unrounded (rhotacized) [schwa]

    u"ɜ": u"\u025c",    # open-mid central unrounded
    u"ɝ": u"\u025d",    # open-mid central unrounded (rhotacized)
    u"ɞ": u"\u025e",    # open-mid central rounded

    u"ɐ": u"\u0250",    # near-open central unrounded [schwa]

    # BACK VOWELS
    u"ɯ": u"\u026f",    # close back unrounded
    u"u": u"u",         # close back rounded

    u"ʊ": u"\u028a",    # near-close near-back rounded (lax)

    u"ɤ": u"\u0264",    # close-mid back unrounded
    u"o": u"o",         # close-mid back rounded

    u"ʌ": u"\u028c",    # open-mid back unrounded
    u"ɔ": u"\u0254",    # open-mid back rounded

    u"ɑ": u"\u0251",    # open back unrounded
    u"ɒ": u"\u0252",    # open back rounded
}

CONSONANTS = {
    u"ɓ": u"\u0253",    # vd bilabial implosive
    u"ʙ": u"\u0299",    # vd bilabial trill
    u"β": u"\u03b2",    # vd bilabial fricative
    u"ɕ": u"\u0255",    # vl alveolopalatal fricative
    u"ç": u"\u00e7",    # vl palatal fricative
    u"ɗ": u"\u0257",    # vd alveolar implosive
    u"ɖ": u"\u0256",    # vd retroflex plosive
    u"ð": u"\u00f0",    # vd dental fricative
    u"ʤ": u"\u02a4",    # vd postalveolar affricate
    u"ɟ": u"\u025f",    # vd palatal plosive
    u"ʄ": u"\u0284",    # vd palatal implosive
    u"ɡ": u"\u0261",    # vd velar plosive
    u"ɠ": u"\u0260",    # vd velar implosive
    u"ɢ": u"\u0262",    # vd uvular plosive
    u"ʛ": u"\u029b",    # vd uvular implosive
    u"ɦ": u"\u0266",    # vd glottal fricative
    u"ɧ": u"\u0267",    # vl multiple-place fricative
    u"ħ": u"\u0127",    # vl pharyngeal fricative
    u"ɥ": u"\u0265",    # labial-palatal approximant
    u"ʜ": u"\u029c",    # vl epiglottal fricative
    u"ʝ": u"\u029d",    # vd palatal fricative
    u"ɭ": u"\u026d",    # vd retroflex lateral
    u"ɬ": u"\u026c",    # vl alveolar lateral fricative
    u"ɫ": u"\u026b",    # velarized vd alveolar lateral (dark l)
    u"ɮ": u"\u026e",    # vd alveolar lateral fricative
    u"ʟ": u"\u029f",    # vd velar lateral
    u"ɱ": u"\u0271",    # vd labiodental nasal
    u"ɰ": u"\u0270",    # velar approximant
    u"ŋ": u"\u014b",    # vd velar nasal
    u"ɳ": u"\u0273",    # vd retroflex nasal
    u"ɲ": u"\u0272",    # vd palatal nasal
    u"ɴ": u"\u0274",    # vd uvular nasal
    u"ɸ": u"\u0278",    # vl bilabial fricative
    u"θ": u"\u03B8",    # vl dental fricative
    u"ʘ": u"\u0298",    # bilabial click
    u"ɹ": u"\u0279",    # vd (post)alveolar approximant
    u"ɺ": u"\u027a",    # vd alveolar lateral flap
    u"ɾ": u"\u027e",    # vd alveolar tap
    u"ɻ": u"\u027b",    # vd retroflex approximant
    u"ʀ": u"\u0280",    # vd uvular trill
    u"ʁ": u"\u0281",    # vd uvular fricative
    u"ɽ": u"\u027d",    # vd retroflex flap
    u"ʂ": u"\u0282",    # vl retroflex fricative
    u"ʃ": u"\u0283",    # vl postalveolar fricative
    u"ʈ": u"\u0288",    # vl retroflex plosive
    u"ʧ": u"\u02a7",    # vl postalveolar affricate
    u"ʋ": u"\u028b",    # vd labiodental approximant
    u"ⱱ": u"\u2c71",    # voiced labiodental flap
    u"ɣ": u"\u0263",    # vd velar fricative
    u"ʍ": u"\u028d",    # vl labial-velar fricative
    u"χ": u"\u03c7",    # vl uvular fricative
    u"ʎ": u"\u028e",    # vd palatal lateral
    u"ʑ": u"\u0291",    # vd alveolopalatal fricative
    u"ʐ": u"\u0290",    # vd retroflex fricative
    u"ʒ": u"\u0292",    # vd postalveolar fricative
    u"ʔ": u"\u0294",    # glottal plosive
    u"ʡ": u"\u02a1",    # vd epiglottal plosive
    u"ʕ": u"\u0295",    # vd pharyngeal fricative
    u"ʢ": u"\u02a2"     # vd epiglottal fricative
}

IPA_LETTERS = CONSONANTS.copy()
IPA_LETTERS.update(VOWELS)

# MANNER NAMES
PLOSIVE = "plosive"
NASAL = "nasal"
SIBILANT_FRICATIVE = "sibilant fricative"
NON_SIBILANT_FRICATIVE = "non-sibilant fricative"
APPROXIMANT = "approximant"
FLAP_TAP = "flap/tap"
TRILL = "trill"
LATERAL_FRICATIVE = "lateral fricative"
LATERAL_APPROXIMANT = "lateral approximant"
LATERAL_FLAP_TAP = "lateral flap/tap"

MANNER_NAMES = [PLOSIVE, NASAL,
                SIBILANT_FRICATIVE, NON_SIBILANT_FRICATIVE,
                APPROXIMANT, FLAP_TAP, TRILL,
                LATERAL_FRICATIVE, LATERAL_APPROXIMANT, LATERAL_FLAP_TAP]

# N.B. False denotes an impossible sound,
#      while None only denotes a sound that no language uses.
NASALS = [u"m̥", u"m", None, u"ɱ", None,                                 # LABIAL
          u"n̼", None, None, u"n̥", u"n", None, None, u"ɳ̊", u"ɳ", None,   # CORONAL
          None, u"ɲ̊", u"ɲ", u"ŋ̊", u"ŋ", None,                           # DORSAL
          u"ɴ", False, False, False, False, False, False]               # LARYNGEAL

PLOSIVES = [u"p", u"b", u"p̪", u"b̪", u"t̼",
            u"d̼", None, None, u"t", u"d", None, None, u"ʈ", u"ɖ", None,
            None, u"c", u"ɟ", u"k", u"ɡ", u"q",
            u"ɢ", False, False, u"ʡ", None, u"ʔ", False]

SIBILANT_FRICATIVES = [False, False, False, False, False,
                       False, None, None, u"s", u"z", u"ʃ", u"ʒ", u"ʂ", u"ʐ", u"ɕ",
                       u"ʑ", False, False, False, False, False,
                       False, False, False, False, False, False, False]

NON_SIBILANT_FRICATIVES = [u"ɸ", u"β", u"f", u"v", u"θ̼",
                           u"ð̼", u"θ", u"ð", u"θ̠", u"ð̠", u"ɹ̠̊˔", u"ɹ̠˔", None, u"ɻ˔", None,
                           None, u"ç", u"ʝ", u"x", u"ɣ", u"χ",
                           u"ʁ", u"ħ", u"ʕ", None, u"ʢ", u"h", u"ɦ"]

APPROXIMANTS = [None, None, u"ʋ̥", u"ʋ", None,
                None, None, None, u"ɹ̥", u"ɹ", None, None, u"ɻ̊", u"ɻ", None,
                None, u"j̊", u"j", u"ɰ̊", u"ɰ", None,
                None, None, None, None, None, None, u"ʔ̞"]

FLAPS_TAPS = [None, u"ⱱ̟", None, u"ⱱ", None,
              u"ɾ̼", None, None, u"ɾ̥", u"ɾ", None, None, u"ɽ̊", u"ɽ", False,
              False, False, False, False, False, None,
              u"ɢ̆", False, False, None, u"ʡ̮", False, False]

TRILLS = [u"ʙ̥", u"ʙ", None, None, None,
          u"r̼", None, None, u"r̥", u"r", None, None, u"ɽ̊ɽ̊", u"ɽɽ", False,
          False, False, False, False, False, u"ʀ̥",
          u"ʀ", False, False, u"ʜ", u"ʢ", False, False]

LATERAL_FRICATIVES = [False, False, False, False, None,
                      None, None, None, u"ɬ", u"ɮ", None, None, u"ɭ̊˔", None, None,
                      None, u"ʎ̥˔", u"ʎ̝", u"ʟ̝̊", u"ʟ̝", None,
                      None, False, False, False, False, False, False]

LATERAL_APPROXIMANTS = [False, False, False, False, None,
                        None, None, None, u"l̥", u"l", None, None, u"ɭ̊", u"ɭ", None,
                        None, u"ʎ̥", u"ʎ", u"ʟ̥", u"ʟ", None,
                        u"ʟ̠", False, False, False, False, False, False]

LATERAL_FLAPS_TAPS = [False, False, False, False, None,
                      None, None, None, None, u"ɺ", None, None, None, u"ɺ̢", None,
                      None, None, u"ʎ̮", None, u"ʟ̆", None,
                      None, False, False, False, False, False, False]

MANNERS = {PLOSIVE: PLOSIVES, NASAL: NASALS,
           SIBILANT_FRICATIVE: SIBILANT_FRICATIVES, NON_SIBILANT_FRICATIVE: NON_SIBILANT_FRICATIVES,
           APPROXIMANT: APPROXIMANTS, FLAP_TAP: FLAPS_TAPS, TRILL: TRILLS,
           LATERAL_FRICATIVE: LATERAL_FRICATIVES,
           LATERAL_APPROXIMANT: LATERAL_APPROXIMANTS,
           LATERAL_FLAP_TAP: LATERAL_FLAPS_TAPS}

# PLACE NAMES
LABIAL = "labial"
CORONAL = "coronal"
DORSAL = "dorsal"
LARYNGEAL = "laryngeal"
BILABIAL = "bilabial"
LABIODENTAL = "labiodental"
DENTAL = "dental"
ALVEOLAR = "alveolar"
POST_ALVEOLAR = "post-alveolar"
RETROFLEX = "retroflex"
PALATAL = "palatal"
VELAR = "velar"
UVULAR = "uvular"
PHARYNGEAL = "pharyngeal"
GLOTTAL = "glottal"

VOICELESS = [MANNERS[manner][::2] for manner in MANNER_NAMES]
VOICED = [MANNERS[manner][1::2] for manner in MANNER_NAMES]

LABIALS = [MANNERS[manner][:5] for manner in MANNER_NAMES]
CORONALS = [MANNERS[manner][5:15] for manner in MANNER_NAMES]
DORSALS = [MANNERS[manner][-13:-7] for manner in MANNER_NAMES]
LARYNGEALS = [MANNERS[manner][-7:] for manner in MANNER_NAMES]

BILABIALS = [MANNERS[manner][:2] for manner in MANNER_NAMES]
LABIODENTALS = [MANNERS[manner][2:4] for manner in MANNER_NAMES]
DENTALS = [MANNERS[manner][4:6] for manner in MANNER_NAMES]
ALVEOLARS = [MANNERS[manner][6:8] for manner in MANNER_NAMES]
POST_ALVEOLARS = [MANNERS[manner][8:10] for manner in MANNER_NAMES]
RETROFLEXES = [MANNERS[manner][10:12] for manner in MANNER_NAMES]
PALATALS = [MANNERS[manner][12:14] for manner in MANNER_NAMES]
VELARS = [MANNERS[manner][14:16] for manner in MANNER_NAMES]
UVULARS = [MANNERS[manner][16:18] for manner in MANNER_NAMES]
PHARYNGEALS = [MANNERS[manner][18:20] for manner in MANNER_NAMES]
GLOTTALS = [MANNERS[manner][20:22] for manner in MANNER_NAMES]

PLACES = {BILABIAL: BILABIALS, LABIODENTAL: LABIODENTALS, DENTAL: DENTALS,
          ALVEOLAR: ALVEOLARS, POST_ALVEOLAR: POST_ALVEOLARS, RETROFLEX: RETROFLEXES,
          PALATAL: PALATALS, VELAR: VELARS, UVULAR: UVULARS,
          PHARYNGEAL: PHARYNGEALS, GLOTTAL: GLOTTALS
}

IPA = (LABIALS + CORONALS + DORSALS + LARYNGEALS)

ALL_SYMBOLS = IPA_LETTERS.copy()
ALL_SYMBOLS.update(SYMBOLS)


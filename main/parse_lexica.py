# Notes
# -----
"""
PARSE_LEXICA:

    Contains functions for parsing a language-to-Blissymbols
    dictionary from plaintext (.txt) and Excel (.xls) files.

    Allows ease of changing Bliss dictionaries, including
    adding languages beyond English.

    Alphabetical list of part-of-speech tags used in the
    Penn Treebank Project:

    Number  Tag     Description
    1.      CC      Coordinating conjunction
    2.      CD	    Cardinal number
    3.	    DT	    Determiner
    4.	    EX	    Existential there
    5.	    FW	    Foreign word
    6.	    IN	    Preposition or subordinating conjunction
    7.	    JJ	    Adjective
    8.	    JJR	    Adjective, comparative
    9.	    JJS	    Adjective, superlative
    10.	    LS	    List item marker
    11.	    MD	    Modal
    12.	    NN	    Noun, singular or mass
    13.	    NNS	    Noun, plural
    14.	    NNP	    Proper noun, singular
    15.	    NNPS	Proper noun, plural
    16.	    PDT	    Predeterminer
    17.	    POS	    Possessive ending
    18.	    PRP	    Personal pronoun
    19.	    PRP$	Possessive pronoun
    20.	    RB	    Adverb
    21.	    RBR	    Adverb, comparative
    22.	    RBS	    Adverb, superlative
    23.	    RP	    Particle
    24.	    SYM	    Symbol
    25.	    TO	    to
    26.	    UH	    Interjection
    27.	    VB	    Verb, base form
    28.	    VBD	    Verb, past tense
    29.	    VBG	    Verb, gerund or present participle
    30.	    VBN	    Verb, past participle
    31.	    VBP	    Verb, non-3rd person singular present
    32.	    VBZ	    Verb, 3rd person singular present
    33.	    WDT	    Wh-determiner
    34.	    WP	    Wh-pronoun
    35.	    WP$	    Possessive wh-pronoun
    36.	    WRB	    Wh-adverb
"""

# Imports
# -------
import sys
import xlrd
from PIL import Image, ImageDraw, ImageFont

# Constants
# ---------
FILE_PATH = sys.path[0] + "/"
IMG_PATH = FILE_PATH + "symbols/full/png/whitebg/"
LEX_PATH = FILE_PATH + "resources/universal bliss lexicon.xls"

languages = ["English", "Swedish", "Norwegian", "Hungarian", "German",
             "Dutch", "Afrikaans", "Russian", "Latvian", "Polish",
             "French", "Spanish", "Portuguese", "Italian", "Danish"]

# Functions
# ---------
def trimWhitespace(word):
    """
    Trims empty space(s) from start and end of given word.

    e.g. trimWhitespace(" full moon  ") -> "full moon"

    :param word: str, word to trim whitespace(s) from
    :return: str, word with whitespace(s) trimmed
    """
    return word.strip(" ")


def parseAlphabetic(word):
    """
    Parses the given non-alphabetic word into an
    alphabetic-only version of the word.
    ~
    String cuts off at end of the first predicted lexeme.

    e.g. parseAlphabetic("English (language)") -> "English"

    :param word: str, non-alphabetic word
    :return: str, alphabetic version of input word
    """
    new_word = []
    remove = False

    for char in word:
        if remove == False and char != "(":
            new_word.append(char)
        elif char == "(":
            remove = True
        elif char == ")":
            remove = False

    return trimWhitespace("".join(new_word))


def getImgFilenames(filename):
    """
    Reads the given XLS file for a cross-lingual Bliss
    dictionary and returns a list of image filenames.

    :param filename: str, name of XLS file
    :return: List[str], image filenames
    """
    book = xlrd.open_workbook(filename)
    sheets = book.sheets()
    sheet = sheets[0]

    rows = sheet.col_values(1)[1:]
    imgs = [row + ".png" for row in rows]

    return imgs


def getDefns(filename, language):
    """
    Reads the given XLS file for a cross-lingual Bliss
    dictionary and returns a list of the given language's
    words shared by the Bliss lexicon.

    :param filename: str, name of XLS file
    :param language: str, output list's desired language
    :return: List[str], given language's Bliss words
    """
    book = xlrd.open_workbook(filename)
    sheets = book.sheets()
    sheet = sheets[0]
    header = sheet.row_values(0)

    defns = []

    for head in range(1, len(header), 2):
        if header[head] == language:
            defns = sheet.col_values(head)[1:]

    if len(defns) == 0:
        raise IOError

    return defns


def pairLists(defns, imgs):
    """
    Creates a dict with defns supplying keys (as words in
    chosen language) and imgs supplying vals (as Blissymbol
    images).
    ~
    This function assumes defns and imgs to be ordered
    and paired.
    ~
    If a definition contains multiple words, this function
    splits the definition and adds each word to the dict as
    separate entries linking to the same Blissymbol.
    ~
    If a word in the file has no corresponding Blissymbol,
    the {key,val} pair is not added to the output dict.

    :param defns: List[str], chosen language's lexicon
    :param imgs: List[str], image filenames for defns
    :return: dict, where...
        keys (str) - words in chosen language
        vals (str) - corresponding image filenames
    """
    lang_bliss_dict = {}

    idx = 0

    for defn in defns:
        words = []  # allows for multiple words

        if defn[-5:] != "(OLD)":
            for word in defn.split(","):
                if "_" in word:
                    word = word.replace("_", " ")
                if "-" in word:
                    word = word.replace("-", " ")
                if len(word) > 0:
                    words.append(word)

        try:
            Image.open(IMG_PATH + imgs[idx])
        except IOError:
            continue
        else:
            for word in words:
                if word[:9] != "indicator":
                    word = parseAlphabetic(word)
                if word in lang_bliss_dict:
                    if type(lang_bliss_dict[word]) != list:
                        lang_bliss_dict[word] = [lang_bliss_dict[word]]
                    lang_bliss_dict[word].append(imgs[idx])
                elif len(word) > 0:
                    lang_bliss_dict[word] = imgs[idx]
        finally:
            idx += 1

    return lang_bliss_dict


def getDefnImgDict(filename, language="English"):
    """
    Reads the given XLS file for a cross-lingual Bliss
    dictionary and returns a word-image dict in the given
    language.
    ~
    If no language specified, produce English dict by
    default.

    :param filename: str, name of XLS file
    :param language: str, output list's desired language
    :return: dict, where...
        keys (str) - words in chosen language
        vals (str) - corresponding image filenames
    """
    return pairLists(getDefns(filename, language), getImgFilenames(filename))


def parseLexicon(filename):
    """
    Parses plaintext file with given filename and returns a dict of words
    with corresponding image file links.
    ~
    If a line in the file contains multiple words, this function splits the line
    and adds each word to the dict as separate entries linking to the same Blissymbol.
    If a word in the file has no corresponding Blissymbol, the {key,val} pair
    is not added to the output dict.

    :param filename: str, filename of .txt file for lexicon (each word sep. by \n)
    :return: dict, where...
        keys (str) - word in filename
        vals (str/List[str]) - word's corresponding Blissymbol image file link(s)
    """
    bliss_dict = {}  # holds words & filenames

    with open(FILE_PATH + filename, "rb", encoding="utf-8") as lex:
        for item in lex:
            item = item[:-1]  # cuts off \n character
            words = []        # allows multiple definitions

            if item[-5:] != "(OLD)":
                for i in item.split(","):
                    if "_" in i:
                        i = i.replace("_", " ")
                    if "-" in i:
                        i = i.replace("-", " ")
                    if len(i) > 0:
                        words.append(i)

            for word in words:
                try:
                    Image.open(IMG_PATH + item + ".png")
                except IOError:
                    continue
                else:
                    if word[:9] != "indicator":
                        word = parseAlphabetic(word)
                    if word in bliss_dict:
                        if type(bliss_dict[word]) != list:
                            bliss_dict[word] = [bliss_dict[word]]
                        bliss_dict[word].append(item + ".png")
                    else:
                        bliss_dict[word] = item + ".png"

    return bliss_dict


def printDict(d):
    """
    Prints the given dictionary as if it were written in code.
    Used for pasting parseLexicon()'s output into other Blisscribe modules.

    :param d: dict, input dictionary
    :return: None
    """
    print("{")
    for key in d:
        print('    "' + key + '": ' + '"' + str(d[key]) + '",')
    print("}")
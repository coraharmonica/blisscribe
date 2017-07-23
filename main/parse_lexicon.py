# Notes
# -----
"""
PARSE_LEXICON:

    Forms a Blissymbols dictionary by parsing each line in lexicon.txt,
    then prints the dictionary as if it were code.

    Allows ease of future changes to main Bliss dictionary (@ lexicon.py),
    including adding languages beyond English.
"""

# Imports
# -------
import sys
import xlrd
from PIL import Image

# Constants
# ---------
IMG_PATH = sys.path[0] + "/symbols/full/png/whitebg/"
FILE_PATH = sys.path[0] + "/"

languages = ["English", "Swedish", "Norwegian", "Hungarian", "German",
             "Dutch", "Afrikaans", "Russian", "Latvian", "Polish",
             "French", "Spanish", "Portuguese", "Italian", "Danish"]

# Functions
# ---------
def getImgFilenames(filename):
    """
    Reads the given XLS file for a cross-lingual Bliss
    dictionary and returns a list of image filenames.

    :param filename: str, name of XLS file
    :return: list, image filenames
    """
    book = xlrd.open_workbook(FILE_PATH + filename)
    sheets = book.sheets()
    sheet = sheets[0]

    rows = sheet.col_values(1)[1:]
    imgs = []

    for row in rows:
        try:
            Image.open(IMG_PATH + row + ".png")
        except IOError:
            continue
        else:
            imgs.append(row + ".png")

    return imgs

def getDefns(filename, language):
    """
    Reads the given XLS file for a cross-lingual Bliss
    dictionary and returns a list of the given language's
    words shared by the Bliss lexicon.

    :param filename: str, name of XLS file
    :param language: str, output list's desired language
    :return: list, given language's Bliss words
    """
    book = xlrd.open_workbook(FILE_PATH + filename)
    sheets = book.sheets()
    sheet = sheets[0]
    header = sheet.row_values(0)

    defns = list

    for head in range(1, len(header), 2):
        if header[head] == language:
            defns = sheet.col_values(head)[1:]

    return defns

def pairLists(defns, imgs):
    """
    Creates a dict with defns supplying keys (as words in
    chosen language) and imgs supplying vals (as Blissymbol
    images).
    ~
    This function assumes defns and imgs to be ordered
    and paired.

    :param defns: List[str], chosen language's lexicon
    :param imgs: List[str], image filenames for defns
    :return: dict, where...
        keys (str) - words in chosen language
        vals (str) - corresponding image filenames
    """
    # TODO: fix to loop through defns/imgs in order
    lang_bliss_dict = {}
    idx = 0
    words = []  # allows multiple definitions

    for defn in defns:
        if defn[-5:] != "(OLD)":
            for word in defn.split(","):
                if "_" in word:
                    word = word.replace("_", " ")
                if "-" in word:
                    word = word.replace("-", " ")
                words.append(word)

    for word in words:
        try:
            Image.open(IMG_PATH + imgs[idx])
        except IOError:
            continue
        else:
            if word[:9] != "indicator":
                word = parseAlphabetic(word)
            if word in lang_bliss_dict:
                if type(lang_bliss_dict[word]) != list:
                    lang_bliss_dict[word] = [lang_bliss_dict[word]]
                lang_bliss_dict[word].append(imgs[idx])
            else:
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

#dutch_bliss_dict = getDefnImgDict("resources/universal bliss lexicon.xls", language="Dutch")
#print(dutch_bliss_dict)

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
        vals (str/list) - word's corresponding Blissymbol image file link(s)
    """
    bliss_dict = {}  # holds words & filenames

    with open(FILE_PATH + filename, "rb") as lex:
        for item in lex:
            item = item[:-1]  # cuts off \n character
            words = []        # allows multiple definitions

            if item[-5:] != "(OLD)":
                for i in item.split(","):
                    if "_" in i:
                        i = i.replace("_", " ")
                    if "-" in i:
                        i = i.replace("-", " ")
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


def parseAlphabetic(word):
    """
    Parses the given non-alphabetic word into an
    alphabetic-only version of the word.
    String cuts off at end of the first predicted lexeme.

    e.g. parseAlphabetic("English (language)") -> "English"

    :param word: str, non-alphabetic word
    :return: str, alphabetic version of input word
    """
    new_word = []
    for char in word:
        if char != "(":
            new_word.append(char)
        else:
            break
    return trimEndSpace(new_word)


def trimEndSpace(word):
    """
    Trims empty space(s) from the end of the given word.
    Assumes more than 2 spaces denote the end of a word.

    e.g. trimEndSpace(" full moon  ") -> " full moon"

    :param word: str, word to trim space from
    :return: str, word with space trimmed
    """
    new_word = []
    idx = 0
    for char in word:
        try:
            word[idx+1]
        except IndexError:
            if char != " " and char != "-":
                new_word.append(char)
                break
        else:
            new_word.append(char)
        idx += 1
    return "".join(new_word)


def printDict(d):
    """
    Prints the given dictionary as if it were written in code.
    Used for pasting parseLexicon()'s output into other Blisscribe modules.

    :param d: dict, input dictionary
    """
    print("{")
    for key in d:
        print('    "' + key + '": ' + '"' + str(d[key]) + '",')
    print("}")
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
from PIL import Image

# Constants
# ---------
IMG_PATH = sys.path[0] + "/symbols/full/png/whitebg/"
FILE_PATH = sys.path[0] + "/"

# Functions
# ---------
def parseLexicon(filename):
    """
    Parses lexicon file with given filename and returns a dictionary of words
    with corresponding image file links.
    If a line in the file contains multiple words, this function splits the line
    and adds each word to the dict as separate entries linking to the same Blissymbol.
    If a word in the file has no corresponding Blissymbol, the {key,val} pair
    is not added to the output dict.

    :param filename: str, filename of text file for lexicon (each word sep. by \n)
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
                    elif "-" in i:
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


#printDict(parseLexicon("lexicon_edited.txt"))
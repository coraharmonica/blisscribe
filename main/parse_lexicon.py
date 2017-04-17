# Notes
# -----
"""
PARSE_LEXICON:

    Forms a Blissymbols dictionary by parsing each line in lexicon.txt,
    then prints the dictionary as if it were code.

    Allows ease of future changes to main Bliss dictionary (@ lexicon.py).
"""

# Imports
# -------
from PIL import Image


# Constants
# ---------
img_path = "/Users/courtney/Documents/creation/programming/\
personal projects/bliss translator/symbols/full/png/whitebg/"
file_path = "/Users/courtney/Documents/creation/programming/\
personal projects/bliss translator/blissymbols git/main/"


# Functions
# ---------

def parseLexicon(lexicon):
    """
    Parses lexicon file with given filename and returns a dictionary of words
    with corresponding image file links.

    :param lexicon: str, filename of text file for lexicon (each word sep. by \n)
    :return: dict, words with image file links
    """
    bliss_dict = {}

    with open(file_path + lexicon, "rb") as lex:

        for item in lex:
            item = item[:-1] # cut off \n character at end
            words = []       # multiple definitions

            for i in item.split(","):
                if "_" not in i and "(" not in i:
                    words.append(i)

            for word in words:
                try:
                    Image.open(img_path + item + ".png")
                except IOError:
                    continue
                else:
                    bliss_dict[word] = item + ".png"

    return bliss_dict


def printDict(d):
    """
    Prints the given dictionary as if it were written in code.

    :param d: dict, input dictionary
    """
    print("{")

    for key in d:
        print('    "' + key + '": ' + '"' + str(d[key]) + '",')

    print("}")


printDict(parseLexicon("lexicon.txt"))
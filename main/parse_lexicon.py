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
imgPath = "/Users/courtney/Documents/creation/programming/\
personal projects/bliss translator/symbols/full/png/whitebg/"

filePath = "/Users/courtney/Documents/creation/programming/\
personal projects/bliss translator/blissymbols git/main/"


# Functions
# ---------

def parseLexicon(lexicon):
    """
    :param lexicon: text file of words (each word separated by \n)
    :return: dictionary of words with definitions
    """
    blissDict = {}

    with open(filePath + lexicon, "rb") as lex:

        for item in lex:
            item = item[:-1] # cut off \n character at end
            words = []       # multiple definitions

            for i in item.split(","):
                if "_" not in i and "(" not in i:
                    words.append(i)

            for word in words:
                try:
                    Image.open(imgPath + item + ".png")
                except IOError:
                    continue
                else:
                    blissDict[word] = item + ".png"

    return blissDict


def printDict(d):
    """
    Prints the given dictionary as if it were written in code.
    :param d: input dictionary
    :return: None
    """
    print("{")
    for k in d:
        print('    "' + k + '": ' + '"' + str(d[k]) + '",')
    print("}")


printDict(parseLexicon("lexicon.txt"))
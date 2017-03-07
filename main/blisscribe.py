# Notes
# =====
"""
REMEMBER:
 To get this on GitHub, commit to VCS and
 select "commit and push changes" option.
"""

# Imports
# =======
import collections
import nltk
# To update NLTK:
#  from nltk import downloader
#  nltk.downloader.download()
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib
import pygame
import glyph
import fontTools
from nltk.corpus import treebank
import excerpts
import ttf_parser
import translation_dictionary

# Fonts
# =====
romanFontPath = "/Users/courtney/Library/Fonts/BLISGRID.TTF" # Helvetica: "/Library/Fonts/Helvetica.dfont
blissFontPath = "/Users/courtney/Library/Fonts/CcfSymbolFont-bliss-2012.ttf"
fontSize = 35
romanFont = ImageFont.truetype(romanFontPath, fontSize)

# ImageMagick Terminal prompt
# ===========================
# Converts
# convert -background none -fill black -font CcfSymbolFont-bliss-2012.ttf -pointsize 300 label:"\ue00a" 1.png

# Lists of most common words...
# =============================
langCommonWords = [] # in origin language
textCommonWords = [] # in origin text


# FUNCTIONS
# =========

# Helpers
# -------

def getWordFreqDict(phrase):
    """
    :param phrase: non-empty string of words
    :return: word frequency dictionary for phrase
    """
    words = nltk.word_tokenize(phrase)
    freqs = collections.defaultdict(int)

    for word in words:
        freqs[word] += 1

    return freqs


def getSortedFreqDict(freqs):
    """
    :param freqs: dict of words and word frequencies
    :return: dict where...
        keys == frequencies > 1 (sorted in decreasing order)
        vals == lists of words with that frequency
    """
    sortedFreqs = collections.defaultdict(list)

    for word in freqs:
        if freqs[word] > 1:
            sortedFreqs[freqs[word]].append(word)

    return sortedFreqs


def getWordWidth(word):
    """
    :param word: str or Image
    :return: word width in pixels
    """
    if type(word) == str:
        return (fontSize / 2) + len(word) * (fontSize / 2)
    else:
        return word.size[0] + 10


def getWordImg(word):
    """
    :param word: str
    :return: image of input str
    """
    img = Image.new('RGBA', (getWordWidth(word), fontSize * 10), (255, 255, 255, 255))
    sketch = ImageDraw.Draw(img)
    sketch.text((10, fontSize), word, font=romanFont, fill="black")
    return img


# Translator
# ----------

def translate(phrase):
    """
    :param phrase: non-empty English text
    :return: image of English text w/ Blissymbols
    """
    tokenPhrase = nltk.word_tokenize(phrase)  # phrase tokenized into word tokens
    blissDict = translation_dictionary.blissDict
    sortedFreqs = []
    taggedDict = {}

    def tagsToDict():
        """
        Adds translatable Blissymbol nouns
        from taggedPhrase to taggedDict.
        """
        taggedPhrase = nltk.pos_tag(tokenPhrase)  # tokens tagged according to word type

        for tup in taggedPhrase:
            if tup[0] in blissDict and tup[1] == "NN":
                taggedDict[tup[0]] = tup[1]


    def sortFreqs():
        """
        Creates a list of word sets sorted
        from lowest to highest frequency,
        and appends to sortedFreqs.
        """
        wordFreqs = getWordFreqDict(phrase)
        usageFreqs = getSortedFreqDict(wordFreqs)

        for k in sorted(usageFreqs):
            newSet = set([])

            for word in usageFreqs[k]:
                if word in blissDict.keys():
                    newSet.add(word)

            if len(newSet) > 0:
                sortedFreqs.append(newSet)


    def renderTranslation():
        """
        :return: rendered image of English text w/ Blissymbols
        """
        # TODO: make spacing between punctuation/words pretty
        rawPhrase = [word.lower() for word in tokenPhrase]  # token words in lowercase

        bgWidth = 2200
        bgHeight = bgWidth/2
        indent = 0
        lineNo = 0
        bg = Image.new("RGBA", (bgWidth, bgHeight), (255, 255, 255, 255))

        seen = set([])
        changed = set([])
        idx = 0

        for word in rawPhrase:
            if word in blissDict.keys() and word in taggedDict.keys():
                # if word can be validly translated into Blissymbols...
                if word in seen or word in changed:
                    # if we've already seen or translated the word before...
                    if word in sortedFreqs[-1]:
                        # removes word from sortedFreqs
                        changed.add(word)

                        if len(sortedFreqs[-1]) > 1:
                            sortedFreqs[-1].remove(word)
                        else:
                            sortedFreqs.remove(sortedFreqs[-1])

                    word = blissDict[word]           # string -> Bliss image
                    img = word.thumbnail((fontSize, bgWidth/2))

                else:
                    # if we haven't seen or translated the word before,
                    # then render English text
                    img = getWordImg(tokenPhrase[idx])
                    seen.add(word)

            else:
                # if word can't be translated to Blissymbols,
                # then render English text
                img = getWordImg(tokenPhrase[idx])

            if indent + getWordWidth(word) > bgWidth:
                indent = 0
                lineNo += 1

            if (lineNo * 100) + 100 > bgHeight:
                bg.show()
                bg = Image.new("RGBA", (bgWidth, bgHeight), (255, 255, 255, 255))
                lineNo = 0

            x = indent
            y = lineNo * 100
            #x2 = indent + img.width
            #y2 = (lineNo * 100) + img.height

            # TODO: fix paste to work with new bliss png files (provide a box)
            bg.paste(img, (indent, lineNo * 100))
            indent += getWordWidth(word)
            idx += 1

        bg.show()

    tagsToDict()
    sortFreqs()
    renderTranslation()

translate("Look at my face, my face")
#translate(excerpts.aliceInWonderland)
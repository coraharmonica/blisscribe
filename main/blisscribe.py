"""
REMEMBER:
 To get this on GitHub, commit to VCS and
 select "commit and push changes" option.
"""


# Libraries
import collections

# To update NLTK:
#  from nltk import downloader
#  nltk.downloader.download()

import nltk
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib
import pygame
import glyph
import fontTools
from nltk.corpus import treebank


# Local modules
import excerpts
import ttf_parser
import translation_dictionary

# Fonts
romanFontPath = "/Users/courtney/Library/Fonts/BLISGRID.TTF" # Helvetica: "/Library/Fonts/Helvetica.dfont
blissFontPath = "/Users/courtney/Library/Fonts/CcfSymbolFont-bliss-2012.ttf"
fontSize = 30
romanFont = ImageFont.truetype(romanFontPath, fontSize)

# Lists of most common words...
langCommonWords = [] # in origin language
textCommonWords = [] # in origin text


def wordFreq(phrase):
    """
    Takes in a non-empty string of words,
    returns a word frequency dictionary.
    """
    words = nltk.word_tokenize(phrase)
    freqs = collections.defaultdict(int)

    for word in words:
        freqs[word] += 1

    return freqs


def sortByUsage(freqs):
    """
    Takes in a dict of words and word frequencies,
    returns dict where:
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
    :param word: input string or Image
    :return: word width in pixels
    """
    if type(word) == str:
        return (fontSize / 2) + len(word) * (fontSize / 2)
    else:
        return word.size[0] + 10


def getWordImg(word):
    """
    :param word: input string
    :return: image of input string
    """
    img = Image.new('RGBA', (getWordWidth(word), fontSize * 10), (255, 255, 255, 255))
    sketch = ImageDraw.Draw(img)
    sketch.text((10, fontSize), word, font=romanFont, fill="black")
    return img


def replaceWords(phrase):
    """
    Given a phrase, determines the most-used words and
    returns the phrase with the second instances of the
    most-used words replaced with foreign words in the
    language of choice.
    """
    tokenPhrase = nltk.word_tokenize(phrase)  # phrase tokenized into word tokens
    blissDict = translation_dictionary.blissDict
    sortedFreqs = []
    taggedDict = {}

    def tagsToDict():
        """
        Creates a dict from taggedPhrase.
        """
        taggedPhrase = nltk.pos_tag(tokenPhrase)  # tokens tagged according to word type

        for tup in taggedPhrase:
            if tup[0] in blissDict and tup[1] == "NN":
                taggedDict[tup[0]] = tup[1]


    def sortFreqs():
        """
        Creates a list of word sets sorted
        from lowest to highest frequency.
        """
        wordFreqs = wordFreq(phrase)
        usageFreqs = sortByUsage(wordFreqs)

        for k in sorted(usageFreqs):
            newSet = set([])

            for word in usageFreqs[k]:
                if word in blissDict.keys():
                    newSet.add(word)

            if len(newSet) > 0:
                sortedFreqs.append(newSet)


    def renderTranslation():
        """
        :return: image of English text with Blissymbols
        """
        # TODO: make it so only second instances of bliss words are translated, otherwise print English word
        # TODO: make spacing between punctuation/words pretty
        # TODO: make it so script doesn't get written off page
        # TODO: modify translation/rendering function so it only renders the NNs (or other specified classes)
        rawPhrase = [word.lower() for word in tokenPhrase]  # token words in lowercase

        bgWidth = 2000
        bgHeight = bgWidth/2
        bg = Image.new("RGBA", (bgWidth, bgHeight), (255, 255, 255, 255))
        indent = 0
        lineNo = 0

        seen = set([])
        changed = set([])
        idx = 0

        def pasteImg(img):
            """
            :param img: input image (English text or Blissymbol)
            """
            bg.paste(img, (indent, lineNo * 100))

        for word in rawPhrase:
            if word in blissDict.keys() and word in taggedDict.keys():
                if word in seen:
                    if word in changed:
                        word = blissDict[word]
                        img = word
                    elif word in sortedFreqs[-1]:
                        changed.add(word)

                        if len(sortedFreqs[-1]) > 1:
                            sortedFreqs[-1].remove(word)
                        else:
                            sortedFreqs.remove(sortedFreqs[-1])

                        word = blissDict[word]
                        img = word
                else:
                    img = getWordImg(tokenPhrase[idx])
                    seen.add(word)
            else:
                img = getWordImg(tokenPhrase[idx])

            if indent + getWordWidth(word) > bgWidth:
                indent = 0
                lineNo += 1

            pasteImg(img)
            indent += getWordWidth(word)
            idx += 1

        bg.show()


    tagsToDict()
    sortFreqs()
    renderTranslation()


def translate(phrase):
    """

    :param phrase:
    :return:
    """
    return ""
    

replaceWords(excerpts.aliceInWonderland)

def loadBlissGlyphs():
    """
    Uses a Blissymbols glyphs parser to create a dictionary
    of Blissymbols.
    :return:
    """
    blissParser = ttf_parser.TTFParser(blissFontPath)
    blissParser.debug_printIndex()
    glyf = blissParser.seek_table("glyf", +0x0000A124)
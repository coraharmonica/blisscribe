# Libraries
import collections

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import nltk
import ttf_parser
from nltk.corpus import treebank
#from nltk import word_tokenize

#from nltk import downloader
#nltk.downloader.download()

import excerpts
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
    rawPhrase = nltk.word_tokenize(phrase)
    freqs = collections.defaultdict(int)

    for word in rawPhrase:
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


def replaceWords(phrase):
    """
    Given a phrase, determines the most-used words and
    returns the phrase with the second instances of the
    most-used words replaced with foreign words in the
    language of choice.
    """
    tokenPhrase = nltk.word_tokenize(phrase)
    rawPhrase = [word.lower() for word in tokenPhrase] #nltk.word_tokenize(phrase.lower())
    blissDict = translation_dictionary.blissDict
    sortedFreqs = []

    def sortFreqs():
        """
        Creates a list of lists of words sorted
        from lowest to highest frequency.
        """
        wordFreqs = wordFreq(phrase)
        usageFreqs = sortByUsage(wordFreqs)

        for k in sorted(usageFreqs):
            newList = []

            for word in usageFreqs[k]:
                if word in blissDict:
                    newList.append(word)

            if len(newList) > 0:
                sortedFreqs.append(newList)

    def renderTranslation():
        # TODO: make it so only second instances of bliss words are translated, otherwise print English word
        # TODO: make spacing between punctuation/words pretty
        # TODO: make it so script doesn't get written off page
        bgWidth = 2000
        bgHeight = bgWidth/2
        bg = Image.new("RGBA", (bgWidth, bgHeight), (255, 255, 255, 255))
        indent = 0
        line = 0

        acc = {"seen": [], "changed": []}
        idx = 0

        for word in rawPhrase:
            if word not in blissDict.keys():
                word = tokenPhrase[idx]
                wordWidth = (fontSize/2) + len(word) * (fontSize/2)
                img = Image.new('RGBA', (wordWidth, fontSize * 10), (255, 255, 255, 255))
                sketch = ImageDraw.Draw(img)
                sketch.text((10, fontSize), word, font=romanFont, fill="black")
                bg.paste(img, (indent % bgWidth, line))
                indent += wordWidth
                line += (indent/bgWidth)*100

            elif word in blissDict.keys():
                if word in sortedFreqs[-1]:
                    if word in acc["seen"]:
                        bg.paste(blissDict[word], (indent%bgWidth, line))
                        indent += blissDict[word].size[0] + 10
                        line += (indent/bgWidth)*100
                        if len(sortedFreqs[-1]) > 0:
                            sortedFreqs[-1].remove(word)
                        else:
                            sortedFreqs.remove(sortedFreqs[-1])
                        acc["changed"].append(word)
                    elif word in acc["changed"]:
                        bg.paste(blissDict[word], (indent%bgWidth, line))
                        indent += blissDict[word].size[0] + 10
                        line += (indent/bgWidth)*100
                    else:
                        word = tokenPhrase[idx]
                        wordWidth = (fontSize / 2) + len(word) * (fontSize / 2)
                        img = Image.new('RGBA', (wordWidth, fontSize * 10), (255, 255, 255, 255))
                        sketch = ImageDraw.Draw(img)
                        sketch.text((10, fontSize), word, font=romanFont, fill="black")
                        bg.paste(img, (indent % bgWidth, line))
                        indent += wordWidth
                        line += (indent / bgWidth) * 100
                        acc["seen"].append(word)

            if indent > bgWidth:
                indent = 0

            idx += 1

        bg.show()

    sortFreqs()
    renderTranslation()

#replaceWords(excerpts.aliceInWonderland)

def loadBlissGlyphs():
    """
    Uses a Blissymbols glyphs parser to create a dictionary
    of Blissymbols.
    :return:
    """
    blissParser = ttf_parser.TTFParser(blissFontPath)
    blissParser.debug_printIndex()
    glyf = blissParser.seek_table("glyf", +0x0000A124)
    print glyf



loadBlissGlyphs()
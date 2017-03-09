# Notes
# -----
"""
REMEMBER:
 To get this on GitHub, commit to VCS and
 select "commit and push changes" option.
"""

# Imports
# -------
import collections
import nltk
# To update NLTK:
#  from nltk import downloader
#  nltk.downloader.download()
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import excerpts
import lexicon


# Fonts
# -----
romanFontPath = "/Users/courtney/Library/Fonts/BLISGRID.TTF" # Helvetica: "/Library/Fonts/Helvetica.dfont
blissFontPath = "/Users/courtney/Library/Fonts/CcfSymbolFont-bliss-2012.ttf"
imgPath = "/Users/courtney/Documents/creation/programming/\
personal projects/bliss translator/symbols/full/png/whitebg/"
fontSize = 30
romanFont = ImageFont.truetype(romanFontPath, fontSize)
blissDict = lexicon.blissDict


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


def tagsToDict(tokenPhrase):
    """
    :param tokenPhrase: list of word tokens in given phrase
    :return: dict with translatable Blissymbols
    """
    taggedPhrase = nltk.pos_tag(tokenPhrase)  # tokens tagged according to word type
    taggedDict = {}
    validPhrases = ["NN", "VB", "JJ", "VBD"] # TODO: expand validPhrases as much as possible

    for tup in taggedPhrase:
        if tup[0] in blissDict and tup[1] in validPhrases:
            taggedDict[tup[0]] = tup[1]

    return taggedDict


def sortFreqs(phrase):
    """
    :param phrase: input string of words
    :return: a list of word sets in phrase,
    sorted from lowest to highest frequency.
    """
    wordFreqs = getWordFreqDict(phrase)
    usageFreqs = getSortedFreqDict(wordFreqs)
    sortedFreqs = []

    for k in sorted(usageFreqs):
        newSet = set([])

        for word in usageFreqs[k]:
            if word in blissDict.keys():
                newSet.add(word)

        if len(newSet) > 0:
            sortedFreqs.append(newSet)

    return sortedFreqs


# Translator
# ----------

def translate(phrase):
    """
    :param phrase: non-empty English text
    :return: image of English text w/ Blissymbols
    """
    tokenPhrase = nltk.word_tokenize(phrase)  # phrase split into word tokens
    taggedDict = tagsToDict(tokenPhrase)
    sortedFreqs = sortFreqs(phrase)

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
                    if word in sortedFreqs:
                        if word in sortedFreqs[-1]:
                            # removes word from sortedFreqs
                            changed.add(word)

                            if len(sortedFreqs[-1]) > 1:
                                sortedFreqs[-1].remove(word)
                            else:
                                sortedFreqs.remove(sortedFreqs[-1])

                    blissWord = Image.open(imgPath + blissDict[word])          # string -> Bliss image
                    img = blissWord
                    img.thumbnail((bgWidth/2, fontSize * 3))

                    # TODO: modify following code so that supertitles appear above words translated first time
                    """
                    if word not in changed:
                        superTitle = getWordImg(tokenPhrase[idx])
                        new = Image.new("RGBA", (max(getWordWidth(img), getWordWidth(superTitle)), img.size[1] + superTitle.size[1]), (255,255,255,255))
                        new.paste(superTitle, (0, 0))
                        new.paste(blissWord, (0, blissWord.size[1]))
                        img = new
                    """

                else:
                    # if we haven't seen or translated the word before,
                    # then render English text
                    img = getWordImg(tokenPhrase[idx])
                    seen.add(word)

            else:
                # if word can't be translated to Blissymbols,
                # then render English text
                img = getWordImg(tokenPhrase[idx])

            if indent + getWordWidth(img) > bgWidth:
                indent = 0
                lineNo += 1

            if (lineNo * 100) + 100 > bgHeight:
                bg.show()
                bg = Image.new("RGBA", (bgWidth, bgHeight), (255, 255, 255, 255))
                lineNo = 0

            # TODO: modify paste to work with vector bliss files
            bg.paste(img, (indent, lineNo * (fontSize * 3)))
            indent += getWordWidth(img)
            idx += 1

        bg.show()

    renderTranslation()


translate(excerpts.aliceInWonderland)
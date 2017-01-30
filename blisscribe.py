import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from collections import *

# sample English texts
DFW = "I am seated in an office, surrounded by heads and bodies. My posture is consciously congruent \
to the shape of my hard chair. This is a cold room in University Administration, wood-walled, Remington-hung, \
double-windowed against the November heat, insulated from Administrative sounds by the reception area outside, \
at which Uncle Charles, Mr. deLint and I were lately received.\
\nI am in here. \
Three faces have resolved into place above summer-weight sportcoats and half-Windsors across a polished pine \
conference table shiny with the spidered light of an Arizona noon. These are three Deans - of Admissions, \
Academic Affairs, Athletic Affairs. I do not know which face belongs to whom."

aliceInWonderland = """
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or \
 twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, `and \
 what is the use of a book,' thought Alice `without pictures or conversation?'
So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), \
whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when \
suddenly a White Rabbit with pink eyes ran close by her.

There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit \
say to itself, `Oh dear! Oh dear! I shall be late!' (when she thought it over afterwards, it occurred to her that \
she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a \
watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed \
across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, \
and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a \
large rabbit-hole under the hedge.
"""

# fonts
fontDir = "/Library/Fonts/BLISGRID.TTF" # "/Library/Fonts/Helvetica.dcaf
fontSize = 35
blissFont = ImageFont.truetype(fontDir, fontSize)


directory = "/Users/courtney/Documents/creation/programming/\
personal projects/bliss translator/symbols/"                   # shortcut
# alphabetized English-to-Blissymbols dictionary
blissDict = {"book": Image.open(directory + "book.png"),
             "business": Image.open(directory + "business.png"),
             "buy": Image.open(directory + "buy.png"),
             "card": Image.open(directory + "paper.png"),
             "child": Image.open(directory + "child.png"),
             "city": Image.open(directory + "city.png"),
             "clan": Image.open(directory + "people.png"),
             "cost": Image.open(directory + "cost.png"),
             "commerce": Image.open(directory + "business.png"),
             "county": Image.open(directory + "province.png"),
             "data": Image.open(directory + "data.png"),
             "day": Image.open(directory + "day.png"),
             "don't": Image.open(directory + "nothing.png"),
             "doesn't": Image.open(directory + "nothing.png"),
             "email": Image.open(directory + "email.png"),
             "employment": Image.open(directory + "work.png"),
             "exterior": Image.open(directory + "out.png"),
             "external": Image.open(directory + "out.png"),
             "eye": Image.open(directory + "eye.png"),
             "find": Image.open(directory + "find.png"),
             "folk": Image.open(directory + "people.png"),
             "free": Image.open(directory + "free.png"),
             "freely": Image.open(directory + "free.png"),
             "hand": Image.open(directory + "hand.png"),
             "he": Image.open(directory + "he.png"),
             "health": Image.open(directory + "health.png"),
             "help": Image.open(directory + "help.png"),
             "her": Image.open(directory + "she.png"),
             "herself": Image.open(directory + "she.png"),
             "him": Image.open(directory + "he.png"),
             "himself": Image.open(directory + "he.png"),
             "his": Image.open(directory + "his.png"),
             "home": Image.open(directory + "home.png"),
             "I": Image.open(directory + "I.png"),
             "information": Image.open(directory + "information.png"),
             "internet": Image.open(directory + "internet.png"),
             "inventory": Image.open(directory + "list.png"),
             #"it": Image.open(directory + "it.png"),
             "job": Image.open(directory + "work.png"),
             "kid": Image.open(directory + "child.png"),
             "label": Image.open(directory + "name.png"),
             "life": Image.open(directory + "life.png"),
             "list": Image.open(directory + "list.png"),
             "look": Image.open(directory + "see.png"),
             "man": Image.open(directory + "man.png"),
             "mind": Image.open(directory + "mind.png"),
             "mine": Image.open(directory + "my.png"),
             "more": Image.open(directory + "more.png"),
             "me": Image.open(directory + "I.png"),
             "music": Image.open(directory + "music.png"),
             "my": Image.open(directory + "my.png"),
             "myself": Image.open(directory + "I.png"),
             "name": Image.open(directory + "name.png"),
             "negative": Image.open(directory + "nothing.png"),
             "new": Image.open(directory + "new.png"),
             "news": Image.open(directory + "news.png"),
             "now": Image.open(directory + "now.png"),
             "no": Image.open(directory + "nothing.png"),
             "none": Image.open(directory + "nothing.png"),
             "not": Image.open(directory + "not.png"),
             "nothing": Image.open(directory + "nothing.png"),
             "our": Image.open(directory + "our.png"),
             "ours": Image.open(directory + "our.png"),
             "ourselves": Image.open(directory + "we.png"),
             "out": Image.open(directory + "out.png"),
             "outside": Image.open(directory + "out.png"),
             "page": Image.open(directory + "paper.png"),
             "paper": Image.open(directory + "paper.png"),
             "people": Image.open(directory + "people.png"),
             "person": Image.open(directory + "person.png"),
             "picture": Image.open(directory + "picture.png"),
             "price": Image.open(directory + "cost.png"),
             "province": Image.open(directory + "province.png"),
             "purchase": Image.open(directory + "buy.png"),
             "rabbit": Image.open(directory + "rabbit.png"),
             "read": Image.open(directory + "read.png"),
             "region": Image.open(directory + "province.png"),
             "school": Image.open(directory + "school.png"),
             "search": Image.open(directory + "search.png"),
             "see": Image.open(directory + "see.png"),
             "she": Image.open(directory + "she.png"),
             "sister": Image.open(directory + "sister.png"),
             "state": Image.open(directory + "province.png"),
             "term": Image.open(directory + "name.png"),
             "their": Image.open(directory + "their (persons).png"),
             "theirs": Image.open(directory + "their (persons).png"),
             "them": Image.open(directory + "they.png"),
             "themselves": Image.open(directory + "they.png"),
             "they": Image.open(directory + "they.png"),
             "time": Image.open(directory + "time.png"),
             "title": Image.open(directory + "name.png"),
             "trade": Image.open(directory + "business.png"),
             "tribe": Image.open(directory + "people.png"),
             "up": Image.open(directory + "up.png"),
             "upward": Image.open(directory + "up.png"),
             "us": Image.open(directory + "we.png"),
             "watch": Image.open(directory + "watch.png"), # also Image.open(directory + "see.png")
             "we": Image.open(directory + "we.png"),
             "website": Image.open(directory + "website.png"),
             "week": Image.open(directory + "week.png"),
             "woman": Image.open(directory + "woman.png"),
             "work": Image.open(directory + "work.png"),
             "world": Image.open(directory + "world.png"),
             "year": Image.open(directory + "year.png"),
             "you": Image.open(directory + "you.png"),
             "youngster": Image.open(directory + "child.png"),
             "yourself": Image.open(directory + "you.png"),
             "your": Image.open(directory + "your (sing).png"),
             "yours": Image.open(directory + "your (sing).png")}

# list of most common words in origin language
langCommonWords = []

# list of most common words in origin text
textCommonWords = []

# English dictionaries:
#    incomplete -> http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt
#    plaintext -> http://www.mso.anu.edu.au/~ralph/OPTED/
#    check out WordNet Python module

# more info on language dictionaries:
#   http://stackoverflow.com/questions/21395011/python-module-with-access-to-english-dictionaries-including-definitions-of-words


def wordFreq(phrase):
    """
    Takes in a non-empty string of words,
    returns a word frequency dictionary.
    """
    words = (phrase.lower()).split()
    freqs = {}

    def addFreqs():
        # init/change freq value
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1

    for word in words:
        # removes punctuation marks @ end of valid words
        # (meta: use regex in future?)
        if not word.isalnum():
            if not word[-1].isalnum() and word[0].isalnum():
                word = word[:-1]
            elif "-" in word:
                word = word.endswith("-")

        addFreqs()

    return freqs


def sortByUsage(freqs):
    """
    Takes in a dict of words and word frequencies,
    returns dict where:
        keys == frequencies > 1 (sorted in decreasing order)
        vals == lists of words with that frequency
    """
    sortedFreqs = {}

    for word in freqs:
        if freqs[word] > 1:
            if freqs[word] in sortedFreqs:
                sortedFreqs[freqs[word]].append(word)
            else:
                sortedFreqs[freqs[word]] = [word]

    return sortedFreqs


def replaceWords(phrase):
    """
    Given a phrase, determines the most-used words and
    returns the phrase with the second instances of the
    most-used words replaced with foreign words in the
    language of choice.
    """
    rawPhrase = (phrase.lower()).split()
    sortedFreqs = []

    def sortFreqs():
        """
        Creates a list of lists of words sorted
        from lowest to highest frequency.
        """
        wordFreqs = wordFreq(phrase)
        usageFreqs = sortByUsage(wordFreqs)
        relevantWords = []

        for k in sorted(usageFreqs):
            newList = []

            for word in usageFreqs[k]:
                if word in blissDict:
                    newList.append(word)

            if len(newList) > 0:
                sortedFreqs.append(newList)


    def translate():
        acc = {"past": [], "changed": []}
        idx = 0 #for indexing words

        for word in rawPhrase:
            if word in acc["past"] and word in sortedFreqs[-1] and word in blissDict:
                rawPhrase[idx] = blissDict[word] #replace original word w/ foreign word
                sortedFreqs[-1].remove(word)  #remove current most popular word
                acc["changed"].append(word)

            elif word in acc["changed"]:
                rawPhrase[idx] = blissDict[word]

            elif word not in acc["past"]:
                acc["past"].append(word)

            idx += 1


    def reCap():
        """
        Re-capitalizes translated text according to
        capitalizations in original text.
        """
        ct = 0
        phraseList = phrase.split()

        for word in phraseList:
            if word not in blissDict and phraseList[ct] != rawPhrase[ct]:
                if word[0].isupper():
                    rawPhrase[ct] = rawPhrase[ct][0].upper() + rawPhrase[ct][1:]
                ct += 1


    def renderTranslation():
        bgWidth = 2000
        bgHeight = bgWidth/2
        bg = Image.new("RGBA", (bgWidth, bgHeight), (255, 255, 255, 255))
        indent = 0
        line = 0

        for word in rawPhrase:
            if word not in blissDict.keys():
                wordWidth = (fontSize/2) + len(word) * (fontSize/2)
                img = Image.new('RGBA', (wordWidth, fontSize * 10), (255, 255, 255, 255))
                sketch = ImageDraw.Draw(img)
                sketch.text((10, fontSize), word, font=blissFont, fill="black")
                bg.paste(img, (indent % bgWidth, line))
                indent += wordWidth
                line += (indent/bgWidth)*100

            elif word in blissDict.keys():
                bg.paste(blissDict[word], (indent%bgWidth, line))
                indent += blissDict[word].size[0] + 10
                line += (indent/bgWidth)*100

            if indent > bgWidth:
                indent = 0

        bg.show()

    sortFreqs()
    #translate()
    reCap()
    renderTranslation()

replaceWords(aliceInWonderland)
#replaceWords(DFW)
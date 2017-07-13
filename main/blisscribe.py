# Notes
# -----
"""
BLISSCRIBE:

    A Python module for translating input English text into a
    combination of English and Blissymbols for reading.

    Input English text into translate() for output images.

    Users will eventually be able to choose which parts of
    speech to translate and how quickly to translate them.
"""

# Imports
# -------
import collections

import nltk
from PIL import Image, ImageDraw, ImageFont, ImageChops
from pattern.text.en import singularize, lemma

import excerpts
import lexicon


# Constants
# ---------
# --> FONTS & IMAGES
ROMAN_FONT_PATH = "/Users/courtney/Library/Fonts/Helvetica.dfont" #"/Users/courtney/Library/Fonts/BLISGRID.TTF"
HELVETICA = "/Users/courtney/Library/Fonts/Helvetica.dfont"
BLISS_FONT_PATH = "/Users/courtney/Library/Fonts/CcfSymbolFont-bliss-2012.ttf"
IMG_PATH = "/Users/courtney/Documents/creation/programming/\
personal projects/bliss translator/symbols/full/png/whitebg/"
DEFAULT_FONT_SIZE = 30
ROMAN_FONT = ImageFont.truetype(ROMAN_FONT_PATH, DEFAULT_FONT_SIZE)
# --> LANGUAGE
BLISS_DICT = lexicon.bliss_dict
PUNCTUATION = [".", ",", ";", ":", "?", "!", "'", '"', "`", "(", ")"]
# initializing accumulators for translate() helpers below
WORDS_SEEN = collections.defaultdict(bool)
WORDS_CHANGED = collections.defaultdict(bool)


# FUNCTIONS
# =========

# Helpers
# -------

def getWordFreqDict(phrase):
    """
    Returns a dictionary with a frequency count for each
    word from input phrase.
    Used to determine most frequently used words in a text
    for translation purposes.

    :param phrase: str, non-empty string of words
    :return: dict, where...
        key (str) - word in phrase
        val (int) - frequency of word occurrences in phrase
    """
    words = nltk.word_tokenize(phrase)
    freqs = collections.defaultdict(int)

    for word in words:
        freqs[word] += 1

    return freqs


def getWordsFreqDict(freqs):
    """
    Returns a dictionary where each value is a list of
    words occurring at a given frequency (> 1).
    Used to determine most frequently used words in a text
    for translation purposes.

    :param freqs: dict, of words and word frequencies
    :return: dict, where...
        key (int) - word frequency (> 1)
        val (List[str]) - list of words with given frequency
    """
    sorted_freqs = collections.defaultdict(list)

    for word in freqs:
        if freqs[word] > 1:
            sorted_freqs[freqs[word]].append(word)

    return sorted_freqs


def getWordWidth(word, font_size = DEFAULT_FONT_SIZE):
    """
    Returns the width of the given string or Image in pixels.

    :param word: str or Image
    :param font_size: int, font size of given word
    :return: int, word width in pixels
    """
    if type(word) == str:
        return trimHorizontal(getWordImg(word)).size[0]
    else:
        try:
            return word.size[0]
        except AttributeError:
            return font_size


def makeBlankImg(x, y):
    """
    Returns a blank image of dimensions x and y.

    :param x: int, x-dimension of image
    :param y: int, y-dimension of image
    :return: Image, blank image
    """
    return Image.new("RGBA", (x, y), (255, 255, 255, 255))


def getWordImg(word, font_size = DEFAULT_FONT_SIZE):
    """
    Draws and returns an Image of the given string.

    :param word: str, word to render to Image
    :param font_size: int, desired font size of text
    :return: Image, image of input str
    """
    img = makeBlankImg(len(word) * font_size, font_size * 5)
    sketch = ImageDraw.Draw(img)
    font = ImageFont.truetype(ROMAN_FONT_PATH, font_size)
    sketch.text((0, font_size), word, font=font, fill="black")

    return trimHorizontal(img)


def getBlissImg(word, max_width = DEFAULT_FONT_SIZE*10, max_height = DEFAULT_FONT_SIZE*3):
    """
    Draws and returns a thumbnail Image of the given str's Blissymbol,
    with a maximum width of max_width, and custom height if desired.

    :param word: str, word to render to Image
    :param max_width: int, maximum width of Blissymbol
    :param max_height: int, maximum height of Blissymbol
    :return: Image, image of input str's Blissymbol
    """
    bliss_word = Image.open(IMG_PATH + BLISS_DICT[word])  # string -> Bliss image
    img = bliss_word
    img.thumbnail((max_width, max_height))

    return img


def getWordAndTag(word):
    """
    Returns a tuple of the given word and its tag.

    :param word: str, word to tag
    :return: (str, str) tuple, given word and its tag
    """
    return nltk.pos_tag([word])[0]


def getWordTag(word):
    """
    Returns the given word's tag.

    Caution: tagging single words outside the context of
    a sentence results in higher errors.

    :param word: str, word to tag
    :return: str, given word's tag
    """
    return getWordAndTag(word)[1]


def tagsToDict(token_phrase):
    """
    Given a list of strings composing a phrase, returns a dict of words
    and word part-of-speech tags, where only words that can be translated
    into Blissymbols form the dict's keys.

    All relevant parts-of-speech tags are enumerated here:
    https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

    :param token_phrase: List[str], list of word tokens from a phrase
    :return: dict, where...
        key (str) - word from phrase translatable into a Blissymbol
        val (str) - key word part-of-speech tag
    """
    # TODO: expand valid_phrases as much as possible
    # TODO: translate plural nouns by translating the singular root and adding plural ending
    # TODO: edit to translate all conjugations of verbs
    tagged_phrase = nltk.pos_tag(token_phrase)  # tokens tagged according to word type
    tagged_dict = {}
    valid_phrases = ["NN", "NNS", "POS", "VB", "VBD", "VBG", "VBN",
                     "RB", "RBR", "RBS", "JJ", "JJR", "JJS"]         # desirable tags (nouns, verbs, adjectives)

    for tup in tagged_phrase:
        if isTranslatable(tup[0]) and tup[1] in valid_phrases:
            tagged_dict[getLexeme(tup[0])] = tup[1]

    return tagged_dict


def sortFreqs(phrase):
    """
    Returns a list of word sets in phrase
    sorted from lowest to highest frequency.

    :param phrase: str, input string of words
    :return: List[str], a list of word sets from phrase
    """
    word_freqs = getWordFreqDict(phrase)
    usage_freqs = getWordsFreqDict(word_freqs)
    sorted_freqs = []

    for key in sorted(usage_freqs):
        new_set = set([])

        for word in usage_freqs[key]:
            if word in BLISS_DICT.keys():
                new_set.add(word)

        if len(new_set) > 0:
            sorted_freqs.append(new_set)

    return sorted_freqs


def trim(img):
    """
    Trims the input image's whitespace.

    :param img: Image, image to be trimmed
    :return: Image, trimmed image

    Taken from http://stackoverflow.com/questions/10615901/trim-whitespace-using-pil/29192070.
    """
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()

    if bbox:
        return img.crop(bbox)


def trimHorizontal(img):
    """
    Trims the input image's whitespace only
    in the x-dimension.

    :param img: Image, image to be trimmed
    :return: Image, trimmed image

    Taken from http://stackoverflow.com/questions/10615901/trim-whitespace-using-pil/29192070.
    """
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    bbox = (bbox[0], 0, bbox[2], img.size[1])

    if bbox:
        return img.crop(bbox)


def getLexeme(word):
    """
    Retrieves the given word's lexeme,
    i.e., the word in dictionary entry form.

    e.g. getLexeme(ran) -> "run"
         getLexeme(puppies) -> "puppy"

    Note: if a lexeme for the given word cannot
    be found, this function returns the input.

    :param word: str, word to convert to lexeme
    :return: str, lexeme of input word
    """
    if isPluralNoun(word):
        lexeme = singularize(word)
    elif isVerb(word):
        lexeme = lemma(word)
    else:
        lexeme = word

    return lexeme


def isNoun(word):
    """
    Returns True if word is a noun, False otherwise.

    :param word: str, word to test whether a noun
    :return: bool, whether given word is a noun
    """
    tag = getWordTag(word)
    return tag[0:2] == "NN"


def isPluralNoun(word):
    """
    Returns True if word is a plural noun, False otherwise.

    :param word: str, word to test whether a plural noun
    :return: bool, whether given word is a plural noun
    """
    return getWordTag(word) == "NNS"


def isVerb(word):
    """
    Returns True if word is a verb, False otherwise.

    :param word: str, word to test whether a verb
    :return: bool, whether given word is a verb
    """
    tag = getWordTag(word)
    return tag[0:2] == "VB"


def isAdj(word):
    """
    Returns True if word is an adjective, False otherwise.

    :param word: str, word to test whether an adjective
    :return: bool, whether given word is an adjective
    """
    tag = getWordTag(word)
    return tag[0:2] == "JJ"


def isTranslatable(word):
    """
    Returns True if word or word lexeme can be translated to
    Blissymbols, False otherwise.

    :param word: str, word to test whether translatable
    :return: bool, whether given word is translatable
    """
    return getLexeme(word) in BLISS_DICT


def tagTranslatable(word):
    """
    Prefixes given Blissymbol-translatable word with @BLISS@.

    :param word: str, word to prefix with @BLISS@
    :return: str, word prefixed with @BLISS@
    """
    return "@BLISS@" + word


def tagTranslatables(phrase):
    """
    Tags each Blissymbol-translatable word in phrase with @BLISS@
    to indicate which words to render as Blissymbol images.

    :param phrase: List[str], words to be translated
    :return: List[str], phrase with translatable words tagged
    """
    idx = 0
    new_phrase = phrase

    for word in phrase:
        if isTranslatable(word):
            new_phrase[idx] = tagTranslatable(word)
        idx += 1

    return new_phrase


def createTranslation(phrase):
    # TODO: finish this
    new_phrase = tagTranslatables(phrase)

    for word in new_phrase:
        if isTranslatable(word):
            word_img = getBlissImg(getLexeme(word))
        else:
            word_img = getWordImg(word)


def drawAlphabet(words, columns=20):
    """
    Draws an alphabet-style Image with definitions for given words,
    with word definition on bottom and corresponding Blissymbol on top.

    :param words: str, words (separated by spaces) to be rendered
    :param columns: int, maximum number of columns
    :return: Image, drawn alphabet of given words
    """
    words_list = words.split(" ")

    glyph_bg_wh = 200
    start = glyph_bg_wh / 2
    space = DEFAULT_FONT_SIZE

    bliss_alphabet = []

    for word in words_list:
        bg = makeBlankImg(glyph_bg_wh, glyph_bg_wh)

        if isTranslatable(word):
            lexeme = getLexeme(word)
            bliss_word = getBlissImg(lexeme, glyph_bg_wh, max_height=DEFAULT_FONT_SIZE * 3)
            eng_word = getWordImg(word.upper(), font_size=DEFAULT_FONT_SIZE / 2)

            bliss_word = trim(bliss_word)
            eng_word = trim(eng_word)

            start_eng_word_x = start - (eng_word.width / 2)
            start_eng_word_y = glyph_bg_wh - eng_word.height - int(space * 3.3)
            start_bliss_word_x = start - (getWordWidth(bliss_word) / 2)
            bg.paste(eng_word, (start_eng_word_x, start_eng_word_y))
            bg.paste(bliss_word, (start_bliss_word_x, space))

        bliss_alphabet.append(bg)

    alphabet_bg_width = glyph_bg_wh * min(len(bliss_alphabet), columns)
    alphabet_bg_height = glyph_bg_wh * (len(bliss_alphabet) / columns + 1)
    alphabet_bg = makeBlankImg(alphabet_bg_width, alphabet_bg_height)
    indent = 0
    line_height = 0

    for defn in bliss_alphabet:
        if (indent + glyph_bg_wh) > alphabet_bg_width:
            indent = 0
            line_height += 1

        if (line_height * glyph_bg_wh) > alphabet_bg_height:
            alphabet_bg.show()
            alphabet_bg = makeBlankImg(alphabet_bg_width, alphabet_bg_height)

        alphabet_bg.paste(defn, (indent, (line_height * glyph_bg_wh)))
        indent += glyph_bg_wh

    return trim(alphabet_bg)


def displayImages(pages):
    """
    Displays each image in pages.

    :param pages: List[Image], images to display
    :return: None
    """
    for page in pages:
        page.show()


def isSeen(word):
    """
    Returns True if the given word is part of the
    WORDS_SEEN dict.

    :param word: str, word to check if in WORDS_SEEN
    :return: bool, whether given word is in WORDS_SEEN
    """
    global WORDS_SEEN
    return word in WORDS_SEEN


def addSeen(word):
    """
    Adds word to WORDS_SEEN dict.

    :param word: str, word to add to WORDS_SEEN
    :return: None
    """
    global WORDS_SEEN
    WORDS_SEEN[word] = True


def isChanged(word):
    """
    Returns True if the given word is part of the
    WORDS_CHANGED dict.

    :param word: str, word to check if in WORDS_CHANGED
    :return: bool, whether given word is in WORDS_CHANGED
    """
    global WORDS_CHANGED
    return word in WORDS_CHANGED


def addChanged(word):
    """
    Adds word to WORDS_CHANGED dict.

    :param word: str, word to add to WORDS_CHANGED
    :return: None
    """
    global WORDS_CHANGED
    WORDS_CHANGED[word] = True


# Translator
# ----------

def translate(phrase):
    """
    Displays image of input English text partially translated to Blissymbols.

    :param phrase: str, non-empty English text
    :return: None
    """
    token_phrase = nltk.word_tokenize(phrase)  # phrase split into word tokens
    tagged_dict = tagsToDict(token_phrase)
    sorted_freqs = sortFreqs(phrase)

    raw_phrase = [word.lower() for word in token_phrase]  # token words in lowercase
    pages = []

    bg_width = 2000
    bg_height = bg_width/2
    bg = makeBlankImg(bg_width, bg_height)

    indent = DEFAULT_FONT_SIZE
    #margins = 10  # pixels of space @ top & bottom margins
    line_no = 0

    idx = 0

    for word in raw_phrase:
        lexeme = getLexeme(word)

        if isTranslatable(word):
            # if word can be validly translated into Blissymbols...
            if isSeen(lexeme) or isChanged(lexeme):
                # if we've already seen or translated the word before...
                try:
                    getBlissImg(lexeme, bg_width / 2)
                except KeyError:
                    idx +=1
                    continue
                except IOError:
                    idx += 1
                    continue
                else:
                    if isChanged(lexeme):
                        img = getBlissImg(lexeme, bg_width / 2)
                    else:
                        # adds subtitles to new words
                        img = drawAlphabet(word)
                        addChanged(lexeme)
                """
                try:
                    #sorted_freqs[-1]
                    if lexeme in sorted_freqs[-1]:
                        # removes word from sorted_freqs
                        addChanged(lexeme)

                        if len(sorted_freqs[-1]) > 1:
                            sorted_freqs[-1].remove(lexeme)
                        else:
                            sorted_freqs.remove(sorted_freqs[-1])
                except IndexError:
                    pass
                else:
                    if lexeme in sorted_freqs[-1]:
                        # removes word from sorted_freqs
                        addChanged(lexeme)

                        if len(sorted_freqs[-1]) > 1:
                            sorted_freqs[-1].remove(lexeme)
                        else:
                            sorted_freqs.remove(sorted_freqs[-1])
                            """

            else:
                # if we haven't seen or translated the word before,
                # then render English text
                img = getWordImg(token_phrase[idx])
                addSeen(lexeme)

        else:
            # if word can't be translated to Blissymbols,
            # then render English text
            img = getWordImg(token_phrase[idx])

        if raw_phrase[idx] in PUNCTUATION or "'" in raw_phrase[idx][:2]:
            # TODO: modify for ( and )
            if raw_phrase[idx] != "(":
                space = 0
        else:
            space = int(DEFAULT_FONT_SIZE / 1.5)

        x_inc = indent + getWordWidth(img) + space
        y_inc = DEFAULT_FONT_SIZE * 3

        try:
            raw_phrase[idx+1]
        except IndexError:
            pass
        else:
            if raw_phrase[idx+1] in PUNCTUATION or raw_phrase[idx-1] in PUNCTUATION:
                if (x_inc + getWordWidth(raw_phrase[idx+1])) > bg_width:
                    # don't let PUNCTUATION trail onto next line alone
                    indent = 0
                    line_no += 1
                elif raw_phrase[idx-1] == "(":
                    space = max(0, space - int(DEFAULT_FONT_SIZE / 1.5))
            elif x_inc > bg_width:
                indent = 0
                line_no += 1
            elif raw_phrase[idx] == "\n":
                # for new paragraphs
                indent = int(DEFAULT_FONT_SIZE)
                line_no += 1

        if y_inc + (line_no * y_inc) > bg_height:
            pages.insert(0, bg)
            bg = makeBlankImg(bg_width, bg_height)
            line_no = 0

        # TODO: modify paste to work with vector bliss files
        bg.paste(img, (indent + space, line_no * y_inc))
        indent += getWordWidth(img) + space
        idx += 1

        try:
            raw_phrase[idx]
        except IndexError:
            pages.insert(0, bg)

    displayImages(pages)
    #writePdf(phrase[20], pages)

translate(excerpts.alice_in_wonderland)
#translate(excerpts.texts[0][:500])

# TODO: launch WordNet app so you can derive definitions for any words (even foreign), or look up synonyms to translate to


# Experimental
# ------------

'''
def saveImages(pages):
    """
    Saves each page in pages as a separate image file.

    :param pages: List[Image], images to save to file
    :return: None
    """
    page_name = 0
    for page in pages:
        page.save(str(page_name))
        page_name += 1


def writePdf(filename, page_names):
    """
    Fetches Image filenames from page_names and pastes Images
    to a page in a .pdf file.

    Images are pasted in exact size.

    :param filename: str, desired name for output .pdf file
    :param page_names: List[str], list of image filenames
    :return: None
    """
    # TODO: get working for actual PDFs
    for page_name in page_names:
        c = canvas.Canvas(filename + '.pdf')
        c.drawImage(page_name, 0, 0)
        c.showPage()
        c.save()
'''
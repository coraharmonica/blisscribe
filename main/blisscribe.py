# Imports
# -------
import collections

import nltk
from PIL import Image, ImageDraw, ImageFont, ImageChops

import excerpts
import lexicon

# Constants
# ---------
roman_font_path = "/Users/courtney/Library/Fonts/BLISGRID.TTF"
# Helvetica: "/Library/Fonts/Helvetica.dfont
bliss_font_path = "/Users/courtney/Library/Fonts/CcfSymbolFont-bliss-2012.ttf"
img_path = "/Users/courtney/Documents/creation/programming/\
personal projects/bliss translator/symbols/full/png/whitebg/"
default_font_size = 30
roman_font = ImageFont.truetype(roman_font_path, default_font_size)
bliss_dict = lexicon.bliss_dict
punctuation = [".", ",", ";", ":", "?", "!", "'", '"', "`"]


# FUNCTIONS
# =========

# Helpers
# -------

def getWordFreqDict(phrase):
    """
    Returns a dictionary with a frequency count for each
    word from input phrase.

    :param phrase: str, non-empty string of words
    :return: dict, word frequency dictionary for phrase
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

    :param freqs: dict, of words and word frequencies
    :return: dict, where...
        key (int) frequency > 1
        val (list) list of words with given frequency
    """
    sorted_freqs = collections.defaultdict(list)

    for word in freqs:
        if freqs[word] > 1:
            sorted_freqs[freqs[word]].append(word)

    return sorted_freqs


def getWordWidth(word, font_size=default_font_size):
    """
    Returns the width of the given string or Image in pixels.

    :param word: str or Image
    :return: int, word width in pixels
    """
    if type(word) == str:
        return len(word) * (font_size / 2)
    else:
        return word.size[0]


def getWordImg(word, font_size=default_font_size):
    """
    Draws and returns an Image of the given string.

    :param word: str
    :param font_size: int, desired font size of text
    :return: Image, image of input str
    """
    word_width = getWordWidth(word, font_size)
    img = Image.new('RGBA', (word_width, font_size * 5), (255, 255, 255, 255))
    sketch = ImageDraw.Draw(img)
    font = ImageFont.truetype(roman_font_path, font_size)
    sketch.text((0, font_size), word, font=font, fill="black")

    return img


def getBlissImg(word, max_width=default_font_size * 10, max_height=default_font_size * 3):
    """
    Draws and returns a thumbnail Image of the given str's Blissymbol,
    with a maximum width of max_width, and custom height if desired.

    :param word: str
    :param max_width: int, maximum width of Blissymbol
    :param max_height: int, maximum height of Blissymbol
    :return: Image, image of input str's Blissymbol
    """
    bliss_word = Image.open(img_path + bliss_dict[word])  # string -> Bliss image
    img = bliss_word
    img.thumbnail((max_width, max_height))

    return img


def tagsToDict(token_phrase):
    """
    Given a list of word tokens in a phrase, returns a
    dictionary of Blissymbols that can be translated into
    said tokens.

    :param token_phrase: list, of word tokens from a phrase
    :return: dict, of translatable Blissymbols and their tokens
    """
    tagged_phrase = nltk.pos_tag(token_phrase)  # tokens tagged according to word type
    tagged_dict = {}
    valid_phrases = ["NN", "NNS", "VB", "JJ", "VBD"]   # desirable tags (nouns, verbs, adjectives)
    # TODO: expand valid_phrases as much as possible
    # TODO: translate plural nouns by translating the singular root and adding plural ending

    for tup in tagged_phrase:
        if tup[1] in valid_phrases and tup[0] in bliss_dict:
            tagged_dict[tup[0]] = tup[1]

    return tagged_dict


def sortFreqs(phrase):
    """
    Returns a list of word sets in phrase
    sorted from lowest to highest frequency.

    :param phrase: str, input string of words
    :return: list, a list of word sets from phrase
    """
    word_freqs = getWordFreqDict(phrase)
    usage_freqs = getWordsFreqDict(word_freqs)
    sorted_freqs = []

    for k in sorted(usage_freqs):
        new_set = set([])

        for word in usage_freqs[k]:
            if word in bliss_dict.keys():
                new_set.add(word)

        if len(new_set) > 0:
            sorted_freqs.append(new_set)

    return sorted_freqs


def trim(img):
    # From http://stackoverflow.com/questions/10615901/trim-whitespace-using-pil/29192070
    bg = Image.new(img.mode, img.size, img.getpixel((0,0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return img.crop(bbox)


def renderAlphabet(words, columns=20):
    """
    Renders an alphabet-style set of definitions for given words,
    with word definition on top and corresponding Blissymbol on bottom.

    :param words: str, words (separated by spaces) to be rendered
    :param columns: int, maximum number of columns
    :return: Image, rendered alphabet of given words
    """
    words_list = words.split(" ")

    glyph_bg_wh = 200
    start = glyph_bg_wh/2
    space = default_font_size

    bliss_alphabet = []

    for word in words_list:
        bg = Image.new("RGBA", (glyph_bg_wh, glyph_bg_wh), (255, 255, 255, 255))

        if word in lexicon.bliss_dict.keys():
            bliss_word = getBlissImg(word, glyph_bg_wh, max_height=default_font_size*3)
            eng_word = getWordImg(word.upper(), font_size=default_font_size/2)

            bliss_word = trim(bliss_word)
            eng_word = trim(eng_word)

            start_eng_word_x = start - (eng_word.width/2)
            start_eng_word_y = glyph_bg_wh - eng_word.height - int(space * 3.3)
            start_bliss_word_x = start - (getWordWidth(bliss_word)/2)

            bg.paste(eng_word, (start_eng_word_x, start_eng_word_y))
            bg.paste(bliss_word, (start_bliss_word_x, space))

        bliss_alphabet.append(bg)

    alphabet_bg_width = glyph_bg_wh * min(len(bliss_alphabet), columns)
    alphabet_bg_height = glyph_bg_wh * (len(bliss_alphabet)/columns + 1)
    alphabet_bg = Image.new("RGBA", (alphabet_bg_width, alphabet_bg_height), (255, 255, 255, 255))
    indent = 0
    line_height = 0

    for defn in bliss_alphabet:
        if (indent + glyph_bg_wh) > alphabet_bg_width:
            indent = 0
            line_height += 1

        if line_height * glyph_bg_wh > alphabet_bg_height:
            alphabet_bg.show()
            alphabet_bg = Image.new("RGBA", (alphabet_bg_width, alphabet_bg_height), (255, 255, 255, 255))

        alphabet_bg.paste(defn, (indent, line_height * glyph_bg_wh))
        indent += glyph_bg_wh

    return trim(alphabet_bg)


# Translator
# ----------

def translate(phrase):
    """
    Displays image of input English text partially translated to Blissymbols.

    :param phrase: str, non-empty English text
    """
    token_phrase = nltk.word_tokenize(phrase)  # phrase split into word tokens
    tagged_dict = tagsToDict(token_phrase)
    sorted_freqs = sortFreqs(phrase)

    def renderTranslation():
        """
        Renders image of English text and Blissymbols.
        """
        # TODO: make spacing between punctuation/words pretty
        # TODO: lern 2 kern
        raw_phrase = [word.lower() for word in token_phrase]  # token words in lowercase
        pages = []

        if len(raw_phrase) == 1:
            bg_width = 200
            bg_height = 200
        else:
            bg_width = 2100
            bg_height = bg_width/2

        indent = default_font_size
        #margins = 10  # pixels of space at the top & bottom margins
        line_no = 0
        bg = Image.new("RGBA", (bg_width, bg_height), (255, 255, 255, 255))

        seen = set([])
        changed = set([])
        idx = 0

        for word in raw_phrase:
            if word in tagged_dict.keys():
                # if word can be validly translated into Blissymbols...
                if word in seen or word in changed:
                    # if we've already seen or translated the word before...
                    try:
                        getBlissImg(word, bg_width / 2)
                    except KeyError:
                        idx +=1
                        continue
                    except IOError:
                        idx += 1
                        continue
                    else:
                        if word in changed:
                            img = getBlissImg(word, bg_width / 2)
                        else:
                            # adds subtitles to new words
                            img = renderAlphabet(word)
                            changed.add(word)

                    try:
                        sorted_freqs[-1]
                    except IndexError:
                        pass
                    else:
                        if word in sorted_freqs[-1]:
                            # removes word from sorted_freqs
                            changed.add(word)

                            if len(sorted_freqs[-1]) > 1:
                                sorted_freqs[-1].remove(word)
                            else:
                                sorted_freqs.remove(sorted_freqs[-1])

                else:
                    # if we haven't seen or translated the word before,
                    # then render English text
                    img = getWordImg(token_phrase[idx])
                    seen.add(word)

            else:
                # if word can't be translated to Blissymbols,
                # then render English text
                img = getWordImg(token_phrase[idx])

            try:
                raw_phrase[idx+1]
            except IndexError:
                pass
            else:
                if raw_phrase[idx] in punctuation or "'" in raw_phrase[idx][:2]:
                    # TODO: modify for ( and )
                    space = 0
                else:
                    space = int(default_font_size / 1.5)

            x_inc = indent + getWordWidth(img) + space
            y_inc = default_font_size * 3

            try:
                raw_phrase[idx+1]
            except IndexError:
                pass
            else:
                if not raw_phrase[idx+1].isalpha():
                    if (x_inc + getWordWidth(raw_phrase[idx+1])) > bg_width:
                        # don't let punctuation trail onto next line alone
                        indent = 0
                        line_no += 1
                elif x_inc > bg_width:
                    indent = 0
                    line_no += 1
                elif raw_phrase[idx] == "\n":
                    # for new paragraphs
                    indent = int(default_font_size)
                    line_no += 1

            if y_inc + (line_no * y_inc) > bg_height:
                pages.insert(0, bg)
                bg = Image.new("RGBA", (bg_width, bg_height), (255, 255, 255, 255))
                line_no = 0

            # TODO: modify paste to work with vector bliss files
            bg.paste(img, (indent + space, line_no * y_inc))
            indent += getWordWidth(img) + space
            idx += 1

            try:
                raw_phrase[idx]
            except IndexError:
                pages.insert(0, bg)

        for page in pages:
            page.show()

    renderTranslation()

translate(excerpts.alice_in_wonderland)
#translate(excerpts.wizard_of_oz)
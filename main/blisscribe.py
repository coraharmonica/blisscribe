# Imports
# -------
import collections
import nltk
# To update NLTK:
#  from nltk import downloader
#  nltk.downloader.download()
from PIL import Image, ImageDraw, ImageFont
import excerpts
import lexicon


# Constants
# ---------
roman_font_path = "/Users/courtney/Library/Fonts/BLISGRID.TTF"
# Helvetica: "/Library/Fonts/Helvetica.dfont
bliss_font_path = "/Users/courtney/Library/Fonts/CcfSymbolFont-bliss-2012.ttf"
img_path = "/Users/courtney/Documents/creation/programming/\
personal projects/bliss translator/symbols/full/png/whitebg/"
font_size = 30
roman_font = ImageFont.truetype(roman_font_path, font_size)
bliss_dict = lexicon.bliss_dict


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


def getWordWidth(word):
    """
    Returns the width of the given string or Image in pixels.

    :param word: str or Image
    :return: int, word width in pixels
    """
    if type(word) == str:
        return (font_size / 2) + len(word) * (font_size / 2)
    else:
        return word.size[0] + 10


def getWordImg(word):
    """
    Draws and returns an Image of the given string.

    :param word: str
    :return: Image, image of input str
    """
    word_width = getWordWidth(word)
    img = Image.new('RGBA', (word_width, font_size * 10), (255, 255, 255, 255))
    sketch = ImageDraw.Draw(img)
    sketch.text((10, font_size), word, font=roman_font, fill="black")

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
    valid_phrases = ["NN", "VB", "JJ", "VBD"]   # desirable tags (nouns, verbs, adjectives)
    # TODO: expand valid_phrases as much as possible

    for tup in tagged_phrase:
        if tup[0] in bliss_dict and tup[1] in valid_phrases:
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
        raw_phrase = [word.lower() for word in token_phrase]  # token words in lowercase

        bg_width = 2400
        bg_height = bg_width/2
        indent = 0
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
                        bliss_dict[word]
                    except KeyError:
                        continue
                    else:
                        bliss_word = Image.open(img_path + bliss_dict[word])          # string -> Bliss image
                        img = bliss_word
                        img.thumbnail((bg_width / 2, font_size * 3))

                    if word in sorted_freqs[-1]:
                        # removes word from sorted_freqs
                        changed.add(word)

                        if len(sorted_freqs[-1]) > 1:
                            sorted_freqs[-1].remove(word)
                        else:
                            sorted_freqs.remove(sorted_freqs[-1])

                    # TODO: modify following code so that supertitles appear above words translated first time
                    '''
                    if word not in changed:
                        super_title = getWordImg(token_phrase[idx])
                        new = Image.new("RGBA", (max(getWordWidth(img), getWordWidth(super_title)), img.size[1] + super_title.size[1]), (255,255,255,255))
                        new.paste(super_title, (0, 0))
                        new.paste(bliss_word, (0, bliss_word.size[1]))
                        img = new
                    '''

                else:
                    # if we haven't seen or translated the word before,
                    # then render English text
                    img = getWordImg(token_phrase[idx])
                    seen.add(word)

            else:
                # if word can't be translated to Blissymbols,
                # then render English text
                img = getWordImg(token_phrase[idx])

            if indent + getWordWidth(img) > bg_width:
                indent = 0
                line_no += 1

            if (line_no * 100) + 100 > bg_height:
                bg.show()
                bg = Image.new("RGBA", (bg_width, bg_height), (255, 255, 255, 255))
                line_no = 0

            # TODO: modify paste to work with vector bliss files
            bg.paste(img, (indent, line_no * (font_size * 3)))
            indent += getWordWidth(img)
            idx += 1

        bg.show()

    renderTranslation()

#translate(excerpts.alice_in_wonderland)
translate(excerpts.wizard_of_oz)
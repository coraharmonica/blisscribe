# Readme
# -----
"""
BLISSCRIBE:

    A Python module for translating input English text into a
    combination of English and Blissymbols for reading.

    Input English text into translate() for output images.

    Users will eventually be able to choose which parts of
    speech to translate and how quickly to translate them.

    All relevant parts-of-speech tags (used throughout) and
    their meanings are enumerated here:
    https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
"""

# Imports
# -------
import collections

import nltk
from PIL import Image, ImageDraw, ImageFont, ImageChops
from pattern.text.en import singularize, lemma

import lexicon


class BlissTranslator:
    """
    A class for translating English text to Images with a
    combination of English text and Blissymbols.

    Input a string with English text to translate() to render
    English text partially replaced with Blissymbols.

    Use chooseTranslatables() to set whether to translate nouns,
    verbs, adjectives, and/or other parts of speech.
    By default, a BlissTranslator will translate all parts of
    speech in VALID_PHRASES, i.e., nouns, verbs, and adjectives.
    To translate all other parts of speech, set self.other to True.
    """

    # Fonts
    # -----
    ROMAN_FONT_PATH = "/Users/courtney/Library/Fonts/BLISGRID.TTF"
    HELVETICA = "/Users/courtney/Library/Fonts/Helvetica.dfont"
    BLISS_FONT_PATH = "/Users/courtney/Library/Fonts/CcfSymbolFont-bliss-2012.ttf"
    DEFAULT_FONT_SIZE = 30
    # Images
    # ------
    IMG_PATH = "/Users/courtney/Documents/creation/programming/personal projects/bliss translator/symbols/full/png/whitebg/"
    BLISS_DICT = lexicon.bliss_dict
    # Linguistics
    # -----------
    FULL_STOPS = set([".", ",", ";", ":", "?", "!"])
    PUNCTUATION = set([".", ",", ";", ":", "?", "!", "'", '"', "`", "(", ")"])
    VALID_PHRASES = set(["NN", "NNS", "VB", "VBD", "VBG", "VBN", "JJ", "JJR", "JJS"])
    PARTS_OF_SPEECH = set(["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS",
                           "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$",
                           "RB", "RBR", "RBS", "RP", "TO", "UH", "VB", "VBD", "VBG",
                           "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"])

    # INITIALIZATIONS
    # ===============

    def __init__(self, font_path = ROMAN_FONT_PATH, font_size = DEFAULT_FONT_SIZE):
        # Fonts
        self.font_size = font_size
        self.font_path = font_path
        self.font = self.initFont(self.font_path, self.font_size)
        # Images
        self.image_heights = self.font_size * 5
        self.pages = []
        # Linguistics
        self.words_seen = dict
        self.words_changed = dict
        self.initSeenChanged()
        # --> parts of speech
        self.nouns = True
        self.verbs = True
        self.adjs = True
        self.other = False

    def initFont(self, font_path, font_size):
        """
        Returns an ImageFont with given font_path and font_size,
        or, if font_path is invalid, returns an ImageFont with a
        default Roman font in font_size.

        :param font_path: str, path to font file
        :param font_size: int, desired font size
        :return: ImageFont, font with given path and font size
        """
        try:
            ImageFont.truetype(font_path, font_size)
        except IOError:
            self.font_path = self.ROMAN_FONT_PATH
            return ImageFont.truetype(self.ROMAN_FONT_PATH, font_size)
        else:
            return ImageFont.truetype(font_path, font_size)

    def initSeenChanged(self):
        """
        Initializes words_seen and words_changed as a default dict.

        :return: None
        """
        self.words_seen = collections.defaultdict(bool)
        self.words_changed = collections.defaultdict(bool)


    # IMAGES
    # ======

    def getWordWidth(self, word):
        """
        Returns the width of the given string or Image in pixels.

        :param word: str or Image
        :return: int, word width in pixels
        """
        if type(word) == str:
            return self.trimHorizontal(self.getWordImg(word, self.font_size)).size[0]
        else:
            try:
                return word.size[0]
            except AttributeError:
                return self.font_size

    def makeBlankImg(self, x, y):
        """
        Returns a blank image of dimensions x and y.

        :param x: int, x-dimension of image
        :param y: int, y-dimension of image
        :return: Image, blank image
        """
        return Image.new("RGBA", (x, y), (255, 255, 255, 255))

    def getWordImg(self, word, font_size=DEFAULT_FONT_SIZE):
        """
        Draws and returns an Image of given word in given font_size.

        :param word: str, word to render to Image
        :param font_size: int, desired font size for string
        :return: Image, image of input str
        """
        img = self.makeBlankImg(len(word) * font_size,
                                self.image_heights)
        sketch = ImageDraw.Draw(img)
        sketch.text((0, font_size),
                    word,
                    font=ImageFont.truetype(font=self.font_path, size=font_size),
                    fill="black")
        return self.trimHorizontal(img)

    def getBlissImg(self, word, max_width, max_height):
        """
        Draws and returns a thumbnail Image of the given str's Blissymbol,
        with width not exceeding max_width.

        :param word: str, word to render to Image
        :param max_width: int, maximum width of Image
        :return: Image, image of input str's Blissymbol
        """
        bliss_word = Image.open(BlissTranslator.IMG_PATH +
                                BlissTranslator.BLISS_DICT[word])
        img = bliss_word
        img.thumbnail((max_width, max_height))
        return img

    def trim(self, img):
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
        else:
            return img

    def trimHorizontal(self, img):
        """
        Trims the input image's whitespace only
        in the x-dimension.

        :param img: Image, image to be trimmed
        :return: Image, trimmed image

        Adapted from http://stackoverflow.com/questions/10615901/trim-whitespace-using-pil/29192070.
        """
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
        diff = ImageChops.difference(img, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        bbox = (bbox[0], 0, bbox[2], img.size[1])

        if bbox:
            return img.crop(bbox)
        else:
            return img

    def incLine(self, line_no, inc=DEFAULT_FONT_SIZE * 3):
        """
        Returns current line_no multiplied by inc to get the
        y-coordinate for this line in pixels.

        :param line_no: int, the current line number
        :param inc: int, factor to multiply line_no by
        :return: int, y-coordinate for this line (in px)
        """
        return line_no * inc

    def getSubtitleSize(self):
        """
        Returns a font size suitable as a subtitle for this
        BlissTranslator's default font_size.

        :return: int, subtitle font size
        """
        return self.font_size - int(self.font_size/2)

    def getSpaceSize(self):
        """
        Returns a space size (in pixels) relative to this BT's
        font_size.

        :return: int, space size (in px)
        """
        return int(self.font_size / 1.5)

    def getMinSpace(self):
        """
        Returns the minimum spacing between characters
        in pixels.
        Useful for standardizing punctuation spacing.

        :return: int, minimum space size (in px)
        """
        return 2

    def drawAlphabet(self, words, columns=10):
        """
        Draws an alphabet-style Image with definitions for given words,
        with word definition on bottom and corresponding Blissymbol on top.

        :param words: str, words (separated by spaces) to be rendered
        :param columns: int, maximum number of columns
        :return: Image, drawn alphabet of given words
        """
        words_list = words.split(" ")

        glyph_bg_wh = self.image_heights
        start = glyph_bg_wh / 2

        bliss_alphabet = []

        for word in words_list:
            bg = self.makeBlankImg(glyph_bg_wh, self.image_heights)

            if self.isTranslatable(word):
                lexeme = self.getLexeme(word)
                bliss_word = self.getBlissImg(lexeme, glyph_bg_wh, self.image_heights / 2)
                eng_word = self.getWordImg(word.upper(), font_size=self.getSubtitleSize())

                bliss_word = self.trim(bliss_word)
                eng_word = self.trim(eng_word)

                bliss_diff_y = (self.font_size*2) - bliss_word.size[1] - eng_word.size[1]

                start_bliss_word_x = start - (self.getWordWidth(bliss_word) / 2)
                start_bliss_word_y = bliss_diff_y
                start_eng_word_x = start - (eng_word.width / 2)
                start_eng_word_y = start_bliss_word_y + bliss_word.size[1] + eng_word.height
                bg.paste(eng_word, (start_eng_word_x, start_eng_word_y))
                bg.paste(bliss_word, (start_bliss_word_x, start_bliss_word_y))

            bliss_alphabet.append(bg)

        alphabet_bg_width = glyph_bg_wh * min(len(bliss_alphabet), columns)
        alphabet_bg_height = glyph_bg_wh * (len(bliss_alphabet) / columns + 1)
        alphabet_bg = self.makeBlankImg(alphabet_bg_width, alphabet_bg_height)
        indent = 0
        line_height = 0

        for defn in bliss_alphabet:
            if (indent + glyph_bg_wh) > alphabet_bg_width:
                indent = 0
                line_height += 1

            if (line_height * glyph_bg_wh) > alphabet_bg_height:
                alphabet_bg.show()
                alphabet_bg = self.makeBlankImg(alphabet_bg_width, alphabet_bg_height)

            alphabet_bg.paste(defn, (indent, self.incLine(line_height, glyph_bg_wh)))
            indent += glyph_bg_wh

        return self.trimHorizontal(alphabet_bg)

    def displayImages(self, pages):
        """
        Displays each image in pages.

        :param pages: List[Image], images to display
        :return: None
        """
        for page in pages:
            page.show()


    # LANGUAGE PROCESSING
    # ===================

    def getWordAndTag(self, word):
        """
        Returns a tuple of the given word and its tag.

        :param word: str, word to tag
        :return: (str, str) tuple, given word and its tag
        """
        return nltk.pos_tag([word])[0]

    def getWordTag(self, word):
        """
        Returns the given word's tag.

        Caution: tagging single words outside the context of
        a sentence results in higher errors.

        :param word: str, word to tag
        :return: str, given word's tag
        """
        return self.getWordAndTag(word)[1]

    def isNoun(self, word):
        """
        Returns True if word is a noun, False otherwise.

        :param word: str, word to test whether a noun
        :return: bool, whether given word is a noun
        """
        tag = self.getWordTag(word)
        return tag[0:2] == "NN"

    def isPluralNoun(self, word):
        """
        Returns True if word is a plural noun, False otherwise.

        :param word: str, word to test whether a plural noun
        :return: bool, whether given word is a plural noun
        """
        return self.getWordTag(word) == "NNS"

    def isVerb(self, word):
        """
        Returns True if word is a verb, False otherwise.

        :param word: str, word to test whether a verb
        :return: bool, whether given word is a verb
        """
        tag = self.getWordTag(word)
        return tag[0:2] == "VB"

    def isAdj(self, word):
        """
        Returns True if word is an adjective, False otherwise.

        :param word: str, word to test whether an adjective
        :return: bool, whether given word is an adjective
        """
        tag = self.getWordTag(word)
        return tag[0:2] == "JJ"

    def getLexeme(self, word):
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
        if self.isPluralNoun(word):
            lexeme = singularize(word)
        elif self.isVerb(word):
            lexeme = lemma(word)
        else:
            lexeme = word
        return lexeme

    def isTranslatable(self, word):
        """
        Returns True if word or word lexeme can be translated to
        Blissymbols, False otherwise.

        :param word: str, word to test whether translatable
        :return: bool, whether given word is translatable
        """
        return self.getLexeme(word) in BlissTranslator.BLISS_DICT

    def chooseNouns(self, nouns):
        """
        Allows user to set whether to translate nouns.

        :param nouns: bool, True to translate nouns
        :return: None
        """
        self.nouns = nouns
        self.setTranslatables()

    def chooseVerbs(self, verbs):
        """
        Allows user to set whether to translate verbs.

        :param verbs: bool, True to translate verbs
        :return: None
        """
        self.verbs = verbs
        self.setTranslatables()

    def chooseAdjs(self, adjs):
        """
        Allows user to set whether to translate adjectives.

        :param adjs: bool, True to translate adjectives
        :return: None
        """
        self.adjs = adjs
        self.setTranslatables()

    def chooseOtherPOS(self, other):
        """
        Allows user to set whether to translate all other
        parts of speech.

        :param other: bool, True to translate other parts of speech
        :return: None
        """
        self.other = other
        self.setTranslatables()

    def chooseTranslatables(self, nouns, verbs, adjs, other):
        """
        Allows user to set whether to translate nouns, verbs,
        adjectives, and/or all other parts of speech.
        Changes this BlissTranslator's variables with the same names.

        :param nouns: bool, True to translate nouns
        :param verbs: bool, True to translate verbs
        :param adjs: bool, True to translate adjectives
        :param other: bool, True to translate all other parts of speech
        :return: None
        """
        self.chooseNouns(nouns)
        self.chooseVerbs(verbs)
        self.chooseAdjs(adjs)
        self.chooseOtherPOS(other)
        self.setTranslatables()

    def setTranslatables(self):
        """
        Resets VALID_PHRASES according to this BlissTranslator's translatables
        (i.e., nouns, verbs, adjs, and other).

        :return: None
        """
        BlissTranslator.VALID_PHRASES = set()

        if self.nouns:
            BlissTranslator.VALID_PHRASES.add("NN")
            BlissTranslator.VALID_PHRASES.add("NNS")
        if self.verbs:
            BlissTranslator.VALID_PHRASES.add("VB")
            BlissTranslator.VALID_PHRASES.add("VBD")
            BlissTranslator.VALID_PHRASES.add("VBG")
            BlissTranslator.VALID_PHRASES.add("VBN")
        if self.adjs:
            BlissTranslator.VALID_PHRASES.add("JJ")
            BlissTranslator.VALID_PHRASES.add("JJR")
            BlissTranslator.VALID_PHRASES.add("JJS")
        if self.other:
            for pos in BlissTranslator.PARTS_OF_SPEECH:
                BlissTranslator.VALID_PHRASES.add(pos)

    def tagsToList(self, token_phrase):
        """
        Given a list of strings composing a phrase, returns a list of words'
        part-of-speech tags in that order.

        All relevant parts-of-speech tags are enumerated here:
        https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

        :param token_phrase: List[str], list of word tokens from a phrase
        :return: List[str], list of word part-to-speech tags
        """
        tagged_phrase = nltk.pos_tag(token_phrase)  # tokens tagged according to word type
        tagged_list = []
        for tup in tagged_phrase:
            tagged_list.append(tup[1])
        return tagged_list

    def isSeen(self, word):
        """
        Returns True if the given word is part of the
        words_seen dict.

        :param word: str, word to check if in words_seen
        :return: bool, whether given word is in words_seen
        """
        return word in self.words_seen

    def addSeen(self, word):
        """
        Adds word to words_seen dict.

        :param word: str, word to add to words_seen
        :return: None
        """
        self.words_seen[word] = True

    def isChanged(self, word):
        """
        Returns True if the given word is part of the
        words_changed dict.

        :param word: str, word to check if in words_changed
        :return: bool, whether given word is in words_changed
        """
        return word in self.words_changed

    def addChanged(self, word):
        """
        Adds word to words_changed dict.

        :param word: str, word to add to words_changed
        :return: None
        """
        self.words_changed[word] = True


    # TRANSLATOR
    # ==========

    def translate(self, phrase, bg_width = 2000):
        """
        Displays image of input English text partially translated to Blissymbols.

        :param phrase: str, non-empty English text
        :param bg_width: int, desired width of image
        :return: None
        """
        token_phrase = nltk.word_tokenize(phrase)             # phrase split into word tokens
        tagged_list = self.tagsToList(token_phrase)
        raw_phrase = [word.lower() for word in token_phrase]  # token words to lowercase

        pages = []

        bg_height = bg_width / 2
        bg = self.makeBlankImg(bg_width, bg_height)
        # margins = self.font_size / 2  # pixels of space @ top & bottom margins
        indent = self.font_size
        line_no = 0

        idx = 0

        for word in raw_phrase:
            lexeme = self.getLexeme(word)

            if self.isTranslatable(word): #and tagged_list[idx] in BlissTranslator.VALID_PHRASES:
                # if word can be validly translated into Blissymbols...
                if True: #self.isSeen(lexeme) or self.isChanged(lexeme):
                    # if we've already seen or translated the word before...
                    try:
                        self.getBlissImg(lexeme, bg_width / 2, self.image_heights)
                    except KeyError:
                        idx += 1
                        continue
                    except IOError:
                        idx += 1
                        continue
                    else:
                        if self.isChanged(lexeme):
                            img = self.getBlissImg(lexeme, bg_width / 2, self.image_heights / 2)
                        else:
                            # adds subtitles to new words
                            img = self.drawAlphabet(word)
                            self.addChanged(lexeme)

                else:
                    # if we haven't seen or translated the word before,
                    # then render English text
                    img = self.getWordImg(token_phrase[idx], self.font_size)
                    self.addSeen(lexeme)

            else:
                # if word can't be translated to Blissymbols,
                # then render English text
                img = self.getWordImg(token_phrase[idx], self.font_size)

            space = self.getSpaceSize()
            x_inc = indent + self.getWordWidth(img) + space
            y_inc = self.font_size * 3

            try:
                raw_phrase[idx+1]
            except IndexError:
                pass
            else:
                if raw_phrase[idx] in BlissTranslator.PUNCTUATION or "'" in raw_phrase[idx][:2]:
                    if raw_phrase[idx] != "(":
                        space = self.getMinSpace()
                elif x_inc > bg_width:
                    indent = 0
                    line_no += 1
                elif raw_phrase[idx] == "\n":
                    # for new paragraphs
                    indent = int(self.font_size)
                    line_no += 1
                elif raw_phrase[idx+1] in BlissTranslator.PUNCTUATION or raw_phrase[idx-1] in BlissTranslator.PUNCTUATION:
                    if (x_inc + self.getWordWidth(raw_phrase[idx+1])) > bg_width:
                        # don't let punctuation trail onto next line alone
                        indent = 0
                        line_no += 1
                    elif raw_phrase[idx-1] == "(":
                        space = self.getMinSpace()
                    elif raw_phrase[idx-1] in BlissTranslator.FULL_STOPS:
                        space = self.getSpaceSize()
                else:
                    space = self.getSpaceSize()

            if (line_no + 1) * y_inc > bg_height:
                # if the next line would go beyond the image,
                # store the current page and go onto a new one
                pages.insert(0, bg)
                bg = self.makeBlankImg(bg_width, bg_height)
                line_no = 0

            # TODO: modify paste to work with vector bliss files (for resizing aesthetics)
            bg.paste(img, (indent + space, self.incLine(line_no, y_inc)))
            indent += self.getWordWidth(img) + space
            idx += 1

            try:
                raw_phrase[idx]
            except IndexError:
                pages.insert(0, bg)

        self.displayImages(pages)
        self.initSeenChanged()

    '''
    def initImports(self):
        try:
            import collections
            import nltk
            from PIL import Image, ImageDraw, ImageFont, ImageChops
            from pattern.text.en import singularize, lemma

            import excerpts
            import lexicon

        except ImportError:
            print("You are missing one of the following libraries:\
            \n  collections\n  nltk\n  PIL\n  pattern.text.en")

        else:
            import collections
            import nltk
            from PIL import Image, ImageDraw, ImageFont, ImageChops
            from pattern.text.en import singularize, lemma

            import excerpts
            import lexicon
    '''

# Testing
# -------

#HelveticaTranslator = BlissTranslator(BlissTranslator.HELVETICA, 20)
#HelveticaTranslator.chooseOtherPOS(True)
#HelveticaTranslator.translate(excerpts.alice_in_wonderland, 1000)

#DefaultTranslator = BlissTranslator()
#DefaultTranslator.translate(excerpts.alice_in_wonderland)
#DefaultTranslator.translate(excerpts.kjv[:5000])
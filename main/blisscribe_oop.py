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
import sys
import os
import collections
import string
import nltk
from nltk.corpus import wordnet
#from nltk.app import wordnet_app
from PIL import Image, ImageDraw, ImageFont, ImageChops
from pattern.text.en import singularize, lemma
from fpdf import FPDF

try:
    import lexicon
    import excerpts
except ImportError:
    print("Lexicon and excerpts modules could not be imported.\n\
    Please try locating the local modules lexicon.py and excerpts.py \n\
    and modifying your sys.path accordingly.")
else:
    import lexicon
    import excerpts


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
    ROMAN_FONT_PATH = "/Users/courtney/Library/Fonts/BLISGRID.TTF"
    HELVETICA = "/Users/courtney/Library/Fonts/Helvetica.dfont"
    BLISS_FONT_PATH = "/Users/courtney/Library/Fonts/CcfSymbolFont-bliss-2012.ttf"
    DEFAULT_FONT_SIZE = 30
    # Images
    IMG_PATH = sys.path[0] + "/symbols/full/png/whitebg/"
    BLISS_DICT = lexicon.bliss_dict
    IMAGES_SAVED = 0
    # Language
    FULL_STOPS = set([".", ",", ";", ":", "?", "!"])
    PUNCTUATION = set([".", ",", ";", ":", "?", "!", "'", '"', "`", "(", ")"])
    VALID_PHRASES = set(["NN", "NNS", "VB", "VBD", "VBG", "VBN", "JJ", "JJR", "JJS"])
    PARTS_OF_SPEECH = set(["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS",
                           "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$",
                           "RB", "RBR", "RBS", "RP", "TO", "UH", "VB", "VBD", "VBG",
                           "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"])

    # INITIALIZATIONS
    # ===============
    def __init__(self, font_path=ROMAN_FONT_PATH, font_size=DEFAULT_FONT_SIZE):
        # Fonts
        self.font_size = font_size
        self.font_path = font_path
        self.font = self.initFont(self.font_path, self.font_size)
        # Images
        self.image_heights = self.font_size * 5
        self.pages = []
        self.sub_all = False
        # Language
        self.words_seen = dict
        self.words_changed = dict
        self.initSeenChanged()
        self.seen_choices = {}
        self.fast_translate = False
        # --> parts of speech
        self.nouns = True
        self.verbs = True
        self.adjs = True
        self.other = False

    def initFont(self, font_path, font_size):
        """
        Returns an ImageFont with given font_path and font_size.
        ~
        If font_path is invalid, returns an ImageFont with a
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

    def setSubAll(self, sub_all):
        """
        Sets self.sub_all equal to input sub_all value.
        ~
        Setting sub_all to True will produce subtitles under
        every Blissymbol.
        Setting sub_all to False will produce subtitles only
        under new Blissymbols.
        ~
        Used for this BlissTranslator's translate() method.

        :param sub_all: bool, whether to subtitle all words in
            input English text to this BlissTranslator
        :return: None
        """
        self.sub_all = sub_all

    def setFastTranslate(self, fast_translate):
        """
        Set's self.fast_translate to fast_translate.
        ~
        Setting fast_translate to True will cause this
        BlissTranslator to translate the first instances of
        every word.
        Setting fast_translate to False will cause it to
        only translate a word after having seen it once.
        ~
        Used for this BlissTranslator's translate() method.

        :param fast_translate: bool, whether to translate
            words to Blissymbols immediately
        :return: None
        """
        self.fast_translate = fast_translate

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

    def chooseDefn(self, word):
        """
        Returns an integer representing user's selection for
        the correct word definition by as an index in given word's
        list of definitions.
        ~
        If list of definitions contains only 1 item, returns 0.

        :param word: str, a word to choose a definition for
        :return: int, the index of the given word's proper definition
        """
        if word not in self.seen_choices.keys():
            defns = BlissTranslator.BLISS_DICT[word]
            assert type(defns) == list
            idx = 1
            print("The word '" + word + "' has multiple definitions:\n")

            for defn in defns:
                print("Definition " + str(idx) + ": " + defn[:-4] + "\n")
                idx += 1

            choice = input("Which of these definitions is most appropriate? ")
            print("\n")

            try:
                defns[choice]
            except IndexError:
                choice = 0
            else:
                choice -= 1  # subtract 1 from choice for 0-based indexing
                self.seen_choices[word] = choice
            return choice
        else:
            return self.seen_choices[word]

    def getBlissImg(self, word, max_width, max_height, choosing=False):
        """
        Draws and returns a thumbnail Image of the given word's
        Blissymbol, with width not exceeding max_width.
        ~
        If a word has multiple meanings, then return the Blissymbol
        corresponding to the first meaning listed in BLISS_DICT.

        :param word: str, word to render to Image
        :param max_width: int, maximum width of Image (in pixels)
        :param max_height: int, maximum height of Image (in pixels)
        :param choosing: bool, whether user can choose definitions for
            ambiguous words
        :return: Image, image of input str's Blissymbol
        """
        if type(BlissTranslator.BLISS_DICT[word]) == list:
            if choosing:
                choice = self.chooseDefn(word)
            else:
                choice = 0
            bliss_word = Image.open(BlissTranslator.IMG_PATH +
                                    BlissTranslator.BLISS_DICT[word][choice])
        else:
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
        Returns an appropriate space size relative to this
        BT's font_size in pixels.

        :return: int, space size (in pixels)
        """
        return int(self.font_size / 1.5)

    def getMinSpace(self):
        """
        Returns the minimum spacing between characters
        in pixels.

        Useful for standardizing punctuation spacing.

        :return: int, minimum space size (in pixels)
        """
        return 2

    def drawAlphabet(self, words, columns=10):
        """
        Returns alphabet-style definition image containing each word in words,
        with word definition on bottom and corresponding Blissymbol on top.
        ~
        If a word in words has no corresponding Blissymbol, this method does
        not draw it.

        :param words: str, words (separated by spaces) to render
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

    def saveImages(self, pages):
        """
        Saves each image in pages as a .png file.
        ~
        Names each image beginning at this BlissTranslator's
        IMAGES_SAVED variable and incrementing by 1.
        ~
        After loop terminates, sets IMAGES_SAVED to the
        final accumulated value.
        ~
        Returns a list of the image filenames created.

        :param pages: List[Image], images to save to file
        :return: None
        """
        filenames = []
        start = BlissTranslator.IMAGES_SAVED

        for page in pages:
            filename = "bliss_img" + str(start) + ".png"
            page.save(filename)
            filenames.append(filename)
            start += 1

        BlissTranslator.IMAGES_SAVED = start
        return filenames

    def makePdf(self, filename, pages, margins=0, delete=True, enumerate=True):
        """
        Pastes each image file linked to in pages to a PDF.
        ~
        Saves PDF under given filename in this directory.
        ~
        If delete is set to True, this method deletes all
        images from pages.
        If delete is set to False, does not delete any
        images from pages.
        ~
        If enumerate is True and phrase extends longer than
        1 page, this method adds a number to the bottom of
        each PDF page.
        If enumerate is False, don't add any numbers.

        Taken from:
        https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images

        :param filename: str, filename for output PDF
        :param pages: List[str], image filenames to paste in PDF
        :param margins: int, space in margins (in pixels)
        :param delete: bool, whether to delete image files
        :param enumerate: bool, whether to enumerate each PDF page
        :return: None
        """
        width, height = Image.open(pages[0]).size
        new_w, new_h = width+(margins*2), height+(margins*2)

        pdf = FPDF(unit="pt", format=[new_w, new_h])
        idx = 0

        for page in pages:
            pdf.add_page()
            pdf.image(page, x=margins, y=margins)
            # TODO: get enumeration to work on PDFs
            if len(pages)>2 and idx>0 and enumerate:
                number = self.getWordImg(str(idx), self.font_size)
                num_fn = "num" + str(idx) + ".png"
                number.save(num_fn)
                pdf.image(num_fn, x=(new_w/2), y=(new_h-(margins/2)))
                os.remove(num_fn)
            if delete:
                os.remove(page)
            idx += 1

        pdf.output(filename + ".pdf", "F")

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

        Caveat: tagging single words outside the context of
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
        be found, this method returns the input.

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
        ~
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

    '''
    # --> HTML

    def getWordPage(self, word):
        """
        Returns a string representing the WordNet HTML page
        for the given word.

        :param word: str, the word to look up on WordNet
        :return: str, the word's HTML page
        """
        return wordnet_app.page_from_word(word)[0]

    def parseHTMLTagStart(self, html):
        """
        Returns the rest of input html string after
        reaching the first intro tag (i.e., "<").
        If no intro tag is reached, return empty string.

        :param html: str, HTML string
        :return: str, HTML string after first "<"
        """
        idx = 0
        for char in html:
            if char == "<":
                try:
                    html[idx+1]
                except IndexError:
                    return ""
                else:
                    return html[idx+1]
            idx += 1
        return ""

    def parseHTMLTagEnd(self, html):
        """
        Returns the first part of input html string up
        until reaching an HTML tag closure (i.e., ">").

        :param html: str, HTML string after HTML beginning
        :return: str, input HTML string up to ">"
        """
        idx = 0
        for char in html:
            if char == ">":
                return html[:idx]
            idx += 1

    def parseHTMLStr(self, html):
        """
        Parses an HTML string for keywords to identify
        which parts of WordNet website each part refers to.

        :param html: str, HTML string for WordNet definition
        :return: str, non-HTML readable string
        """
        headers = []
        defns = {}

        header_now = None
        defn_now = None

        idx = 0

        for char in html:
            rest = html[idx:]
            if rest[:idx+3] == "h3 ":
                pass  # parse header fxn
            elif rest[:idx+14] == "a href lookup ":
                pass  # parse hyperlink fxn
            elif rest[:idx+2] == "b ":
                pass
            elif rest[:idx+2] == "a ":
                pass

    def getStrFromHTML(self, html):
        """
        Returns a simplified string representing the given
        HTML page in a non-HTML readable form.

        :param html: str, a WordNet HTML page
        :return: str, a readable form of the input HTML page
        """

        new_str = []

        for char in html:
            try:
                self.parseHTMLTagEnd(self.parseHTMLTagStart(html))
            except IndexError:
                continue
            else:
                if html[-1] != " ":
                    # no more than 1 space between terms
                    new_str.append(" ")

        new_str = "".join(new_str)
        return new_str

        if html == "":
            return ""
        else:
            new_html = self.parseHTMLTagEnd(self.parseHTMLTagStart(html))
            return new_html + self.getStrFromHTML(new_html)


    def getWordDesc(self, word):
        """
        Returns a simplified string representing the given
        word's WordNet HTML page in a non-HTML readable form.

        :param html: str, the word to look up on WordNet
        :return: str, a readable form of the input HTML page
        """
        return self.getStrFromHTML(self.getWordPage(word))

    # --> HREF

    def getHREFPage(self, href):
        """
        Returns a string representing the given hyperlink.
        Used for synset hyperlinks in HTML strings.

        :param href: str, a hyperlink
        :return: str, a page representing the given hyperlink
        """
        return wordnet_app.page_from_href(href)[0]

    def getHREFStr(self, href):
        """
        Returns a simplified string representing the given
        hyperlink.

        :param href: str, a hyperlink
        :return: str, a page representing the given hyperlink
        """
        href_page = self.getHREFPage(href)
        '''

    def getWordSynsets(self, word):
        """
        Creates a WordNet synset from the given word,
        beginning with the given word at index 0 and
        continuing with its synonyms at further indices.

        WordNet lookup link here:
        http://wordnetweb.princeton.edu/perl/webwn?s=&sub=Search+WordNet

        :param lexeme: str, a word to lookup in WordNet
        :return: List[Synset], the word's synsets
        """
        pos = self.getWordPOS(word)
        synsets = wordnet.synsets(word, pos)
        return synsets

    def getWordPOS(self, word):
        """
        Returns the given word's part of speech, abbreviated as a
        single letter.

        POS constants (from WordNet.py):
            ADJ, ADJ_SAT, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'

        :param word: str, word to determine pos
        :return: str, letter representing input word's pos
        """
        if self.isNoun(word):
            return "n"
        elif self.isVerb(word):
            return "v"
        elif self.isAdj(word):
            return "a"
        elif self.getWordTag(word)[0:2] == "RB":
            return "r"
        elif self.getWordTag(word) == "JJS":
            return "s"

    def translateSynsets(self, synsets):
        """
        Given a list of synsets, attempts to translate each
        synset into Blissymbols.
        ~
        If a synonym is translatable to Blissymbols, return
        that synonym. Otherwise, return the first word in the
        synset.

        :param synsets: List[Synset], a root word and its synonyms
        :return: str, the first word in given synset that can
        be translated to Blissymbols
        """
        for synset in synsets:
            name = synset.name()
            if self.isTranslatable(name):
                return name
        return synsets[0]

    def translateUntranslatable(self, word):
        """
        Attempts to translate the given word's synonyms to
        Blissymbols.
        ~
        If a synonym can be translated, this method returns
        that synonym. Otherwise, this method returns the
        input word.

        :param word: str, word to translate to Blissymbols
        :return: str, translatable synonym of given word
        """
        return self.translateSynsets(self.getWordSynsets(word))

    def getSynsetDefn(self, synset):
        """
        Returns this Synset's definition.

        :param synset: Synset, a WordNet synset
        :return: str, the given synset's definition
        """
        return synset.definition()

    def getWordDefns(self, word, single=False):
        """
        Returns a list of possible definitions for the
        given word.
        ~
        If single is True, then this method will
        return the first definition reached.

        :param word: str, the word to define
        :param single: bool, whether to return the first
            definition reached
        :return: List[str], the word's possible definitions
        """
        defns = []
        synsets = self.getWordSynsets(word)

        for synset in synsets:
            defns.append(self.getSynsetDefn(synset))
            if single:
                return defns

        return defns

    def getWordDefn(self, word):
        """
        Returns the first possible definition for the
        given word.

        :param word: str, the word to define
        :return: str, the word's first possible definition
        """
        return self.getSynsetDefn(self.getWordSynsets(word)[0])

    def getTitle(self, title, phrase):
        """
        Returns a valid title for the given phrase.
        ~
        If input title is None, this method returns the first 20
        alphabetic characters and/or spaces in phrase as a working title.
        Otherwise, this method returns the input title's valid characters.

        :param title: None or str, user-selected title
        :param phrase: str, phrase being titled
        :return: str, valid title for given phrase
        """
        if title is None:
            title = phrase[:20]
        else:
            title = title
        final = ''.join([c for c in title if c.isalpha() or c==" "])
        return final

    def makeTitlePage(self, title, x, y):
        """
        Returns a title page of given dimensions x and y with the given
        title.

        :param title: str, title name
        :param x: int, x-dimension of output title page
        :param y: int, y-dimension of output title page
        :return: Image, title page
        """
        img = self.makeBlankImg(x, y)
        title_img = self.getWordImg(title, self.font_size)

        img_x = x/2 - title_img.size[0]/2
        img_y = y/3

        img.paste(title_img, (img_x, img_y))
        return img



    # TRANSLATOR
    # ==========

    def translate(self, phrase, title=None, img_w=816, img_h=1056):
        """
        Translates this input English phrase to Blissymbols
        according to this BlissTranslator's POS preferences.
        ~
        Saves translation to a PDF file in this directory
        under the first <=20 characters of input phrase.
        ~
        Default image size is 816x1056px.

        :param phrase: str, non-empty English text
        :param title: None or str, desired title for output PDF
        :param img_w: int, desired width of PDF images (in pixels)
        :param img_h: int, desired height of PDF images (in pixels)
        :return: None
        """
        token_phrase = nltk.word_tokenize(phrase)             # phrase split into word tokens
        tagged_list = self.tagsToList(token_phrase)
        raw_phrase = [word.lower() for word in token_phrase]  # token words to lowercase

        new_title = self.getTitle(title, phrase)
        pages = []
        title_page = self.makeTitlePage(new_title, img_w, img_h)
        pages.append(title_page)

        bg = self.makeBlankImg(img_w, img_h)
        indent = self.font_size
        line_no = 0
        idx = 0

        for word in raw_phrase:
            lexeme = self.getLexeme(word)

            if self.isTranslatable(word) and tagged_list[idx] in BlissTranslator.VALID_PHRASES:
                # if word can be validly translated into Blissymbols...
                if self.fast_translate or self.isSeen(lexeme) or self.isChanged(lexeme):
                    # if we've already seen or translated the word before...
                    try:
                        self.getBlissImg(lexeme, img_w/2, self.image_heights)
                    except KeyError:
                        idx += 1
                        continue
                    except IOError:
                        idx += 1
                        continue
                    else:
                        if not self.sub_all and self.isChanged(lexeme):
                            img = self.getBlissImg(lexeme, img_w/2, self.image_heights/2)
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
                elif x_inc > img_w:
                    indent = 0
                    line_no += 1
                elif raw_phrase[idx] == "\n":
                    # for new paragraphs
                    indent = int(self.font_size)
                    line_no += 1
                elif raw_phrase[idx+1] in BlissTranslator.PUNCTUATION or raw_phrase[idx-1] in BlissTranslator.PUNCTUATION:
                    if (x_inc + self.getWordWidth(raw_phrase[idx+1])) > img_w:
                        # don't let punctuation trail onto next line alone
                        indent = 0
                        line_no += 1
                    elif raw_phrase[idx-1] == "(":
                        space = self.getMinSpace()
                    elif raw_phrase[idx-1] in BlissTranslator.FULL_STOPS:
                        space = self.getSpaceSize()
                else:
                    space = self.getSpaceSize()

            if (line_no + 1) * y_inc > img_h:
                # if the next line would go beyond the image,
                # store the current page and go onto a new one
                pages.insert(0, bg)
                bg = self.makeBlankImg(img_w, img_h)
                line_no = 0

            # TODO: modify paste to work with vector bliss files (for resizing aesthetics)
            bg.paste(img, (indent + space, self.incLine(line_no, y_inc)))
            indent += self.getWordWidth(img) + space
            idx += 1

        pages.insert(0, bg)

        self.makePdf(new_title, self.saveImages(pages[::-1]), margins=50)
        self.initSeenChanged()

    '''
    def initImports(self):
        try:
            import collections
            import nltk
            from PIL import Image, ImageDraw, ImageFont, ImageChops
            from pattern.text.en import singularize, lexeme

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

#HelveticaTranslator = BlissTranslator(BlissTranslator.HELVETICA)
#HelveticaTranslator.setSubAll(True)
#HelveticaTranslator.chooseOtherPOS(True)
#HelveticaTranslator.setFastTranslate(True)
#HelveticaTranslator.translate(excerpts.alice_in_wonderland)

DefaultTranslator = BlissTranslator(font_size=20)
#DefaultTranslator.setSubAll(True)
DefaultTranslator.chooseOtherPOS(True)
DefaultTranslator.setFastTranslate(True)
DefaultTranslator.translate(excerpts.alice_in_wonderland, title="Alice in Wonderland")
#DefaultTranslator.translate(excerpts.kjv[:5000])
#fox_desc = DefaultTranslator.getWordDesc("fox")
#print(fox_desc)

'''
def printHypernyms(synsets):
    for synset in synsets:
        print(synset.hypernyms())
'''
#printHypernyms(DefaultTranslator.getWordSynsets("heaven"))
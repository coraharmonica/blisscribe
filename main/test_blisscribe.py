# Notes
# -----
"""
TEST_BLISSCRIBE:

    Python testing suite for blisscribe.py.
    Tests helpers and main translation function.
"""

# Imports
# -------
import unittest

from PIL import Image, ImageDraw, ImageFont

import blisscribe
import excerpts


class blisscribeTest(unittest.TestCase):
    def testGetWordFreqDict(self):
        # empty
        self.assertEqual(blisscribe.getWordFreqDict(""), {})

        # 4-word phrase
        self.assertEqual(blisscribe.getWordFreqDict("hello hello my wife"), {"hello": 2, "my": 1, "wife": 1})


    def testGetWordsFreqDict(self):
        # empty
        self.assertEqual(blisscribe.getWordsFreqDict(blisscribe.getWordFreqDict("")), {})

        # 4-word phrase
        self.assertEqual(blisscribe.getWordsFreqDict(blisscribe.getWordFreqDict("hello hello my wife")), {"hello": 2})


    def testGetWordWidth(self):
        # input str, default font size
        self.assertEqual(blisscribe.getWordWidth("parrot"), len("parrot") * (blisscribe.default_font_size / 2))

        # input str, custom font size
        self.assertEqual(blisscribe.getWordWidth("parrot", 42), len("parrot") * (42 / 2))

        # input Image
        self.assertEqual(blisscribe.getWordWidth(Image.open(blisscribe.img_path + "Abraham.png")), 1236)


    def testGetWordImg(self):
        # default font size
        word_width = blisscribe.getWordWidth("parrot")
        img = Image.new('RGBA', (word_width, blisscribe.default_font_size * 5), (255, 255, 255, 255))
        sketch = ImageDraw.Draw(img)
        font = ImageFont.truetype(blisscribe.roman_font_path, blisscribe.default_font_size)
        sketch.text((0, blisscribe.default_font_size), "parrot", font=font, fill="black")
        self.assertEqual(blisscribe.getWordImg("parrot"), img)

        # custom font size
        word_width = blisscribe.getWordWidth("parrot", 42)
        img = Image.new('RGBA', (word_width, 42 * 5), (255, 255, 255, 255))
        sketch = ImageDraw.Draw(img)
        font = ImageFont.truetype(blisscribe.roman_font_path, 42)
        sketch.text((0, 42), "parrot", font=font, fill="black")
        self.assertEqual(blisscribe.getWordImg("parrot", 42), img)


    def testGetBlissImg(self):
        # default width/height
        img = Image.open(blisscribe.img_path + "accessibility.png")
        img.thumbnail((blisscribe.default_font_size * 10, blisscribe.default_font_size * 3))
        self.assertEqual(blisscribe.getBlissImg("accessibility"), img)

        # custom width/height
        img = Image.open(blisscribe.img_path + "accessibility.png")
        img.thumbnail((100, 30))
        self.assertEqual(blisscribe.getBlissImg("accessibility", 100, 30), img)


    def testTagsToDict(self):
        # all untranslatable words
        self.assertEqual(blisscribe.tagsToDict(["yolo", "meta", "postmodern"]), {})

        # singular nouns
        self.assertEqual(blisscribe.tagsToDict(["boar", "hill", "postmodern"]), {"boar": "NN", "hill": "NN"})

        # plural to singular noun
        self.assertEqual(blisscribe.tagsToDict(["boar", "hills", "postmodern"]), {"boar": "NN", "hill": "NN"})

        # adjective and verb
        self.assertEqual(blisscribe.tagsToDict(["hopeful", "go", "postmodern"]), {"hopeful": "JJ", "go": "VB"})


    def testSortFreqs(self):
        # EMPTY SET
        # empty string
        self.assertEqual(blisscribe.sortFreqs(""), [])
        # <=1 repetition per word
        self.assertEqual(blisscribe.sortFreqs("hello my wife"), [])
        # non-translatable repeated words
        self.assertEqual(blisscribe.sortFreqs("run run as fast as you can"), [])

        # 1 SET
        # set w/ 1 item
        self.assertEqual(blisscribe.sortFreqs("hello hello my wife"), [set(["hello"])])
        # set 2/ >1 items
        self.assertEqual(blisscribe.sortFreqs("dog dog catch bone bone"), [set(["dog", "bone"])])
        self.assertEqual(blisscribe.sortFreqs("you can run but you can not hide"), [set(["you", "can"])])
        self.assertEqual(blisscribe.sortFreqs("do you know the muffin man the muffin man the muffin man"), [set(["the", "muffin", "man"])])

        # >1 SETS
        self.assertEqual(blisscribe.sortFreqs("hello hello hello my my wife wife"), [set(["my", "wife"]), set(["hello"])])
        self.assertEqual(blisscribe.sortFreqs("do you know the muffin man the muffin man muffin man"), [set(["the"]), set(["muffin", "man"])])


    def testTranslate(self):
        # Alice in Wonderland
        self.assertEqual(type(blisscribe.translate(excerpts.alice_in_wonderland)), type(None))

        # Wizard of Oz
        self.assertEqual(type(blisscribe.translate(excerpts.wizard_of_oz)), type(None))
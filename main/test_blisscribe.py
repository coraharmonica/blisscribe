# -*- coding: utf-8 -*-
"""
TEST_BLISSCRIBE:

    Python testing suite for blisscribe.py.
    Tests methods in BlissTranslator class.
"""
import unittest
from PIL import Image, ImageDraw, ImageFont
import blisscribe
import excerpts


class TestBlisscribe(unittest.TestCase):
    """
    A class for testing methods from blisscribe.py's BlissTranslator class.
    """
    def testGetWordWidth(self):
        translator = blisscribe.BlissTranslator()
        # input str, default font size
        self.assertEqual(translator.getWordWidth("parrot"), len("parrot") * (translator.DEFAULT_FONT_SIZE / 2))
        # input str, custom font size
        self.assertEqual(translator.getWordWidth("parrot"), len("parrot") * (translator.font_size / 2))
        # input Image
        self.assertEqual(translator.getWordWidth(Image.open(translator.IMG_PATH + "Abraham.png")), 1236)

    def testMakeBlankImg(self):
        translator = blisscribe.BlissTranslator()
        # 1x1 blank image
        self.assertEqual(translator.makeBlankImg(1, 1), Image.new("RGBA", (1, 1), (255, 255, 255, 255)))
        # 10x20 blank image
        self.assertEqual(translator.makeBlankImg(10, 20), Image.new("RGBA", (10, 20), (255, 255, 255, 255)))

    def testGetWordImg(self):
        translator = blisscribe.BlissTranslator()
        # default font size
        word_width = translator.getWordWidth("parrot")
        img = Image.new('RGBA', (word_width, translator.DEFAULT_FONT_SIZE * 5), (255, 255, 255, 255))
        sketch = ImageDraw.Draw(img)
        font = ImageFont.truetype(translator.ROMAN_FONT, translator.DEFAULT_FONT_SIZE)
        sketch.text((0, translator.DEFAULT_FONT_SIZE), "parrot", font=font, fill="black")
        self.assertEqual(translator.getWordImg("parrot"), img)
        # custom font size
        word_width = translator.getWordWidth("parrot")
        img = Image.new('RGBA', (word_width, translator.font_size * 5), (255, 255, 255, 255))
        sketch = ImageDraw.Draw(img)
        font = ImageFont.truetype(translator.ROMAN_FONT, translator.font_size)
        sketch.text((0, translator.font_size), "parrot", font=font, fill="black")
        self.assertEqual(translator.getWordImg("parrot", translator.font_size), img)

    def testGetBlissImg(self):
        translator = blisscribe.BlissTranslator()
        # default width/height
        img = Image.open(translator.IMG_PATH + "accessibility.png")
        width, height = (translator.DEFAULT_FONT_SIZE * 10, translator.DEFAULT_FONT_SIZE * 3)
        img.thumbnail((width, height))
        self.assertEqual(translator.getBlissImg("accessibility", max_width=width, max_height=height), img)
        # custom width/height
        img = Image.open(translator.IMG_PATH + "accessibility.png")
        img.thumbnail((100, 30))
        self.assertEqual(translator.getBlissImg("accessibility", 100, 30), img)

    def testGetWordTag(self):
        # TODO: fix issues w/ comparative & superlative adjectives/adverbs (context?)
        translator = blisscribe.BlissTranslator()
        
        self.assertEqual(translator.getWordTag("and"), "CC")
        self.assertEqual(translator.getWordTag("cheese"), "NN")
        self.assertEqual(translator.getWordAndTag("happy"), "JJ")
        self.assertEqual(translator.getWordAndTag("quietly"), "RB")
        self.assertEqual(translator.getWordAndTag("run"), "VB")
        
        self.assertEqual(translator.getWordAndTag("and"), ("and", "CC"))
        self.assertEqual(translator.getWordAndTag("seven"), ("seven", "CD"))
        self.assertEqual(translator.getWordAndTag("42"), ("42", "CD"))
        self.assertEqual(translator.getWordAndTag("the"), ("the", "DT"))
        self.assertEqual(translator.getWordAndTag("that"), ("that", "IN"))
        self.assertEqual(translator.getWordAndTag("happy"), ("happy", "JJ"))
        #self.assertEqual(translator.getWordAndTag("greener"), ("greener", "JJR"))
        #self.assertEqual(translator.getWordAndTag("greenest"), ("greenest", "JJS"))
        self.assertEqual(translator.getWordAndTag("should"), ("should", "MD"))
        self.assertEqual(translator.getWordAndTag("cheese"), ("cheese", "NN"))
        self.assertEqual(translator.getWordAndTag("dog"), ("dog", "NN"))
        self.assertEqual(translator.getWordAndTag("dogs"), ("dogs", "NNS"))
        self.assertEqual(translator.getWordAndTag("Friday"), ("Friday", "NNP"))
        #self.assertEqual(translator.getWordAndTag("Mondays"), ("Mondays", "NNPS"))
        #self.assertEqual(translator.getWordAndTag("Jack's"), ("Jack's", "POS"))
        self.assertEqual(translator.getWordAndTag("she"), ("she", "PRP"))
        self.assertEqual(translator.getWordAndTag("her"), ("her", "PRP$"))
        self.assertEqual(translator.getWordAndTag("quietly"), ("quietly", "RB"))
        #self.assertEqual(translator.getWordAndTag("better"), ("better", "RBR"))
        #self.assertEqual(translator.getWordAndTag("best"), ("best", "RBS"))
        self.assertEqual(translator.getWordAndTag("to"), ("to", "TO"))
        self.assertEqual(translator.getWordAndTag("run"), ("run", "VB"))
        self.assertEqual(translator.getWordAndTag("walked"), ("walked", "VBD"))
        self.assertEqual(translator.getWordAndTag("lying"), ("lying", "VBG"))
        self.assertEqual(translator.getWordAndTag("lied"), ("lied", "VBN"))

    def testTranslate(self):
        translator = blisscribe.BlissTranslator()
        # PDF with name "Alice in Wonderland" should appear, output should be None
        self.assertEqual(type(translator.translate(excerpts.alice_in_wonderland)), type(None))

    def testGetLexeme(self):
        translator = blisscribe.BlissTranslator()
        self.assertEqual(translator.getLexeme("walked"), "walk")
        self.assertEqual(translator.getLexeme("puppies"), "puppy")
        self.assertEqual(translator.getLexeme("puppy"), "puppy")
        self.assertEqual(translator.getLexeme("hellokitty"), "hellokitty")


if __name__ == '__main__':
    unittest.main()
"""
BLISSCRIPT:

    Used for running Blisscribe from command line.
"""
from blisscribe import *


def basic_bliss_translator(language, text):
    bt = BlissTranslator(language)
    bt.translate(text, pos=PARTS_OF_SPEECH, fast=True, sub_all=True)


if __name__ == '__main__':
    language = input("What language is your translation in?\t")
    text = input("What would you like to translate?\t")
    basic_bliss_translator(language, text)
    print("You can find your translation under /out/translation.pdf.")

"""
BLISSCRIPT:

    Used for running Blisscribe from command line.
"""
from blisscribe import *


def basic_bliss_translator(language, text):
    bt = BlissTranslator(language)
    bt.set_translatables(all=True)
    bt.set_fast_translate(True)
    bt.set_sub_all(True)
    bt.translate(text)


if __name__ == '__main__':
    language = input("What language is your translation in?\t")
    text = input("What would you like to translate?\t")
    basic_bliss_translator(language, text)
    print("You can find your translation under /out/translation.pdf.")

# Notes
# -----
"""
DEMO:

    Used to demonstrate translation capabilities of
    blisscribe.py BlissTranslator.translate().
"""

import blisscribe
import excerpts


DefaultTranslator = blisscribe.BlissTranslator(font_path=blisscribe.BlissTranslator.ROMAN_FONT, language="French")
DefaultTranslator.setSubAll(True)
DefaultTranslator.chooseOtherPOS(True)
DefaultTranslator.setFastTranslate(True)
#DefaultTranslator.translate(excerpts.alice_in_wonderland, title="Alice in Wonderland")
#DefaultTranslator.translateFile("/sample texts/salinger-catcher_test.txt", title="Catcher in the Rye")
DefaultTranslator.translate(excerpts.maupassant, title="La parure")
#DefaultTranslator.setLanguage("Dutch")
#DefaultTranslator.translate(excerpts.bible_dutch, title="Het Boek")

#DefaultTranslator.translate(excerpts.hesse_siddhartha[:5000], title="Siddhartha")
#DefaultTranslator.translate(excerpts.DFW, title="Infinite Jest", page_nums=True)
#DefaultTranslator.translate(excerpts.kjv[:5000], title="The King James Bible")
#DefaultTranslator.translate(excerpts.leaves_of_grass, title="Leaves of Grass")

#HelveticaTranslator = BlissTranslator(BlissTranslator.HIP_FONT)
#HelveticaTranslator.setSubAll(True)
#HelveticaTranslator.chooseOtherPOS(True)
#HelveticaTranslator.setFastTranslate(True)
#HelveticaTranslator.translate(excerpts.alice_in_wonderland[:1000])
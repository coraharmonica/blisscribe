# Notes
# -----
"""
DEMO:

    Used to demonstrate translation capabilities of
    blisscribe_oop.py BlissTranslator.translate().

    Translates several pages of Alice in Wonderland
    by default.
"""
import blisscribe_oop
import excerpts

DefaultTranslator = blisscribe_oop.BlissTranslator(font_path=blisscribe_oop.BlissTranslator.SANS_FONT)
DefaultTranslator.setSubAll(True)
DefaultTranslator.chooseOtherPOS(True)
DefaultTranslator.setFastTranslate(True)
DefaultTranslator.translate(excerpts.alice_in_wonderland, title="Alice in Wonderland", page_nums=True)

#DefaultTranslator.translate(excerpts.DFW, title="Infinite Jest", page_nums=True)
#DefaultTranslator.translate(excerpts.kjv[:5000], title="The King James Bible")
#DefaultTranslator.translate(excerpts.leaves_of_grass, title="Leaves of Grass")

#HelveticaTranslator = BlissTranslator(BlissTranslator.HELVETICA_FONT)
#HelveticaTranslator.setSubAll(True)
#HelveticaTranslator.chooseOtherPOS(True)
#HelveticaTranslator.setFastTranslate(True)
#HelveticaTranslator.translate(excerpts.alice_in_wonderland[:1000])
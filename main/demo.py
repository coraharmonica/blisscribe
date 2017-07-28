# Notes
# -----
"""
DEMO:

    Used to demonstrate translation capabilities of
    blisscribe.py BlissTranslator.translate().
"""

import blisscribe
import excerpts


DefaultTranslator = blisscribe.BlissTranslator(font_path=blisscribe.BlissTranslator.SANS_FONT, language="English")
DefaultTranslator.setSubAll(True)
DefaultTranslator.chooseOtherPOS(True)
DefaultTranslator.setFastTranslate(True)
DefaultTranslator.translate(excerpts.alice_in_wonderland[:3000], title="Alice in Wonderland")
#DefaultTranslator.translate(excerpts.petit_prince, title="Le petit prince")
#DefaultTranslator.translate(excerpts.hitchhikers_guide[:1000], title="The Hitchhiker's Guide to the Galaxy")


#DefaultTranslator.translate(excerpts.alice_in_wonderland_polish, title="Alice in Wonderland")
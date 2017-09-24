# -*- coding: utf-8 -*-
"""
DEMO:

    Used to demonstrate translation capabilities of
    blisscribe.py BlissTranslator.translate().

    Uncomment the calls to BlissTranslator's translate()
    method below to translate Alice in Wonderland or
    Hitchhiker's Guide to the Galaxy to Blissymbols.

    A selection of sample texts from Project Gutenberg
    can be found in the excerpts module.  Additional
    texts are located as plaintext files in this
    directory under the sample texts folder.

    If the user wishes to supply their own texts, it is
    recommended to place them in this directory or in the
    sample texts folder, then call excerpts.parsePlaintext()
    on the filepath relative to the main folder.
"""
import blisscribe
import excerpts


#DefaultTranslator = blisscribe.BlissTranslator()  # defaults to English, Times New Roman, size 30
#DefaultTranslator.translate("hi", "ho")
#DefaultTranslator.translate(excerpts.alice_in_wonderland[:3000], title="Alice in Wonderland")
#DefaultTranslator.translate(excerpts.hitchhikers_guide[:1000], title="The Hitchhiker's Guide to the Galaxy")

'''
CustomTranslator = blisscribe.BlissTranslator(language="German", font_path=excerpts.BlissTranslator.SANS_FONT)
CustomTranslator.setSubAll(True)         # add Polish subtitles below all Blissymbols
CustomTranslator.chooseOtherPOS(True)    # translate all parts of speech possible to Blissymbols
CustomTranslator.setFastTranslate(True)  # translate Polish to Blissymbols immediately
CustomTranslator.translate("ich habe kein lust mehr, unser wir uns", title='title')
'''

# Polish translation
CustomTranslator = blisscribe.BlissTranslator(language="Polish", font_path=excerpts.BlissTranslator.SANS_FONT)
CustomTranslator.setSubAll(True)         # add Polish subtitles below all Blissymbols
CustomTranslator.chooseOtherPOS(True)    # translate all parts of speech possible to Blissymbols
CustomTranslator.setFastTranslate(True)  # translate Polish to Blissymbols immediately
CustomTranslator.translate(excerpts.alice_in_wonderland_polish[:200], title='Alicja w Krainie Czar\xc3\xb3w')

#blisscribe.BlissTranslator.LEX_PARSER.printDict(blisscribe.BlissTranslator.LEX_PARSER.getBlissEncodings("/resources/lexica/blissymbol encoding.txt"))
#CustomTranslator.translate('Ksi\xc4\x85\xc5\xbcka', title="Alice")
#translator = blisscribe.BlissTranslator()
#translator.writePdf(text="/u3200")

# French translation
#CustomTranslator.setLanguage(language="French")
#CustomTranslator.chooseOtherPOS(False)
#CustomTranslator.translate(excerpts.petit_prince, title="Le petit prince")


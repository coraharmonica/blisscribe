# -*- coding: utf-8 -*-
"""
DEMO:

    Used to demonstrate translation capabilities of
    blisscribe_py.py BlissTranslator.translate().

    Uncomment the calls to BlissTranslator's translate()
    method below to translate Alice in Wonderland or
    Hitchhiker's Guide to the Galaxy to Blissymbols.

    A selection of defn texts from Project Gutenberg
    can be found in the excerpts module.  Additional
    texts are located as plaintext files in this
    directory under the defn texts folder.

    If the user wishes to supply their own texts, it is
    recommended to place them in this directory or in the
    defn texts folder, then call excerpts.parsePlaintext()
    on the filepath relative to the main folder.
"""
import blisscribe
import excerpts

#bt = blisscribe.BlissTranslator()
#lp = blisscribe.LexiconParser(bt)
#multi_dict = lp.getMultilingualBlissDict()
#lp.writeBlissWordnet(lp.blissDictToWordnet(multi_dict))


DefaultTranslator = blisscribe.BlissTranslator()  # defaults to English, Times New Roman, size 30
DefaultTranslator.setSubAll(True)         # add Polish subtitles below all Blissymbols
DefaultTranslator.chooseOtherPOS(True)    # translate all parts of speech possible to Blissymbols
DefaultTranslator.setFastTranslate(True)  # translate Polish to Blissymbols immediately
DefaultTranslator.setTranslateAll(True)
#DefaultTranslator.translate(excerpts.kjv[:500], title="The Bible", title_page=False)
#DefaultTranslator.translate(excerpts.leaves_of_grass[:500], title="Leaves of Grass", title_page=False)
DefaultTranslator.translate(excerpts.hitchhikers_guide[:300], title="The Hitchhiker's Guide to the Galaxy")

'''
CustomTranslator = blisscribe_py.BlissTranslator(language="German", font_path=excerpts.BlissTranslator.SANS_FONT)
CustomTranslator.setSubAll(True)         # add Polish subtitles below all Blissymbols
CustomTranslator.chooseOtherPOS(True)    # translate all parts of speech possible to Blissymbols
CustomTranslator.setFastTranslate(True)  # translate Polish to Blissymbols immediately
CustomTranslator.translate("ich habe kein lust mehr, unser wir uns", title='title')
'''
'''
# Polish translation
CustomTranslator = blisscribe.BlissTranslator(language="Polish", font_path=excerpts.BlissTranslator.SANS_FONT)
CustomTranslator.setSubAll(True)         # add Polish subtitles below all Blissymbols
CustomTranslator.chooseOtherPOS(True)    # translate all parts of speech possible to Blissymbols
CustomTranslator.setFastTranslate(True)  # translate Polish to Blissymbols immediately
CustomTranslator.setTranslateAll(True)
CustomTranslator.translate(excerpts.alice_in_wonderland_polish[:500], title='Alicja w Krainie Czar\xc3\xb3w')

# French translation
CustomTranslator = blisscribe.BlissTranslator(language="French", font_path=blisscribe.BlissTranslator.SANS_FONT)
CustomTranslator.setSubAll(True)         # add Polish subtitles below all Blissymbols
CustomTranslator.chooseOtherPOS(True)    # translate all parts of speech possible to Blissymbols
CustomTranslator.setFastTranslate(True)  # translate Polish to Blissymbols immediately
CustomTranslator.setTranslateAll(True)
CustomTranslator.setSafeTranslate(False)
CustomTranslator.chooseOtherPOS(True)
CustomTranslator.translate(excerpts.petit_prince[100:200], title="Le petit prince")

CustomTranslator = blisscribe.BlissTranslator(language="English")
CustomTranslator.chooseOtherPOS(True)
CustomTranslator.setSubAll(True)
CustomTranslator.setFastTranslate(True)
CustomTranslator.setTranslateAll(True)
CustomTranslator.translate("soccer", title="Test", title_page=False)
'''
#CustomTranslator.translate("el partido de futbol es esta noche", title="My translation")
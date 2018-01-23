# -*- coding: utf-8 -*-
"""
DEMO:

    Used to demonstrate translation capabilities of
    blisscribe_py.py BlissTranslator.translate().

    Also used to test functions whose output is hard
    to test (e.g. translate() producing a PDF translation).

    Uncomment the calls to BlissTranslator's translate()
    method below to translate Alice in Wonderland or
    Hitchhiker's Guide to the Galaxy to Blissymbols.

    A selection of defn texts from Project Gutenberg
    can be found in the excerpts module.  Additional
    texts are located as plaintext files in this
    directory under the defn texts folder.

    If the user wishes to supply their own texts, it is
    recommended to place them in this directory or in the
    defn texts folder, then call excerpts.parse_plaintext()
    on the filepath relative to the main folder.
"""
from blisscribe import *
import blisslearn
import excerpts
from concept_analyzer import *
from bliss_images import *


bt = BlissTranslator()
bt.set_sub_all(True)
bt.set_fast_translate(True)
bt.set_translate_all(True)
bt.choose_other_pos(True)
bt.set_machine_translate(True)
bt.translate(excerpts.metamorphosis[:500], title="Metamorphosis")

'''
bt.translate(excerpts.hitchhikers_guide[:300], title="The Hitchhiker's Guide to the Galaxy")

#lp = bt.get_lex_parser()
#lexicon = lp.init_bliss_lexicon()

#for entry in lexicon:
#    print entry, lexicon[entry]


#indicators = beside(get_bliss_img("indicator_(action)"), get_bliss_img("indicator_(imperative_form)"))
#overlay(indicators, get_bliss_img("chive"))

#a = ConceptAnalyzer("English")
#a.draw_concept_cloud('any region in space outside the solar system', language="English", title='deep space')
#a.draw_concept_cloud('any of various burrowing animals of the family Leporidae having long ears and short tails; '
#                   'some domesticated and raised for pets or food', language="English", title='rabbit')
#draw_concept_cloud(excerpts.alice_in_wonderland_polish, language="Polish", title="Alicja w Krainie Czar\xc3\xb3w")

#a.translator.make_blissymbol("space,outer_space.png", "NN", "(outside + earth)", {"English": [u"space", u"outer space"]})
#a.translator.set_machine_translate(True)
#a.draw_word_concepts("love")

raw_input("???")

bt = BlissTranslator()
twp = bt.make_translation_word("Poseidon", "NN")
twj = bt.make_translation_word("Jupiter", "NN")
twn = bt.make_translation_word("Neptune", "NN")
tws = bt.make_translation_word("Saturn", "NN")

bl = blisslearn.BlissLearner(bt)
print twp.get_word()
print " ".join(bl.predict_word(twp, debug=False))
print
print twj.get_word()
print " ".join(bl.predict_word(twj, debug=False))
print
print twn.get_word()
print " ".join(bl.predict_word(twn, debug=False))
print
print tws.get_word()
print " ".join(bl.predict_word(tws, debug=False))
print
raw_input("???")

freqs = bt.analyze_concepts(excerpts.the_raven)
sorted_freqs = sorted(freqs, key=lambda k: freqs[k], reverse=True)

for sf in sorted_freqs:
    print " " * (50 - len(sf)), sf[:50].replace("_", " "), "\t", freqs[sf]


DefaultTranslator = BlissTranslator()  # defaults to English, Times New Roman, size 30
DefaultTranslator.set_sub_all(True)         # add Polish subtitles below all Blissymbols
DefaultTranslator.choose_other_pos(True)    # translate all parts of speech possible to Blissymbols
DefaultTranslator.set_fast_translate(True)  # translate Polish to Blissymbols immediately
DefaultTranslator.set_translate_all(True)
DefaultTranslator.set_machine_translate(True)
#DefaultTranslator.translate(excerpts.kjv[:500], title="The Bible", title_page=False)
#DefaultTranslator.translate(excerpts.leaves_of_grass[:500], title="Leaves of Grass", title_page=False)
DefaultTranslator.translate(excerpts.hitchhikers_guide[:300], title="The Hitchhiker's Guide to the Galaxy")


CustomTranslator = blisscribe.BlissTranslator(language="Polish", font_path=blisscribe.BlissTranslator.SANS_FONT)
CustomTranslator.set_sub_all(True)
CustomTranslator.set_fast_translate(True)
CustomTranslator.set_translate_all(True)
CustomTranslator.choose_other_pos(True)
CustomTranslator.set_safe_translate(False)
#CustomTranslator.lex_parser.write_bliss_wordnet(CustomTranslator.get_eng_bliss_dict())
#CustomTranslator.translate("Hi") #"Ich habe kein lust mehr, unser wir uns.")
CustomTranslator.translate(excerpts.alice_in_wonderland_polish[:1000])



# Polish translation
CustomTranslator = BlissTranslator(language="Polish", font_path=SANS_FONT)
CustomTranslator.set_sub_all(True)         # add Polish subtitles below all Blissymbols
CustomTranslator.choose_other_pos(True)    # translate all parts of speech possible to Blissymbols
CustomTranslator.set_fast_translate(True)  # translate Polish to Blissymbols immediately
CustomTranslator.set_translate_all(True)
CustomTranslator.set_machine_translate(True)
CustomTranslator.set_safe_translate(True)
#CustomTranslator.translate("Alicja", title='Alicja w Krainie Czar\xc3\xb3w')
CustomTranslator.translate(excerpts.alice_in_wonderland_polish[:100], title='Alicja w Krainie Czar\xc3\xb3w')



# French translation
CustomTranslator = blisscribe.BlissTranslator(language="French", font_path=blisscribe.BlissTranslator.SANS_FONT)
CustomTranslator.set_sub_all(True)         # add Polish subtitles below all Blissymbols
CustomTranslator.choose_other_pos(True)    # translate all parts of speech possible to Blissymbols
CustomTranslator.set_fast_translate(True)  # translate Polish to Blissymbols immediately
CustomTranslator.set_translate_all(True)
CustomTranslator.set_safe_translate(False)
CustomTranslator.translate(excerpts.petit_prince[100:200], title="Le petit prince")
CustomTranslator.translate("ballon")

CustomTranslator = blisscribe.BlissTranslator(language="English")
CustomTranslator.choose_other_pos(True)
CustomTranslator.set_sub_all(True)
CustomTranslator.set_fast_translate(True)
CustomTranslator.set_translate_all(True)
CustomTranslator.translate("soccer", title="Test", title_page=False)
'''
#CustomTranslator.translate("el partido de futbol es esta noche", title="My translation")
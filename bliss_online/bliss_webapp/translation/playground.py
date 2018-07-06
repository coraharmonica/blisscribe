# -*- coding: utf-8 -*-
"""
DEMO:

    Used to test functions whose output is hard
    to test (e.g. translate() producing a PDF translation).

    Not for GitHub.
"""
import excerpts
#from speechart.blisschart import BlissChart
from blisscribe import *


bt = BlissTranslator(language='Polish')
bt.set_sub_all(True)                # add subtitles below all Blissymbols
bt.set_fast_translate(True)         # translate words to Blissymbols immediately
bt.set_translatables(other=True)    # translate all parts of speech to Blissymbols
bt.set_translate_all(False)         # translate ALL words, taking user input if necessary
bt.set_machine_translate(False)     # enable machine learning translations for unknown words
bt.set_safe_translate(False)        # translate words with uncertain Blissymbols

# bt.translate(excerpts.alice_in_wonderland[:1000], title="Alice in Wonderland")
# bt.translate(excerpts.hitchhikers_guide[:500], title="The Hitchhiker's Guide to the Galaxy")
# bt.translate(excerpts.kjv[:500], title="The Bible")
# bt.translate(excerpts.leaves_of_grass[:500], title="Leaves of Grass", title_page=False)

# Polish
#bt.set_language("Polish")
bt.set_machine_translate(False)
bt.set_safe_translate(True)
bt.translate(excerpts.alice_in_wonderland_polish[:8000], title='Alicja w Krainie Czarów')
bt.init_lang_parser().refresh_data()


'''
bt = BlissTranslator(language="English")
bt.set_fast_translate(True)
bt.set_safe_translate(False)
bt.set_sub_all(True)

bt.set_translatables(nouns=True, verbs=False, adjs=False, other=False)
bt.save_images(bt.images_to_lines(bt.translate_to_images("The quick brown fox jumps over the lazy dog")))

bt.set_translatables(nouns=False, verbs=True, adjs=False, other=False)
bt.save_images(bt.images_to_lines(bt.translate_to_images("The quick brown fox jumps over the lazy dog")))

bt.set_translatables(nouns=False, verbs=False, adjs=True, other=False)
bt.save_images(bt.images_to_lines(bt.translate_to_images("The quick brown fox jumps over the lazy dog")))

bt.set_translatables(nouns=False, verbs=False, adjs=False, other=True)
bt.save_images(bt.images_to_lines(bt.translate_to_images("The quick brown fox jumps over the lazy dog")))


lp = LanguageParser("Polish")
print lp.find_stemwords(u"lepiej")
print lp.find_english_translations(u"lepiej")
lp.refresh_data()

bc = BlissChart("English")
bc.add_bliss_sentences(excerpts.alice_in_wonderland[:15000])
bc.chart("Blissymbols in Alice in Wonderland").save("out/alice_in_wonderland.png")
bc.refresh_data()

bc = BlissChart("Polish")
bc.add_bliss_sentences(excerpts.alice_in_wonderland_polish[:10000])
bc.chart(u"Blissymbols in Alicja w Kranie Czarów").save(u"out/alicja_w_kranie_czarów.png")
bc.refresh_data()

bt = BlissTranslator(language='English')
bt.set_fast_translate(True)
bt.set_sub_all(True)
bt.set_translate_all(True)
bt.set_safe_translate(False)
bt.set_translatables(other=True)    # translate all parts of speech to Blissymbols
bt.translate(excerpts.alice_in_wonderland[:1000], title='Alice in Wonderland')

bt.set_language("Polish")
#bt = BlissTranslator(language='Polish')
#bt.set_fast_translate(True)
#bt.set_sub_all(True)
#bt.set_translatables(other=True)    # translate all parts of speech to Blissymbols
bt.translate(excerpts.alice_in_wonderland_polish[:1000], title='Alicja w Krainie Czar\xc3\xb3w')

bt = BlissTranslator(language='English')
bt.set_sub_all(True)                # add subtitles below all Blissymbols
bt.set_fast_translate(True)         # translate words to Blissymbols immediately
bt.set_translatables(other=True)    # translate all parts of speech to Blissymbols
bt.set_translate_all(False)         # translate ALL words, taking user input if necessary
bt.set_machine_translate(False)     # enable machine learning translations for unknown words
bt.set_safe_translate(False)        # translate words with uncertain Blissymbols
#bt.translate(excerpts.hitchhikers_guide[:2000], title="Hitchhiker's Guide")
bt.translate(excerpts.alice_in_wonderland[:2000], title="Alice in Wonderland")
#bt.translate("daisy")
'''


# -*- coding: utf-8 -*-
"""
DEMO:

    Used to demo BlissTranslator.translate().

    Also used to test functions whose output is hard
    to test (e.g. translate() producing a PDF translation).

    Uncomment the calls to BlissTranslator's translate()
    method below to translate Alice in Wonderland,
    Hitchhiker's Guide to the Galaxy, and more to Blissymbols.

    A selection of texts from Project Gutenberg
    can be found in the excerpts module.  Additional
    texts are located as plaintext files in this
    directory under the "sample texts" folder.

    To use custom texts, place them in the sample texts folder,
    then call excerpts.parse_plaintext() on the filename.
"""
import bliss_online.bliss_webapp.translation.excerpts as excerpts
from bliss_online.bliss_webapp.translation.blisscribe import *


bt = BlissTranslator(language="English")

bt.translate(excerpts.alice_in_wonderland[:1000], title="Alice in Wonderland", pos=PARTS_OF_SPEECH)
# bt.translate(excerpts.hitchhikers_guide[:500], title="The Hitchhiker's Guide to the Galaxy")
# bt.translate(excerpts.kjv[:500], title="The Bible")
# bt.translate(excerpts.leaves_of_grass[:500], title="Leaves of Grass", title_page=False)


'''
# Polish
bt.set_language("Polish")
bt.translate(excerpts.alice_in_wonderland_polish[:500], title='Alicja w Krainie Czarów')

# French
bt.set_language("French")
bt.translate(excerpts.petit_prince[:500], title="Le petit prince")

# Spanish
bt.set_language("Spanish")
bt.translate("el partido de futbol es esta noche", title="My translation")
'''

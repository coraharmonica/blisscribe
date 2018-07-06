"""
NL_ANALOGUE:

    Used for creating nonstandard Blissymbols for
    representing natural language.
"""
import os
import images
import speechart.images as simages


NL_PATH = os.getcwd() + "/symbols/nl_analogues/indicators/"


def new_blissymbol(bliss_name, derivations):
    bliss_names = derivations
    bliss_images = [images.Image.open(NL_PATH + bn + ".png") for bn in bliss_names]
    bliss_img = simages.beside_all(bliss_images, align='bottom', space=5, trim_imgs=False)
    bliss_img.save(NL_PATH + bliss_name + ".png")
    bliss_img.show()
    return bliss_img


new_blissymbol("aspect/future_perfect", derivations=["tense/future", "aspect/perfect"])

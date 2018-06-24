'''

FONT_DICT = blisscribe_py.blisscribe.BlissTranslator.FONT_FAMS
FONT_FAMS = [(FONT_DICT[font], font) for font in FONT_DICT]

FONT_SIZES = [(str(n), str(n)) for n in range(15, 51)]

from blisscribe import BlissTranslator
#from translation.blisscribe import BlissTranslator

LANGS = [BlissTranslator.DEFAULT_LANG] #.SUPPORTED_LANGS
SUPPORTED_LANGS = [(lang, lang) for lang in LANGS]

try:
    from blisscribe import BlissTranslator
except ImportError:
    import sys, os
    print("CURRENT WORKING DIRECTORY:", os.getcwd())
    curr_path = os.path.dirname(__file__)
    print("CURRENT PATH:", curr_path)
    top_dir = curr_path.rsplit("/", maxsplit=2)[0]
    print("CURRENT TOP DIR:", top_dir)
    os.chdir(top_dir)
    print("CURRENT WORKING DIRECTORY:", os.getcwd())
    from translation import blisscribe

LANGS = [BlissTranslator.DEFAULT_LANG] #.SUPPORTED_LANGS
SUPPORTED_LANGS = [(lang, lang) for lang in LANGS]
'''

ROMAN_FONT = "/Library/Fonts/Times New Roman.ttf"
SANS_FONT = "/Library/Fonts/Arial.ttf"
HIP_FONT = "/Library/Fonts/Helvetica.dfont"
FONT_FAMS = [(ROMAN_FONT, "Times New Roman"),
             (SANS_FONT, "Arial"),
             (HIP_FONT, "Helvetica")]
FONT_SIZES = [(str(n), str(n)) for n in range(10, 31)]
LANGS = ["English", "Spanish", "German", "French", "Italian", "Dutch", "Polish"]
SUPPORTED_LANGS = [(lang, lang) for lang in LANGS]

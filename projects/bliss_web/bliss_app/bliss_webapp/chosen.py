ROMAN_FONT = "/Library/Fonts/Times New Roman.ttf"
SANS_FONT = "/Library/Fonts/Arial.ttf"
HIP_FONT = "/Library/Fonts/Helvetica.dfont"
FONT_FAMS = [(ROMAN_FONT, "Times New Roman"),
             (SANS_FONT, "Arial"),
             (HIP_FONT, "Helvetica")]
FONT_SIZES = [(str(n), str(n)) for n in range(10, 31)]
LANGS = ["English", "Spanish", "German", "French", "Italian", "Dutch", "Polish"]
SUPPORTED_LANGS = [(lang, lang) for lang in LANGS]
import ttf_parser
from blisscribe import blissFontPath

def loadBlissGlyphs():
    """
    :return: parsed dict of Blissymbols
    """
    blissParser = ttf_parser.TTFParser(blissFontPath)
    blissParser.debug_printIndex()
    glyf = blissParser.seek_table("glyf", +0x0000A124)
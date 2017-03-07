# NOTES
# =====
#
# Fetch Glyph Address(es)
# -----------------------
# Given the first and last glyph addresses in a font family,
# returns a list of all glyph addresses in the same font family.


# CONSTANTS
# =========

blissFontPath = "/Users/courtney/Library/Fonts/CcfSymbolFont-bliss-2012.ttf"
firstBlissChar = "\ue00a"
lastBlissChar = "\uf3c0"


# FUNCTIONS
# =========

# helpers
# -------

def getNextChar(char):
    """
    :param char: character in hexadecimal (i.e., abcdef0123456789)
    :return: next hexadecimal character
    """
    hex = "0123456789abcdef"
    idx = 0

    for elt in hex:
        idx += 1
        if elt == char:
            if elt == hex[-1]:
                return hex[0]
            else:
                return hex[idx]

    return ""


def reverse(string):
    """
    :param string: [str] any given string
    :return: [str] given string spelled backwards
    """
    new = ""

    for char in string:
        new = char + new

    return new


# main
# ----

def getNextGlyphAddress(prev):
    """
    :param prev: [str] preceding glyph address (in hex)
    :return: [str] next glyph address (in hex)
    """
    new = ""
    revPrev = reverse(prev) # reversed for ease of addition (+)
    idx = 0
    changeNext = False

    for char in revPrev:
        if idx == 0 or changeNext == True:
            new += getNextChar(char)
            if char == "f":
                changeNext = True
            else:
                changeNext = False
        else:
            new += char
        idx += 1

    return reverse(new)


def getNextGlyphAddresses(first, last):
    """
    :param first: [str] first glyph address in a given font set
    :param last: [str] last glyph address in (same) font set
    :return: [list] all glyph addresses in a font set
    """
    addresses = [first]
    current = first
    goal = last

    while current != goal:
        current = getNextGlyphAddress(current)
        addresses.append(current)

    return addresses


#getNextGlyphAddresses(firstBlissChar, lastBlissChar)
blissFontPath = "/Users/courtney/Library/Fonts/CcfSymbolFont-bliss-2012.ttf"
firstBlissChar = "\ue00a"
lastBlissChar = "\ue00f" #f3c0

# TODO: create list of all glyph addresses based on first and last glyph addresses (in hexadecimal)

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
            return hex[idx]


def reverse(string):
    """
    :param string: [str] any given string
    :return: [str] given string spelled backwards
    """
    new = ""

    for char in string:
        new = string + new

    return new


def getNextGlyphAddress(prev):
    """
    :param prev: [str] preceding glyph address (in hex)
    :return: [str] next glyph address (in hex)
    """
    new = "\u"
    abcs = "abcdef"
    nums = "0123456789"

    revPrev = reverse(prev)
    idx = 0

    for char in revPrev:
        if idx == 0:
            new += getNextChar(prev[-1])
            if char == "f":
                new += getNextChar(prev[-2])
        else:
            new += char

    return new


def getGlyphAddresses(first, last):
    """
    :param first: [str] first glyph address in a given font set
    :param last: [str] last glyph address in (same) font set
    :return: [list] all glyph addresses in a font set
    """
    addresses = [first]
    rsf = []

    current = first
    goal = last

    while current != goal:
        getNextGlyphAddress(current)

    for address in rsf:
        addresses.append("\u" + address)

    return addresses


getGlyphAddresses(firstBlissChar, lastBlissChar)
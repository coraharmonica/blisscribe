from PIL import Image, ImageDraw, ImageFont
from blisscribe import getWordWidth
from translation_dictionary import blissDict
from blisscribe import romanFont

# most basic symbols in Blissymbols
blocks = {}

def render_symbol(name, size):
    """
    :param name: name of symbol to render
    :param size: height of rendered image
    :return: named symbol rendered at given size
    """
    base = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    over = Image.new("RGBA", (size, size), (255, 255, 255, 255))

    # LEGEND
    # ======
    # x-coord:
    #   x=0   -> left
    #   x=max -> right
    #
    # y-coord:
    #   y=0   -> top
    #   y=max -> bottom

    start = size / 10
    end = size - start

    drawing = ImageDraw.Draw(over)

    # drawings for...
    # "earth"
    #drawing.line([(start, end), (end, end)], fill=(0,0,0,255), width=3)
    # "sky"
    #drawing.line([(start, start), (end, start)], fill=(0,0,0,255), width=3)
    # "eye"
    drawing.ellipse((start,end,start,end), fill=(0,0,0,255), outline=5)
    over.paste(blissDict[0])

    out = Image.alpha_composite(base, over)

    out.show()

    #for block in blissDict[name]:
    #    bg.paste(block.img, block.loc, block.img)

class block:
    def __init__(self, img, loc):
        block.img = img
        block.loc = loc  # tuple of starting x and y coordinates

render_symbol("len", 100)
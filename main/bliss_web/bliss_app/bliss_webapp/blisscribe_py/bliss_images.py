# coding: utf-8
"""
BLISS_IMAGES:

    A module for modifying images for Blisscribe.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageChops

PATH = os.path.dirname(os.path.realpath(__file__))
IMG_PATH = PATH + "/symbols/png/full/"


def equate_images(img1, img2):
    """
    Returns a 2-tuple of the given images but
    set to the same size as each other.

    :param img1: Image, first image to set equal in size
    :param img2: Image, second image to set equal in size
    :return: 2-tuple(Image, Image), images set to equal sizes
    """
    img1 = img1.convert('RGBA')
    img2 = img2.convert('RGBA')
    w1, h1 = img1.size
    w2, h2 = img2.size

    if w1 != w2 or h1 != h2:
        bg_size = max(w1, w2), max(h1, h2)
        bg = Image.new(mode='RGBA', size=bg_size, color=(255, 255, 255, 0))

        if img1.size == bg_size:
            x = w1/2 - w2/2
            y = h1/2 - h2/2
            bg.paste(img2, (x, y))
            img2 = bg
        elif img2.size == bg_size:
            x = w2/2 - w1/2
            y = h2/2 - h1/2
            bg.paste(img1, (x, y))
            img1 = bg
        else:
            bg_img1 = bg
            bg_img2 = bg_img1.copy()
            x_mid = bg_size[0]/2
            y_mid = bg_size[1]/2
            x1 = x_mid - img1.size[0]/2
            y1 = y_mid - img1.size[1]/2
            x2 = x_mid - img2.size[0]/2
            y2 = y_mid - img2.size[1]/2
            bg_img1.paste(img1, (x1, y1))
            bg_img2.paste(img2, (x2, y2))
            img1 = bg_img1
            img2 = bg_img2

    return img1, img2


def overlay(front, back):
    """
    Overlays front image on top of back image.
    ~
    Preserves alpha values of both images.

    :param front: Image, image to place in front
    :param back: Image, image to place in back
    :return: Image, foreground overlaid on background
    """
    front, back = equate_images(front, back)
    img = Image.alpha_composite(back, front)
    return img


def beside(left, right):
    """
    Places left image beside right image.
    ~
    Preserves alpha values of both images.

    :param left: Image, image to place to left
    :param right: Image, image to place to right
    :return: Image, foreground overlaid on background
    """
    w, h = left.size[0] + right.size[0], max(left.size[1], right.size[1])
    img = Image.new(mode="RGBA", size=(w, h))
    img.paste(left, (0, 0))
    img.paste(right, (left.size[0], 0))
    return img


def above(top, bottom):
    """
    Places top image above bottom image.
    ~
    Preserves alpha values of both images.

    :param top: Image, image to place on top
    :param bottom: Image, image to place on bottom
    :return: Image, foreground overlaid on background
    """
    top_w, top_h = top.size
    bottom_w, bottom_h = bottom.size
    w, h = max(top_w, bottom_w), top_h + bottom_h
    img = Image.new(mode="RGBA", size=(w, h))
    img.paste(top, (w/2 - top_w/2, 0))
    img.paste(bottom, (w/2 - bottom_w/2, top.size[1]))
    return img


def make_blank_img(x, y):
    """
    Returns a blank (white) image of dimensions x and y.

    :param x: int, x-dimension of image
    :param y: int, y-dimension of image
    :return: Image, blank image
    """
    return Image.new("RGBA", (x, y), (255, 255, 255, 255))


def get_word_img(word, font_path, font_size, img_h):
    """
    Draws and returns an Image of given word in given font_size.
    ~
    If font_size is left as None, uses this BlissTranslator's
    font size.

    :param word: str, word to render to Image
    :param font_size: int, desired font size for string
    :param img_h: int, desired height for output image
    :return: Image, image of input str
    """
    if word == "\n":
        return make_blank_img(1, img_h)
    else:
        font = ImageFont.truetype(font=font_path, size=font_size)
        img = make_blank_img(font.getsize(word)[0], img_h)
        sketch = ImageDraw.Draw(img)
        sketch.text((0, int(font_size*0.75)),
                    word,
                    fill="black",
                    font=font)
        return trim_horizontal(img)


def get_bliss_img(bliss_name, max_width=None, max_height=None):
    """
    Draws and returns a thumbnail Image of the given word's
    Blissymbol, with width not exceeding max_width.
    ~
    If a word has multiple meanings, then return the Blissymbol
    corresponding to the best meaning in bliss_dict.

    :param bliss_name: str, Blissymbol image filename
    :param max_width: int, maximum width of Image (in pixels)
    :param max_height: int, maximum height of Image (in pixels)
    :return: Image, image of input str's Blissymbol
    """
    img = Image.open(IMG_PATH + bliss_name + ".png")
    if max_width is None:
        max_width = img.size[0]
    if max_height is None:
        max_height = img.size[1]
    img.thumbnail((max_width, max_height))
    return img


def get_trans_bliss_img(trans_word, max_width=None, max_height=None):
    """
    Draws and returns a thumbnail Image of the given trans_word's
    Blissymbol, with width/height not exceeding max_width/max_height.
    ~
    If trans_word has no Blissymbol, this method returns an Image
    with trans_word's word as text instead.

    :param trans_word: TranslationWord, word to render to Image
    :param max_width: int, maximum width of Image (in pixels)
    :param max_height: int, maximum height of Image (in pixels)
    :return: Image, image of input str's Blissymbol
    """
    img_filename = trans_word.get_bliss_name()
    font_path = trans_word.translator.font_path
    font_size = trans_word.translator.font_size

    if not trans_word.has_blissymbol():
        return get_word_img(trans_word.word, font_path, font_size, max_height)
    else:
        img = get_bliss_img(img_filename, max_width, max_height)
        if trans_word.is_plural_noun():
            img = get_plural_img(img)
        return img


def get_subbed_bliss_img(trans_word, max_width=None, max_height=None, subs=True):
    """
    Returns the given word as a Blissymbol with subtitles
    in this BlissTranslator's chosen language.
    ~
    If subs is set to False, output Image has no subtitles, but
    still offsets as if there were.

    :param trans_word: TranslationWord, word to translate & subtitle
    :param max_width: int, max width of output image (in pixels)
    :param max_height: int, max height of output image (in pixels)
    :param subs: bool, whether to subtitle output image
    :return: Image, subtitled Blissymbol image
    """
    word = trans_word.word
    word = trans_word.translator.unicodize(word)
    bliss_img = get_trans_bliss_img(trans_word, max_width, max_height)
    font_path = trans_word.translator.font_path
    sub_size = trans_word.translator.subtitle_size()
    img_h = trans_word.translator.image_heights()
    text = get_word_img(word.upper(), font_path, sub_size, img_h)
    text = trim(text)

    if not trans_word.has_blissymbol() or not subs:
        blank = make_blank_img(1, text.size[1])
        img = above(bliss_img, blank)
    else:
        img = above(bliss_img, text)

    return img


def get_indicator_bliss_img(indicator, max_width=None, max_height=None):
    """
    Returns the Blissymbol image corresponding to the
    given Blissymbol indicator string.

    :param indicator: str, Blissymbol indicator to get image of
    :param max_width: int, maximum width of Image (in pixels)
    :param max_height: int, maximum height of Image (in pixels)
    :return: Image, input indicator Blissymbol image
    """
    indicator = indicator.replace(" ", "_(")
    indicator += ")"
    return get_bliss_img(indicator, max_width, max_height)


def get_plural_img(img):
    """
    Returns the given Blissymbol image with the plural
    Blissymbol at the end.

    :param img: Image, Blissymbol image to pluralize
    :return: Image, input image pluralized
    """
    plural = get_indicator_bliss_img("indicator plural", img.size[0], img.size[1])
    return overlay(img, plural)


def trim(img, bbox=None):
    """
    Trims the input image's whitespace.
    ~
    For a custom crop specify the x1, y1,
    x2, and y2 coordinates in a 4-tuple.
    ~
    Taken from http://stackoverflow.com/questions/10615901/trim-whitespace-using-pil/29192070.

    :param img: Image, image to be trimmed
    :param bbox: tuple(int,int,int,int), dimensions to trim
    :return: Image, trimmed image
    """
    if bbox is None:
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
        diff = ImageChops.difference(img, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()

    if bbox:
        return img.crop(bbox)
    else:
        return img


def trim_horizontal(img):
    """
    Trims the input image's whitespace only
    in the x-dimension.

    :param img: Image, image to be trimmed
    :return: Image, trimmed image

    Adapted from http://stackoverflow.com/questions/10615901/trim-whitespace-using-pil/29192070.
    """
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()

    if bbox:
        bbox = (bbox[0], 0, bbox[2], img.height)
        return img.crop(bbox)
    else:
        return img


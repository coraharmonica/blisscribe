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
            x = w1//2 - w2//2
            y = h1//2 - h2//2
            bg.paste(img2, (x, y))
            img2 = bg
        elif img2.size == bg_size:
            x = w2//2 - w1//2
            y = h2//2 - h1//2
            bg.paste(img1, (x, y))
            img1 = bg
        else:
            bg_img1 = bg
            bg_img2 = bg_img1.copy()
            x_mid = bg_size[0]//2
            y_mid = bg_size[1]//2
            x1 = x_mid - img1.size[0]//2
            y1 = y_mid - img1.size[1]//2
            x2 = x_mid - img2.size[0]//2
            y2 = y_mid - img2.size[1]//2
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
    img.paste(top, (w//2 - top_w//2, 0))
    img.paste(bottom, (w//2 - bottom_w//2, top.size[1]))
    return img


def blank_image(x, y, opacity=0):
    """
    Returns a blank (white) image of dimensions x and y.

    :param x: int, x-dimension of image
    :param y: int, y-dimension of image
    :return: Image, blank image
    """
    return Image.new("RGBA", (x, y), (255, 255, 255, opacity))


def word_image(word, img_h, **kwargs):
    """
    Draws and returns an Image of given word in given font,
    or the font specified by font_path and font_size.
    ~
    If font_size is left as None, uses this BlissTranslator's
    font size.

    :param word: str, word to render to Image
    :param img_h: int, height of output image

    kwargs:
    :param font_path: str, font's directory path
    :param font_size: int, word's font size

    :return: Image, image of str
    """
    if word == "\n":
        return blank_image(1, img_h)
    else:
        font = kwargs.get('font', None)
        if font is None:
            font_path = kwargs.get('font_path', None)
            font_size = kwargs.get('font_size', 12)
            font = make_font(font_path, font_size)
        img = blank_image(font.getsize(word)[0], img_h)
        sketch = ImageDraw.Draw(img)
        sketch.text((0, int(font.size*0.75)),
                    word,
                    fill="black",
                    font=font)
        return trim_horizontal(img)


def make_font(font_path, font_size):
    """
    Returns an ImageFont with given font_path and font_size.
    ~
    If font_path is invalid, returns an ImageFont using this
    BlissTranslator's Arial font and font_size.

    :param font_path: str, path to font file
    :param font_size: int, desired font size
    :return: ImageFont, font with given path and font size
    """
    try:
        return ImageFont.truetype(font_path, font_size)
    except OSError:
        try:
            font_path = font_path.replace("/Library", "Windows")
            return ImageFont.truetype(font_path, font_size)
        except OSError:
            try:
                font = font_path.split("/")[-1].lower()
                return ImageFont.truetype(font=font, size=font_size)
            except OSError:
                try:
                    return ImageFont.truetype(font="arial.ttf", size=font_size)
                except OSError:
                    return ImageFont.load_default()


def trim(image, bbox=None):
    """
    Trims this Image's whitespace.
    ~
    For a custom crop specify the x1, y1,
    x2, and y2 coordinates in a 4-tuple.

    :param image: Image, image to be trimmed
    :param bbox: tuple(int,int,int,int), dimensions to trim
    :return: Image, trimmed image
    """
    if bbox is None:
        bg = Image.new(image.mode, image.size, image.getpixel((0, 0)))
        diff = ImageChops.difference(image, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()

    if bbox:
        return image.crop(bbox)
    else:
        return image


def trim_horizontal(image):
    """
    Trims the input image's whitespace only
    in the x-dimension.

    :param image: Image, image to be trimmed
    :return: Image, trimmed image
    """
    bg = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()

    if bbox:
        bbox = (bbox[0], 0, bbox[2], image.height)
        return image.crop(bbox)
    else:
        return image


# coding: utf-8
"""
IMAGES:

    A module for modifying images.
"""
from PIL import Image, ImageDraw, ImageFont, ImageChops


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


def overlay(front, back, equate=True):
    """
    Overlays front image on top of back image.
    ~
    Preserves opacity values of both images.
    ~
    If equate is set to True, equates both images in
    size before overlaying.  Otherwise, overlays
    front image on top of back image.

    :param front: Image, image to place in front
    :param back: Image, image to place in back
    :param equate: bool, whether to equate images before overlaying
    :return: Image, foreground overlaid on background
    """
    if equate:
        front, back = equate_images(front, back)
        img = Image.alpha_composite(back, front)
    else:
        w, h = max(front.size[0], back.size[0]), max(front.size[1], back.size[1])
        img = make_blank_img(w, h, opacity=0)
        front_x = w/2 - front.size[0]/2
        front_y = h/2 - front.size[1]/2
        back_x = w/2 - back.size[0]/2
        back_y = h/2 - back.size[1]/2
        img.paste(back, (back_x, back_y))
        img.paste(front, (front_x, front_y))
    return img


def beside(left, right, align='bottom'):
    """
    Places left image beside right image.
    ~
    Preserves opacity values of both images.
    ~
    Align can be set to 'center', 'top', or 'bottom'.

    :param left: Image, image to place to left
    :param right: Image, image to place to right
    :param align: str, alignment of right image relative to left
    :return: Image, left image beside right image
    """
    left, right = trim(left), trim(right)
    w, h = left.size[0] + right.size[0], max(left.size[1], right.size[1])
    img = Image.new(mode="RGBA", size=(w, h))

    if align == 'top':
        ly, ry = 0, 0
    elif align == 'bottom':
        ly = h - left.size[1]
        ry = h - right.size[1]
    else:  # center or otherwise
        ly = (h/2 - left.size[1]/2)
        ry = (h/2 - right.size[1]/2)

    img.paste(left, (0, ly))
    img.paste(right, (left.size[0], ry))
    return img


def beside_all(imgs, align='bottom', space=0):
    """
    Places each image in imgs beside each other.
    ~
    Preserves opacity values of all images.
    ~
    Align can be set to 'center', 'top', or 'bottom'.

    :param imgs: List[Image], images to place beside each other
    :param align: str, alignment of images relative to each other
    :param space: int, space between each image
    :return: Image, imgs beside one another
    """
    final_img = make_blank_img(0, 0, opacity=0)
    space_img = make_blank_img(space, space, opacity=0)
    for img in imgs:
        if space > 0:
            final_img = beside(final_img, space_img, align=align)
        final_img = beside(final_img, img, align=align)
    return final_img


def above(top, bottom, align='center'):
    """
    Places top image above bottom image.
    ~
    Preserves opacity values of both images.

    :param top: Image, image to place on top
    :param bottom: Image, image to place on bottom
    :param align: str, alignment of top image relative to bottom
    :return: Image, top image overlaid on bottom image
    """
    top, bottom = trim(top), trim(bottom)
    top_w, top_h = top.size
    bottom_w, bottom_h = bottom.size
    w, h = max(top_w, bottom_w), top_h + bottom_h
    img = Image.new(mode="RGBA", size=(w, h))

    if align == 'left':
        x1, x2 = 0, 0
    elif align == 'right':
        x1 = w - top_w
        x2 = w - bottom_w
    else:
        x1 = w/2 - top_w/2
        x2 = w/2 - bottom_w/2

    img.paste(top, (x1, 0))
    img.paste(bottom, (x2, top.size[1]))
    return img


def above_all(imgs, align='center'):
    """
    Places top image above bottom image.
    ~
    Preserves opacity values of both images.

    :param imgs: List[Image], images to place on top of one another
    :param align: str, alignment of images relative to each other
    :return: Image, top image overlaid on bottom image
    """
    final_img = make_blank_img(0, 0)
    for img in imgs:
        final_img = above(final_img, img, align=align)
    return final_img


def make_blank_img(x, y, colour=(255, 255, 255), opacity=255):
    """
    Returns a blank image of dimensions x and y with optional
    background colour and opacity values.

    :param x: int, x-dimension of image
    :param y: int, y-dimension of image
    :param colour: tuple(int,int,int), RBG value for background colour
    :param opacity: int[0,255], opacity value
    :return: Image, blank image
    """
    return Image.new("RGBA", (x, y), colour + (opacity,))


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
    if 0 in img.size:
        return img

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


def circle(width, height=None, fill='white', outline=None, opacity=0):
    height = width if height is None else height
    img = make_blank_img(width, height, opacity=opacity)
    draw = ImageDraw.Draw(img)
    outline = fill if outline is None else outline
    draw.ellipse((0, 0, width-1, height-1), fill, outline)
    return img


def rectangle(width, height, fill='white', outline=None, opacity=0):
    img = make_blank_img(width, height, opacity=opacity)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, width-1, height-1), fill, outline)
    return img


def triangle(width, height, fill='white', vertical=True, outline=None, opacity=0):
    img = make_blank_img(width, height, opacity=opacity)
    draw = ImageDraw.Draw(img)
    outline = fill if outline is None else outline
    width, height = width-1, height-1
    min_w, max_w = sorted([0, width])
    min_h, max_h = sorted([0, height])
    if vertical:
        dims = [(0, min_h), (width/2, max_h), (width, min_h)]
    else:
        dims = [(min_w, 0), (min_w, height), (max_w, height/2)]
    draw.polygon(dims, fill, outline)
    return img

def polygon(width, height, num_sides, fill='white', vertical=True, outline=None, opacity=0):
    if num_sides > 2:
        img = make_blank_img(width, height, opacity=opacity)
        draw = ImageDraw.Draw(img)
        outline = fill if outline is None else outline
        width, height = width-1, height-1
        min_w, max_w = sorted([0, width])
        min_h, max_h = sorted([0, height])
        mid_x = max_w/2
        mid_y = max_h/2
        if vertical:
            num_mids = num_sides - 2 #max(0, (num_sides % 2) - 2)
            # min_w, min_h
            # max_w/(num_sides-1), max_h/(num_sides-1)
            # max_w/(num_sides-1) * 2, max_h/(num_sides-1) * 2...
            # max_w/(num_sides-1) * num_sides-1, max_h/(num_sides-1) * num_sides-1
            # max_w/(num_sides-1) * 2, max_h/(num_sides-1)...
            # max_w/(num_sides-1), max_h/(num_sides-1)
            # max_w, max_h

            # triangle: (0, 0), (width/2, height), (width, 0)
            # square: (0,0), (0, width), (0, height), (width, height)
            # pentagon:


            dims = [(0, min_h), (width, min_h)]
            if num_mids != 0:
                # width, min_h
                mid_tups = [(mid_x - max_w/(num_sides-i), mid_y - max_h/(num_sides-i)) if i < num_mids
                            else (mid_x + max_w/(num_sides-num_mids-i), mid_y + max_h/(num_sides-num_mids-i))
                            for i in range(1, num_mids)]
                dims = dims[:1] + mid_tups + dims[-1:]
                print dims
        else:
            dims = [(min_w, 0), (min_w, height), (max_w, height/(num_sides-1))]
        draw.polygon(dims, fill, outline)
        img.show()
        return img

def load_default_font(font_name="Arial Bold.ttf", size=12):
    font = "/Library/Fonts/%s" % font_name
    return ImageFont.truetype(font=font, size=size)


def lang_font(lang):
    if lang == "Chinese":
        return "NotoSansCJKtc-Bold.otf"
    elif lang == "Japanese":
        return "NotoSansCJKjp-Bold.otf"
    elif lang == "Korean":
        return "NotoSansCJKkr-Bold.otf"
    else:
        return "Arial Bold.ttf"


def text_size(text, lang="English", size=12, font=None):
    if font is None:
        font = load_default_font(lang_font(lang), size=size)
    return font.getsize(text)


def text_image(message, lang="English", size=12, colour="black", bg_fill=(255, 255, 255),
               opacity=255, bg_opacity=0, font=None):
    if font is None:
        font = load_default_font(lang_font(lang), size=size)
    w, h = font.getsize(message)
    img = make_blank_img(w, h, bg_fill, opacity=bg_opacity)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), message, fill=colour, font=font, alpha=opacity)
    return img


def arrow(width, height, fill='black', angle=0, label=None, align_label=False,
          opacity=0, lang="English", font=None, font_size=0):
    vertical = width < height
    arrow_w, arrow_h = (3 * (width if vertical else height),) * 2  # width & height of arrowhead are 3 * stem width
    arrowhead = triangle(arrow_w, arrow_h, fill, vertical, opacity=opacity)
    rect_w = abs(width - (arrow_w if not vertical else 0))
    rect_h = abs(height - (arrow_h if vertical else 0))
    stem = rectangle(rect_w, rect_h, fill)

    if vertical:
        # if height >= 0, arrow points up; otherwise, points down
        top, bottom = (arrowhead, stem) if height >= 0 else (stem, arrowhead)
        img = above(top, bottom)
    else:
        # if width >= 0, arrow points right; otherwise, points left
        left, right = (stem, arrowhead) if width >= 0 else (arrowhead, stem)
        img = beside(left, right, align='center')

    if label is not None:
        txt = text_image(label, lang, opacity=0, size=font_size, font=font)
        if not align_label:
            img = trim(rotate(img, angle))
        img = overlay(txt, img)

    if align_label or label is None:
        img = trim(rotate(img, angle))

    return img


def rotate(img, angle):
    """
    Rotates img by the given angle and
    returns the result.

    :param img: Image, image to rotate
    :param angle: int, angle to rotate img
    :return: Image, image rotated by angle
    """
    if angle != 0:
        max_dim = max(img.size)
        img = overlay(img,
                      make_blank_img(max_dim * 2, max_dim * 2, opacity=0)).rotate(angle)
    return img


def venn_diagram(colours, diameter=100):
    """
    Returns a Venn diagram of the given colours as circles of
    the given diameter overlapping each other.
    ~
    Used to show colour combinations.

    :param colours: List[tuple], list of RGB values to display
    :return: Image, input colours in overlapping diagram
    """
    circles = []
    opacity = int(255.0 / len(colours))

    for rgb in colours:
        colour = rgb[:3] + (opacity,)
        circ = circle(diameter, height=diameter*2, fill=colour, opacity=0)
        circles.append(circ)

    fill = (255, 255, 255, 0)
    diagram = rectangle(1, 1, fill=fill, opacity=255)
    bg = rectangle(diameter / 2, diameter / 2, fill=fill, opacity=255)
    offset = int(360.0 / len(circles))
    angle = 0

    for i in range(len(circles)):
        circ = circles[i]
        circ = beside(circ, bg)
        circ = rotate(circ, angle)
        diagram = overlay(circ, diagram)
        angle += offset

    return trim(diagram)


def flower_diagram(colours, diameter=100):
    """
    Returns a flower diagram of the given colours overlapping each other.
    ~
    Used to show colour combinations.

    :param circles: List[Image], images to turn into Venn diagram
    :return: Image, input images as Venn diagram
    """
    circles = []
    opacity = int(255.0 / len(colours))

    for rgb in colours:
        colour = rgb[:3] + (opacity,)
        circ = circle(diameter, fill=colour, opacity=0)
        circles.append(circ)

    centre = circles[0]
    circles = circles[1:]
    fill = (255, 255, 255, 0)
    diagram = centre
    bg = rectangle(int(diameter*1.1), int(diameter*1.1), fill=fill, opacity=255)
    offset = int(360.0 / len(circles))
    angle = 0

    for i in range(len(circles)):
        circ = circles[i]
        circ = beside(circ, bg)
        circ = rotate(circ, angle)
        diagram = overlay(circ, diagram)
        angle += offset

    return diagram


"""
BLISS_DRAWER:

    Parses blissymbols-gh-pages data.
    An adaptation of the BlissViewer class in JavaScript for Python.
"""
import os
from speechart.images import *
from translation.resources.data.blissymbols_gh_pages.blissdata_words import BLISS_WORD_DATA
from translation.resources.data.blissymbols_gh_pages.blissdata_chars import BLISS_CHAR_DATA

PATH = os.path.dirname(os.path.realpath(__file__))


class BlissDrawer:
    """
    A class for drawing Blissymbols (in SVG?) from raw data.
    """
    BLISS_WORDS = BLISS_WORD_DATA["words"]
    BLISS_CHARS = BLISS_CHAR_DATA["chars"]

    BLISS_SHAPES = BLISS_CHAR_DATA["shapes"]
    BLISS_PATHS = BLISS_CHAR_DATA["paths"]

    BLISS_CENTER = BLISS_CHAR_DATA["center"]  # center of Bliss-chars relative to image's absolute center
    BLISS_KERNING_LEFT = BLISS_CHAR_DATA["kerning_left"]  # distance of Bliss-char relative to chars on its left
    BLISS_KERNING_RIGHT = BLISS_CHAR_DATA["kerning_right"]  # distance of Bliss-char relative to chars on its right

    IMAGE_HEIGHT = 1000
    PATH_FORMS = ["arc", "bigarc", "circle", "line", "dot", "disc", "text"]
    MODIFIERS = {
        'a,an,any': True,
        'ago,then_(past)': True,
        'belongs_to,of_(possessive)': True,
        'bliss-name': True,
        'comparative_more': True,
        'dot': True,
        'generalization': True,
        'group_of,much_of,many_of,quantity_of': True,
        'indicator_(combine)': True,
        'intensity': True,
        'line,stripe': True,
        'metaphor': True,
        'minus,no,without': True,
        'more': True,
        'most,maximum': True,
        'now': True,
        'opposite_meaning,opposite_of,opposite': True,
        'part,bit,piece,portion,part_of': True,
        'superlative_most': True,
        'then,so,later': True
    }
    PUNCTUATIONS = {
        'comma': True,
        'period,point,full_stop,decimal_point': True,
        'question_mark': True,
        'exclamation_mark': True
    }

    BLISSQUARE = 128
    BLISSHEIGHT = BLISSQUARE * 5 / 2
    BLISSQUARE_SPACE = BLISSQUARE / 4
    GRIDSIZE = BLISSQUARE / 2

    # SVG information
    SVG_START = ('<svg xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="true" ' + 'class="bliss-svg" viewBox="{x} {y} {w} {h}"><g>');
    SVG_END = '</g></svg>'
    SVG_ELEMS = {
        'dot': '<circle class="bliss-dot" cx="{x}" cy="{y}" r="{r}"/>',
        'disc': '<circle class="bliss-disc" cx="{x}" cy="{y}" r="{r}"/>',
        'circle': '<circle class="bliss-line" cx="{x}" cy="{y}" r="{r}"/>',
        'text': '<text class="bliss-text" text-anchor="middle" ' + 'x="{x}" y="{y}" style="font-size:{fontsize}">{text}</text>',
        'line': '<line class="bliss-line" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>',
        'arc': '<path class="bliss-line" d="M {x1},{y1} A {r},{r} 0 0,0 {x2},{y2}"/>',
        'bigarc': '<path class="bliss-line" d="M {x1},{y1} A {r},{r} 0 1,0 {x2},{y2}"/>',
        'grid': '<line class="bliss-grid-{grid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'
    }

    def __init__(self, dot_radius=4, line_thickness=8, symbol_size=10, font_size=14):
        self.dot_radius = dot_radius
        self.line_thickness = line_thickness
        self.symbol_size = symbol_size
        self.font_size = font_size
        self.margin = self.symbol_size / 5  # default: 8
        self.punctmargin = -self.symbol_size / 10

    def get_data(self, strdata):
        return self.SVG_START + strdata + self.SVG_END

    def blissymbol_svg(self, bliss_name):
        """
        Writes an SVG file to xml with for the Blissymbol with this
        bliss_name.

        :param bliss_name: str, name of Blissymbol to write SVG file for
        :return: str, XML string for Blissymbol's SVG file
        """
        bliss_chars = self.decompose_to_chars(bliss_name)
        chars_strdata = [self.blisschar_svg(bc) for bc in bliss_chars]
        bliss_strdata = self.get_data("\n".join(chars_strdata))
        self.write_svg(bliss_name, bliss_strdata)
        return bliss_strdata

    def blisschar_svg(self, blisschar):
        """
        Writes an SVG file to xml with for this Bliss character blisschar.

        :param blisschar: str, name of Bliss-char to write SVG file for
        :return: str, XML string for Bliss-char's SVG file
        """
        return ""

    def write_svg(self, filename, string):
        """
        Writes an SVG file to xml with this string and
        saves it to this filename.

        :param filename: str, filename for SVG image to save
        :param string: str, XML information for SVG image
        :return: None
        """
        return ""

    # Private predicates from BlissViewer adapted to Python
    def is_modifier(self, mod):
        return self.MODIFIERS.get(mod, False)

    def is_digit(self, dig):
        return dig[-7:] == '(digit)'

    def is_letter(self, letter):
        suffix = letter[-11:]
        return suffix == '(uppercase)' or suffix == '(lowercase)'

    def is_punctuation(self, punct):
        return self.PUNCTUATIONS.get(punct, False)

    def is_indicator(self, ind):
        return ind[:10] == 'indicator_' and ind not in self.MODIFIERS

    def decompose_to_chars(self, bliss_name):
        """
        Returns a list of (atomic) Bliss characters composing the
        Blissymbol with this bliss_name.

        :param bliss_name: str, name for Blissymbol to decompose
        :return: List[str], bliss_name Blissymbol's constituent Bliss-chars
        """
        bliss_chars = []

        if bliss_name in self.BLISS_WORDS:
            bliss_names = self.BLISS_WORDS[bliss_name]
            # recurse on bliss_name's constituent symbols
            for bn in bliss_names:
                bliss_chars += self.decompose_to_chars(bn)
        elif bliss_name in self.BLISS_CHARS:
            # end recursion when bliss_name is a Bliss-char
            bliss_chars.append(bliss_name)

        return bliss_chars

    def blissymbol_image(self, bliss_name):
        """
        Draws and returns an Image of the Blissymbol with this
        bliss_name according to specifications in BLISSDATA_CHARS.

        :param bliss_name: str, name of Blissymbol to draw
        :return: Image, Blissymbol with this bliss_name
        """
        # TODO: GET BLISSYMBOLS WORKING
        blisschars = self.decompose_to_chars(bliss_name)
        bliss_images = []

        for i in range(len(blisschars)):
            blisschar = blisschars[i]
            if blisschar in self.BLISS_CHARS:
                if i == 0:
                    bliss_image = self.bliss_char_image(blisschar, right_space=True)
                elif 0 < i < len(blisschars)-1:
                    bliss_image = self.bliss_char_image(blisschar, left_space=True, right_space=True)
                else:
                    bliss_image = self.bliss_char_image(blisschar, left_space=True)

                if bliss_image is not None:
                    bliss_images.append(bliss_image)
            else:
                bliss_images.append(self.blissymbol_image(blisschar))

        print("currently on bliss:\t", bliss_name, end="\n\n")
        print("\t\t\tshowing image for bliss...")
        bliss_image = beside_all(bliss_images, trim_imgs=False)
        bliss_image.show()
        input("continue?\n")
        return bliss_image

    def bliss_char_image(self, char_name, left_space=False, right_space=False):
        """
        Draws and returns an Image of the Bliss character with this
        char_name according to specifications in BLISSDATA_CHARS.

        :param char_name: str, name of Bliss-char to draw
        :return: Image, Bliss-char with this char_name
        """
        # TODO: GET CHARS WORKING
        chardata = self.BLISS_CHARS[char_name]
        char_shapes = chardata["d"]
        lspace = self.BLISSQUARE_SPACE if left_space else 0   # self.BLISS_KERNING_LEFT.get(char_name, 0) if left_space else 0
        rspace = self.BLISSQUARE_SPACE if right_space else 0  # self.BLISS_KERNING_RIGHT.get(char_name, 0) if right_space else 0
        char_width = chardata.get("w", 0)
        img_width = lspace + char_width + rspace
        print(char_name, chardata)
        char_height = chardata.get("h", 0)


        img_width += self.line_thickness * 2
        char_height += self.line_thickness * 2

        #char_midwidth = char_width / 2
        #char_center = BLISS_CENTER[char_name]

        char_image = make_blank_img(img_width, char_height, opacity=0)

        for char_shape in char_shapes:
            shape_name = char_shape["d"]
            shape_x = char_shape["x"]
            shape_y = char_shape["y"]
            shape_image = self.bliss_shape_image(shape_name)
            if shape_image is not None:
                char_image.paste(shape_image, box=(shape_x, shape_y))

        print("\tcurrently on char: \t", char_name, end="\n\n")
        print("\t\t\tshowing image for char...")
        char_image.show()
        input("continue?\n")
        return char_image

    def bliss_shape_image(self, shape_name):
        # SHAPES KINDA WORKING

        # x & y values appear to be oriented as Cartesian coordinates,
        # i.e. centred in the lower-left corner (rather than top-left)
        # therefore use (height - y) as top-left centred y-coord
        subshapes_data = self.BLISS_SHAPES[shape_name]
        img_x, img_y = (0, 0)

        for subshape_data in subshapes_data:
            subshape_x = subshape_data["x"]
            subshape_y = subshape_data["y"]
            img_x = max(img_x, subshape_x)
            img_y = max(img_y, subshape_y)

        img_x += self.line_thickness * 2
        img_y += self.line_thickness * 2

        shape_image = make_blank_img(img_x, img_y, opacity=0)

        for subshape_data in subshapes_data:
            subshape_name = subshape_data["d"]
            subshape_x = subshape_data["x"]
            subshape_y = subshape_data["y"]

            if subshape_name in self.BLISS_PATHS:
                subshape_image = self.bliss_path_image(subshape_name)
            elif subshape_name in self.BLISS_SHAPES:
                subshape_image = self.bliss_shape_image(subshape_name)
            else:
                raise KeyError("Invalid shape or path name:  " + subshape_name)

            x, y = (subshape_x, subshape_y)
            print("\t\tpasting", subshape_name, "at coords: ", x, ", ", y)
            shape_image.paste(subshape_image, (x, y))

        print("\t\tcurrently on shape:\t", shape_name, end="\n\n")
        print("\t\tshowing image for shape...")
        shape_image.show()
        input("continue?\n")
        return shape_image

    def bliss_path_image(self, path_name):
        pathdata = self.BLISS_PATHS[path_name]
        form = pathdata["form"]
        w = max(2, pathdata["w"])
        h = max(2, pathdata["h"])

        w += self.line_thickness * 2
        h += self.line_thickness * 2

        path_image = make_blank_img(w, h, opacity=0)
        path_draw = ImageDraw.Draw(path_image)

        radius = pathdata.get("r", None)
        x = pathdata.get("x", None)
        y = pathdata.get("y", None)
        x1 = pathdata.get("x1", None)
        x2 = pathdata.get("x2", None)
        y1 = pathdata.get("y1", None)
        y2 = pathdata.get("y2", None)

        if form == "arc" or form == "bigarc":
            draw_arc(path_image, (x1, y1, x2, y2), width=self.line_thickness, outline='black')
        elif form == "circle" or form == "disc":
            draw_ellipse(path_image, (x, y, x+w, y+h), width=self.line_thickness, outline='black')
        elif form == "dot":
            draw_ellipse(path_image, (0, 0, radius + self.dot_radius, radius + self.dot_radius),
                         width=self.line_thickness, outline='black')
        elif form == "line":
            path_draw.line((x1, y1, x2, y2), fill='black', width=self.line_thickness)
        elif form == "text":
            text = pathdata["text"]
            size = self.font_size + pathdata["fontsize"]
            text_img = text_image(text, lang="English", size=size, colour='black', bg_opacity=0)
            path_image.paste(text_img, box=(x, y))

        print("\t\t\tcurrently on path: \t", path_name)
        print("\t\t\tshowing image for path...")
        path_image.show()
        #input("continue?\n")
        return path_image



drawer = BlissDrawer()
drawer.blissymbol_image("blind").show()


"""
BLISS_DRAWER:

    An adaptation of the BlissViewer class from JavaScript to Python
    for writing and displaying SVG files.
"""
import os, sys
PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(PATH)
import json
import math
import re
from bs4 import BeautifulSoup
from speechart.images import *
from math import degrees, pi, sin, cos, asin, acos


class BlissDrawer:
    """
    A class for drawing Blissymbols in SVG from numerical data.
    """
    BLISS_PATH = PATH + "/resources/data/blissymbols_gh_pages/"

    BLISS_WORD_DATA = json.load(open(BLISS_PATH + "blissdata_words.json"))
    BLISS_CHAR_DATA = json.load(open(BLISS_PATH + "blissdata_chars.json"))

    BLISS_WORDS = BLISS_WORD_DATA["words"]
    BLISS_CHARS = BLISS_CHAR_DATA["chars"]

    BLISS_SHAPES = BLISS_CHAR_DATA["shapes"]
    BLISS_PATHS = BLISS_CHAR_DATA["paths"]

    BLISS_CENTER = BLISS_CHAR_DATA["center"]  # center of Bliss-chars relative to image's absolute center
    BLISS_KERNING_LEFT = BLISS_CHAR_DATA["kerning_left"]  # distance of Bliss-char relative to chars on its left
    BLISS_KERNING_RIGHT = BLISS_CHAR_DATA["kerning_right"]  # distance of Bliss-char relative to chars on its right

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
    BLISSQSPACE = BLISSQUARE / 4
    GRIDSIZE = BLISSQUARE / 2
    BLISSWORD_IS_ADDED = " ___BLISSWORD_IS_ALREADY_ADDED___"

    # SVG information
    SVG_START = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' \
                '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.0//EN" ' \
                '"https://www.w3.org/Graphics/SVG/1.1/DTD/svg11-flat-20110816.dtd">\n' \
                '<svg xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="true" stroke-linecap="round" ' \
                'class="bliss-svg" width="{w}" height="{h}" viewBox="{x} {y} {w} {h}">\n' \
                '<g fill="none" style="stroke:black;stroke-width:{strokewidth}">\n'
    SVG_END = '</g>\n</svg>'
    SVG_ELEMS = {
        'dot': '<circle class="bliss-dot" cx="{x}" cy="{y}" r="{r}"/>',
        'disc': '<circle class="bliss-disc" cx="{x}" cy="{y}" r="{r}"/>',
        'circle': '<circle class="bliss-line" cx="{x}" cy="{y}" r="{r}"/>',
        'text': '<text class="bliss-text" text-anchor="middle" ' +
                'x="{x}" y="{y}" style="font-size:{fontsize}">{text}</text>',
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
        self.blissoup = None
        self.reset_blissoup()

    def reload_word_data(self):
        self.BLISS_WORD_DATA = json.load(open(self.BLISS_PATH + "blissdata_words.json", 'r', encoding='utf-8'))
        self.BLISS_WORDS = self.BLISS_WORD_DATA['words']

    def dump_word_data(self):
        json.dump(self.BLISS_WORD_DATA, open(self.BLISS_PATH + "blissdata_words.json", 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1, sort_keys=True)

    def reset_blissoup(self):
        self.blissoup = self.new_soup()

    def new_soup(self, text=''):
        return BeautifulSoup(text, 'lxml')

    # Private predicates
    def is_modifier(self, mod):
        return self.MODIFIERS.get(mod, False)

    def is_digit(self, dig):
        return dig is not None and dig[-7:] == '(digit)'

    def is_letter(self, letter):
        try:
            suffix = letter[-11:]
        except TypeError:
            return False
        else:
            return suffix == '(uppercase)' or suffix == '(lowercase)'

    def is_punctuation(self, punct):
        return self.PUNCTUATIONS.get(punct, False)

    def is_indicator(self, ind):
        return ind[:10] == 'indicator_' and ind not in self.MODIFIERS

    def get_data(self, id):
        """
        Returns this id key's data from BLISS_WORD_DATA or
        BLISS_CHAR_DATA.  Must be one of a Bliss path, shape, char,
        or word.

        :param id: str, name of key for a Bliss path/shape/char/word
        :return: dict/list, data for Bliss path/shape/char/word with id
        """
        data = self.BLISS_PATHS.get(id, None)
        if data is not None:
            return data
        data = self.BLISS_SHAPES.get(id, None)
        if data is not None:
            return data
        data = self.BLISS_CHARS.get(id, None)
        if data is not None:
            return data
        return self.BLISS_WORDS.get(id, None)

    def to_svg_grid(self, dim, grid):
        svg = ""
        margin = self.margin
        left = dim['left'] - margin
        right = dim['right'] + margin
        top = dim['top'] - margin
        bottom = dim['bottom'] + margin
        istart = int(math.floor(grid * left / self.GRIDSIZE))
        istop = int(math.ceil(grid * max(right, bottom) / self.GRIDSIZE))

        for i in range(istart, istop):
            xy = self.GRIDSIZE * i / grid
            gridtype = 'minor' if i % grid != 0 else 'major'
            if xy <= right:
                svg += self.SVG_ELEMS['grid'].format(grid=gridtype, x1=xy, x2=xy, y1=top, y2=bottom) + "\n"
            if xy <= bottom:
                svg += self.SVG_ELEMS['grid'].format(grid=gridtype, x1=left, x2=right, y1=xy, y2=xy) + "\n"

        return svg

    def to_svg_obj(self, x, y, obj):
        if type(obj) == str:
            print("FOUND A STRING:", obj)
            return self.to_svg_obj(x, y, self.get_data(obj))
        elif type(obj) == list:
            print("FOUND A LIST:", obj)
            svg = ""
            for o in obj:
                svg += self.to_svg_obj(x, y, o)
            return svg
        elif type(obj) == dict and 'd' in obj:
            print("FOUND A DICT:", obj)
            x += obj.get('x', 0)
            y += obj.get('y', 0)
            return self.to_svg_obj(x, y, obj['d'])
        else:
            clone = {}

            for k in obj:
                if k[0] == 'x':
                    clone[k] = obj[k] + x
                elif k[0] == 'y':
                    clone[k] = self.BLISSHEIGHT - obj[k] - y
                else:
                    clone[k] = obj[k]

            if clone['form'] == 'text':
                clone['x'] += clone['w'] / 2
                clone['y'] += clone['h']
            elif clone['form'] == 'dot':
                clone['r'] = self.dot_radius

            return self.SVG_ELEMS[clone['form']].format(**clone) + "\n"

    def expand_list(self, words, inds):
        chars = []

        for n in range(len(words)):
            w = words[n]
            if self.is_indicator(w) and len(chars) != 0:
                prev_inds = chars[len(chars) - 1]['inds']
                prev_inds.extend(inds)
                prev_inds.append(w)
                inds = []
            elif self.is_modifier(w) or self.is_punctuation(w) or (n == 0 and self.is_digit(w)):
                chars.append({'ch': w, 'inds': []})
            else:
                chars.append({'ch': w, 'inds': inds})
                inds = []

        groups = []
        new_inds = []

        for n in range(len(chars)):
            ch, chinds = chars[n]['ch'], chars[n]['inds']
            if ch in self.BLISS_WORDS:
                new_groups_inds = self.expand_list(self.BLISS_WORDS[ch], new_inds + chinds)
                groups.extend(new_groups_inds['groups'])
                new_inds = new_groups_inds['inds']
            else:
                if ch not in self.BLISS_CHARS:
                    print("Unknown character:", ch)
                    ch = "question_mark"
                groups.append({'ch': ch, 'inds': new_inds + chinds})
                new_inds = []

        return {'groups': groups, 'inds': new_inds + inds}

    def expand_word(self, word):
        if type(word) == str:
            word = [word]

        groups_inds = self.expand_list(word, [])
        groups, grinds = groups_inds['groups'], groups_inds['inds']

        if len(grinds) != 0:
            raise IOError("Inds left:", word, "-->", groups, "/", grinds)

        chars = []
        x, left, right, prev = 0, 0, 0, None
        print("GROUPS:", groups)

        for g in range(len(groups)):
            print("\tGROUP:", groups[g])
            ch = groups[g]['ch']
            inds = groups[g]['inds']
            w = self.BLISS_CHARS[ch]['w']
            x += self.calculate_spacing(prev, ch)
            chars.append({'x': x, 'y': 0, 'd': ch})

            if inds is not None:
                iw = (len(inds) - 1) * self.BLISSQSPACE / 2

                for ind in inds:
                    iw += self.BLISS_CHARS[ind]['w']
                    if ind in self.BLISS_CENTER:
                        iw += 2 * self.BLISS_CENTER[ind]

                ix = x + (w - iw) / 2

                if ch in self.BLISS_CENTER:
                    ix += self.BLISS_CENTER[ch]

                left = min(left, ix)
                iy = max(0, self.BLISS_CHARS[ch].get('h', self.BLISSHEIGHT) - 192)

                for i in range(len(inds)):
                    ind = inds[i]
                    if i > 0:
                        ix += self.BLISSQSPACE / 2
                    chars.append({'x': ix, 'y': iy, 'd': ind})
                    ix += self.BLISS_CHARS[ind]['w']

                right = max(right, ix)
                print("new right:", right)

            x += w
            prev = ch

        right = max(right, x)
        return {'top': 0, 'bottom': self.BLISSHEIGHT, 'left': left, 'right': right, 'chars': chars}

    def calculate_spacing(self, prev, current):
        """
        Returns the proper spacing between prev and current
        Blissymbols.

        :param prev: str, name of previous Blissymbol
        :param current: str, name of current Blissymbol
        :return: int, proper spacing between prev and current
        """
        if prev is None:
            return 0
        elif self.is_kerning_possible(prev, current):
            return 0
        elif self.is_digit(prev) and self.is_digit(current):
            return self.BLISSQSPACE / 2
        elif self.is_letter(prev) and self.is_letter(current):
            return self.BLISSQSPACE / 2
        elif current == 'comma':
            return self.BLISSQSPACE * (3 / 4)
        else:
            return self.BLISSQSPACE

    def default_kerning(self, h):
        """
        Returns the default kerning for Blissymbols of this height.

        :param h: int, height of Blissymbol
        :return: int, kerning for Blissymbols of this height
        """
        if h is None:
            return 12  # indicator = 0b1100
        elif h <= 80:
            return 2   # lowest = 0b0010
        elif h <= 144:
            return 6   # low = 0b0110
        return 14      # normal, high, highest = 0b1110

    def is_kerning_possible(self, prev, current):
        """
        Returns True if kerning possible between prev and
        current, False otherwise.

        :param prev: str, name of previous Blissymbol
        :param current: str, name of current Blissymbol
        :return: bool, True if kerning possible between prev and current
        """
        if (self.BLISS_CHARS[prev]['w'] <= 24) or (self.BLISS_CHARS[current]['w'] <= 24):
            return False
        right = self.BLISS_KERNING_RIGHT.get(prev, None)
        if right is None:
            right = self.default_kerning(self.BLISS_CHARS[prev]['h'])
        left = self.BLISS_KERNING_LEFT.get(current, None)
        if left is None:
            left = self.default_kerning(self.BLISS_CHARS[current]['h'])
        return right == 0 and left == 0

    def add_blissword(self, parent, blissword, textword=None, grid=None):
        """
        Adds the Blissymbol with this blissword to this BeautifulSoup
        XML parent with the associated textword subtitle and grid size.

        :param parent: BeautifulSoup, holding XML for SVG image
        :param blissword: str, name of Blissymbol to add to parent
        :param textword: str, text to display below blissword
        :param grid: Optional[str], size of grid to overlay
        :return: None
        """
        bliss_elem = parent.new_tag("span", attrs={"className": "bliss-symbol"})
        self.blissoup.append(bliss_elem)
        if textword != None:
            text_elem = self.blissoup.new_tag("span", attrs={"className": "bliss-caption"})
            if textword.isalpha():
                text_elem['textContent'] = textword
            else:
                text_elem['innerHTML'] = '&nbsp'
            parent.append(text_elem)

        if blissword is not None and len(blissword) != 0:
            first = blissword[0] if type(blissword) == list else blissword
            if self.is_punctuation(first):
                parent['className'] += ' punctuation'
            self.add_blissvg(bliss_elem, blissword, grid)

    def add_blissvg(self, parent, blissword, grid=None):
        """
        Adds the Blissymbol with this blissword to this BeautifulSoup
        XML parent with this grid size.

        :param parent: BeautifulSoup, holding XML for SVG image
        :param blissword: str, name of Blissymbol to add to parent
        :param grid: Optional[str], size of grid to overlay
        :return: None
        """
        exp = self.expand_word(blissword)
        margin = self.margin
        x = exp['left'] - margin - (self.line_thickness / 2)
        y = exp['top'] - margin - (self.line_thickness / 2)
        w = exp['right'] - exp['left'] + (2 * margin) + self.line_thickness
        h = exp['bottom'] - exp['top'] + (2 * margin) + self.line_thickness

        svg = self.SVG_START.format(x=x, y=y, w=w, h=h, strokewidth=self.line_thickness)
        if grid is not None:
            svg += self.to_svg_grid(exp, grid)
        svg += self.to_svg_obj(0, 0, exp['chars'])
        svg += self.SVG_END

        parent.append(svg)

    def add_blisstext(self, parent, blisswords, textwords, grid=None):
        """
        Adds the Blissymbol with this blissword to this BeautifulSoup
        XML parent with this grid size.

        :param parent: BeautifulSoup, holding XML for SVG image
        :param blisswords: List[str], names of Blissymbols to add to parent
        :param textwords: List[str], words to display below blisswords
        :param grid: Optional[str], size of grid to overlay
        :return: None
        """
        for i in range(len(blisswords)):
            textwd = textwords[i] if i < len(textwords) else ''
            self.add_blissword(parent, blisswords[i], textwd, grid)

    def add_blisswords_to_cls(self, cls, grid=None):
        """
        Adds blisswords with this grid setting to all
        XML elements in self.blissoup with the name 'cls'.

        :param cls: str, name of class to find
        :param grid: Optional[int], overlaid grid size
        :return: None
        """
        elements = self.blissoup.find_all(cls)
        for i in range(len(elements)):
            elem = elements[i]
            if self.BLISSWORD_IS_ADDED not in elem['className']:
                title = re.split("\s+", elem['title'].strip())
                text = elem['textContent']
                elem['textContent'] = ""
                self.add_blissword(elem, title, text, grid)
                elem['className'] += self.BLISSWORD_IS_ADDED

    def write_blissvg(self, blissword, grid=None):
        """
        Writes an SVG file for the Blissymbol with this blissword
        and saves it to this directory.
        ~
        If grid is set to an integer, SVG file will contain an
        overlaid grid with grid's size.

        :param blissword: str, name of Blissymbol to write SVG for
        :param grid: Optional[int], size of overlaid grid
        :return: str, XML for SVG image
        """
        self.add_blissvg(self.blissoup, blissword, grid=grid)
        xmlstr = self.blissoup.string
        self.reset_blissoup()
        svg_file = open(PATH + "/" + blissword + ".svg", mode="w")
        svg_file.writelines(xmlstr)
        svg_file.close()
        return xmlstr

    def create_blissvg(self, filename, blisswords, grid=None):
        """
        Writes an SVG file to XML with these blisswords and
        saves it to this filename.

        :param filename: str, filename for SVG image to save
        :param blisswords: List[str], XML for SVG image
        :return: str, XML for SVG image
        """
        self.add_blissword_to_words(filename, blisswords)
        return self.write_blissvg(filename, grid)

    def blissvg_image(self, blissword, grid=None):
        svg = self.write_blissvg(blissword, grid)
        # TODO: convert XML to Pillow Image

    def add_blissword_to_words(self, word, blisswords):
        """
        Adds this word and its corresponding derivative blisswords
        as a key-value pair to blissdata_words.json.

        :param word: str, word to define in Blissymbols
        :param blisswords: str, Blissymbols in this word
        :return: None
        """
        self.BLISS_WORD_DATA['words'][word] = blisswords
        self.dump_word_data()
        self.reload_word_data()

    def decompose_to_chars(self, blissname):
        """
        Returns a list of (atomic) Bliss characters composing the
        Blissymbol with this blissname.

        :param blissname: str, name for Blissymbol to decompose
        :return: List[str], bliss_name Blissymbol's constituent Bliss-chars
        """
        bliss_chars = []

        if blissname in self.BLISS_WORDS:
            blissnames = self.BLISS_WORDS[blissname]
            # recurse on blissname's constituent symbols
            for bn in blissnames:
                bliss_chars += self.decompose_to_chars(bn)
        elif blissname in self.BLISS_CHARS:
            # end recursion when blissname is a Bliss-char
            bliss_chars.append(blissname)

        return bliss_chars

    def get_style_settings(self, blissoup):
        gdata = blissoup.find('g')
        stylesettings = {'fill': gdata.get('fill')}
        style = gdata.get('style')
        styles = style.split(";")
        for style in styles:
            k, v = style.split(":")
            stylesettings[k.strip()] = v.strip()
        return stylesettings

    def blissword_to_image(self, blissword):
        """
        Returns this XML for a Blissymbol SVG image rendered as a
        PIL Image.

        :param svgxml: str/BeautifulSoup, XML for SVG image
        :return: Image, svg turned into image
        """
        derivs = self.decompose_to_chars(blissword)
        xmls = [self.write_blissvg(deriv) for deriv in derivs]
        imgs = [self.blissvg_to_image(xml) for xml in xmls]
        bliss_img = self.empty_image()

        for i in range(len(imgs)):
            img = imgs[i]
            deriv = derivs[i]

            if self.is_indicator(deriv) or self.is_modifier(deriv):
                pass
            else:
                pass

        bliss_img.show()
        return bliss_img

    def blissvg_to_image(self, svgxml):
        """
        Returns this XML for a Blissymbol SVG image rendered as a
        PIL Image.

        :param svgxml: str/BeautifulSoup, XML for SVG image
        :return: Image, svg turned into image
        """
        if type(svgxml) != str:
            svgxml = svgxml.string

        blissoup = self.new_soup(svgxml)
        svgdata = blissoup.find('svg')
        width, height = float(svgdata.get('width')), float(svgdata.get('height'))

        print("XML:\t", svgxml)

        stylesettings = self.get_style_settings(blissoup)
        outline = stylesettings.get('stroke', (0, 0, 0))
        shapes = {}

        img = make_blank_img(int(width), int(height), opacity=0)
        drawing = aggdraw.Draw(img)
        pen = aggdraw.Pen(outline, self.line_thickness)
        brush = aggdraw.Brush(outline)

        for elt in blissoup.find_all():
            if elt.name == 'circle':
                cx = float(elt.get('cx'))
                cy = float(elt.get('cy'))
                r = float(elt.get('r'))
                drawing.ellipse((cx-r, cy-r, cx+r, cy+r), pen, brush)
                drawing.flush()
                shapes.setdefault(elt.name, list())
                shapes[elt.name].append({'x': cx, 'y': cy, 'r': r})

            elif elt.name == 'line':
                x1 = float(elt.get('x1'))
                x2 = float(elt.get('x2'))
                y1 = float(elt.get('y1'))
                y2 = float(elt.get('y2'))
                drawing.line((x1, y1, x2, y2), pen)
                drawing.flush()
                shapes.setdefault(elt.name, list())
                shape = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}
                shapes[elt.name].append(shape)

            elif elt.name == 'path':
                d = elt.get('d')
                m, a = d.split('A')
                x1, y1 = tuple(int(float(xy)) for xy in m[2:-1].split(","))
                r1r2, is_big_arc, n2n3, x2y2 = a[1:].split(" ")
                r = float(r1r2.split(",")[0])
                x2, y2 = tuple(int(float(xy)) for xy in x2y2.split(","))
                print("PATH:", d)
                x_diff = abs(x2 - x1)
                y_diff = abs(y2 - y1)
                xy_diff = self.euclidean_distance(x1, y1, x2, y2)
                print("X2 - X1:", x_diff)
                print("Y2 - Y1:", y_diff)
                print("XY DIFF:", xy_diff)

                origin_x1, origin_y1 = 0, 0            # x1 - x1, y1 - y1
                offset_x2, offset_y2 = x_diff, y_diff  # x2 - x1, y2 - y1
                # add x1 to return to original xy vals

                '''
                cx = (r**2 - cy**2)**0.5
                cy = (r**2 - cx**2)**0.5

                cx = (offset_y2**2 - offset_x2**2 - 2*offset_y2*cy)/2*offset_x2
                cy = (offset_y2**2 - 2*offset_x2*cx - offset_x2**2)/2*offset_y2

                cx = (r**2 - cy**2)**0.5 = (offset_y2**2 - offset_x2**2 - 2*offset_y2*cy) / (2*offset_x2)
                cy = (r**2 - cx**2)**0.5 = (offset_y2**2 - 2*offset_x2*cx - offset_x2**2) / (2*offset_y2)
                '''

                # Cy = (AB**2 + AC**2 - BC**2)/(2 * AB)
                # Cy = (xy_diff**2 + r**2 - r**2)/(2 * xy_diff)
                # Cy = (xy_diff**2)/(2 * xy_diff)
                cy = (xy_diff**2)/(2 * xy_diff)

                # Cx = (AC**2 - Cy**2)**0.5
                cx = (r**2 - cy**2)**0.5

                print("CENTRE:", cx, cy)

                # figure out quadrant of each x,y coord
                if x1 > cx:
                    if y1 > cy:
                        start_quadrant = 4
                    else:
                        start_quadrant = 1
                else:
                    if y1 > cy:
                        start_quadrant = 3
                    else:
                        start_quadrant = 2

                if x2 > cx:
                    if y2 > cy:
                        end_quadrant = 4
                    else:
                        end_quadrant = 1
                else:
                    if y2 > cy:
                        end_quadrant = 3
                    else:
                        end_quadrant = 2

                #cx += x1
                #cy += y1

                # calculate inverse sine for triangle from x,y coords to centre
                # sin(theta/2) = o/h
                # sin^-1(sin(theta/2)) = sin^-1(o/h)
                # theta/2 = sin^-1(o/h)
                # theta = 2 * sin^-1(o/h)
                # theta = 2 * sin^-1(o/h)
                start_path_diff = self.pythagorean_theorem(x1 - cx, y1 - cy)/2
                end_path_diff = self.pythagorean_theorem(x2 - cx, y2 - cy)/2

                print("START PATH DIFF:", start_path_diff)
                print("  END PATH DIFF:", end_path_diff)
                start_sine = start_path_diff / r
                end_sine = end_path_diff / r

                print("START SINE:", start_sine)
                print("  END SINE:", end_sine)

                loops = 0

                # x = cx + r * cos(a)
                # x - cx = r * cos(a)
                # (x - cx) / r = cos(a)
                # a = acos((x - cx) / r)

                # y = cy + r * sin(a)
                # y - cy = r * sin(a)
                # (y - cy) / r = sin(a)
                # a = asin((y - cy) / r)

                quadrant_rads = lambda q: (pi/2) * (q - 1)

                while True:
                    try:
                        start_rad = 2 * asin(start_sine + quadrant_rads(start_quadrant))
                    except ValueError:
                        start_sine -= pi/2
                        print("START SINE:", start_sine)
                        loops += 1
                    else:
                        print("START RAD:", start_rad)
                        break

                    if loops > 1000:
                        return

                while True:
                    try:
                        print("  END SINE:", end_sine)
                        end_rad = 2 * asin(end_sine + quadrant_rads(end_quadrant))
                    except ValueError:
                        end_sine -= pi/2
                        print("  END SINE:", end_sine)
                        loops += 1
                    except TypeError:
                        end_rad = 0
                        break
                    else:
                        print("  END RAD:", end_rad)
                        break

                    if loops > 1000:
                        return

                start_angle, end_angle = degrees(start_rad), degrees(end_rad)

                x1_arc, x2_arc = x1, y1 - 2*cy
                y1_arc, y2_arc = x2 + 2*cx, y2
                start, end = start_angle, end_angle

                print("START:", start)
                print("END:", end)

                if not is_big_arc:
                    start, end = end, start

                drawing.arc((x1_arc, y1_arc, x2_arc, y2_arc), start, end, pen)
                drawing.flush()
                shapes.setdefault(elt.name, list())
                shape = {'x1': x1_arc, 'y1': y1_arc, 'x2': x2_arc, 'y2': y2_arc, 'r': r, 'start': start, 'end': end}
                shapes[elt.name].append(shape)
                print("ARC:", shape)

            elif elt.name == 'text':
                x = float(elt.get('x'))
                y = float(elt.get('y'))
                fontsize = float(elt.get('fontsize'))
                text = elt.get('text')
                font = load_default_font(size=fontsize)
                drawing.Text((x, y), font=font)
                drawing.flush()
                shapes.setdefault(elt.name, list())
                shape = {'x': x, 'y': y, 'fontsize': fontsize, 'text': text}
                shapes[elt.name].append(shape)

        print(shapes)
        img.show()
        return img

    def euclidean_distance(self, x1, y1, x2, y2):
        """
        Returns the distance between point x1,y1 and x2,y2.

        :param x1: float, x-val of point 1
        :param y1: float, y-val of point 1
        :param x2: float, x-val of point 2
        :param y2: float, y-val of point 2
        :return: float, distance between points 1 & 2
        """
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    def pythagorean_theorem(self, a=0, b=0, c=0):
        """
        Returns the result of whichever of a, b, or c
        is left as 0.0 in the Pythagorean equation for a
        right triangle, i.e., a**2 + b**2 == c**2.

        :param a: float, flat side of a right triangle
        :param b: float, other flat side of a right triangle
        :param c: float, hypotenuse of a right triangle
        :return: float, result of missing variable
        """
        if a == 0:
            cb = c**2 - b**2
            a = cb**0.5
            return a
        elif b == 0:
            ca = c**2 - a**2
            b = ca**0.5
            return b
        elif c == 0:
            ab = a**2 + b**2
            print("AB:", ab)
            c = ab**0.5

        return c

    def blissvg_to_image2(self, svgxml):
        """
        Returns this XML for a Blissymbol SVG image rendered as a
        PIL Image.

        :param svgxml: str/BeautifulSoup, XML for SVG image
        :return: Image, svg turned into image
        """
        if type(svgxml) != str:
            svgxml = svgxml.string

        blissoup = self.new_soup(svgxml)

        svgdata = blissoup.find('svg')
        width, height = float(svgdata.get('width')), float(svgdata.get('height'))
        viewbox = [float(v) for v in svgdata.get('viewbox').split(" ")]
        if viewbox[0] != 0:
            viewbox[2] -= viewbox[0]
            viewbox[0] = 0
        if viewbox[1] != 0:
            viewbox[3] -= viewbox[1]
            viewbox[1] = 0

        gdata = blissoup.find('g')
        fill = gdata.get('fill')
        stylesettings = {}
        style = gdata.get('style')
        styles = style.split(";")
        for style in styles:
            k, v = style.split(":")
            stylesettings[k.strip()] = v.strip()
        outline = stylesettings.get('stroke', (0, 0, 0))
        shapes = {}

        img = make_blank_img(int(width), int(height), opacity=0)
        drawing = aggdraw.Draw(img)
        pen = aggdraw.Pen(outline, self.line_thickness)
        brush = aggdraw.Brush(outline)

        last_x, last_y = 0, 0

        for elt in blissoup.find_all():
            if elt.name == 'circle':
                cx = float(elt.get('cx'))
                cy = float(elt.get('cy'))
                r = float(elt.get('r'))
                drawing.ellipse((cx-r, cy-r, cx+r, cy+r), pen, brush)
                drawing.flush()
                shapes.setdefault(elt.name, list())
                shapes[elt.name].append({'x': cx, 'y': cy, 'r': r})
                last_x = max(last_x, cx + r)
                last_y = max(last_y, cy + r)
            elif elt.name == 'line':
                x1 = float(elt.get('x1'))
                x2 = float(elt.get('x2'))
                y1 = float(elt.get('y1'))
                y2 = float(elt.get('y2'))
                drawing.line((x1, y1, x2, y2), pen)
                drawing.flush()
                shapes.setdefault(elt.name, list())
                shapes[elt.name].append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})
                last_x = x2 #max(last_x, x2)
                last_y = y2 #max(last_y, y2)
            elif elt.name == 'path':
                d = elt.get('d')
                m, a = d.split('A')
                x1, y1 = tuple(float(xy) for xy in m[2:-1].split(","))
                r1r2, is_big_arc, n2n3, x2y2 = a[1:].split(" ")
                r = float(r1r2.split(",")[0])  # for all Blissymbols r1 == r2
                x2, y2 = tuple(float(xy) for xy in x2y2.split(","))
                print("PATH:", d)

                x_path_diff = x2 - x1
                y_path_diff = y2 - y1
                xy_path_diff = (x_path_diff**2 + y_path_diff**2)**0.5
                
                if x1:
                    pass
                
                print("XY2 - XY1:", xy_path_diff)

                # Cy = (AB**2 + AC**2 - BC**2)/(2 * AB)
                cy = abs((xy_path_diff**2)/(2 * xy_path_diff))

                # Cx = (AC**2 - Cy**2)**0.5
                cx = abs(r**2 - cy**2)**0.5

                print("CENTRE:", cx, cy)

                # figure out quadrant of each x,y coord
                if x1 > cx:
                    if y1 > cy:
                        start_quadrant = 4
                    else:
                        start_quadrant = 1
                else:
                    if y1 > cy:
                        start_quadrant = 3
                    else:
                        start_quadrant = 2

                if x2 > cx:
                    if y2 > cy:
                        end_quadrant = 4
                    else:
                        end_quadrant = 1
                else:
                    if y2 > cy:
                        end_quadrant = 3
                    else:
                        end_quadrant = 2

                # calculate inverse sine for triangle from x,y coords to centre
                # sin(theta/2) = o/h
                # sin^-1(sin(theta/2)) = sin^-1(o/h)
                # theta/2 = sin^-1(o/h)
                # theta = 2 * sin^-1(o/h)
                # theta = 2 * sin^-1(o/h)
                start_path_diff = (((x1 - cx)**2 + (y1 - cy)**2)**0.5)/2
                end_path_diff = (((x2 - cx)**2 + (y2 - cy)**2)**0.5)/2

                print("START PATH DIFF:", start_path_diff)
                print("  END PATH DIFF:", end_path_diff)
                start_sine = start_path_diff / r
                end_sine = end_path_diff / r

                print("START SINE:", start_sine)
                print("  END SINE:", end_sine)

                loops = 0

                # x = cx + r * cos(a)
                # x - cx = r * cos(a)
                # (x - cx) / r = cos(a)
                # a = acos((x - cx) / r)

                # y = cy + r * sin(a)
                # y - cy = r * sin(a)
                # (y - cy) / r = sin(a)
                # a = asin((y - cy) / r)

                quadrant_rads = lambda q: (pi/2) * (q - 1)

                while True:
                    try:
                        start_rad = 2 * asin(start_sine + quadrant_rads(start_quadrant))
                    except ValueError:
                        start_sine -= pi/2
                        print("START SINE:", start_sine)
                        loops += 1
                    else:
                        print("START RAD:", start_rad)
                        break

                    if loops > 1000:
                        return

                while True:
                    try:
                        end_rad = 2 * asin(end_sine + quadrant_rads(end_quadrant))
                    except ValueError:
                        end_sine -= pi/2
                        print("  END SINE:", end_sine)
                        loops += 1
                    else:
                        print("  END RAD:", end_rad)
                        break

                    if loops > 1000:
                        return

                start_angle, end_angle = degrees(start_rad), degrees(end_rad)

                print("LAST X:", last_x)
                print("LAST Y:", last_y)

                x1_arc, x2_arc = last_x, last_x + (2*r)
                y1_arc, y2_arc = last_y - (2*r), last_y
                start, end = start_angle, end_angle

                print("START:", start)
                print("END:", end)

                if not is_big_arc:
                    start, end = end, start

                drawing.arc((x1_arc, y1_arc, x2_arc, y2_arc), start, end, pen)
                drawing.flush()
                shapes.setdefault(elt.name, list())
                arc = {'x1': x1_arc, 'y1': y1_arc, 'x2': x2_arc, 'y2': y2_arc, 'r': r, 'start': start, 'end': end}
                shapes[elt.name].append(arc)
                print("ARC:", arc)
                last_x = max(last_x, x2_arc)
                last_y = max(last_y, y2_arc)

            elif elt.name == 'text':
                x = float(elt.get('x'))
                y = float(elt.get('y'))
                fontsize = float(elt.get('fontsize'))
                text = elt.get('text')
                font = load_default_font(size=fontsize)
                drawing.Text((x, y), font=font)
                drawing.flush()
                shapes.setdefault(elt.name, list())
                shapes[elt.name].append({'x': x, 'y': y, 'fontsize': fontsize, 'text': text})
                last_x = max(last_x, x + font.getsize(text)[0])
                last_y = max(last_y, y + font.getsize(text)[1])

        print(shapes)
        img.show()
        return img


d = BlissDrawer()
ear_svg = d.write_blissvg("ear") #d.create_blissvg("sexy", ["sexual_intercourse,intercourse,copulation", "indicator_(description)"])
#d.create_blissvg("modern", ["newness,novelty", "intensity", "indicator_(description)"])
#d.create_blissvg("modernism", ["newness,novelty", "intensity"])
#d.create_blissvg("modernity", ["newness,novelty", "intensity"])
#d.create_blissvg("postmodernism", ["after,behind", "modernism"])
d.blissvg_to_image(ear_svg).save('ear.png')
#img = Image.open(PATH + "/sexy.svg")
#img = open(PATH + "/sexy.svg")
#img

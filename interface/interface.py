import os, sys
import random
import pygame
import string
import fpdf
from pygame.locals import *
from PIL import Image, ImageDraw, ImageFont
import translation.blisscribe as blisscribe


class BlissGame:
    """
    A class for representing an instance of someone using
    Blissymbols to read.

    Users can choose whether they'd prefer to download a PDF
    or read in-app.
    """
    FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

    ORIGIN = (0, 0)
    WIDTH = 1000 #1024
    HEIGHT = 700 #768
    RESOLUTION = (WIDTH, HEIGHT)
    HEADER = pygame.image.load(FILE_PATH + "header.png")
    TICK = 1000

    HEADER_FONT = ImageFont.truetype(font="Arial Rounded Bold.ttf", size=50)
    FONT = ImageFont.truetype(font="Arial Rounded Bold.ttf", size=25)

    COLOURS = {"charcoal": (44, 44, 44),
               "yellow": (243, 220, 26),
               "grey": (200, 200, 200),
               "white": (255, 255, 255)}

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.bg = None
        self.translator = None #blisscribe.BlissTranslator()
        self.screen = None
        self.main()

    def init_screen(self):
        if self.screen is None:
            self.screen = pygame.display.set_mode(self.RESOLUTION)
            #screen = pygame.display.set_mode(self.RESOLUTION, FULLSCREEN)

    def init_bg(self):
        if self.bg is None:
            self.bg = self.load_surface("background.png")

    def init_translator(self, language, font_path=None, font_size=20):
        if self.translator is None:
            if font_path is None:
                self.translator = blisscribe.BlissTranslator(language, font_size=font_size)
            else:
                self.translator = blisscribe.BlissTranslator(language, font_path, font_size)
        else:
            self.translator.set_language(language)
            if font_path is not None:
                self.translator.set_font(font_path, font_size)

    def tile(self, img, res=RESOLUTION):
        """
        Returns this image tiled as a background with
        resolution res.

        :param img: Image, image to tile to background
        :param res: tuple(int,int), background to fit tile to
        :return: Image, tiled background of size res
        """
        img = Image.open("bg_tile.jpeg") #self.load_surface("bg_tile.jpeg")
        w, h = res
        imgw, imgh = img.size

        if w < imgw or h < imgh:
            return img
        background = Image.new("RGBA", res, (255,255,255,255))

        for x in range(0, w, imgw):
            for y in range(0, h, imgh):
                background.paste(img, (x,y))

        background.save("background.png")

        return background

    def make_button(self, label, size):
        """
        Returns an image of a button of given size with given label.

        :param label: str, label for output button
        :param size: tuple(int,int), size of output button
        :return: Image, button in given size with given label
        """
        button = Image.new("RGB", size, self.COLOURS["yellow"])
        sketch = ImageDraw.Draw(button)
        textsize = sketch.textsize(text=label, font=self.FONT)
        textw, texth = textsize
        sketch.text((size[0]/2 - textw/2, size[1]/2 - texth/2),
                    label,
                    font=self.FONT,
                    fill=(255, 255, 255))
        return button

    def make_buttons(self, labels):
        # later include "teach" for ML
        # later allow users to hover over a word/Blissymbol to retrieve
        #   definitions & alternate translations
        button_w = self.WIDTH // (len(labels)*2)
        button_h = self.HEIGHT // 10
        button_wh = (button_w, button_h)
        buttons = {label: self.make_button(label.lower(), button_wh) for label in labels}
        return buttons

    def render_buttons(self, buttons, selected, space=50):
        """
        Renders the given set of buttons, including the user's
        given selected button.

        :param buttons: dict, where...
            key (str) - button label
            val (Image) - button image
        :param selected: str, button label to highlight for user
        :param space: int, space in between buttons
        :return: None
        """
        buttons_iter = iter(sorted(buttons, reverse=True))
        label = next(buttons_iter)
        img = buttons[label]
        button_w, button_h = img.size
        total_h = (button_h + space) * len(buttons)
        start_h = (self.HEIGHT - space*(len(buttons) - 1)) - total_h

        for y in range(start_h, self.HEIGHT, button_h+space):
            img = buttons[label]

            if label == selected:
                frame = 10
                size = (button_w+frame, button_h+frame)
                bg = Image.new("RGBA", size, self.COLOURS["grey"])
                bg.paste(img, (frame//2, frame//2))
                img = bg

            button = self.img_to_surface(img)
            x = self.WIDTH//2 - img.size[0]//2
            self.screen.blit(button, (x, y))
            try:
                label = next(buttons_iter)
            except StopIteration:
                break

        pygame.display.flip()

    def display_text(self, text, screen=None, posn=None):
        """
        Prints text to screen.  If text length is 0, no change.
        ~
        If screen is None, screen is set to this EmotionSim game's
        current screen.
        ~
        If posn is None, text is displayed in middle of screen.
        Otherwise, text is displayed at posn.

        :param message: str, message to display
        :param screen: Display, screen to render text box onto
        :param posn: (int, int), position to render text box
        :return: None
        """
        match = pygame.font.match_font(u"arialroundedmtbold")
        fontobject = pygame.font.Font(match, 12)
        frame = 4

        if screen is None:
            screen = self.screen

        if posn is None:
            width, height = screen.get_width()//6, screen.get_height()//6
        else:
            width, height = posn

        msg = fontobject.render(text, 1, self.COLOURS["charcoal"])
        msg_w = msg.get_width()
        msg_h = msg.get_height()

        screen.blit(msg,
                    (width-(msg_w//2), height-(msg_h//2)))

        pygame.display.flip()

    def display_box(self, message, screen=None, posn=None):
        """
        Prints message to screen.  If message length is 0, prints empty box.
        ~
        If screen is None, screen is set to this EmotionSim game's
        current screen.
        ~
        If posn is None, box is displayed in middle of screen.
        Otherwise, box is displayed at posn.

        :param message: str, message to display in text box
        :param screen: Display, screen to render text box onto
        :param posn: (int, int), position to render text box
        :return: None
        """
        match = pygame.font.match_font(u"arialroundedmtbold")
        fontobject = pygame.font.Font(match, 12)
        frame = 4

        if screen is None:
            screen = self.screen

        if posn is None:
            width, height = screen.get_width()//6, screen.get_height()//6
        else:
            width, height = posn

        msg = fontobject.render(message, 1, self.COLOURS["charcoal"])
        msg_w = self.WIDTH*(1/2.0) #msg.get_width()
        msg_h = msg.get_height()  #self.HEIGHT/10.0 #msg.get_height()

        pygame.draw.rect(screen, self.COLOURS["white"],
                         (width, # width - box_w/2,
                          height, # height - box_h/2,
                          msg_w, msg_h), 0)
        pygame.draw.rect(screen, self.COLOURS["charcoal"],
                         (width - frame, #width - (msg_w+frame)/2,
                          height - frame, #height - (msg_h+frame)/2,
                          msg_w + frame, msg_h + frame), 1) #msg_w+frame, msg_h+frame), 1)

        screen.blit(msg,
                    (width, height))

        pygame.display.flip()

    def ask(self, question, screen, posn=None):
        "ask(question, screen) -> answer"
        pygame.font.init()
        current_string = []
        self.display_box(question + "\t" + "".join(current_string), screen, posn)
        while 1:
            inkey = self.get_key()
            if inkey == pygame.QUIT:
                current_string = current_string[0:-1]
            elif inkey == K_BACKSPACE:
                current_string = current_string[0:-1]
            elif inkey == K_RETURN:
                break
            elif inkey == K_MINUS:
                current_string.append("_")
            elif inkey == K_ESCAPE:
                sys.exit(0)
            elif inkey <= 127:
                current_string.append(chr(inkey))
            self.display_box(question + ": " + "".join(current_string), screen, posn)
        return "".join(current_string)

    def translate(self):
        start_x = self.WIDTH//10
        start_y = self.HEIGHT//10
        text = self.ask("text to translate", self.screen, (start_x, start_y))
        language = self.ask("language", self.screen, (start_x, start_y*2))
        font_size = 20
        self.init_translator(language, font_size=font_size)
        inkey = self.get_key()

        if inkey == pygame.QUIT:
            return 0

        elif inkey == K_RETURN:
            title = ""
            nouns = True
            verbs = True
            adjvs = True
            other = True
            page_nums = False
            fast_translate = True
            poses = {}

            if nouns:
                poses.update(blisscribe.NOUNS)
            if verbs:
                poses.update(blisscribe.VERBS)
            if adjvs:
                poses.update(blisscribe.ADJS)
                poses.update(blisscribe.ADVS)
            if other:
                poses.update(blisscribe.OTHER)

            self.blit_bg()
            pdf = self.translator.translate(text, title=title, img_w=self.WIDTH, imgls_h=self.HEIGHT,
                                            page_nums=page_nums)
            '''
            pages = self.translator.translate_to_pages(text, title=title, img_w=self.WIDTH, img_h=self.HEIGHT)
            pages = [self.img_to_surface(blisscribe.overlay(pg, blisscribe.blank_image(pg.size[0], pg.size[1])))
                     for pg in pages]
            page_count = 0

            while page_count < len(pages):
                inkey = self.get_key()

                if inkey == pygame.QUIT:
                    return 0
                elif inkey == K_LEFT:
                    page_count -= 1
                elif inkey == K_RIGHT:
                    page_count += 1
                elif inkey == K_ESCAPE:
                    return 0

                page = pages[page_count % len(pages)]
                pygame.display.flip()
                #self.screen.fill(self.COLOURS["white"])
                self.screen.blit(page, self.ORIGIN)
                pygame.display.flip()
            '''

        elif inkey == K_ESCAPE:
            return 0

    def make_header(self):
        """
        Returns the Blisscribe header as a Pygame Surface.

        :return: Surface, the Blisscribe header image
        """
        title = "Blisscribe"
        space = 10

        icon = Image.open("blisscribe_icon.jpg")
        icon.thumbnail((120, 120))
        icon_w, icon_h = icon.size
        bgw, bgh = self.WIDTH, (icon_h + space) * 2

        title_w, title_h = self.HEADER_FONT.getsize(title)
        x, y = bgw//2 - title_w//2, bgh - space - title_h
        left, upper = self.WIDTH//2 - icon_w//2, y - space - icon_h

        header = Image.new("RGBA", (bgw, bgh), (255, 255, 255, 0))
        header.paste(icon, (left, upper))
        sketch = ImageDraw.Draw(header)
        sketch.text((x, y), title, fill=self.COLOURS["charcoal"], font=self.HEADER_FONT)
        header.save("header.png")
        surf = self.img_to_surface(header)
        return surf

    def img_to_surface(self, img):
        """
        Converts the given PIL image to a Pygame Surface.

        :param img: Image, PIL image
        :return: Surface, Pygame-compatible Surface of this image
        """
        data = img.tobytes()
        size = img.size
        mode = img.mode
        img = pygame.image.fromstring(data, size, mode)
        return img

    def tick(self):
        self.clock.tick(self.TICK)

    def blit_bg(self):
        self.screen.blit(self.bg, self.ORIGIN)
        self.screen.blit(self.HEADER, self.ORIGIN)

    def blit(self, img):
        self.screen.blit(img, self.ORIGIN)

    def flip(self):
        pygame.display.flip()

    def main(self):
        # user inputs:
        #   text to translate
        #   text language
        #   title of text (opt)
        #   font to use (opt)
        #   font size
        #   translate... translate_nouns, translate_verbs, adj/advs, translate_other
        #   translate uncommon words
        #   include page #s
        pygame.init()
        pygame.display.set_caption('Blisscribe')

        level = True
        labels = ["translate", "learn"]
        selected = 0

        self.init_screen()
        self.init_bg()
        self.blit(self.bg)
        self.tick()
        self.flip()

        self.tick()
        self.blit(self.HEADER)
        intro_buttons = self.make_buttons(labels)
        self.render_buttons(intro_buttons, labels[selected])
        self.flip()

        while level >= 1:
            self.clock.tick(self.TICK)
            self.blit_bg()
            self.render_buttons(intro_buttons, labels[selected % len(labels)])

            inkey = self.get_key()

            if inkey == pygame.QUIT:
                level = 0
            elif inkey == K_ESCAPE:
                level -= 1
            elif inkey == K_RETURN:
                level += 1
            elif inkey == K_UP:
                selected -= 1
            elif inkey == K_DOWN:
                selected += 1

            # make app work just with keys first,
            # then add mouse support

            selected_label = labels[selected % len(labels)]

            while level >= 2:
                self.blit(self.bg)

                if selected_label == "translate":
                    lvl = self.translate()
                    if lvl is not None:
                        level = lvl
                    break
                elif selected_label == "learn":
                    break

                pygame.display.flip()

            #self.get_mouse()

            pygame.display.flip()

    def language_form(self):
        """
        Displays a language form to the user with
        selections for the language to translate from.
        Returns the user's selection.

        :return: str, language to translate from
        """
        selections = []
        # display selections as drop-down box
        select_language = None
        return select_language

    def font_form(self):
        """
        Displays a font form to the user with
        options for font family and font size.
        Returns a tuple of user selections.

        :return: tuple(str, int), desired font family & size
        """
        # font family
        # font size
        family = None
        size = None
        return family, size

    def translatables_form(self):
        """
        Displays a translatables form to the user with
        options for which parts of speech to translate from
        nouns, verbs, adjs/advs and other.
        Returns a tuple of user selections.

        :return: 4-tuple(bool), choices for parts of speech to translate
        """
        nouns = False
        verbs = False
        adjvs = False
        other = False
        return nouns, verbs, adjvs, other

    def text_form(self):
        """
        Displays a text entry form to the user with
        2 text boxes for the text's title and for text to enter.
        Returns a tuple of user input.

        :return: 2-tuple(str), title and text to translate
        """
        # title
        # text
        title = ""
        text = ""
        return title, text

    def main2(self):
        # user inputs:
        #   text to translate
        #   text language
        #   title of text (opt)
        #   font to use (opt)
        #   font size
        #   translate... translate_nouns, translate_verbs, adj/advs, translate_other
        #   translate uncommon words
        #   include page #s
        pygame.init()
        pygame.display.set_caption('Blisscribe')

        level = True
        # incl form for native grammar vs bliss grammar
        forms = ['language', 'font family', 'font size', 'nouns', 'verbs', 'adjvs', 'other', 'title', 'text']
        labels = ["translate", "learn"]
        selected = 0

        self.init_screen()
        self.bg = self.load_surface("background.png")
        self.screen.blit(self.bg, self.ORIGIN)
        self.clock.tick(self.TICK)
        pygame.display.flip()

        self.clock.tick(self.TICK)
        self.screen.blit(self.HEADER, self.ORIGIN)
        buttons = self.make_buttons(labels)
        self.render_buttons(buttons, labels[selected])
        pygame.display.flip()

        while level >= 1:
            self.clock.tick(self.TICK)
            self.screen.blit(self.bg, self.ORIGIN)
            self.screen.blit(self.HEADER, self.ORIGIN)
            self.render_buttons(buttons, labels[selected])

            inkey = self.get_key()

            if inkey == pygame.QUIT:
                level = 0
            elif inkey == K_ESCAPE:
                level -= 1
            elif inkey == K_RETURN:
                level += 1
            elif inkey == K_UP:
                selected -= 1
            elif inkey == K_DOWN:
                selected += 1

            # make app work just with keys first,
            # then add mouse support

            selected = selected % len(labels)

            while level >= 2:
                self.screen.blit(self.bg, self.ORIGIN)

                if labels[selected] == "translate":
                    lvl = self.translate()
                    if lvl is not None:
                        level = lvl
                elif labels[selected] == "learn":
                    break

                pygame.display.flip()

            self.get_mouse()

            pygame.display.flip()

    def get_key(self):
        while 1:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                return event.type
            elif event.type == KEYDOWN:
                return event.key
            else:
                pass

    def get_mouse(self):
        # FIXME: return mouse info, not event.key
        while 1:
            event = pygame.event.poll()
            if event.type in {MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP}:
                return pygame.mouse.get_pos()
            else:
                pass

    def load_image(self, name):
        """
        Loads the image by the given name into Pygame.

        :param name: str, name of image file to load (incl. extension)
        :return: Image, loaded image into Pygame
        """
        path = str(self.FILE_PATH) + name
        return Image.open(path)

    def load_surface(self, name):
        """
        Loads the image with this name into Pygame as a Surface.

        :param name: str, name of image file to load (incl. extension)
        :return: Surface, image as a Pygame Surface
        """
        path = str(self.FILE_PATH) + name

        try:
            image = pygame.image.load(path)
        except pygame.error:
            print("Cannot load image: " + name)
            raise SystemExit

        return image

    def background_img(self, tile_img, width=WIDTH, height=HEIGHT):
        bg_img = blisscribe.blank_image(0, 0)
        while bg_img.size[0] < width:
            bg_img = blisscribe.beside(bg_img, tile_img)
        bg_row = bg_img
        while bg_img.size[1] < height:
            bg_img = blisscribe.above(bg_img, bg_row)
        bg_img = blisscribe.trim(bg_img, (0, 0, int(width), int(height)))
        bg_img.save("background.png")


bg = BlissGame()


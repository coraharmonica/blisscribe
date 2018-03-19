import os, sys
import random
import pygame
import string
from pygame.locals import *
from PIL import Image, ImageDraw, ImageFont

import main.bliss_web.bliss_app.bliss_webapp.blisscribe_py.blisscribe as blisscribe

class BlissGame:
    """
    A class for representing an instance of someone using
    Blissymbols to read.

    Users can choose whether they'd prefer to download a PDF
    or read in-app.
    """
    FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

    WIDTH = 1000 #1024
    HEIGHT = 700 #768
    RESOLUTION = (WIDTH,HEIGHT)
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
        screen = pygame.display.set_mode(self.RESOLUTION)
        #screen = pygame.display.set_mode(self.RESOLUTION, FULLSCREEN)
        return screen

    def tile(self, img, res=RESOLUTION):
        """
        Returns this image tiled as a background with
        resolution res.

        :param img: Image, image to tile to background
        :param res: tuple(int,int), background to fit tile to
        :return: Image, tiled background of size res
        """
        img = Image.open("bg_tile.jpeg") #self.load_image("bg_tile.jpeg")
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
        button_w = self.WIDTH / (len(labels)+3)
        button_h = self.HEIGHT / 10
        button_wh = (button_w, button_h)
        buttons = {label: self.make_button(label.lower(), button_wh) for label in labels}
        return buttons

    def render_buttons(self, buttons, selected):
        """
        Renders the given set of buttons, including the user's
        given selected button.

        :param buttons: dict, where...
            key (str) - button label
            val (Image) - button image
        :param selected: str, button label to highlight for user
        :return: None
        """
        buttons_iter = iter(sorted(buttons, reverse=True))
        label = buttons_iter.next()
        img = buttons[label]
        button_w, button_h = img.size
        space = 50
        total_h = (button_h + space) * len(buttons)
        start_h = (self.HEIGHT - space*3) - total_h

        for y in range(start_h, self.HEIGHT, button_h+space):
            img = buttons[label]

            if label == selected:
                frame = 10
                size = (button_w+frame, button_h+frame)
                bg = Image.new("RGBA", size, self.COLOURS["grey"])
                bg.paste(img, (frame/2, frame/2))
                img = bg

            button = self.img_to_surface(img)
            x = self.WIDTH/2 - img.size[0]/2
            self.screen.blit(button, (x, y))
            try:
                label = buttons_iter.next()
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
            width, height = screen.get_width()/6, screen.get_height()/6
        else:
            width, height = posn

        msg = fontobject.render(text, 1, self.COLOURS["charcoal"])
        msg_w = msg.get_width()
        msg_h = msg.get_height()

        screen.blit(msg,
                    (width-(msg_w/2), height-(msg_h/2)))

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
            width, height = screen.get_width()/6, screen.get_height()/6
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
        "ask(screen, question) -> answer"
        pygame.font.init()
        current_string = []
        self.display_box(question + "\t" + string.join(current_string,""), screen) #, posn)
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
            self.display_box(question + ": " + "".join(current_string), screen) #, posn)
        return "".join(current_string)

    def intro(self, screen):
        """
        Renders Blisscribe's introductory animation.
        ~
        Returns Bliss header used in animation.

        :param screen: Surface, display to render animation to
        :return: None
        """
        header = self.make_header(screen)
        #screen.blit(header, (0, 0))
        return header

    def make_header(self, screen):
        """
        Returns the Blisscribe header as a Pygame Surface.

        :param screen: Surface, display to render animation to
        :return: Surface, the Blisscribe header image
        """
        title = "Blisscribe"
        space = 10

        icon = Image.open("blisscribe_icon.jpg")
        icon.thumbnail((120, 120))
        icon_w, icon_h = icon.size
        bgw, bgh = self.WIDTH, (icon_h + space) * 2

        title_w, title_h = self.HEADER_FONT.getsize(title)
        x, y = bgw/2 - title_w/2, bgh - space - title_h

        # render icon
        left, upper = self.WIDTH/2 - icon_w/2, y - space - icon_h
        #header.paste(icon, (left, upper))

        header = Image.new("RGBA", (bgw, bgh), (255, 255, 255, 0))
        header.paste(icon, (left, upper))
        sketch = ImageDraw.Draw(header)
        sketch.text((x, y), title, fill=self.COLOURS["charcoal"], font=self.HEADER_FONT)
        pygame.display.flip()

        surf = self.img_to_surface(header)
        screen.blit(surf, (0, 0))

        # render Blisscribe title
        '''
        for i in range(0, len(title)+1):
            header = Image.new("RGBA", (bgw, bgh), (255, 255, 255, 0))
            header.paste(icon, (left, upper))
            chars = title[:i]
            char_w, char_h = self.HEADER_FONT.getsize(chars)
            x, y = bgw/2 - char_w/2, bgh - space - char_h
            sketch = ImageDraw.Draw(header)
            sketch.text((x, y), chars, fill=self.COLOURS["charcoal"], font=self.HEADER_FONT)
            surf = self.img_to_surface(header)
            self.screen.blit(surf, (0, 0))
            pygame.display.flip()
            #self.screen.fill(self.COLOURS["white"])
            self.screen.blit(self.bg, (0, 0))
        '''

        return self.img_to_surface(header)

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
        origin = (0, 0)
        labels = ["translate", "learn"]
        selected = 0

        self.screen = self.init_screen()
        self.bg = self.load_image("background.png")
        self.screen.blit(self.bg, origin)
        self.clock.tick(self.TICK)
        header = self.intro(self.screen)
        pygame.display.flip()
        self.clock.tick(self.TICK)
        self.screen.blit(header, origin)
        buttons = self.make_buttons(labels)
        self.render_buttons(buttons, labels[selected])
        pygame.display.flip()

        while level >= 1:
            self.clock.tick(self.TICK)
            self.screen.blit(self.bg, origin)
            self.screen.blit(header, origin)
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
                self.screen.blit(self.bg, origin)

                if labels[selected] == "translate":
                    start_x = self.WIDTH/10
                    start_y = self.HEIGHT/10
                    text = self.ask("text to translate", self.screen, (start_x, start_y))
                    language = self.ask("language", self.screen, (start_x, start_y*2))
                    title = ""
                    font = "Arial"
                    font_path = blisscribe.BlissTranslator.FONT_FAMS[font]
                    font_size = 20
                    nouns = True
                    verbs = True
                    adjvs = True
                    other = True
                    uncommon = True
                    page_nums = False
                    fast_translate = True

                    inkey = self.get_key()

                    if inkey == pygame.QUIT:
                        level = 0
                        break

                    elif inkey == K_RETURN:
                        if self.translator is None:
                            self.translator = blisscribe.BlissTranslator(language, font_path, font_size)
                        else:
                            self.translator.set_language(language)
                            self.translator.set_font(font_path, font_size)
                        self.translator.set_translatables(nouns, verbs, adjvs, other)
                        self.translator.set_translate_all(uncommon)
                        self.translator.set_page_nums(page_nums)
                        self.translator.set_fast_translate(fast_translate)
                        pages = self.translator.translate(text, title=title, img_w=self.WIDTH, img_h=self.HEIGHT)
                        page_count = 0

                        while page_count < pages:
                            inkey = self.get_key()

                            if inkey == pygame.QUIT:
                                level = 0
                                break
                            elif inkey == K_LEFT:
                                page_count -= 1
                            elif inkey == K_RIGHT:
                                page_count += 1
                            elif inkey == K_ESCAPE:
                                level = 0
                                break

                            page_img = pages[page_count]
                            page = self.img_to_surface(page_img)

                            pygame.display.flip()
                            self.screen.fill(self.COLOURS["white"])
                            self.screen.blit(page, origin)
                            pygame.display.flip()

                    elif inkey == K_ESCAPE:
                        level = 0
                        break

                elif labels[selected] == "learn":
                     break

                pygame.display.flip()

            # inmouse = self.get_mouse()

            # if inmouse == MOUSEBUTTONUP:
            #    pass
            # elif inmouse == MOUSEBUTTONDOWN:
            #    pass
            # elif inmouse == MOUSEMOTION:
            #    pass

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
                return event.key
            else:
                pass

    def load_image(self, name):
        """
        Loads the image by the given name into Pygame.

        :param name: str, name of image file to load (incl. extension)
        :return: Image, loaded image into Pygame
        """
        path = str(self.FILE_PATH) + name

        try:
            image = pygame.image.load(path)
        except pygame.error: #, msg:
            print("Cannot load image: " + name)
            raise SystemExit #, msg

        return image

bg = BlissGame()
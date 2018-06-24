"""
NEURAL NET GAME

    Begin with the void.  Click symbols to branch outwards.
"""
import os, sys
import pygame
import string
from pygame.locals import *
from pygame.sprite import *
from PIL import Image, ImageDraw, ImageFont
import main.bliss_web.bliss_app.bliss_webapp.blisscribe_py.speechart.blissweb as blissweb
import main.bliss_web.bliss_app.bliss_webapp.blisscribe_py.speechart.neural_net.neural_net as neural_net


class NeuralWebGame(blissweb.BlissWeb):
    """
    A class for representing an instance of someone using
    Blissymbols to read.

    Users can choose whether they'd prefer to download a PDF
    or read in-app.
    """
    FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

    WIDTH = 1000
    HEIGHT = 700
    RESOLUTION = (WIDTH, HEIGHT)
    TICK = 1000
    ORIGIN = (0, 0)

    HEADER_FONT = ImageFont.truetype(font="Arial Rounded Bold.ttf", size=25)
    FONT = ImageFont.truetype(font="Arial Rounded Bold.ttf", size=15)

    COLOURS = {"charcoal": (44, 44, 44),
               "yellow": (243, 220, 26),
               "grey": (200, 200, 200),
               "white": (255, 255, 255),
               "black": (0, 0, 0)}

    STATES = ["minus,no,without", "and,also,plus,too", "life"]

    def __init__(self, language="English"):
        blissweb.BlissWeb.__init__(self, language)
        self.clock = pygame.time.Clock()
        self.screen = None
        self.main()

    def init_screen(self):
        screen = pygame.display.set_mode(self.RESOLUTION)
        return screen

    def state_circle(self, state_num):
        """
        Returns a circle with state_num overlaid.
        ~
        If given state_num is a success state, output circle
        will be outlined.

        :param state_num: int, number for state circle
        :return: Image, circle with state_num overlaid
        """
        is_success = state_num in self.success_states
        state_colour = self.lookup_state_colour(state_num)
        img = blissweb.circle(self.RADIUS - 8, fill=state_colour, outline='gray')
        transitions = self.state_transitions(state_num)
        transition = self.beside_all(transitions, mini=True)

        if is_success:
            outline = 'gray'
        else:
            outline = 'white'

        img = blissweb.overlay(blissweb.circle(self.RADIUS, fill=None, outline=outline), img)
        img = blissweb.overlay(transition, img)
        return img

    def state_arrow(self, length, angle, transition=""):
        """
        Returns an arrow image with this length and angle,
        overlaid with this transition label.

        :param length: int, length of arrow
        :param angle: int[0,360), angle of arrow
        :param transition: str, transition label
        :return: Image, arrow with this length, angle, & transition label
        """
        return blissweb.arrow(width=length, height=2, fill="lightgray",
                              angle=angle, label="", font_size=self.FONT_SIZE, lang=self.chart_lang, font=self.font)

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

    def render_nodes(self):
        img = self.visualize_connections() #self.image()
        midx, midy = self.WIDTH/2 - img.width/2, self.HEIGHT/2 - img.height/2
        surf = self.img_to_surface(img)
        self.screen.blit(surf, (midx, midy))

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
        Prints text_image to screen.  If text_image length is 0, no change.
        ~
        If screen is None, screen is set to this EmotionSim game's
        current screen.
        ~
        If posn is None, text_image is displayed in middle of screen.
        Otherwise, text_image is displayed at posn.

        :param message: str, message to display
        :param screen: Display, screen to render text_image box onto
        :param posn: (int, int), position to render text_image box
        :return: None
        """
        match = pygame.font.match_font(u"arialroundedmtbold")
        fontobject = pygame.font.Font(match, 12)

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

        :param message: str, message to display in text_image box
        :param screen: Display, screen to render text_image box onto
        :param posn: (int, int), position to render text_image box
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
        :return: Surface, display with header rendered
        """
        header = self.make_header(screen)

        return header

    def make_header(self, screen):
        """
        Returns the Blisscribe header as a Pygame Surface.

        :param screen: Surface, display to render animation to
        :return: Surface, the Blisscribe header image
        """
        title = "In the beginning, there was the void."
        space = 10
        bgw, bgh = self.WIDTH, self.HEIGHT

        title_w, title_h = self.HEADER_FONT.getsize(title)
        x, y = bgw/2 - title_w/2, space + title_h

        header = Image.new("RGBA", (bgw, bgh), (255, 255, 255, 0))
        sketch = ImageDraw.Draw(header)
        sketch.text((x, y), title, fill=self.COLOURS["black"], font=self.HEADER_FONT)
        pygame.display.flip()

        surf = self.img_to_surface(header)
        screen.blit(surf, (0, 0))
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

    def main(self):
        # user inputs:
        #   text_image to translate
        #   text_image language
        #   title of text_image (opt)
        #   font to use (opt)
        #   font size
        #   translate... translate_nouns, translate_verbs, adj/advs, translate_other
        #   translate uncommon words
        #   include page #s
        pygame.init()
        pygame.display.set_caption('Neural Netting')

        self.screen = self.init_screen()
        self.screen.fill(color=self.COLOURS["white"])
        self.clock.tick(self.TICK)
        header = self.intro(self.screen)
        pygame.display.flip()
        self.clock.tick(self.TICK)
        self.screen.blit(header, self.ORIGIN)
        pygame.display.flip()
        state = 0

        while True:
            self.clock.tick(self.TICK)
            self.screen.fill(color=self.COLOURS["white"])
            if len(self.states) == 1:
                self.screen.blit(header, self.ORIGIN)
            self.render_nodes()

            inkey = self.get_key()
            # make app work just with keys first,
            # then add mouse support
            if inkey == pygame.QUIT:
                break
            elif inkey == K_ESCAPE:
                break
            elif inkey == K_SPACE:
                if len(self.states) < len(self.STATES):
                    label = self.STATES[state]
                    blissymbol = self.translator.blissword_to_blissymbol(label)
                    if state == 0:
                        self.add_state(0, label=blissymbol)
                    else:
                        start = max(state-2, 0)
                        prev_states = {i for i in range(start, state)}
                        incoming = set()
                        for ps in prev_states:
                            self.add_state(ps, label=blissymbol, outgoing={state})
                            incoming.update(self.state_connections(ps))
                        self.add_connection(label=blissymbol, incoming=incoming)
                    state += 1
                    print "CONNECTIONS:", self.connections

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
        except pygame.error:
            print("Cannot load image: " + name)
            raise SystemExit

        return image

    class NeuralNode:
        def __init__(self, blissword):
            self.blissword = blissword


class NeuralNodeSprite(pygame.sprite.Sprite):
    """
    Represents a clickable node from a neural web in a NeuralWebGame.
    """
    def __init__(self, label, game):
        pygame.sprite.Sprite.__init__(self)
        self.node = neural_net.NeuralNode(label)
        self.game = game
        self.net = self.game.net
        self.image = self.net.img_to_surface(self.net.node_img(self))
        self.rect = self.image.get_rect()

    def update(self, selected=False):
        self.image = self.net.img_to_surface(self.net.node_img(self, selected))



class NeuralNodeSprites(pygame.sprite.Group):
    """
    Represents a clickable node from a neural web in a NeuralWebGame.
    """
    def __init__(self, sprites, game):
        pygame.sprite.Group.__init__(self, sprites)
        self.game = game
        self.net = self.game.net



bg = NeuralWebGame()


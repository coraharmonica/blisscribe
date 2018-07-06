from bliss_drawer import *
from images import *
import unittest


class TestParseBlissData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # setup before testing starts
        cls.drawer = BlissDrawer()

    def testDrawBlissymbol(self):
        drawn_img = self.drawer.blissymbol_image("rabbit,hare")
        stored_img = get_bliss_img("rabbit,hare")
        self.assertEqual(drawn_img, stored_img)

    def testDrawBlissChar(self):
        drawn_img = self.drawer.bliss_char_image("a,an,any")
        stored_img = get_bliss_img("a,an,any")
        self.assertEqual(drawn_img, stored_img)

    def testDrawBlissShape(self):
        img = self.drawer.bliss_shape_image("+0001")
        img = self.drawer.bliss_shape_image("@0196")

    def testDrawBlissPath(self):
        img = self.drawer.bliss_path_image("#A106-E:128") # arc
        img = self.drawer.bliss_path_image("#A270-NE:16") # bigarc
        img = self.drawer.bliss_path_image("#CIRCLE:128") # circle
        img = self.drawer.bliss_path_image("#DISC:8")     # disc
        img = self.drawer.bliss_path_image("#DOT:0")      # dot
        img = self.drawer.bliss_path_image("#L+0:128")    # line
        img = self.drawer.bliss_path_image("#TEXT:K:56")  # text


if __name__ == '__main__':
    unittest.main()


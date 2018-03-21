# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blisscribe import *
import unittest


class TestBlisscribe(unittest.TestCase):
    BLISS_TRANSLATOR = BlissTranslator()

    def test_get_subderivations(self):
        rabbit = Blissymbol("rabbit,hare.png", "NN",  "(rodent + ear)",  {"English": ["rabbit", "hare"]},
                            self.BLISS_TRANSLATOR)
        self.assertEqual([str(deriv) for deriv in rabbit.get_subsymbols()], ["animal,beast", "teeth", "ear"])


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
from blisscribe import *
import unittest


class TestBlisscribe(unittest.TestCase):
    BLISS_TRANSLATOR = BlissTranslator()
    BLISS_TRANSLATOR.lex_parser.fresh_bliss_derivations()

    def test_classifier(self):
        self.BLISS_TRANSLATOR.init_classifier()

    def test_get_subderivations(self):
        rabbit = self.BLISS_TRANSLATOR.word_to_blissymbol("rabbit,hare", language="English", pos="NN")
        self.assertEqual([str(d) for d in rabbit.derivation_blissymbols()], ["animal,beast", "teeth", "ear"])

    def test_remove_parens(self):
        hyena_txt = u"animal,beast + sound + up,upward + mouth [up + mouth is a contraction of laugh,laughter]: " \
                     u"the hyena is known for its laughing sound"
        hyena_ans = u"animal,beast + sound + up,upward + mouth : " \
                    u"the hyena is known for its laughing sound"
        self.assertEqual(self.BLISS_TRANSLATOR.remove_parens(hyena_txt, starts={u"["}, ends={u"]"}), hyena_ans)

    def test_extract_parens(self):
        hyena_txt = u"animal,beast + sound + up,upward + mouth [up + mouth is a contraction of laugh,laughter]: " \
                     u"the hyena is known for its laughing sound"
        hyena_ans = u"up + mouth is a contraction of laugh,laughter"
        coffin_txt = u"(enclosure [modified, rectangular] + reclining,lying_(person_lying_down) " \
                     u"[modified, higher position, shortened line for feet])  - Character (superimposed - modified)"
        coffin_ans = u"enclosure [modified, rectangular] + reclining,lying_(person_lying_down) " \
                     u"[modified, higher position, shortened line for feet]"
        self.assertEqual(self.BLISS_TRANSLATOR.extract_parens(hyena_txt, starts={u"["}, ends={u"]"}), hyena_ans)
        self.assertEqual(self.BLISS_TRANSLATOR.extract_parens(coffin_txt, starts={u"("}, ends={u")"}), coffin_ans)

    BLISS_TRANSLATOR.refresh_bliss_dicts()


if __name__ == '__main__':
    unittest.main()


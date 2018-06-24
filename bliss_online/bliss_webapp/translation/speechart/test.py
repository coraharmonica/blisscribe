# coding: utf-8
"""
TEST:

    Testing suite for WiktionaryParser and derived classes.
"""
#from __future__ import unicode_literals
from blissweb import BlissWeb
from neural_net.neural_images import NeuralNodeImage, NeuralNetImage
from speecharts import SentenceChart
from morpheme_parser import *
import unittest
import main.bliss_web.bliss_app.bliss_webapp.blisscribe_py.excerpts as excerpts


class TestSpeechart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        unittest.TestCase.setUpClass()
        cls.maxDiff = None
        cls.words = dict()  # word-pronunciation dict in language & IPA
        cls.language = "English" #"Finnish"
        cls.parser = MorphemeParser(cls.language)
        cls.blissweb = BlissWeb(cls.language)
        cls.speechart = SentenceChart(cls.language)

        cls.nn1 = cls.blissweb.neural_net.create_node("minus,no,without")
        cls.nn2 = cls.blissweb.neural_net.create_node("and,also,plus,too")
        cls.nn3 = cls.blissweb.neural_net.create_node("life")
        cls.nn4 = cls.blissweb.neural_net.create_node("mind,intellect,reason")
        cls.nn5 = cls.blissweb.neural_net.create_node("body,trunk")
        cls.nn6 = cls.blissweb.neural_net.create_node("feeling,emotion,sensation")
        cls.nn7 = cls.blissweb.neural_net.create_node("love,affection")
        cls.nn8 = cls.blissweb.neural_net.create_node("person,human_being,individual,human")
        cls.nn9 = cls.blissweb.neural_net.create_node("existence,being_(1)")
        cls.nn10 = cls.blissweb.neural_net.create_node("soul")

        cls.nn1.set_outgoing([cls.nn3, cls.nn4])
        cls.nn2.set_outgoing([cls.nn3, cls.nn5])
        cls.nn3.set_outgoing([cls.nn4, cls.nn5])
        cls.nn6.extend_incoming([cls.nn4, cls.nn5])
        cls.nn6.extend_outgoing([cls.nn7])
        cls.nn8.extend_incoming([cls.nn3, cls.nn5])
        cls.nn9.extend_incoming([cls.nn3, cls.nn4])
        cls.nn10.extend_incoming([cls.nn6, cls.nn8, cls.nn3])

        cls.blissweb.neural_net.set_nodes([cls.nn1, cls.nn2, cls.nn3, cls.nn4, cls.nn5,
                                           cls.nn6, cls.nn7, cls.nn8, cls.nn9, cls.nn10])

        # cls.parser.common_phonemes(50)
    '''
    def test_table(self):
        self.parser.reset_language(language="Finnish")
        self.assertEqual(self.parser.word_declension(u"naapuri", language="Finnish"),
                         {u"singular": {u"nominative": [u"naapuri"],
                                        u"accusative > nom.": [u"naapuri"],
                                        u"accusative > gen.": [u"naapurin"],
                                        u"genitive": [u"naapurin"],
                                        u"partitive": [u"naapuria"],
                                        u"inessive": [u"naapurissa"],
                                        u"elative": [u"naapurista"],
                                        u"illative": [u"naapuriin"],
                                        u"adessive": [u"naapurilla"],
                                        u"ablative": [u"naapurilta"],
                                        u"allative": [u"naapurille"],
                                        u"essive": [u"naapurina"],
                                        u"translative": [u"naapuriksi"],
                                        u"instructive": [u"—"],
                                        u"abessive": [u"naapuritta"],
                                        u"comitative": [u"—"]},
                          u"plural": {u"nominative": [u"naapurit"],
                                      u"accusative > nom.": [u"naapurit"],
                                      u"accusative > gen.": [u"naapurit"],
                                      u"genitive": [u"naapurien",
                                                    u"naapureiden",
                                                    u"naapureitten"],
                                      u"partitive": [u"naapureita",
                                                     u"naapureja"],
                                      u"inessive": [u"naapureissa"],
                                      u"elative": [u"naapureista"],
                                      u"illative": [u"naapureihin"],
                                      u"adessive": [u"naapureilla"],
                                      u"ablative": [u"naapureilta"],
                                      u"allative": [u"naapureille"],
                                      u"essive": [u"naapureina"],
                                      u"translative": [u"naapureiksi"],
                                      u"instructive": [u"naapurein"],
                                      u"abessive": [u"naapureitta"],
                                      u"comitative": [u"naapureineen"]}})
        self.parser.word_declension("olla")

    def test_break_syllable(self):
        self.parser.reset_language("Polish")
        syllable = u"lat͡ɕ"
        ans = (u"l", u"a", u"t͡ɕ")
        self.assertEqual(self.parser.break_syllable(syllable), ans)

        self.parser.reset_language("Dutch")
        syllable = u"tjə"
        ans = (u"t", u"jə", u"")
        self.assertEqual(self.parser.break_syllable(syllable), ans)

    def test_break_syllables(self):
        self.parser.reset_language("Polish")
        ans = [(u"", u"ɔ", u""),
               (u"b", u"a", u""),
               (u"l", u"a", u"t͡ɕ")]
        ipa = u"ɔbalat͡ɕ"
        self.assertEqual(self.parser.break_syllables(ipa, use_syllables=False), ans)

        self.parser.reset_language("Dutch")
        ans = [(u"kl", u"ɛi", u"̯n"),
               (u"t", u"jə", u"")]
        ipa = u"klɛi̯ntjə"
        self.assertEqual(self.parser.break_syllables(ipa, use_syllables=False), ans)

    def test_extract_syllable(self):
        self.parser.reset_language("Polish")
        ans = (u"l", u"a", u"t͡ɕ")
        ipa = u"ɔbalat͡ɕ"
        num = 2
        self.assertEqual(self.parser.extract_syllable(ipa, num, use_syllables=False), ans)

        self.parser.reset_language("Dutch")
        ans = (u"kl", u"ɛi̯", u"n")
        ipa = u"klɛi̯ntjə"
        num = 0
        self.assertEqual(self.parser.extract_syllable(ipa, num, use_syllables=False), ans)

    def test_add_syllables(self):
        self.parser.reset_language("Polish")
        ans = u"ɔ.ba.lat͡ɕ"
        ipa = u"ɔbalat͡ɕ"
        self.assertEqual(self.ipa_word.add_syllables(ipa), ans)

        self.parser.reset_language("Dutch")
        ans = u"klɛi̯n.tjə"
        ipa = u"klɛi̯ntjə"
        self.assertEqual(self.ipa_word.add_syllables(ipa), ans)

    def test_next_phoneme(self):
        self.parser.reset_language("Polish")
        ans1 = u"ɔ" if self.language == "Polish" else u"k"
        ans2 = u"b" if self.language == "Polish" else u"l"
        ans3 = u"a" if self.language == "Polish" else u"ɛi"
        next_phoneme, next_ipa = self.parser.next_phoneme(self.ipa, use_syllables=False)
        self.assertEqual(next_phoneme, ans1)
        next_phoneme, next_ipa = self.parser.next_phoneme(next_ipa, use_syllables=False)
        self.assertEqual(next_phoneme, ans2)
        self.assertEqual(self.parser.next_phoneme(next_ipa, remove=False, use_syllables=False), ans3)

        self.parser.reset_language("Dutch")
        ans1 = u"k"
        ans2 = u"l"
        ans3 = u"ɛi"
        next_phoneme, next_ipa = self.parser.next_phoneme(self.ipa, use_syllables=False)
        self.assertEqual(next_phoneme, ans1)
        next_phoneme, next_ipa = self.parser.next_phoneme(next_ipa, use_syllables=False)
        self.assertEqual(next_phoneme, ans2)
        self.assertEqual(self.parser.next_phoneme(next_ipa, remove=False, use_syllables=False), ans3)

    def test_next_syllable(self):
        self.parser.reset_language("Polish")
        next_syllable, rest_ipa = self.parser.next_syllable(self.ipa)
        ans1 = u"ɔ"
        ans2 = u"ba"
        ans3 = u"lat͡ɕ"
        self.assertEqual(next_syllable, ans1)
        next_syllable, rest_ipa = self.parser.next_syllable(rest_ipa)
        self.assertEqual(next_syllable, ans2)
        self.assertEqual(self.parser.next_syllable(rest_ipa, remove=False), ans3)

        self.parser.reset_language("Dutch")
        next_syllable, rest_ipa = self.parser.next_syllable(self.ipa)
        ans1 = u"klɛi̯n"
        ans2 = u"tjə"
        ans3 = u""
        self.assertEqual(next_syllable, ans1)
        next_syllable, rest_ipa = self.parser.next_syllable(rest_ipa)
        self.assertEqual(next_syllable, ans2)
        self.assertEqual(self.parser.next_syllable(rest_ipa, remove=False), ans3)

    def test_split_syllables(self):
        self.parser.reset_language("Polish")
        ans = [u"ɔ", u"ba", u"lat͡ɕ"]
        ipa = u"ɔbalat͡ɕ"
        self.assertEqual(self.parser.split_syllables(ipa, use_syllables=False), ans)

        self.parser.reset_language("Dutch")
        ans = [u"klɛi̯n", u"tjə"]
        ipa = u"klɛi̯ntjə"
        self.assertEqual(self.parser.split_syllables(ipa, use_syllables=False), ans)

    def test_find_ipa_vowels(self):
        self.parser.reset_language("Polish")
        ans = u"ɔ", u"balat͡ɕ"
        ipa = u"ɔbalat͡ɕ"
        word = u"obalać"
        ipa_word = IPAWord(word, "Polish", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_vowels(ipa), ans)

        self.parser.reset_language("Dutch")
        ans = u"ɛi", u"̯ntjə"
        ipa = u"klɛi̯ntjə"
        word = u"kleintje"
        ipa_word = IPAWord(word, "Dutch", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_vowels(ipa), ans)

        self.parser.reset_language("Finnish")
        ans = u"ɑː", u"puri"
        word = u"naapuri"
        ipa = u"ˈnɑːpuri"
        ipa_word = IPAWord(word, "Finnish", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_vowels(ipa), ans)

    def test_find_ipa_consonants(self):
        self.parser.reset_language("Polish")
        ans = u"b", u"alat͡ɕ"
        ipa = u"ɔbalat͡ɕ"
        word = u"obalać"
        ipa_word = IPAWord(word, "Polish", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_consonants(ipa), ans)

        self.parser.reset_language("Dutch")
        ans = u"kl", u"ɛi̯ntjə"
        ipa = u"klɛi̯ntjə"
        word = u"kleintje"
        ipa_word = IPAWord(word, "Dutch", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_consonants(ipa), ans)

        self.parser.reset_language("Finnish")
        ans = u"ˈn", u"ɑːpuri"
        word = u"naapuri"
        ipa = u"ˈnɑːpuri"
        ipa_word = IPAWord(word, "Finnish", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_consonants(ipa), ans)
    '''

    def test_shortest_path(self):
        nn1, nn2, nn3, nn4, nn5 = self.blissweb.neural_net.nodes
        self.assertEqual(self.blissweb.shortest_path(nn1, nn2), None)
        self.assertEqual(self.blissweb.shortest_path(nn1, nn5), [nn1, nn3, nn5])

    def test_longest_path(self):
        nn1, nn2, nn3, nn4, nn5 = self.blissweb.neural_net.nodes
        self.assertEqual(self.blissweb.longest_path(nn1, nn4), [nn1, nn2, nn3, nn4])
        self.assertEqual(self.blissweb.longest_path(nn5, nn1), None)

    def test_cycles(self):
        nn1, nn2, nn3, nn4, nn5 = self.blissweb.neural_net.nodes
        nn4.set_outgoing([nn1])
        self.assertEqual(self.blissweb.find_cycle(nn1), [nn1, nn2, nn4, nn1])
        self.assertEqual(self.blissweb.find_cycle(nn5), None)

    def test_visualization(self):
        nn1, nn2, nn3, nn4, nn5, nn6, nn7, nn8, nn9, nn10 = self.blissweb.neural_net.nodes
        neural_img = NeuralNetImage(self.blissweb.neural_net.nodes, blissweb=self.blissweb)
        neural_img.draw_layers()
        neural_img.draw_web()
        self.blissweb.arrow_fan(self.blissweb.node_img(nn1), len(nn1.outgoing)).show()
        alice = excerpts.alice_in_wonderland[:5000]
        title = "Blissymbols in Alice in Wonderland"
        self.blissweb.add_bliss_sentences(alice)
        self.blissweb.chart(title)

    def test_speechart(self):
        alice = excerpts.alice_in_wonderland[:1000]
        title = "Alice in Wonderland"
        self.speechart.add_text(alice)
        self.speechart.chart(title)
        self.speechart.refresh_data()

    def test_tokenize_punct(self):
        self.assertEqual(self.speechart.tokenize_punct("Hello, this is my friend, Molly"),
                         [["Hello"], ["this", "is", "my", "friend"], ["Molly"]])


if __name__ == '__main__':
    unittest.main()


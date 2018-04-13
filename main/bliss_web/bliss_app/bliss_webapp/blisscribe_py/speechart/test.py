# coding: utf-8
"""
TEST:

    Testing suite for WiktionaryParser and derived classes.
"""
from phoneme_parser import *
import unittest


class TestIPAWord(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        unittest.TestCase.setUpClass()
        cls.maxDiff = None
        cls.words = dict()  # word-pronunciation dict in language & IPA
        cls.language = "Finnish"
        cls.parser = PhonemeParser(cls.language)
        cls.parser.common_phonemes(50)

        if cls.language == "Polish":
            cls.word = u"obalać"
            cls.ipa = u"ɔbalat͡ɕ"
            cls.words[cls.word] = cls.ipa
            cls.words[u"jestem"] = u"jɛs̪t̪ɛm"
            cls.ipa_word = IPAWord(cls.word, cls.language, cls.parser)
        elif cls.language == "Dutch":
            cls.word = u"kleintje"
            cls.ipa = u"klɛi̯ntjə"
            cls.words[cls.word] = cls.ipa
            cls.ipa_word = IPAWord(cls.word, cls.language, cls.parser)
        elif cls.language == "Finnish":
            cls.word = u"naapuri"
            cls.ipa = u"ˈnɑːpuri"
            cls.words[cls.word] = cls.ipa
            cls.ipa_word = IPAWord(cls.word, cls.language, cls.parser)

    def test_table(self):
        self.assertEqual(self.parser.word_declension(self.word),
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
        if self.language == "Polish":
            syllable = u"lat͡ɕ"
            ans = (u"l", u"a", u"t͡ɕ")
        else:
            syllable = u"tjə"
            ans = (u"t", u"jə", u"")
        self.assertEqual(self.ipa_word.break_syllable(syllable), ans)

    def test_break_syllables(self):
        if self.language == "Polish":
            ans = [(u"", u"ɔ", u""),
                   (u"b", u"a", u""),
                   (u"l", u"a", u"t͡ɕ")]
        else:
            ans = [(u"kl", u"ɛi", u"̯n"),
                   (u"t", u"jə", u"")]
        self.assertEqual(self.ipa_word.break_syllables(self.ipa, use_syllables=False), ans)

    def test_extract_syllable(self):
        if self.language == "Polish":
            num = 2
            ans = (u"l", u"a", u"t͡ɕ")
        else:
            num = 0
            ans = (u"kl", u"ɛi̯", u"n")
        self.assertEqual(self.ipa_word.extract_syllable(self.ipa, num, use_syllables=False), ans)

    def test_add_syllables(self):
        if self.language == "Polish":
            ans = u"ɔ.ba.lat͡ɕ"
        else:
            ans = u"klɛi̯n.tjə"
        self.assertEqual(self.ipa_word.add_syllables(self.ipa), ans)

    def test_next_phoneme(self):
        ans1 = u"ɔ" if self.language == "Polish" else u"k"
        ans2 = u"b" if self.language == "Polish" else u"l"
        ans3 = u"a" if self.language == "Polish" else u"ɛi"
        next_phoneme, next_ipa = self.ipa_word.next_phoneme(self.ipa, use_syllables=False)
        self.assertEqual(next_phoneme, ans1)
        next_phoneme, next_ipa = self.ipa_word.next_phoneme(next_ipa, use_syllables=False)
        self.assertEqual(next_phoneme, ans2)
        self.assertEqual(self.ipa_word.next_phoneme(next_ipa, remove=False, use_syllables=False), ans3)

    def test_next_syllable(self):
        next_syllable, rest_ipa = self.ipa_word.next_syllable(self.ipa)
        ans1 = u"ɔ" if self.language == "Polish" else u"klɛi̯n"
        ans2 = u"ba" if self.language == "Polish" else u"tjə"
        ans3 = u"lat͡ɕ" if self.language == "Polish" else u""
        self.assertEqual(next_syllable, ans1)
        next_syllable, rest_ipa = self.ipa_word.next_syllable(rest_ipa)
        self.assertEqual(next_syllable, ans2)
        self.assertEqual(self.ipa_word.next_syllable(rest_ipa, remove=False), ans3)

    def test_split_syllables(self):
        ans = [u"ɔ", u"ba", u"lat͡ɕ"] if self.language == "Polish" else [u"klɛi̯n", u"tjə"]
        self.assertEqual(self.ipa_word.split_syllables(self.ipa, use_syllables=False), ans)

    def test_find_ipa_vowels(self):
        ans = (u"ɔ", u"balat͡ɕ") if self.language == "Polish" else (u"ɛi", u"̯ntjə")
        self.assertEqual(self.ipa_word.find_ipa_vowels(self.ipa), ans)

    def test_find_ipa_consonants(self):
        ans = (u"b", u"alat͡ɕ") if self.language == "Polish" else (u"kl", u"ɛi̯ntjə")
        self.assertEqual(self.ipa_word.find_ipa_consonants(self.ipa), ans)


if __name__ == '__main__':
    unittest.main()


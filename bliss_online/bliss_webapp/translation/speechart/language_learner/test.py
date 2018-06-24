# coding: utf-8
"""
TEST:

    Testing suite for WiktionaryParser and derived classes.
"""
import unittest
import main.bliss_web.bliss_app.bliss_webapp.blisscribe_py.excerpts as excerpts
import language_learner
import sys

PATH = '/Users/courtney/Documents/creation/programming/blisscribe/blisscribe'
sys.path.extend([PATH, PATH + '/main/bliss_web/bliss_app/bliss_webapp/blisscribe_py/speechart/language_learner'])

ALICE_EN = excerpts.alice_in_wonderland
ALICE_PL = excerpts.alice_in_wonderland_polish
ALICE_FR = excerpts.alice_in_wonderland_french
ALICE_SP = excerpts.alice_in_wonderland_spanish
LANG_LEARNER = language_learner.LanguageLearner()


class TestSpeechart(unittest.TestCase):
    def test_translate(self):
        self.maxDiff = None
        en_sent_short = "The cat is on the mat"
        fr_sent_short = "Le chat est sur le tapis"
        en_fr_dict = {u"Alice": [u"Alice"], u"was": [], u"beginning": [u"commençait"], u"to": [u"à"],
                      u"get": [u"sentir"], u"very": [u"très"], u"tired": [u"lasse"], u"of": [u"de"],
                      u"sitting": [u"assise"], u"by": [u"à côté de"], u"her": [u"sa"], u"sister": [u"sœur"],
                      u"on": [u"sur"], u"the": [u"le"], u"bank": [u"talus"], u"and": [u"et"],
                      u"having": [u"avoir"], u"nothing": [u"rien"], u"do": [u"faire"],
                      u"having nothing to do": [u"n'avoir rien à faire"], u"once": [u"une fois"],
                      u"or": [u"ou", u"ni"], u"twice": [u"deux"], u"she": [u"elle"], u"had": [u"avait"],
                      u"peeped into": [u"jeté un coup d’œil"], u"book": [u"livre"], u"reading": [u"lisait"],
                      u"but": [u"mais"], u"it": [u"il"], u"no": [u"ne", u"ni"], u"pictures": [u"images"],
                      u"conversations": [u"dialogues"], u"in": [u"contenait"],
                      u"what": [u"quoi"], u"is": [u"peut"], u"use": [u"servir"], u"a": [u"un"],
                      u"thought": [u"pensait"], u"without": [u"n'y"], u"conversation": [u"dialogues"]}

        en_pl_dict = {u"Alice": [u"Alicja"], u"was": [], u"beginning": [u"już"],
                      u"get": [u"miała"], u"very tired": [u"dość"],
                      u"of sitting": [u"siedzenia"], u"by": [u"obok"], u"sister": [u"siostra", u"siostry"],
                      u"on": [u"na"], u"the bank": [u"ławce"], u"and": [u"i", u"a"],
                      u"of having nothing to do": [u"próżnowania"], u"once": [u"raz"],
                      u"or": [u"ani", u"czy"], u"twice": [u"dwa razy"], u"she had peeped": [u"zerknęła"],
                      u"into": [u"do"], u"book": [u"książki", u"książce", u"książka"],
                      u"reading": [u"czytała"], u"but": [u"niestety"], u"it": [], u"no": [u"nie"],
                      u"pictures": [u"obrazków"], u"conversations": [u"rozmów"], u"in": [u"w"],
                      u"what": [u"cóż"], u"is": [u"jest"], u"use": [u"warta"], u"a": [],
                      u"thought": [u"pomyślała"], u"without": [u"nie ma"], u"conversation": [u"rozmów"]}
        # [Alice | Alicja] [was feeling | miała] [now | już] [enough | dość] [sitting | siedzenia]
        # [on | na] [bench | ławce] [next to | obok] [her sister | siostry]

        # ENGLISH
        alice_en = u"Alice was beginning to get very tired of sitting by her sister on the bank, " \
        u"and of having nothing to do: once or twice she had peeped into the book her " \
        u"sister was reading, but it had no pictures or conversations in it, 'and what " \
        u"is the use of a book,' thought Alice 'without pictures or conversation?'"

        # POLISH
        # Alice was feeling now enough of sitting on bench by sister and of idleness.
        # Once or two times she looked into book, which read [by] sister.
        # Unfortunately, in book was no pictures or conversations.
        # "And what is worth [of] book - thought Alice - in which not has conversations or pictures?"

        alice_pl = u"Alicja miała już dość siedzenia na ławce obok siostry i próżnowania. " \
        u"Raz czy dwa razy zerknęła do książki, którą czytała " \
        u"siostra. Niestety, w książce nie było obrazków ani rozmów. „A cóż " \
        u"jest warta książka - pomyślała Alicja - w której nie ma rozmów ani obrazków?”"
        # FRENCH
        alice_fr = u"Alice commençait à se sentir très lasse de rester assise à côté de sa sœur sur le talus, " \
        u"et de n’avoir rien à faire : une fois ou deux, elle avait jeté un coup d’œil sur le livre que lisait sa " \
        u"sœur; mais il ne contenait ni images ni dialogues: « Et, " \
        u"pensait Alice, à quoi peut bien servir un livre où il n’y a ni images ni dialogues ? »"

        self.assertEqual(LANG_LEARNER.words_translations(alice_en.split(u",")[0],
                                                         alice_fr.split(u",")[0]),
                         en_fr_dict)
        self.assertEqual(LANG_LEARNER.triangulate_translation("cat", "The cat is on the mat", "Le chat est sur le tapis",
                                                              {"is": ["est"], "the": ["le"]}),
                         [u"chat"])

        self.assertEqual(LANG_LEARNER.triangulate_translation(u"sitting",
                                                              u"Alice was beginning to get very tired of " +
                                                              u"sitting by her sister on the bank, and of " +
                                                              u"having nothing to do",
                                                              u"Alicja miała już dość siedzenia na " +
                                                              u"ławce obok siostry i próżnowania.",
                                                              {u"get": [u"miała"], u"on": [u"na"]}),
                         [u"już", u"dość", u"siedzenia"])
        # self.assertEqual(LANG_LEARNER.words_translations("The cat is on the mat", "Le chat est sur le tapis"),
        #                  {"the": ["le"], "cat": ["chat"], "is": ["est"], "on": ["sur"], "mat": ["tapis"]})
        alice_en_words = LANG_LEARNER.tokenize_words(ALICE_EN)
        alice_fr_words = LANG_LEARNER.tokenize_words(ALICE_FR)
        self.assertEqual(LANG_LEARNER.words_translations(alice_en_words[:int(len(alice_en_words) / 100.0)],
                                                         alice_fr_words[:int(len(alice_fr_words) / 100.0)]),
                         en_fr_dict)
        self.assertEqual(LANG_LEARNER.words_translations(alice_en, alice_fr),
                         en_fr_dict)
        #self.assertEqual(LANG_LEARNER.words_translations(alice_en, alice_pl),
        #                 en_pl_dict)
        '''
        self.assertEqual(LANG_LEARNER.word_difference("the", "the", en_sent_short, en_sent_short), 0)
        self.assertEqual(LANG_LEARNER.word_difference("the", "le", en_sent_short, fr_sent_short), 0)
        self.assertEqual(LANG_LEARNER.word_difference("cat", "chat", en_sent_short, fr_sent_short), 0)
        self.assertEqual(LANG_LEARNER.word_difference("mat", "tapis", en_sent_short, fr_sent_short), 0)
        self.assertEqual(LANG_LEARNER.word_difference("the", "tapis", en_sent_short, fr_sent_short), 677)

        self.assertEqual(LANG_LEARNER.word_translation("the", en_sent_short, fr_sent_short), "le")
        self.assertEqual(LANG_LEARNER.word_translation("cat", en_sent_short, fr_sent_short), "chat")
        self.assertEqual(LANG_LEARNER.word_translation("Alice", alice_en, alice_fr), "Alice")
        self.assertEqual(LANG_LEARNER.word_translation("sister", alice_en, alice_fr), "sœur")
        self.assertEqual(LANG_LEARNER.word_translation("book", alice_en, alice_fr), "livre")

        #self.assertEqual(LANG_LEARNER.word_difference("Alice", "Alice", ALICE_EN, ALICE_FR), 0)
        #self.assertEqual(LANG_LEARNER.word_difference("Alice", "Alicj", ALICE_EN, ALICE_PL, contains2=True), 0)
        #self.assertEqual(LANG_LEARNER.word_difference("Alice", "Alicia", ALICE_EN, ALICE_SP), 0)
        '''
        '''
        self.maxDiff = None

        self.assertEqual(LANG_LEARNER.translation_dict(en_sent_short),
                         {u"The": dict(), u"cat": dict(), u"is": dict(), u"on": dict(),
                          u"the": dict(), u"mat": dict()})
        self.assertEqual(LANG_LEARNER.crossmatch([en_sent_short, fr_sent_short], [u"English", u"French"]),
                         {u"English": {u"the": {u"fr": [u"le"]}, u"cat": {u"fr": [u"chat"]},
                                       u"is": {u"fr": [u"est"]}, u"on":  {u"fr": [u"sur"]},
                                       u"mat": {u"fr": [u"tapis"]}, u"The": {u"fr": [u"Le"]}},
                          u"French": {u"le": {u"en": [u"the"]}, u"chat": {u"en": [u"cat"]},
                                      u"est": {u"en": [u"is"]}, u"sur": {u"en": [u"on"]},
                                      u"tapis": {u"en": [u"mat"]}, u"Le": {u"en": [u"The"]}}})

        en_sent_long = ALICE_EN.split("?")[0]
        pl_sent_long = ALICE_PL.split("?")[0]
        fr_sent_long = ALICE_FR.split("?")[0]
        sp_sent_long = ALICE_SP.split("?")[0]

        en_sent = u"Alice was beginning to get" # very tired of sitting by her sister on the bank"

        pl_sent = u"Alicja miała już dość siedzenia na ławce obok siostry"
        # -> Alice was feeling now enough sitting on bench next to her sister.
        # [Alice | Alicja] [was feeling | miała] [now | już] [enough | dość] [sitting | siedzenia]
        # [on | na] [bench | ławce] [next to | obok] [her sister | siostry]
        u"Alice commençait à se sentir très lasse de rester assise à côté de sa sœur, sur le talus"
        # -> Alice was beginning to feel very tired of resting seated next to her sister, on the bank
        u"Alicia empezaba a estar harta de seguir tanto rato sentada en la orilla, junto a su hermana"
        # -> Alice was beginning to be tired to go on a while sitting on the bank, next to her sister

        # ENGLISH
        u"Alice was beginning to get very tired of sitting by her sister on the bank, " \
        u"and of having nothing to do: once or twice she had peeped into the book her " \
        u"sister was reading, but it had no pictures or conversations in it, 'and what " \
        u"is the use of a book,' thought Alice 'without pictures or conversation?'"

        # POLISH
        u"Alicja miała już dość siedzenia na ławce obok siostry i próżnowania. " \
        u"Raz czy dwa razy zerknęła do książki, którą czytała " \
        u"siostra. Niestety, w książce nie było obrazków ani rozmów. „A cóż " \
        u"jest warta książka - pomyślała Alicja - w której nie ma rozmów ani obrazków?”"

        # FRENCH
        u"Alice commençait à se sentir très lasse de rester assise à côté de sa sœur, sur le talus, " \
        u"et de n’avoir rien à faire : une fois ou deux, elle avait jeté un coup d’œil sur le livre que lisait sa " \
        u"sœur; mais il ne contenait ni images ni dialogues: «Et, " \
        u"pensait Alice, à quoi peut bien servir un livre où il n’y a ni images ni dialogues ? »"

        # SPANISH
        u"Alicia empezaba a estar harta de seguir tanto rato sentada en la orilla, junto a su hermana, " \
        u"sin hacer nada, una o dos veces se había asomado al libro que su " \
        u"hermana estaba leyendo, pero no tenía ilustraciones ni diálogos, “¿y " \
        u"de qué sirve un libro —pensó Alicia— si no tiene ilustraciones ni diálogos?”"

        #self.assertEqual(LANG_LEARNER.crossteach(texts=[en_sent, pl_sent], langs=["English", "Polish"]),
        #                 {"Alice": ["Alicja"], "was": ["miała"], "sitting": ["siedzenia"],
        #                  "by": ["na"], "to": ["do"], "once": ["raz"], "book": ["książki"]})

        self.assertEqual(LANG_LEARNER.translation_dict(u"Alice was beginning to get very tired"),
                         {u"Alice": dict(), u"was": dict(), u"beginning": dict(), u"to": dict(), u"get": dict(),
                          u"very": dict(), u"tired": dict()})
        self.assertEqual(LANG_LEARNER.crossmatch([en_sent, pl_sent], [u"English", u"Polish"]),
                         {u"English": {u"Alice": {u"pl": [u"Alicja"]}, u"to get": {u"pl": [u"miała"]},
                                       u"was beginning": {u"pl": [u"już"]}},
                          u"Polish": {u"Alicja": {u"en": [u"Alice"]}, u"miała": {u"en": [u"to get"]},
                                      u"już": {u"en": [u"was beginning"]}}})

        print LANG_LEARNER.crossmatch([en_sent_long, pl_sent_long],
                                      ["English", "Polish"])
        print LANG_LEARNER.crossmatch([en_sent_long, pl_sent_long, fr_sent_long, sp_sent_long],
                                      ["English", "Polish", "French", "Spanish"])
                                      '''


if __name__ == '__main__':
    unittest.main()


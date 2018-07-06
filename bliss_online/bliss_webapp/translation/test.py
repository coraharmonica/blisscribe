from blisscribe import *
import unittest

ALICE = """
CHAPTER I
Down the Rabbit-Hole
 
    Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'
"""

ALICE_PL = """
ROZDZIAŁ I
PRZEZ KRÓLICZĄ NORĘ

	Alicja miała już dość siedzenia na ławce obok siostry i próżnowania. Raz czy dwa razy zerknęła do książki, którą czytała siostra. Niestety, w książce nie było obrazków ani rozmów. „A cóż jest warta książka - pomyślała Alicja - w której nie ma rozmów ani obrazków?”
"""

ALICE_2 = """
        So she was considering in her own mind (as well as she could, 
    for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain 
    would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit 
    with pink eyes ran close by her. There was nothing so VERY remarkable in that; nor did Alice 
    think it so VERY much out of the way to hear the Rabbit say to itself, 'Oh dear! Oh dear! 
    I shall be late!' (when she thought it over afterwards, it occurred to her that she ought to 
    have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually 
    TOOK A WATCH OUT OF ITS WAISTCOAT-POCKET, and looked at it, and then hurried on, Alice started to 
    her feet, for it flashed across her mind that she had never before seen a rabbit with either a 
    waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the 
    field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the 
    hedge. In another moment down went Alice after it, never once considering how in the world she was 
    to get out again. The rabbit-hole went straight on like a tunnel for some way, and then dipped 
    suddenly down, so suddenly that Alice had not a moment to think about stopping herself before 
    she found herself falling down a very deep well. Either the well was very deep, or she fell 
    very slowly, for she had plenty of time as she went down to look about her and to wonder what 
    was going to happen next. First, she tried to look down and make out what she was coming to, 
    but it was too dark to see anything; then she looked at the sides of the well, and noticed that 
    they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung 
    upon pegs. She took down a jar from one of the shelves as she passed; it was labelled 'ORANGE MARMALADE', 
    but to her great disappointment it was empty: she did not like to drop the jar for fear of killing 
    somebody, so managed to put it into one of the cupboards as she fell past it. 'Well!' thought Alice to 
    herself, 'after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll 
    all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' 
    (Which was very likely true.) Down, down, down. Would the fall NEVER come to an end! 
    'I wonder how many miles I've fallen by this time?' she said aloud. 'I must be getting somewhere 
    near the centre of the earth. Let me see: that would be four thousand miles down, I think--' 
    (for, you see, Alice had learnt several things of this sort in her lessons in the schoolroom, a
"""

class TestBlisscribe(unittest.TestCase):
    BLISS_TRANSLATOR = BlissTranslator("Polish")
    BLISS_TRANSLATOR.lex_parser.fresh_bliss_derivations()

    '''
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
    '''

    def test_translation(self):
        #self.maxDiff = None
        bt, tw = self.BLISS_TRANSLATOR, TranslationWord
        '''
        blisscribe_transwords = bt.translate_to_transwords(ALICE)
        desired_transwords = [tw("CHAPTER", "NN", bt, "English"),
                              tw("I", "CD", bt, "English"),
                              tw("Down", "VB", bt, "English"),
                              tw("the", "DT", bt, "English"),
                              tw("Rabbit", "NN", bt, "English"),
                              tw("Hole", "NN", bt, "English"),
                              tw("Alice", "NNP", bt, "English"),
                              tw("was", "VBD", bt, "English"),
                              tw("beginning", "VBG", bt, "English"),
                              tw("to", "TO", bt, "English"),
                              tw("feel", "VB", bt, "English"),
                              tw("very", "JJ", bt, "English"),
                              tw("tired", "JJ", bt, "English"),
                              tw("of", "IN", bt, "English"),
                              tw("sitting", "VBG", bt, "English"),
                              tw("by", "IN", bt, "English"),
                              tw("her", "PRP$", bt, "English"),
                              tw("sister", "NN", bt, "English"),
                              tw("on", "IN", bt, "English"),
                              tw("the", "DT", bt, "English"),
                              tw("bank", "NN", bt, "English"),
                              tw("and", "CC", bt, "English"),
                              tw("of", "IN", bt, "English"),
                              tw("having", "VBG", bt, "English"),
                              tw("nothing", "NN", bt, "English"),
                              tw("to", "TO", bt, "English"),
                              tw("do", "VB", bt, "English"),
                              tw("once", "RB", bt, "English"),
                              tw("or", "CC", bt, "English"),
                              tw("twice", "RB", bt, "English"),
                              tw("she", "PRP", bt, "English"),
                              tw("had", "VBD", bt, "English"),
                              tw("peeped", "VBD", bt, "English"),
                              tw("into", "IN", bt, "English"),
                              tw("the", "DT", bt, "English"),
                              tw("book", "NN", bt, "English"),
                              tw("her", "PRP$", bt, "English"),
                              tw("sister", "NN", bt, "English"),
                              tw("was", "VBD", bt, "English"),
                              tw("reading", "VBG", bt, "English"),
                              tw("but", "CC", bt, "English"),
                              tw("it", "NN", bt, "English"),
                              tw("had", "VBD", bt, "English"),
                              tw("no", "DT", bt, "English"),
                              tw("pictures", "NNS", bt, "English"),
                              tw("or", "CC", bt, "English"),
                              tw("conversations", "NNS", bt, "English"),
                              tw("in", "IN", bt, "English"),
                              tw("it", "NN", bt, "English"),
                              tw("and", "CC", bt, "English"),
                              tw("what", "WDT", bt, "English"),
                              tw("is", "VB", bt, "English"),
                              tw("the", "DT", bt, "English"),
                              tw("use", "VB", bt, "English"),
                              tw("of", "IN", bt, "English"),
                              tw("a", "DT", bt, "English"),
                              tw("book", "NN", bt, "English"),
                              tw("thought", "VB", bt, "English"),
                              tw("Alice", "NNP", bt, "English"),
                              tw("without", "DT", bt, "English"),
                              tw("pictures", "NNS", bt, "English"),
                              tw("or", "CC", bt, "English"),
                              tw("conversation", "NN", bt, "English")]
        self.assertEqual(blisscribe_transwords, desired_transwords)
        '''

        blisscribe_transwords_pl = bt.translate_to_transwords(ALICE_PL)
        desired_transwords_pl = [tw("ROZDZIAŁ", "NN", bt, "Polish"),
                                 tw("I", "CD", bt, "Polish"),
                                 tw("PRZEZ", "IN", bt, "Polish"),
                                 tw("KRÓLICZĄ", "NN", bt, "Polish"),
                                 tw("NORĘ", "NN", bt, "Polish"),
                                 tw("Alicja", "NNP", bt, "Polish"),
                                 tw("miała", "VBD", bt, "Polish"),
                                 tw("już", "RB", bt, "Polish"),
                                 tw("dość", "VB", bt, "Polish"),
                                 tw("siedzenia", "VB", bt, "Polish"),
                                 tw("na", "IN", bt, "Polish"),
                                 tw("ławce", "NN", bt, "Polish"),
                                 tw("obok", "IN", bt, "Polish"),
                                 tw("siostry", "NN", bt, "Polish"),
                                 tw("i", "CC", bt, "Polish"),
                                 tw("próżnowania", "VB", bt, "Polish"),
                                 tw("Raz", "CD", bt, "Polish"),
                                 tw("czy", "CC", bt, "Polish"),
                                 tw("dwa", "CD", bt, "Polish"),
                                 tw("razy", "NNS", bt, "Polish"),
                                 tw("zerknęła", "VBD", bt, "Polish"),
                                 tw("do", "IN", bt, "Polish"),
                                 tw("książki", "NN", bt, "Polish"),
                                 tw("którą", "WP", bt, "Polish"),
                                 tw("czytała", "VB", bt, "Polish"),
                                 tw("siostra", "NN", bt, "Polish"),
                                 tw("Niestety", "RB", bt, "Polish"),
                                 tw("w", "IN", bt, "Polish"),
                                 tw("książce", "NN", bt, "Polish"),
                                 tw("nie", "DT", bt, "Polish"),
                                 tw("było", "VB", bt, "Polish"),
                                 tw("obrazków", "NNS", bt, "Polish"),
                                 tw("ani", "CC", bt, "Polish"),
                                 tw("rozmów", "NNS", bt, "Polish"),
                                 tw("A", "CC", bt, "Polish"),
                                 tw("cóż", "WP", bt, "Polish"),
                                 tw("jest", "VB", bt, "Polish"),
                                 tw("warta", "NN", bt, "Polish"),
                                 tw("książka", "NN", bt, "Polish"),
                                 tw("pomyślała", "VBD", bt, "Polish"),
                                 tw("Alicja", "NNP", bt, "Polish"),
                                 tw("w", "IN", bt, "Polish"),
                                 tw("której", "WP", bt, "Polish"),
                                 tw("nie", "DT", bt, "Polish"),
                                 tw("ma", "VB", bt, "Polish"),
                                 tw("rozmów", "NNS", bt, "Polish"),
                                 tw("ani", "CC", bt, "Polish"),
                                 tw("obrazków", "NNS", bt, "Polish")
                                 ]
        self.assertEqual(blisscribe_transwords_pl, desired_transwords_pl)

    BLISS_TRANSLATOR.refresh_bliss_dicts()


if __name__ == '__main__':
    unittest.main()


# coding: utf-8
"""
CONCEPT_ANALYZER:

    Used for representing and drawing concept cloud images
    using a text's most prominent Blissymbols.
"""
from string import zfill
from numpy import log
from bliss_images import *
from excerpts import books as novels


class ConceptAnalyzer:

    def __init__(self, translator):
        self.translator = translator

    def rescale(self, values, new_min=0, new_max=100):
        """
        Rescales the data in values according to new_min
        and new_max.

        :param values: List[int/float], values to rescale
        :param new_min: int/float, new min to scale data to
        :param new_max: int/float, new max to scale data to
        :return: List[int/float], values rescaled
        """
        scaled_values = []
        old_min, old_max = min(values), max(values)

        for val in values:
            new_val = float(new_max - new_min) / (old_max - old_min) * (val - old_min) + new_min
            scaled_values.append(new_val)

        return scaled_values

    def draw_concept_cloud(self, text, title=u"concept cloud", cap=None):
        """
        Draws a concept cloud image for text in this ConceptAnalyzer's language
        and saves it under this title.
        ~
        By default cap is set to None, so this function draws all concepts
        in this text until their frequency drops below the 10th percentile.
        Users can opt to set cap to a custom maximum number of concepts to draw.
        ~
        Returns None.

        :param text: str, text to draw concept cloud for
        :param language: str, native language of text
        :param title: str, title to save image as
        :param cap: bool, option to cap number of concepts drawn
        :return: None
        """
        if len(text) == 0:
            return

        bliss_dict = self.translator.get_eng_bliss_dict()
        width, height = 800, 600
        bg = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        trans_words = self.translator.translate_to_transwords(text)
        freqs = self.translator.analyze_trans_word_concepts(trans_words)
        concept_freqs = sorted(freqs, key=lambda k: freqs[k], reverse=True)[:cap]
        highest_freq = freqs[concept_freqs[0]]

        x, y = 0, 0     # coords of latest Blissymbol
        space = 5       # space b/t Blissymbols in img
        highest_height = None
        # scale each frequency to be log(freq) out of 100:
        calc_img_w = lambda x: ((100.0)/log(highest_freq)) * (log(x) - log(highest_freq)) + 125.0

        for i in range(0, len(concept_freqs)):
            concept = concept_freqs[i]
            freq = freqs[concept]

            if concept.isdigit():
                # skip visualizing numbers
                continue
            else:
                img_w = calc_img_w(freq)
                if img_w < 1:
                    break

            try:
                bliss_dict[concept]
            except KeyError:
                if concept[:9] == "indicator":
                    blissymbols = bliss_dict["indicator"]
                else:
                    concepts = concept.split(",")
                    if len(concepts) > 1:
                        for c in concepts:
                            try:
                                bliss_dict[c]
                            except KeyError:
                                continue
                            else:
                                if c.isdigit():
                                    continue
                                else:
                                    blissymbols = bliss_dict[c]
                                    break
                        else:
                            continue
                    else:
                        continue
            else:
                blissymbols = bliss_dict[concept]

            if len(blissymbols) == 0:
                continue
            elif len(blissymbols) == 1:
                blissymbol = blissymbols.pop()
                blissymbols.add(blissymbol)
            else:
                for blissymbol in blissymbols:
                    name = blissymbol.get_bliss_name()
                    if concept == name:
                        break
                    elif concept in name.split(","):
                        break
                else:
                    blissymbol = blissymbols.pop()
                    blissymbols.add(blissymbol)

            img_filename = blissymbol.get_bliss_name()
            img = self.translator.get_bliss_img(img_filename, int(img_w), int(img_w))
            x_add = img.size[0] + space

            if highest_height is None:
                highest_height = img.size[1]

            if x + x_add > bg.size[0]:
                x = 0
                y += highest_height
                highest_height = None

            bg.paste(img, (x, y))
            x += x_add

        bg.save("out/" + title + ".png")
        bg.show()

        self.write_concept_cloud(freqs, title)

    def write_concept_cloud(self, bliss_freqs, title=u"concept cloud"):
        """
        Writes each concept in bliss_freqs in decreasing order
        of frequency to a file saved under this title.
        ~
        Returns None.

        :param bliss_freqs: dict, where...
                key (str) - name of Blissymbol concept
                val (int) - number of occurrences in translation
        :param title: str, title to save image as
        :return: None
        """
        sorted_freqs = sorted(bliss_freqs, key=lambda k: bliss_freqs[k], reverse=True)
        digs = len(str(bliss_freqs[sorted_freqs[0]]))

        with open("out/" + title.replace(" ", "_") + "_concepts.txt", "w") as out:
            for concept in sorted_freqs:
                freq = bliss_freqs[concept]
                out.write(zfill(freq, digs) + "\t" + concept + "\n")

    def fetch_all_contexts(self, word, cap=10):
        """
        Fetches a list of all sentences from NLTK's
        Project Gutenberg and translate_other sources using this
        word.
        ~
        This method halts when it has found cap sentences.
        By default, cap is set to 100.

        :param word: str, word to fetch contexts for
        :param cap: int, max number of sentences to fetch
        :return: List[List[str]], list of sentences using given word
        """
        contexts = []
        print
        idx = 0

        for title in novels:
            if idx > cap:
                break

            novel = novels[title]
            print novel
            phrases = novel.split(".")

            for c in range(len(phrases)):
                phrase = phrases[c]
                words = phrase.split(" ")

                for i in range(len(words)):
                    w = words[i].lower()
                    if w == word:
                        contexts.append(phrase)
                        print phrase
            idx += 1

        return contexts

    def draw_word_concepts(self, word):
        """
        Draws a concept cloud image for this word.
        ~
        Returns None.

        :param word: str, word to draw concept cloud for
        :return: None
        """
        contexts = self.fetch_all_contexts(word, cap=500)
        text = "\n".join(contexts)
        print text
        self.draw_concept_cloud(text, word)


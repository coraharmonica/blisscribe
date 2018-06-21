"""
WIKT CHART:

    Used for graphing Wiktionary data on words.
"""
from speecharts import Speechart


class WiktChart(Speechart):
    def __init__(self, language):
        Speechart.__init__(self, language)

    def word_sentences(self, word):
        entry = self.find_wiktionary_entry(word, self.language)

    def speak(self, length=2):
        """
        Returns a phrase from this WiktChart of this length.

        :param length: int, length of desired phrase
        :return: List[str], words in phrase
        """
        pass

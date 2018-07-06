"""
WIKT CHART:

    Used for graphing Wiktionary data on words.
"""
from speechart.speecharts import Speechart


class WiktChart(Speechart):
    def __init__(self, language):
        Speechart.__init__(self, language)

    def word_sentences(self, word, incl_samples=True):
        """
        Returns a list of sentences containing this word
        fetched from Wiktionary and WordNet.
        ~
        If incl_samples is True, also includes files from
        sample texts folder.

        :param word: str, word to return sentences for
        :param incl_samples: bool, includes files from sample texts if True
        :return:
        """
        entry = self.find_wiktionary_entry(word, self.language)
        return

    def speak(self, length=2):
        """
        Returns a phrase from this WiktChart of this length.

        :param length: int, length of desired phrase
        :return: List[str], words in phrase
        """
        pass

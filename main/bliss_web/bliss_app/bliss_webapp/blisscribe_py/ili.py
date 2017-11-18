# -*- coding: utf-8 -*-
"""
ILI:

    Contains classes for representing ILI dictionaries
    and their entries.

    Purpose TBD.  Hoping to incorporate Blissymbols into
    conceptual dictionary after creating Blissymbols
    wordnet.
"""

class ILIDict:
    """
    A class representing a set of word entries in the
    Interlingual Language Index (ILI).
    ~
    In ILI, each entry is a unique cross-lingual
    concept with an English definition.
    """
    LANGUAGE = "English"

    def __init__(self, bliss_dict):
        self.bliss_dict = bliss_dict
        self.entries = set([])

    def makeEntry(self, idx, address, pwn_words):
        """
        Adds a new ILIEntry with the given index, address,
        and PWN word definitions to self.ENTRIES.
        ~
        Returns the new ILIEntry.

        :param idx: int, index of synset definition from 0 to 117,659
        :param address: str, PWN address of form [0-9]{8}-[a|n|r|s|v]
        :param pwn_words: List[str], English PWN words for ILI concept
        :return: ILIEntry
        """
        entry = ILIEntry(idx, address, pwn_words, self.bliss_dict)
        self.entries.add(entry)
        return entry


class ILIEntry:
    """
    A class to represent a word entry in the
    Interlingual Language Index (ILI).
    ~
    In ILI, each entry is a unique cross-lingual
    concept with an English definition.
    """
    PARTS_OF_SPEECH = {"a": "ADJ", "n": "NOUN", "r": "ADV", "s": "ADJ_SAT", "v": "VERB"}

    def __init__(self, idx, address, pwn_words, bliss_dict):
        """
        Represents a word entry in ILI.
        ~
        Each ILIEntry has an index tying it to Princeton WordNet 3.0 (PWN),
        a PWN address, and a corresponding PWN English word.

        :param idx: int, index of synset definition from 0 to 117,659
        :param address: str, PWN address of form [0-9]{8}-[a|n|r|s|v]
        :param pwn_words: List[str], English PWN words for ILI concept
        :param bliss_dict: dict,
        :type bliss_words: List[Blissymbol]
        """
        self.idx = idx
        self.address = address
        self.pos = self.address[-1]
        self.pwn_words = pwn_words
        self.bliss_words = []
        self.setBlissWords(bliss_dict)

    def setBlissWords(self, bliss_dict):
        """
        Sets this ILIEntry's self.bliss_defns to the
        Blissymbol value(s) in ILIEntry's BLISS_DICT.
        ~
        Loops through ILIEntry's self.words

        :type bliss_words: List[Blissymbol]
        :return: None
        """
        bliss_words = set([])
        for word in self.pwn_words:
            try:
                bliss_dict[word]
            except KeyError:
                continue
            else:
                translations = bliss_dict[word]
                translation = translations[-1]
                bliss_words.add(translation)
        self.bliss_words.extend(bliss_words)

    def getBlissDefns(self):
        return self.bliss_words

    def __str__(self):
        return "entry "+ self.getIdxStr() + ":\n" + \
               "\t" + "address \t" + self.getAddressStr() + "\n" + \
               "\t" + "pos \t\t" + self.getPosStr() + "\n" + \
               "\t" + "word(s) \t" + self.getWordsStr() + "\n" + \
               "\t" + "blissymbol \t" + self.getBlissWordsStr() + "\n"

    __repr__ = __str__

    def getIdxStr(self):
        return str(self.idx)

    def getAddressStr(self):
        return str(self.address)

    def getWordsStr(self):
        defns = []
        for word in self.pwn_words:
            defns.append(str(word.replace("_", " ")))
        return ", ".join(defns)

    def getPosStr(self):
        return str(self.PARTS_OF_SPEECH[self.pos])

    def getBlissWordsStr(self):
        defns = []

        for word in self.bliss_words:
            bliss_word = str(word)
            bliss_name = bliss_word.replace("_", " ")
            bliss_name = bliss_name.replace(",", "/")
            defns.append(bliss_name)

        if len(defns) == 0:
            return "N/A"
        else:
            return ", ".join(defns)
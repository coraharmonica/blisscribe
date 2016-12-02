# dummy text
DFW = "I am seated in an office, surrounded by heads and bodies. My posture is consciously congruent \
to the shape of my hard chair. This is a cold room in University Administration, wood-walled, Remington-hung, \
double-windowed against the November heat, insulated from Administrative sounds by the reception area outside, \
at which Uncle Charles, Mr. deLint and I were lately received.\
\nI am in here. \
Three faces have resolved into place above summer-weight sportcoats and half-Windsors across a polished pine \
conference table shiny with the spidered light of an Arizona noon. These are three Deans - of Admissions, \
Academic Affairs, Athletic Affairs. I do not know which face belongs to whom."

# dummy English-to-X dict
foreignDict = {"the": "le", "is": "est", "a": "un", "an": "une", "i": "je", "my": "mon"}

# dummy list of X most common words in origin language
mostCommonWords = []

# English dictionaries:
#    incomplete -> http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt
#    plaintext -> http://www.mso.anu.edu.au/~ralph/OPTED/
#    check out WordNet Python module

# more info on language dictionaries:
#   http://stackoverflow.com/questions/21395011/python-module-with-access-to-english-dictionaries-including-definitions-of-words


def wordFreq(phrase):
    """
    Takes in a non-empty string of words,
    returns a word frequency dictionary.
    """
    words = (phrase.lower()).split()
    freqs = {}

    for word in words:
        #removes punctuation marks @ end of valid words
        if not word.isalnum():
            if not word[-1].isalnum() and word[0].isalnum():
                word = word[:-1]
        #change/init freq value
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1

    return freqs


def sortByUsage(freqs):
    """
    Takes in a dict of words and word frequencies,
    returns dict where:
        keys == frequencies > 1
        vals == lists of words with that frequency
    """
    sortedFreqs = {}

    for word in freqs:
        if freqs[word] > 1:
            if freqs[word] in sortedFreqs:
                sortedFreqs[freqs[word]].append(word)
            else:
                sortedFreqs[freqs[word]] = [word]

    return sortedFreqs


def replaceWords(phrase):
    """
    Given a phrase, determines the most-used words and
    returns the phrase with the second instances of the
    most-used words replaced with foreign words in the
    language of choice.
    """
    words = (phrase.lower()).split()
    sortedFreqs = []

    def sortFreqs():
        """
        Creates a list of lists of words sorted
        from lowest to highest frequency.
        """
        #helpers
        wordFreqs = wordFreq(phrase)
        usageFreqs = sortByUsage(wordFreqs)

        for k in sorted(usageFreqs):
            sortedFreqs.append(usageFreqs[k])

    def translate():
        acc = {"past": [], "changed": []}
        ct = 0 #for indexing words

        for word in words:
            if word in acc["past"] and word in sortedFreqs[-1] and word in foreignDict:
                words[ct] = foreignDict[word] #replace original word w/ foreign word
                sortedFreqs[-1].remove(word)  #remove current most popular word
                acc["changed"].append(word)

            elif word in acc["changed"]:
                words[ct] = foreignDict[word]

            elif word not in acc["past"]:
                acc["past"].append(word)

            ct += 1

    def reCap():
        """
        Re-capitalizes translated text according to
        capitalizations in original text.
        """
        ct = 0
        phraseList = phrase.split()

        for word in phraseList:
            if phraseList[ct] != words[ct]:
                if word[0].isupper():
                    words[ct] = words[ct][0].upper() + words[ct][1:]
            ct += 1

    sortFreqs()
    translate()
    reCap()

    return " ".join(words)

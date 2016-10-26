# Bliss Program: Blisspeak, Blisscribe, Blisstudy, Blissynthesis, Blissight, Blisscript, Blisspell, Blissavvy
# -------------
#
#  ^
#  O
#
# features:
# ========
# - (partially) translates English text into Blissymbols:
#    e.g. I like dogs -> I like [Blissymbol for dogs] (more @ functions section below)
# - can email PDFs(?) to users, or return text as a single image, or email/return plaintext w/ multiple embedded images
# - users can choose the frequency/rate of word translation (e.g. immediate "full" translation [as full as is possible/comprehensible],
#    or partial translation incrementing by X words until end of text, etc.)
#
#
# caveats:
# ========
# - unknown words will not be translated ---solution--> program can machine-learn how to create new symbols for unknown words
#    by creating representation of word(s) thru scanning dictionary definitions & combining appropriate/salient rudimentary Blissymbols
# - copyright (utilizes Blissymbols, created by Charles Bliss & owned by Bliss Foundation) ---solution---> contact Bliss Foundation for permissions(?)
# - translations of useless/non-symbolic words ---solution---> translate nouns first(?) or offer users option to prioritize which words are replaced
#    e.g. option to replace all words, only nouns, verbs first, etc.
#
#
# constants:
# =========
# 1) have existing sorted list of x most common English (/ origin language) words
# 2) have existing English/Blissymbols dictionary (English keys, Blissymbol values)
#   - figure out how to store/display Blissymbols in Python/Xcode/Java/etc. (as images, ASCII/text) -> ImageLibrary? (from ImageLibrary import *)
#
#
# functions:
# =========
# - I/O:
#    input: English text
#    output: English text partially-to-fully translated into Blissymbols
#
# 1) take in English text and ...
#    .1) create a dict of most common words in text (key = word, val = frequency) if option for most common words in text is chosen; OR
#    .2) load existing dict of most common English words [constant] if option for most common English words is chosen.
# 2) take in English text and determine the rate of word translation desired, taking into mind user's selections and text length.
# 3) using the English/Blissymbols dict, common words dicts (within-text if 1.1, or English if 1.2), and ideal word replacement frequency, begin
#     creating a copy (type == list) of original text string:
#   - first, take the most common word from the user's desired dictionary, and replace all instances of it from the second time used and onward;
#   - next, take the nth most common word [...ditto...] and replace all instances of it from the 1+(n*x) th time used and onward, where x is the
#     factor of desired translation speed:
#     e.g. x=0 immediate full translation, x=1 1 word translated per step, x=2 1 word translated every 2 steps, x=0.5 two words translated per step.
# 4) calculate the rate of change needed for a given text if all text is to be fully translated by the end
#     e.g. the first sentence is full English, the last sentence is fully translated
#     n.b. "full" translation not measured by sentences, measured by translating a certain fraction of characters/words in the text (e.g. 100% nouns, 90% verbs, & 75% adjectives)
# 5) determine modes of speech for ambiguous words (e.g. whether word is adjective, adverb, verb, noun, etc.) -> create conceptual framework for sentence meaning based on context
#     if word intent is ambiguous, then leave untranslated, or ask user if they want to help the program label particles (it will give machine learning examples!)
# 6) convert translated text into desired output format (string, PDF, image, etc.).
# 7) output converted text to user.
#
#
# options:
# =======
# - write a script to auto-compose a foreign Blissymbols dictionary by browsing web/using Google Translate/scanning dictionaries/etc. (using the Internet to collect examples)
#
# - users can choose b/t replacing words by
#    most common in English language (-> have list of most common words ready, then once list is exhausted, begin replacing by most common words in text), or
#    most common in input text (-> build freqlist of words in text)
#
# - offer a read-along feature that synchronizes w/ Kindle/iBooks
#    allow users to keep track of which words they know/have seen before
#    allow users option to tap a word they would like to see in Blissymbols, & offer option to replace all future instances
#    allow users option to tap a word they would like to convert back to English, & offer option to un-translate all instances
#
# - create classification system for distinguishing nouns, verbs, adjectives, adverbs, etc. & include in foreign dictionary
#    verb tenses (e.g. is, am, are) all under one main verb, pronouns (e.g. I, me) all under one pronoun, etc.
#    classify verbs according to tense (past/present/future)&  subject (I/you/he/she/they/we)
#    replace concrete nouns first? or offer users the option to select which types of words to replace & in which order
#    check for proper nouns (names) through 1st-letter capitalization, sentence location cues (is it the subject/object?), etc.
#    ONLY replace certain parts of speech (e.g. nouns and verbs)
#
# - when necesssary, include multiple origin words in 1 key translating to 1 foreign word (thesaurus-like)
#
# - offer a number of books from Project Gutenberg - Alice in Wonderland, The Little Prince, etc.
#
# - create a reverse translator that stores the most common words in a foreign language and ONLY translates to English the words that are NOT common, or translates backwards from foreign to English


# FAQ
# ===
# who what when where why how
#
# mission statement:
# -----------------
#
# How might you try to teach someone who's never spoken what a dog is?  [/Imagine meeting a person without language.  How might you teach them
# what a dog is?] You likely wouldn't say "dog" to them (though you might try it once or twice) because of the inherent language barrier: they
# can't know what "dog" means without speaking your language.  You likewise wouldn't try to say "dog" to them in any other language either,
# since those words are just as useless.
#
# Instead, you might play a game of charades and show them how a dog acts by panting and barking, or draw them a picture of a dog.  Despite the
# fact that this method doesn't use words, you are still communicating.  The former method--of showing how a dog acts--is a form of sign
# language, while the latter method--of showing how a dog looks--is a form of pictoral language.
#
# Now try to imagine the same situation, except this time you are teaching them the word "the".  This, you will realize, is impossible, since
# "the" is only part of our language for the sake of grammatical coherence.  It interacts with other words, but has no meaning on its own.
# This doesn't mean that words like "the" are unnecessary in English--you must, of course, continue to use them!--but rather that such
# grammatical constructions are unnecessary for purely semantic communication, as allowed by visuo-spatial languages.
#
# We can imagine a natural language that remains purely semantic.  Many constructed languages, such as [...] have attempted to meet this
# important criteria.  Yet these languages, however successful in their attempts, still cannot be understood by non-speakers.
# Visuo-spatial languages, by comparison, are immediately and intuitively understood by all humankind through the common senses of vision and
# space.
#
# In line with Charles Bliss' motivations for inventing Blissymbols, Blisspeak hopes to transcend linguistic barriers and bring people of all
# languages together to enable universal communication and understanding.  Blisspeak combines the intuitive visualization of Blissymbols with
# existing language structures, with the ultimate goal of allowing users, through reading Blissymbols, to deepen their semantic understanding
# and speak a language beyond linguistics.
#
# Unlike words, ideograms have immediately salient semantics.  Blissymbols is a language understood with the heart, not the mind.
#
# Words are dead on their own: language requires that its speakers make repeated associations between words and phenomena before they are able to
# communicate.  The language of pictures removes the layer of linguistic abstraction, allowing pure associations between language and phenomena.
# Ideograms, unlike words, are alive without context.
#
# Communication between human beings has long been limited by linguistic structures.  We can only speak with a common language, and though
# English is gaining worldwide popularity as the lingua franca of choice, it is still a language primarily of grammar, and only secondarily
# of semantics.
#
# In China, the written language system is the same for Mandarin as well as Cantonese speakers.  They cannot understand each other verbally, but
# through reading and writing in the same language system, they are able to overlook their linguistic differences.  Despite their linguisti
# differences, communication prevails.
#
# As of 1969, the moon has bore a plaque bearing a facsimile of Richard Nixon's signature, and since the 1970s, the Pioneer plaques and Arecibo
# message have bore pictoral representations of human life and scientific knowledge.  If we were to receive alien visitors to the moon, or to
# earth after human life is long gone, how could we ensure that our vast bodies of knowledge would not be lost in linguistic abstractions?  Language
# only allows meaning between its speakers--to an alien troupe, Nixon's signature would appear to be no more than an arbitrary scribble.  Is there
# a way to preserve meaning across time, across all modes of life?
#
# In considering how to inform future human people of radioactive waste, scientists and thinkers have come up with a variety of communication
# methods: sharp, menacing rocks; ghastly pictures; phosphorescent cats.  In such modern times, we must consider how to communicate to
# creatures (human, animal, or alien) that do not share our current language systems.
#
# It can be presumed that the human mind's fixation on sight as the ultimate faculty of understanding will outlast the ages.  Ideographic languages
# are therefore a language of the future, not only for explicit learners but for non-learners as well, to whom meaning can be quickly and explicitly
# communicated.
#
# Blisspeak proposes a new way of thinking about language, not as a system of rules but as a method of information transfer between thinking beings.
#
# Much of English class has been dedicated to spelling, grammar, and linguistic rules, but seldom has language-learning focussed on semantics: the meaning
# behind words.
#
# If a picture is worth a thousand words, then ideographic languages are more concise than our own.
#
#
# what is blisspeak?
# -----------------
# Blisspeak is a translation service which slowly converts a language (now only English) into Blissymbols.  The translation begins with nouns
# and verbs, since these are the most salient symbols.  This allows you to not only learn Blissymbols more intuitively, but to transform your
# experience of language such that the experience of reading comes closer to actual sensation than words.
#
# what are blissymbols?
# --------------------
# Blissymbols is an ideographic language system invented by Charles Bliss in 1949, originally intended as a universal language.  It is commonly
# used by theose with mental, visual, and/or auditory impairment so that they may use language as the rest of us do.
#
# why learn blissymbols?
# ---------------------
# ~
#
# who uses blissymbols?
# --------------------
# ~
#
# how can I contribute to blisspeak?
# ---------------------------------
# ~
#


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

# coding: utf-8
"""
DEMO:

    Used for demoing MorphemeParser, MorphemeChart, and more.
"""
from speechart.speecharts import *


# construct a MorphemeChart to create a DFA for words in your desired language
dfa = MorphemeChart("English")
dfa.add_words("hello there my friend how are you today")
img = dfa.chart()
img.save("out/en_word_chart.png")    # save chart to file
dfa.refresh_data()

dfa = MorphemeChart("Finnish")
dfa.word_declension("nuo")  # adds nuo's declension to this dfa
dfa.refresh_data()          # stores all changes from this DFA's data back to JSONs (in data)
dfa.clear()                 # resets this DFA's states
# fetch nearest homophones between languages
dfa.nearest_homophone("naapuri", "English")
dfa.nearest_homophone("kuulu", "English")
dfa.refresh_data()

'''
# supports chart visualization in many languages
dfa = MorphemeChart("Chinese")
dfa.add_states(lim=500)
dfa.chart("Chinese Morpheme Chart")

dfa = MorphemeChart("Korean")
dfa.add_states(lim=500)
dfa.chart("Korean Morpheme Chart")

dfa = PhonemeChart("Japanese")
dfa.add_states(lim=500)
dfa.chart("Japanese Phoneme Chart")
'''

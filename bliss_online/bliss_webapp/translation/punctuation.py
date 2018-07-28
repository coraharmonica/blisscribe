# coding: utf-8
"""
PUNCTUATION:

    Holds punctuation for Blisscribe.
"""
import string


START_PUNCT = {"(", '"', "-",
               "\xe2\x80\x9c", "\xe2\x80\x98", "\xe2\x80\x9e"}  # spacing before
END_PUNCT = {".", ",", ";", ":", "?", "!", ")", '"', "-",
             "\xe2\x80\x9d", "\xe2\x80\x99", u"\u201d"}         # spacing after
PUNCTUATION = START_PUNCT.union(END_PUNCT)
MID_PUNCT = {u"-", u"\u2013", u"\u2014"}
CONTRACTIONS = {u"'"}
PUNCTUATION.update(set(string.punctuation))
PUNCTUATION = PUNCTUATION.union(MID_PUNCT.union(CONTRACTIONS))
WHITESPACE = {u"\n", u'', u' ', u'_'}

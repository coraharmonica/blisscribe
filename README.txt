 Blissymbols Project:
   "Blisscribe" \^
 -------------------
 An English-to-Blissymbols translator.

 table of contents
 =================

 A) summary
 B) constants
 C) functions
 D) caveats


  A) summary
  ==========
  1) partially translates English text into Blissymbols
     e.g. I like dogs -> I like [Blissymbol for dogs]
     e.g. Let's look at the pond -> Let's [Blissymbol for look] at the [Blissymbol for pond]
  2) users can choose the rate of word translation
     e.g. immediate "full" translation [as full as is possible/comprehensible]
     e.g. partial translation incrementing by X words until end of text
  3) can email PDFs(?) to users, or return text as a single image, or email/return plaintext w/ multiple embedded images
  ~ see a more in-depth look at the functions in the C) functions section below ~
 
 
  B) constants
  ============
  1) preexisting sorted list of x most common English (/ origin language) words
  2) preexisting English/Blissymbols dictionary (English keys, Blissymbol values)
    - figure out how to store/display Blissymbols in Java (as images, ASCII/text, rich text/LaTeX, etc.)
 
 
  C) functions
  ============
  I/O
  ---
    input: English text
    output: English text partially-to-fully translated into Blissymbols

  method
  ------
  1) take in English text and ...
    .1) create a dict of most common words in text (key = word, val = frequency) if option for most common words in text is chosen; OR
    .2) load existing dict of most common English words [constant] if option for most common English words is chosen.
  2) determine the rate of word translation desired, taking into mind user's selections and input English text length.
  3) using the English/Blissymbols dict, common words dicts (within-text if C)1.1, or English if C)1.2), and ideal word replacement
     frequency, begin creating a copy (type == list) of original text string:
    .1) first, take the most common word from the user's desired dictionary, and replace all instances of it from the second time used and
        onward;
    .2) next, take the nth most common word from the same dictionary, and replace all instances of it from the 1+(n*x) th time used and
        onward, where x is the factor of desired translation speed:
        e.g. x=0 immediate full translation, x=1 1 word translated per step, x=2 1 word translated every 2 steps, x=0.5 two words
        translated per step.
 4) calculate the rate of change needed for a given text if all text is to be fully translated by the end
     e.g. the first sentence is full English, the last sentence is fully translated
     n.b. "full" translation not measured by sentences, measured by translating a certain fraction of characters/words in the text (e.g. 
    100% nouns, 90% verbs, & 75% adjectives)
  5) determine modes of speech for ambiguous words (e.g. whether word is adjective, adverb, verb, noun, etc.) -> create conceptual
     framework for sentence meaning based on context if word intent is ambiguous, then leave untranslated, or ask user if they want to
     help the program label particles (it'll provide machine learning examples!)
  6) convert translated text into desired output format (string, PDF, image, etc.).
  7) output converted text to user.
 
 
  D) caveats
   ==========
  1) unknown words will not be translated ---solution--> program can machine-learn how to create new symbols for unknown words
     by creating representation of word(s) thru scanning dictionary definitions & combining appropriate/salient rudimentary Blissymbols
  2) copyright (utilizes Blissymbols, created by Charles Bliss & owned by Bliss Foundation) ---solution---> contact Bliss Foundation for
     permissions(?)
  3) translations of useless/non-symbolic words ---solution---> translate nouns first(?) or offer users option to prioritize which words
     are replaced
     e.g. option to replace all words, only nouns, verbs first, etc.

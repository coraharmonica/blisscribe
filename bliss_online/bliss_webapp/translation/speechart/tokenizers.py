from nltk.tokenize import WordPunctTokenizer, PunktSentenceTokenizer, BlanklineTokenizer
from nltk import pos_tag_sents
from nltk.tokenize import regexp_tokenize, wordpunct_tokenize, blankline_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

word_tokenizer = None
sent_tokenizer = None
line_tokenizer = None
lemmatizer = None


def init_word_tokenizer():
    global word_tokenizer
    if word_tokenizer is None:
        word_tokenizer = WordPunctTokenizer()


def init_sent_tokenizer():
    global sent_tokenizer
    if sent_tokenizer is None:
        sent_tokenizer = PunktSentenceTokenizer()


def init_line_tokenizer():
    global line_tokenizer
    if line_tokenizer is None:
        line_tokenizer = BlanklineTokenizer()


def init_lemmatizer():
    # lang = english
    global lemmatizer
    if lemmatizer is None:
        lemmatizer = WordNetLemmatizer()


def lemmatize(word, pos):
    init_lemmatizer()
    return lemmatizer.lemmatize(word, pos)


def sent_tokenize(text):
    try:
        return sent_tokenizer.tokenize(text)
    except AttributeError:
        init_sent_tokenizer()
        return sent_tokenizer.tokenize(text)


def word_tokenize(text):
    try:
        return word_tokenizer.tokenize(text)
    except AttributeError:
        init_word_tokenizer()
        return word_tokenizer.tokenize(text)


def tokenize_pos_tag(phrase, lang_code="eng"):
    init_line_tokenizer()
    phrase = ".\n".join(blankline_tokenize(phrase))  # add period to blank lines to simulate "sentences"
    sents = sent_tokenize(phrase)
    sents_tokens = [word_tokenize(s) for s in sents]
    sents_tags = pos_tag_sents(sents_tokens, lang=lang_code)
    print("sents:", sents_tokens)
    print("tokens:", sents_tags)
    word_tags = []
    for s in sents_tags:
        word_tags.extend(s)
    return word_tags


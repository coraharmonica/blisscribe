from nltk.tokenize import WordPunctTokenizer, PunktSentenceTokenizer


word_tokenizer = None
sent_tokenizer = None


def init_word_tokenizer():
    global word_tokenizer
    if word_tokenizer is None:
        word_tokenizer = WordPunctTokenizer()


def init_sent_tokenizer():
    global sent_tokenizer
    if sent_tokenizer is None:
        sent_tokenizer = PunktSentenceTokenizer()


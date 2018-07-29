"""
EXCERPTS:

    Holds defn English texts used for testing
    and reading.
"""
import os
from nltk.corpus import gutenberg #, brown

FILE_PATH = os.path.dirname(os.path.realpath(__file__))


def pair_titles_texts(titles, texts):
    """
    Initializes a dict with titles providing keys and
    texts providing values.
    ~
    Assumes titles and texts are paired and ordered.

    :return: dict, where...
        keys (str) - author and title (name) of a text_image
        vals (str) - text_image contents
    """
    books = {}
    idx = 0
    for title in titles:
        books[title] = texts[idx]
        idx += 1
    return books


def parse_plaintext(filename):
    """
    Parses plaintext file with this filename and returns a string representing
    its contents.

    :param filename: str, filename of text_image file
    :return: str, text_image file's contents
    """
    contents = []
    slash = "/" if filename[0] != "/" else ""

    with open(FILE_PATH + slash + filename, "r", encoding='utf-8') as text:
        for line in text:
            contents.append(line)

    return "".join([str(c) for c in contents])


def parse_excerpts(filenames):
    """
    Parses plaintext files with given filenames and returns a dictionary of words
    with corresponding image file links.
    If a line in the file contains multiple words, this function splits the line
    and adds each word to the dict as separate entry linking to the same Blissymbol.
    If a word in the file has no corresponding Blissymbol, the {key,val} pair
    is not added to the output dict.

    :param filename: str, filename of text_image file for lexicon (each word sep. by \n)
    :return: dict, where...
        keys (str) - word in filename
        vals (str/list) - word's corresponding Blissymbol image file link(s)
    """
    books = {}

    for filename in filenames:
        title = filename[14:-4].replace("-", " ")
        books[title] = parse_plaintext(filename)

    return books


def write_plaintext(text, filename):
    """
    Writes this text to this filename.

    :param text: str, text to write to file
    :param filename: str, name of file to write to
    :return: None
    """
    slash = "/" if filename[0] != "/" else ""

    with open(FILE_PATH + slash + filename, mode="w+", encoding='utf-8') as out:
        out.write(text)
        out.close()


sample_texts = ["/sample texts/adams-hitchhiker's_guide.txt",
                "/sample texts/barrie-peter_pan.txt",
                "/sample texts/carroll-alice_in_wonderland.txt",
                "/sample texts/carroll-alice_in_wonderland_polish.txt",
                "/sample texts/carroll-alice_in_wonderland_french.txt",
                "/sample texts/carroll-alice_in_wonderland_spanish.txt",
                "/sample texts/baum-wizard_of_oz.txt",
                "/sample texts/conrad-heart_of_darkness.txt",
                "/sample texts/dfw-infinite_jest.txt",
                "/sample texts/exupery-little_prince.txt",
                "/sample texts/exupery-little_prince_german.txt",
                "/sample texts/exupery-little_prince_polish.txt",
                "/sample texts/exupery-little_prince_russian.txt",
                "/sample texts/exupery-little_prince_spanish.txt",
                "/sample texts/exupery-petit_prince.txt",
                "/sample texts/juster-phantom_tollbooth.txt",
                "/sample texts/l'engle-wrinkle_in_time.txt",
                "/sample texts/kafka-metamorphosis_english.txt",
                "/sample texts/kafka-metamorphosis_german.txt",
                "/sample texts/lewis-chronicles_of_narnia.txt",
                "/sample texts/nabokov-lolita.txt",
                "/sample texts/poe-raven.txt",
                "/sample texts/pynchon-gravity's_rainbow.txt",
                "/sample texts/sapowski-witcher_1_polish.txt",
                "/sample texts/sapowski-witcher_2_polish.txt",
                "/sample texts/tolkien-the_hobbit.txt",
                "/sample texts/tolkien-lord_of_the_rings_1.txt",
                "/sample texts/tolkien-lord_of_the_rings_2.txt",
                "/sample texts/tolkien-lord_of_the_rings_3.txt",
                "/sample texts/dosto-notes_from_underground.txt",
                "/sample texts/dosto-notes_from_underground_russian.txt",
                "/sample texts/rimbaud-saison_en_enfer.txt",
                "/sample texts/frost-woods.txt",
                "/sample texts/ievan_polkka.txt"]
#brown_texts = {file_id: " ".join(brown.words(file_id)) for file_id in brown.fileids()}
# remove Gutenberg header for analysis
gutenberg_texts = {file_id[:-4].replace("-", " "): " ".join(gutenberg.words(file_id)).split("]", 1)[1]
                   for file_id in gutenberg.fileids()}

books = {}
books.update(parse_excerpts(sample_texts))
#books.update(brown_texts)
books.update(gutenberg_texts)


# Fiction
# --> Children's
alice_in_wonderland = books["carroll alice_in_wonderland"]
alice_in_wonderland_polish = books["carroll alice_in_wonderland_polish"]
alice_in_wonderland_french = books["carroll alice_in_wonderland_french"]
alice_in_wonderland_spanish = books["carroll alice_in_wonderland_spanish"]
little_prince = books["exupery little_prince"]
little_prince_german = books["exupery little_prince_german"]
little_prince_polish = books["exupery little_prince_polish"]
little_prince_russian = books["exupery little_prince_russian"]
little_prince_spanish = books["exupery little_prince_spanish"]
petit_prince = books["exupery petit_prince"]
phantom_tollbooth = books["juster phantom_tollbooth"]
wrinkle_in_time = books["l'engle wrinkle_in_time"]
chronicles_of_narnia = books["lewis chronicles_of_narnia"]
wizard_of_oz = books["baum wizard_of_oz"]
peter_pan = books["barrie peter_pan"]
# --> Adult
notes_from_underground = books["dosto notes_from_underground"]
notes_from_underground_russian = books["dosto notes_from_underground_russian"]
heart_of_darkness = books["conrad heart_of_darkness"]
metamorphosis_english = books["kafka metamorphosis_english"]
metamorphosis_german = books["kafka metamorphosis_german"]
# --> Fantasy
hitchhikers_guide = books["adams hitchhiker's_guide"]
moby_dick = books["melville moby_dick"]
witcher_1 = books["sapowski witcher_1_polish"]
witcher_2 = books["sapowski witcher_2_polish"]
hobbit = books["tolkien the_hobbit"]
lotr1 = books["tolkien lord_of_the_rings_1"]
lotr2 = books["tolkien lord_of_the_rings_2"]
lotr3 = books["tolkien lord_of_the_rings_3"]

# Poetry
blake_songs = books["blake poems"]
frost_poem = books["frost woods"]
leaves_of_grass = books["whitman leaves"]
paradise_lost = books["milton paradise"]
the_raven = books["poe raven"]
saison_en_enfer = books["rimbaud saison_en_enfer"]

# Scripture
kjv = books["bible kjv"]
# try to find in all languages, should be easy enough rite?
# jk the kjv is MASSIVE

# Song
ievan_polkka = books["ievan_polkka"]

# Theatre
hamlet = books["shakespeare hamlet"]
julius_caesar = books["shakespeare caesar"]
macbeth = books["shakespeare macbeth"]


# Texts in specific languages
shakespearean_texts = [hamlet, julius_caesar, macbeth]
lord_of_the_rings = [hobbit, lotr1, lotr2, lotr3]
multilingual_texts = {"eng": [alice_in_wonderland, little_prince, wizard_of_oz, peter_pan,
                              phantom_tollbooth, wrinkle_in_time, chronicles_of_narnia,
                              hitchhikers_guide, metamorphosis_english, heart_of_darkness,
                              the_raven, blake_songs, frost_poem, leaves_of_grass, paradise_lost,
                              hamlet, julius_caesar, macbeth, kjv] + lord_of_the_rings + list(gutenberg_texts.values()),
                      "fin": [ievan_polkka],
                      "fra": [alice_in_wonderland_french, petit_prince, saison_en_enfer],
                      "deu": [metamorphosis_german, little_prince_german],
                      "pol": [alice_in_wonderland_polish, little_prince_polish, witcher_1, witcher_2],
                      "rus": [little_prince_russian, notes_from_underground_russian],
                      "spa": [alice_in_wonderland_spanish, little_prince_spanish]}
english_texts = multilingual_texts["eng"]
finnish_texts = multilingual_texts["fin"]
french_texts = multilingual_texts["fra"]
german_texts = multilingual_texts["deu"]
polish_texts = multilingual_texts["pol"]
russian_texts = multilingual_texts["rus"]
spanish_texts = multilingual_texts["spa"]


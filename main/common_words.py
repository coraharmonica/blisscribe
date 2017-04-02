import lexicon
import blisscribe
from PIL import Image, ImageDraw, ImageFont

common_words = ['time', 'issue', 'year', 'side', 'people', 'kind', 'way', 'head', 'day', 'house',
                'man', 'service', 'thing', 'friend', 'woman', 'father', 'life', 'power', 'child', 'hour',
                'world', 'game', 'school', 'line', 'state', 'end', 'family', 'member', 'student', 'law',
                'group', 'car', 'country', 'city', 'problem', 'community', 'hand', 'name', 'part', 'president',
                'place', 'team', 'case', 'minute', 'week', 'idea', 'company', 'kid', 'system', 'body',
                'program', 'information', 'question', 'back', 'work', 'parent', 'government', 'face', 'number', 'others',
                'night', 'level', 'Mr', 'office', 'point', 'door', 'home', 'health', 'water', 'person',
                'room', 'art', 'mother', 'war', 'area', 'history', 'money', 'party', 'story', 'result',
                'fact', 'change', 'month', 'morning', 'lot', 'reason', 'right', 'research', 'study', 'girl',
                'book', 'guy', 'eye', 'food', 'job', 'moment', 'word', 'air', 'business', 'teacher']

bliss_alphabet = []

for word in common_words:
    if word in lexicon.bliss_dict.keys():
        bg_wh = 200
        bliss_word = blisscribe.getBlissImg(word, bg_wh)
        eng_word = blisscribe.getWordImg(word)

        #bg_width = max(eng_word.width, bliss_word.width)
        #bg_height = max(eng_word.height, bliss_word.height)
        ratio = 2
        start_eng_word = bg_wh/2 - (eng_word.width/2)
        start_bliss_word = bg_wh/2 - (blisscribe.getWordWidth(bliss_word)/2)

        bg = Image.new("RGBA", (bg_wh, bg_wh), (255, 255, 255, 255))
        bg.paste(eng_word, (start_eng_word, 0))
        bg.paste(bliss_word, (start_bliss_word, blisscribe.font_size * ratio))

        bliss_alphabet.append(bg)


alphabet_bg_wh = 2000
alphabet_bg = Image.new("RGBA", (alphabet_bg_wh, alphabet_bg_wh-400), (255, 255, 255, 255))
indent = 0
line_height = 0

for defn in bliss_alphabet:
    alphabet_bg.paste(defn, (indent, line_height * 200))
    if (indent + blisscribe.getWordWidth(defn)) > alphabet_bg_wh:
        indent = 0
        line_height += 1
    else:
        indent += blisscribe.getWordWidth(defn)


alphabet_bg.show()
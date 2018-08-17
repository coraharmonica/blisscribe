
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
#from translation.blisscribe import tokenizers


alice_txt = """ROZDZIAŁ I: PRZEZ KRÓLICZĄ NORĘ

Alicja miała już dość siedzenia na ławce obok siostry i próżnowania. Raz czy dwa razy zerknęła do książki, którą czytała siostra. Niestety, w książce nie było obrazków ani rozmów. „A cóż jest warta książka - pomyślała Alicja - w której nie ma rozmów ani obrazków?”
Alicja rozmyślała właśnie - a raczej starała się rozmyślać, ponieważ upał czynił ją bardzo senną i niemrawą - czy warto męczyć się przy zrywaniu stokrotek po to, aby uwić z nich wianek. Nagle tuż obok niej przebiegł Biały Królik o różowych ślepkach.
Właściwie nie było w tym nic nadzwyczajnego. Alicja nie dziwiła się nawet zbytnio słysząc, jak Królik szeptał do siebie: „O rety, o rety, na pewno się spóźnię”. Dopiero kiedy Królik wyjął z kieszonki od kamizelki zegarek, spojrzał nań i puścił się pędem w dalszą drogę, Alicja zerwała się na równe nogi. Przyszło jej bowiem na myśl, że nigdy przedtem nie widziała królika w kamizelce ani królika z zegarkiem. Płonąc z ciekawości pobiegła na przełaj przez pole za Białym Królikiem i zdążyła jeszcze spostrzec, że znikł w sporej norze pod żywopłotem. Wczołgała się więc za nim do króliczej nory nie myśląc o tym, jak się później stamtąd wydostanie.
Nora była początkowo prosta niby tunel, po czym skręcała w dół tak nagle, że Alicja nie mogła już się zatrzymać i runęła w otwór przypominający wylot głębokiej studni.
Studnia była widać tak głęboka, czy może Alicja spadała tak wolno, że miała dość czasu, aby rozejrzeć się dokoła i zastanowić nad tym, co się dalej stanie. Przede wszystkim starała się dojrzeć dno studni, ale jak to zrobić w ciemnościach? Zauważyła jedynie, że ściany nory zapełnione były szafami i półkami na książki. Tu i ówdzie wisiały mapy i obrazki. Mijając jedna z półek Alicja zdążyła zdjąć z niej słój z naklejką Marmolada pomarańczowa. Niestety był on pusty. Alicja nie upuściła słoja, obawiając się, że może zabić nim kogoś na dole. Postawiła go po drodze na jednej z niższych półek.
„No, no - pomyślała - po tej przygodzie żaden upadek ze schodów nie zrobi już na mnie wrażenia. W domu zdziwią się, że jestem taka dzielna. Nawet gdybym spadła z samego wierzchołka kamienicy, nie pisnęłabym ani słówka”. Co do tego miała niewątpliwie rację).
W dół, w dół, wciąż w dół. Czy już nigdy nie skończy się to spadanie?
- Ciekawa jestem, ile mil dotychczas przebyłam - rzekła nagle Alicja. - Muszę być już gdzieś w pobliżu środka ziemi. Zaraz... zaraz... To będzie, zdaje się, około tysiąca mil. (Alicja uczyła się wielu podobnych rzeczy w szkole. Nie była to co prawda chwila na popisywanie się wiedzą, no i imponować nie było komu. Uznała jednak, że mała „powtórka” bywa czasami pożyteczna).
„Tak, wydaje mi się, że to będzie właśnie tysiąc mil. Ciekawe, pod jaką szerokością i długością geograficzną obecnie się znajduję”. (Alicja nie imała najmniejszego pojęcia, co oznacza „długość” lub „szerokość geograficzna”, ale słowa te wydały jej się dźwięczne i pełne mądrości).
    Tymczasem rozmyślała dalej:
„Chciałabym wiedzieć, czy przelecę całą ziemię na wylot. Jakie to będzie śmieszne, kiedy znajdę się naraz wśród ludzi chodzących do góry nogami. Zapytam ich o nazwę kraju, do którego przybyłam. „Przepraszam panią bardzo, czy to Nowa Zelandia, czy Australia?” (Tu Alicja usiłowała dygnąć, ale spróbujcie to zrobić w takich warunkach. Czy sądzicie, że Wam się to uda?)
„I co oni sobie o mnie pomyślą? Chyba że jestem głupia. Nie, już lepiej nie pytać. Może zobaczę gdzieś jaki napis”.
W dół, w dół, wciąż w dół. Nie było nic do roboty, więc Alicja zabawiała się nadal rozmową z samą sobą:
„Jacek będzie tęsknił za mną dziś wieczorem”. (Jacek był to kot). „Mam nadzieję, że w domu nie zapomną dać mu mleka na podwieczorek. Kochany, najdroższy Jacku! Gdybym cię teraz miała przy sobie! Obawiam się, co prawda, że w powietrzu nie ma myszy, ale mógłbyś chwytać nietoperze, a gacki bardzo przypominają myszy. Ale czy Jacek zjadłby gacka?”
Tu Alicji zachciało się nagle spać i zaczęła powtarzać na wpół sennie: „Czy Jacek zjadłby gacka? Czy Jacek zjadłby gacka?”, a czasami: „Czy gacek zjadłby Jacka?” Tak czy inaczej, nie umiała odpowiedzieć na te pytania, było jej więc właściwie wszystko jedno. Wreszcie poczuła, ze zasypia. Śniło jej się, że jest na spacerze z Jackiem i że mówi do niego bardzo groźnie: „Powiedz mi teraz całą prawdę, Jacku, czyś ty kiedy zjadł nietoperza?” I nagle - tym razem już na jawie - Alicja usiadła miękko na stosie chrustu i suchych liści. Spadanie skończyło się.
    Alicja nie potłukła się ani trochę i po chwili była już na nogach. Spojrzała w górę, lecz panowały tam straszne ciemności. Przed nią ciągnął się znowu długi korytarz. W dali spostrzegła pędzącego Białego Królika. Nie było ani chwili do stracenia.
    Puściła się więc w pogoń za Królikiem i przed jednym z zakrętów korytarza usłyszała jego zdyszany głosik:
- O, na moje uszy i bokobrody, robi się strasznie późno!
Była już zupełnie blisko, ale za zakrętem Biały Królik znikł w sposób niewytłumaczony. Alicja znalazła się w podłużnej, niskiej sali z długim rzędem lamp zwisających z sufitu.
    Rozejrzała się dokoła i spostrzegła mnóstwo drzwi. Usiłowała otworzyć każde z nich po kolei, ale wszystkie były zaryglowane. Zasmucona, odeszła więc ku środkowi sali, straciła bowiem nadzieję, że się kiedykolwiek stąd wydostanie.
    Nagle znalazła się przed stolikiem na trzech nogach, zrobionym z grubego szkła. Na stoliku leżał maleńki, złoty kluczyk. Alicja ucieszyła się myśląc, iż otwiera on jakieś drzwi. Niestety. Czy zamki były zbyt wielkie, czy kluczyk zbyt mały, dość ze nie pasował on nigdzie. Obchodząc salę po raz drugi, Alicja zauważyła jednak coś, czego nie dostrzegła przedtem: zasłonę, za którą znajdowały się drzwi niespełna półmetrowej wysokości. Przymierzyła złoty kluczyk i przekonała się z radością, ze pasuje.
    Drzwiczki prowadziły do korytarzyka niewiele większego od szczurzej nory. Alicja uklękła i przez korytarzyk ujrzała najpiękniejszy chyba na świecie ogród. Jakże pragnęła przechadzać się tam wśród ślicznych kwietników i orzeźwiających wodotrysków! ale jak tu o tym marzyć, skoro nie potrafiłaby wsunąć przez norkę
nawet głowy. „A zresztą, gdyby nawet moja głowa dostała się do ogrodu, nie na wiele by się zdała bez ramion i reszty. Och, gdybym mogła złożyć się tak jak teleskop∗. Może bym nawet i umiała, ale jak się do tego zabrać?” (Alicja bowiem doznała ostatnio tylu niezwykłych wrażeń, że nic nie wydawało się jej niemożliwe).
    Dłużej stać pod drzwiczkami nie miało sensu. Wróciła więc do stolika z niejasnym przeczuciem, że znajdzie na nim nowy kluczyk albo chociaż przepis na składanie ludzi na wzór teleskopów. Tym razem na stoliku stała buteleczka(„Na pewno nie było jej tu przedtem” - pomyślała Alicja) z przytwierdzoną do szyjki za pomocą nitki karteczką. Alicja przeczytała na niej pięknie wykaligrafowane słowa: Wypij mnie.
    Łatwo powiedzieć „Wypij mnie”, ale nasza mała, mądra Alicja bynajmniej się do tego nie kwapiła. „Zobaczę najpierw - pomyślała - czy nie ma tam napisu: Uwaga - Trucizna. Czytała bowiem wiele uroczych opowiastek o dzieciach, które spaliły się, zostały pożarte przez dzikie bestie lub doznały innych przykrości tylko dlatego, że nie stosowały się do prostych nauk: na przykład, że rozpalonym do białości pogrzebaczem można się oparzyć, gdy trzyma się go zbyt długo w ręku, albo że - gdy zaciąć się bardzo głęboko scyzorykiem, to palec krwawi. Alicja przypomniała sobie doskonale, że picie z butelki opatrzonej napisem: „Uwaga - Trucizna rzadko komu wychodzi na zdrowie.
    Ta buteleczka jednak nie miała napisu: Trucizna. Alicja zdecydowała się więc skosztować płynu. Był on bardzo smaczny miał jednocześnie smak ciasta z wiśniami, kremu, ananasa, pieczonego indyka, cukierka i bułeczki z masłem), tak że po chwili buteleczka została opróżniona.
"""

ALICE_TAGGED = [
    [('ROZDZIAŁ', 'NN'),
     ('I', 'CD'),
     (':', ':'),
     ('PRZEZ', 'IN'),
     ('KRÓLICZĄ', 'NN'),
     ('NORĘ', 'NN'),
     ('.', '.')],
    [('Alicja', 'NNP'),
     ('miała', 'VBD'),
     ('już', 'RB'),
     ('dość', 'RB'),
     ('siedzenia', 'VB'),
     ('na', 'IN'),
     ('ławce', 'NN'),
     ('obok', 'IN'),
     ('siostry', 'NN'),
     ('i', 'CC'),
     ('próżnowania', 'NN'),
     ('.', '.')],
    [('Raz', 'NN'),
     ('czy', 'CC'),
     ('dwa', 'CD'),
     ('razy', 'NNS'),
     ('zerknęła', 'VBD'),
     ('do', 'IN'),
     ('książki', 'NN'),
     (',', ','),
     ('którą', 'DT'),
     ('czytała', 'VBD'),
     ('siostra', 'NN'),
     ('.', '.')],
    [('Niestety', 'RB'),
     (',', ','),
     ('w', 'IN'),
     ('książce', 'NN'),
     ('nie', 'DT'),
     ('było', 'VBD'),
     ('obrazków', 'NNS'),
     ('ani', 'CC'),
     ('rozmów', 'NNS'),
     ('.', '.')],
    [('"', '"'),
     ('A', 'CC'),
     ('cóż', 'DT'),
     ('jest', 'VB'),
     ('warta', 'NN'),
     ('książka', 'NN'),
     ('-', ':'),
     ('pomyślała', 'VBD'),
     ('Alicja', 'NNP'),
     ('-', ':'),
     ('w', 'IN'),
     ('której', 'DT'),
     ('nie', 'DT'),
     ('ma', 'VB'),
     ('rozmów', 'NNS'),
     ('ani', 'CC'),
     ('obrazków', 'NNS'),
     ('?', '?'),
     ('"', '"')],
    [('Alicja', 'NNP'),
     ('rozmyślała', 'VBD'),
     ('właśnie', 'RP'),
     ('-', ':'),
     ('a', 'CC'),
     ('raczej', 'CC'),
     ('starała', 'VBD'),
     ('się', 'NNP'),
     ('rozmyślać', 'VB'),
     (',', ','),
     ('ponieważ', 'CC'),
     ('upał', 'NN'),
     ('czynił', 'VBD'),
     ('ją', 'CC'),
     ('bardzo', 'RB'),
     ('senną', 'JJ'),
     ('i', 'CC'),
     ('niemrawą', 'JJ'),
     ('-', ':'),
     ('czy', 'CC'),
     ('warto', 'VB'),
     ('męczyć', 'VB'),
     ('się', 'NNP'),
     ('przy', 'IN'),
     ('zrywaniu', 'VBG'),
     ('stokrotek', 'NNS'),
     ('po', 'IN'),
     ('to', 'NNP'),
     (',', ','),
     ('aby', 'CC'),
     ('uwić', 'VB'),
     ('z', 'IN'),
     ('nich', 'DT'),
     ('wianek', 'NN'),
     ('.', '.')]
]

def features(sentence, index):
    return {
        'word': sentence[index],
        'prev_word': '' if index == 0 else sentence[index-1],
        'next_word': '' if index+1 == len(sentence) else sentence[index+1],
        'prefix-1': sentence[index][0],
        'prefix-2': sentence[index][:2],
        'prefix-3': sentence[index][:3],
        'suffix-1': sentence[index][-1],
        'suffix-2': sentence[index][-2:],
        'suffix-3': sentence[index][-3:],
        'is_first': index == 0,
        'is_last': index == len(sentence) - 1,
        'is_capitalized': sentence[index][0].upper() == sentence[index][0],
        'is_all_caps': sentence[index].upper() == sentence[index],
        'is_all_lower': sentence[index].lower() == sentence[index],
        'has_hyphen': '-' in sentence[index],
        'is_numeric': sentence[index].isdigit(),
    }


def untag(tagged_sentence):
    return [t for w, t in tagged_sentence]


def transform_to_dataset(tagged_sentences):
    x, y = [], []

    for tagged in tagged_sentences:
        for index in range(len(tagged)):
            x.append(features(untag(tagged), index))
            y.append(tagged[index][1])

    return x, y


# Split the dataset for training and testing
cutoff = int(.75 * len(ALICE_TAGGED))
training_sentences = ALICE_TAGGED[:cutoff]
test_sentences = ALICE_TAGGED[cutoff:]

print(len(training_sentences))
print(len(test_sentences))

ALICE_X, ALICE_Y = transform_to_dataset(training_sentences)

classifier = Pipeline([('vectorizer', DictVectorizer(sparse=False)),
                       ('classifier', DecisionTreeClassifier(criterion='entropy'))])
classifier.fit(ALICE_X[:cutoff], ALICE_Y[:cutoff])

x_test, y_test = transform_to_dataset(test_sentences)
print("Accuracy:", classifier.score(x_test, y_test))


'''
tagged_tokens = tokenizers.tokenize_pos_tag(alice_txt, lang_code="pol")
print("ALICE_TAGGED = {")
for token_tag in tagged_tokens:
    print('    ', token_tag, ",", sep="")
print("}")
'''

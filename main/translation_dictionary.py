from PIL import Image, ImageDraw, ImageFont
from decimal import *

directory = "/Users/courtney/Documents/creation/programming/\
personal projects/bliss translator/symbols/full/png/small/"            # shortcut

# alphabetized English-to-Blissymbols dictionary
"""
blissDict = {"air": Image.open(directory + "air.png"),
             "also": Image.open(directory + "also.png"),
             "and": Image.open(directory + "and.png"),
             "animal": Image.open(directory + "animal.png"),
             "book": Image.open(directory + "book.png"),
             "business": Image.open(directory + "business.png"),
             "buy": Image.open(directory + "buy.png"),
             "card": Image.open(directory + "paper.png"),
             "chair": Image.open(directory + "chair.png"),
             "child": Image.open(directory + "child.png"),
             "city": Image.open(directory + "city.png"),
             "clan": Image.open(directory + "people.png"),
             "cloud": Image.open(directory + "cloud.png"),
             "cost": Image.open(directory + "cost.png"),
             "commerce": Image.open(directory + "business.png"),
             "container": Image.open(directory + "container.png"),
             "county": Image.open(directory + "province.png"),
             "creation": Image.open(directory + "creation.png"),
             "data": Image.open(directory + "data.png"),
             "day": Image.open(directory + "day.png"),
             "division": Image.open(directory + "division.png"),
             "don't": Image.open(directory + "nothing.png"),
             "doesn't": Image.open(directory + "nothing.png"),
             "ear": Image.open(directory + "ear.png"),
             "earth": Image.open(directory + "earth.png"),
             "electricity": Image.open(directory + "electricity.png"),
             "email": Image.open(directory + "email.png"),
             "employment": Image.open(directory + "work.png"),
             "equal": Image.open(directory + "equal.png"),
             "exterior": Image.open(directory + "out.png"),
             "external": Image.open(directory + "out.png"),
             "eye": Image.open(directory + "eye.png"),
             "eyes": Image.open(directory + "eye.png"),
             "feeling": Image.open(directory + "feeling.png"),
             "find": Image.open(directory + "find.png"),
             "fire": Image.open(directory + "fire.png"),
             "flower": Image.open(directory + "flower.png"),
             "folk": Image.open(directory + "people.png"),
             "free": Image.open(directory + "free.png"),
             "freely": Image.open(directory + "free.png"),
             "ground": Image.open(directory + "ground.png"),
             "hand": Image.open(directory + "hand.png"),
             "he": Image.open(directory + "he.png"),
             "health": Image.open(directory + "health.png"),
             "help": Image.open(directory + "help.png"),
             #"her": Image.open(directory + "she.png"),
             #"herself": Image.open(directory + "she.png"),
             #"him": Image.open(directory + "he.png"),
             #"himself": Image.open(directory + "he.png"),
             #"his": Image.open(directory + "his.png"),
             "home": Image.open(directory + "home.png"),
             "house": Image.open(directory + "house.png"),
             "I": Image.open(directory + "I.png"),
             "information": Image.open(directory + "information.png"),
             "intensity": Image.open(directory + "intensity.png"),
             "internet": Image.open(directory + "internet.png"),
             "inventory": Image.open(directory + "list.png"),
             #"it": Image.open(directory + "it.png"),
             "job": Image.open(directory + "work.png"),
             "kid": Image.open(directory + "child.png"),
             "knowledge": Image.open(directory + "knowledge.png"),
             "label": Image.open(directory + "name.png"),
             "language": Image.open(directory + "language.png"),
             "life": Image.open(directory + "life.png"),
             "light": Image.open(directory + "light.png"),
             "list": Image.open(directory + "list.png"),
             "look": Image.open(directory + "see.png"),
             "man": Image.open(directory + "man.png"),
             "me": Image.open(directory + "I.png"),
             "medicine": Image.open(directory + "medicine.png"),
             "mind": Image.open(directory + "mind.png"),
             "mine": Image.open(directory + "my.png"),
             "minus": Image.open(directory + "minus.png"),
             "moon": Image.open(directory + "moon.png"),
             "more": Image.open(directory + "more.png"),
             "multiplication": Image.open(directory + "multiplication.png"),
             "music": Image.open(directory + "music.png"),
             "my": Image.open(directory + "my.png"),
             "myself": Image.open(directory + "I.png"),
             "name": Image.open(directory + "name.png"),
             "nature": Image.open(directory + "nature.png"),
             "negative": Image.open(directory + "nothing.png"),
             "new": Image.open(directory + "new.png"),
             "news": Image.open(directory + "news.png"),
             "now": Image.open(directory + "now.png"),
             "no": Image.open(directory + "nothing.png"),
             "none": Image.open(directory + "nothing.png"),
             "not": Image.open(directory + "not.png"),
             "nothing": Image.open(directory + "nothing.png"),
             "number": Image.open(directory + "number.png"),
             "our": Image.open(directory + "our.png"),
             "ours": Image.open(directory + "our.png"),
             "ourselves": Image.open(directory + "we.png"),
             #"out": Image.open(directory + "out.png"),
             "outside": Image.open(directory + "out.png"),
             "page": Image.open(directory + "paper.png"),
             "paper": Image.open(directory + "paper.png"),
             "part": Image.open(directory + "part.png"),
             "pen": Image.open(directory + "pen.png"),
             "pencil": Image.open(directory + "pencil.png"),
             "people": Image.open(directory + "people.png"),
             "person": Image.open(directory + "person.png"),
             "picture": Image.open(directory + "picture.png"),
             "pictures": Image.open(directory + "picture.png"),
             "piece": Image.open(directory + "piece.png"),
             "plus": Image.open(directory + "plus.png"),
             "price": Image.open(directory + "cost.png"),
             "protection": Image.open(directory + "protection.png"),
             "province": Image.open(directory + "province.png"),
             "purchase": Image.open(directory + "buy.png"),
             "rabbit": Image.open(directory + "rabbit.png"),
             "read": Image.open(directory + "read.png"),
             "region": Image.open(directory + "province.png"),
             "rock": Image.open(directory + "rock.png"),
             "room": Image.open(directory + "room.png"),
             "same": Image.open(directory + "same.png"),
             "school": Image.open(directory + "school.png"),
             "search": Image.open(directory + "search.png"),
             "see": Image.open(directory + "see.png"),
             #"she": Image.open(directory + "she.png"),
             "sister": Image.open(directory + "sister.png"),
             "sky": Image.open(directory + "sky.png"),
             "stairs": Image.open(directory + "stairs.png"),
             "state": Image.open(directory + "province.png"),
             "sun": Image.open(directory + "sun.png"),
             "table": Image.open(directory + "table.png"),
             "teeth": Image.open(directory + "teeth.png"),
             "term": Image.open(directory + "name.png"),
             #"their": Image.open(directory + "their (persons).png"),
             #"theirs": Image.open(directory + "their (persons).png"),
             #"them": Image.open(directory + "they.png"),
             #"themselves": Image.open(directory + "they.png"),
             #"they": Image.open(directory + "they.png"),
             "thing": Image.open(directory + "thing.png"),
             "time": Image.open(directory + "time.png"),
             "timepiece": Image.open(directory + "timepiece.png"),
             "title": Image.open(directory + "name.png"),
             "trade": Image.open(directory + "business.png"),
             "tree": Image.open(directory + "tree.png"),
             "tribe": Image.open(directory + "people.png"),
             "up": Image.open(directory + "up.png"),
             "upward": Image.open(directory + "up.png"),
             #"us": Image.open(directory + "we.png"),
             "watch": Image.open(directory + "watch.png"), # also Image.open(directory + "see.png")
             "water": Image.open(directory + "water.png"),
             #"we": Image.open(directory + "we.png"),
             "website": Image.open(directory + "website.png"),
             "week": Image.open(directory + "week.png"),
             "wheel": Image.open(directory + "wheel.png"),
             "without": Image.open(directory + "without.png"),
             "woman": Image.open(directory + "woman.png"),
             "work": Image.open(directory + "work.png"),
             "world": Image.open(directory + "world.png"),
             "year": Image.open(directory + "year.png"),
             "you": Image.open(directory + "you.png"),
             "youngster": Image.open(directory + "child.png"),
             "yourself": Image.open(directory + "you.png"),
             "your": Image.open(directory + "your (sing).png"),
             "yours": Image.open(directory + "your (sing).png")}
"""

blissDict = {
    'bagpipe': Image.open(directory + 'bagpipe.png'),
    'ladybird': Image.open(directory + 'ladybird.png'),
    'desirable': Image.open(directory + 'desirable.png'),
    'sleep': Image.open(directory + 'sleep.png'),
    'grandparent': Image.open(directory + 'grandparent.png'),
    'muzzle': Image.open(directory + 'muzzle.png'),
    'electricity': Image.open(directory + 'electricity.png'),
    'swan': Image.open(directory + 'swan.png'),
    'firecraft': Image.open(directory + 'firecraft.png'),
    'teaspoon': Image.open(directory + 'teaspoon.png'),
    'sorry': Image.open(directory + 'sorry.png'),
    'Euro': Image.open(directory + 'Euro.png'),
    'alternating': Image.open(directory + 'alternating.png'),
    'rescue': Image.open(directory + 'rescue.png'),
    'geology': Image.open(directory + 'geology.png'),
    'fireplace': Image.open(directory + 'fireplace.png'),
    'missionary': Image.open(directory + 'missionary.png'),
    'school': Image.open(directory + 'school.png'),
    'holiness': Image.open(directory + 'holiness.png'),
    'humidity': Image.open(directory + 'humidity.png'),
    'crotch': Image.open(directory + 'crotch.png'),
    'farmhouse': Image.open(directory + 'farmhouse.png'),
    'bicycle': Image.open(directory + 'bicycle.png'),
    'bacon': Image.open(directory + 'bacon.png'),
    'nail': Image.open(directory + 'nail.png'),
    'street': Image.open(directory + 'street.png'),
    'cactus': Image.open(directory + 'cactus.png'),
    'discus': Image.open(directory + 'discus.png'),
    'thunder': Image.open(directory + 'thunder.png'),
    'poison': Image.open(directory + 'poison.png'),
    'fjord': Image.open(directory + 'fjord.png'),
    'new': Image.open(directory + 'new.png'),
    'net': Image.open(directory + 'net.png'),
    'hero': Image.open(directory + 'hero.png'),
    'never': Image.open(directory + 'never.png'),
    'here': Image.open(directory + 'here.png'),
    'anthropology': Image.open(directory + 'anthropology.png'),
    'tornado': Image.open(directory + 'tornado.png'),
    'celebration': Image.open(directory + 'celebration.png'),
    'dry': Image.open(directory + 'dry.png'),
    'substance': Image.open(directory + 'substance.png'),
    'daughter': Image.open(directory + 'daughter.png'),
    'economics': Image.open(directory + 'economics.png'),
    'credit': Image.open(directory + 'credit.png'),
    'smoke': Image.open(directory + 'smoke.png'),
    'stressed': Image.open(directory + 'stressed.png'),
    'neurologist': Image.open(directory + 'neurologist.png'),
    'envious': Image.open(directory + 'envious.png'),
    'Jew': Image.open(directory + 'Jew.png'),
    'sliced': Image.open(directory + 'sliced.png'),
    'patience': Image.open(directory + 'patience.png'),
    'stern': Image.open(directory + 'stern.png'),
    'cheating': Image.open(directory + 'cheating.png'),
    'slaughterer': Image.open(directory + 'slaughterer.png'),
    'hungry': Image.open(directory + 'hungry.png'),
    'June': Image.open(directory + 'June.png'),
    'princess': Image.open(directory + 'princess.png'),
    'music': Image.open(directory + 'music.png'),
    'passport': Image.open(directory + 'passport.png'),
    'blueberry': Image.open(directory + 'blueberry.png'),
    'holy': Image.open(directory + 'holy.png'),
    'meteorologist': Image.open(directory + 'meteorologist.png'),
    'warm': Image.open(directory + 'warm.png'),
    'excellent': Image.open(directory + 'excellent.png'),
    'hole': Image.open(directory + 'hole.png'),
    'stickball': Image.open(directory + 'stickball.png'),
    'word': Image.open(directory + 'word.png'),
    'room': Image.open(directory + 'room.png'),
    'gasoline': Image.open(directory + 'gasoline.png'),
    'worm': Image.open(directory + 'worm.png'),
    'advocacy': Image.open(directory + 'advocacy.png'),
    'dizzy': Image.open(directory + 'dizzy.png'),
    'Brahma': Image.open(directory + 'Brahma.png'),
    'elbow': Image.open(directory + 'elbow.png'),
    'root': Image.open(directory + 'root.png'),
    'wand': Image.open(directory + 'wand.png'),
    'artillery': Image.open(directory + 'artillery.png'),
    'Superman': Image.open(directory + 'Superman.png'),
    'motivated': Image.open(directory + 'motivated.png'),
    'currency': Image.open(directory + 'currency.png'),
    'woodpecker': Image.open(directory + 'woodpecker.png'),
    'ceremony': Image.open(directory + 'ceremony.png'),
    'song': Image.open(directory + 'song.png'),
    'slalom': Image.open(directory + 'slalom.png'),
    'panpipe': Image.open(directory + 'panpipe.png'),
    'rhinoceros': Image.open(directory + 'rhinoceros.png'),
    'how': Image.open(directory + 'how.png'),
    'interview': Image.open(directory + 'interview.png'),
    'ancestor': Image.open(directory + 'ancestor.png'),
    'gamble': Image.open(directory + 'gamble.png'),
    'pizza': Image.open(directory + 'pizza.png'),
    'briefcase': Image.open(directory + 'briefcase.png'),
    'beauty': Image.open(directory + 'beauty.png'),
    'ladder': Image.open(directory + 'ladder.png'),
    'president': Image.open(directory + 'president.png'),
    'law': Image.open(directory + 'law.png'),
    'parallel': Image.open(directory + 'parallel.png'),
    'scarf': Image.open(directory + 'scarf.png'),
    'ambulance': Image.open(directory + 'ambulance.png'),
    'wind': Image.open(directory + 'wind.png'),
    'wine': Image.open(directory + 'wine.png'),
    'Brazil': Image.open(directory + 'Brazil.png'),
    'fetus': Image.open(directory + 'fetus.png'),
    'popsicle': Image.open(directory + 'popsicle.png'),
    'office': Image.open(directory + 'office.png'),
    'deck': Image.open(directory + 'deck.png'),
    'alternation': Image.open(directory + 'alternation.png'),
    'hibernation': Image.open(directory + 'hibernation.png'),
    'ewe': Image.open(directory + 'ewe.png'),
    'keyboard': Image.open(directory + 'keyboard.png'),
    'adolescence': Image.open(directory + 'adolescence.png'),
    'lifeline': Image.open(directory + 'lifeline.png'),
    'avocado': Image.open(directory + 'avocado.png'),
    'better': Image.open(directory + 'better.png'),
    'Spain': Image.open(directory + 'Spain.png'),
    'coffee': Image.open(directory + 'coffee.png'),
    'Judaism': Image.open(directory + 'Judaism.png'),
    'tourist': Image.open(directory + 'tourist.png'),
    'sterilization': Image.open(directory + 'sterilization.png'),
    'unemployed': Image.open(directory + 'unemployed.png'),
    'caterpillar': Image.open(directory + 'caterpillar.png'),
    'giraffe': Image.open(directory + 'giraffe.png'),
    'therapy': Image.open(directory + 'therapy.png'),
    'Asia': Image.open(directory + 'Asia.png'),
    'hydrotherapist': Image.open(directory + 'hydrotherapist.png'),
    'silver': Image.open(directory + 'silver.png'),
    'bank': Image.open(directory + 'bank.png'),
    'aport': Image.open(directory + 'aport.png'),
    'meat': Image.open(directory + 'meat.png'),
    'sleepless': Image.open(directory + 'sleepless.png'),
    'India': Image.open(directory + 'India.png'),
    'arrow': Image.open(directory + 'arrow.png'),
    'volcano': Image.open(directory + 'volcano.png'),
    'meal': Image.open(directory + 'meal.png'),
    'bone': Image.open(directory + 'bone.png'),
    'burial': Image.open(directory + 'burial.png'),
    'cartography': Image.open(directory + 'cartography.png'),
    'telescope': Image.open(directory + 'telescope.png'),
    'spider': Image.open(directory + 'spider.png'),
    'waffle': Image.open(directory + 'waffle.png'),
    'sukkah': Image.open(directory + 'sukkah.png'),
    'navy': Image.open(directory + 'navy.png'),
    'enclosure': Image.open(directory + 'enclosure.png'),
    'troublesome': Image.open(directory + 'troublesome.png'),
    'itch': Image.open(directory + 'itch.png'),
    'Sivan': Image.open(directory + 'Sivan.png'),
    'surprise': Image.open(directory + 'surprise.png'),
    'washer': Image.open(directory + 'washer.png'),
    'Tammuz': Image.open(directory + 'Tammuz.png'),
    'eternal': Image.open(directory + 'eternal.png'),
    'grapes': Image.open(directory + 'grapes.png'),
    'acrobat': Image.open(directory + 'acrobat.png'),
    'enormous': Image.open(directory + 'enormous.png'),
    'September': Image.open(directory + 'September.png'),
    'ritual': Image.open(directory + 'ritual.png'),
    'correctness': Image.open(directory + 'correctness.png'),
    'Torah': Image.open(directory + 'Torah.png'),
    'fuse': Image.open(directory + 'fuse.png'),
    'signature': Image.open(directory + 'signature.png'),
    'Antarctic': Image.open(directory + 'Antarctic.png'),
    'naughty': Image.open(directory + 'naughty.png'),
    'lovable': Image.open(directory + 'lovable.png'),
    'Buddhism': Image.open(directory + 'Buddhism.png'),
    'scissors': Image.open(directory + 'scissors.png'),
    'hoof': Image.open(directory + 'hoof.png'),
    'mercury': Image.open(directory + 'mercury.png'),
    'toy': Image.open(directory + 'toy.png'),
    'top': Image.open(directory + 'top.png'),
    'engagement': Image.open(directory + 'engagement.png'),
    'historian': Image.open(directory + 'historian.png'),
    'attack': Image.open(directory + 'attack.png'),
    'boating': Image.open(directory + 'boating.png'),
    'bitter': Image.open(directory + 'bitter.png'),
    'shallowness': Image.open(directory + 'shallowness.png'),
    'toe': Image.open(directory + 'toe.png'),
    'ceiling': Image.open(directory + 'ceiling.png'),
    'murder': Image.open(directory + 'murder.png'),
    'Spiderman': Image.open(directory + 'Spiderman.png'),
    'midsummer': Image.open(directory + 'midsummer.png'),
    'western': Image.open(directory + 'western.png'),
    'cereal': Image.open(directory + 'cereal.png'),
    'gambler': Image.open(directory + 'gambler.png'),
    'distance': Image.open(directory + 'distance.png'),
    'anxiety': Image.open(directory + 'anxiety.png'),
    'coward': Image.open(directory + 'coward.png'),
    'Allah': Image.open(directory + 'Allah.png'),
    'tree': Image.open(directory + 'tree.png'),
    'shower': Image.open(directory + 'shower.png'),
    'guilt': Image.open(directory + 'guilt.png'),
    'friend': Image.open(directory + 'friend.png'),
    'iron': Image.open(directory + 'iron.png'),
    'rag': Image.open(directory + 'rag.png'),
    'headmouse': Image.open(directory + 'headmouse.png'),
    'Moomintroll': Image.open(directory + 'Moomintroll.png'),
    'handkerchief': Image.open(directory + 'handkerchief.png'),
    'rattle': Image.open(directory + 'rattle.png'),
    'ram': Image.open(directory + 'ram.png'),
    'mine': Image.open(directory + 'mine.png'),
    'ginger': Image.open(directory + 'ginger.png'),
    'seed': Image.open(directory + 'seed.png'),
    'cipher': Image.open(directory + 'cipher.png'),
    'Shavuot': Image.open(directory + 'Shavuot.png'),
    'silversmith': Image.open(directory + 'silversmith.png'),
    'responsible': Image.open(directory + 'responsible.png'),
    'snow': Image.open(directory + 'snow.png'),
    'chest': Image.open(directory + 'chest.png'),
    'niece': Image.open(directory + 'niece.png'),
    'Lakshmi': Image.open(directory + 'Lakshmi.png'),
    'snowflake': Image.open(directory + 'snowflake.png'),
    'stirrup': Image.open(directory + 'stirrup.png'),
    'milkman': Image.open(directory + 'milkman.png'),
    'mouth': Image.open(directory + 'mouth.png'),
    'Brontosaurus': Image.open(directory + 'Brontosaurus.png'),
    'coin': Image.open(directory + 'coin.png'),
    'the': Image.open(directory + 'the.png'),
    'grave': Image.open(directory + 'grave.png'),
    'glow': Image.open(directory + 'glow.png'),
    'singer': Image.open(directory + 'singer.png'),
    'chemistry': Image.open(directory + 'chemistry.png'),
    'observation': Image.open(directory + 'observation.png'),
    'grove': Image.open(directory + 'grove.png'),
    'alarm': Image.open(directory + 'alarm.png'),
    'camp': Image.open(directory + 'camp.png'),
    'metal': Image.open(directory + 'metal.png'),
    'storm': Image.open(directory + 'storm.png'),
    'aunt': Image.open(directory + 'aunt.png'),
    'pineapple': Image.open(directory + 'pineapple.png'),
    'dot': Image.open(directory + 'dot.png'),
    'currants': Image.open(directory + 'currants.png'),
    'queen': Image.open(directory + 'queen.png'),
    'barley': Image.open(directory + 'barley.png'),
    'gauge': Image.open(directory + 'gauge.png'),
    'nephew': Image.open(directory + 'nephew.png'),
    'toast': Image.open(directory + 'toast.png'),
    'vasectomy': Image.open(directory + 'vasectomy.png'),
    'geyser': Image.open(directory + 'geyser.png'),
    'shellfish': Image.open(directory + 'shellfish.png'),
    'acne': Image.open(directory + 'acne.png'),
    'maturation': Image.open(directory + 'maturation.png'),
    'Frey': Image.open(directory + 'Frey.png'),
    'geologist': Image.open(directory + 'geologist.png'),
    'polenta': Image.open(directory + 'polenta.png'),
    'folder': Image.open(directory + 'folder.png'),
    'rice': Image.open(directory + 'rice.png'),
    'Elul': Image.open(directory + 'Elul.png'),
    'personality': Image.open(directory + 'personality.png'),
    'mixture': Image.open(directory + 'mixture.png'),
    'sunglasses': Image.open(directory + 'sunglasses.png'),
    'pocket': Image.open(directory + 'pocket.png'),
    'boathouse': Image.open(directory + 'boathouse.png'),
    'cushion': Image.open(directory + 'cushion.png'),
    'jaguar': Image.open(directory + 'jaguar.png'),
    'rowing': Image.open(directory + 'rowing.png'),
    'disco': Image.open(directory + 'disco.png'),
    'microscope': Image.open(directory + 'microscope.png'),
    'linguist': Image.open(directory + 'linguist.png'),
    'steam': Image.open(directory + 'steam.png'),
    'secretary': Image.open(directory + 'secretary.png'),
    'uninhabited': Image.open(directory + 'uninhabited.png'),
    'nut': Image.open(directory + 'nut.png'),
    'lemonade': Image.open(directory + 'lemonade.png'),
    'Christianity': Image.open(directory + 'Christianity.png'),
    'best': Image.open(directory + 'best.png'),
    'sail': Image.open(directory + 'sail.png'),
    'continent': Image.open(directory + 'continent.png'),
    'Purim': Image.open(directory + 'Purim.png'),
    'score': Image.open(directory + 'score.png'),
    'finger': Image.open(directory + 'finger.png'),
    'approach': Image.open(directory + 'approach.png'),
    'pirate': Image.open(directory + 'pirate.png'),
    'amplitude': Image.open(directory + 'amplitude.png'),
    'weak': Image.open(directory + 'weak.png'),
    'termite': Image.open(directory + 'termite.png'),
    'vestment': Image.open(directory + 'vestment.png'),
    'toothbrush': Image.open(directory + 'toothbrush.png'),
    'mezuzah': Image.open(directory + 'mezuzah.png'),
    'cousin': Image.open(directory + 'cousin.png'),
    'horsehair': Image.open(directory + 'horsehair.png'),
    'kitchen': Image.open(directory + 'kitchen.png'),
    'climate': Image.open(directory + 'climate.png'),
    'accident': Image.open(directory + 'accident.png'),
    'cow': Image.open(directory + 'cow.png'),
    'revelry': Image.open(directory + 'revelry.png'),
    'incense': Image.open(directory + 'incense.png'),
    'hummus': Image.open(directory + 'hummus.png'),
    'cod': Image.open(directory + 'cod.png'),
    'receiver': Image.open(directory + 'receiver.png'),
    'pita': Image.open(directory + 'pita.png'),
    'betting': Image.open(directory + 'betting.png'),
    'lullaby': Image.open(directory + 'lullaby.png'),
    'Ireland': Image.open(directory + 'Ireland.png'),
    'pregnancy': Image.open(directory + 'pregnancy.png'),
    'lighthouse': Image.open(directory + 'lighthouse.png'),
    'tallith': Image.open(directory + 'tallith.png'),
    'beef': Image.open(directory + 'beef.png'),
    'Sandman': Image.open(directory + 'Sandman.png'),
    'beer': Image.open(directory + 'beer.png'),
    'grapefruit': Image.open(directory + 'grapefruit.png'),
    'beet': Image.open(directory + 'beet.png'),
    'interest': Image.open(directory + 'interest.png'),
    'pancreas': Image.open(directory + 'pancreas.png'),
    'website': Image.open(directory + 'website.png'),
    'life': Image.open(directory + 'life.png'),
    'mushroom': Image.open(directory + 'mushroom.png'),
    'eastern': Image.open(directory + 'eastern.png'),
    'paraskiing': Image.open(directory + 'paraskiing.png'),
    'Poland': Image.open(directory + 'Poland.png'),
    'worker': Image.open(directory + 'worker.png'),
    'bladder': Image.open(directory + 'bladder.png'),
    'CD': Image.open(directory + 'CD.png'),
    'craft': Image.open(directory + 'craft.png'),
    'toboggan': Image.open(directory + 'toboggan.png'),
    'westward': Image.open(directory + 'westward.png'),
    'glider': Image.open(directory + 'glider.png'),
    'tide': Image.open(directory + 'tide.png'),
    'tank': Image.open(directory + 'tank.png'),
    'sheath': Image.open(directory + 'sheath.png'),
    'voice': Image.open(directory + 'voice.png'),
    'anchor': Image.open(directory + 'anchor.png'),
    'pyramid': Image.open(directory + 'pyramid.png'),
    'canoeing': Image.open(directory + 'canoeing.png'),
    'equator': Image.open(directory + 'equator.png'),
    'challah': Image.open(directory + 'challah.png'),
    'it': Image.open(directory + 'it.png'),
    'shame': Image.open(directory + 'shame.png'),
    'tissue': Image.open(directory + 'tissue.png'),
    'cone': Image.open(directory + 'cone.png'),
    'violin': Image.open(directory + 'violin.png'),
    'mouse': Image.open(directory + 'mouse.png'),
    'if': Image.open(directory + 'if.png'),
    'bricklayer': Image.open(directory + 'bricklayer.png'),
    'toaster': Image.open(directory + 'toaster.png'),
    'forehead': Image.open(directory + 'forehead.png'),
    'several': Image.open(directory + 'several.png'),
    'wheel': Image.open(directory + 'wheel.png'),
    'independent': Image.open(directory + 'independent.png'),
    'satellite': Image.open(directory + 'satellite.png'),
    'conversion': Image.open(directory + 'conversion.png'),
    'rain': Image.open(directory + 'rain.png'),
    'hand': Image.open(directory + 'hand.png'),
    'waterfall': Image.open(directory + 'waterfall.png'),
    'garlic': Image.open(directory + 'garlic.png'),
    'unicorn': Image.open(directory + 'unicorn.png'),
    'jealous': Image.open(directory + 'jealous.png'),
    'Sleipnir': Image.open(directory + 'Sleipnir.png'),
    'paediatrician': Image.open(directory + 'paediatrician.png'),
    'butter': Image.open(directory + 'butter.png'),
    'tombstone': Image.open(directory + 'tombstone.png'),
    'juridical': Image.open(directory + 'juridical.png'),
    'musical': Image.open(directory + 'musical.png'),
    'left': Image.open(directory + 'left.png'),
    'snowman': Image.open(directory + 'snowman.png'),
    'indigo': Image.open(directory + 'indigo.png'),
    'unemployment': Image.open(directory + 'unemployment.png'),
    'laptop': Image.open(directory + 'laptop.png'),
    'sleepy': Image.open(directory + 'sleepy.png'),
    'stepdaughter': Image.open(directory + 'stepdaughter.png'),
    'cervix': Image.open(directory + 'cervix.png'),
    'starboard': Image.open(directory + 'starboard.png'),
    'sunflower': Image.open(directory + 'sunflower.png'),
    'royal': Image.open(directory + 'royal.png'),
    'passive': Image.open(directory + 'passive.png'),
    'hay': Image.open(directory + 'hay.png'),
    'board': Image.open(directory + 'board.png'),
    'east': Image.open(directory + 'east.png'),
    'turquoise': Image.open(directory + 'turquoise.png'),
    'menorah': Image.open(directory + 'menorah.png'),
    'scrotum': Image.open(directory + 'scrotum.png'),
    'Freya': Image.open(directory + 'Freya.png'),
    'vulture': Image.open(directory + 'vulture.png'),
    'possible': Image.open(directory + 'possible.png'),
    'paratrooper': Image.open(directory + 'paratrooper.png'),
    'birth': Image.open(directory + 'birth.png'),
    'judge': Image.open(directory + 'judge.png'),
    'shoulder': Image.open(directory + 'shoulder.png'),
    'specific': Image.open(directory + 'specific.png'),
    'mosquito': Image.open(directory + 'mosquito.png'),
    'night': Image.open(directory + 'night.png'),
    'starvation': Image.open(directory + 'starvation.png'),
    'cowardice': Image.open(directory + 'cowardice.png'),
    'right': Image.open(directory + 'right.png'),
    'old': Image.open(directory + 'old.png'),
    'Bangladesh': Image.open(directory + 'Bangladesh.png'),
    'crown': Image.open(directory + 'crown.png'),
    'invoice': Image.open(directory + 'invoice.png'),
    'escape': Image.open(directory + 'escape.png'),
    'dear': Image.open(directory + 'dear.png'),
    'unless': Image.open(directory + 'unless.png'),
    'harassment': Image.open(directory + 'harassment.png'),
    'sociology': Image.open(directory + 'sociology.png'),
    'fox': Image.open(directory + 'fox.png'),
    'ice': Image.open(directory + 'ice.png'),
    'creative': Image.open(directory + 'creative.png'),
    'track': Image.open(directory + 'track.png'),
    'fog': Image.open(directory + 'fog.png'),
    'participation': Image.open(directory + 'participation.png'),
    'peel': Image.open(directory + 'peel.png'),
    'deflation': Image.open(directory + 'deflation.png'),
    'corn': Image.open(directory + 'corn.png'),
    'trampoline': Image.open(directory + 'trampoline.png'),
    'illustration': Image.open(directory + 'illustration.png'),
    'discount': Image.open(directory + 'discount.png'),
    'Sweden': Image.open(directory + 'Sweden.png'),
    'menopause': Image.open(directory + 'menopause.png'),
    'peer': Image.open(directory + 'peer.png'),
    'pliers': Image.open(directory + 'pliers.png'),
    'plug': Image.open(directory + 'plug.png'),
    'foreskin': Image.open(directory + 'foreskin.png'),
    'empowerment': Image.open(directory + 'empowerment.png'),
    'eaves': Image.open(directory + 'eaves.png'),
    'coral': Image.open(directory + 'coral.png'),
    'Austria': Image.open(directory + 'Austria.png'),
    'storeroom': Image.open(directory + 'storeroom.png'),
    'seaplane': Image.open(directory + 'seaplane.png'),
    'horizon': Image.open(directory + 'horizon.png'),
    'leprechaun': Image.open(directory + 'leprechaun.png'),
    'octopus': Image.open(directory + 'octopus.png'),
    'nerve': Image.open(directory + 'nerve.png'),
    'digestion': Image.open(directory + 'digestion.png'),
    'dilemma': Image.open(directory + 'dilemma.png'),
    'yen': Image.open(directory + 'yen.png'),
    'Scotland': Image.open(directory + 'Scotland.png'),
    'son': Image.open(directory + 'son.png'),
    'prisoner': Image.open(directory + 'prisoner.png'),
    'fuselage': Image.open(directory + 'fuselage.png'),
    'librarian': Image.open(directory + 'librarian.png'),
    'electorate': Image.open(directory + 'electorate.png'),
    'piglet': Image.open(directory + 'piglet.png'),
    'Woden': Image.open(directory + 'Woden.png'),
    'flying': Image.open(directory + 'flying.png'),
    'wildflower': Image.open(directory + 'wildflower.png'),
    'way': Image.open(directory + 'way.png'),
    'war': Image.open(directory + 'war.png'),
    'fork': Image.open(directory + 'fork.png'),
    'head': Image.open(directory + 'head.png'),
    'deaf': Image.open(directory + 'deaf.png'),
    'failure': Image.open(directory + 'failure.png'),
    'heat': Image.open(directory + 'heat.png'),
    'uncle': Image.open(directory + 'uncle.png'),
    'blindness': Image.open(directory + 'blindness.png'),
    'crystal': Image.open(directory + 'crystal.png'),
    'veterinarian': Image.open(directory + 'veterinarian.png'),
    'passenger': Image.open(directory + 'passenger.png'),
    'evidence': Image.open(directory + 'evidence.png'),
    'trombone': Image.open(directory + 'trombone.png'),
    'Sif': Image.open(directory + 'Sif.png'),
    'prayer': Image.open(directory + 'prayer.png'),
    'crutches': Image.open(directory + 'crutches.png'),
    'relay': Image.open(directory + 'relay.png'),
    'dotted': Image.open(directory + 'dotted.png'),
    'Tibet': Image.open(directory + 'Tibet.png'),
    'glacier': Image.open(directory + 'glacier.png'),
    'foremother': Image.open(directory + 'foremother.png'),
    'meteorology': Image.open(directory + 'meteorology.png'),
    'when': Image.open(directory + 'when.png'),
    'ammeter': Image.open(directory + 'ammeter.png'),
    'reality': Image.open(directory + 'reality.png'),
    'flood': Image.open(directory + 'flood.png'),
    'tin': Image.open(directory + 'tin.png'),
    'republic': Image.open(directory + 'republic.png'),
    'holding': Image.open(directory + 'holding.png'),
    'digital': Image.open(directory + 'digital.png'),
    'leek': Image.open(directory + 'leek.png'),
    'steamship': Image.open(directory + 'steamship.png'),
    'welcome': Image.open(directory + 'welcome.png'),
    'diet': Image.open(directory + 'diet.png'),
    'Koran': Image.open(directory + 'Koran.png'),
    'exported': Image.open(directory + 'exported.png'),
    'weekend': Image.open(directory + 'weekend.png'),
    'longer': Image.open(directory + 'longer.png'),
    'potato': Image.open(directory + 'potato.png'),
    'navel': Image.open(directory + 'navel.png'),
    'broadband': Image.open(directory + 'broadband.png'),
    'reception': Image.open(directory + 'reception.png'),
    'time': Image.open(directory + 'time.png'),
    'peacock': Image.open(directory + 'peacock.png'),
    'chain': Image.open(directory + 'chain.png'),
    'avalanche': Image.open(directory + 'avalanche.png'),
    'skin': Image.open(directory + 'skin.png'),
    'milk': Image.open(directory + 'milk.png'),
    'devoted': Image.open(directory + 'devoted.png'),
    'ballet': Image.open(directory + 'ballet.png'),
    'suicide': Image.open(directory + 'suicide.png'),
    'crater': Image.open(directory + 'crater.png'),
    'environment': Image.open(directory + 'environment.png'),
    'tracker': Image.open(directory + 'tracker.png'),
    'melon': Image.open(directory + 'melon.png'),
    'division': Image.open(directory + 'division.png'),
    'Sukkot': Image.open(directory + 'Sukkot.png'),
    'yeast': Image.open(directory + 'yeast.png'),
    'kitten': Image.open(directory + 'kitten.png'),
    'trouble': Image.open(directory + 'trouble.png'),
    'minute': Image.open(directory + 'minute.png'),
    'tricycle': Image.open(directory + 'tricycle.png'),
    'Kali': Image.open(directory + 'Kali.png'),
    'brother': Image.open(directory + 'brother.png'),
    'cloudy': Image.open(directory + 'cloudy.png'),
    'magnet': Image.open(directory + 'magnet.png'),
    'excellence': Image.open(directory + 'excellence.png'),
    'team': Image.open(directory + 'team.png'),
    'attic': Image.open(directory + 'attic.png'),
    'crescent': Image.open(directory + 'crescent.png'),
    'parachuting': Image.open(directory + 'parachuting.png'),
    'headset': Image.open(directory + 'headset.png'),
    'constitution': Image.open(directory + 'constitution.png'),
    'uniform': Image.open(directory + 'uniform.png'),
    'current': Image.open(directory + 'current.png'),
    'agnosticism': Image.open(directory + 'agnosticism.png'),
    'international': Image.open(directory + 'international.png'),
    'jury': Image.open(directory + 'jury.png'),
    'clerk': Image.open(directory + 'clerk.png'),
    'makeup': Image.open(directory + 'makeup.png'),
    'agreement': Image.open(directory + 'agreement.png'),
    'magnetism': Image.open(directory + 'magnetism.png'),
    'witch': Image.open(directory + 'witch.png'),
    'address': Image.open(directory + 'address.png'),
    'earthquake': Image.open(directory + 'earthquake.png'),
    'alto': Image.open(directory + 'alto.png'),
    'zombie': Image.open(directory + 'zombie.png'),
    'swash': Image.open(directory + 'swash.png'),
    'Portugal': Image.open(directory + 'Portugal.png'),
    'guilty': Image.open(directory + 'guilty.png'),
    'bow': Image.open(directory + 'bow.png'),
    'trial': Image.open(directory + 'trial.png'),
    'cinnamon': Image.open(directory + 'cinnamon.png'),
    'raccoon': Image.open(directory + 'raccoon.png'),
    'massage': Image.open(directory + 'massage.png'),
    'homeward': Image.open(directory + 'homeward.png'),
    'schach': Image.open(directory + 'schach.png'),
    'retired': Image.open(directory + 'retired.png'),
    'hiking': Image.open(directory + 'hiking.png'),
    'radish': Image.open(directory + 'radish.png'),
    'kayak': Image.open(directory + 'kayak.png'),
    'snowboard': Image.open(directory + 'snowboard.png'),
    'ache': Image.open(directory + 'ache.png'),
    'embarrassing': Image.open(directory + 'embarrassing.png'),
    'crime': Image.open(directory + 'crime.png'),
    'market': Image.open(directory + 'market.png'),
    'Australia': Image.open(directory + 'Australia.png'),
    'August': Image.open(directory + 'August.png'),
    'runes': Image.open(directory + 'runes.png'),
    'positive': Image.open(directory + 'positive.png'),
    'gallop': Image.open(directory + 'gallop.png'),
    'visit': Image.open(directory + 'visit.png'),
    'wicket': Image.open(directory + 'wicket.png'),
    'memory': Image.open(directory + 'memory.png'),
    'today': Image.open(directory + 'today.png'),
    'October': Image.open(directory + 'October.png'),
    'club': Image.open(directory + 'club.png'),
    'clitoris': Image.open(directory + 'clitoris.png'),
    'Eve': Image.open(directory + 'Eve.png'),
    'chocolate': Image.open(directory + 'chocolate.png'),
    'employee': Image.open(directory + 'employee.png'),
    'olive': Image.open(directory + 'olive.png'),
    'prophecy': Image.open(directory + 'prophecy.png'),
    'fly': Image.open(directory + 'fly.png'),
    'judo': Image.open(directory + 'judo.png'),
    'Pope': Image.open(directory + 'Pope.png'),
    'lumberjack': Image.open(directory + 'lumberjack.png'),
    'cap': Image.open(directory + 'cap.png'),
    'soul': Image.open(directory + 'soul.png'),
    'believer': Image.open(directory + 'believer.png'),
    'sandstorm': Image.open(directory + 'sandstorm.png'),
    'ferry': Image.open(directory + 'ferry.png'),
    'meatball': Image.open(directory + 'meatball.png'),
    'heart': Image.open(directory + 'heart.png'),
    'reflector': Image.open(directory + 'reflector.png'),
    'sense': Image.open(directory + 'sense.png'),
    'parachute': Image.open(directory + 'parachute.png'),
    'drawer': Image.open(directory + 'drawer.png'),
    'matzo': Image.open(directory + 'matzo.png'),
    'chin': Image.open(directory + 'chin.png'),
    'boules': Image.open(directory + 'boules.png'),
    'lulav': Image.open(directory + 'lulav.png'),
    'divided': Image.open(directory + 'divided.png'),
    'freezer': Image.open(directory + 'freezer.png'),
    'elephant': Image.open(directory + 'elephant.png'),
    'tile': Image.open(directory + 'tile.png'),
    'persuasion': Image.open(directory + 'persuasion.png'),
    'testicle': Image.open(directory + 'testicle.png'),
    'afternoon': Image.open(directory + 'afternoon.png'),
    'map': Image.open(directory + 'map.png'),
    'information': Image.open(directory + 'information.png'),
    'sacrifice': Image.open(directory + 'sacrifice.png'),
    'southern': Image.open(directory + 'southern.png'),
    'accessory': Image.open(directory + 'accessory.png'),
    'birthday': Image.open(directory + 'birthday.png'),
    'tablecloth': Image.open(directory + 'tablecloth.png'),
    'headscarf': Image.open(directory + 'headscarf.png'),
    'jellyfish': Image.open(directory + 'jellyfish.png'),
    'classroom': Image.open(directory + 'classroom.png'),
    'stress': Image.open(directory + 'stress.png'),
    'waist': Image.open(directory + 'waist.png'),
    'liquid': Image.open(directory + 'liquid.png'),
    'curry': Image.open(directory + 'curry.png'),
    'wheelchair': Image.open(directory + 'wheelchair.png'),
    'switch': Image.open(directory + 'switch.png'),
    'mango': Image.open(directory + 'mango.png'),
    'Islam': Image.open(directory + 'Islam.png'),
    'archeologist': Image.open(directory + 'archeologist.png'),
    'spitting': Image.open(directory + 'spitting.png'),
    'midnight': Image.open(directory + 'midnight.png'),
    'pillowcase': Image.open(directory + 'pillowcase.png'),
    'Loki': Image.open(directory + 'Loki.png'),
    'brain': Image.open(directory + 'brain.png'),
    'cold': Image.open(directory + 'cold.png'),
    'pointer': Image.open(directory + 'pointer.png'),
    'group': Image.open(directory + 'group.png'),
    'thumb': Image.open(directory + 'thumb.png'),
    'accordion': Image.open(directory + 'accordion.png'),
    'chalice': Image.open(directory + 'chalice.png'),
    'shofar': Image.open(directory + 'shofar.png'),
    'window': Image.open(directory + 'window.png'),
    'farmer': Image.open(directory + 'farmer.png'),
    'hamentasch': Image.open(directory + 'hamentasch.png'),
    'rake': Image.open(directory + 'rake.png'),
    'insomnia': Image.open(directory + 'insomnia.png'),
    'nation': Image.open(directory + 'nation.png'),
    'now': Image.open(directory + 'now.png'),
    'ketchup': Image.open(directory + 'ketchup.png'),
    'nor': Image.open(directory + 'nor.png'),
    'barrow': Image.open(directory + 'barrow.png'),
    'opera': Image.open(directory + 'opera.png'),
    'drop': Image.open(directory + 'drop.png'),
    'France': Image.open(directory + 'France.png'),
    'fisherman': Image.open(directory + 'fisherman.png'),
    'sow': Image.open(directory + 'sow.png'),
    'ejaculation': Image.open(directory + 'ejaculation.png'),
    'bookshop': Image.open(directory + 'bookshop.png'),
    'woodcraft': Image.open(directory + 'woodcraft.png'),
    'zebra': Image.open(directory + 'zebra.png'),
    'beetle': Image.open(directory + 'beetle.png'),
    'girl': Image.open(directory + 'girl.png'),
    'sunrise': Image.open(directory + 'sunrise.png'),
    'troll': Image.open(directory + 'troll.png'),
    'opener': Image.open(directory + 'opener.png'),
    'receiving': Image.open(directory + 'receiving.png'),
    'monster': Image.open(directory + 'monster.png'),
    'possibility': Image.open(directory + 'possibility.png'),
    'flyer': Image.open(directory + 'flyer.png'),
    'ajar': Image.open(directory + 'ajar.png'),
    'notary': Image.open(directory + 'notary.png'),
    'inhaler': Image.open(directory + 'inhaler.png'),
    'card': Image.open(directory + 'card.png'),
    'language': Image.open(directory + 'language.png'),
    'bisexuality': Image.open(directory + 'bisexuality.png'),
    'ostrich': Image.open(directory + 'ostrich.png'),
    'swing': Image.open(directory + 'swing.png'),
    'blacksmith': Image.open(directory + 'blacksmith.png'),
    'Hungary': Image.open(directory + 'Hungary.png'),
    'promotion': Image.open(directory + 'promotion.png'),
    'adventure': Image.open(directory + 'adventure.png'),
    'blind': Image.open(directory + 'blind.png'),
    'pelican': Image.open(directory + 'pelican.png'),
    'intuition': Image.open(directory + 'intuition.png'),
    'audiologist': Image.open(directory + 'audiologist.png'),
    'pushboat': Image.open(directory + 'pushboat.png'),
    'fast': Image.open(directory + 'fast.png'),
    'ring': Image.open(directory + 'ring.png'),
    'open': Image.open(directory + 'open.png'),
    'tomorrow': Image.open(directory + 'tomorrow.png'),
    'size': Image.open(directory + 'size.png'),
    'sheep': Image.open(directory + 'sheep.png'),
    'checked': Image.open(directory + 'checked.png'),
    'silent': Image.open(directory + 'silent.png'),
    'plastic': Image.open(directory + 'plastic.png'),
    'white': Image.open(directory + 'white.png'),
    'west': Image.open(directory + 'west.png'),
    'mermaid': Image.open(directory + 'mermaid.png'),
    'anus': Image.open(directory + 'anus.png'),
    'addict': Image.open(directory + 'addict.png'),
    'starfish': Image.open(directory + 'starfish.png'),
    'season': Image.open(directory + 'season.png'),
    'osteopath': Image.open(directory + 'osteopath.png'),
    'boyfriend': Image.open(directory + 'boyfriend.png'),
    'television': Image.open(directory + 'television.png'),
    'iceberg': Image.open(directory + 'iceberg.png'),
    'sailing': Image.open(directory + 'sailing.png'),
    'oats': Image.open(directory + 'oats.png'),
    'future': Image.open(directory + 'future.png'),
    'gigantic': Image.open(directory + 'gigantic.png'),
    'tractor': Image.open(directory + 'tractor.png'),
    'physiotherapist': Image.open(directory + 'physiotherapist.png'),
    'coconut': Image.open(directory + 'coconut.png'),
    'Shiva': Image.open(directory + 'Shiva.png'),
    'generalization': Image.open(directory + 'generalization.png'),
    'ant': Image.open(directory + 'ant.png'),
    'rent': Image.open(directory + 'rent.png'),
    'breakfast': Image.open(directory + 'breakfast.png'),
    'sap': Image.open(directory + 'sap.png'),
    'saw': Image.open(directory + 'saw.png'),
    'lumpy': Image.open(directory + 'lumpy.png'),
    'Jewish': Image.open(directory + 'Jewish.png'),
    'Tishri': Image.open(directory + 'Tishri.png'),
    'zoo': Image.open(directory + 'zoo.png'),
    'endangered': Image.open(directory + 'endangered.png'),
    'thermometer': Image.open(directory + 'thermometer.png'),
    'glassware': Image.open(directory + 'glassware.png'),
    'Kazakhstan': Image.open(directory + 'Kazakhstan.png'),
    'Hemulen': Image.open(directory + 'Hemulen.png'),
    'theatre': Image.open(directory + 'theatre.png'),
    'kibbutz': Image.open(directory + 'kibbutz.png'),
    'zigzag': Image.open(directory + 'zigzag.png'),
    'pair': Image.open(directory + 'pair.png'),
    'knee': Image.open(directory + 'knee.png'),
    'bluebird': Image.open(directory + 'bluebird.png'),
    'voluntary': Image.open(directory + 'voluntary.png'),
    'tendon': Image.open(directory + 'tendon.png'),
    'proud': Image.open(directory + 'proud.png'),
    'sale': Image.open(directory + 'sale.png'),
    'tooth': Image.open(directory + 'tooth.png'),
    'sunset': Image.open(directory + 'sunset.png'),
    'hedgehog': Image.open(directory + 'hedgehog.png'),
    'salt': Image.open(directory + 'salt.png'),
    'masturbation': Image.open(directory + 'masturbation.png'),
    'cornea': Image.open(directory + 'cornea.png'),
    'recipe': Image.open(directory + 'recipe.png'),
    'bright': Image.open(directory + 'bright.png'),
    'therapist': Image.open(directory + 'therapist.png'),
    'shoe': Image.open(directory + 'shoe.png'),
    'corner': Image.open(directory + 'corner.png'),
    'blissymbol': Image.open(directory + 'blissymbol.png'),
    'geography': Image.open(directory + 'geography.png'),
    'pump': Image.open(directory + 'pump.png'),
    'either': Image.open(directory + 'either.png'),
    'liberation': Image.open(directory + 'liberation.png'),
    'Pegasus': Image.open(directory + 'Pegasus.png'),
    'wool': Image.open(directory + 'wool.png'),
    'psychiatrist': Image.open(directory + 'psychiatrist.png'),
    'July': Image.open(directory + 'July.png'),
    'artist': Image.open(directory + 'artist.png'),
    'leather': Image.open(directory + 'leather.png'),
    'through': Image.open(directory + 'through.png'),
    'where': Image.open(directory + 'where.png'),
    'husband': Image.open(directory + 'husband.png'),
    'picnic': Image.open(directory + 'picnic.png'),
    'concert': Image.open(directory + 'concert.png'),
    'masseur': Image.open(directory + 'masseur.png'),
    'asleep': Image.open(directory + 'asleep.png'),
    'seal': Image.open(directory + 'seal.png'),
    'calendar': Image.open(directory + 'calendar.png'),
    'sport': Image.open(directory + 'sport.png'),
    'stepson': Image.open(directory + 'stepson.png'),
    'loudspeaker': Image.open(directory + 'loudspeaker.png'),
    'vertical': Image.open(directory + 'vertical.png'),
    'dressage': Image.open(directory + 'dressage.png'),
    'opening': Image.open(directory + 'opening.png'),
    'enough': Image.open(directory + 'enough.png'),
    'skyscraper': Image.open(directory + 'skyscraper.png'),
    'between': Image.open(directory + 'between.png'),
    'import': Image.open(directory + 'import.png'),
    'reading': Image.open(directory + 'reading.png'),
    'across': Image.open(directory + 'across.png'),
    'parent': Image.open(directory + 'parent.png'),
    'January': Image.open(directory + 'January.png'),
    'spark': Image.open(directory + 'spark.png'),
    'comb': Image.open(directory + 'comb.png'),
    'reaction': Image.open(directory + 'reaction.png'),
    'etrog': Image.open(directory + 'etrog.png'),
    'berry': Image.open(directory + 'berry.png'),
    'comet': Image.open(directory + 'comet.png'),
    'Snufkin': Image.open(directory + 'Snufkin.png'),
    'sulky': Image.open(directory + 'sulky.png'),
    'cancer': Image.open(directory + 'cancer.png'),
    'kazoo': Image.open(directory + 'kazoo.png'),
    'accusation': Image.open(directory + 'accusation.png'),
    'Norway': Image.open(directory + 'Norway.png'),
    'colon': Image.open(directory + 'colon.png'),
    'polo': Image.open(directory + 'polo.png'),
    'pod': Image.open(directory + 'pod.png'),
    'mare': Image.open(directory + 'mare.png'),
    'cycling': Image.open(directory + 'cycling.png'),
    'toothpaste': Image.open(directory + 'toothpaste.png'),
    'undershirt': Image.open(directory + 'undershirt.png'),
    'breath': Image.open(directory + 'breath.png'),
    'dictator': Image.open(directory + 'dictator.png'),
    'helicopter': Image.open(directory + 'helicopter.png'),
    'ravioli': Image.open(directory + 'ravioli.png'),
    'tasteless': Image.open(directory + 'tasteless.png'),
    'singalong': Image.open(directory + 'singalong.png'),
    'tiger': Image.open(directory + 'tiger.png'),
    'polytheism': Image.open(directory + 'polytheism.png'),
    'stovetop': Image.open(directory + 'stovetop.png'),
    'careful': Image.open(directory + 'careful.png'),
    'spirit': Image.open(directory + 'spirit.png'),
    'robber': Image.open(directory + 'robber.png'),
    'pilot': Image.open(directory + 'pilot.png'),
    'sound': Image.open(directory + 'sound.png'),
    'gland': Image.open(directory + 'gland.png'),
    'these': Image.open(directory + 'these.png'),
    'stepfather': Image.open(directory + 'stepfather.png'),
    'canoe': Image.open(directory + 'canoe.png'),
    'engaged': Image.open(directory + 'engaged.png'),
    'telephone': Image.open(directory + 'telephone.png'),
    'return': Image.open(directory + 'return.png'),
    'technology': Image.open(directory + 'technology.png'),
    'worry': Image.open(directory + 'worry.png'),
    'helmet': Image.open(directory + 'helmet.png'),
    'Israel': Image.open(directory + 'Israel.png'),
    'synagogue': Image.open(directory + 'synagogue.png'),
    'participant': Image.open(directory + 'participant.png'),
    'projector': Image.open(directory + 'projector.png'),
    'paw': Image.open(directory + 'paw.png'),
    'gelding': Image.open(directory + 'gelding.png'),
    'macaroni': Image.open(directory + 'macaroni.png'),
    'workplace': Image.open(directory + 'workplace.png'),
    'week': Image.open(directory + 'week.png'),
    'baguette': Image.open(directory + 'baguette.png'),
    'foal': Image.open(directory + 'foal.png'),
    'cymbal': Image.open(directory + 'cymbal.png'),
    'running': Image.open(directory + 'running.png'),
    'fruit': Image.open(directory + 'fruit.png'),
    'advertisement': Image.open(directory + 'advertisement.png'),
    'footprint': Image.open(directory + 'footprint.png'),
    'teetotalism': Image.open(directory + 'teetotalism.png'),
    'floor': Image.open(directory + 'floor.png'),
    'Ramadan': Image.open(directory + 'Ramadan.png'),
    'Latvia': Image.open(directory + 'Latvia.png'),
    'breeze': Image.open(directory + 'breeze.png'),
    'veal': Image.open(directory + 'veal.png'),
    'joystick': Image.open(directory + 'joystick.png'),
    'sinner': Image.open(directory + 'sinner.png'),
    'summer': Image.open(directory + 'summer.png'),
    'anemometer': Image.open(directory + 'anemometer.png'),
    'scabies': Image.open(directory + 'scabies.png'),
    'misuse': Image.open(directory + 'misuse.png'),
    'steamer': Image.open(directory + 'steamer.png'),
    'actor': Image.open(directory + 'actor.png'),
    'speed': Image.open(directory + 'speed.png'),
    'blot': Image.open(directory + 'blot.png'),
    'mandolin': Image.open(directory + 'mandolin.png'),
    'rose': Image.open(directory + 'rose.png'),
    'improvement': Image.open(directory + 'improvement.png'),
    'bioenergy': Image.open(directory + 'bioenergy.png'),
    'treatment': Image.open(directory + 'treatment.png'),
    'armchair': Image.open(directory + 'armchair.png'),
    'around': Image.open(directory + 'around.png'),
    'dart': Image.open(directory + 'dart.png'),
    'dark': Image.open(directory + 'dark.png'),
    'inflation': Image.open(directory + 'inflation.png'),
    'traffic': Image.open(directory + 'traffic.png'),
    'world': Image.open(directory + 'world.png'),
    'furniture': Image.open(directory + 'furniture.png'),
    'towel': Image.open(directory + 'towel.png'),
    'stranger': Image.open(directory + 'stranger.png'),
    'postcard': Image.open(directory + 'postcard.png'),
    'nosy': Image.open(directory + 'nosy.png'),
    'bracelet': Image.open(directory + 'bracelet.png'),
    'homosexuality': Image.open(directory + 'homosexuality.png'),
    'miracle': Image.open(directory + 'miracle.png'),
    'lightning': Image.open(directory + 'lightning.png'),
    'tsunami': Image.open(directory + 'tsunami.png'),
    'nose': Image.open(directory + 'nose.png'),
    'tower': Image.open(directory + 'tower.png'),
    'doll': Image.open(directory + 'doll.png'),
    'pickled': Image.open(directory + 'pickled.png'),
    'boar': Image.open(directory + 'boar.png'),
    'astronomer': Image.open(directory + 'astronomer.png'),
    'lobster': Image.open(directory + 'lobster.png'),
    'pasture': Image.open(directory + 'pasture.png'),
    'spasm': Image.open(directory + 'spasm.png'),
    'slice': Image.open(directory + 'slice.png'),
    'mood': Image.open(directory + 'mood.png'),
    'noon': Image.open(directory + 'noon.png'),
    'legal': Image.open(directory + 'legal.png'),
    'moon': Image.open(directory + 'moon.png'),
    'babysitter': Image.open(directory + 'babysitter.png'),
    'recorder': Image.open(directory + 'recorder.png'),
    'nonspeaking': Image.open(directory + 'nonspeaking.png'),
    'wheat': Image.open(directory + 'wheat.png'),
    'raincoat': Image.open(directory + 'raincoat.png'),
    'slaughter': Image.open(directory + 'slaughter.png'),
    'broken': Image.open(directory + 'broken.png'),
    'Frigg': Image.open(directory + 'Frigg.png'),
    'innocence': Image.open(directory + 'innocence.png'),
    'resurrection': Image.open(directory + 'resurrection.png'),
    'bazaar': Image.open(directory + 'bazaar.png'),
    'greengrocer': Image.open(directory + 'greengrocer.png'),
    'on': Image.open(directory + 'on.png'),
    'island': Image.open(directory + 'island.png'),
    'shrimp': Image.open(directory + 'shrimp.png'),
    'ox': Image.open(directory + 'ox.png'),
    'chive': Image.open(directory + 'chive.png'),
    'or': Image.open(directory + 'or.png'),
    'fertile': Image.open(directory + 'fertile.png'),
    'curling': Image.open(directory + 'curling.png'),
    'burning': Image.open(directory + 'burning.png'),
    'communication': Image.open(directory + 'communication.png'),
    'Balder': Image.open(directory + 'Balder.png'),
    'earring': Image.open(directory + 'earring.png'),
    'harness': Image.open(directory + 'harness.png'),
    'syringe': Image.open(directory + 'syringe.png'),
    'watchdog': Image.open(directory + 'watchdog.png'),
    'trapeze': Image.open(directory + 'trapeze.png'),
    'there': Image.open(directory + 'there.png'),
    'harpsichord': Image.open(directory + 'harpsichord.png'),
    'Moominpappa': Image.open(directory + 'Moominpappa.png'),
    'hen': Image.open(directory + 'hen.png'),
    'valley': Image.open(directory + 'valley.png'),
    'bubble': Image.open(directory + 'bubble.png'),
    'hare': Image.open(directory + 'hare.png'),
    'fanatic': Image.open(directory + 'fanatic.png'),
    'prawn': Image.open(directory + 'prawn.png'),
    'soprano': Image.open(directory + 'soprano.png'),
    'lymph': Image.open(directory + 'lymph.png'),
    'with': Image.open(directory + 'with.png'),
    'dromedary': Image.open(directory + 'dromedary.png'),
    'strawberry': Image.open(directory + 'strawberry.png'),
    'cornmeal': Image.open(directory + 'cornmeal.png'),
    'grass': Image.open(directory + 'grass.png'),
    'toilet': Image.open(directory + 'toilet.png'),
    'gong': Image.open(directory + 'gong.png'),
    'USA': Image.open(directory + 'USA.png'),
    'rapids': Image.open(directory + 'rapids.png'),
    'taste': Image.open(directory + 'taste.png'),
    'deep': Image.open(directory + 'deep.png'),
    'general': Image.open(directory + 'general.png'),
    'homosexual': Image.open(directory + 'homosexual.png'),
    'at': Image.open(directory + 'at.png'),
    'schoolmate': Image.open(directory + 'schoolmate.png'),
    'girlfriend': Image.open(directory + 'girlfriend.png'),
    'politics': Image.open(directory + 'politics.png'),
    'bishop': Image.open(directory + 'bishop.png'),
    'film': Image.open(directory + 'film.png'),
    'cream': Image.open(directory + 'cream.png'),
    'again': Image.open(directory + 'again.png'),
    'biochemistry': Image.open(directory + 'biochemistry.png'),
    'nutcracker': Image.open(directory + 'nutcracker.png'),
    'field': Image.open(directory + 'field.png'),
    'puppy': Image.open(directory + 'puppy.png'),
    'houseboat': Image.open(directory + 'houseboat.png'),
    'classmate': Image.open(directory + 'classmate.png'),
    'teeth': Image.open(directory + 'teeth.png'),
    'pear': Image.open(directory + 'pear.png'),
    'peas': Image.open(directory + 'peas.png'),
    'nucleus': Image.open(directory + 'nucleus.png'),
    'pool': Image.open(directory + 'pool.png'),
    'psychology': Image.open(directory + 'psychology.png'),
    'cowshed': Image.open(directory + 'cowshed.png'),
    'condensation': Image.open(directory + 'condensation.png'),
    'wife': Image.open(directory + 'wife.png'),
    'mast': Image.open(directory + 'mast.png'),
    'ovary': Image.open(directory + 'ovary.png'),
    'Canada': Image.open(directory + 'Canada.png'),
    'skeleton': Image.open(directory + 'skeleton.png'),
    'dollar': Image.open(directory + 'dollar.png'),
    'month': Image.open(directory + 'month.png'),
    'cardiologist': Image.open(directory + 'cardiologist.png'),
    'Moses': Image.open(directory + 'Moses.png'),
    'religious': Image.open(directory + 'religious.png'),
    'dumpling': Image.open(directory + 'dumpling.png'),
    'tail': Image.open(directory + 'tail.png'),
    'dairy': Image.open(directory + 'dairy.png'),
    'painter': Image.open(directory + 'painter.png'),
    'fountain': Image.open(directory + 'fountain.png'),
    'passivity': Image.open(directory + 'passivity.png'),
    'fax': Image.open(directory + 'fax.png'),
    'appointment': Image.open(directory + 'appointment.png'),
    'chameleon': Image.open(directory + 'chameleon.png'),
    'screwdriver': Image.open(directory + 'screwdriver.png'),
    'psychologist': Image.open(directory + 'psychologist.png'),
    'fan': Image.open(directory + 'fan.png'),
    'awful': Image.open(directory + 'awful.png'),
    'Noah': Image.open(directory + 'Noah.png'),
    'dinosaur': Image.open(directory + 'dinosaur.png'),
    'sand': Image.open(directory + 'sand.png'),
    'portable': Image.open(directory + 'portable.png'),
    'tea': Image.open(directory + 'tea.png'),
    'grasshopper': Image.open(directory + 'grasshopper.png'),
    'past': Image.open(directory + 'past.png'),
    'orgasm': Image.open(directory + 'orgasm.png'),
    'lawyer': Image.open(directory + 'lawyer.png'),
    'belief': Image.open(directory + 'belief.png'),
    'conscience': Image.open(directory + 'conscience.png'),
    'what': Image.open(directory + 'what.png'),
    'imported': Image.open(directory + 'imported.png'),
    'darkness': Image.open(directory + 'darkness.png'),
    'sun': Image.open(directory + 'sun.png'),
    'protractor': Image.open(directory + 'protractor.png'),
    'anniversary': Image.open(directory + 'anniversary.png'),
    'nurse': Image.open(directory + 'nurse.png'),
    'multitude': Image.open(directory + 'multitude.png'),
    'full': Image.open(directory + 'full.png'),
    'christian': Image.open(directory + 'christian.png'),
    'Finland': Image.open(directory + 'Finland.png'),
    'behaviour': Image.open(directory + 'behaviour.png'),
    'tragedy': Image.open(directory + 'tragedy.png'),
    'publisher': Image.open(directory + 'publisher.png'),
    'inspired': Image.open(directory + 'inspired.png'),
    'experience': Image.open(directory + 'experience.png'),
    'airport': Image.open(directory + 'airport.png'),
    'milkshake': Image.open(directory + 'milkshake.png'),
    'social': Image.open(directory + 'social.png'),
    'narrow': Image.open(directory + 'narrow.png'),
    'family': Image.open(directory + 'family.png'),
    'cowardly': Image.open(directory + 'cowardly.png'),
    'commandments': Image.open(directory + 'commandments.png'),
    'armed': Image.open(directory + 'armed.png'),
    'Europe': Image.open(directory + 'Europe.png'),
    'eye': Image.open(directory + 'eye.png'),
    'stander': Image.open(directory + 'stander.png'),
    'odometer': Image.open(directory + 'odometer.png'),
    'more': Image.open(directory + 'more.png'),
    'flat': Image.open(directory + 'flat.png'),
    'door': Image.open(directory + 'door.png'),
    'flax': Image.open(directory + 'flax.png'),
    'excuse': Image.open(directory + 'excuse.png'),
    'flag': Image.open(directory + 'flag.png'),
    'fishburger': Image.open(directory + 'fishburger.png'),
    'science': Image.open(directory + 'science.png'),
    'schooner': Image.open(directory + 'schooner.png'),
    'history': Image.open(directory + 'history.png'),
    'fundamentalist': Image.open(directory + 'fundamentalist.png'),
    'shark': Image.open(directory + 'shark.png'),
    'hamburger': Image.open(directory + 'hamburger.png'),
    'ballooning': Image.open(directory + 'ballooning.png'),
    'archipelago': Image.open(directory + 'archipelago.png'),
    'salty': Image.open(directory + 'salty.png'),
    'beaver': Image.open(directory + 'beaver.png'),
    'fundamentalism': Image.open(directory + 'fundamentalism.png'),
    'dress': Image.open(directory + 'dress.png'),
    'botanist': Image.open(directory + 'botanist.png'),
    'string': Image.open(directory + 'string.png'),
    'huge': Image.open(directory + 'huge.png'),
    'triathlon': Image.open(directory + 'triathlon.png'),
    'goal': Image.open(directory + 'goal.png'),
    'rye': Image.open(directory + 'rye.png'),
    'goat': Image.open(directory + 'goat.png'),
    'Tyr': Image.open(directory + 'Tyr.png'),
    'plant': Image.open(directory + 'plant.png'),
    'sandwich': Image.open(directory + 'sandwich.png'),
    'northward': Image.open(directory + 'northward.png'),
    'blood': Image.open(directory + 'blood.png'),
    'horizontal': Image.open(directory + 'horizontal.png'),
    'short': Image.open(directory + 'short.png'),
    'orchard': Image.open(directory + 'orchard.png'),
    'rowdy': Image.open(directory + 'rowdy.png'),
    'departure': Image.open(directory + 'departure.png'),
    'volleyball': Image.open(directory + 'volleyball.png'),
    'responsibility': Image.open(directory + 'responsibility.png'),
    'hobbit': Image.open(directory + 'hobbit.png'),
    'prostitution': Image.open(directory + 'prostitution.png'),
    'copper': Image.open(directory + 'copper.png'),
    'soon': Image.open(directory + 'soon.png'),
    'dough': Image.open(directory + 'dough.png'),
    'hell': Image.open(directory + 'hell.png'),
    'its': Image.open(directory + 'its.png'),
    'moshav': Image.open(directory + 'moshav.png'),
    'astrology': Image.open(directory + 'astrology.png'),
    'muskrat': Image.open(directory + 'muskrat.png'),
    'March': Image.open(directory + 'March.png'),
    'late': Image.open(directory + 'late.png'),
    'speech': Image.open(directory + 'speech.png'),
    'colleague': Image.open(directory + 'colleague.png'),
    'evening': Image.open(directory + 'evening.png'),
    'hysterectomy': Image.open(directory + 'hysterectomy.png'),
    'food': Image.open(directory + 'food.png'),
    'hunter': Image.open(directory + 'hunter.png'),
    'snowball': Image.open(directory + 'snowball.png'),
    'foot': Image.open(directory + 'foot.png'),
    'adventurous': Image.open(directory + 'adventurous.png'),
    'reflexologist': Image.open(directory + 'reflexologist.png'),
    'chairlift': Image.open(directory + 'chairlift.png'),
    'pregnant': Image.open(directory + 'pregnant.png'),
    'trolleybus': Image.open(directory + 'trolleybus.png'),
    'ashes': Image.open(directory + 'ashes.png'),
    'astarboard': Image.open(directory + 'astarboard.png'),
    'athletics': Image.open(directory + 'athletics.png'),
    'heavy': Image.open(directory + 'heavy.png'),
    'weight': Image.open(directory + 'weight.png'),
    'energy': Image.open(directory + 'energy.png'),
    'Vishnu': Image.open(directory + 'Vishnu.png'),
    'farfalle': Image.open(directory + 'farfalle.png'),
    'operation': Image.open(directory + 'operation.png'),
    'insurance': Image.open(directory + 'insurance.png'),
    'harp': Image.open(directory + 'harp.png'),
    'flower': Image.open(directory + 'flower.png'),
    'lipstick': Image.open(directory + 'lipstick.png'),
    'glitter': Image.open(directory + 'glitter.png'),
    'research': Image.open(directory + 'research.png'),
    'health': Image.open(directory + 'health.png'),
    'hill': Image.open(directory + 'hill.png'),
    'flame': Image.open(directory + 'flame.png'),
    'gardener': Image.open(directory + 'gardener.png'),
    'Ukraine': Image.open(directory + 'Ukraine.png'),
    'bass': Image.open(directory + 'bass.png'),
    'pensioner': Image.open(directory + 'pensioner.png'),
    'difficulty': Image.open(directory + 'difficulty.png'),
    'suntan': Image.open(directory + 'suntan.png'),
    'heroic': Image.open(directory + 'heroic.png'),
    'definition': Image.open(directory + 'definition.png'),
    'Iyar': Image.open(directory + 'Iyar.png'),
    'prophet': Image.open(directory + 'prophet.png'),
    'cloudberry': Image.open(directory + 'cloudberry.png'),
    'corkscrew': Image.open(directory + 'corkscrew.png'),
    'snowboarding': Image.open(directory + 'snowboarding.png'),
    'botany': Image.open(directory + 'botany.png'),
    'stepmother': Image.open(directory + 'stepmother.png'),
    'knocking': Image.open(directory + 'knocking.png'),
    'number': Image.open(directory + 'number.png'),
    'sailor': Image.open(directory + 'sailor.png'),
    'florist': Image.open(directory + 'florist.png'),
    'speedometer': Image.open(directory + 'speedometer.png'),
    'sunburn': Image.open(directory + 'sunburn.png'),
    'horse': Image.open(directory + 'horse.png'),
    'temperature': Image.open(directory + 'temperature.png'),
    'divorce': Image.open(directory + 'divorce.png'),
    'obedience': Image.open(directory + 'obedience.png'),
    'collar': Image.open(directory + 'collar.png'),
    'station': Image.open(directory + 'station.png'),
    'saint': Image.open(directory + 'saint.png'),
    'Belgium': Image.open(directory + 'Belgium.png'),
    'compartment': Image.open(directory + 'compartment.png'),
    'syrup': Image.open(directory + 'syrup.png'),
    'banana': Image.open(directory + 'banana.png'),
    'statement': Image.open(directory + 'statement.png'),
    'voyeurism': Image.open(directory + 'voyeurism.png'),
    'exploded': Image.open(directory + 'exploded.png'),
    'needle': Image.open(directory + 'needle.png'),
    'park': Image.open(directory + 'park.png'),
    'dentist': Image.open(directory + 'dentist.png'),
    'interviewer': Image.open(directory + 'interviewer.png'),
    'grace': Image.open(directory + 'grace.png'),
    'surfboard': Image.open(directory + 'surfboard.png'),
    'king': Image.open(directory + 'king.png'),
    'architect': Image.open(directory + 'architect.png'),
    'weapon': Image.open(directory + 'weapon.png'),
    'dried': Image.open(directory + 'dried.png'),
    'motivation': Image.open(directory + 'motivation.png'),
    'God': Image.open(directory + 'God.png'),
    'juicy': Image.open(directory + 'juicy.png'),
    'magical': Image.open(directory + 'magical.png'),
    'gale': Image.open(directory + 'gale.png'),
    'lid': Image.open(directory + 'lid.png'),
    'lie': Image.open(directory + 'lie.png'),
    'koala': Image.open(directory + 'koala.png'),
    'Iceland': Image.open(directory + 'Iceland.png'),
    'cave': Image.open(directory + 'cave.png'),
    'heterosexual': Image.open(directory + 'heterosexual.png'),
    'labour': Image.open(directory + 'labour.png'),
    'Germany': Image.open(directory + 'Germany.png'),
    'chairman': Image.open(directory + 'chairman.png'),
    'banjo': Image.open(directory + 'banjo.png'),
    'salmon': Image.open(directory + 'salmon.png'),
    'handcycle': Image.open(directory + 'handcycle.png'),
    'cigarette': Image.open(directory + 'cigarette.png'),
    'virus': Image.open(directory + 'virus.png'),
    'charm': Image.open(directory + 'charm.png'),
    'darts': Image.open(directory + 'darts.png'),
    'achievement': Image.open(directory + 'achievement.png'),
    'archery': Image.open(directory + 'archery.png'),
    'Egypt': Image.open(directory + 'Egypt.png'),
    'sometimes': Image.open(directory + 'sometimes.png'),
    'amphibian': Image.open(directory + 'amphibian.png'),
    'clean': Image.open(directory + 'clean.png'),
    'physics': Image.open(directory + 'physics.png'),
    'perseverance': Image.open(directory + 'perseverance.png'),
    'Saehrimnir': Image.open(directory + 'Saehrimnir.png'),
    'gold': Image.open(directory + 'gold.png'),
    'impact': Image.open(directory + 'impact.png'),
    'giant': Image.open(directory + 'giant.png'),
    'causality': Image.open(directory + 'causality.png'),
    'northern': Image.open(directory + 'northern.png'),
    'justice': Image.open(directory + 'justice.png'),
    'scooter': Image.open(directory + 'scooter.png'),
    'condom': Image.open(directory + 'condom.png'),
    'circle': Image.open(directory + 'circle.png'),
    'porcupine': Image.open(directory + 'porcupine.png'),
    'shepherd': Image.open(directory + 'shepherd.png'),
    'his': Image.open(directory + 'his.png'),
    'triangle': Image.open(directory + 'triangle.png'),
    'dependent': Image.open(directory + 'dependent.png'),
    'sunny': Image.open(directory + 'sunny.png'),
    'courage': Image.open(directory + 'courage.png'),
    'batter': Image.open(directory + 'batter.png'),
    'longest': Image.open(directory + 'longest.png'),
    'theft': Image.open(directory + 'theft.png'),
    'compass': Image.open(directory + 'compass.png'),
    'silk': Image.open(directory + 'silk.png'),
    'chimney': Image.open(directory + 'chimney.png'),
    'Triceratops': Image.open(directory + 'Triceratops.png'),
    'gospel': Image.open(directory + 'gospel.png'),
    'tanker': Image.open(directory + 'tanker.png'),
    'cheese': Image.open(directory + 'cheese.png'),
    'snowstorm': Image.open(directory + 'snowstorm.png'),
    'voltage': Image.open(directory + 'voltage.png'),
    'vulva': Image.open(directory + 'vulva.png'),
    'art': Image.open(directory + 'art.png'),
    'farrier': Image.open(directory + 'farrier.png'),
    'plough': Image.open(directory + 'plough.png'),
    'culture': Image.open(directory + 'culture.png'),
    'lion': Image.open(directory + 'lion.png'),
    'Kislev': Image.open(directory + 'Kislev.png'),
    'bark': Image.open(directory + 'bark.png'),
    'arm': Image.open(directory + 'arm.png'),
    'barn': Image.open(directory + 'barn.png'),
    'please': Image.open(directory + 'please.png'),
    'fishball': Image.open(directory + 'fishball.png'),
    'marriage': Image.open(directory + 'marriage.png'),
    'champagne': Image.open(directory + 'champagne.png'),
    'funeral': Image.open(directory + 'funeral.png'),
    'cartographer': Image.open(directory + 'cartographer.png'),
    'attention': Image.open(directory + 'attention.png'),
    'death': Image.open(directory + 'death.png'),
    'sailboard': Image.open(directory + 'sailboard.png'),
    'ampullae': Image.open(directory + 'ampullae.png'),
    'bronze': Image.open(directory + 'bronze.png'),
    'both': Image.open(directory + 'both.png'),
    'prescription': Image.open(directory + 'prescription.png'),
    'foreign': Image.open(directory + 'foreign.png'),
    'eggplant': Image.open(directory + 'eggplant.png'),
    'mausoleum': Image.open(directory + 'mausoleum.png'),
    'load': Image.open(directory + 'load.png'),
    'bell': Image.open(directory + 'bell.png'),
    'battery': Image.open(directory + 'battery.png'),
    'harbour': Image.open(directory + 'harbour.png'),
    'village': Image.open(directory + 'village.png'),
    'indefinite': Image.open(directory + 'indefinite.png'),
    'hovercraft': Image.open(directory + 'hovercraft.png'),
    'stamp': Image.open(directory + 'stamp.png'),
    'apostle': Image.open(directory + 'apostle.png'),
    'strategy': Image.open(directory + 'strategy.png'),
    'Passover': Image.open(directory + 'Passover.png'),
    'secret': Image.open(directory + 'secret.png'),
    'Toffle': Image.open(directory + 'Toffle.png'),
    'chipmunk': Image.open(directory + 'chipmunk.png'),
    'Advent': Image.open(directory + 'Advent.png'),
    'empty': Image.open(directory + 'empty.png'),
    'squirrel': Image.open(directory + 'squirrel.png'),
    'fire': Image.open(directory + 'fire.png'),
    'Universe': Image.open(directory + 'Universe.png'),
    'gas': Image.open(directory + 'gas.png'),
    'awake': Image.open(directory + 'awake.png'),
    'liver': Image.open(directory + 'liver.png'),
    'politician': Image.open(directory + 'politician.png'),
    'horseshoe': Image.open(directory + 'horseshoe.png'),
    'sexuality': Image.open(directory + 'sexuality.png'),
    'Italy': Image.open(directory + 'Italy.png'),
    'century': Image.open(directory + 'century.png'),
    'calculator': Image.open(directory + 'calculator.png'),
    'shamrock': Image.open(directory + 'shamrock.png'),
    'ecstasy': Image.open(directory + 'ecstasy.png'),
    'urethra': Image.open(directory + 'urethra.png'),
    'chase': Image.open(directory + 'chase.png'),
    'protestantism': Image.open(directory + 'protestantism.png'),
    'sociologist': Image.open(directory + 'sociologist.png'),
    'government': Image.open(directory + 'government.png'),
    'butcher': Image.open(directory + 'butcher.png'),
    'viola': Image.open(directory + 'viola.png'),
    'development': Image.open(directory + 'development.png'),
    'temporary': Image.open(directory + 'temporary.png'),
    'biochemist': Image.open(directory + 'biochemist.png'),
    'snail': Image.open(directory + 'snail.png'),
    'mountain': Image.open(directory + 'mountain.png'),
    'leopard': Image.open(directory + 'leopard.png'),
    'yesterday': Image.open(directory + 'yesterday.png'),
    'strength': Image.open(directory + 'strength.png'),
    'cucumber': Image.open(directory + 'cucumber.png'),
    'purpose': Image.open(directory + 'purpose.png'),
    'birch': Image.open(directory + 'birch.png'),
    'early': Image.open(directory + 'early.png'),
    'werewolf': Image.open(directory + 'werewolf.png'),
    'cheek': Image.open(directory + 'cheek.png'),
    'edge': Image.open(directory + 'edge.png'),
    'crayfish': Image.open(directory + 'crayfish.png'),
    'empowered': Image.open(directory + 'empowered.png'),
    'margarine': Image.open(directory + 'margarine.png'),
    'prince': Image.open(directory + 'prince.png'),
    'abstention': Image.open(directory + 'abstention.png'),
    'retirement': Image.open(directory + 'retirement.png'),
    'cup': Image.open(directory + 'cup.png'),
    'scales': Image.open(directory + 'scales.png'),
    'cemetery': Image.open(directory + 'cemetery.png'),
    'horseradish': Image.open(directory + 'horseradish.png'),
    'circumcision': Image.open(directory + 'circumcision.png'),
    'acrobatics': Image.open(directory + 'acrobatics.png'),
    'easter': Image.open(directory + 'easter.png'),
    'voltmeter': Image.open(directory + 'voltmeter.png'),
    'surprised': Image.open(directory + 'surprised.png'),
    'chess': Image.open(directory + 'chess.png'),
    'emergency': Image.open(directory + 'emergency.png'),
    'advocate': Image.open(directory + 'advocate.png'),
    'bib': Image.open(directory + 'bib.png'),
    'Thor': Image.open(directory + 'Thor.png'),
    'game': Image.open(directory + 'game.png'),
    'jackfruit': Image.open(directory + 'jackfruit.png'),
    'springbok': Image.open(directory + 'springbok.png'),
    'optician': Image.open(directory + 'optician.png'),
    'message': Image.open(directory + 'message.png'),
    'eel': Image.open(directory + 'eel.png'),
    'walrus': Image.open(directory + 'walrus.png'),
    'dictatorship': Image.open(directory + 'dictatorship.png'),
    'woking': Image.open(directory + 'woking.png'),
    'spring': Image.open(directory + 'spring.png'),
    'palm': Image.open(directory + 'palm.png'),
    'clown': Image.open(directory + 'clown.png'),
    'mirror': Image.open(directory + 'mirror.png'),
    'falafel': Image.open(directory + 'falafel.png'),
    'candle': Image.open(directory + 'candle.png'),
    'biathlon': Image.open(directory + 'biathlon.png'),
    'pet': Image.open(directory + 'pet.png'),
    'decision': Image.open(directory + 'decision.png'),
    'physiotherapy': Image.open(directory + 'physiotherapy.png'),
    'blackberry': Image.open(directory + 'blackberry.png'),
    'porridge': Image.open(directory + 'porridge.png'),
    'portability': Image.open(directory + 'portability.png'),
    'eruption': Image.open(directory + 'eruption.png'),
    'perpendicular': Image.open(directory + 'perpendicular.png'),
    'Ganesh': Image.open(directory + 'Ganesh.png'),
    'stew': Image.open(directory + 'stew.png'),
    'from': Image.open(directory + 'from.png'),
    'altimeter': Image.open(directory + 'altimeter.png'),
    'Russia': Image.open(directory + 'Russia.png'),
    'tefillin': Image.open(directory + 'tefillin.png'),
    'shine': Image.open(directory + 'shine.png'),
    'Romania': Image.open(directory + 'Romania.png'),
    'volunteering': Image.open(directory + 'volunteering.png'),
    'sacrament': Image.open(directory + 'sacrament.png'),
    'drama': Image.open(directory + 'drama.png'),
    'pollution': Image.open(directory + 'pollution.png'),
    'accessible': Image.open(directory + 'accessible.png'),
    'Mjolnir': Image.open(directory + 'Mjolnir.png'),
    'deafness': Image.open(directory + 'deafness.png'),
    'into': Image.open(directory + 'into.png'),
    'nonsense': Image.open(directory + 'nonsense.png'),
    'jockey': Image.open(directory + 'jockey.png'),
    'question': Image.open(directory + 'question.png'),
    'parsnip': Image.open(directory + 'parsnip.png'),
    'asteroid': Image.open(directory + 'asteroid.png'),
    'infected': Image.open(directory + 'infected.png'),
    'parting': Image.open(directory + 'parting.png'),
    'suit': Image.open(directory + 'suit.png'),
    'forward': Image.open(directory + 'forward.png'),
    'Cheshvan': Image.open(directory + 'Cheshvan.png'),
    'reed': Image.open(directory + 'reed.png'),
    'atom': Image.open(directory + 'atom.png'),
    'Switzerland': Image.open(directory + 'Switzerland.png'),
    'crane': Image.open(directory + 'crane.png'),
    'penguin': Image.open(directory + 'penguin.png'),
    'chiropractor': Image.open(directory + 'chiropractor.png'),
    'forefather': Image.open(directory + 'forefather.png'),
    'apricot': Image.open(directory + 'apricot.png'),
    'Africa': Image.open(directory + 'Africa.png'),
    'planet': Image.open(directory + 'planet.png'),
    'those': Image.open(directory + 'those.png'),
    'prosecutor': Image.open(directory + 'prosecutor.png'),
    'gymnastics': Image.open(directory + 'gymnastics.png'),
    'fried': Image.open(directory + 'fried.png'),
    'influence': Image.open(directory + 'influence.png'),
    'accessibility': Image.open(directory + 'accessibility.png'),
    'warning': Image.open(directory + 'warning.png'),
    'paddock': Image.open(directory + 'paddock.png'),
    'kidney': Image.open(directory + 'kidney.png'),
    'cotton': Image.open(directory + 'cotton.png'),
    'rainbow': Image.open(directory + 'rainbow.png'),
    'rainy': Image.open(directory + 'rainy.png'),
    'lemon': Image.open(directory + 'lemon.png'),
    'May': Image.open(directory + 'May.png'),
    'altar': Image.open(directory + 'altar.png'),
    'freighter': Image.open(directory + 'freighter.png'),
    'mustard': Image.open(directory + 'mustard.png'),
    'rabies': Image.open(directory + 'rabies.png'),
    'favourite': Image.open(directory + 'favourite.png'),
    'tablespoon': Image.open(directory + 'tablespoon.png'),
    'breasts': Image.open(directory + 'breasts.png'),
    'fertilized': Image.open(directory + 'fertilized.png'),
    'clue': Image.open(directory + 'clue.png'),
    'desert': Image.open(directory + 'desert.png'),
    'organism': Image.open(directory + 'organism.png'),
    'age': Image.open(directory + 'age.png'),
    'depth': Image.open(directory + 'depth.png'),
    'Aegir': Image.open(directory + 'Aegir.png'),
    'amenorrhea': Image.open(directory + 'amenorrhea.png'),
    'Av': Image.open(directory + 'Av.png'),
    'walker': Image.open(directory + 'walker.png'),
    'fresh': Image.open(directory + 'fresh.png'),
    'Hattifatteners': Image.open(directory + 'Hattifatteners.png'),
    'once': Image.open(directory + 'once.png'),
    'scratch': Image.open(directory + 'scratch.png'),
    'snowmobile': Image.open(directory + 'snowmobile.png'),
    'discordant': Image.open(directory + 'discordant.png'),
    'wizard': Image.open(directory + 'wizard.png'),
    'young': Image.open(directory + 'young.png'),
    'rudder': Image.open(directory + 'rudder.png'),
    'stable': Image.open(directory + 'stable.png'),
    'dislike': Image.open(directory + 'dislike.png'),
    'ingredient': Image.open(directory + 'ingredient.png'),
    'confirmation': Image.open(directory + 'confirmation.png'),
    'garden': Image.open(directory + 'garden.png'),
    'ukulele': Image.open(directory + 'ukulele.png'),
    'ladle': Image.open(directory + 'ladle.png'),
    'fishnet': Image.open(directory + 'fishnet.png'),
    'dessert': Image.open(directory + 'dessert.png'),
    'rhyme': Image.open(directory + 'rhyme.png'),
    'wave': Image.open(directory + 'wave.png'),
    'snowshoe': Image.open(directory + 'snowshoe.png'),
    'spoon': Image.open(directory + 'spoon.png'),
    'surgeon': Image.open(directory + 'surgeon.png'),
    'magic': Image.open(directory + 'magic.png'),
    'Estonia': Image.open(directory + 'Estonia.png'),
    'asparagus': Image.open(directory + 'asparagus.png'),
    'knight': Image.open(directory + 'knight.png'),
    'Turkey': Image.open(directory + 'Turkey.png'),
    'jump': Image.open(directory + 'jump.png'),
    'MMS': Image.open(directory + 'MMS.png'),
    'uncomfortable': Image.open(directory + 'uncomfortable.png'),
    'trackball': Image.open(directory + 'trackball.png'),
    'spaghetti': Image.open(directory + 'spaghetti.png'),
    'depression': Image.open(directory + 'depression.png'),
    'Durga': Image.open(directory + 'Durga.png'),
    'sauerkraut': Image.open(directory + 'sauerkraut.png'),
    'vampire': Image.open(directory + 'vampire.png'),
    'cell': Image.open(directory + 'cell.png'),
    'experiment': Image.open(directory + 'experiment.png'),
    'twins': Image.open(directory + 'twins.png'),
    'bird': Image.open(directory + 'bird.png'),
    'leg': Image.open(directory + 'leg.png'),
    'kidnapper': Image.open(directory + 'kidnapper.png'),
    'brooch': Image.open(directory + 'brooch.png'),
    'poverty': Image.open(directory + 'poverty.png'),
    'vinegar': Image.open(directory + 'vinegar.png'),
    'insulin': Image.open(directory + 'insulin.png'),
    'grandchild': Image.open(directory + 'grandchild.png'),
    'popcorn': Image.open(directory + 'popcorn.png'),
    'opinion': Image.open(directory + 'opinion.png'),
    'Valhalla': Image.open(directory + 'Valhalla.png'),
    'apple': Image.open(directory + 'apple.png'),
    'danger': Image.open(directory + 'danger.png'),
    'manna': Image.open(directory + 'manna.png'),
    'terrified': Image.open(directory + 'terrified.png'),
    'private': Image.open(directory + 'private.png'),
    'respirator': Image.open(directory + 'respirator.png'),
    'composer': Image.open(directory + 'composer.png'),
    'cheerleader': Image.open(directory + 'cheerleader.png'),
    'cloud': Image.open(directory + 'cloud.png'),
    'lime': Image.open(directory + 'lime.png'),
    'celery': Image.open(directory + 'celery.png'),
    'fee': Image.open(directory + 'fee.png'),
    'metaphor': Image.open(directory + 'metaphor.png'),
    'orthopaedist': Image.open(directory + 'orthopaedist.png'),
    'next': Image.open(directory + 'next.png'),
    'camera': Image.open(directory + 'camera.png'),
    'Lent': Image.open(directory + 'Lent.png'),
    'otolaryngologist': Image.open(directory + 'otolaryngologist.png'),
    'disgust': Image.open(directory + 'disgust.png'),
    'Denmark': Image.open(directory + 'Denmark.png'),
    'musician': Image.open(directory + 'musician.png'),
    'infection': Image.open(directory + 'infection.png'),
    'charming': Image.open(directory + 'charming.png'),
    'train': Image.open(directory + 'train.png'),
    'penis': Image.open(directory + 'penis.png'),
    'harvest': Image.open(directory + 'harvest.png'),
    'casserole': Image.open(directory + 'casserole.png'),
    'charity': Image.open(directory + 'charity.png'),
    'account': Image.open(directory + 'account.png'),
    'salad': Image.open(directory + 'salad.png'),
    'this': Image.open(directory + 'this.png'),
    'challenge': Image.open(directory + 'challenge.png'),
    'drill': Image.open(directory + 'drill.png'),
    'worksheet': Image.open(directory + 'worksheet.png'),
    'coffin': Image.open(directory + 'coffin.png'),
    'control': Image.open(directory + 'control.png'),
    'hip': Image.open(directory + 'hip.png'),
    'thirsty': Image.open(directory + 'thirsty.png'),
    'lock': Image.open(directory + 'lock.png'),
    'tax': Image.open(directory + 'tax.png'),
    'skirt': Image.open(directory + 'skirt.png'),
    'Christmas': Image.open(directory + 'Christmas.png'),
    'rape': Image.open(directory + 'rape.png'),
    'hangar': Image.open(directory + 'hangar.png'),
    'lamb': Image.open(directory + 'lamb.png'),
    'democracy': Image.open(directory + 'democracy.png'),
    'poetry': Image.open(directory + 'poetry.png'),
    'goldsmith': Image.open(directory + 'goldsmith.png'),
    'comedy': Image.open(directory + 'comedy.png'),
    'sin': Image.open(directory + 'sin.png'),
    'hurdles': Image.open(directory + 'hurdles.png'),
    'farm': Image.open(directory + 'farm.png'),
    'testimony': Image.open(directory + 'testimony.png'),
    'discomfort': Image.open(directory + 'discomfort.png'),
    'wrist': Image.open(directory + 'wrist.png'),
    'multiplication': Image.open(directory + 'multiplication.png'),
    'cabbage': Image.open(directory + 'cabbage.png'),
    'tongue': Image.open(directory + 'tongue.png'),
    'tomato': Image.open(directory + 'tomato.png'),
    'daycare': Image.open(directory + 'daycare.png'),
    'light': Image.open(directory + 'light.png'),
    'cutlery': Image.open(directory + 'cutlery.png'),
    'bakery': Image.open(directory + 'bakery.png'),
    'agenda': Image.open(directory + 'agenda.png'),
    'Greece': Image.open(directory + 'Greece.png'),
    'necklace': Image.open(directory + 'necklace.png'),
    'addiction': Image.open(directory + 'addiction.png'),
    'insight': Image.open(directory + 'insight.png'),
    'sperm': Image.open(directory + 'sperm.png'),
    'comma': Image.open(directory + 'comma.png'),
    'galaxy': Image.open(directory + 'galaxy.png'),
    'perfect': Image.open(directory + 'perfect.png'),
    'linguistics': Image.open(directory + 'linguistics.png'),
    'inlet': Image.open(directory + 'inlet.png'),
    'broom': Image.open(directory + 'broom.png'),
    'eastward': Image.open(directory + 'eastward.png'),
    'flour': Image.open(directory + 'flour.png'),
    'Adar': Image.open(directory + 'Adar.png'),
    'swordfish': Image.open(directory + 'swordfish.png'),
    'snake': Image.open(directory + 'snake.png'),
    'kiss': Image.open(directory + 'kiss.png'),
    'fingerprint': Image.open(directory + 'fingerprint.png'),
    'flea': Image.open(directory + 'flea.png'),
    'cage': Image.open(directory + 'cage.png'),
    'day': Image.open(directory + 'day.png'),
    'Havdalah': Image.open(directory + 'Havdalah.png'),
    'tram': Image.open(directory + 'tram.png'),
    'university': Image.open(directory + 'university.png'),
    'cider': Image.open(directory + 'cider.png'),
    'slide': Image.open(directory + 'slide.png'),
    'trap': Image.open(directory + 'trap.png'),
    'truth': Image.open(directory + 'truth.png'),
    'tray': Image.open(directory + 'tray.png'),
    'schoolbag': Image.open(directory + 'schoolbag.png'),
    'society': Image.open(directory + 'society.png'),
    'frequency': Image.open(directory + 'frequency.png'),
    'witness': Image.open(directory + 'witness.png'),
    'hippopotamus': Image.open(directory + 'hippopotamus.png'),
    'semen': Image.open(directory + 'semen.png'),
    'parasailing': Image.open(directory + 'parasailing.png'),
    'China': Image.open(directory + 'China.png'),
    'playground': Image.open(directory + 'playground.png'),
    'lecture': Image.open(directory + 'lecture.png'),
    'cause': Image.open(directory + 'cause.png'),
    'philosophy': Image.open(directory + 'philosophy.png'),
    'umbrella': Image.open(directory + 'umbrella.png'),
    'utensil': Image.open(directory + 'utensil.png'),
    'shekel': Image.open(directory + 'shekel.png'),
    'Messiah': Image.open(directory + 'Messiah.png'),
    'drowning': Image.open(directory + 'drowning.png'),
    'steak': Image.open(directory + 'steak.png'),
    'yard': Image.open(directory + 'yard.png'),
    'geographer': Image.open(directory + 'geographer.png'),
    'skateboard': Image.open(directory + 'skateboard.png'),
    'timer': Image.open(directory + 'timer.png'),
    'chilly': Image.open(directory + 'chilly.png'),
    'keel': Image.open(directory + 'keel.png'),
    'mortal': Image.open(directory + 'mortal.png'),
    'workbook': Image.open(directory + 'workbook.png'),
    'south': Image.open(directory + 'south.png'),
    'embryo': Image.open(directory + 'embryo.png'),
    'embarrassed': Image.open(directory + 'embarrassed.png'),
    'puppet': Image.open(directory + 'puppet.png'),
    'quality': Image.open(directory + 'quality.png'),
    'long': Image.open(directory + 'long.png'),
    'Iran': Image.open(directory + 'Iran.png'),
    'publication': Image.open(directory + 'publication.png'),
    'dove': Image.open(directory + 'dove.png'),
    'traveller': Image.open(directory + 'traveller.png'),
    'vagina': Image.open(directory + 'vagina.png'),
    'ankle': Image.open(directory + 'ankle.png'),
    'Iraq': Image.open(directory + 'Iraq.png'),
    'beard': Image.open(directory + 'beard.png'),
    'shorts': Image.open(directory + 'shorts.png'),
    'shelf': Image.open(directory + 'shelf.png'),
    'shallow': Image.open(directory + 'shallow.png'),
    'unending': Image.open(directory + 'unending.png'),
    'monotheism': Image.open(directory + 'monotheism.png'),
    'rickshaw': Image.open(directory + 'rickshaw.png'),
    'goblin': Image.open(directory + 'goblin.png'),
    'steel': Image.open(directory + 'steel.png'),
    'prune': Image.open(directory + 'prune.png'),
    'shampoo': Image.open(directory + 'shampoo.png'),
    'bed': Image.open(directory + 'bed.png'),
    'bee': Image.open(directory + 'bee.png'),
    'firework': Image.open(directory + 'firework.png'),
    'reproduction': Image.open(directory + 'reproduction.png'),
    'sculpture': Image.open(directory + 'sculpture.png'),
    'devotion': Image.open(directory + 'devotion.png'),
    'anthropologist': Image.open(directory + 'anthropologist.png'),
    'beggar': Image.open(directory + 'beggar.png'),
    'bisexual': Image.open(directory + 'bisexual.png'),
    'deodorant': Image.open(directory + 'deodorant.png'),
    'cricket': Image.open(directory + 'cricket.png'),
    'robot': Image.open(directory + 'robot.png'),
    'tonight': Image.open(directory + 'tonight.png'),
    'screw': Image.open(directory + 'screw.png'),
    'microphone': Image.open(directory + 'microphone.png'),
    'angle': Image.open(directory + 'angle.png'),
    'bacterium': Image.open(directory + 'bacterium.png'),
    'Batman': Image.open(directory + 'Batman.png'),
    'billiards': Image.open(directory + 'billiards.png'),
    'bagel': Image.open(directory + 'bagel.png'),
    'cherries': Image.open(directory + 'cherries.png'),
    'ashore': Image.open(directory + 'ashore.png'),
    'pharmacist': Image.open(directory + 'pharmacist.png'),
    'orthoptist': Image.open(directory + 'orthoptist.png'),
    'Sniff': Image.open(directory + 'Sniff.png'),
    'raindrop': Image.open(directory + 'raindrop.png'),
    'acupuncturist': Image.open(directory + 'acupuncturist.png'),
    'handbag': Image.open(directory + 'handbag.png'),
    'Abraham': Image.open(directory + 'Abraham.png'),
    'class': Image.open(directory + 'class.png'),
    'spleen': Image.open(directory + 'spleen.png'),
    'urn': Image.open(directory + 'urn.png'),
    'upset': Image.open(directory + 'upset.png'),
    'thanksgiving': Image.open(directory + 'thanksgiving.png'),
    'face': Image.open(directory + 'face.png'),
    'skunk': Image.open(directory + 'skunk.png'),
    'fact': Image.open(directory + 'fact.png'),
    'kite': Image.open(directory + 'kite.png'),
    'seaweed': Image.open(directory + 'seaweed.png'),
    'bedroom': Image.open(directory + 'bedroom.png'),
    'economist': Image.open(directory + 'economist.png'),
    'decade': Image.open(directory + 'decade.png'),
    'staff': Image.open(directory + 'staff.png'),
    'scorpion': Image.open(directory + 'scorpion.png'),
    'hopeful': Image.open(directory + 'hopeful.png'),
    'fuel': Image.open(directory + 'fuel.png'),
    'hope': Image.open(directory + 'hope.png'),
    'spermicide': Image.open(directory + 'spermicide.png'),
    'handle': Image.open(directory + 'handle.png'),
    'wiggly': Image.open(directory + 'wiggly.png'),
    'bear': Image.open(directory + 'bear.png'),
    'joint': Image.open(directory + 'joint.png'),
    'bean': Image.open(directory + 'bean.png'),
    'perfection': Image.open(directory + 'perfection.png'),
    'exchanger': Image.open(directory + 'exchanger.png'),
    'striped': Image.open(directory + 'striped.png'),
    'tobacco': Image.open(directory + 'tobacco.png'),
    'ashtray': Image.open(directory + 'ashtray.png'),
    'motorboat': Image.open(directory + 'motorboat.png'),
    'eyebrow': Image.open(directory + 'eyebrow.png'),
    'corruption': Image.open(directory + 'corruption.png'),
    'Buddha': Image.open(directory + 'Buddha.png'),
    'rein': Image.open(directory + 'rein.png'),
    'buzzer': Image.open(directory + 'buzzer.png'),
    'Afghanistan': Image.open(directory + 'Afghanistan.png'),
    'national': Image.open(directory + 'national.png'),
    'icing': Image.open(directory + 'icing.png'),
    'intensity': Image.open(directory + 'intensity.png'),
    'computer': Image.open(directory + 'computer.png'),
    'washable': Image.open(directory + 'washable.png'),
    'southward': Image.open(directory + 'southward.png'),
    'hammock': Image.open(directory + 'hammock.png'),
    'supernatural': Image.open(directory + 'supernatural.png'),
    'closed': Image.open(directory + 'closed.png'),
    'neither': Image.open(directory + 'neither.png'),
    'frustrated': Image.open(directory + 'frustrated.png'),
    'tent': Image.open(directory + 'tent.png'),
    'explosive': Image.open(directory + 'explosive.png'),
    'cauliflower': Image.open(directory + 'cauliflower.png'),
    'amen': Image.open(directory + 'amen.png'),
    'monarchy': Image.open(directory + 'monarchy.png'),
    'physicist': Image.open(directory + 'physicist.png'),
    'embarrassment': Image.open(directory + 'embarrassment.png'),
    'key': Image.open(directory + 'key.png'),
    'empathy': Image.open(directory + 'empathy.png'),
    'lifeboat': Image.open(directory + 'lifeboat.png'),
    'heterosexuality': Image.open(directory + 'heterosexuality.png'),
    'ramp': Image.open(directory + 'ramp.png'),
    'unfolding': Image.open(directory + 'unfolding.png'),
    'wall': Image.open(directory + 'wall.png'),
    'DVD': Image.open(directory + 'DVD.png'),
    'invisible': Image.open(directory + 'invisible.png'),
    'incest': Image.open(directory + 'incest.png'),
    'news': Image.open(directory + 'news.png'),
    'table': Image.open(directory + 'table.png'),
    'poem': Image.open(directory + 'poem.png'),
    'sari': Image.open(directory + 'sari.png'),
    'cent': Image.open(directory + 'cent.png'),
    'teamwork': Image.open(directory + 'teamwork.png'),
    'treat': Image.open(directory + 'treat.png'),
    'Thailand': Image.open(directory + 'Thailand.png'),
    'feather': Image.open(directory + 'feather.png'),
    'circus': Image.open(directory + 'circus.png'),
    'puberty': Image.open(directory + 'puberty.png'),
    'neighbour': Image.open(directory + 'neighbour.png'),
    'Epiphany': Image.open(directory + 'Epiphany.png'),
    'bull': Image.open(directory + 'bull.png'),
    'present': Image.open(directory + 'present.png'),
    'volunteer': Image.open(directory + 'volunteer.png'),
    'vanilla': Image.open(directory + 'vanilla.png'),
    'frustrating': Image.open(directory + 'frustrating.png'),
    'Haggadah': Image.open(directory + 'Haggadah.png'),
    'resident': Image.open(directory + 'resident.png'),
    'neuron': Image.open(directory + 'neuron.png'),
    'encouragement': Image.open(directory + 'encouragement.png'),
    'tenor': Image.open(directory + 'tenor.png'),
    'Viking': Image.open(directory + 'Viking.png'),
    'cremation': Image.open(directory + 'cremation.png'),
    'terrorist': Image.open(directory + 'terrorist.png'),
    'balloon': Image.open(directory + 'balloon.png'),
    'buddhist': Image.open(directory + 'buddhist.png'),
    'member': Image.open(directory + 'member.png'),
    'strange': Image.open(directory + 'strange.png'),
    'terrorism': Image.open(directory + 'terrorism.png'),
    'Snork': Image.open(directory + 'Snork.png'),
    'ball': Image.open(directory + 'ball.png'),
    'millepede': Image.open(directory + 'millepede.png'),
    'Moominmamma': Image.open(directory + 'Moominmamma.png'),
    'sauna': Image.open(directory + 'sauna.png'),
    'sufganiya': Image.open(directory + 'sufganiya.png'),
    'Belarus': Image.open(directory + 'Belarus.png'),
    'whale': Image.open(directory + 'whale.png'),
    'magician': Image.open(directory + 'magician.png'),
    'broccoli': Image.open(directory + 'broccoli.png'),
    'Tarzan': Image.open(directory + 'Tarzan.png'),
    'reflection': Image.open(directory + 'reflection.png'),
    'shalom': Image.open(directory + 'shalom.png'),
    'colour': Image.open(directory + 'colour.png'),
    'position': Image.open(directory + 'position.png'),
    'muscle': Image.open(directory + 'muscle.png'),
    'Adam': Image.open(directory + 'Adam.png'),
    'camel': Image.open(directory + 'camel.png'),
    'domestic': Image.open(directory + 'domestic.png'),
    'clinic': Image.open(directory + 'clinic.png'),
    'fishing': Image.open(directory + 'fishing.png'),
    'biologist': Image.open(directory + 'biologist.png'),
    'piggery': Image.open(directory + 'piggery.png'),
    'drunk': Image.open(directory + 'drunk.png'),
    'sky': Image.open(directory + 'sky.png'),
    'hall': Image.open(directory + 'hall.png'),
    'bobsleigh': Image.open(directory + 'bobsleigh.png'),
    'adoption': Image.open(directory + 'adoption.png'),
    'citizen': Image.open(directory + 'citizen.png'),
    'match': Image.open(directory + 'match.png'),
    'myth': Image.open(directory + 'myth.png'),
    'disappearance': Image.open(directory + 'disappearance.png'),
    'knot': Image.open(directory + 'knot.png'),
    'doughnut': Image.open(directory + 'doughnut.png'),
    'pier': Image.open(directory + 'pier.png'),
    'placenta': Image.open(directory + 'placenta.png'),
    'loss': Image.open(directory + 'loss.png'),
    'England': Image.open(directory + 'England.png'),
    'success': Image.open(directory + 'success.png'),
    'housekeeper': Image.open(directory + 'housekeeper.png'),
    'candy': Image.open(directory + 'candy.png'),
    'garage': Image.open(directory + 'garage.png'),
    'journalist': Image.open(directory + 'journalist.png'),
    'chick': Image.open(directory + 'chick.png'),
    'soft': Image.open(directory + 'soft.png'),
    'heel': Image.open(directory + 'heel.png'),
    'virginity': Image.open(directory + 'virginity.png'),
    'because': Image.open(directory + 'because.png'),
    'thief': Image.open(directory + 'thief.png'),
    'hail': Image.open(directory + 'hail.png'),
    'hair': Image.open(directory + 'hair.png'),
    'export': Image.open(directory + 'export.png'),
    'home': Image.open(directory + 'home.png'),
    'leaf': Image.open(directory + 'leaf.png'),
    'bet': Image.open(directory + 'bet.png'),
    'lead': Image.open(directory + 'lead.png'),
    'overlay': Image.open(directory + 'overlay.png'),
    'archeology': Image.open(directory + 'archeology.png'),
    'cockerel': Image.open(directory + 'cockerel.png'),
    'hurricane': Image.open(directory + 'hurricane.png'),
    'philosopher': Image.open(directory + 'philosopher.png'),
    'tadpole': Image.open(directory + 'tadpole.png'),
    'expensive': Image.open(directory + 'expensive.png'),
    'saucepan': Image.open(directory + 'saucepan.png'),
    'forgiven': Image.open(directory + 'forgiven.png'),
    'biology': Image.open(directory + 'biology.png'),
    'fledgeling': Image.open(directory + 'fledgeling.png'),
    'murderer': Image.open(directory + 'murderer.png'),
    'pressure': Image.open(directory + 'pressure.png'),
    'Yahrzeit': Image.open(directory + 'Yahrzeit.png'),
    'although': Image.open(directory + 'although.png'),
    'pasta': Image.open(directory + 'pasta.png'),
    'sister': Image.open(directory + 'sister.png'),
    'saddle': Image.open(directory + 'saddle.png'),
    'December': Image.open(directory + 'December.png'),
    'dependency': Image.open(directory + 'dependency.png'),
    'beige': Image.open(directory + 'beige.png'),
    'cranberry': Image.open(directory + 'cranberry.png'),
    'Japan': Image.open(directory + 'Japan.png'),
    'tomb': Image.open(directory + 'tomb.png'),
    'wilderness': Image.open(directory + 'wilderness.png'),
    'functional': Image.open(directory + 'functional.png'),
    'polisher': Image.open(directory + 'polisher.png'),
    'weather': Image.open(directory + 'weather.png'),
    'promise': Image.open(directory + 'promise.png'),
    'brush': Image.open(directory + 'brush.png'),
    'zoology': Image.open(directory + 'zoology.png'),
    'zoologist': Image.open(directory + 'zoologist.png'),
    'museum': Image.open(directory + 'museum.png'),
    'spiral': Image.open(directory + 'spiral.png'),
    'windmill': Image.open(directory + 'windmill.png'),
    'slang': Image.open(directory + 'slang.png'),
    'frustration': Image.open(directory + 'frustration.png'),
    'drumstick': Image.open(directory + 'drumstick.png'),
    'November': Image.open(directory + 'November.png'),
    'function': Image.open(directory + 'function.png'),
    'funnel': Image.open(directory + 'funnel.png'),
    'receipt': Image.open(directory + 'receipt.png'),
    'north': Image.open(directory + 'north.png'),
    'triangular': Image.open(directory + 'triangular.png'),
    'rectum': Image.open(directory + 'rectum.png'),
    'ear': Image.open(directory + 'ear.png'),
    'count': Image.open(directory + 'count.png'),
    'dangerous': Image.open(directory + 'dangerous.png'),
    'smooth': Image.open(directory + 'smooth.png'),
    'excitement': Image.open(directory + 'excitement.png'),
    'carriage': Image.open(directory + 'carriage.png'),
    'cello': Image.open(directory + 'cello.png'),
    'problem': Image.open(directory + 'problem.png'),
    'minutes': Image.open(directory + 'minutes.png'),
    'skating': Image.open(directory + 'skating.png'),
    'hydrotherapy': Image.open(directory + 'hydrotherapy.png'),
    'pin': Image.open(directory + 'pin.png'),
    'Tevet': Image.open(directory + 'Tevet.png'),
    'domino': Image.open(directory + 'domino.png'),
    'year': Image.open(directory + 'year.png'),
    'pig': Image.open(directory + 'pig.png'),
    'tabletop': Image.open(directory + 'tabletop.png'),
    'goodness': Image.open(directory + 'goodness.png'),
    'education': Image.open(directory + 'education.png'),
    'visa': Image.open(directory + 'visa.png'),
    'fencing': Image.open(directory + 'fencing.png'),
    'boot': Image.open(directory + 'boot.png'),
    'book': Image.open(directory + 'book.png'),
    'boom': Image.open(directory + 'boom.png'),
    'branch': Image.open(directory + 'branch.png'),
    'chemist': Image.open(directory + 'chemist.png'),
    'February': Image.open(directory + 'February.png'),
    'star': Image.open(directory + 'star.png'),
    'ecstatic': Image.open(directory + 'ecstatic.png'),
    'April': Image.open(directory + 'April.png'),
    'astronomy': Image.open(directory + 'astronomy.png'),
    'veil': Image.open(directory + 'veil.png'),
    'inspiration': Image.open(directory + 'inspiration.png'),
    'baker': Image.open(directory + 'baker.png'),
    'jewel': Image.open(directory + 'jewel.png'),
    'flatfish': Image.open(directory + 'flatfish.png'),
    'atheism': Image.open(directory + 'atheism.png'),
    'gynecologist': Image.open(directory + 'gynecologist.png'),
}

baseheight = 100
bg = Image.new("RGBA", (500, 500), (255, 255, 255, 255))
sym = blissDict["gynecologist"]
over = Image.new("RGBA", (sym.width, sym.height), (255, 255, 255, 0))
over.paste(sym, (250,250))

hpercent = Decimal(baseheight) / Decimal(over.height)
wsize = Decimal(over.width * 0.1)
over = over.resize((wsize, baseheight))
bg.paste(over)
bg.show()



def createTranslationDict(lex):
    """
    Used with lexicon to construct blissDict.

    :param lex: complete lexicon of origin language
    :return: translation dictionary between origin and destination language
    """
    dict = {}

    for term in lex.split("\n"):
        if term.isalnum():
            for part in term.split(","):
                dict[part] = "Image.open(directory + '" + term + ".png'" + ")"

    print("{")

    for entry in dict:
        print("    '" + entry + "': " + dict[entry] + ",")

    print("}")


lexicon = """
exclamation_mark
percent,percentage,%
question_mark
period,point,full_stop,decimal_point
comma
colon
zero_(digit),0
one_(digit),1
two_(digit),2
three_(digit),3
four_(digit),4
five_(digit),5
six_(digit),6
seven_(digit),7
eight_(digit),8
nine_(digit),9
zero_(index_number)
one_(index_number)
two_(index_number)
three_(index_number)
four_(index_number)
five_(index_number)
six_(index_number)
seven_(index_number)
eight_(index_number)
nine_(index_number)
a_(lowercase)
b_(lowercase)
c_(lowercase)
d_(lowercase)
e_(lowercase)
f_(lowercase)
g_(lowercase)
h_(lowercase)
i_(lowercase)
j_(lowercase)
k_(lowercase)
l_(lowercase)
m_(lowercase)
n_(lowercase)
o_(lowercase)
p_(lowercase)
q_(lowercase)
r_(lowercase)
s_(lowercase)
t_(lowercase)
u_(lowercase)
v_(lowercase)
w_(lowercase)
x_(lowercase)
y_(lowercase)
z_(lowercase)
A_(uppercase)
B_(uppercase)
C_(uppercase)
D_(uppercase)
E_(uppercase)
F_(uppercase)
G_(uppercase)
H_(uppercase)
I_(uppercase)
J_(uppercase)
K_(uppercase)
L_(uppercase)
M_(uppercase)
N_(uppercase)
O_(uppercase)
P_(uppercase)
Q_(uppercase)
R_(uppercase)
S_(uppercase)
T_(uppercase)
U_(uppercase)
V_(uppercase)
W_(uppercase)
X_(uppercase)
Y_(uppercase)
Z_(uppercase)
indicator_(action)
indicator_(active)
indicator_(conditional)
indicator_(description_after_fact)
indicator_(description_before_fact)
indicator_(description)
indicator_(future_action)
indicator_(future_conditional)
indicator_(future_passive)
indicator_(future_passive_conditional)
indicator_(passive)
indicator_(past_action)
indicator_(past_conditional)
indicator_(past_passive_conditional)
indicator_(past_passive)
indicator_(present_passive_conditional)
indicator_(thing)
indicator_(things)
indicator_(plural)
a,an,any
ability,capability,capacity,potential
abortion_(induced)
about,concerning,in_relation_to,of,on
absorbent_material,sponge
celibacy,chastity,abstinence
abuse,assault,violence
accessory
accident,chance_event
account
ache
acne
across
action,act,deed
activity,male_gender_(in_combinations)
active,actively
Adar
add,gain-(to)
addition,gain
adolescence
adult,grownup
adult,mature
advance,go-(to)
advertisement
advice,counsel,recommendation
advise,counsel,recommend-(to)
afraid,frightened,scared
after,behind
afternoon
again
against,opposed_to
ago,then_(past)
agree-(to)
agreement
aid,device,support
air,atmosphere
airplane,aeroplane,plane
airport
alcoholic_drink,alcoholic_beverage,liquor
all,every,everything,total,whole
all_gone
alligator,crocodile
alone,just,only,solitary
along_with
alpana,rangoli_(decoration)
alphabet,letters_(lowercase)
although
always,ever,forever
ambulance
amenorrhea
amphibian
amuse,entertain,please-(to)
anal_intercourse
and,also,plus,too
angel_(OLD)
angle
angry,angrily,mad
animal,beast
animal_(bovine),bovine,ovine
dog,canine_(animal),canid
deer,cervine_(animal),cervid
domestic_animal
cat,feline_(animal),felid
kangaroo,marsupial_(animal),pouched_mammal
animal_(protected)
rat,rodent,gnawer,gnawing_animal
animal_skin,hide,pelt
lizard,reptile_(snake_like_animal)
animal_(water)
animal_(wild)
ankle
anniversary
answer,reply
answer,reply-(to)
ant
anus
anxiety
anxious,anxiously
anyone,anybody,somebody,someone
anything,something
anytime,sometime
anywhere,anyplace,someplace,somewhere
apartment,flat,unit
apologize,apologise,regret_(express)-(to)
apple
appointment
approach
approve-(to)
apricot
April
apron,coverall,smock,overall
architect
argue,dispute,quarrel-(to)
argument,dispute,quarrel
arm
armchair
military,armed_forces,armed_services
around
art
art_gallery,gallery
artificial_insemination
artificial_respiration
give_artificial_respiration,resuscitate,revive-(to)
ashes
ashtray
ask,inquire,question-(to)
asleep
astronaut,cosmonaut
at
atom
attack_(of_illness)
attention
August
aunt
autumn,fall_(ckb)
autumn,fall
Av
avocado
awake
away,at_a_distance,off_(OLD)
baby,infant
baby_boy
baby_carriage,buggy,pram,pushchair,stroller
baby_clinic
baby_girl
babysitter
back_(body)
back_and_forth,backward_and_forward,to_and_fro
backpack,rucksack
back_up-(to)
backward,back
bacon
bad,wrong
badge,shield
badminton_(activity)
baggage,bag,luggage,suitcase
bake,cook,roast-(to)
balcony,porch,veranda
ball
balloon
banana
band,orchestra_(OLD)
bandage,dressing
bank
bar,pub
barber,hairdresser
barbershop,beauty_shop
barn,stable,shed
barrier_(contraceptive)
baseball_(activity)
base_camp
basketball_(activity)
bat_(sport)
bat_(animal)
bathroom,washroom
battery
be,am,are,is,exist-(to)
beach,bank,coast,shore
beach_tennis_(activity)_(OLD)
bean
bear
beard
beautiful,attractive,good-looking,handsome,pretty
beaver
because
become-(to)
bed
bedroom
bee
beef
beer
beet
beetle
before,in_front_of,prior_to
begin,start-(to)
beginning,start
behaviour
belief
believe-(to)
bell
belongs_to,of_(possessive)
belt,sash
bench,pew
berry
best
better
between
beyond,past_(OLD)
bib
bicycle
big,large
bindi,tika_(decoration)
bird
bird_(domestic)
bird_(protected)
duck,bird_(water),waterbird,waterfowl,seabird,seafowl
bird_(wild)
birth_(reproduction)
birth
birth_control
birth_control_pill,pill
birthday
bite-(to)
bitter
black_(bci)
black_(ckb)
blackbird,crow,raven
blackboard,chalkboard,whiteboard,writing_board
bladder
blanket,duvet,quilt
bleed-(to)
blind
blissymbol
blissymbol_part
blissymbolics_resource_centre
block,brick
blood
blow_(wind)-(to)
blow_(mouth)-(to)
blue_(bci)
blue_(ckb)
blueberry
bluebird
board_(material)
boat,ship
body,trunk
boil_(food)-(to)
boil_(liquid)-(to)
bone
bonfire,barbeque,campfire
book
boot
borrow-(to)
boss,supervisor_(OLD)
both
bottle,flask
bottom,base
bow_(knot)
bowel,intestine_(OLD)
bowel_movement,defecation,shitting,feces,shit,poop
bowling_(activity)
box,cube
boxing_(activity)
boy,lad
bra,brassiere
medical_aid
bracha,berakah,prayer_(small)
Brahma
brain
branch
bread,loaf_of_bread,loaf
break,crack,fracture,tear-(to)
breakable,fragile
breakfast
breasts
breath
breathe-(to)
bridge,overpass
bright
bring-(to)
broccoli
broil,barbecue,grill-(to)
broken
broom
brother
brown_(bci)
brown_(ckb)
brush
brush-(to)
brush_teeth-(to)
brussels_sprout(s)
bubble
buffalo,bison
bulb_(flower)
bull
bull_(fighting)
burn-(to)
burned,burnt
burning
burp,belch-(to)
bury_(person)-(to)
bus,coach
bus_stop,bus_bay_(OLD)
bus_driver
bush,shrub
business,economy,commerce,trade
but,except
butter
butterfly,moth
buttocks,bottom,bum,rear,ass
button,gripper,snap
buy,purchase-(to)
by,by_means_of,of
cabbage
cabin,cottage,hut
caesarean_section,C-section
cafe,coffee_house,snack_bar
cage
cake,bread_with_sugar
calculate-(to)
calculator
calendar
camel
camera
camp
camper,caravan,mobile_home
can,be_able-(to)
cylinder,can
Canada
candle
candy_(OLD)
cane,stick,walking_stick
cannon,gun
car,automobile,motor_vehicle
cards,playing_cards
careful
carrot,vegetable_(wedge-shaped)
carry,move,transport-(to)
carrycot,bassinet
cart,carriage
cassette,audiocassette,videocassette
cast_(medical)
catch,grab-(to)
caterpillar
cauliflower
cause
cause-(to)
be_caused_by-(to)
cave
cavity,caries
ceiling
celery
celibacy,chastity
cemetery
cent
century
cereal
certain_(OLD)
cervix
chair,seat
challah
chameleon
change,alteration
change,alter-(to)
Chanukah,Hanukkah
charity
cheap_(OLD)
cheek
cheese
chemical_product
cherries
Cheshvan
chest
chest_of_drawers,bureau,dresser
chew-(to)
chicken_(bird)
chicken_(food),poultry
child,kid,youngster
child_abuse
chimney
chin
chipmunk
chocolate_(OLD)
chocolate_drink_(OLD)
chocolate_flavouring,cocoa,cacao_powder_(OLD)
chocolate_spread_(OLD)
choice,selection,election
choir,chorus
choke,gag-(to)
choose,pick,select-(to)
chop-(to)
christian
Christmas
Chumash,Pentateuch
church,mosque,temple
cigarette
circle
circumcision
citizen
town,city_(small)
class
classroom
claw_(animal)
claw_(bird)
clean_(OLD)
clean-(to)
clear,transparent
clerk
climb-(to)
clinic
clitoris
clock,timepiece
close,enclose,shut-(to)
cloth,fabric,material,textile,net
clothing,clothes,garment
cloud
cloudy
club
biomass,biofuel
coat,jacket,jumper,sweater
coconut
coffee
coin
cold
cold_(opposite_hot)
colour
comb
comb-(to)
combination,connection
combine,connect,link-(to)
indicator_(combine)
come,approach-(to)
comet
comfort,console-(to)
comfortable,restful
commandments
communicate-(to)
communication
compare-(to)
compete,race-(to)
composer
computer_(OLD)
conception,fertilization,fertilized_egg
concert_hall
concrete,cement
condom
conductor_(music)_(OLD)
cone
conscience
considerate,thoughtful
container,bowl,holder,pouch,basket
continue,pass-(to)
uterine_contraction
contrast-(to)
control_oneself-(to)
cook-(to)
cookie,biscuit
cool,chilly
cool,chilly_(opposite_warm)
copy,duplicate
corn
corner_(room)
cornmeal
correct,accurate,good,right
cost,price
costume,disguise
couch,chesterfield,sofa
cough-(to)
counsellor,adviser
count-(to)
country,state
countryside,country
couple_(heterosexual)
couple_(two_persons)
family,couple
court,field_(OLD)
cousin
cow
craft
cramp,spasm
cranberry
crane
crash_(forward)
crash_(downward)-(to)
crash_(air)
crash_(car)
crash_(forward)-(to)
crash_(downward)
crawl-(to)
crayon,coloured_pencil,marker
cream
create-(to)
creation,nature
creative
creature,being
crescent
crochet-(to)
croquet_(activity)
cross,Christianity_(in_combinations)
cross-(to)
crotch
crush,squeeze-(to)
crutches
cry,weep-(to)
crystal
cucumber
mug,cup
cupboard,closet,wardrobe
currants
current
current_events
curtain(s),drape(s)
curve,curved_line
cut_(scissors)-(to)
cut_(knife)-(to)
cutlery
dance-(to)
danger
dangerous
dark_(OLD)
date_(man_woman)
date_(two_persons)
date_(fruit)
daughter
day
daycare
day_care_centre
dead,deceased
deaf
dear
death
decade
December
decide-(to)
decision
decoration_(OLD)
decrease,reduce-(to)
deep
deep-fry-(to)
Denmark_(OLD)
dental_floss
dentist
deodorant
departure
depression
descend,go_down-(to)
describe-(to)
desirable
desk,worktable,work_table
dessert
destroy,annul,cancel,cross_out,delete-(to)
develop-(to)
development
dhoti,lungi
diamond_(shape),rhombus,rhomb
diaper,nappy
diaphragm_(contraceptive),pessary
die-(to)
diet
diet-(to)
different,other,difference
difficult,hard
dig-(to)
digest-(to)
digestion
dining_room
dinosaur_(OLD)
direction,cardinal_point
dirty,soiled
disability,handicap,impairment_(OLD)
disc,disk
disco
discomfort
discuss,converse,debate-(to)
discussion,conversation,debate,chat
dish,plate,platter
dislike
dislike-(to)
divide-(to)
division
divorce
divorce-(to)
do,act-(to)
doctor,physician
doll
dollar
dolphin,porpoise_(etc)
donkey,mule
door
dot
doubt-(to)
down,downward
downward_and_backward
downward_and_forward
drain,sift,strain-(to)
draw,sketch-(to)
drawer
dream-(to)
dress
dress,wear-(to)
dress_up,disguise-(to)
dressing_gown,housecoat,robe
dried_bean_(OLD)
drink,beverage
drink-(to)
drive-(to)
driver,chauffeur
dromedary
drunk
dry_(OLD)
dry-(to)_(OLD)
duck_(food)
dump_truck,dumper,tipper_lorry,tipper
Durga
during,while
each,every
ear
ear_mold
early
earmuffs_(protection)
earn-(to)
earphones,headphones
earth,globe,world
earth,ground,land
east
easter
eastern
easy_(OLD)
eat-(to)
edge
education
eel
effect,result
egg,ovum_(1)
egg,ovum_(2)
eggplant
either
ejaculation
elbow
electric,electrical
electricity
electric_light,lamp
electric_wheelchair
electric_wire,electric_cord,cord,cable,lead
electromagnetic_radiation
elephant
elevator,lift
Elul
embarrassed
embarrassing
embarrassment
embryo
emergency
empathy
empty_(OLD)
empty-(to)_(OLD)
enclosure
end,arrival,stop
energy
engaged
enjoy-(to)
enough
enter,absorb,insert,penetrate-(to)
envious
environment
equal-(to)
erection,erect_penis
eternal_life,immortality_(after_death)
etrog
evaluate-(to)
appreciate,value,treasure-(to)
evaluation,value
evening
evening_before_holiday,evening_of_Sabbath
event,happening,occasion
ever,whenever
evergreen_tree,spruce,fir,fir_tree
everybody,everyone
exchange,substitute,trade-(to)
ecstatic
ecstasy
exclude-(to)
excuse
excuse-(to)
exercise,work_out-(to)
exhibitionism,immodesty,indecent_exposure
exit-(to)
expect,anticipate-(to)
expectation,anticipation
expensive_(OLD)
explain,give_a_reason-(to)
explode,blow_up,detonate,burst-(to)
explosion,detonation,blowup
eye
eyebrow
eyebrow_pencil
eyelid_(upper)
eye_makeup
face
fact
factory,plant
falafel
fall-(to)
fallopian_tube
family_(traditional)
family_(cohabiting)
police_force,police
family_planning
family_planning_clinic
fan
far,distant_(OLD)
farm
farmer
fast_day
fasten,attach,join,append,connect-(to)
fastener,gripper,velcro,zipper
fat,thick_(OLD)
father,dad,daddy,papa,pa,pop
favourite
fear,be_afraid,dread-(to)
feather
February
feed-(to)
feel-(to)
feeling,emotion,sensation
female,feminine_(person)
female_(gender)
fence,wall
fertile
fertility_counselling
fetus
few,little_(OLD)
fidelity,loyalty,solidarity
field
field_hockey,hockey_(activity)
fight,combat-(to)
fill-(to)
film
finally,at_last
find-(to)
finger
finish,complete-(to)
Finland
fire
firefighter,fireman
fireplace
fire_truck,fire_engine
first,primary
fish_(animal)
fish_(food)
fish-(to)
fishing
fix,mend,repair-(to)
flag
flame
burnable,combustible,ignitable
flashlight,lantern
flat
flavouring,condiment,seasoning
flea
float-(to)
flood
floor
floor_covering,linoleum
flour
flower
flower_(from_bulb)
flower_(protected)
wildflower
fly
fly-(to)
flying
fog
fold,pleat-(to)
follow-(to)_(OLD)
food
food_ball
foot
football,soccer_(activity)
for_(in_exchange_for)
for_(the_purpose_of),in_order_to
forced,compelled,obliged
forehead
foreskin
forest,bush,wood,woods
forget-(to)
forgive,pardon-(to)
fork
forward
foster_mother
foster_parent
four_o'clock_eating_break
fox
free,freely
freedom,liberty
freeze,solidify-(to)
French_fries,chips_(OLD)
fresh
Friday_(OLD)
friend
frog,toad
from
food_(frozen)
fruit
fruit_juice,juice
fruit_yogurt,fruit_yoghurt
frustrated
frustrating
frustration
fry,saute-(to)
fuel
full
funny,humorous
fur,coat_(animal),hair_(animal)
furniture
future
game
Ganesh
garage
garbage_can,rubbish_bin,trash_can
garden
garlic
gas
gasoline
gather,assemble-(to)
gathering,assembly,meeting,conference
gender,sex
indefinite
generalization
genitals,sex_organs
genitals,sex_organs_(female)
genitals,sex_organs_(male)
gerbil,guinea_pig,hamster
get,acquire,receive-(to)
ghost_(OLD)
gift,offering,present
giraffe
girl
give,offer,provide-(to)
glass_material
glass,drinking_glass
glasses,eyeglasses
glassware
sports_glove,glove,mitt
glove(s),mitt(s),mitten(s)
glue,adhesive,paste
glue,paste,stick-(to)
go,depart,leave-(to)
goal
God
goldfish,guppy,pet_fish
golf_(activity)
goodbye,farewell
Good_Friday
goodness
goods,contents
goose_(bird)
goose_(food)
gopher,ground_hog
govern,rule-(to)
government_(OLD)
good,well,fine,ok,okay,all_right
grain,cereal
grandfather,granddad,grandpa
grandfather_(maternal)
grandfather_(paternal)
grandmother,grandma,granny
grandmother_(maternal)
grandmother_(paternal)
grandparent
grape_juice
grapefruit
grapes
grass
grasshopper
grave
gray,grey
great_experience
green_(bci)
green_(ckb)
greenhouse,glasshouse,hothouse
green_onion,scallion,spring_onion
grocery_store,food_store,supermarket_(OLD)
group
group_of,much_of,many_of,quantity_of
grove
grow-(to)
guard_duty
guess,estimate-(to)
guilt
guilty
gull,seagull,sea_gull
gun,firearm
gym,gymnasium_(OLD)
gym_mat_(OLD)
Haggadah
hail
hair
hair_(head)
Halloween,All_Saint's_Day_(OLD)
halva,halvah,halwa
hamburger_(OLD)
hamentasch
hammer,gavel,mallet
hand
handbag
handball_(activity)
handgun,pistol
handkerchief
handmade_object,handicraft
hang,hook-(to)
happen,occur-(to)
happiness,fun,joy,pleasure
happy,glad,gladly,happily
harassment
harbour
hard_(OLD)
harmony,harmoniousness,concord,concordance
harvest
hat,cap,hood
hate-(to)_(OLD)
Havdalah
have-(to)
hawk,eagle
he,him,himself
he,she,him,her,one
head
health
healthy,well
hear,listen-(to)
hearing_aid
hearing-impaired_(OLD)
heart
heat
heat-(to)
heavy
hedgehog_(OLD)
heel
helicopter
hello,greetings
helmet_(OLD)
help,aid,assistance,support
help,aid,assist,serve,support-(to)
helper,aide,assistant,personal_assistant
her,hers
here
heterosexuality
hide,conceal-(to)
high,tall
hill
hip
hippopotamus
his
his,her,hers,one's
hit-(to)
hobby,pastime
hoist,lift
hold,contain_(1)-(to)
hole
holiday,festival
home
home_run
homosexuality_(female),lesbianism
homosexuality_(male)
honey_(spread)
honey_(food)
hook,hanger
hop-(to)
hope-(to)
horizon
trumpet,horn,cornet_(1)
horn(s)
horse
horseradish
hospital,clinic
hot_(temperature)
hot,spicy,peppery
hot_dog,frankfurter
hotel,motel
hour,o'clock
house,building,dwelling,residence
how
how-(question)
how_much,how_many
hug,cuddle,embrace-(to)
humble,meek
hummus
hungry
hurt,pain_(feel),suffer-(to)
husband
hysterectomy
I,me,myself
I,me,myself-(feminine)
I,me,myself-(masculine)
ice
ice_cream_(OLD)
ice_cream_(cone)
ice_hockey_(activity)
Iceland
ice_skates
icy,frozen
idea,thought
if
immoral,bad,wrong
important,significant
improve-(to)
in,inside,interior,internal
incest
include-(to)
incorrect,bad,inaccurate,wrong
increase,enlarge-(to)
Independence_Day_(Israel)
indigo
infertile,sterile
infinite,limitless_(OLD)
injection,inoculation,shot
injure,hurt-(to)
insect,bug
insect_(pest)
instruction,teaching
instruction(s),direction(s)
intensity
interesting,interested
international
intimacy,closeness
intimate,close
into
invent-(to)
Ireland
iron,smoothing_iron
iron-(to)
ironing_board
island
Israel
it
apparent(ly),clear(ly),evident(ly),obvious(ly),plain(ly)
its
intrauterine_device,IUD
Iyar
jam,jelly,marmalade,preserves
January
jealous
Jerusalem_Day
Jesus_(of_Nazareth),Jesus_Christ,Christ
jet,jet_plane
jewel
Jewish
joint
joke-(to)
July
jump_rope,skipping_rope
jump-(to)
June
Kabbalat_Shabbat
Kali
keep,preserve,save-(to)
key
kibbutz
kick-(to)
kiddush,blessing_over_wine
kill,murder-(to)
kind,kindly
Kislev
kiss
kiss-(to)
kitchen
kite
kitten_(OLD)
knee
kneel-(to)
knife,sword
knit-(to)
know-(to)
knowledge,class_(in_combinations)
koala
eyeliner,kohl
labour
ladder
Lag_B'Omer
lake,pond
Lakshmi
lamb,mutton
landing,airplane_landing
language
last,final
last_night
last_week
last_year
late
laugh-(to)
laundromat,launderette,laundry
lawn,meadow
lead,direct,guide-(to)
leader,director,guide_(2)
leaf
learn-(to)
fewest,least
leather
left
leg
legs_and_feet
lemon
lemonade
lend,loan-(to)
length,longness
leopard
fewer,less
let,allow,permit-(to)
let_us,let's
letter,mail,post
letter_carrier,postman,mailman
lettuce,leafy_vegetable
library_(building)
library_(room)
lie_(OLD)
lie-(to)_(OLD)
lie_down,lie-(to)
life
lift,raise-(to)
light
lightning
like-(to)
lime
limited_time,interval,period,awhile,for_a_while
limit(s),limitation_(OLD)
line,stripe
linear,straight
linear_thing,pole
lion
lip(s)
lipstick
list,inventory
little,small
live_(life)-(to)
live,dwell,reside-(to)
living_room,lounge,sitting_room,front_room,parlor,parlour,waiting_room
crab,shellfish_(with_claws)
lock-(to)
lonely,lonesome
long
longer
longest
lose_(fail_to_keep)-(to)
lose_(fail_to_win)-(to)_(OLD)
loss
loud,noisy
lovable
love,affection
love-(to)
low,short
luck,fortune
lucky,fortunate
lulav
lunch,dinner
machine,appliance,engine,motor
magazine,journal
mail,post-(to)
mailbox,letterbox,postbox
make,manufacture,produce-(to)
make-believe,pretend,imaginary
maker,manufacturer,producer
makeup
male,masculine_(person)
man,male
male_genitals_(man_with_penis)
manager,secretary
mango
man-made
map
maple-leaf
March
margarine
marriage
marry-(to)
mash,crush,squeeze,squash_(food)-(to)
mask,false_face
masturbation
match
material,raw_material,stuff
mathematics,arithmetic,math_(2)
maturation
matzo
May
possibility
congratulate-(to)
meal
mean,cruel
mean,signify-(to)
meaning,sense,significance
measure-(to)
measurement,measure
meat
meatball
medical,medically
medical_insurance
medicine,medication
meet,encounter,see-(to)
meeting,assembly,conference
Megillah_(Book_of_Esther)
melon
menopause
menorah
menstruation,menstrual_period,period
mental,intellectual,rational,thinking
disabled,handicapped_(intellectually,mentally)_(OLD)
merry-go-round,carousel
metal
metaphor
mezuzah
microwave-(to)
microwave_oven
middle,centre
midsummer
military_plane
military_reserve_duty
milk
milkman
milkshake
mind,intellect,reason
mine
minister,pastor,preacher,priest,rabbi
minus,no,without
minute
arrow_(bent)
miscarriage,abortion_(spontaneous)
miss,lose-(to)
mistake,error,fault
mite,tick
mix,blend-(to)
recreation_room,moadan
Monday_(OLD)
money,cash
monkey,ape,gorilla,primate
monster
congratulations,best_of_luck,mazel_tov
month
mood
moon
moose,elk
moral,good,right
more
morning_(before_noon)
morning_(early)
mortal
moshav
Muslim,Moslem,Islamic
mosquito
most,maximum
mother,mom,mommy,mum
mountain
mountain_berry,cowberry,lingonberry
mouse
mouth
move-(to)
move_bowels,defecate,stool,shit,ca-ca-(to)
movie,film
movie_theatre,cinema
much,many,very
mud,clay
multiplication
multiply-(to)
multitude
muscle_(OLD)
museum
mushroom
music
musical_group
musical_instrument
musical_note
musician
muskrat
must,have_to,be_forced_to-(to)
my,mine
my,mine-(feminine)
my,mine-(masculine)
nail
nail_polish,nail_varnish
name,label,term,title
napkin,serviette
narrow
naughty
naughty,not_nice
navy
near,almost,close,nearly
necessary,necessarily,needed
neck_(head)
neck_(body)
need_(needy_person)
need-(to)
needle
hypodermic_needle
neighbour
neither
nephew
Netherlands_(The),Holland
never_(OLD)
new
New_Year's_Day
news
newspaper,bulletin,newsletter
next
next_week
next_year
nice,pleasant
niece
night
nipple(s)
Nisan,Nissan
no-(exclamatory)
no_one,nobody
nocturnal_emission,wet_dream
none,nothing_(OLD)
nonsense
nonsense-(exclamatory)
nonspeaking
nor
north
northern
nose
not,negative,no,don't,doesn't
notebook,writing_book
November
now
nowhere,no_place
nuclear_energy
nuclear_fallout,radioactive_dust
nuclear_radiation,radioactivity
nucleus
number
nurse
nut
obey,comply-(to)
observe-(to)
ocean,sea
October
office
offspring,child
often,frequent,frequently
oil,lubricant
old_(opposite_new)_(OLD)
old,elderly
olive
on
once
bulb_(plant)
open
open-(to)
opening
operation
opinion
opossum,possum
opposite_meaning,opposite_of,opposite
opposition,counter_purpose
or
oral_sex
orange_(bci)
orange_(ckb)
orange,citrus_fruit
orchard
organize,arrange-(to)
orgasm
ostrich
other,another_(person)
our,ours-(feminine)
our,ours-(masculine)
our,ours
out,exterior,external,outside
out_of,exit_(forward)
out_of,exit_(downward)
outing,excursion
oval,ellipse
ovary
over,above,superior
owl,night_bird
own,possess-(to)
ox
oyster,clam
pail,bucket
pain,suffering
painful,painfully,sore
paint,dye
paint,dye-(to)
painter
pair
palm
pants,jeans,slacks,trousers
paper,card,page
parakeet,budgie
parallel
paratrooper
parcel,package
pardon,what_did_you_say
parent
park
parrot,myna,talking_bird
parsnip
part,bit,piece,portion,part_of
party,festival
Passover
past
patience
be_patient-(to)
paw
pay,spend-(to)
peace_(opposite_war)
peace,peace_of_mind,serenity
peaceful,serene,calm
peach,nectarine
peacock
peanut_butter
pear
peas
peel
peel-(to)
pelican
pen,pencil
penetrate,go_through-(to)
penguin
penis
pepper_(vegetable)
pepper_(seasoning)
perfume,fragrance,aroma,scent
perpendicular
person,human_being,individual,human
kneeling_(kneeling_person)
reclining,lying_(person_lying_down)
illness,disease,sickness_(sick_person)
seat,sitting_(sitting_person)
standing_(standing_person)
weakness_(weak_person)
pet
photograph,photo,pic
disabled,handicapped_(physically)_(OLD)
picnic
picture,image,icon,painting
pie,tart
pier_(OLD)
pig
pill,tablet
pillow,cushion
pillowcase
pilot
pimple,blemish
pin
pineapple
table_tennis,ping-pong_(activity)_(OLD)
pink_(bci)
pink_(ckb)
pipe,smoking_pipe
pipe,hose,tube_(1)
pit,stone
pit,stone-(to)
pita
pitcher,jug,kettle,pot
pizza
place,area,location,space
plan,design,method,system
plan,design-(to)
plant
plastic
stop,platform_(vehicle)_(OLD)
play,recreation
play-(to)
play_football-(to)
playground
playroom,family_room,recreation_room
please
pliers
plough
plug
plum,drupe
pocket
poem
poetry
point,tip,peak
point,indicate-(to)
point_of_view
poison
polenta
police_officer,policeman,policewoman
pollution
pool
poor_(little_money)
popcorn
porcupine_(OLD)
pork,ham
position
positive
maybe,perhaps,possibly
postcard
post_office
pot,pan
potato
potato_chips,crisps_(OLD)
pound_sterling
powder,dust
power_(physics)
practise,practice,drill,exercise,rehearse-(to)
pray-(to)
prayer
prayer_book,Siddur
preceding_(OLD)
pregnancy
pregnant
pregnant_(ckb)
premature_birth
prepare,set,set_up,ready,gear_up,fix-(to)
prepare_food,cook-(to)
present
pretend,make_believe-(to)
prison,jail
private
probable,likely,probably
problem
projector
promise,pledge-(to)
prostitution
protect,cover,shelter,take_care_of-(to)
protection,shelter
protest,object,oppose-(to)
proud
province,county,region,state
prune_(OLD)
puberty
pubic_hair
public_(of_the_public)
public_(not_private)
public_(the_public)
public_room
pull,drag,tow,tug-(to)
puncture,prick-(to)
puppet
puppy
Purim
purple,violet_(bci)
purpose
purse,pocketbook,wallet
push,shove-(to)
put,locate,place-(to)
jigsaw_puzzle
pyjama(s),nightgown,nightie,pajama(s)
pyramid
question
quick,fast,quickly,rapid,rapidly
quiet,quietly
rabbit,hare
rabies
raccoon
race,competition,contest
racket,racquet
radio_(1)
radish
rain
rain-(to)
raincoat
rainy
raise,grow,bring_up,cultivate-(to)
raisins_(OLD)
rake
rape
raspberry,blackberry,compound_berry
raw,uncooked
read-(to)
ready,prepared
real,really
recent,recently
recipe
CD,record
CD_player,record_player,stereo
rectangle,oblong
rectangular,oblong
red_(bci)
red_(ckb)
refrigerator_(OLD)
regret-(to)
reindeer,caribou
less_than_(relation)
greater_than_(relation)
relative,relation
who,that,which-(relative)
religion,naturalism_(OLD)
religious_(OLD)
remember-(to)_(OLD)
remembrance_day
repeat,copy,duplicate,reproduce-(to)
reproduction
request-(to)
resent-(to)
resident
residential_institution,group_home,hostel,residential_home
resource_centre
respect,admiration
rest,comfort
rest-(to)
rest_period,break
restaurant,cafeteria
return
return,come_back,reverse-(to)
rhinoceros
rhyme
rhythm_method
ribbon,tape
rice
rich_(taste)
rich,wealthy
rickshaw
ride-(to)
rifle,shotgun
right
angle_(right),right_angle
ring
rise,ascend,go_up-(to)
river,stream,current
road_(1)
roadrunner_(bird)
rocket,spaceship
rocking_chair
rocking_horse_(OLD)
roll,bun
roller_skate-(to)
roller_skates
roof,cover
room
root(s),rootage,root_system
Rosh_Hashana
rotate,circle,circulate,wind_up,orbit-(to)
roti,chapati,flatbread
rouge,blusher
round,circular
rub,massage-(to)
rug,carpet,mat
rule,regulation
ruler,measuring_stick,tapeline,tape_measure
run-(to)
Sabbath,day_of_rest
sack,bag
sad,sadly,unhappily,unhappy
sadness,sorrow,unhappiness
safe,safely,secure,securely
safety,security
sail_(OLD)
sailboat_(OLD)
sailor
salad
saliva,spit
salt_crystal
salty
same,equal,equality
same_sound
sand
sandal(s)
sandbox,sandpit,sandtray
sandwich
sanitary_napkin,sanitary_towel,tampon
sari
satisfaction,contentment
Saturday_(OLD)
sauce,gravy,relish,dressing_(OLD)
sauerkraut
sauna
sausage,frankfurter,hotdog,hot_dog
saw
say,speak,talk,tell,express-(to)
scales
scarf
scenery,landscape
schach
schedule,timetable
school
science,body_of_learning
scissors
score
scorpion
screw
screwdriver
scrotum
search-(to)
second_(time)
second_(ordinal)
secret
secretary
see,look,watch-(to)
see_you_again
seed
seem-(to)
seesaw,teeter-totter,teeter_board
self,oneself,ego_(person)
self-harm
self-control
selfish,self-centred,self-centered,egoistic,egoistical,egocentric
sell-(to)
semen
seminal_vesicle
send-(to)
sentence,clause,phrase
September
several
sew-(to)
sewing_machine
sex_drive,sexual_urge,libido
sexual_abuse,sexual_assault,sexual_violence
sexual_arousal,sexual_excitement
sexual_harassment
sexual_intercourse,intercourse,copulation
sexual_pleasure
sexuality
shake,jiggle-(to)
shallow
shalom
shame
shampoo
shamrock
shape,form
share-(to)
shark
sharp_(knife)
sharp_(taste),acid,sour
shave_(beard)-(to)
shaver,razor
shaving_soap,shaving_cream
Shavuot
she,her,herself
sheep
sheet(s),bedclothes,bed_linen
shekel
shelf
shell,crust
shelter,refuge
shine,beam-(to)
shirt,blouse
Shiva
shoe
shofar
shopping_centre_(OLD)
short
shorts
shoulder
shout-(to)
shovel,spade
show,demonstrate-(to)
shower
shower-(to)
exhibition_hall,showplace
Shevat,Shvat
sibling(s)
sick,ill
side_(body)
side_(enclosure)
sieve,colander,strainer
sign,advertisement
sign_(OLD)
signature
signature_stamp
silence,quiet
silent
Simchat_Torah
similar,like,alike
similar_looking,looks_similar
similar_sound,sounds_like
simmer,poach-(to)
sin
sin-(to)
sing-(to)
singer
bath,washing
sinner
sister
sit-(to)
Sivan
skateboard
skeleton
ski_boot(s)
ski_pole(s)
skin
skirt
skis_(pair_of)
skullcap,kipa,yarmulke
skunk
sky
sled,sledge,sleigh,toboggan
sleep
sleep-(to)
sleeping_bag
slide
slip,petticoat,half-slip,underskirt
slipper(s)
slow,slowly_(OLD)
smart,bright,clever,intelligent
smash,grind,shatter,splinter-(to)
smell,odour
smell-(to)
smell,give_off_odour-(to)
smell_bad,stink-(to)
smile,grin-(to)
smoke
smoke-(to)
smooth
snack_(food)
snail
snake
water_snake
sneeze-(to)
snow
snow-(to)
snowball
snowflake
snowman
snowshoe_(OLD)
snowstorm
snowsuit,winter_clothing
soap,detergent
social_worker
soda_pop,pop,soft_drink
soft
soldier,warrior
solid_thing
solve-(to)
some,any
sometimes
son
song
songbird,finch,thrush
soon
wound,cut,sore
sorry
sufganiya
sound
sound-(to)
soup,broth
south
southern
space,dimension
spaghetti_(OLD)
special,particular
specific
speech_impaired_(OLD)
sperm
spermicide
spice_box
spider
spiral,curl_(shape)
spit-(to)
splash-(to)
spoon
sport_(OLD)
sport_stick
spot,mark
spouse,cohabitant,partner
spread,paste
spread_(cover_with_spread)-(to)
spring_(ckb)
spring
square_(shape)
square_(description)
squash,pumpkin
squirrel
staff
stairs,steps
stamp
stand-(to)
stander
star_of_David
star
starfish_(OLD)
stay,remain-(to)
steam
steam-(to)
steam_bath
steel
stem,stalk
stepfather
stepmother
sterilization
stick,log
stocking(s),sock(s),pantyhose,tights
stomach,abdomen,belly
stone_material
stone,rock
stop,arrive,end-(to)
store_(OLD)
storeroom
gale
story,report,tale
stove,furnace,heater,oven
strange
stranger
strap,string,velcro,rope,cord
straw,drinking_straw
strawberry
street
string_bean,green_bean,runner_bean,wax_bean
stroke-(to)
strong,powerful
structure,construction
student,pupil
stupid,dumb_(OLD)
subtract,remove,take_away-(to)
subtraction,loss
succeed-(to)
success
suddenly,abrupt,sudden
sugar,sweetener
suggest,propose-(to)
suggestion,proposal
suit
sukkah
Sukkot
summer_(ckb)
summer
summer_day_camp
sun
sunscreen,sunblock,sun_lotion
Sunday_(OLD)
sunny
sunrise
sunset
supper,dinner
support-(to)
surprise-(to)_(OLD)
swallow-(to)
swamp,bog,marsh
swan
sweat,perspire-(to)
sweat,perspiration
sweet_(metaphor)
sweet_(taste)
sweet,confection
sweet_potato,yam
sweetheart,lover
swim-(to)
swimming_pool
swimsuit,swimwear,bathing_suit
swing
swing,sway,rock-(to)
handle
switch-(to)
symbol_display,symbol_board,symbol_chart
synagogue
syringe
table_game
table
tablecloth
tahini,sesame_seed_spread
tail
take,bring,carry,move-(to)
take_away,remove-(to)
takeoff,take-off,airplane_take-off
talcum_powder
tallith
Tammuz
tangerine,clementine,mandarin
tank
tape_recorder
taste
taste-(to)
taxi,cab
taxi_driver,cab_driver
tea
teach,instruct-(to)
teacher,instructor
team
tease-(to)
teenager,adolescent,youth
teeth
telephone
television
temperature
ten_o'clock_eating_break
tennis_(activity)_(OLD)
tent
termite
terrified
terrorist
terrorize-(to)
test,assessment,exam
testicle
Tevet
tefillin
thank-(to)
thanks,thank_you
thanksgiving
that_(there)
too_bad,I'm_sorry,I'm_so_sorry
thaw,melt-(to)
the
their,theirs-(persons)
their,theirs-(indefinite)
their,theirs-(feminine_plural)
their,theirs-(masculine_plural)
then,so,later
therapist_(OLD)
there
therefore,so,so_that
thermometer
thermos,cooler,flask
these
they,them,themselves-(indefinite)
they,them,themselves-(persons)
they,them,themselves-(feminine_plural)
they,them,themselves-(masculine_plural)
thin,slim,narrow
thing,object
think,reason-(to)
thirsty
this
this_week
this_year
those
through
throw-(to)
thumb
thunder
Thursday_(OLD)
ticket,pass
tie,necktie
tiger
time
tiptoe-(to)
tire,tyre
tired,exhausted,weary
Tisha_B'Av
Tishri
tissue
to,toward,towards
toast
toast-(to)
toaster
tobacco
today
toe
together,attached,appended,fastened,joined
toilet
toilet_paper
tomato
tomorrow
tomorrow_night
tongue
tonight
too_much,too_many
tool,instrument
toothbrush
toothpaste
top
dreidel_top
Torah
touch,feel-(to)
towel_(OLD)
toy
toy_animal,stuffed_animal
tractor
traffic
train
trampoline
translate-(to)
transvestite_(female)
transvestite_(male)
travel-(to)
tray
treat
tree
triangle
triangular
tricycle
trip,journey,travel,voyage
trouble
truck,lorry
true,truly,truthful,truthfully
trunk,tree_trunk,bole
trust-(to)
trust,confidence
truth
try,attempt-(to)
Tu_Bishvat
tubal_ligation
Tuesday_(OLD)
tune,melody
turkey_(bird)
turkey_(food)
turn,play
turn-(to)
turnip,rutabaga,vegetable_(large-leafed)
turtle,tortoise
twinkle,shine,sparkle-(to)
type,kind,sort
printer,typewriter
ugh,yuk-(exclamatory)
ugly,unattractive
umbilical_cord
umbrella
uncle
uncomfortable
under,below,inferior
bomb_shelter
underpants,briefs,panties
undershirt
understand,see-(to)
underwear,underclothes
unemployment
unfold-(to)_(OLD)
unidentified_object_(suspected_explosive)
unit,example,sample
United_Kingdom
university
unless
until,till,to
up,upward
up_and_down_(OLD)
upset
upward_and_backward
upward_and_forward
urethra
urinate,make_water,pass_water,micturate,pee,piddle,piss,wee-(to)
urine,piss,pee,piddle,weewee,water
use-(to)
usually,usual
utensil
uterus,womb
vacation,holiday
vagina
Valentine_(card)
Valentine's_Day
valley
van,minibus
vas_deferens
vasectomy
veal
vegetable_(above_ground)
vegetable_(below_ground)
onion,vegetable_(bulb)
vegetable_(cylinder-shaped)
vehicle,carriage,railway_car
video_recorder
village
vinegar
purple,violet_(ckb)
virginity
Vishnu
visit-(to)
visitor,guest
visually_impaired_(OLD)
volcano
volunteer
vomit,throw_up,puke-(to)
voyeurism
vulture
vulva
wading_pool,paddling_pool
wage(s),pay,salary
wagon,cart,truck
waist
wait-(to)
walk,go-(to)
walker
wall
wand
want,desire-(to)
war
warm
wash,bathe,bath-(to)
washable
washcloth,washrag,flannel
washer
washing_machine,washer
waste,garbage,rubbish,trash
watch,wristwatch
watch-(to)
watchful,alert
water,fluid,liquid
we,us,ourselves-(feminine)
we,us,ourselves-(masculine)
we,us,ourselves
weak
weather
weave-(to)
Wednesday_(OLD)
week
weekend_(6-7)
weekend_(7-1)
weigh-(to)
weight
weight_(a)
welcome
west
western
wet,damp,moist,watery
whale
what
what,question_mark
what_kind-(question)
what_(thing)-(question)
wheel
wheelchair
when
when,what_time-(question)
where
where-(question)
which,that-(relative)
which-(question)
whisper-(to)
whistle-(to)
white
who,whom-(question)
who,whom,that-(relative)
whose_(neutral)
whose_(person)
whose-(question)
why-(question)
wide,broad
wife
wiggle,squirm-(to)
wiggly
win-(to)
wind
window
barred_window
wine
wing(s)
wink,blink-(to)
winter_(ckb)
winter_(snow)
winter_(rain)
wipe,dust,polish-(to)
wire,cable
wish,desire-(to)
with
wolf,dingo,wild_dog
woman,female
wood,lumber,timber
wool
word
work,employment,job
work-(to)
work_of_art,art_object
workbook
worker
world
worm
worry
worry-(to)
wow,super,great,neat,cool-(exclamatory)
wrestling_(activity)
wrist
write-(to)
Yahrzeit
yard
yawn-(to)
year
yell,scream-(to)
yellow_(bci)
yellow_(ckb)
yen
yes-(exclamatory)
yesterday
yogurt,yoghurt
Yom_Kippur
you,yourselves-(feminine_plural)
you,yourself-(feminine_singular)
you,yourselves-(masculine_plural)
you,yourself-(masculine_singular)
you,yourselves-(plural)
you,yourself
you_are_welcome,you're_welcome
young
your,yours-(feminine_plural)
your,yours-(feminine_singular)
your,yours-(masculine_plural)
your,yours-(masculine_singular)
your,yours-(plural)
your,yours-(singular)
zebra
zoo
cross_(a)
eternal_life,immortality
star_of_David_(a)
therapist
muscle
sport
sail
sailboat,sailing_boat,yacht
spaghetti
sauce,gravy,relish,dressing
salt
up_and_down
tasty,good,appetizing
mirror
can,tin,jar
hard,firm
religion_(God_based)
religious
religion,naturalism
belief_(supernatural)
believer_(in_God)
believer
Jesus_Christ
devil_(1)
devil_(2)
angel_(2)
angel_(1)
family
religious_ceremony
religious_ceremony_(God_based)
marriage,wedding
marriage_(religious)
funeral_(religious)
funeral
burial
burial_(religious)
bury-(to)
poor_(without_possessions)
football,soccer_(sport)
baseball_(sport)
basketball_(sport)
croquet_(sport)
bowling_(sport)
badminton_(sport)
handball_(sport)
ice_hockey_(sport)
field_hockey,hockey_(sport)
golf_(sport)
rugby,football_(N.A.)
wrestling_(sport)
judo
boxing_(sport)
skiing_(sport)
skiing_(activity)
board
stable
carriage
tennis,racquet_sports_(OLD)
table_tennis,ping-pong_(sport)_(OLD)
beach_tennis_(sport)_(OLD)
team_(sport)
snack_(meal)
bun_(food)
hamburger
chocolate_flavouring
chocolate_drink
monotheism
polytheism
Christianity
Judaism
Islam
Eastern_Orthodox_Church
Christian_(person)
Jew
Muslim,Moslem
Muhammad,Mohammed,Muhammed
Allah
supernatural-(noun)
Vatican,Vatican_City
Roman_Catholicism,Roman_Catholic_Church
protestantism
grace
divine,holy
bandy_(sport)
Messiah
spirit
soul
Mary_(Mother_of_Christ)
Joseph,Saint_Joseph
prophecy
prophesy-(to)
prophet
predict-(to)
follow-(to)
leader,director,guide_(1)
religious_leader
bishop
Pope
disperse,disseminate,scatter,spread-(to)
apostle
missionary
horn(s),antler(s)
hell
Adam
Eve
Noah
Abraham
Moses
holy_book
Bible_(Christian)
Old_Testament
New_Testament
Koran
hymnal,hymn_book
hymn,psalm,gospel_song
missal,liturgical_book
gospel
appearance,manifestation
appear-(to)
disappearance
disappear-(to)
holiness
holy
sanctify,consecrate-(to)
saint
Holy_Infant
sanctity_of_life
Holy_City
Holy_Family
single_parent
single_mother
single_father
single_parent_family
family_(group_home)
religious_event
ceremony
meditate-(to)
insight
confess-(to)
Christian_event
holy_event
sacrament
sacrament_of_baptism
sacrament_of_confirmation
sacrament_of_communion
sacrament_of_absolution
sacrament_of_holy_orders
sacrament_of_marriage
sacrament_of_anointment_of_sick
confirmation
bat_mitzvah_(Hebrew)
bar_mitzvah_(Hebrew)
circumcision_ceremony
coffin
mausoleum
scatter_ashes-(to)
urn
vase,urn,trophy_cup
tomb
tombstone
cremation
cremate-(to)
revelry
religious_gathering
awful
celebration
celebration_of_life
misericordia_(forgiveness_from_God)
forgiveness,pardon
unforgivable,inexcusable
shiva_(judaism)
mourn-(to)
mystery,unknown
mysterious,unknown
miracle
vision,apparition
atheism
Christian_faith
Christian_hope
Christian_love
Christian_charity
poverty
impoverish-(to)
abstention
obedience
preach-(to)
persuade,convince-(to)
amen
dead_person
dead_(the_dead)
corpse,cadaver
resurrection
ritual
perseverance
persevere-(to)
convert-(to)
conversion
fast
fast-(to)
Ramadan
forefather
foremother
ancestor
all_knowing
all_powerful
unending
eternal_(OLD)
interrogate-(to)
beg,plead-(to)
command,order-(to)
demand-(to)
proclaim,announce-(to)
proclamation,announcement
proclamation_(written)
flyer
correctness
excellence
excellent
perfection
perfect
evangelise-(to)
evangelise_(christian)-(to)
drown-(to)
drown_(cause_to)-(to)
desert
wilderness
huge
enormous
gigantic
manna
uninhabited
fishnet
incense
calling,vocation
calling,profession,career
nag-(to)
oil_lamp
goblet,wineglass
chalice
ampullae
paten,holy_tray
Host,wafer_(in_religious_ceremony)
altar
altar_cloth
vestment
Christmas_tree
interview
interview-(to)
interviewer
universal,world-wide
forgiven
sign-(to)
sign_language
polder_(Dutch)
cell
Euro
astronomy
economics
chemistry
biochemistry
biology
botany
anthropology
zoology
geology
sociology
psychology_(OLD)
history
archeology
meteorology
physics
linguistics
mathematics,arithmetic,math_(1)
scientist,academic
astronomer
economist
chemist
biochemist
biologist
botanist
zoologist
geologist
sociologist
historian
archeologist
meteorologist
linguist
mathematician_(academic)
paediatrician
surgeon
otolaryngologist
orthopaedist
ophthalmologist,oculist
doctor_(rehab,hab)
gynecologist
general_practitioner
cardiologist
neurologist
psychiatrist
central_nervous_system,CNS
psychologist_(researcher)_(OLD)
psychologist_(OLD)
psychology_teacher_(OLD)
therapy
speech_therapist
occupational_therapist
physiotherapist
audiologist
orthoptist
communication_therapist
podiatrist,chiropodist
hydrotherapist
music_therapist
dance_therapist
osteopath
chiropractor
masseur
aroma_therapist
reflexologist
acupuncturist
massage
view_of_life
culture
people,tribe,clan,folk
nation
folk_music
genocide,holocaust
headscarf
veil
helmet
riding_helmet
hockey_helmet
bicycle_helmet,crash_helmet
knee_pad
elbow_pad
protective_mask
suit_of_armour
cap
bliss-name
ball_sports
water_sports
contact_sports
athletics
equestrian_sports
winter_sports
motor_sports
mountain_sports
sky_sports
shooting_sports
gymnastics
mind_sports
table_sports
boating
stickball
volleyball
water_polo
boules
rugby_ball
cricket
wicket
motorcycle,scooter
scooter
scooter_(3_wheeled_electric)
prone_board,scooter-board
handcycle
recumbent_bicycle
tandem_bicycle
mountain_bike
ATB,all-terrain_bike
wheelchair_bike
stander_(wheeled)
sidecar_(motorcycle)
go-kart,kart
cycling
speed_cycling
mountain_biking
motorcycling,motocross
motorcycle_racing
sidecar_(motorcycle_sport)
car_racing,auto_racing
Formula_One,NASCAR_Kart
kart_racing,karting,go-karting
cycle,ride_a_bike-(to)
go_by_car-(to)
go_by_airplane-(to)
go_by_horse-(to)
ride_(horse)-(to)
fencing
martial_arts
running
hurdles
relay
relay_(sport)
high_jump
pole_vaulting
long_jump_(OLD)
shot_put
discus
hammer_throw
chain
dart
javelin_throw
arrow
darts
javelin,spear
bow_and_arrow
archery
multi-sport_event
triathlon
weight_lifting
skating
speed_skating
figure_skating
slalom
downhill_skiing
cross_country_skiing
ski_jumping
freestyle_skiing
snowboarding
snowboard
sled_sport
toboggan
bobsleigh
horse_sled,horse-drawn_sleigh
dog_sled
horse_sled_sport
rocking_horse
dogsled_sport,dogsled_racing
sled_dog
curling
wave
surfboard
sailboard
water_ski
jet_ski
wind_surfing
water_skiing
sailing
canoeing
rowing
motorboat_sport
swimming_(sport)
synchronized_diving,synchro_diving_(sport)
diving_(sport)
synchronized_swimming_(sport)
snorkeling,scuba_diving,deep_sea_diving_(sport)
fishing_(sport)
mast
boom
deck
bow,fore
stern
keel
hull,body
rudder
paddle,oar
paddle_(two_blades)
freighter
tanker
oil_tanker
barge,river_boat
schooner
motorboat
canoe
rowing_boat
kayak
lifeboat
pilot_boat
towboat,tugboat
pushboat
cruise_ship
ferry
steamship
hovercraft
rubber_boat,dinghy
catamaran,pontoon_boat
paddle_boat,pedal_boat,water_bike,pedalo
houseboat
boathouse
horse_rider,equestrian
jockey
sulky
horse_racing
carriage_racing
showjumping_(horse)
dressage
polo
billiards
pool,snooker
squash_(sport)_(OLD)
lacrosse_(sport)_(OLD)
glider
seaplane
parachute
parachuting
balloon_(hot_air)
ballooning
mountain_climbing
abseiling,rappelling
wall_climbing
parasailing
paraskiing
hang_gliding
kite_flying
indoor_(character)
outdoor,outdoors
appetizer,starter,entree
main_course
fishburger
decorated_cake
muffin,bun_(sweet)
cupcake,fancy_cake,pastry
doughnut
bagel
waffle
fishball
dumpling
pasta
macaroni
farfalle
pasta_wheel
lasagne,lasagna
ravioli
rice_flour
rice_noodle
egg_(boiled),boiled_egg
egg_(fried),fried_egg
omelette,omelet
scrambled_eggs
egg_(poached),poached_egg
fruit_salad
shellfish_salad
pasta_salad
pudding,cream
Christmas_pudding
flavouring,seasoning_(liquid)
flavouring,seasoning_(powder)
bark
cinnamon
cinnamon_(powder)
vanilla
vanilla_(powder)
vanilla_(liquid)
vanilla_sauce
ginger
ginger_(powder)
ginger_sauce
herb_flavouring_(powder)
herb_flavouring
herb_sauce
salad_dressing
pepper_(powder)
pepper_sauce
curry
curry_(powder)
curry_sauce
mustard
mustard_(powder)
mustard_sauce
sap_(flavouring)
maple_syrup_flavouring
syrup
sap
syrup_(from_tree)
maple_syrup
corn_syrup
chocolate,cocoa,cacao_(sweet_powder)
chocolate,cocoa,cacao_(bitter_powder)
chocolate_sauce
chocolate_(hagel)
sweet_drink
sparkling_wine
champagne
cider
juicy
pickled
fried
delicious,scrumptious,yummy
tasteless
disgusting_(taste)
meat_(frozen),frozen_meat
fish_(frozen)
yogurt,yoghurt_(frozen)
hard_cheese
soft_cheese
spreadable_cheese
fresh_cheese
lump(s)
lumpy
cottage_cheese
lollipop,sucker
ice_cream_(lollipop)
water_ice_lollipop
popsicle
ice_cream,sherbet,sorbet
ice_cream_(bar)
bar,cake
candy_bar
chocolate_bar
reflect,consider-(to)
candy
candy,sweets
mixture
dough
batter
ingredient
slice
slice-(to)
sliced
reflection
reflector
shine
shine-(to)
shiny,glossy
polish-(to)
polisher
vacuum_cleaner
mixer,blender
food_processor,kitchen_machine
opener
bottle_opener
can_opener
cleaning_tool
cleaning_cloth
kitchen_tool,utensils
grater,grinder
whisk,beater
corkscrew
kitchen_tongs
nutcracker
reaching_aid,grabber
measuring_spoon
teaspoon
tablespoon
serving_spoon
mixing_spoon
ladle
funnel
oven_tray
baking_tin,baking_pan,ovenware
stovetop
cup
saucepan
electric_pan
frying_pan
woking
lid
pot,kettle,boiler
deep_fryer
steamer
electric_kettle
storage_jar,preserving_jar
glass_jar
tin,can
cookie_jar,biscuit_tin
rolling_pin
hot_tray
table_mat,placemat
pot_stand,trivet
potholder,oven_mitt
dish_gloves,rubber_gloves
equator
South_Pole
North_Pole
continent
Africa
Antarctic
Asia
Australia
Europe
North_America
South_America
Belgium
England
rose
Norway
fjord
Scotland
South_Africa
springbok
Sweden
crown
The_Nordic_countries
earthquake
continental_drift
waterfall
rapids
tidal_wave
inlet
tide
low_tide,ebb
high_tide
low_water
high_water
spring_(water)
hot_spring
constellation_of_stars
light_year
telescope
astrology
weather_forecast
Aries_(in_zodiac)
Taurus_(in_zodiac)
Cancer_(in_zodiac)
Leo_(in_zodiac)
Virgo_(in_zodiac)
Libra_(in_zodiac)
Scorpio_(in_zodiac)
Sagittarius_(in_zodiac)
Capricorn_(in_zodiac)
Aquarius_(in_zodiac)
Pisces_(in_zodiac)
Nordic_God
Woden
Frigg
Thor
Sif
Mjolnir
Gemini_(in_zodiac)
Balder
Frey
Freya
Tyr
Aegir
Loki_(OLD)
Hugin_and_Munin
Sleipnir
Saehrimnir
Midgard's_serpent
Valhalla
Viking
Viking_ship
runes
offer,sacrifice-(to)
sacrifice
blot
planet
lawn_bowling,bowls_(sport)
solar_system
pod
saddle
court,field
burial_site
astrologer,astrologist
beauty
call,telephone,ring-(to)
chocolate
chocolate_spread
cook,chef
cooking,cookery,preparation_(hot_food)
cooking,cookery,preparation_(general)
dirt,soil
doubt,uncertainty
fear,fright,concern
leadership,guidance
must_(a)
religious_(God_based)
self-harming
smartness,brightness,cleverness,intelligence
uncertain,unsure
accusation
accusation_(legal),charge,prosecution
accuse-(to)
accuse_(legal),charge,prosecute-(to)
act,demonstrate_(in_favour_of)-(to)
act_in_favour_of_(legal)-(to)
action,demonstration_(in_favour_of)
activity_centre
activity_centre_(children)
activity_centre_(leisure_time),after_school_club,youth_club
activity_centre_(teenagers)
advocate
advocate-(to)
advocate_(legal)
advocate_(legal)-(to)
advocate_(legal,speaking)
advocate_(speaking),spokesperson
altimeter
anemometer
angle_(measurement)
any_day,someday
apartment_block
archipelago
area_(meaurement)
arrest-(to)
attic
bakery
barometer,manometer
basement,cellar
biology_(class)
Bliss,Bliss_language,Blissymbolics
Bliss_(class)
board-(to)
bookshop
bronze
bronze_age
butcher_shop
care_centre
cheap,inexpensive
chemistry_(class)
clerk,legal_aid
clothing_shop
cockerel
cod
control_tower
copper
corridor,hall
cotton
cotton_fabric
count
court,courthouse
court,courtroom
crayfish
day_and_night
day_centre
care,protection,defence
defence_(legal)
defence_(spoken)
care,protect,defend-(to)
defend_(legal)-(to)
defend_(speak)-(to)
defend_(speak,legal)-(to)
caregiver,protector,defender
deflation
act,demonstrate_(against)-(to)
action,demonstration_(against)
department_store
discount
discount_sale
discount_store
distance_(OLD)
drugstore,pharmacy
eaves
economics_(class)
electricity_meter
elementary_school,primary_school
English_(class)
English_(language)
evidence
expensive
just,fair
fine_(penalty)
flatfish
flax
floor,storey,level,etage
floor_(42nd)
floor_(first)
florist
foundation_(building)
fuel_gauge
garden_centre
gauge
geography
geography_(class)
geology_(class)
gift_shop
goat
God_the_father
God_the_son
gold
greengrocer
grocery_store,food_store,supermarket
gutter,eaves_trough
half_an_hour
hall
handicraft_shop
handwriting,penmanship_(class)
health_goods_shop
Hebrew_(class)
Hebrew_(language)
herb,spice_plant
history_(class)
history_teacher
Holy_Spirit
Holy_Trinity
horizontal
horizontal-(a)
illegal,criminal
inflation
innocence
innocent,not_guilty
iron
iron_age
jellyfish
judge
judge-(to)
judgement,law_(in_combinations)
juridical
jury
justice
language_(class)
law
law-(a)
law,The_Law
lawyer
lawyer_(for_the_defence)
lead
legal
legal_aid
legal_person_(in_combinations)
leisure_time
light_meter
lighthouse
linen,flax_fabric
liquor_shop
lobster
market
math,mathematics_(class)_(1)
mercury
metal_bar
city,metropolis
midnight
multi_storey_building
multi_storey_home
naming_ceremony
naming_ceremony_(religious)
noon
notary
notary_(lawyer)
octopus
odometer_(OLD)
oil_gauge
one_storey_building,bungalow
one_storey_home
peer
pencil_case,pencil_box
physics_(class)
prawn
pressure
pressure_gauge
price_rise
promote-(to)
promotion
prosecutor
protest,objection,opposition
protest,resist-(to)
protest,resistance
protractor
psychologist
psychologist_(researcher)
psychology
psychology_teacher
quarter_of_an_hour
rain_gauge
reading_(class)
reading_lesson
religion_(class)
religion_(science_of),theology
religion_teacher
religious_service
row_house,attached_houses
sale
salmon
sandwich_(open_face)
scale_(weighing)
school_(in_combinations)
season
capture,catch,seize-(to)
semi-detached_house
sentence,condemn-(to)
service_(work)
shellfish_(without_claws)
sheltered_workshop
shoal,school_(of_fish)
shopping_centre,mall,plaza
shopping_mall
short_time_home
shrimp
silk
silk_fabric
silver
size
skyscraper
speed
speedometer
sport_lesson
sport_shop
starfish
statement
stone_age
store,shop
support_(oral)
support_(orally)-(to)
Swedish_(class)
Swedish_(language)
sweet_shop,candy_store
synthetic_fabric
tax
tax_(federal)
tax_(real_estate)
tax_(sales)
tax_(state,regional)
testify-(to)
testimony
theatre
timer
tin
tower
toy_shop
trial
two_storey_building
unfair,unjust
watch_tower,observation_tower
water_meter
water_tower
weight_(measurement)
vertical
vertical-(a)
witness
workplace
writing_(class)
aboard,on_board
address
anti-virus_program
ashore
ATM,cash_machine
attach_(computer)-(to)
attached_(computer)
attachment,appendix,annex
attachment_(computer)
backspace_(computer)-(to)
baker
ball_pool
ballet
bank_card,money_card
barrow
blackberry
brave,courageous
bricklayer
briefcase
Brontosaurus
brownie,house_elf
Buddha
Buddhism
buddhist
buddhist_(person)
budget,business_plan
butcher
car_mechanic
car_track
card
card_game
cartographer
cartography
cartoon,animated_picture
casserole
castle,palace
castle,palace_(royal)
causality
chilly
civil_engineer
clown
be_cold-(to)
comedy
community_centre,town_hall,village_hall
computer
computer_case
computer_game
computer_peripheral
computer_screen,monitor
concert
conjure,turn_to,transform-(to)
constructional_blocks,lego_(etc)
constructional_toy
copier,photocopier
coral
coral_reef
cordless_phone
courage
coward
cowardice
cowardly
currency
cut_and_paste_(computer)-(to)
dare-(to)
data_(digital_information)
delete_(computer)-(to)
designer,planner
desktop_computer
detach,take_apart-(to)
Dharma_wheel
meat_(diced),diced_meat,chunks_of_meat
digital
digital_processing,artificial_intelligence,AI
digits_(computer)
dinosaur
disembark-(to)
document,written_record
drama
dwarf,gnome
electrical_engineer
elf_(fog)
elf_(star)
e-mail,email
e-mail_address,email_address
embark,board-(to)
enter_(computer)
export
export-(to)
export_(computer)-(to)
exported
eye_mouse,eye_gaze
fairy,fairy_godmother
fall_asleep-(to)
fashion_designer
fax
fax-(to)
fax_(machine)
file,data_file_(digital)
filled,stuffed
filled_cabbage,stuffed_cabbage
filled_food,stuffed_food
filled_leaf,dolma
filled_vegetable,stuffed_vegetable
finger_spelling,finger_alphabet
fingerspell-(to)
fish_finger
fisherman
flower_fairy
folder
folder_(digital)
foster_home
freezer
fruit_cream,compote
function
function-(to)
functional
gardener
ghost,phantom
giant
giant_(human)
go_ashore-(to)
go_to_sea-(to)
goblin
headmouse
hedgehog
hero
heroic
herring,sardine
hobbit
hold_(with_hand)-(to)
homework,home_studying
hope
hopeful
house_work,housekeeping,housework
hunt-(to)
import
import-(to)
import_(computer)-(to)
imported
information
internet_(1)
internet_(2)
intranet_(1)
intranet_(2)
introduce,present-(to)
journalist
joystick
jump
Kazakhstan
ketchup
key_(computer)
key_guard
keyboard_(computer)
keyboard_(expanded)
keyboard_(mini)
kindergarten,preschool,nursery,play_group
king
landscape_design
landscape_designer
laptop
lay_the_table-(to)
lecture
lecture-(to)
leprechaun
lesson,lecture,class
librarian
light_switch
little_person
lotto,bingo_(etc)
lumberjack
lunch_box
magician
make_the_bed-(to)
make-believe_man
make-believe_person,imaginary_person
make-believe_person_(in_forest)
make-believe_person_(in_water),water_nymph
make-believe_person_(under_ground)
make-believe_woman
man_doll_(e.g._Ken)
making,production,fashioning
matching_game
math,mathematics_(class)_(2)
meat_sauce
mechanic,technician
mechanical_engineer
memory
mermaid
meat_(minced),minced_meat,ground_meat
mobile_phone,cellphone
mouse,pointing_device
musical
net
noisemaker,musical_toy
opera
optician
oval_shape
overlay
overlay_keyboard,membrane_keyboard
palmtop,PDA
pancake,crepe,tortilla
paper_money,bill
passenger
educationalist,educationist_(academic)
education,didactics,pedagogy
Pegasus
perform-(to)
performance,show
pharmacist
philosopher
philosopher_(academic)
philosophy
philosophy_(class)
pirate
play_(theater)
play_(in_combinations)
pointer
porcupine
porridge
prince
princess
print-(to)
Pterosaur,Pterodactyl
queen
quills,spines
railway_track
ramp
redo-(to)
redo_(computer)-(to)
refrigerator,fridge
remember,recall-(to)
research
rice_pudding,rice_porridge
rob-(to)
robber
robot_doll
roll-(to)
ruin,wreck,wreckage_(building)_(2)
Russia
samosa,pirogue
sand_play
sand_toy
Sandman
Santa_Claus,Father_Christmas
save_(computer)-(to)
save_as_(computer)-(to)
schoolbag
science
scientist,researcher
sea_anemone
sea_cucumber
sea_lion
sea_urchin
seal
seaweed
select_all,mark_all-(to)
shellfish
shepherd
shoot-(to)
siren_of_the_woods
software,computer_program,application,app
spell-(to)
sport_elf
steal-(to)
stew
subject_(of_study)
switch
swordfish
tablet_computer,tablet,tablet_PC_(2)
tabletop
tailor,dressmaker,seamstress
teacher,pedagogue,educator
teacher,pedagogue,educator_(in_combinations)
telephone_card
temporary_home
text_phone
theologian,theologist
theology,philosophy_of_religion
therapy_centre,rehabilitation_centre
thief
Tibet
tomato_sauce
tooth_fairy
touch_screen
touchpad,trackpad
toy_(in_combinations)
track
trackball
tragedy
traveller
Triceratops
troll
troll_(tailed)
tuna_fish
type-(to)
Tyrannosaurus_Rex
undo-(to)
undo_(computer)-(to)
unicorn
wake_up-(to)
walrus
wash_up,do_the_dishes-(to)
water_creature
water_play
water_toy
website
vegetable(s)
virus_(computer)
witch
wizard
woman_doll_(e.g._Barbie)
worksheet
writer,author
accident
accordion
alto
amplifier_(1)
amplifier_(2)
autoharp,zither,kantele
bagpipe
banjo
bass
bass_clarinet
bass_guitar
bassoon_(1)
bassoon_(2)
bells,chime_bars,tubular_bells
block,city_block
bongo_drum,hand_drum
bow,arc
bow_(musical_instrument)
bow_and_string_(musical)
bow_and_string_instrument
brake_(general)
brake_(vehicle)
brass_instrument
breeze
bugle_(1)
bugle_(2)
burned-out,burnt-out
calm,lull
calm_(weather)
castanets_(1)
castanets_(2)
CD_cover
celeriac,celery
cello
children's_song,nursery_rhyme
Chronic_Fatigue_Syndrome
clarinet,reed_instrument_(1)
clarinet,reed_instrument_(2)
condensation
condense-(to)
country_music
cymbal
dance_music
dark
detest,despise-(to)
disaster,catastrophe
district,neighbourhood_(countryside)
district,city_district,neighbourhood_(town)
double_bass,bass_fiddle,contrabass
double_bassoon_(1)
double_bassoon_(2)
dried
driving_license
drum_(1)
drum_(2)
drumstick
dry
dry-(to)
dryness,drought
eager,keen,willing
easy,easily
electric_piano
empty
empty,evacuate,throw_away,void-(to)
energy_(mental)
energy_(physical)
error,mishap
exciting,excitingly,excited,excitedly
excitement
exhausted,worn_out
flute,recorder
flute,transverse_flute
flute_(alto)
flute_(soprano)
foam,mousse
French_horn_(1)
French_horn_(2)
gong
guitar,string_instrument
hair_spray
harp
harpsichord
hate-(to)
hum-(to)
humid,damp,moist
humidity
hurricane
kazoo
kebab_(Middle_East)
kebab_(Scandinavia)
kebab_(UK,NL)
keyboard
last_(person,etc)
lie
lie-(to)
line,queue
lose_(fail_to_win)-(to)
loudspeaker
mandolin
maracas,calabash_(etc)
melodica,blow-organ
microphone
MP3_player,iPod_(etc)
musical_instrument_(in_combinations)
musical_instrument_(with_many_strings)
never
nothing,none
oboe_(1)
oboe_(2)
old
organ,pipe_organ
panpipe
park-(to)
parking_permit
parking_ticket
participant
participate-(to)
participation
participation,involvement
pennywhistle,tin_whistle
percussion_instrument
piano_(1)
piano_(2)
piccolo_(1)
piccolo_(2)
pipe,hose,tube_(2)
pipe,tube_(closed)
key,tonality
pitch_(sound)
play_(instrument)-(to)
pop_music
punk_rock
rainbow
rap_(music)
rattle
rattle_(musical_instrument)
recorder
recorder_(alto)
recorder_(bass)
recorder_(soprano)
recorder_(tenor)
reed
rhythm_instrument
roe_deer
rotisserie,spit
saxophone_(1)
saxophone_(2)
sit_ski_(OLD)
small_pancake,blini
snowmobile
snowplow,snowplough
soprano
spray,vaporize-(to)
spray_bottle,vaporizer,spray_can
stave,staff
storm
stressed
string
string_(for_musical_instrument)
surprise
surprise-(to)
surprised
synthesizer,synthesiser,keyboard
tambourine_(1)
tambourine_(2)
tenor
tornado
triangle_(instrument)_(1)
triangle_(instrument)_(2)
trombone
trumpet,horn,cornet_(2)
tsunami
tuba_(1)
tuba_(2)
tuning_fork
twin_brother
twin_sister
twins
ukulele
unfold-(to)
wind_instrument
viola
violin
voice
woodwind_instrument
xylophone,vibraphone_(1)
xylophone,vibraphone_(2)
acrobat
acrobatics
adding,additive
Advent
agnosticism
agreement_(spoken)
agreement_(written),contract
aid_store_room
animal_droppings
ankle_splint
other,another_(thing)
apricot_(dried)
Ascension_(of_Christ)
Ascension_Day
asparagus
assessment_room
at_one's_destination,there
auditor,accountant
avalanche
bark-(to)
bean_(dried),chick-pea,kidney_bean,pinto_bean
bicycle_path
bisexual
bisexuality
bit_(horse)
bleat,baa-(to)
Bliss_fanatic
blood_vessel
blush-(to)
body_brace,corset
body_fluid
body_hair
body_part
body_temperature
bolt_(horse)-(to)
bomb,explosive
bow
bridle,headstall
bus_lane
bus_station
bus_stop,bus_bay
cable_car
cancer
canter-(to)
celibacy_(religious)
ceramics,pottery
certain,sure
chairlift
chairman
challenge
charm
charming
checked
chest_hair
child_care
child_harness,walking_reins
Children's_Day
chirp,twitter-(to)
circus
clean
cloakroom,walk-in_closet
cloudberry
cold,common_cold
common,mutual,shared
commuter_train
conductive_education
conductor_(teacher,therapist)
constipation_(1)
constipation_(2)
constitution
croak_(frog)-(to)
crown_prince
crown_princess
cuddle-(to)
cure-(to)
dancing_therapy
decoration,ornament
democracy
depending_on
devoted
devotee,fan
devotion
diarrhea,diarrhoea
domestic
dotted
drying_cupboard,airing_cupboard
drying_room,drying_chamber
dump,dispose-(to)
elbow_splint
voter,elector
electorate
endangered
Epiphany
escalator,moving_stairs
Estonia
existence,being_(1)
experiment-(to)
exploded
explosive
facial_hair
Family_Day
fan_(machine)
fanatic
fanatic_(person)
farrier
Father's_Day
fee
fertilized
few,little
fever,temperature
financial_support
fingernail,nail
fish_(dried)
flower_(dried)
flu,influenza
foreign
fort,fortress
foundation,base,fundament
fruit_(dried)
fundamental,basic
fundamental_law
fundamental_rule
fundamentalism
fundamentalism_(religious)
fundamentalist
fundamentalist_(religious)
gallop-(to)
gelding
general
girth,cinch
glacier
glass_craft
glow
glow-(to)
groom_(horse)
groom_(horse)-(to)
growl_(dog)-(to)
grunt_(pig)-(to)
hair_drier,blow_dryer
hand_splint
harness
harness-(to)
harness_(horse)
harness_(horse)-(to)
hay
heal-(to)
Heaven,Kingdom_of_God
hibernation
hiss_(cat)-(to)
hitch,tie_up,fix_up-(to)
homosexual
homosexuality
hoof
hoof_pick
horse_box,stall
horse_brush,body_brush
horse_cloth
horse_droppings
horse_trailer,horsebox
horsehair
horseshoe
horseshoe_nail
Hungary
hurry,rush
hurry,rush-(to)
hurry_(in_a),hurried,rushed
hydrotherapy
ice_field
iceberg
independent
invisible
jaguar
kidney
knot
Lent
liberation
linear_thing_(horizontal),bar
long_time
lower_body
make_sign_of_the_cross-(to)
mane_(horse)
manure,fertilizer
mare
meat_(dried),dried_meat
medical_treatment,medical_care
menstrual_blood
metal_craft
mew,meow-(to)
minister_(government)
monarchy
moo,bellow-(to)
Mother's_Day
muzzle
nature_craft
navel
neigh,whinny-(to)
occupational_therapy
occupational_therapy_room
organ_(body)_(OLD)
paddock
paper_craft
parachute_harness
parking_lot
passport
pasture,enclosed_field
pavement,sidewalk
personality
physiotherapy
physiotherapy_room
placenta_(OLD)
platform,stage
politician
politics
pram_straps,safety_harness
preceding,previous,former,earlier
prescription
president
prime_minister
program,programme
protected,saved
protection_of_the_environment
prune
psychology_room
public_transport
purr_(cat)-(to)
rack,single-foot-(to)
raisins,currants
rash_(skin)
reclaim_(marshes_etc)-(to)
religious_fanatic
religious_fanatic_(God_based)
repair_room
repair_shop
republic
respirator
responsibility
responsible
Resurrection_of_Christ
riding_boots
riding_clothes
riding_instructor
riding_school,manege
road_(2)
roar_(lion)-(to)
rotation,circulation,orbit,lap,circle,round
royal
royal_family
saddle_pad,saddle_blanket
salvation_(religious)
scabies
seat_belt
service_(help)
sexual_activity
sexual_aid
sexual_play
sexually_mature
shall,will-(modal_aux_v)
shampoo-(to)
shave-(to)
should,would-(modal_aux_v)
sign_of_the_cross
skin_disease,eczema
skytrain,monorail
slow,slowly
social
society
somersault_(1)
somersault_(2)
spark
spasm
speech_therapy
speech_therapy_room
spiritual_awareness
splint_(orthopedic)
sport_fanatic
square_(public)
stallion,entire
starvation
station
still,continuing,ongoing
still,continuously
stirrup
stomach_flu
stomach_illness
stop,platform_(vehicle)
stretch_(elongate)-(to)
stretch_(muscles)-(to)
striped
study-(to)
stupid,dumb
subway,metro,underground,tube
sunflower
swash
switch_off,turn_off-(to)
switch_on,turn_on-(to)
tack_room
tadpole
tail_(horse)
tail_lift,lift
teamwork
teetotalism
temporary
textile_craft
that_(conj)
therapeutic_riding
tie,bind_together,lash-(to)
towel
train_station_(building)
train_station_(platforms)
tram
treat,care_for_(medically)-(to)
trolleybus
trot_(horse)-(to)
tumble-drier,tumble-dryer
tunnel,subway,underpass
underground_station,subway_station
unharness_(horse)-(to)
union_(political_unit)
upper_body
vaginal_discharge
walk_(horse)-(to)
walkway,footpath
wart,papilloma_(venereal)
water-(to)
water_bucket
vehicle_(long)
venereal_disease
venereal_papilloma
wheelchair_straps
wild_strawberry
visa
volte_(horse)-(to)
woodcraft
wrist_splint
achieve-(to)
achievement
addict
addiction
alcoholism,alcohol_addiction
alcohol_abuse,alcohol_addiction
allergy,hypersensitivity
baby_animal
baby_bottle,feeding_bottle
bacterial_infection
bacterium
bend-(to)
bet
bet-(to)
betting
binoculars,field_glass_(OLD)
blacksmith
bottle_nipple,teat
bruise,contusion,haematoma
bruise,dent
bruised,dented
bump,press,pressing
bump,press-(to)
cease-fire,armistice
Ceres_(dwarf_planet)
chance,risk
chive
control_(OLD)
dependency
disability_benefit_(OLD)
dish_rack
domino
dribble-(to)
drug_addict
drug_addiction
drug_dependency
dwarf_planet
Earth,Tellus_(planet)
eating_disorder
Eris_(dwarf_planet)
examination,investigation
examine_(medically)-(to)
existence,being_(2)
fail-(to)
failure
fan_club
fledgeling
foal
football_supporters_club
football_team
galaxy
gamble
gamble-(to)
gambler
gas_planet
goldsmith
Good_day_(bye)
Good_day_(hello)
Good_evening_(bye)
Good_evening_(hello)
Good_morning_(bye)
Good_morning_(hello)
Good_night_(bye)
Good_night_(hello)
guest_room
have_impact_on-(to)
impact
infect-(to)
infected
infection
infectious,contagious
itch
Jupiter_(planet)
kitten
lamb
leek
lottery,game_of_chance
magnifier,magnifying_glass
Mars_(planet)
medical_examination
meeting_room,auditorium
mental_illness
Mercury_(planet)
message
message,content_(communication)
micro-organism
microscope
drug,mind-altering_drug
money_on_a_regular_basis
negative_dependency
Neptune_(planet)
old-age_pension
organism
outcome,result
pacifier,dummy
pensioner
Pluto_(dwarf_planet)
program,programme,presentation
react-(to)
reaction
reception
retirement_pension
rock_planet,terrestrial_planet
Saturn_(planet)
scratch
scratch-(to)
senior_citizen
short_message_system_(SMS),text_message
silversmith
sink,basin
smoking_addiction_(2)
smoking_addiction_(1)
substance
tap_(1)
tap_(2)
tile
treatment
Universe
Uranus_(planet)
Venus_(planet)
viral_infection
virus
young_animal
adventure_(OLD)
aerial,antenna
agenda
anchor
Earth_axis
band_(of_frequencies)_(OLD)
Bangladesh
barley
berth,bunk
board,board_of_directors,executive
boat_ladder
boot,trunk,roof_box,luggage_compartment
broadband_(OLD)
broadcast,transmit-(to)
buzzer
cabin_(boat)
camper_van,RV
canal_(water)
care_manager,care_plan_manager
CD
channel_(programs)
Christmas_song,carol
communication_satellite
compartment
compass
connection_(computer)
connector,interface_box
corruption_(OLD)
crack,gap,cleft
crater
credit
credit_card
crew,staff
crew_(boat)
crew_(plane)
dependent
digital_device
digital_signal
digital_memory,digital_storage
digital_storage_device
dizzy
document_(electronic),digital_document
drop_anchor-(to)
DVD
DVD,movie_disc
DVD_player
empower-(to)_(OLD)
empowered_(OLD)
empowerment_(OLD)
erupt-(to)
eruption
exchanger
external_hard_drive
firework
fish_cage
French_fries,chips
galley_(boat)
game_box
GPS,satnav
GPS_(system)
hammock
hard_rock
I_need_more_time,give_me_time
indicator_(adverb)
indicator_(continuous_form)
indicator_(definite_form)
indicator_(female)
indicator_(first_person)
indicator_(imperative_form)
indicator_(indefinite_form)
indicator_(neutral_form)
indicator_(object_form)
indicator_(past_participle_1)
indicator_(past_participle_2)
indicator_(possessive_form)
indicator_(present_participle)
indicator_(second_person)
indicator_(third_person)
inflammable,flammable
invoice
jackfruit
janitor,caretaker
lava,magma
lee,shelter
let_fall,drop-(to)
life-jacket
lower-(to)
lullaby
lunar_eclipse
media_player
member
memo,reminder_note
memory_stick,USB-memory
metal_(music)
minutes
misuse
misuse-(to)
MMS
monument,commemorative_work
move_(change_position)-(to)
movement,motion_(1)
movement,motion_(2)
navigational_sign
oats
okra,lady's_finger
overspend,buy_over_budget-(to)
pay_channel
pick-(to)
plug_in,connect_(digital)-(to)
plug_in,connect_(power)-(to)
port_(boat)
port_(device)
portability
portable
potato_chip(s),chip(s),crisp(s)
potty,chamber_pot,bedpan
power,powerfulness_(OLD)
powerful,mighty_(OLD)
quality
quality_(measurement)
quantity_(measurement)
raise-(to)
receipt
receiver
receiver,dish
receiving
reef-(to)
rein
remote_control
rent
rent,lease,let-(to)
rent,lease,hire,charter-(to)
respiratory_illness
road_sign
rock_music
rough_sea
rye
satellite
satellite_dish_(1)
satellite_dish_(2)
satellite_signal
school_uniform
sea_captain,skipper
sea_chart
shadow,shade
shipping_forecast
shower_chair
sign,signal
signal,broadcast,transmitting
signal_receiver_(1)
signal_receiver_(2)
signal_reception
singalong
solar_eclipse
speech
spending_spree
splurge-(to)
stand-in,substitute,alternate
starboard
step,stair
stranger,unknown_(person)
submerged_rock
sun_lounger,deck_chair
sunbathe-(to)
sunburn
sunglasses
suntan
Take_your_time!
toilet_chair,commode_chair
tourist
tourist_(foreign)
TV_programme,TV_show,radio_programme
TV_studio,radio_studio
urine_bottle
USA
waiter,waitress
water_flower,water_lily
weather_satellite,spy_satellite
wheat
video_phone
wireless_connection,WiFi
bear's_head
bell,chime_bar
man-made_item,artefact,artifact,product
eagerness,keenness,willingness
jump_(backward)
scale,measurement
indicator_(present_action)
agreed,in_agreement,harmonious
bathtub,bath,tub
bugle_(hunting)
conductor_(music)
government
homosexual_(female),lesbian
homosexual_(male),gay
in_love
massage-(to)
niece_or_nephew
psychology_(class)
quickness,rapidity,speediness
terrorism
troublesome
upset,disturbance,agitation
cry_out,call-(to)
laugh,laughter
push,pushing
jewelry,jewellery
boring,dull,depressing
laundry_(workplace)
great,wonderful,fantastic
geyser
terror,panic
wait,waiting
wish,desire
want,desire
last_month
anthropologist
children's_room
cost-(to)
expose_oneself_indecently-(to)
finished,complete,completed
light_(not_dark)
observation
usage,use
hug,squeeze,embrace
boss,supervisor
brake_(general)-(to)
brake_(vehicle)-(to)
break,fracture
dance,dancing
drowning
fight,combat
improvement
pier
visit
advocacy
advocacy,representation_(legal)
band,orchestra
be_named,be_called-(to)
bigness,largeness
board_and_lodging,room_and_board
build,construct-(to)
clearness,clarity,transparency,transparence
comparative_more
consideration,thoughtfulness
continuance,continuation
crown_(currency)
deletion,cancellation,destruction
difficulty
disgust
disgusting_(general)
dispersion,dissemination,scattering,spread,spreading
divided
earmuffs_(general)
ease,easiness,simplicity
emptying,voidance,evacuation
eternity,infinity_(OLD)
experiment
fall,drop,spill,tumble
fantasy,phantasy,imagination,illusion
farness,remoteness,farawayness_(OLD)
filling,fill,fullness
fixing,fix,mending,mend,repair,reparation
forgetting,amnesia
fountain
gallop
geographer
giving,gift
grid,matrix
growth,growing
half,one-half
hate,hatred
height,tallness
heterosexual
hitchrack,hitching_bar
holding
importance,significance
indoor,indoors
infiniteness,boundlessness,limitlessness_(OLD)
interest
littleness,smallness
lowness,shortness_(height)
malodor,malodour,stench
medicine,medical_practice
next_month
noise_(loud)
oere_(currency)
oval,elliptic,elliptical
ownership,possession
permission,allowance
persuasion
physicist
preparation,readying,readiness,preparedness
promise
protected,sheltered
quarter,one_quarter
reading
repetition,copying,duplication,replication
research-(to)
riding,horseback_riding
selfishness,egoism
shortness_(distance,length)
sport_(class)
spray,vaporization
strength
stress
stress-(to)
superlative_most
supernatural
sweetness,sweet
swimming,swim
this_month
wakefulness,alertness
vomiting,vomit,puking
slang
coarse_slang
aport
astarboard
hunt,hunting
church_ruin,temple_ruin,wreck,wreckage_(church,temple,mosque)_(2)
army,regular_army,ground_forces
destroyed,ruined,demolished,deleted,erased,cancelled
access-(to)
accessibility
accessible
adopt-(to)
adoption
adventure
adventurous
Afghanistan
ajar
alcohol,ethanol
alphabet,letters_(uppercase)
applaud,clap-(to)
applause,clapping
armed
Austria
bandit,armed_robber
bazaar
beggar
Belarus
bioenergy
braid,plait-(to)
braid,plait,pigtail(s)
Brazil
cheer-(to)
cheering_(the_sound)
cheerleader
cheers_(toast)
China
city_tour
climate
code,password
collection,pile,tussock_(etc)
coup,hijack,takeover
coup,coup_d'etat
crime
criminal_(person)
criminality,crime
curiosity,curiousness,inquisitiveness
curious,inquisitive
cushion
cushion_(seat)
Czech_Republic
deflate,let_out_air-(to)
detective,investigator
diaphragm,midriff
disinfectant,antiseptic
drill
drilling_rig_(gas)
drilling_rig_(oil)
drilling_rig_(water)
each_other,one_another
encourage-(to)
encouragement
escape
escape-(to)
espionage,spying
explore-(to)
explorer,enquirer
fart,wind
fatal,lethal
fossil_fuel,coal_(etc)
France
Friday_(day5)
Friday_(day6)
Friday_(day7)
gas_(fuel)
gas_(fuel_from_biomass)
geothermal_energy
gravity,gravitation
Greece
habit,custom
Hattifatteners
Hemulen
hiccup(s)_(1)
hiccup(s)_(2)
hide,conceal_(secret)-(to)
hide_and_seek
hiding_place,cache
hijack,make_a_coup-(to)
hijacker,coup_maker
hold,contain_(2)-(to)
hostage_(1)
hostage_(2)
hunter
hydropower,hydro_energy
identity_card
index,list_of_contents_(in_a_book_etc)
India
inflate-(to)
invitation_(general_spoken)
invitation_(general_written)
invitation_(spoken)
invitation_(written)
Iraq
Italy
Japan
kidnap-(to)
kidnapper
killer,murderer
killing,murder,slaughter
knock,tap-(to)
knock,tap_(sound)
knocking
land_(rocket)-(to)
landing_(rocket)
Little_My
load
make_a_speech-(to)
Monday_(day1)
Monday_(day2)
Monday_(day3)
Moominmamma
Moominpappa
Moomintroll
move,movement
mummy_(general)
mummy_(imaginary)
murder
murder-(to)
murderer
nosy
nuclear_fuel
oil_(fuel)
oil_power,oil_energy
OK,alright
Olympics,Olympic_games
oppressed,unfree
oppression,captivity,slavery
out_of_(backward)
out_of_(upward)
passive
passivity
pill_box
Poland
Portugal
power_plant,power_station
precious,treasured
precious_thing,treasure
prison_officer
prisoner
pump
pump-(to)
rag
rags_(worn-out_clothes)
resign,quit_(1)-(to)
resign,quit_(2)-(to)
resignation_(1)
resignation_(2)
retire-(to)
retired
retirement
roast,joint_(of_meat)
robot
sack,dismiss-(to)
sacked,dismissed
sacking,dismissal
safari,wildlife_expedition
Saturday_(day1)
Saturday_(day6)
Saturday_(day7)
scoundrel,villain
protector,guard
Sniff
Snork
Snork_Maiden
Snufkin
solar_energy,solar_power
space_travel,space_voyage,space_flight
speech_(event)
secret_agent,spy
steak
still,calm,peaceful,tranquil
stolen_goods
summary,abstract
Sunday_(day1)
Sunday_(day2)
Sunday_(day7)
supporters,cheering_section
Switzerland
take_off_(rocket)-(to)
takeoff_(rocket)
technology
The_Groke
theft
thrilling,scary
Thursday_(day4)
Thursday_(day5)
Thursday_(day6)
Toffle
tour,sightseeing
trap
trap-(to)
hidden_treasure,treasure_trove
tropical_rain_forest,jungle
Tuesday_(day2)
Tuesday_(day3)
Tuesday_(day4)
Turkey
Ukraine
usually_do,habitually_do-(to)
vampire
warn-(to)
warning
wave_power,wave_energy
weapon
Wednesday_(day3)
Wednesday_(day4)
Wednesday_(day5)
weekend
werewolf
wind_power,wind_energy,wind_farm
worn-out,raddled
zombie
touch,touching
airforce,air_force
airport_terminal
air_traffic_controller
alarm
alternate-(to)
alternating
alternating_current,AC
alternation
ammeter
amplitude
Arabic_(language)
attack
attack-(to)
Batman
bedbug,wall_louse
beige
biathlon
bird_of_prey,raptor
bless-(to)
have_a_view,have_an_opinion-(to)
cabin_(airplane)
camping_mat,sleeping_mat
camping_stove
carve-(to)
chase
chase-(to)
cipher
closed
clue
cousin_(male)
cousin_(female)
direct_current,DC
cylinder_for_breathing
Danish_(language)_(OLD)
digital_memory,RAM
Egypt
electric_circuit
electric_conductor
electric_current
electric_field
electric_insulator,electrical_insulator
electro_magnet
engagement
Estonian_(language)
fiance,groom-to-be
fiancee,bride-to-be
fingerprint
Finnish_(class)
Finnish_(language)
fire_extinguisher
fire_place,campfire_site
firecraft
first_aid
fish_bone
flight_instrument(s)
flight_deck,cockpit
footprint
French_(language)
frequency_(wave_motion)
front,front_of_a_thing
full,satisfied
fuse
fuselage
gas_cylinder
gathering_of_scouts,jamboree
hangar
head_louse
headset
hike-(to)
hiking
Icelandic_(language)
illustrate-(to)
illustrated,illustrating
illustration
impermeable_material,insulation_(material)
imprint,trace,track
inhaler
insomnia
Iran
Irish_(language)
Italian_(language)
ladybird
landing_gear
lifeline
light_(weight)
liquid
magnet
magnetic_field
magnetism
make_and_tend_a_fire-(to)
medication_for_breathing
memory_game,Kim's_game
national
national_day
navigate_airplane-(to)
Norwegian_(language)
organization,organizing
orienteer_(sport)-(to)
orienteer,read_map-(to)
orienteering_(sport)
map_reading
PEP_mask
perch_(fish)
period_(wave_motion)
permeable_material
Persian_(language)
personal_measurement
plant-louse
propeller,rotor_(blades)
radio_(2)
rear,back_of_a_thing
rowdy
runway_(airport)
Russian_(language)
equal,same
science_centre
scout_(etc)
scouting_(etc)
signal_strength_meter
sleepy
sniffer_dog
social_network,facebook_(etc)
Spain
Spanish,Castilian_(language)
Spiderman
state_of_mind
suicide
Superman
tail_(airplane)
tail_wing_(airplane)
take_off_(airplane)-(to)
Tarzan
tie_whipping_knot-(to)
top,top_of_a_thing
tracker
turquoise
uniform
wave_length
veterinarian
whipping_knot
wind_turbine
windmill
voltage
voltmeter
wrap,wind-(to)
wreck,wreckage_(airplane)
wreck,wreckage_(boat)
ascending_and_descending
land_(airplane)-(to)
different,other
swing,swinging
magnetic_pole
bottom,bottom_of_a_thing
breathing_aid
sitting_mat
frequency
sleepless
quarrel,row
Germany
German_(language)
Thailand
Romania
artillery
German_(class)
Romanian_(class)
Romanian_(language)
armoured_force,tank_force
Thai_(class)
Thai_(language)
appendix,cecum,caecum
beginning_of_year
body_painting
bracelet
brain_signal
breastbone,sternum
brooch
cannula_(with_needle)
cardiovascular_system
catheter_(urine)
cellular_fluid
Christmas_Eve_(day)
Christmas_Eve_(evening)
circulatory_system
collarbone,clavicle
day_before_holiday
drug_(leaf_based)
earring
end_of_year
endocrine_system
feeding_tube
gastrointestinal_system
gland
glitter
have_a_tea_break,have_a_coffee_break-(to)
heel_(shoe)
high_heeled_shoes,high_heels
humerus,upper_arm_bone
indicator_(diminutive_form)
insulin
intestine(s),bowel(s),gut(s)
large_intestine
liver
lower_arm
lower_arm_bone(s)
lung(s)
lymph
lymph_node,lymph_gland
lymphatic_system
medical_tube,catheter,cannula
necklace
nerve
nervous_system
neuron
New_Year_(general)
New_Year's_eve_(day)
New_Year's_eve_(evening)
New_Year's_eve,end_of_year_(day)
New_Year's_eve,end_of_year_(evening)
oesophagus,gullet
organ,inner_organ,inner_body_part
pancreas
pierce_(jewellery)-(to)
pierce-(to)
piercing_(thing)
rectum
respiratory_system
rib(s)
ring_(finger)
salivary_gland
sequin(s),spangle(s)
shoulder_blade,scapula
skull,cranium
small_intestine
snuff_(nose)
snuff,kat,coca
spleen
stoma,medical_hole
stomach,tummy,tum
tattoo_(permanent)
tattoo_(sticker)
tattoo,picture_on_skin
tea_break,coffee_break
tendon
tissue_(body)
trachea,wind_pipe
tracheotomy_tube,tracheal_tube
upper_arm
vascular_system
work_day
ability_(half_sized)
animal_(bushy_tailed)
away,at_a_distance,off
bad_conscience
ball_field
biochemical_product,organic_compound
blindness
boarding,embarkation_(to_sea)
bones_with_joint
bottleneck,bottle_opening
bread_surface
buttocks_and_genitals
case,casing
coldness,cold
compression,compressing,squeezing
container,basket_(high)
container_(low)
corner
correct_thinking
incorrect_thinking
couple_(female)
couple_(male)
crossed_racquets
deafness
debarkation,disembarkation_(ashore)
adversity,hardship,setback
depth
miscarriage,abortion_(general)
detachment,separation,breakup
diamond_(character)
digging,excavation
digital_space_(limited)
digital_world
disturbance,unrest
evaluation,value_(half-sized)
exchange,substitution
extinction,extinguishing_(fire)
eyelid(s)
eyelid_(lower)
farness,remoteness,farawayness
fatness,thickness
fatness,thickness_(OLD)
floating_container
flower,bloom,blossom
fold,folding,pleating
freezing,hardening,solidifying
from_sky
fruit_(pointed)
future_(uncertain)
good_conscience
hidden_thing
horse_neck
horse_rump
hypodermic_needlepoint
hypothesis,theory
imprint,depression
insurance
left_turn,left_(position_or_direction)
leg_and_foot
limit(s),limitation,restriction
mane_(lion_etc)
mash,mush,pulp_(food)
mask_(disguise)
meeting,encounter
meeting_and_parting
metaphor_(winged)
nearness,closeness,proximity
newness,novelty
no_speech,anarthria
opposing_forces,counter-forces
out_of_body_(upward)
outdoor_(character)
parting
permission,allowance_(moral)
pizza_slice(s),sector(s),circle_sector(s)
plus_minus
plus_sign_(low)
protected_water
protection_with_pointer
pull,pulling
raised_wavy_line
recording_disk
reflection_(mental),consideration
ride,drive
right_turn,right_(position_or_direction)
ruin,wreck,wreckage_(building)_(1)
shallowness
shekel_(character)
shuttlecock,birdie_(badminton)
sitski,sit_ski
ski,runner_(sled_etc)
smoking_(cigarette)
smoking_(pipe)
snowshoe
projectile,rocket,spacecraft
sperm_destruction
spiral
spitting
sport_stick_and_ball,bandy_stick
sport_stick_and_puck,hockey_stick
square_(oblique)
thawing,melting
thinness,narrowness
three_Danish_waters_(OLD)
trailer,container_transport
transport,transportation
tree_or_wood_destruction
turn,turning
under_(ground_level)
understanding,comprehension
unfolding
Union_Jack_pattern
water_animal_(big_tail)
water_on_ground_(flooding)
wideness,broadness
wok,wok_pan
woman_(below_waist)
actor
Alice_(in_Wonderland)
altruism,selflessness
among,amongst
artist
baguette
baking_powder
ballot,voting_slip
barn
bird_nest,birdnest
birdhouse,house_for_bird
blog,web_blog
boar
boyfriend
bread_(sliced),sliced_bread
bread_crust
bread_knife
bread_with_fruit
bread_with_seeds
brother-in-law_(husband's_brother)
brother-in-law_(partner's_brother)
brother-in-law_(wife's_brother)
bun_(soft),roll_(soft),scone,brioche
business_idea
cactus
chat_(online)
chat_(online)-(to)
cheat-(to)
cheating
chick
classmate
claw_(shellfish)
client,customer
colleague
combine_(harvester)
compass_(drawing)
cone,conifer_cone,strobilus
core_activity
cowshed
daughter-in-law
definition
dice,die
dichotomy,duality
dictator
dictatorship
dilemma
doll_pram,doll_carriage
dollhouse,doll_house
domestic_science,home_economics
domestic_science,home_economics_(class)
dormouse_(sleepy_rodent)
drop
employed,working
employee
equilateral_triangle
ewe
even_number
excavator,digger,power_shovel
experience
explanation,reason
family,couple_(female)
family,couple_(male)
family_(female)
family_(male)
farmhouse
father-in-law_(partner's_father)
female_friend
flower_meadow
get_engaged-(to)
girlfriend
grandchild
graze-(to)
handcraft,craft-(to)
handmade_figure,handicraft_(animal)
handmade_figure,handicraft_(person)
hare
height,altitude
hen
henhouse,chicken_coop
home_worker
housekeep,housework-(to)
housekeeper
ice_layer
ice_skating_rink_(indoor)
icing
influence
influence,affect-(to)
influenced,affected
inspiration
inspire-(to)
inspired
interrupt_(in_conversation)-(to)
interruption_(in_conversation)
intuition
isosceles_triangle
jobcentre,job-centre
knight
lawn_mower,mower
layer,level
long_for,yearn-(to)
longing,yearning
make_cheese-(to)
male_friend
married_(to_be)
measuring_cup
mislead-(to)
molasses,dark_syrup,black_treacle
mother-in-law_(partner's_mother)
motivate-(to)
motivated
motivation
odd_number
partner_(game,dancing,business)
pasture
pasture,put_out_to_pasture-(to)
patient,enduring
patient_(in_medical_care)
pig_(wild),boar_(wild)
piggery
piglet
playhouse,play_house
powdered_sugar,icing_sugar
principal,headteacher
prize,award,trophy
publication
publish-(to)
publisher
puddle,pool
ram
reality
rescue
rescue-(to)
right_triangle
root
ruin_(castle),castle_ruin
salesperson,shop_owner
scalene_triangle
sceptical,skeptical,questioning
scepticism,skepticism
schoolmate
sculpture
self-raising_flour
set_square
sheath
sheep_shed,sheep_barn
sister-in-law_(husband's_sister)
sister-in-law_(partner's_sister)
sister-in-law_(wife's_sister)
slaughter
slaughter-(to)
slaughterer
slaughterhouse,abattoir
slice_of_bread,bread_slice
slide,skid,slip-(to)
smartphone,digital_phone
son-in-law
sow
speaker,lecturer
speech_recognition
spider_web,cobweb,orb_web
sports_centre
stepdaughter
stepparent,step-parent
stepson
strategy
sugar_lump,cube_(sugar)
surrounded,encircled,surrounding
swim_centre
swimming_hall,indoor_swimming_pool
synthetic_speech,text-to-speech,tts
tablet_computer,tablet,tablet_PC_(1)
taco,taco_shell
tooth
unemployed
well,water_well
voluntary
voluntary_work,unpaid_work
volunteering
work_from_home-(to)
working_from_home
yeast
possible
question,be_sceptical,doubt-(to)
age
asteroid
balance,sense_of_balance
balance_(general),poise
balance_(general),poise-(to)
balance_(walking,standing)-(to)
barrow,grave_mound
bathing_rule(s)
bike_lamp
birch
birdfeeder,bird_table
cardboard,paperboard
chess
chewing-gum
collar
cornea
covered,hidden
dairy
darkness
den,lair
dense,thick,compact,tight,jammed
density,denseness,compactness,tightness_(general)
density,denseness,concentration_(measurement)
disagree,discord,disaccord-(to)
disagreement,discord
discordant
diver_(activ_under_water)
diver_(jump)
diving,activity_under_water
diving_equipment,diving_gear
doorway,gate
dove
dust_storm,duster,sirocco
ear,spike,capitulum
eastward
equipment,gear
fable,allegory,parable
fairy_tale
fiber,fibre,fibril,filament,strand
folk_tale,legend
football_rule(s)
four-leaf_clover
free_of_charge,gratis,for_free
game_rule(s)
give_birth-(to)
globe_(map)
grave_field
habitation,dwelling_place,site
head_lamp
heap_of_sand
hearing,audition,auditory_sense
homeward
ice_coated,ice_covered
ice_covering,ice_crust,ice_coating
into_(backward)
into_(downward)
into_(upward)
iris_(eye)
labyrinth,maze
lamb-(to)
Lapps,Lapplander(s),Sami(s)
Latvia
Latvian_(class)
Latvian_(language)
leaf,flap
lick-(to)
lock
lower_leg,shank,shin
magic
magical
manhole_cover
midnight_sun
milkmaid,dairymaid
millepede
mother's_milk
mountain_pasture
mouth_(wide-open),open_mouth,gape
myth
northward
open_one's_mouth,hold_one's_mouth_open,gape-(to)
others_(persons)
overturn,turn_over,tip_over-(to)
paper_clip
people_in_the_north_(Lapps,Eskimos)
place_to_feed,feeding_place,feeding_ground
plant_(edible)
polar_bear
polar_night
pupil_(eye)
raindrop
raise_one's_hand,put_up_one's_hand-(to)
reed,bamboo_(tall_grass)
rock_(geology)
rope,hawser
sandstorm
school_way
season_of_darkness
sense
show_of_hands
sight,vision,visual_sense
smell,sense_of_smell,olfaction
snake_(dangerous),viper,boa_(etc)
snake_(not_dangerous),grass_snake_(etc)
sole_(of_shoe)
southward
spill,slop-(to)
sprout,germinate-(to)
story_(historical),historic_story
summer_day
summer_house,summerhouse
swimming_rule(s)
tanker_truck,tank_lorry
taste,gustation,sense_of_taste
tear,teardrop
tear_along,advance_fast,go_fast-(to)
thigh,upper_leg
thread,string,cord
touch,sense_of_touch,tactile_sense
traffic_rule(s)
trapeze
T-shirt,tee_shirt,jersey
tuft_of_grass,tussock
watchdog
way
very_much,very_many
westward
wheelchair_tricycle
winter_day
winter_house
woodpecker
work_method
zigzag
zigzag_line
band_(of_frequencies)
beach_tennis_(activity)
beach_tennis_(sport)
beyond,past
binoculars,field_glass
broadband
church_ruin,temple_ruin,wreck,wreckage_(church,temple,mosque)_(1)
control
corruption
Danish_(class)
Danish_(language)
Denmark
disability,handicap,impairment
disability_benefit
disabled,impaired,handicapped_(intellectually,mentally)
disabled,impaired,handicapped_(physically)
distance
empower-(to)
empowered
empowerment
eternal
eternity,infinity
far,distant
fat,thick
guess,estimation
gym,gymnasium
gym_mat
Halloween,All_Saint's_Day
hearing_impairment
hearing-impaired
infinite,limitless
infiniteness,boundlessness,limitlessness
intellectual_impairment,cognitive_impairment,mental_impairment
lacrosse_(sport)
limit,restrict,restrain,confine-(to)
limited,restricted,confined
Loki
long_jump_(sport)
louse,stinging_insect
odometer
physical_impairment,physical_disability
placenta
power,powerfulness
powerful,mighty
sitski,sit_ski_(sport)
speech_impaired
speech_impairment,dysarthria
squash_(sport)
table_tennis,ping-pong_(activity)
table_tennis,ping-pong_(sport)
tennis,racket_sport,racquet_sport
tennis_(activity)
visual_impairment
visually_impaired
"""
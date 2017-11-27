# -*- coding: utf-8 -*-
"""
BLISS ENCODING:

    Conforms to encoding style specified here:
    http://std.dkuug.dk/JTC1/SC2/WG2/docs/n1866.pdf

    Contains 886 Blissymbols total. (Glyph 353C missing in link & font.)
"""
#import blissnet


BLISS_TO_UNICODE = {
    "raised wavy line": ["U+3200"],
    "squirrel": ["U+3201"],
    "fire": ["U+3202"],
    "mango": ["U+3203"],
    "horizontal wavy line on skyline": ["U+3204"],
    "cloud": ["U+3205"],
    "water": ["U+3206"],
    "oil": ["U+3207"],
    "three channels of water": ["U+3208"],
    "steam": ["U+3209"],
    "rain": ["U+320a"],
    "hail": ["U+320b"],
    "beverage": ["U+320c"],
    "basin": ["U+320d"],
    "ice": ["U+320e"],
    "pool": ["U+320f"],
    "snow": ["U+3210"],
    "snowflake": ["U+3211"],
    "freeze": ["U+3212"],
    "horizontal wavy line on earthline": ["U+3213"],
    "rice": ["U+3214"],
    "mud": ["U+3215"],
    "swamp": ["U+3216"],
    "island": ["U+3217"],
    "reversed wavy line": ["U+3218"],
    "medicine": ["U+3219"],
    "horizontal reversed wavy line": ["U+321a"],
    "sperm": ["U+321b"],
    "fertilization": ["U+321c"],
    "non-fertilization": ["U+321d"],
    "barrier contraceptive": ["U+321e"],
    "feeling": ["U+321f"],
    "expressing feelings": ["U+3220"],
    "comfort": ["U+3221"],
    "discomfort": ["U+3222"],
    "cloth": ["U+3223"],
    "number": ["U+3224"],
    "building": ["U+3225"],
    "garage": ["U+3226"],
    "mobile home": ["U+3227"],
    "yard": ["U+3228"],
    "fence": ["U+3229"],
    "chimney": ["U+322a"],
    "ear": ["U+322b"],
    "sound": ["U+322c"],
    "deafness": ["U+322d"],
    "extended arrow": ["U+322e"],
    "continue": ["U+322f"],
    "upward": ["U+3230"],
    "gas": ["U+3231"],
    "bubble": ["U+3232"],
    "give": ["U+3233"],
    "exchange": ["U+3234"],
    "upward and forward": ["U+3235"],
    "forward": ["U+3236"],
    "meet": ["U+3237"],
    "greetings and partings": ["U+3238"],
    "river": ["U+3239"],
    "agreement": ["U+323a"],
    "back and forth": ["U+323b"],
    "through": ["U+323c"],
    "visit": ["U+323d"],
    "understand": ["U+323e"],
    "into": ["U+323f"],
    "crush": ["U+3240"],
    "push": ["U+3241"],
    "squeeze": ["U+3242"],
    "end": ["U+3243"],
    "race": ["U+3244"],
    "downward and forward": ["U+3245"],
    "downward": ["U+3246"],
    "get": ["U+3247"],
    "crash": ["U+3248"],
    "downward and backward": ["U+3249"],
    "bent arrow": ["U+324a"],
    "mirror": ["U+324b"],
    "reversed arrow on skyline": ["U+324c"],
    "success": ["U+324d"],
    "backward": ["U+324e"],
    "opposing forces": ["U+324f"],
    "upward and backward": ["U+3250"],
    "gathering": ["U+3251"],
    "explosive": ["U+3252"],
    "year": ["U+3253"],
    "orbit": ["U+3254"],
    "atom": ["U+3255"],
    "nucleus": ["U+3256"],
    "rotate": ["U+3257"],
    "mix": ["U+3258"],
    "jump": ["U+3259"],
    "turn": ["U+325a"],
    "rotated jump": ["U+325b"],
    "swing": ["U+325c"],
    "half jump": ["U+325d"],
    "wheel of dharma": ["U+325e"],
    "tractor": ["U+325f"],
    "wheel": ["U+3260"],
    "journey": ["U+3261"],
    "tyre": ["U+3262"],
    "large circle centred on skyline": ["U+3263"],
    "balloon": ["U+3264"],
    "sun": ["U+3265"],
    "north": ["U+3266"],
    "east": ["U+3267"],
    "south": ["U+3268"],
    "west": ["U+3269"],
    "weather": ["U+326a"],
    "change": ["U+326b"],
    "development": ["U+326c"],
    "machine": ["U+326d"],
    "ring": ["U+326e"],
    "melon": ["U+326f"],
    "light": ["U+3270"],
    "egg": ["U+3271"],
    "disk": ["U+3272"],
    "head": ["U+3273"],
    "face": ["U+3274"],
    "chin": ["U+3275"],
    "cheek": ["U+3276"],
    "forehead": ["U+3277"],
    "beard": ["U+3278"],
    "pimple": ["U+3279"],
    "neck withhead": ["U+327a"],
    "raccoon": ["U+327b"],
    "bear": ["U+327c"],
    "day": ["U+327d"],
    "life": ["U+327e"],
    "death": ["U+327f"],
    "new": ["U+3280"],
    "pizza": ["U+3281"],
    "planet earth": ["U+3282"],
    "time": ["U+3283"],
    "small circle on skyline": ["U+3284"],
    "poetry": ["U+3285"],
    "metaphor": ["U+3286"],
    "pretend": ["U+3287"],
    "small circle beneath skyline": ["U+3288"],
    "generalization": ["U+3289"],
    "girl": ["U+328a"],
    "boy": ["U+328b"],
    "child": ["U+328c"],
    "money": ["U+328d"],
    "commerce": ["U+328e"],
    "flower": ["U+328f"],
    "stem": ["U+3290"],
    "garden": ["U+3291"],
    "flower from bulb": ["U+3292"],
    "bulb with flower": ["U+3293"],
    "plant": ["U+3294"],
    "park": ["U+3295"],
    "tennis": ["U+3296"],
    "mouth": ["U+3297"],
    "lips": ["U+3298"],
    "currants": ["U+3299"],
    "spider": ["U+329a"],
    "eye": ["U+329b"],
    "eyelid": ["U+329c"],
    "colour": ["U+329d"],
    "news": ["U+329e"],
    "eyeglasses": ["U+329f"],
    "blind": ["U+32a0"],
    "taste": ["U+32a1"],
    "food": ["U+32a2"],
    "spread": ["U+32a3"],
    "be": ["U+32a4"],
    "event": ["U+32a5"],
    "nonspeaking": ["U+32a6"],
    "name": ["U+32a7"],
    "language": ["U+32a8"],
    "combination": ["U+32a9"],
    "spit": ["U+32aa"],
    "kiss": ["U+32ab"],
    "grapes": ["U+32ac"],
    "bow": ["U+32ad"],
    "berry": ["U+32ae"],
    "strawberry": ["U+32af"],
    "small circle on earth line": ["U+32b0"],
    "disk": ["U+32b1"],
    "ball": ["U+32b2"],
    "bowling ball": ["U+32b3"],
    "earphones": ["U+32b4"],
    "fruit": ["U+32b5"],
    "citrus fruit": ["U+32b6"],
    "plum": ["U+32b7"],
    "cherries": ["U+32b8"],
    "tube": ["U+32b9"],
    "smoking": ["U+32ba"],
    "cigarette": ["U+32bb"],
    "pipe": ["U+32bc"],
    "baby girl": ["U+32bd"],
    "baby boy": ["U+32be"],
    "scissors": ["U+32bf"],
    "musical note": ["U+32c0"],
    "baby": ["U+32c1"],
    "indicator combine": ["U+32c2"],
    "indicator-sized circle": ["U+32c3"],
    "raspberry": ["U+32c4"],
    "large top half circle above skyline": ["U+32c5"],
    "conscience": ["U+32c6"],
    "forgive": ["U+32c7"],
    "moral": ["U+32c8"],
    "immoral": ["U+32c9"],
    "mind": ["U+32ca"],
    "wish": ["U+32cb"],
    "allow": ["U+32cc"],
    "decision": ["U+32cd"],
    "idea": ["U+32ce"],
    "opinion": ["U+32cf"],
    "observe": ["U+32d0"],
    "nonsense": ["U+32d1"],
    "state of mind": ["U+32d2"],
    "fact": ["U+32d3"],
    "meaning": ["U+32d4"],
    "use": ["U+32d5"],
    "knowledge": ["U+32d6"],
    "forget": ["U+32d7"],
    "system": ["U+32d8"],
    "kind": ["U+32d9"],
    "fan": ["U+32da"],
    "good": ["U+32db"],
    "science": ["U+32dc"],
    "truth": ["U+32dd"],
    "mathematics": ["U+32de"],
    "beetle": ["U+32df"],
    "tortoise": ["U+32e0"],
    "bad": ["U+32e1"],
    "judge": ["U+32e2"],
    "selfishness": ["U+32e3"],
    "consideration": ["U+32e4"],
    "doubt": ["U+32e5"],
    "interest": ["U+32e6"],
    "importance": ["U+32e7"],
    "calculate": ["U+32e8"],
    "lead": ["U+32e9"],
    "large top half circle on earthline": ["U+32ea"],
    "swan": ["U+32eb"],
    "fish": ["U+32ec"],
    "morning": ["U+32ed"],
    "horizon": ["U+32ee"],
    "curve": ["U+32ef"],
    "container": ["U+32f0"],
    "float": ["U+32f1"],
    "sieve": ["U+32f2"],
    "take": ["U+32f3"],
    "small top half circle on skyline": ["U+32f4"],
    "palm tree": ["U+32f5"],
    "small top half circle on midline": ["U+32f6"],
    "apple": ["U+32f7"],
    "peach": ["U+32f8"],
    "cabbage": ["U+32f9"],
    "suitcase": ["U+32fa"],
    "ice cream cone": ["U+32fb"],
    "handbag": ["U+32fc"],
    "dromedary": ["U+32fd"],
    "camel": ["U+32fe"],
    "bison": ["U+32ff"],
    "mushroom": ["U+3300"],
    "snake": ["U+3301"],
    "watersnake": ["U+3302"],
    "small right half circle": ["U+3303"],
    "dolphin": ["U+3304"],
    "small bottom half circle beneath skyline": ["U+3305"],
    "pig": ["U+3306"],
    "spiral": ["U+3307"],
    "small bottom half circle beneath midline": ["U+3308"],
    "gun": ["U+3309"],
    "small left half circle": ["U+330a"],
    "pliers": ["U+330b"],
    "dog": ["U+330c"],
    "tail": ["U+330d"],
    "upper right quarter circle on skyline": ["U+330e"],
    "pineapple": ["U+330f"],
    "upper right quarter circle beneath skyline": ["U+3310"],
    "wings": ["U+3311"],
    "airplane": ["U+3312"],
    "badminton bird": ["U+3313"],
    "talon": ["U+3314"],
    "angel": ["U+3315"],
    "fly": ["U+3316"],
    "bird": ["U+3317"],
    "waterbird": ["U+3318"],
    "bat": ["U+3319"],
    "upper right quarter circle on earthline": ["U+331a"],
    "leafy vegetable": ["U+331b"],
    "lower right quarter circle below skyline": ["U+331c"],
    "curtains": ["U+331d"],
    "tree": ["U+331e"],
    "branch": ["U+331f"],
    "trunk": ["U+3320"],
    "evergreen tree": ["U+3321"],
    "countryside": ["U+3322"],
    "lower right quarter circle on midline": ["U+3323"],
    "shrub": ["U+3324"],
    "lower right quarter circle below earth line": ["U+3325"],
    "pumpkin": ["U+3326"],
    "shamrock": ["U+3327"],
    "vegetable above ground": ["U+3328"],
    "cylinder-shaped vegetable": ["U+3329"],
    "corn": ["U+332a"],
    "celery": ["U+332b"],
    "lower left quarter circle on earthline": ["U+332c"],
    "cheese": ["U+332d"],
    "grass": ["U+332e"],
    "grain": ["U+332f"],
    "field": ["U+3330"],
    "iron": ["U+3331"],
    "beaver": ["U+3332"],
    "large horizontal parenthesis": ["U+3333"],
    "shellfish": ["U+3334"],
    "past": ["U+3335"],
    "present": ["U+3336"],
    "moon": ["U+3337"],
    "banana": ["U+3338"],
    "future": ["U+3339"],
    "bean": ["U+333a"],
    "peas": ["U+333b"],
    "expectation": ["U+333c"],
    "insurance": ["U+333d"],
    "snowshoe": ["U+333e"],
    "leaf": ["U+333f"],
    "turnip": ["U+3340"],
    "lemon": ["U+3341"],
    "butterfly": ["U+3342"],
    "body": ["U+3343"],
    "chest": ["U+3344"],
    "breasts": ["U+3345"],
    "crotch": ["U+3346"],
    "side of body": ["U+3347"],
    "waist": ["U+3348"],
    "shoulder": ["U+3349"],
    "neck withbody": ["U+334a"],
    "stomach": ["U+334b"],
    "embryo": ["U+334c"],
    "foetus": ["U+334d"],
    "pubic hair": ["U+334e"],
    "uterus": ["U+334f"],
    "birthgiving": ["U+3350"],
    "vagina": ["U+3351"],
    "ago": ["U+3352"],
    "now": ["U+3353"],
    "then": ["U+3354"],
    "olive": ["U+3355"],
    "pear": ["U+3356"],
    "avocado": ["U+3357"],
    "bread": ["U+3358"],
    "toast": ["U+3359"],
    "pita": ["U+335a"],
    "roll": ["U+335b"],
    "indicator past action": ["U+335c"],
    "indicator future action": ["U+335d"],
    "hair on head": ["U+335e"],
    "indicator-sized parenthesis": ["U+335f"],
    "hair": ["U+3360"],
    "fur": ["U+3361"],
    "pit": ["U+3362"],
    "enclosure": ["U+3363"],
    "bottom": ["U+3364"],
    "side of object": ["U+3365"],
    "top": ["U+3366"],
    "centre": ["U+3367"],
    "heater": ["U+3368"],
    "window with bars": ["U+3369"],
    "out of": ["U+336a"],
    "camera": ["U+336b"],
    "projector": ["U+336c"],
    "secret": ["U+336d"],
    "sleep": ["U+336e"],
    "crust": ["U+336f"],
    "inside": ["U+3370"],
    "outside": ["U+3371"],
    "post": ["U+3372"],
    "window": ["U+3373"],
    "all": ["U+3374"],
    "unionjack": ["U+3375"],
    "chest of drawers": ["U+3376"],
    "drawer": ["U+3377"],
    "book": ["U+3378"],
    "cupboard": ["U+3379"],
    "answer": ["U+337a"],
    "exit": ["U+337b"],
    "postcard": ["U+337c"],
    "cube": ["U+337d"],
    "small square below skyline": ["U+337e"],
    "transport": ["U+337f"],
    "cart": ["U+3380"],
    "lorry": ["U+3381"],
    "thing": ["U+3382"],
    "goods": ["U+3383"],
    "raw material": ["U+3384"],
    "waste": ["U+3385"],
    "waste container": ["U+3386"],
    "melt": ["U+3387"],
    "block": ["U+3388"],
    "ear mould": ["U+3389"],
    "pull": ["U+338a"],
    "small square on earthline": ["U+338b"],
    "solid thing": ["U+338c"],
    "sledge": ["U+338d"],
    "indicator thing": ["U+338e"],
    "indicator thing plural": ["U+338f"],
    "diagonal square on skyline": ["U+3390"],
    "kite": ["U+3391"],
    "extended rectable": ["U+3392"],
    "video cassette": ["U+3393"],
    "rectangle": ["U+3394"],
    "parcel": ["U+3395"],
    "paper": ["U+3396"],
    "door": ["U+3397"],
    "goal": ["U+3398"],
    "shelf": ["U+3399"],
    "room": ["U+339a"],
    "ceiling": ["U+339b"],
    "floor": ["U+339c"],
    "floor covering": ["U+339d"],
    "wall": ["U+339e"],
    "corner": ["U+339f"],
    "steam bath": ["U+33a0"],
    "shower": ["U+33a1"],
    "opening": ["U+33a2"],
    "fireplace": ["U+33a3"],
    "freedom": ["U+33a4"],
    "awake": ["U+33a5"],
    "question": ["U+33a6"],
    "public room": ["U+33a7"],
    "wide open rectangle beneath skyline": ["U+33a8"],
    "badge": ["U+33a9"],
    "table": ["U+33aa"],
    "board": ["U+33ab"],
    "edge": ["U+33ac"],
    "train platform": ["U+33ad"],
    "bus bay": ["U+33ae"],
    "pier": ["U+33af"],
    "wide top open rectangle below skyline": ["U+33b0"],
    "brush": ["U+33b1"],
    "box": ["U+33b2"],
    "comb": ["U+33b3"],
    "shekel": ["U+33b4"],
    "pot": ["U+33b5"],
    "glass": ["U+33b6"],
    "mug": ["U+33b7"],
    "tall left-open rectangle": ["U+33b8"],
    "effect": ["U+33b9"],
    "make": ["U+33ba"],
    "cause": ["U+33bb"],
    "therefore": ["U+33bc"],
    "mountain": ["U+33bd"],
    "mine": ["U+33be"],
    "stone": ["U+33bf"],
    "right triangle pointing tolower left": ["U+33c0"],
    "valley": ["U+33c1"],
    "dot aboveskyline": ["U+33c2"],
    "indicator description before the fact": ["U+33c3"],
    "dot onskyline": ["U+33c4"],
    "bone": ["U+33c5"],
    "structure": ["U+33c6"],
    "joint": ["U+33c7"],
    "dot below skyline": ["U+33c8"],
    "over": ["U+33c9"],
    "division": ["U+33ca"],
    "part": ["U+33cb"],
    "dot": ["U+33cc"],
    "again": ["U+33cd"],
    "there": ["U+33ce"],
    "before": ["U+33cf"],
    "around": ["U+33d0"],
    "either": ["U+33d1"],
    "dot below midline": ["U+33d2"],
    "that": ["U+33d3"],
    "dot on earth line": ["U+33d4"],
    "powder": ["U+33d5"],
    "northeast right angle": ["U+33d6"],
    "stamp": ["U+33d7"],
    "southwest right angle": ["U+33d8"],
    "fold": ["U+33d9"],
    "right angle": ["U+33da"],
    "space": ["U+33db"],
    "arm": ["U+33dc"],
    "wrist": ["U+33dd"],
    "elbow": ["U+33de"],
    "muscle": ["U+33df"],
    "strong": ["U+33e0"],
    "compel": ["U+33e1"],
    "health": ["U+33e2"],
    "person sitting": ["U+33e3"],
    "ride": ["U+33e4"],
    "small northwest right angle": ["U+33e5"],
    "steps": ["U+33e6"],
    "indicator-sized northeast right angle": ["U+33e7"],
    "tray": ["U+33e8"],
    "person standing": ["U+33e9"],
    "back of a person": ["U+33ea"],
    "buttocks": ["U+33eb"],
    "genitals": ["U+33ec"],
    "erection": ["U+33ed"],
    "male": ["U+33ee"],
    "penis": ["U+33ef"],
    "left": ["U+33f0"],
    "right": ["U+33f1"],
    "northeast long right angle": ["U+33f2"],
    "key": ["U+33f3"],
    "person lying down": ["U+33f4"],
    "protection": ["U+33f5"],
    "harbour": ["U+33f6"],
    "clothing": ["U+33f7"],
    "marriage": ["U+33f8"],
    "cone": ["U+33f9"],
    "farm": ["U+33fa"],
    "parent": ["U+33fb"],
    "birth": ["U+33fc"],
    "daughter": ["U+33fd"],
    "son": ["U+33fe"],
    "offspring": ["U+33ff"],
    "umbrella": ["U+3400"],
    "mother": ["U+3401"],
    "father": ["U+3402"],
    "relative": ["U+3403"],
    "wife": ["U+3404"],
    "stepmother": ["U+3405"],
    "grandparent": ["U+3406"],
    "aunt": ["U+3407"],
    "uncle": ["U+3408"],
    "grandmother": ["U+3409"],
    "maternal grandmother": ["U+340a"],
    "paternal grandmother": ["U+340b"],
    "grandfather": ["U+340c"],
    "maternal grandfather": ["U+340d"],
    "paternal grandfather": ["U+340e"],
    "up-pointing right angle on earth line": ["U+340f"],
    "illness": ["U+3410"],
    "relation pro": ["U+3411"],
    "purpose": ["U+3412"],
    "person weak": ["U+3413"],
    "down-pointing right angle belowskyline": ["U+3414"],
    "alcoholic beverage": ["U+3415"],
    "relation con": ["U+3416"],
    "opposition": ["U+3417"],
    "small up-pointing right angle belowskyline": ["U+3418"],
    "crystal": ["U+3419"],
    "in exchange for": ["U+341a"],
    "pointer": ["U+341b"],
    "about": ["U+341c"],
    "for the purpose of": ["U+341d"],
    "at": ["U+341e"],
    "here": ["U+341f"],
    "towards": ["U+3420"],
    "although": ["U+3421"],
    "by means of": ["U+3422"],
    "heat": ["U+3423"],
    "cold": ["U+3424"],
    "nuclear radiation": ["U+3425"],
    "or": ["U+3426"],
    "against": ["U+3427"],
    "person": ["U+3428"],
    "couple of persons": ["U+3429"],
    "first person": ["U+342a"],
    "second person": ["U+342b"],
    "third person": ["U+342c"],
    "spouse": ["U+342d"],
    "cohabiting family": ["U+342e"],
    "person needy": ["U+342f"],
    "mutual aid": ["U+3430"],
    "addition": ["U+3431"],
    "possess": ["U+3432"],
    "with the help of": ["U+3433"],
    "and": ["U+3434"],
    "small crosson earth line": ["U+3435"],
    "have to": ["U+3436"],
    "belongs to": ["U+3437"],
    "cross": ["U+3438"],
    "across": ["U+3439"],
    "multiplication": ["U+343a"],
    "small diagonal cross below skyline": ["U+343b"],
    "choice": ["U+343c"],
    "more": ["U+343d"],
    "much": ["U+343e"],
    "war": ["U+343f"],
    "indicator plural": ["U+3440"],
    "indicator-sized cross below skyline": ["U+3441"],
    "wand": ["U+3442"],
    "indicator-sized cross on midline": ["U+3443"],
    "star": ["U+3444"],
    "muslim": ["U+3445"],
    "indicator-sized cross on earth line": ["U+3446"],
    "comet": ["U+3447"],
    "knife": ["U+3448"],
    "sharp point": ["U+3449"],
    "plough": ["U+344a"],
    "creation": ["U+344b"],
    "star of david": ["U+344c"],
    "danger": ["U+344d"],
    "pyramid": ["U+344e"],
    "small isosceles triangle on midline": ["U+344f"],
    "rocket": ["U+3450"],
    "female": ["U+3451"],
    "tooth": ["U+3452"],
    "teeth": ["U+3453"],
    "cavity": ["U+3454"],
    "large symmetric acute angle above skyline": ["U+3455"],
    "god": ["U+3456"],
    "action": ["U+3457"],
    "legs and feet": ["U+3458"],
    "hip": ["U+3459"],
    "leg": ["U+345a"],
    "heel": ["U+345b"],
    "foot": ["U+345c"],
    "kick": ["U+345d"],
    "toe": ["U+345e"],
    "roller skates": ["U+345f"],
    "ice skates": ["U+3460"],
    "evaluation": ["U+3461"],
    "small symmetric acute angle on midline": ["U+3462"],
    "work": ["U+3463"],
    "action or male": ["U+3464"],
    "gender": ["U+3465"],
    "insect": ["U+3466"],
    "indicator action": ["U+3467"],
    "indicator active": ["U+3468"],
    "indicator description": ["U+3469"],
    "indicator description after the fact": ["U+346a"],
    "indicator past passive": ["U+346b"],
    "indicator future passive": ["U+346c"],
    "indicator passive": ["U+346d"],
    "indicator passive conditional": ["U+346e"],
    "indicator past passive conditional": ["U+346f"],
    "indicator future passive conditional": ["U+3470"],
    "up-pointing left half of right triangle": ["U+3471"],
    "electricity": ["U+3472"],
    "pointing": ["U+3473"],
    "hand": ["U+3474"],
    "thumb": ["U+3475"],
    "finger": ["U+3476"],
    "tool": ["U+3477"],
    "barb pointing up": ["U+3478"],
    "opposite": ["U+3479"],
    "nose": ["U+347a"],
    "odour": ["U+347b"],
    "extended horizontal line on earth line": ["U+347c"],
    "road": ["U+347d"],
    "long horizontal line on midline": ["U+347e"],
    "bus": ["U+347f"],
    "long horizontal line on earth line": ["U+3480"],
    "worm": ["U+3481"],
    "sky": ["U+3482"],
    "fog": ["U+3483"],
    "environment": ["U+3484"],
    "peace": ["U+3485"],
    "disturbance": ["U+3486"],
    "world": ["U+3487"],
    "blissymbol": ["U+3488"],
    "lightning": ["U+3489"],
    "air": ["U+348a"],
    "wind": ["U+348b"],
    "subtraction": ["U+348c"],
    "vehicle": ["U+348d"],
    "automobile": ["U+348e"],
    "steering wheel": ["U+348f"],
    "fill": ["U+3490"],
    "sailboat": ["U+3491"],
    "under": ["U+3492"],
    "weight": ["U+3493"],
    "animal": ["U+3494"],
    "paw": ["U+3495"],
    "water animal": ["U+3496"],
    "hippopotamus": ["U+3497"],
    "cervine animal": ["U+3498"],
    "bovine animal": ["U+3499"],
    "horn or antler": ["U+349a"],
    "feline animal": ["U+349b"],
    "claw": ["U+349c"],
    "giraffe": ["U+349d"],
    "horse": ["U+349e"],
    "rhinoceros": ["U+349f"],
    "horn": ["U+34a0"],
    "hanger": ["U+34a1"],
    "ground": ["U+34a2"],
    "place": ["U+34a3"],
    "vegetable below ground": ["U+34a4"],
    "bulb": ["U+34a5"],
    "onion": ["U+34a6"],
    "roots": ["U+34a7"],
    "seed": ["U+34a8"],
    "carrot": ["U+34a9"],
    "grave": ["U+34aa"],
    "snail": ["U+34ab"],
    "lawn": ["U+34ac"],
    "night": ["U+34ad"],
    "evening": ["U+34ae"],
    "shore": ["U+34af"],
    "street": ["U+34b0"],
    "ski": ["U+34b1"],
    "skateboard": ["U+34b2"],
    "short horizontal line on sky line": ["U+34b3"],
    "adult": ["U+34b4"],
    "teenager": ["U+34b5"],
    "eyebrow": ["U+34b6"],
    "large": ["U+34b7"],
    "temperature": ["U+34b8"],
    "most": ["U+34b9"],
    "high": ["U+34ba"],
    "nail": ["U+34bb"],
    "shovel": ["U+34bc"],
    "dig": ["U+34bd"],
    "short horizontal line below skyline": ["U+34be"],
    "same": ["U+34bf"],
    "different": ["U+34c0"],
    "not": ["U+34c1"],
    "nowhere": ["U+34c2"],
    "low": ["U+34c3"],
    "pin": ["U+34c4"],
    "small": ["U+34c5"],
    "love": ["U+34c6"],
    "but": ["U+34c7"],
    "break": ["U+34c8"],
    "short horizontal line on earth line": ["U+34c9"],
    "on": ["U+34ca"],
    "bridge": ["U+34cb"],
    "hole": ["U+34cc"],
    "indicator-sized horizontal line": ["U+34cd"],
    "maple leaf": ["U+34ce"],
    "line": ["U+34cf"],
    "screw": ["U+34d0"],
    "after": ["U+34d1"],
    "between": ["U+34d2"],
    "attach": ["U+34d3"],
    "parallel": ["U+34d4"],
    "other": ["U+34d5"],
    "copy": ["U+34d6"],
    "thin": ["U+34d7"],
    "limits": ["U+34d8"],
    "deep": ["U+34d9"],
    "thick": ["U+34da"],
    "wide": ["U+34db"],
    "broom": ["U+34dc"],
    "perpendicular": ["U+34dd"],
    "beginning": ["U+34de"],
    "interval": ["U+34df"],
    "month": ["U+34e0"],
    "needle": ["U+34e1"],
    "high three-quarter length vertical line": ["U+34e2"],
    "account": ["U+34e3"],
    "low three-quarter length vertical line": ["U+34e4"],
    "commandments": ["U+34e5"],
    "small vertical line below skyline": ["U+34e6"],
    "chair": ["U+34e7"],
    "toilet": ["U+34e8"],
    "wheelchair": ["U+34e9"],
    "armchair": ["U+34ea"],
    "bed": ["U+34eb"],
    "pillow": ["U+34ec"],
    "bottle": ["U+34ed"],
    "woman": ["U+34ee"],
    "lesbian couple": ["U+34ef"],
    "first person feminine": ["U+34f0"],
    "second person feminine": ["U+34f1"],
    "third person feminine": ["U+34f2"],
    "cohabiting lesbian couple": ["U+34f3"],
    "man": ["U+34f4"],
    "first person masculine": ["U+34f5"],
    "second person masculine": ["U+34f6"],
    "third person masculine": ["U+34f7"],
    "citizen": ["U+34f8"],
    "husband": ["U+34f9"],
    "cohabiting heterosexual couple": ["U+34fa"],
    "cohabiting homosexual couple": ["U+34fb"],
    "stepfather": ["U+34fc"],
    "married family": ["U+34fd"],
    "heterosexual couple": ["U+34fe"],
    "homosexual couple": ["U+34ff"],
    "boat": ["U+3500"],
    "sack": ["U+3501"],
    "crab": ["U+3502"],
    "person kneeling": ["U+3503"],
    "ankle": ["U+3504"],
    "knee": ["U+3505"],
    "menorah": ["U+3506"],
    "small verticalline on midline": ["U+3507"],
    "near": ["U+3508"],
    "at a distance": ["U+3509"],
    "far": ["U+350a"],
    "from": ["U+350b"],
    "cancontainer": ["U+350c"],
    "length": ["U+350d"],
    "measurement": ["U+350e"],
    "injection": ["U+350f"],
    "hypodermic needle": ["U+3510"],
    "short": ["U+3511"],
    "pepper": ["U+3512"],
    "it": ["U+3513"],
    "until": ["U+3514"],
    "flag": ["U+3515"],
    "country": ["U+3516"],
    "sail": ["U+3517"],
    "crown": ["U+3518"],
    "shallow": ["U+3519"],
    "fight": ["U+351a"],
    "soft": ["U+351b"],
    "indicator-sized vertical line on skyline": ["U+351c"],
    "etrog": ["U+351d"],
    "megillah": ["U+351e"],
    "torah": ["U+351f"],
    "ladder": ["U+3520"],
    "indicator-sized verticalline on midline": ["U+3521"],
    "spinning top": ["U+3522"],
    "diagonal of verticalrectangle": ["U+3523"],
    "help": ["U+3524"],
    "reversed diagonal of vertical rectangle": ["U+3525"],
    "sport stick": ["U+3526"],
    "hockey stick": ["U+3527"],
    "golfclub": ["U+3528"],
    "short reversed diagonal of vertical rectangle": ["U+3529"],
    "bucket": ["U+352a"],
    "diagonal of horizontal rectangle": ["U+352b"],
    "helicopter": ["U+352c"],
    "seesaw": ["U+352d"],
    "reversed diagonal of horizontal rectangle": ["U+352e"],
    "electromagnetic radiation": ["U+352f"],
    "energy": ["U+3530"],
    "fuel": ["U+3531"],
    "microwave oven": ["U+3532"],
    "power": ["U+3533"],
    "extended diagonal of square": ["U+3534"],
    "saw": ["U+3535"],
    "diagonal of square on skyline": ["U+3536"],
    "tank": ["U+3537"],
    "destroy": ["U+3538"],
    "angle": ["U+3539"],
    "cannon": ["U+353a"],
    "chemical product": ["U+353b"],
    "three-quarter sized diagonal of square": ["U+353c"],
    "smalldiagonal of square": ["U+353d"],
    "fork": ["U+353e"],
    "hammer": ["U+353f"],
    "the": ["U+3540"],
    "this": ["U+3541"],
    "small diagonal of square above earthline": ["U+3542"],
    "spoon": ["U+3543"],
    "racquet": ["U+3544"],
    "pen": ["U+3545"],
    "reversed smalldiagonal of square": ["U+3546"],
    "couch": ["U+3547"],
    "pitcher": ["U+3548"],
    "wagon": ["U+3549"],
    "hedgehog": ["U+354a"],
    "quill": ["U+354b"],
    "a or any": ["U+354c"],
    "somewhere": ["U+354d"],
    "reversed small diagonal of square above earthline": ["U+354e"],
    "soup": ["U+354f"],
    "salad": ["U+3550"],
    "dish": ["U+3551"],
    "cereal": ["U+3552"],
    "apostrophe on midline": ["U+3553"],
    "relativizer": ["U+3554"],
    "what": ["U+3555"],
    "where": ["U+3556"],
    "command": ["U+3557"],
    "full stop": ["U+3558"],
    "comma": ["U+3559"],
    "colon": ["U+355a"],
    "semicolon": ["U+355b"],
    "question mark": ["U+355c"],
    "exclamation mark": ["U+355d"],
    "alphabet": ["U+355e"],
    "zero": ["U+355f"],
    "one": ["U+3560"],
    "self": ["U+3561"],
    "two": ["U+3562"],
    "three": ["U+3563"],
    "four": ["U+3564"],
    "five": ["U+3565"],
    "six": ["U+3566"],
    "seven": ["U+3567"],
    "eight": ["U+3568"],
    "nine": ["U+3569"],
    "percent sign": ["U+356a"],
    "cent sign": ["U+356b"],
    "dollar sign": ["U+356c"],
    "pound sign": ["U+356d"],
    "yen sign": ["U+356e"],
    "euro sign": ["U+356f"],
    "indicator conditional": ["U+3570"],
    "indicator past conditional": ["U+3571"],
    "indicator future conditional": ["U+3572"],
    "space (whitespace)": ["U+3573"],
    "half space": ["U+3574"],
    "quarter space": ["U+3575"],
    "difficult": ["U+3576"],
}

UNICODE_TO_BLISS = {
    "U+3200": ["raised wavy line"],
    "U+3201": ["squirrel"],
    "U+3202": ["fire"],
    "U+3203": ["mango"],
    "U+3204": ["horizontal wavy line on skyline"],
    "U+3205": ["cloud"],
    "U+3206": ["water"],
    "U+3207": ["oil"],
    "U+3208": ["three channels of water"],
    "U+3209": ["steam"],
    "U+320a": ["rain"],
    "U+320b": ["hail"],
    "U+320c": ["beverage"],
    "U+320d": ["basin"],
    "U+320e": ["ice"],
    "U+320f": ["pool"],
    "U+3210": ["snow"],
    "U+3211": ["snowflake"],
    "U+3212": ["freeze"],
    "U+3213": ["horizontal wavy line on earthline"],
    "U+3214": ["rice"],
    "U+3215": ["mud"],
    "U+3216": ["swamp"],
    "U+3217": ["island"],
    "U+3218": ["reversed wavy line"],
    "U+3219": ["medicine"],
    "U+321a": ["horizontal reversed wavy line"],
    "U+321b": ["sperm"],
    "U+321c": ["fertilization"],
    "U+321d": ["non-fertilization"],
    "U+321e": ["barrier contraceptive"],
    "U+321f": ["feeling"],
    "U+3220": ["expressing feelings"],
    "U+3221": ["comfort"],
    "U+3222": ["discomfort"],
    "U+3223": ["cloth"],
    "U+3224": ["number"],
    "U+3225": ["building"],
    "U+3226": ["garage"],
    "U+3227": ["mobile home"],
    "U+3228": ["yard"],
    "U+3229": ["fence"],
    "U+322a": ["chimney"],
    "U+322b": ["ear"],
    "U+322c": ["sound"],
    "U+322d": ["deafness"],
    "U+322e": ["extended arrow"],
    "U+322f": ["continue"],
    "U+3230": ["upward"],
    "U+3231": ["gas"],
    "U+3232": ["bubble"],
    "U+3233": ["give"],
    "U+3234": ["exchange"],
    "U+3235": ["upward and forward"],
    "U+3236": ["forward"],
    "U+3237": ["meet"],
    "U+3238": ["greetings and partings"],
    "U+3239": ["river"],
    "U+323a": ["agreement"],
    "U+323b": ["back and forth"],
    "U+323c": ["through"],
    "U+323d": ["visit"],
    "U+323e": ["understand"],
    "U+323f": ["into"],
    "U+3240": ["crush"],
    "U+3241": ["push"],
    "U+3242": ["squeeze"],
    "U+3243": ["end"],
    "U+3244": ["race"],
    "U+3245": ["downward and forward"],
    "U+3246": ["downward"],
    "U+3247": ["get"],
    "U+3248": ["crash"],
    "U+3249": ["downward and backward"],
    "U+324a": ["bent arrow"],
    "U+324b": ["mirror"],
    "U+324c": ["reversed arrow on skyline"],
    "U+324d": ["success"],
    "U+324e": ["backward"],
    "U+324f": ["opposing forces"],
    "U+3250": ["upward and backward"],
    "U+3251": ["gathering"],
    "U+3252": ["explosive"],
    "U+3253": ["year"],
    "U+3254": ["orbit"],
    "U+3255": ["atom"],
    "U+3256": ["nucleus"],
    "U+3257": ["rotate"],
    "U+3258": ["mix"],
    "U+3259": ["jump"],
    "U+325a": ["turn"],
    "U+325b": ["rotated jump"],
    "U+325c": ["swing"],
    "U+325d": ["half jump"],
    "U+325e": ["wheel of dharma"],
    "U+325f": ["tractor"],
    "U+3260": ["wheel"],
    "U+3261": ["journey"],
    "U+3262": ["tyre"],
    "U+3263": ["large circle centred on skyline"],
    "U+3264": ["balloon"],
    "U+3265": ["sun"],
    "U+3266": ["north"],
    "U+3267": ["east"],
    "U+3268": ["south"],
    "U+3269": ["west"],
    "U+326a": ["weather"],
    "U+326b": ["change"],
    "U+326c": ["development"],
    "U+326d": ["machine"],
    "U+326e": ["ring"],
    "U+326f": ["melon"],
    "U+3270": ["light"],
    "U+3271": ["egg"],
    "U+3272": ["disk"],
    "U+3273": ["head"],
    "U+3274": ["face"],
    "U+3275": ["chin"],
    "U+3276": ["cheek"],
    "U+3277": ["forehead"],
    "U+3278": ["beard"],
    "U+3279": ["pimple"],
    "U+327a": ["neck withhead"],
    "U+327b": ["raccoon"],
    "U+327c": ["bear"],
    "U+327d": ["day"],
    "U+327e": ["life"],
    "U+327f": ["death"],
    "U+3280": ["new"],
    "U+3281": ["pizza"],
    "U+3282": ["planet earth"],
    "U+3283": ["time"],
    "U+3284": ["small circle on skyline"],
    "U+3285": ["poetry"],
    "U+3286": ["metaphor"],
    "U+3287": ["pretend"],
    "U+3288": ["small circle beneath skyline"],
    "U+3289": ["generalization"],
    "U+328a": ["girl"],
    "U+328b": ["boy"],
    "U+328c": ["child"],
    "U+328d": ["money"],
    "U+328e": ["commerce"],
    "U+328f": ["flower"],
    "U+3290": ["stem"],
    "U+3291": ["garden"],
    "U+3292": ["flower from bulb"],
    "U+3293": ["bulb with flower"],
    "U+3294": ["plant"],
    "U+3295": ["park"],
    "U+3296": ["tennis"],
    "U+3297": ["mouth"],
    "U+3298": ["lips"],
    "U+3299": ["currants"],
    "U+329a": ["spider"],
    "U+329b": ["eye"],
    "U+329c": ["eyelid"],
    "U+329d": ["colour"],
    "U+329e": ["news"],
    "U+329f": ["eyeglasses"],
    "U+32a0": ["blind"],
    "U+32a1": ["taste"],
    "U+32a2": ["food"],
    "U+32a3": ["spread"],
    "U+32a4": ["be"],
    "U+32a5": ["event"],
    "U+32a6": ["nonspeaking"],
    "U+32a7": ["name"],
    "U+32a8": ["language"],
    "U+32a9": ["combination"],
    "U+32aa": ["spit"],
    "U+32ab": ["kiss"],
    "U+32ac": ["grapes"],
    "U+32ad": ["bow"],
    "U+32ae": ["berry"],
    "U+32af": ["strawberry"],
    "U+32b0": ["small circle on earth line"],
    "U+32b1": ["disk"],
    "U+32b2": ["ball"],
    "U+32b3": ["bowling ball"],
    "U+32b4": ["earphones"],
    "U+32b5": ["fruit"],
    "U+32b6": ["citrus fruit"],
    "U+32b7": ["plum"],
    "U+32b8": ["cherries"],
    "U+32b9": ["tube"],
    "U+32ba": ["smoking"],
    "U+32bb": ["cigarette"],
    "U+32bc": ["pipe"],
    "U+32bd": ["baby girl"],
    "U+32be": ["baby boy"],
    "U+32bf": ["scissors"],
    "U+32c0": ["musical note"],
    "U+32c1": ["baby"],
    "U+32c2": ["indicator combine"],
    "U+32c3": ["indicator-sized circle"],
    "U+32c4": ["raspberry"],
    "U+32c5": ["large top half circle above skyline"],
    "U+32c6": ["conscience"],
    "U+32c7": ["forgive"],
    "U+32c8": ["moral"],
    "U+32c9": ["immoral"],
    "U+32ca": ["mind"],
    "U+32cb": ["wish"],
    "U+32cc": ["allow"],
    "U+32cd": ["decision"],
    "U+32ce": ["idea"],
    "U+32cf": ["opinion"],
    "U+32d0": ["observe"],
    "U+32d1": ["nonsense"],
    "U+32d2": ["state of mind"],
    "U+32d3": ["fact"],
    "U+32d4": ["meaning"],
    "U+32d5": ["use"],
    "U+32d6": ["knowledge"],
    "U+32d7": ["forget"],
    "U+32d8": ["system"],
    "U+32d9": ["kind"],
    "U+32da": ["fan"],
    "U+32db": ["good"],
    "U+32dc": ["science"],
    "U+32dd": ["truth"],
    "U+32de": ["mathematics"],
    "U+32df": ["beetle"],
    "U+32e0": ["tortoise"],
    "U+32e1": ["bad"],
    "U+32e2": ["judge"],
    "U+32e3": ["selfishness"],
    "U+32e4": ["consideration"],
    "U+32e5": ["doubt"],
    "U+32e6": ["interest"],
    "U+32e7": ["importance"],
    "U+32e8": ["calculate"],
    "U+32e9": ["lead"],
    "U+32ea": ["large top half circle on earthline"],
    "U+32eb": ["swan"],
    "U+32ec": ["fish"],
    "U+32ed": ["morning"],
    "U+32ee": ["horizon"],
    "U+32ef": ["curve"],
    "U+32f0": ["container"],
    "U+32f1": ["float"],
    "U+32f2": ["sieve"],
    "U+32f3": ["take"],
    "U+32f4": ["small top half circle on skyline"],
    "U+32f5": ["palm tree"],
    "U+32f6": ["small top half circle on midline"],
    "U+32f7": ["apple"],
    "U+32f8": ["peach"],
    "U+32f9": ["cabbage"],
    "U+32fa": ["suitcase"],
    "U+32fb": ["ice cream cone"],
    "U+32fc": ["handbag"],
    "U+32fd": ["dromedary"],
    "U+32fe": ["camel"],
    "U+32ff": ["bison"],
    "U+3300": ["mushroom"],
    "U+3301": ["snake"],
    "U+3302": ["watersnake"],
    "U+3303": ["small right half circle"],
    "U+3304": ["dolphin"],
    "U+3305": ["small bottom half circle beneath skyline"],
    "U+3306": ["pig"],
    "U+3307": ["spiral"],
    "U+3308": ["small bottom half circle beneath midline"],
    "U+3309": ["gun"],
    "U+330a": ["small left half circle"],
    "U+330b": ["pliers"],
    "U+330c": ["dog"],
    "U+330d": ["tail"],
    "U+330e": ["upper right quarter circle on skyline"],
    "U+330f": ["pineapple"],
    "U+3310": ["upper right quarter circle beneath skyline"],
    "U+3311": ["wings"],
    "U+3312": ["airplane"],
    "U+3313": ["badminton bird"],
    "U+3314": ["talon"],
    "U+3315": ["angel"],
    "U+3316": ["fly"],
    "U+3317": ["bird"],
    "U+3318": ["waterbird"],
    "U+3319": ["bat"],
    "U+331a": ["upper right quarter circle on earthline"],
    "U+331b": ["leafy vegetable"],
    "U+331c": ["lower right quarter circle below skyline"],
    "U+331d": ["curtains"],
    "U+331e": ["tree"],
    "U+331f": ["branch"],
    "U+3320": ["trunk"],
    "U+3321": ["evergreen tree"],
    "U+3322": ["countryside"],
    "U+3323": ["lower right quarter circle on midline"],
    "U+3324": ["shrub"],
    "U+3325": ["lower right quarter circle below earth line"],
    "U+3326": ["pumpkin"],
    "U+3327": ["shamrock"],
    "U+3328": ["vegetable above ground"],
    "U+3329": ["cylinder-shaped vegetable"],
    "U+332a": ["corn"],
    "U+332b": ["celery"],
    "U+332c": ["lower left quarter circle on earthline"],
    "U+332d": ["cheese"],
    "U+332e": ["grass"],
    "U+332f": ["grain"],
    "U+3330": ["field"],
    "U+3331": ["iron"],
    "U+3332": ["beaver"],
    "U+3333": ["large horizontal parenthesis"],
    "U+3334": ["shellfish"],
    "U+3335": ["past"],
    "U+3336": ["present"],
    "U+3337": ["moon"],
    "U+3338": ["banana"],
    "U+3339": ["future"],
    "U+333a": ["bean"],
    "U+333b": ["peas"],
    "U+333c": ["expectation"],
    "U+333d": ["insurance"],
    "U+333e": ["snowshoe"],
    "U+333f": ["leaf"],
    "U+3340": ["turnip"],
    "U+3341": ["lemon"],
    "U+3342": ["butterfly"],
    "U+3343": ["body"],
    "U+3344": ["chest"],
    "U+3345": ["breasts"],
    "U+3346": ["crotch"],
    "U+3347": ["side of body"],
    "U+3348": ["waist"],
    "U+3349": ["shoulder"],
    "U+334a": ["neck withbody"],
    "U+334b": ["stomach"],
    "U+334c": ["embryo"],
    "U+334d": ["foetus"],
    "U+334e": ["pubic hair"],
    "U+334f": ["uterus"],
    "U+3350": ["birthgiving"],
    "U+3351": ["vagina"],
    "U+3352": ["ago"],
    "U+3353": ["now"],
    "U+3354": ["then"],
    "U+3355": ["olive"],
    "U+3356": ["pear"],
    "U+3357": ["avocado"],
    "U+3358": ["bread"],
    "U+3359": ["toast"],
    "U+335a": ["pita"],
    "U+335b": ["roll"],
    "U+335c": ["indicator past action"],
    "U+335d": ["indicator future action"],
    "U+335e": ["hair on head"],
    "U+335f": ["indicator-sized parenthesis"],
    "U+3360": ["hair"],
    "U+3361": ["fur"],
    "U+3362": ["pit"],
    "U+3363": ["enclosure"],
    "U+3364": ["bottom"],
    "U+3365": ["side of object"],
    "U+3366": ["top"],
    "U+3367": ["centre"],
    "U+3368": ["heater"],
    "U+3369": ["window with bars"],
    "U+336a": ["out of"],
    "U+336b": ["camera"],
    "U+336c": ["projector"],
    "U+336d": ["secret"],
    "U+336e": ["sleep"],
    "U+336f": ["crust"],
    "U+3370": ["inside"],
    "U+3371": ["outside"],
    "U+3372": ["post"],
    "U+3373": ["window"],
    "U+3374": ["all"],
    "U+3375": ["unionjack"],
    "U+3376": ["chest of drawers"],
    "U+3377": ["drawer"],
    "U+3378": ["book"],
    "U+3379": ["cupboard"],
    "U+337a": ["answer"],
    "U+337b": ["exit"],
    "U+337c": ["postcard"],
    "U+337d": ["cube"],
    "U+337e": ["small square below skyline"],
    "U+337f": ["transport"],
    "U+3380": ["cart"],
    "U+3381": ["lorry"],
    "U+3382": ["thing"],
    "U+3383": ["goods"],
    "U+3384": ["raw material"],
    "U+3385": ["waste"],
    "U+3386": ["waste container"],
    "U+3387": ["melt"],
    "U+3388": ["block"],
    "U+3389": ["ear mould"],
    "U+338a": ["pull"],
    "U+338b": ["small square on earthline"],
    "U+338c": ["solid thing"],
    "U+338d": ["sledge"],
    "U+338e": ["indicator thing"],
    "U+338f": ["indicator thing plural"],
    "U+3390": ["diagonal square on skyline"],
    "U+3391": ["kite"],
    "U+3392": ["extended rectable"],
    "U+3393": ["video cassette"],
    "U+3394": ["rectangle"],
    "U+3395": ["parcel"],
    "U+3396": ["paper"],
    "U+3397": ["door"],
    "U+3398": ["goal"],
    "U+3399": ["shelf"],
    "U+339a": ["room"],
    "U+339b": ["ceiling"],
    "U+339c": ["floor"],
    "U+339d": ["floor covering"],
    "U+339e": ["wall"],
    "U+339f": ["corner"],
    "U+33a0": ["steam bath"],
    "U+33a1": ["shower"],
    "U+33a2": ["opening"],
    "U+33a3": ["fireplace"],
    "U+33a4": ["freedom"],
    "U+33a5": ["awake"],
    "U+33a6": ["question"],
    "U+33a7": ["public room"],
    "U+33a8": ["wide open rectangle beneath skyline"],
    "U+33a9": ["badge"],
    "U+33aa": ["table"],
    "U+33ab": ["board"],
    "U+33ac": ["edge"],
    "U+33ad": ["train platform"],
    "U+33ae": ["bus bay"],
    "U+33af": ["pier"],
    "U+33b0": ["wide top open rectangle below skyline"],
    "U+33b1": ["brush"],
    "U+33b2": ["box"],
    "U+33b3": ["comb"],
    "U+33b4": ["shekel"],
    "U+33b5": ["pot"],
    "U+33b6": ["glass"],
    "U+33b7": ["mug"],
    "U+33b8": ["tall left-open rectangle"],
    "U+33b9": ["effect"],
    "U+33ba": ["make"],
    "U+33bb": ["cause"],
    "U+33bc": ["therefore"],
    "U+33bd": ["mountain"],
    "U+33be": ["mine"],
    "U+33bf": ["stone"],
    "U+33c0": ["right triangle pointing tolower left"],
    "U+33c1": ["valley"],
    "U+33c2": ["dot aboveskyline"],
    "U+33c3": ["indicator description before the fact"],
    "U+33c4": ["dot onskyline"],
    "U+33c5": ["bone"],
    "U+33c6": ["structure"],
    "U+33c7": ["joint"],
    "U+33c8": ["dot below skyline"],
    "U+33c9": ["over"],
    "U+33ca": ["division"],
    "U+33cb": ["part"],
    "U+33cc": ["dot"],
    "U+33cd": ["again"],
    "U+33ce": ["there"],
    "U+33cf": ["before"],
    "U+33d0": ["around"],
    "U+33d1": ["either"],
    "U+33d2": ["dot below midline"],
    "U+33d3": ["that"],
    "U+33d4": ["dot on earth line"],
    "U+33d5": ["powder"],
    "U+33d6": ["northeast right angle"],
    "U+33d7": ["stamp"],
    "U+33d8": ["southwest right angle"],
    "U+33d9": ["fold"],
    "U+33da": ["right angle"],
    "U+33db": ["space"],
    "U+33dc": ["arm"],
    "U+33dd": ["wrist"],
    "U+33de": ["elbow"],
    "U+33df": ["muscle"],
    "U+33e0": ["strong"],
    "U+33e1": ["compel"],
    "U+33e2": ["health"],
    "U+33e3": ["person sitting"],
    "U+33e4": ["ride"],
    "U+33e5": ["small northwest right angle"],
    "U+33e6": ["steps"],
    "U+33e7": ["indicator-sized northeast right angle"],
    "U+33e8": ["tray"],
    "U+33e9": ["person standing"],
    "U+33ea": ["back of a person"],
    "U+33eb": ["buttocks"],
    "U+33ec": ["genitals"],
    "U+33ed": ["erection"],
    "U+33ee": ["male"],
    "U+33ef": ["penis"],
    "U+33f0": ["left"],
    "U+33f1": ["right"],
    "U+33f2": ["northeast long right angle"],
    "U+33f3": ["key"],
    "U+33f4": ["person lying down"],
    "U+33f5": ["protection"],
    "U+33f6": ["harbour"],
    "U+33f7": ["clothing"],
    "U+33f8": ["marriage"],
    "U+33f9": ["cone"],
    "U+33fa": ["farm"],
    "U+33fb": ["parent"],
    "U+33fc": ["birth"],
    "U+33fd": ["daughter"],
    "U+33fe": ["son"],
    "U+33ff": ["offspring"],
    "U+3400": ["umbrella"],
    "U+3401": ["mother"],
    "U+3402": ["father"],
    "U+3403": ["relative"],
    "U+3404": ["wife"],
    "U+3405": ["stepmother"],
    "U+3406": ["grandparent"],
    "U+3407": ["aunt"],
    "U+3408": ["uncle"],
    "U+3409": ["grandmother"],
    "U+340a": ["maternal grandmother"],
    "U+340b": ["paternal grandmother"],
    "U+340c": ["grandfather"],
    "U+340d": ["maternal grandfather"],
    "U+340e": ["paternal grandfather"],
    "U+340f": ["up-pointing right angle on earth line"],
    "U+3410": ["illness"],
    "U+3411": ["relation pro"],
    "U+3412": ["purpose"],
    "U+3413": ["person weak"],
    "U+3414": ["down-pointing right angle belowskyline"],
    "U+3415": ["alcoholic beverage"],
    "U+3416": ["relation con"],
    "U+3417": ["opposition"],
    "U+3418": ["small up-pointing right angle belowskyline"],
    "U+3419": ["crystal"],
    "U+341a": ["in exchange for"],
    "U+341b": ["pointer"],
    "U+341c": ["about"],
    "U+341d": ["for the purpose of"],
    "U+341e": ["at"],
    "U+341f": ["here"],
    "U+3420": ["towards"],
    "U+3421": ["although"],
    "U+3422": ["by means of"],
    "U+3423": ["heat"],
    "U+3424": ["cold"],
    "U+3425": ["nuclear radiation"],
    "U+3426": ["or"],
    "U+3427": ["against"],
    "U+3428": ["person"],
    "U+3429": ["couple of persons"],
    "U+342a": ["first person"],
    "U+342b": ["second person"],
    "U+342c": ["third person"],
    "U+342d": ["spouse"],
    "U+342e": ["cohabiting family"],
    "U+342f": ["person needy"],
    "U+3430": ["mutual aid"],
    "U+3431": ["addition"],
    "U+3432": ["possess"],
    "U+3433": ["with the help of"],
    "U+3434": ["and"],
    "U+3435": ["small crosson earth line"],
    "U+3436": ["have to"],
    "U+3437": ["belongs to"],
    "U+3438": ["cross"],
    "U+3439": ["across"],
    "U+343a": ["multiplication"],
    "U+343b": ["small diagonal cross below skyline"],
    "U+343c": ["choice"],
    "U+343d": ["more"],
    "U+343e": ["much"],
    "U+343f": ["war"],
    "U+3440": ["indicator plural"],
    "U+3441": ["indicator-sized cross below skyline"],
    "U+3442": ["wand"],
    "U+3443": ["indicator-sized cross on midline"],
    "U+3444": ["star"],
    "U+3445": ["muslim"],
    "U+3446": ["indicator-sized cross on earth line"],
    "U+3447": ["comet"],
    "U+3448": ["knife"],
    "U+3449": ["sharp point"],
    "U+344a": ["plough"],
    "U+344b": ["creation"],
    "U+344c": ["star of david"],
    "U+344d": ["danger"],
    "U+344e": ["pyramid"],
    "U+344f": ["small isosceles triangle on midline"],
    "U+3450": ["rocket"],
    "U+3451": ["female"],
    "U+3452": ["tooth"],
    "U+3453": ["teeth"],
    "U+3454": ["cavity"],
    "U+3455": ["large symmetric acute angle above skyline"],
    "U+3456": ["god"],
    "U+3457": ["action"],
    "U+3458": ["legs and feet"],
    "U+3459": ["hip"],
    "U+345a": ["leg"],
    "U+345b": ["heel"],
    "U+345c": ["foot"],
    "U+345d": ["kick"],
    "U+345e": ["toe"],
    "U+345f": ["roller skates"],
    "U+3460": ["ice skates"],
    "U+3461": ["evaluation"],
    "U+3462": ["small symmetric acute angle on midline"],
    "U+3463": ["work"],
    "U+3464": ["action or male"],
    "U+3465": ["gender"],
    "U+3466": ["insect"],
    "U+3467": ["indicator action"],
    "U+3468": ["indicator active"],
    "U+3469": ["indicator description"],
    "U+346a": ["indicator description after the fact"],
    "U+346b": ["indicator past passive"],
    "U+346c": ["indicator future passive"],
    "U+346d": ["indicator passive"],
    "U+346e": ["indicator passive conditional"],
    "U+346f": ["indicator past passive conditional"],
    "U+3470": ["indicator future passive conditional"],
    "U+3471": ["up-pointing left half of right triangle"],
    "U+3472": ["electricity"],
    "U+3473": ["pointing"],
    "U+3474": ["hand"],
    "U+3475": ["thumb"],
    "U+3476": ["finger"],
    "U+3477": ["tool"],
    "U+3478": ["barb pointing up"],
    "U+3479": ["opposite"],
    "U+347a": ["nose"],
    "U+347b": ["odour"],
    "U+347c": ["extended horizontal line on earth line"],
    "U+347d": ["road"],
    "U+347e": ["long horizontal line on midline"],
    "U+347f": ["bus"],
    "U+3480": ["long horizontal line on earth line"],
    "U+3481": ["worm"],
    "U+3482": ["sky"],
    "U+3483": ["fog"],
    "U+3484": ["environment"],
    "U+3485": ["peace"],
    "U+3486": ["disturbance"],
    "U+3487": ["world"],
    "U+3488": ["blissymbol"],
    "U+3489": ["lightning"],
    "U+348a": ["air"],
    "U+348b": ["wind"],
    "U+348c": ["subtraction"],
    "U+348d": ["vehicle"],
    "U+348e": ["automobile"],
    "U+348f": ["steering wheel"],
    "U+3490": ["fill"],
    "U+3491": ["sailboat"],
    "U+3492": ["under"],
    "U+3493": ["weight"],
    "U+3494": ["animal"],
    "U+3495": ["paw"],
    "U+3496": ["water animal"],
    "U+3497": ["hippopotamus"],
    "U+3498": ["cervine animal"],
    "U+3499": ["bovine animal"],
    "U+349a": ["horn or antler"],
    "U+349b": ["feline animal"],
    "U+349c": ["claw"],
    "U+349d": ["giraffe"],
    "U+349e": ["horse"],
    "U+349f": ["rhinoceros"],
    "U+34a0": ["horn"],
    "U+34a1": ["hanger"],
    "U+34a2": ["ground"],
    "U+34a3": ["place"],
    "U+34a4": ["vegetable below ground"],
    "U+34a5": ["bulb"],
    "U+34a6": ["onion"],
    "U+34a7": ["roots"],
    "U+34a8": ["seed"],
    "U+34a9": ["carrot"],
    "U+34aa": ["grave"],
    "U+34ab": ["snail"],
    "U+34ac": ["lawn"],
    "U+34ad": ["night"],
    "U+34ae": ["evening"],
    "U+34af": ["shore"],
    "U+34b0": ["street"],
    "U+34b1": ["ski"],
    "U+34b2": ["skateboard"],
    "U+34b3": ["short horizontal line on sky line"],
    "U+34b4": ["adult"],
    "U+34b5": ["teenager"],
    "U+34b6": ["eyebrow"],
    "U+34b7": ["large"],
    "U+34b8": ["temperature"],
    "U+34b9": ["most"],
    "U+34ba": ["high"],
    "U+34bb": ["nail"],
    "U+34bc": ["shovel"],
    "U+34bd": ["dig"],
    "U+34be": ["short horizontal line below skyline"],
    "U+34bf": ["same"],
    "U+34c0": ["different"],
    "U+34c1": ["not"],
    "U+34c2": ["nowhere"],
    "U+34c3": ["low"],
    "U+34c4": ["pin"],
    "U+34c5": ["small"],
    "U+34c6": ["love"],
    "U+34c7": ["but"],
    "U+34c8": ["break"],
    "U+34c9": ["short horizontal line on earth line"],
    "U+34ca": ["on"],
    "U+34cb": ["bridge"],
    "U+34cc": ["hole"],
    "U+34cd": ["indicator-sized horizontal line"],
    "U+34ce": ["maple leaf"],
    "U+34cf": ["line"],
    "U+34d0": ["screw"],
    "U+34d1": ["after"],
    "U+34d2": ["between"],
    "U+34d3": ["attach"],
    "U+34d4": ["parallel"],
    "U+34d5": ["other"],
    "U+34d6": ["copy"],
    "U+34d7": ["thin"],
    "U+34d8": ["limits"],
    "U+34d9": ["deep"],
    "U+34da": ["thick"],
    "U+34db": ["wide"],
    "U+34dc": ["broom"],
    "U+34dd": ["perpendicular"],
    "U+34de": ["beginning"],
    "U+34df": ["interval"],
    "U+34e0": ["month"],
    "U+34e1": ["needle"],
    "U+34e2": ["high three-quarter length vertical line"],
    "U+34e3": ["account"],
    "U+34e4": ["low three-quarter length vertical line"],
    "U+34e5": ["commandments"],
    "U+34e6": ["small vertical line below skyline"],
    "U+34e7": ["chair"],
    "U+34e8": ["toilet"],
    "U+34e9": ["wheelchair"],
    "U+34ea": ["armchair"],
    "U+34eb": ["bed"],
    "U+34ec": ["pillow"],
    "U+34ed": ["bottle"],
    "U+34ee": ["woman"],
    "U+34ef": ["lesbian couple"],
    "U+34f0": ["first person feminine"],
    "U+34f1": ["second person feminine"],
    "U+34f2": ["third person feminine"],
    "U+34f3": ["cohabiting lesbian couple"],
    "U+34f4": ["man"],
    "U+34f5": ["first person masculine"],
    "U+34f6": ["second person masculine"],
    "U+34f7": ["third person masculine"],
    "U+34f8": ["citizen"],
    "U+34f9": ["husband"],
    "U+34fa": ["cohabiting heterosexual couple"],
    "U+34fb": ["cohabiting homosexual couple"],
    "U+34fc": ["stepfather"],
    "U+34fd": ["married family"],
    "U+34fe": ["heterosexual couple"],
    "U+34ff": ["homosexual couple"],
    "U+3500": ["boat"],
    "U+3501": ["sack"],
    "U+3502": ["crab"],
    "U+3503": ["person kneeling"],
    "U+3504": ["ankle"],
    "U+3505": ["knee"],
    "U+3506": ["menorah"],
    "U+3507": ["small verticalline on midline"],
    "U+3508": ["near"],
    "U+3509": ["at a distance"],
    "U+350a": ["far"],
    "U+350b": ["from"],
    "U+350c": ["cancontainer"],
    "U+350d": ["length"],
    "U+350e": ["measurement"],
    "U+350f": ["injection"],
    "U+3510": ["hypodermic needle"],
    "U+3511": ["short"],
    "U+3512": ["pepper"],
    "U+3513": ["it"],
    "U+3514": ["until"],
    "U+3515": ["flag"],
    "U+3516": ["country"],
    "U+3517": ["sail"],
    "U+3518": ["crown"],
    "U+3519": ["shallow"],
    "U+351a": ["fight"],
    "U+351b": ["soft"],
    "U+351c": ["indicator-sized vertical line on skyline"],
    "U+351d": ["etrog"],
    "U+351e": ["megillah"],
    "U+351f": ["torah"],
    "U+3520": ["ladder"],
    "U+3521": ["indicator-sized verticalline on midline"],
    "U+3522": ["spinning top"],
    "U+3523": ["diagonal of verticalrectangle"],
    "U+3524": ["help"],
    "U+3525": ["reversed diagonal of vertical rectangle"],
    "U+3526": ["sport stick"],
    "U+3527": ["hockey stick"],
    "U+3528": ["golfclub"],
    "U+3529": ["short reversed diagonal of vertical rectangle"],
    "U+352a": ["bucket"],
    "U+352b": ["diagonal of horizontal rectangle"],
    "U+352c": ["helicopter"],
    "U+352d": ["seesaw"],
    "U+352e": ["reversed diagonal of horizontal rectangle"],
    "U+352f": ["electromagnetic radiation"],
    "U+3530": ["energy"],
    "U+3531": ["fuel"],
    "U+3532": ["microwave oven"],
    "U+3533": ["power"],
    "U+3534": ["extended diagonal of square"],
    "U+3535": ["saw"],
    "U+3536": ["diagonal of square on skyline"],
    "U+3537": ["tank"],
    "U+3538": ["destroy"],
    "U+3539": ["angle"],
    "U+353a": ["cannon"],
    "U+353b": ["chemical product"],
    "U+353c": ["three-quarter sized diagonal of square"],
    "U+353d": ["smalldiagonal of square"],
    "U+353e": ["fork"],
    "U+353f": ["hammer"],
    "U+3540": ["the"],
    "U+3541": ["this"],
    "U+3542": ["small diagonal of square above earthline"],
    "U+3543": ["spoon"],
    "U+3544": ["racquet"],
    "U+3545": ["pen"],
    "U+3546": ["reversed smalldiagonal of square"],
    "U+3547": ["couch"],
    "U+3548": ["pitcher"],
    "U+3549": ["wagon"],
    "U+354a": ["hedgehog"],
    "U+354b": ["quill"],
    "U+354c": ["a or any"],
    "U+354d": ["somewhere"],
    "U+354e": ["reversed small diagonal of square above earthline"],
    "U+354f": ["soup"],
    "U+3550": ["salad"],
    "U+3551": ["dish"],
    "U+3552": ["cereal"],
    "U+3553": ["apostrophe on midline"],
    "U+3554": ["relativizer"],
    "U+3555": ["what"],
    "U+3556": ["where"],
    "U+3557": ["command"],
    "U+3558": ["full stop"],
    "U+3559": ["comma"],
    "U+355a": ["colon"],
    "U+355b": ["semicolon"],
    "U+355c": ["question mark"],
    "U+355d": ["exclamation mark"],
    "U+355e": ["alphabet"],
    "U+355f": ["zero"],
    "U+3560": ["one"],
    "U+3561": ["self"],
    "U+3562": ["two"],
    "U+3563": ["three"],
    "U+3564": ["four"],
    "U+3565": ["five"],
    "U+3566": ["six"],
    "U+3567": ["seven"],
    "U+3568": ["eight"],
    "U+3569": ["nine"],
    "U+356a": ["percent sign"],
    "U+356b": ["cent sign"],
    "U+356c": ["dollar sign"],
    "U+356d": ["pound sign"],
    "U+356e": ["yen sign"],
    "U+356f": ["euro sign"],
    "U+3570": ["indicator conditional"],
    "U+3571": ["indicator past conditional"],
    "U+3572": ["indicator future conditional"],
    "U+3573": ["space (whitespace)"],
    "U+3574": ["half space"],
    "U+3575": ["quarter space"],
    "U+3576": ["difficult"],
}

#bn = blissnet.BLISSNET

#for uni in bn:
#    synsets = bn[uni]


BLISS_TO_UNICODE["ATB"] = ["U+3577"]
UNICODE_TO_BLISS["U+3577"] = ["ATB"]
BLISS_TO_UNICODE["all terrain bike"] = ["U+3577"]
UNICODE_TO_BLISS["U+3577"].append("all terrain bike")
BLISS_TO_UNICODE["ATB,all-terrain bike"] = ["U+3577"]
UNICODE_TO_BLISS["U+3577"].append("ATB,all-terrain bike")
BLISS_TO_UNICODE["bicycle"] = ["U+3578"]
UNICODE_TO_BLISS["U+3578"] = ["bicycle"]
BLISS_TO_UNICODE["yellow"] = ["U+3579"]
UNICODE_TO_BLISS["U+3579"] = ["yellow"]
BLISS_TO_UNICODE["3"] = ["U+357a"]
UNICODE_TO_BLISS["U+357a"] = ["3"]
BLISS_TO_UNICODE["4"] = ["U+3564"]
UNICODE_TO_BLISS["U+3564"].append("4")
BLISS_TO_UNICODE["Arabic numeral 4"] = ["U+357b"]
UNICODE_TO_BLISS["U+357b"] = ["Arabic numeral 4"]
BLISS_TO_UNICODE["Arabic numeral 4 small"] = ["U+357c"]
UNICODE_TO_BLISS["U+357c"] = ["Arabic numeral 4 small"]
BLISS_TO_UNICODE["forest"] = ["U+357d"]
UNICODE_TO_BLISS["U+357d"] = ["forest"]
BLISS_TO_UNICODE["bush"] = ["U+357d"]
UNICODE_TO_BLISS["U+357d"].append("bush")
BLISS_TO_UNICODE["wood"] = ["U+357d"]
UNICODE_TO_BLISS["U+357d"].append("wood")
BLISS_TO_UNICODE["woods"] = ["U+357d"]
UNICODE_TO_BLISS["U+357d"].append("woods")
BLISS_TO_UNICODE["forest,bush,wood,woods"] = ["U+357d"]
UNICODE_TO_BLISS["U+357d"].append("forest,bush,wood,woods")
BLISS_TO_UNICODE["many"] = ["U+357e"]
UNICODE_TO_BLISS["U+357e"] = ["many"]
BLISS_TO_UNICODE["trees"] = ["U+357f"]
UNICODE_TO_BLISS["U+357f"] = ["trees"]
BLISS_TO_UNICODE["Olympics"] = ["U+3580"]
UNICODE_TO_BLISS["U+3580"] = ["Olympics"]
BLISS_TO_UNICODE["Olympic games"] = ["U+3580"]
UNICODE_TO_BLISS["U+3580"].append("Olympic games")
BLISS_TO_UNICODE["Olympics,Olympic games"] = ["U+3580"]
UNICODE_TO_BLISS["U+3580"].append("Olympics,Olympic games")
BLISS_TO_UNICODE["competition"] = ["U+3581"]
UNICODE_TO_BLISS["U+3581"] = ["competition"]
BLISS_TO_UNICODE["5"] = ["U+3582"]
UNICODE_TO_BLISS["U+3582"] = ["5"]
BLISS_TO_UNICODE["garbage can"] = ["U+3583"]
UNICODE_TO_BLISS["U+3583"] = ["garbage can"]
BLISS_TO_UNICODE["rubbish bin"] = ["U+3583"]
UNICODE_TO_BLISS["U+3583"].append("rubbish bin")
BLISS_TO_UNICODE["trash can"] = ["U+3583"]
UNICODE_TO_BLISS["U+3583"].append("trash can")
BLISS_TO_UNICODE["garbage can,rubbish bin,trash can"] = ["U+3583"]
UNICODE_TO_BLISS["U+3583"].append("garbage can,rubbish bin,trash can")
BLISS_TO_UNICODE["conjure"] = ["U+3584"]
UNICODE_TO_BLISS["U+3584"] = ["conjure"]
BLISS_TO_UNICODE["turn to"] = ["U+3584"]
UNICODE_TO_BLISS["U+3584"].append("turn to")
BLISS_TO_UNICODE["transform"] = ["U+3584"]
UNICODE_TO_BLISS["U+3584"].append("transform")
BLISS_TO_UNICODE["conjure,turn to,transform"] = ["U+3584"]
UNICODE_TO_BLISS["U+3584"].append("conjure,turn to,transform")
BLISS_TO_UNICODE["short message system"] = ["U+3585"]
UNICODE_TO_BLISS["U+3585"] = ["short message system"]
BLISS_TO_UNICODE["text message"] = ["U+3585"]
UNICODE_TO_BLISS["U+3585"].append("text message")
BLISS_TO_UNICODE["letter"] = ["U+3586"]
UNICODE_TO_BLISS["U+3586"] = ["letter"]
BLISS_TO_UNICODE["telephone"] = ["U+3587"]
UNICODE_TO_BLISS["U+3587"] = ["telephone"]
BLISS_TO_UNICODE["pictograph"] = ["U+3588"]
UNICODE_TO_BLISS["U+3588"] = ["pictograph"]
BLISS_TO_UNICODE["sexual abuse"] = ["U+3589"]
UNICODE_TO_BLISS["U+3589"] = ["sexual abuse"]
BLISS_TO_UNICODE["sexual assault"] = ["U+3589"]
UNICODE_TO_BLISS["U+3589"].append("sexual assault")
BLISS_TO_UNICODE["sexual violence"] = ["U+3589"]
UNICODE_TO_BLISS["U+3589"].append("sexual violence")
BLISS_TO_UNICODE["sexual abuse,sexual assault,sexual violence"] = ["U+3589"]
UNICODE_TO_BLISS["U+3589"].append("sexual abuse,sexual assault,sexual violence")
BLISS_TO_UNICODE["abuse"] = ["U+358a"]
UNICODE_TO_BLISS["U+358a"] = ["abuse"]
BLISS_TO_UNICODE["assault"] = ["U+358b"]
UNICODE_TO_BLISS["U+358b"] = ["assault"]
BLISS_TO_UNICODE["violence"] = ["U+358c"]
UNICODE_TO_BLISS["U+358c"] = ["violence"]
BLISS_TO_UNICODE["sexual"] = ["U+358d"]
UNICODE_TO_BLISS["U+358d"] = ["sexual"]
BLISS_TO_UNICODE["taco"] = ["U+358e"]
UNICODE_TO_BLISS["U+358e"] = ["taco"]
BLISS_TO_UNICODE["taco shell"] = ["U+358e"]
UNICODE_TO_BLISS["U+358e"].append("taco shell")
BLISS_TO_UNICODE["taco,taco shell"] = ["U+358e"]
UNICODE_TO_BLISS["U+358e"].append("taco,taco shell")
BLISS_TO_UNICODE["shell"] = ["U+358f"]
UNICODE_TO_BLISS["U+358f"] = ["shell"]
BLISS_TO_UNICODE["wake up"] = ["U+3590"]
UNICODE_TO_BLISS["U+3590"] = ["wake up"]
BLISS_TO_UNICODE["to go"] = ["U+3591"]
UNICODE_TO_BLISS["U+3591"] = ["to go"]
BLISS_TO_UNICODE["Euro"] = ["U+3592"]
UNICODE_TO_BLISS["U+3592"] = ["Euro"]
BLISS_TO_UNICODE["international symbol for Euro"] = ["U+3593"]
UNICODE_TO_BLISS["U+3593"] = ["international symbol for Euro"]
BLISS_TO_UNICODE["water flower"] = ["U+3594"]
UNICODE_TO_BLISS["U+3594"] = ["water flower"]
BLISS_TO_UNICODE["water lily"] = ["U+3594"]
UNICODE_TO_BLISS["U+3594"].append("water lily")
BLISS_TO_UNICODE["water flower,water lily"] = ["U+3594"]
UNICODE_TO_BLISS["U+3594"].append("water flower,water lily")
BLISS_TO_UNICODE["coat"] = ["U+3361"]
UNICODE_TO_BLISS["U+3361"].append("coat")
BLISS_TO_UNICODE["hair"].append("U+3361")
UNICODE_TO_BLISS["U+3361"].append("hair")
BLISS_TO_UNICODE["fur,coat"] = ["U+3361"]
UNICODE_TO_BLISS["U+3361"].append("fur,coat")
BLISS_TO_UNICODE["prize"] = ["U+3595"]
UNICODE_TO_BLISS["U+3595"] = ["prize"]
BLISS_TO_UNICODE["award"] = ["U+3595"]
UNICODE_TO_BLISS["U+3595"].append("award")
BLISS_TO_UNICODE["trophy"] = ["U+3595"]
UNICODE_TO_BLISS["U+3595"].append("trophy")
BLISS_TO_UNICODE["prize,award,trophy"] = ["U+3595"]
UNICODE_TO_BLISS["U+3595"].append("prize,award,trophy")
BLISS_TO_UNICODE["win"] = ["U+3596"]
UNICODE_TO_BLISS["U+3596"] = ["win"]
BLISS_TO_UNICODE["car racing"] = ["U+3597"]
UNICODE_TO_BLISS["U+3597"] = ["car racing"]
BLISS_TO_UNICODE["auto racing"] = ["U+3597"]
UNICODE_TO_BLISS["U+3597"].append("auto racing")
BLISS_TO_UNICODE["car racing,auto racing"] = ["U+3597"]
UNICODE_TO_BLISS["U+3597"].append("car racing,auto racing")
BLISS_TO_UNICODE["sport"] = ["U+3598"]
UNICODE_TO_BLISS["U+3598"] = ["sport"]
BLISS_TO_UNICODE["car"] = ["U+3599"]
UNICODE_TO_BLISS["U+3599"] = ["car"]
BLISS_TO_UNICODE["rent"] = ["U+359a"]
UNICODE_TO_BLISS["U+359a"] = ["rent"]
BLISS_TO_UNICODE["lease"] = ["U+359a"]
UNICODE_TO_BLISS["U+359a"].append("lease")
BLISS_TO_UNICODE["hire"] = ["U+359a"]
UNICODE_TO_BLISS["U+359a"].append("hire")
BLISS_TO_UNICODE["charter"] = ["U+359a"]
UNICODE_TO_BLISS["U+359a"].append("charter")
BLISS_TO_UNICODE["rent,lease,hire,charter"] = ["U+359a"]
UNICODE_TO_BLISS["U+359a"].append("rent,lease,hire,charter")
BLISS_TO_UNICODE["limited time"] = ["U+359b"]
UNICODE_TO_BLISS["U+359b"] = ["limited time"]
BLISS_TO_UNICODE["bus driver"] = ["U+359c"]
UNICODE_TO_BLISS["U+359c"] = ["bus driver"]
BLISS_TO_UNICODE["tired"] = ["U+359d"]
UNICODE_TO_BLISS["U+359d"] = ["tired"]
BLISS_TO_UNICODE["exhausted"] = ["U+359d"]
UNICODE_TO_BLISS["U+359d"].append("exhausted")
BLISS_TO_UNICODE["weary"] = ["U+359d"]
UNICODE_TO_BLISS["U+359d"].append("weary")
BLISS_TO_UNICODE["tired,exhausted,weary"] = ["U+359d"]
UNICODE_TO_BLISS["U+359d"].append("tired,exhausted,weary")
BLISS_TO_UNICODE["rest"] = ["U+359e"]
UNICODE_TO_BLISS["U+359e"] = ["rest"]
BLISS_TO_UNICODE["to need"] = ["U+359f"]
UNICODE_TO_BLISS["U+359f"] = ["to need"]
BLISS_TO_UNICODE["bacon"] = ["U+35a0"]
UNICODE_TO_BLISS["U+35a0"] = ["bacon"]
BLISS_TO_UNICODE["pork"] = ["U+35a1"]
UNICODE_TO_BLISS["U+35a1"] = ["pork"]
BLISS_TO_UNICODE["linear thing"] = ["U+35a2"]
UNICODE_TO_BLISS["U+35a2"] = ["linear thing"]
BLISS_TO_UNICODE["second"] = ["U+35a3"]
UNICODE_TO_BLISS["U+35a3"] = ["second"]
BLISS_TO_UNICODE["two apostrophes"] = ["U+35a4"]
UNICODE_TO_BLISS["U+35a4"] = ["two apostrophes"]
BLISS_TO_UNICODE[" used in astronomy to indicate a second"] = ["U+35a5"]
UNICODE_TO_BLISS["U+35a5"] = [" used in astronomy to indicate a second"]
BLISS_TO_UNICODE["2"] = ["U+35a6"]
UNICODE_TO_BLISS["U+35a6"] = ["2"]
BLISS_TO_UNICODE["decimal point"] = ["U+35a7"]
UNICODE_TO_BLISS["U+35a7"] = ["decimal point"]
BLISS_TO_UNICODE["satellite dish"] = ["U+35a8"]
UNICODE_TO_BLISS["U+35a8"] = ["satellite dish"]
BLISS_TO_UNICODE["signal receiver"] = ["U+35a9"]
UNICODE_TO_BLISS["U+35a9"] = ["signal receiver"]
BLISS_TO_UNICODE["communication satellite"] = ["U+35aa"]
UNICODE_TO_BLISS["U+35aa"] = ["communication satellite"]
BLISS_TO_UNICODE["oneself"] = ["U+3561"]
UNICODE_TO_BLISS["U+3561"].append("oneself")
BLISS_TO_UNICODE["ego"] = ["U+3561"]
UNICODE_TO_BLISS["U+3561"].append("ego")
BLISS_TO_UNICODE["self,oneself,ego"] = ["U+3561"]
UNICODE_TO_BLISS["U+3561"].append("self,oneself,ego")
BLISS_TO_UNICODE["1"] = ["U+35ab"]
UNICODE_TO_BLISS["U+35ab"] = ["1"]
BLISS_TO_UNICODE["infertile"] = ["U+35ac"]
UNICODE_TO_BLISS["U+35ac"] = ["infertile"]
BLISS_TO_UNICODE["sterile"] = ["U+35ac"]
UNICODE_TO_BLISS["U+35ac"].append("sterile")
BLISS_TO_UNICODE["infertile,sterile"] = ["U+35ac"]
UNICODE_TO_BLISS["U+35ac"].append("infertile,sterile")
BLISS_TO_UNICODE["without"] = ["U+35ad"]
UNICODE_TO_BLISS["U+35ad"] = ["without"]
BLISS_TO_UNICODE["tuft of grass"] = ["U+35ae"]
UNICODE_TO_BLISS["U+35ae"] = ["tuft of grass"]
BLISS_TO_UNICODE["tussock"] = ["U+35ae"]
UNICODE_TO_BLISS["U+35ae"].append("tussock")
BLISS_TO_UNICODE["tuft of grass,tussock"] = ["U+35ae"]
UNICODE_TO_BLISS["U+35ae"].append("tuft of grass,tussock")
BLISS_TO_UNICODE["collection"] = ["U+35af"]
UNICODE_TO_BLISS["U+35af"] = ["collection"]
BLISS_TO_UNICODE["pile"] = ["U+35b0"]
UNICODE_TO_BLISS["U+35b0"] = ["pile"]
BLISS_TO_UNICODE["shirt"] = ["U+35b1"]
UNICODE_TO_BLISS["U+35b1"] = ["shirt"]
BLISS_TO_UNICODE["blouse"] = ["U+35b1"]
UNICODE_TO_BLISS["U+35b1"].append("blouse")
BLISS_TO_UNICODE["shirt,blouse"] = ["U+35b1"]
UNICODE_TO_BLISS["U+35b1"].append("shirt,blouse")
BLISS_TO_UNICODE["tooth fairy"] = ["U+35b2"]
UNICODE_TO_BLISS["U+35b2"] = ["tooth fairy"]
BLISS_TO_UNICODE["fairy"] = ["U+35b3"]
UNICODE_TO_BLISS["U+35b3"] = ["fairy"]
BLISS_TO_UNICODE["forgetting"] = ["U+35b4"]
UNICODE_TO_BLISS["U+35b4"] = ["forgetting"]
BLISS_TO_UNICODE["amnesia"] = ["U+35b4"]
UNICODE_TO_BLISS["U+35b4"].append("amnesia")
BLISS_TO_UNICODE["forgetting,amnesia"] = ["U+35b4"]
UNICODE_TO_BLISS["U+35b4"].append("forgetting,amnesia")
BLISS_TO_UNICODE["konowledge"] = ["U+35b5"]
UNICODE_TO_BLISS["U+35b5"] = ["konowledge"]
BLISS_TO_UNICODE["thunder"] = ["U+35b6"]
UNICODE_TO_BLISS["U+35b6"] = ["thunder"]
BLISS_TO_UNICODE["cooking"] = ["U+35b7"]
UNICODE_TO_BLISS["U+35b7"] = ["cooking"]
BLISS_TO_UNICODE["cookery"] = ["U+35b7"]
UNICODE_TO_BLISS["U+35b7"].append("cookery")
BLISS_TO_UNICODE["preparation"] = ["U+35b7"]
UNICODE_TO_BLISS["U+35b7"].append("preparation")
BLISS_TO_UNICODE["cooking,cookery,preparation"] = ["U+35b7"]
UNICODE_TO_BLISS["U+35b7"].append("cooking,cookery,preparation")
BLISS_TO_UNICODE["to make"] = ["U+35b8"]
UNICODE_TO_BLISS["U+35b8"] = ["to make"]
BLISS_TO_UNICODE["set square"] = ["U+35b9"]
UNICODE_TO_BLISS["U+35b9"] = ["set square"]
BLISS_TO_UNICODE["hero"] = ["U+35ba"]
UNICODE_TO_BLISS["U+35ba"] = ["hero"]
BLISS_TO_UNICODE["heroic"] = ["U+35bb"]
UNICODE_TO_BLISS["U+35bb"] = ["heroic"]
BLISS_TO_UNICODE["herb"] = ["U+35bc"]
UNICODE_TO_BLISS["U+35bc"] = ["herb"]
BLISS_TO_UNICODE["spice plant"] = ["U+35bc"]
UNICODE_TO_BLISS["U+35bc"].append("spice plant")
BLISS_TO_UNICODE["herb,spice plant"] = ["U+35bc"]
UNICODE_TO_BLISS["U+35bc"].append("herb,spice plant")
BLISS_TO_UNICODE["smash"] = ["U+35bd"]
UNICODE_TO_BLISS["U+35bd"] = ["smash"]
BLISS_TO_UNICODE["grind"] = ["U+35bd"]
UNICODE_TO_BLISS["U+35bd"].append("grind")
BLISS_TO_UNICODE["shatter"] = ["U+35bd"]
UNICODE_TO_BLISS["U+35bd"].append("shatter")
BLISS_TO_UNICODE["splinter"] = ["U+35bd"]
UNICODE_TO_BLISS["U+35bd"].append("splinter")
BLISS_TO_UNICODE["smash,grind,shatter,splinter"] = ["U+35bd"]
UNICODE_TO_BLISS["U+35bd"].append("smash,grind,shatter,splinter")
BLISS_TO_UNICODE["to break"] = ["U+35be"]
UNICODE_TO_BLISS["U+35be"] = ["to break"]
BLISS_TO_UNICODE["piece"] = ["U+35bf"]
UNICODE_TO_BLISS["U+35bf"] = ["piece"]
BLISS_TO_UNICODE["two dots"] = ["U+35c0"]
UNICODE_TO_BLISS["U+35c0"] = ["two dots"]
BLISS_TO_UNICODE["carriage"] = ["U+3380"]
UNICODE_TO_BLISS["U+3380"].append("carriage")
BLISS_TO_UNICODE["cart,carriage"] = ["U+3380"]
UNICODE_TO_BLISS["U+3380"].append("cart,carriage")
BLISS_TO_UNICODE["cart"].append("U+3549")
UNICODE_TO_BLISS["U+3549"].append("cart")
BLISS_TO_UNICODE["truck"] = ["U+3549"]
UNICODE_TO_BLISS["U+3549"].append("truck")
BLISS_TO_UNICODE["wagon,cart,truck"] = ["U+3549"]
UNICODE_TO_BLISS["U+3549"].append("wagon,cart,truck")
BLISS_TO_UNICODE["diagonal line"] = ["U+35c1"]
UNICODE_TO_BLISS["U+35c1"] = ["diagonal line"]
BLISS_TO_UNICODE[" representing a handle"] = ["U+35c2"]
UNICODE_TO_BLISS["U+35c2"] = [" representing a handle"]
BLISS_TO_UNICODE["her"] = ["U+35c3"]
UNICODE_TO_BLISS["U+35c3"] = ["her"]
BLISS_TO_UNICODE["hers"] = ["U+35c3"]
UNICODE_TO_BLISS["U+35c3"].append("hers")
BLISS_TO_UNICODE["her,hers"] = ["U+35c3"]
UNICODE_TO_BLISS["U+35c3"].append("her,hers")
BLISS_TO_UNICODE["she"] = ["U+35c4"]
UNICODE_TO_BLISS["U+35c4"] = ["she"]
BLISS_TO_UNICODE["his"] = ["U+35c5"]
UNICODE_TO_BLISS["U+35c5"] = ["his"]
BLISS_TO_UNICODE["her"].append("U+35c5")
UNICODE_TO_BLISS["U+35c5"].append("her")
BLISS_TO_UNICODE["hers"].append("U+35c5")
UNICODE_TO_BLISS["U+35c5"].append("hers")
BLISS_TO_UNICODE["one's"] = ["U+35c5"]
UNICODE_TO_BLISS["U+35c5"].append("one's")
BLISS_TO_UNICODE["his,her,hers,one's"] = ["U+35c5"]
UNICODE_TO_BLISS["U+35c5"].append("his,her,hers,one's")
BLISS_TO_UNICODE["he"] = ["U+35c6"]
UNICODE_TO_BLISS["U+35c6"] = ["he"]
BLISS_TO_UNICODE["pancreas"] = ["U+35c7"]
UNICODE_TO_BLISS["U+35c7"] = ["pancreas"]
BLISS_TO_UNICODE["gland"] = ["U+35c8"]
UNICODE_TO_BLISS["U+35c8"] = ["gland"]
BLISS_TO_UNICODE["insulin"] = ["U+35c9"]
UNICODE_TO_BLISS["U+35c9"] = ["insulin"]
BLISS_TO_UNICODE["substance"] = ["U+35ca"]
UNICODE_TO_BLISS["U+35ca"] = ["substance"]
BLISS_TO_UNICODE["material"] = ["U+35cb"]
UNICODE_TO_BLISS["U+35cb"] = ["material"]
BLISS_TO_UNICODE["low tide"] = ["U+35cc"]
UNICODE_TO_BLISS["U+35cc"] = ["low tide"]
BLISS_TO_UNICODE["ebb"] = ["U+35cc"]
UNICODE_TO_BLISS["U+35cc"].append("ebb")
BLISS_TO_UNICODE["low tide,ebb"] = ["U+35cc"]
UNICODE_TO_BLISS["U+35cc"].append("low tide,ebb")
BLISS_TO_UNICODE["tide"] = ["U+35cd"]
UNICODE_TO_BLISS["U+35cd"] = ["tide"]
BLISS_TO_UNICODE["physiotherapy room"] = ["U+35ce"]
UNICODE_TO_BLISS["U+35ce"] = ["physiotherapy room"]
BLISS_TO_UNICODE["physiotherapy"] = ["U+35cf"]
UNICODE_TO_BLISS["U+35cf"] = ["physiotherapy"]
BLISS_TO_UNICODE["neurologist"] = ["U+35d0"]
UNICODE_TO_BLISS["U+35d0"] = ["neurologist"]
BLISS_TO_UNICODE["doctor"] = ["U+35d1"]
UNICODE_TO_BLISS["U+35d1"] = ["doctor"]
BLISS_TO_UNICODE["central nervous system"] = ["U+35d2"]
UNICODE_TO_BLISS["U+35d2"] = ["central nervous system"]
BLISS_TO_UNICODE["military"] = ["U+35d3"]
UNICODE_TO_BLISS["U+35d3"] = ["military"]
BLISS_TO_UNICODE["armed forces"] = ["U+35d3"]
UNICODE_TO_BLISS["U+35d3"].append("armed forces")
BLISS_TO_UNICODE["armed services"] = ["U+35d3"]
UNICODE_TO_BLISS["U+35d3"].append("armed services")
BLISS_TO_UNICODE["military,armed forces,armed services"] = ["U+35d3"]
UNICODE_TO_BLISS["U+35d3"].append("military,armed forces,armed services")
BLISS_TO_UNICODE["group"] = ["U+35d4"]
UNICODE_TO_BLISS["U+35d4"] = ["group"]
BLISS_TO_UNICODE["deletion"] = ["U+35d5"]
UNICODE_TO_BLISS["U+35d5"] = ["deletion"]
BLISS_TO_UNICODE["cancellation"] = ["U+35d5"]
UNICODE_TO_BLISS["U+35d5"].append("cancellation")
BLISS_TO_UNICODE["destruction"] = ["U+35d5"]
UNICODE_TO_BLISS["U+35d5"].append("destruction")
BLISS_TO_UNICODE["deletion,cancellation,destruction"] = ["U+35d5"]
UNICODE_TO_BLISS["U+35d5"].append("deletion,cancellation,destruction")
BLISS_TO_UNICODE["diagonal line used to cross out something"] = ["U+35d6"]
UNICODE_TO_BLISS["U+35d6"] = ["diagonal line used to cross out something"]
BLISS_TO_UNICODE["roadrunner"] = ["U+35d7"]
UNICODE_TO_BLISS["U+35d7"] = ["roadrunner"]
BLISS_TO_UNICODE["to walk"] = ["U+35d8"]
UNICODE_TO_BLISS["U+35d8"] = ["to walk"]
BLISS_TO_UNICODE["little"] = ["U+35d9"]
UNICODE_TO_BLISS["U+35d9"] = ["little"]
BLISS_TO_UNICODE["divide"] = ["U+35da"]
UNICODE_TO_BLISS["U+35da"] = ["divide"]
BLISS_TO_UNICODE["stern"] = ["U+35db"]
UNICODE_TO_BLISS["U+35db"] = ["stern"]
BLISS_TO_UNICODE["oil lamp"] = ["U+35dc"]
UNICODE_TO_BLISS["U+35dc"] = ["oil lamp"]
BLISS_TO_UNICODE["lamp"] = ["U+35dd"]
UNICODE_TO_BLISS["U+35dd"] = ["lamp"]
BLISS_TO_UNICODE["tree trunk"] = ["U+3320"]
UNICODE_TO_BLISS["U+3320"].append("tree trunk")
BLISS_TO_UNICODE["bole"] = ["U+3320"]
UNICODE_TO_BLISS["U+3320"].append("bole")
BLISS_TO_UNICODE["trunk,tree trunk,bole"] = ["U+3320"]
UNICODE_TO_BLISS["U+3320"].append("trunk,tree trunk,bole")
BLISS_TO_UNICODE["cheating"] = ["U+35de"]
UNICODE_TO_BLISS["U+35de"] = ["cheating"]
BLISS_TO_UNICODE["activity"] = ["U+35df"]
UNICODE_TO_BLISS["U+35df"] = ["activity"]
BLISS_TO_UNICODE["Sagittarius"] = ["U+35e0"]
UNICODE_TO_BLISS["U+35e0"] = ["Sagittarius"]
BLISS_TO_UNICODE["constellation of stars"] = ["U+35e1"]
UNICODE_TO_BLISS["U+35e1"] = ["constellation of stars"]
BLISS_TO_UNICODE["bow and arrow"] = ["U+35e2"]
UNICODE_TO_BLISS["U+35e2"] = ["bow and arrow"]
BLISS_TO_UNICODE["music"] = ["U+35e3"]
UNICODE_TO_BLISS["U+35e3"] = ["music"]
BLISS_TO_UNICODE["so"] = ["U+33bc"]
UNICODE_TO_BLISS["U+33bc"].append("so")
BLISS_TO_UNICODE["so that"] = ["U+33bc"]
UNICODE_TO_BLISS["U+33bc"].append("so that")
BLISS_TO_UNICODE["therefore,so,so that"] = ["U+33bc"]
UNICODE_TO_BLISS["U+33bc"].append("therefore,so,so that")
BLISS_TO_UNICODE["passport"] = ["U+35e4"]
UNICODE_TO_BLISS["U+35e4"] = ["passport"]
BLISS_TO_UNICODE["permission"] = ["U+35e5"]
UNICODE_TO_BLISS["U+35e5"] = ["permission"]
BLISS_TO_UNICODE["allowance"] = ["U+35e6"]
UNICODE_TO_BLISS["U+35e6"] = ["allowance"]
BLISS_TO_UNICODE["travel"] = ["U+35e7"]
UNICODE_TO_BLISS["U+35e7"] = ["travel"]
BLISS_TO_UNICODE["till"] = ["U+3514"]
UNICODE_TO_BLISS["U+3514"].append("till")
BLISS_TO_UNICODE["to"] = ["U+3514"]
UNICODE_TO_BLISS["U+3514"].append("to")
BLISS_TO_UNICODE["until,till,to"] = ["U+3514"]
UNICODE_TO_BLISS["U+3514"].append("until,till,to")
BLISS_TO_UNICODE["arrowhead"] = ["U+35e8"]
UNICODE_TO_BLISS["U+35e8"] = ["arrowhead"]
BLISS_TO_UNICODE["reference line"] = ["U+35e9"]
UNICODE_TO_BLISS["U+35e9"] = ["reference line"]
BLISS_TO_UNICODE["fall asleep"] = ["U+35ea"]
UNICODE_TO_BLISS["U+35ea"] = ["fall asleep"]
BLISS_TO_UNICODE["asleep"] = ["U+35eb"]
UNICODE_TO_BLISS["U+35eb"] = ["asleep"]
BLISS_TO_UNICODE["divine"] = ["U+35ec"]
UNICODE_TO_BLISS["U+35ec"] = ["divine"]
BLISS_TO_UNICODE["holy"] = ["U+35ec"]
UNICODE_TO_BLISS["U+35ec"].append("holy")
BLISS_TO_UNICODE["divine,holy"] = ["U+35ec"]
UNICODE_TO_BLISS["U+35ec"].append("divine,holy")
BLISS_TO_UNICODE["God"] = ["U+35ed"]
UNICODE_TO_BLISS["U+35ed"] = ["God"]
BLISS_TO_UNICODE["holiness"] = ["U+35ee"]
UNICODE_TO_BLISS["U+35ee"] = ["holiness"]
BLISS_TO_UNICODE["indicator descriptive"] = ["U+35ef"]
UNICODE_TO_BLISS["U+35ef"] = ["indicator descriptive"]
BLISS_TO_UNICODE["calling"] = ["U+35f0"]
UNICODE_TO_BLISS["U+35f0"] = ["calling"]
BLISS_TO_UNICODE["vocation"] = ["U+35f0"]
UNICODE_TO_BLISS["U+35f0"].append("vocation")
BLISS_TO_UNICODE["calling,vocation"] = ["U+35f0"]
UNICODE_TO_BLISS["U+35f0"].append("calling,vocation")
BLISS_TO_UNICODE["hurt"] = ["U+35f1"]
UNICODE_TO_BLISS["U+35f1"] = ["hurt"]
BLISS_TO_UNICODE["pain"] = ["U+35f1"]
UNICODE_TO_BLISS["U+35f1"].append("pain")
BLISS_TO_UNICODE["suffer"] = ["U+35f1"]
UNICODE_TO_BLISS["U+35f1"].append("suffer")
BLISS_TO_UNICODE["hurt,pain"] = ["U+35f1"]
UNICODE_TO_BLISS["U+35f1"].append("hurt,pain")
BLISS_TO_UNICODE["injure"] = ["U+35f2"]
UNICODE_TO_BLISS["U+35f2"] = ["injure"]
BLISS_TO_UNICODE["hurt"].append("U+35f2")
UNICODE_TO_BLISS["U+35f2"].append("hurt")
BLISS_TO_UNICODE["injure,hurt"] = ["U+35f2"]
UNICODE_TO_BLISS["U+35f2"].append("injure,hurt")
BLISS_TO_UNICODE["to cause"] = ["U+35f3"]
UNICODE_TO_BLISS["U+35f3"] = ["to cause"]
BLISS_TO_UNICODE["meteorologist"] = ["U+35f4"]
UNICODE_TO_BLISS["U+35f4"] = ["meteorologist"]
BLISS_TO_UNICODE["meteorology"] = ["U+35f5"]
UNICODE_TO_BLISS["U+35f5"] = ["meteorology"]
BLISS_TO_UNICODE["drinking glass"] = ["U+33b6"]
UNICODE_TO_BLISS["U+33b6"].append("drinking glass")
BLISS_TO_UNICODE["glass,drinking glass"] = ["U+33b6"]
UNICODE_TO_BLISS["U+33b6"].append("glass,drinking glass")
BLISS_TO_UNICODE["earth"] = ["U+35f6"]
UNICODE_TO_BLISS["U+35f6"] = ["earth"]
BLISS_TO_UNICODE["hold"] = ["U+35f7"]
UNICODE_TO_BLISS["U+35f7"] = ["hold"]
BLISS_TO_UNICODE["contain"] = ["U+35f7"]
UNICODE_TO_BLISS["U+35f7"].append("contain")
BLISS_TO_UNICODE["hold,contain"] = ["U+35f7"]
UNICODE_TO_BLISS["U+35f7"].append("hold,contain")
BLISS_TO_UNICODE["prepare"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"] = ["prepare"]
BLISS_TO_UNICODE["set"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"].append("set")
BLISS_TO_UNICODE["set up"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"].append("set up")
BLISS_TO_UNICODE["ready"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"].append("ready")
BLISS_TO_UNICODE["gear up"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"].append("gear up")
BLISS_TO_UNICODE["fix"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"].append("fix")
BLISS_TO_UNICODE["prepare,set,set up,ready,gear up,fix"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"].append("prepare,set,set up,ready,gear up,fix")
BLISS_TO_UNICODE["unit"] = ["U+35f9"]
UNICODE_TO_BLISS["U+35f9"] = ["unit"]
BLISS_TO_UNICODE["example"] = ["U+35f9"]
UNICODE_TO_BLISS["U+35f9"].append("example")
BLISS_TO_UNICODE["sample"] = ["U+35f9"]
UNICODE_TO_BLISS["U+35f9"].append("sample")
BLISS_TO_UNICODE["unit,example,sample"] = ["U+35f9"]
UNICODE_TO_BLISS["U+35f9"].append("unit,example,sample")
BLISS_TO_UNICODE["motorcycle racing"] = ["U+35fa"]
UNICODE_TO_BLISS["U+35fa"] = ["motorcycle racing"]
BLISS_TO_UNICODE["motor cycle"] = ["U+35fb"]
UNICODE_TO_BLISS["U+35fb"] = ["motor cycle"]
BLISS_TO_UNICODE["fast"] = ["U+35fc"]
UNICODE_TO_BLISS["U+35fc"] = ["fast"]
BLISS_TO_UNICODE["vertical line"] = ["U+35fd"]
UNICODE_TO_BLISS["U+35fd"] = ["vertical line"]
BLISS_TO_UNICODE["unfair"] = ["U+35fe"]
UNICODE_TO_BLISS["U+35fe"] = ["unfair"]
BLISS_TO_UNICODE["unjust"] = ["U+35fe"]
UNICODE_TO_BLISS["U+35fe"].append("unjust")
BLISS_TO_UNICODE["unfair,unjust"] = ["U+35fe"]
UNICODE_TO_BLISS["U+35fe"].append("unfair,unjust")
BLISS_TO_UNICODE["fair"] = ["U+35ff"]
UNICODE_TO_BLISS["U+35ff"] = ["fair"]
BLISS_TO_UNICODE["artillery"] = ["U+3600"]
UNICODE_TO_BLISS["U+3600"] = ["artillery"]
BLISS_TO_UNICODE["boat ladder"] = ["U+3601"]
UNICODE_TO_BLISS["U+3601"] = ["boat ladder"]
BLISS_TO_UNICODE["chocolate sauce"] = ["U+3602"]
UNICODE_TO_BLISS["U+3602"] = ["chocolate sauce"]
BLISS_TO_UNICODE["sauce"] = ["U+3603"]
UNICODE_TO_BLISS["U+3603"] = ["sauce"]
BLISS_TO_UNICODE["chocolate"] = ["U+3604"]
UNICODE_TO_BLISS["U+3604"] = ["chocolate"]
BLISS_TO_UNICODE["currency"] = ["U+3605"]
UNICODE_TO_BLISS["U+3605"] = ["currency"]
BLISS_TO_UNICODE["want"] = ["U+3606"]
UNICODE_TO_BLISS["U+3606"] = ["want"]
BLISS_TO_UNICODE["desire"] = ["U+3606"]
UNICODE_TO_BLISS["U+3606"].append("desire")
BLISS_TO_UNICODE["want,desire"] = ["U+3606"]
UNICODE_TO_BLISS["U+3606"].append("want,desire")
BLISS_TO_UNICODE["trip"] = ["U+3607"]
UNICODE_TO_BLISS["U+3607"] = ["trip"]
BLISS_TO_UNICODE["journey"].append("U+3607")
UNICODE_TO_BLISS["U+3607"].append("journey")
BLISS_TO_UNICODE["travel"].append("U+3607")
UNICODE_TO_BLISS["U+3607"].append("travel")
BLISS_TO_UNICODE["voyage"] = ["U+3607"]
UNICODE_TO_BLISS["U+3607"].append("voyage")
BLISS_TO_UNICODE["trip,journey,travel,voyage"] = ["U+3607"]
UNICODE_TO_BLISS["U+3607"].append("trip,journey,travel,voyage")
BLISS_TO_UNICODE["tropical rain forest"] = ["U+3608"]
UNICODE_TO_BLISS["U+3608"] = ["tropical rain forest"]
BLISS_TO_UNICODE["jungle"] = ["U+3608"]
UNICODE_TO_BLISS["U+3608"].append("jungle")
BLISS_TO_UNICODE["tropical rain forest,jungle"] = ["U+3608"]
UNICODE_TO_BLISS["U+3608"].append("tropical rain forest,jungle")
BLISS_TO_UNICODE["grove"] = ["U+3609"]
UNICODE_TO_BLISS["U+3609"] = ["grove"]
BLISS_TO_UNICODE["equator"] = ["U+360a"]
UNICODE_TO_BLISS["U+360a"] = ["equator"]
BLISS_TO_UNICODE["panpipe"] = ["U+360b"]
UNICODE_TO_BLISS["U+360b"] = ["panpipe"]
BLISS_TO_UNICODE["wood instrument"] = ["U+360c"]
UNICODE_TO_BLISS["U+360c"] = ["wood instrument"]
BLISS_TO_UNICODE["appliance"] = ["U+326d"]
UNICODE_TO_BLISS["U+326d"].append("appliance")
BLISS_TO_UNICODE["engine"] = ["U+326d"]
UNICODE_TO_BLISS["U+326d"].append("engine")
BLISS_TO_UNICODE["motor"] = ["U+326d"]
UNICODE_TO_BLISS["U+326d"].append("motor")
BLISS_TO_UNICODE["machine,appliance,engine,motor"] = ["U+326d"]
UNICODE_TO_BLISS["U+326d"].append("machine,appliance,engine,motor")
BLISS_TO_UNICODE["how"] = ["U+360d"]
UNICODE_TO_BLISS["U+360d"] = ["how"]
BLISS_TO_UNICODE["who"] = ["U+360e"]
UNICODE_TO_BLISS["U+360e"] = ["who"]
BLISS_TO_UNICODE["hot"] = ["U+360f"]
UNICODE_TO_BLISS["U+360f"] = ["hot"]
BLISS_TO_UNICODE["spicy"] = ["U+360f"]
UNICODE_TO_BLISS["U+360f"].append("spicy")
BLISS_TO_UNICODE["peppery"] = ["U+360f"]
UNICODE_TO_BLISS["U+360f"].append("peppery")
BLISS_TO_UNICODE["hot,spicy,peppery"] = ["U+360f"]
UNICODE_TO_BLISS["U+360f"].append("hot,spicy,peppery")
BLISS_TO_UNICODE["hop"] = ["U+3610"]
UNICODE_TO_BLISS["U+3610"] = ["hop"]
BLISS_TO_UNICODE["sense"] = ["U+32d4"]
UNICODE_TO_BLISS["U+32d4"].append("sense")
BLISS_TO_UNICODE["significance"] = ["U+32d4"]
UNICODE_TO_BLISS["U+32d4"].append("significance")
BLISS_TO_UNICODE["meaning,sense,significance"] = ["U+32d4"]
UNICODE_TO_BLISS["U+32d4"].append("meaning,sense,significance")
BLISS_TO_UNICODE["to think"] = ["U+3611"]
UNICODE_TO_BLISS["U+3611"] = ["to think"]
BLISS_TO_UNICODE["to say"] = ["U+3612"]
UNICODE_TO_BLISS["U+3612"] = ["to say"]
BLISS_TO_UNICODE["to write"] = ["U+3613"]
UNICODE_TO_BLISS["U+3613"] = ["to write"]
BLISS_TO_UNICODE["significance"].append("U+32e7")
UNICODE_TO_BLISS["U+32e7"].append("significance")
BLISS_TO_UNICODE["importance,significance"] = ["U+32e7"]
UNICODE_TO_BLISS["U+32e7"].append("importance,significance")
BLISS_TO_UNICODE["intensity"] = ["U+3614"]
UNICODE_TO_BLISS["U+3614"] = ["intensity"]
BLISS_TO_UNICODE["right turn"] = ["U+3615"]
UNICODE_TO_BLISS["U+3615"] = ["right turn"]
BLISS_TO_UNICODE["right"].append("U+3615")
UNICODE_TO_BLISS["U+3615"].append("right")
BLISS_TO_UNICODE["right turn,right"] = ["U+3615"]
UNICODE_TO_BLISS["U+3615"].append("right turn,right")
BLISS_TO_UNICODE["horizontal line"] = ["U+3616"]
UNICODE_TO_BLISS["U+3616"] = ["horizontal line"]
BLISS_TO_UNICODE["beauty"] = ["U+3617"]
UNICODE_TO_BLISS["U+3617"] = ["beauty"]
BLISS_TO_UNICODE["happiness"] = ["U+3618"]
UNICODE_TO_BLISS["U+3618"] = ["happiness"]
BLISS_TO_UNICODE["fun"] = ["U+3619"]
UNICODE_TO_BLISS["U+3619"] = ["fun"]
BLISS_TO_UNICODE["joy"] = ["U+361a"]
UNICODE_TO_BLISS["U+361a"] = ["joy"]
BLISS_TO_UNICODE["pleasure"] = ["U+361b"]
UNICODE_TO_BLISS["U+361b"] = ["pleasure"]
BLISS_TO_UNICODE["opossum"] = ["U+361c"]
UNICODE_TO_BLISS["U+361c"] = ["opossum"]
BLISS_TO_UNICODE["possum"] = ["U+361c"]
UNICODE_TO_BLISS["U+361c"].append("possum")
BLISS_TO_UNICODE["opossum,possum"] = ["U+361c"]
UNICODE_TO_BLISS["U+361c"].append("opossum,possum")
BLISS_TO_UNICODE["marsupial"] = ["U+361d"]
UNICODE_TO_BLISS["U+361d"] = ["marsupial"]
BLISS_TO_UNICODE["wrong"] = ["U+32e1"]
UNICODE_TO_BLISS["U+32e1"].append("wrong")
BLISS_TO_UNICODE["bad,wrong"] = ["U+32e1"]
UNICODE_TO_BLISS["U+32e1"].append("bad,wrong")
BLISS_TO_UNICODE["negative"] = ["U+361e"]
UNICODE_TO_BLISS["U+361e"] = ["negative"]
BLISS_TO_UNICODE["bad"].append("U+32c9")
UNICODE_TO_BLISS["U+32c9"].append("bad")
BLISS_TO_UNICODE["wrong"].append("U+32c9")
UNICODE_TO_BLISS["U+32c9"].append("wrong")
BLISS_TO_UNICODE["immoral,bad,wrong"] = ["U+32c9"]
UNICODE_TO_BLISS["U+32c9"].append("immoral,bad,wrong")
BLISS_TO_UNICODE["bad conscience"] = ["U+361f"]
UNICODE_TO_BLISS["U+361f"] = ["bad conscience"]
BLISS_TO_UNICODE["incorrect"] = ["U+3620"]
UNICODE_TO_BLISS["U+3620"] = ["incorrect"]
BLISS_TO_UNICODE["bad"].append("U+3620")
UNICODE_TO_BLISS["U+3620"].append("bad")
BLISS_TO_UNICODE["inaccurate"] = ["U+3620"]
UNICODE_TO_BLISS["U+3620"].append("inaccurate")
BLISS_TO_UNICODE["wrong"].append("U+3620")
UNICODE_TO_BLISS["U+3620"].append("wrong")
BLISS_TO_UNICODE["incorrect,bad,inaccurate,wrong"] = ["U+3620"]
UNICODE_TO_BLISS["U+3620"].append("incorrect,bad,inaccurate,wrong")
BLISS_TO_UNICODE["incorrect thinking"] = ["U+3621"]
UNICODE_TO_BLISS["U+3621"] = ["incorrect thinking"]
BLISS_TO_UNICODE["electric kettle"] = ["U+3622"]
UNICODE_TO_BLISS["U+3622"] = ["electric kettle"]
BLISS_TO_UNICODE["wash up"] = ["U+3623"]
UNICODE_TO_BLISS["U+3623"] = ["wash up"]
BLISS_TO_UNICODE["do the dishes"] = ["U+3623"]
UNICODE_TO_BLISS["U+3623"].append("do the dishes")
BLISS_TO_UNICODE["wash up,do the dishes"] = ["U+3623"]
UNICODE_TO_BLISS["U+3623"].append("wash up,do the dishes")
BLISS_TO_UNICODE["to wash"] = ["U+3624"]
UNICODE_TO_BLISS["U+3624"] = ["to wash"]
BLISS_TO_UNICODE["glassware"] = ["U+3625"]
UNICODE_TO_BLISS["U+3625"] = ["glassware"]
BLISS_TO_UNICODE["baggage"] = ["U+3626"]
UNICODE_TO_BLISS["U+3626"] = ["baggage"]
BLISS_TO_UNICODE["bag"] = ["U+3626"]
UNICODE_TO_BLISS["U+3626"].append("bag")
BLISS_TO_UNICODE["luggage"] = ["U+3626"]
UNICODE_TO_BLISS["U+3626"].append("luggage")
BLISS_TO_UNICODE["suitcase"].append("U+3626")
UNICODE_TO_BLISS["U+3626"].append("suitcase")
BLISS_TO_UNICODE["baggage,bag,luggage,suitcase"] = ["U+3626"]
UNICODE_TO_BLISS["U+3626"].append("baggage,bag,luggage,suitcase")
BLISS_TO_UNICODE["wing"] = ["U+3628"]
UNICODE_TO_BLISS["U+3628"] = ["wing"]
BLISS_TO_UNICODE["fart"] = ["U+3629"]
UNICODE_TO_BLISS["U+3629"] = ["fart"]
BLISS_TO_UNICODE["wind"].append("U+3629")
UNICODE_TO_BLISS["U+3629"].append("wind")
BLISS_TO_UNICODE["fart,wind"] = ["U+3629"]
UNICODE_TO_BLISS["U+3629"].append("fart,wind")
BLISS_TO_UNICODE["wrap"] = ["U+362a"]
UNICODE_TO_BLISS["U+362a"] = ["wrap"]
BLISS_TO_UNICODE["wind"].append("U+362a")
UNICODE_TO_BLISS["U+362a"].append("wind")
BLISS_TO_UNICODE["wrap,wind"] = ["U+362a"]
UNICODE_TO_BLISS["U+362a"].append("wrap,wind")
BLISS_TO_UNICODE["wine"] = ["U+362b"]
UNICODE_TO_BLISS["U+362b"] = ["wine"]
BLISS_TO_UNICODE["alcoholic drink"] = ["U+362c"]
UNICODE_TO_BLISS["U+362c"] = ["alcoholic drink"]
BLISS_TO_UNICODE["limit"] = ["U+362d"]
UNICODE_TO_BLISS["U+362d"] = ["limit"]
BLISS_TO_UNICODE["limitation"] = ["U+362d"]
UNICODE_TO_BLISS["U+362d"].append("limitation")
BLISS_TO_UNICODE["restriction"] = ["U+362d"]
UNICODE_TO_BLISS["U+362d"].append("restriction")
BLISS_TO_UNICODE["three connecting dots"] = ["U+362e"]
UNICODE_TO_BLISS["U+362e"] = ["three connecting dots"]
BLISS_TO_UNICODE["viral infection"] = ["U+362f"]
UNICODE_TO_BLISS["U+362f"] = ["viral infection"]
BLISS_TO_UNICODE["virus"] = ["U+3630"]
UNICODE_TO_BLISS["U+3630"] = ["virus"]
BLISS_TO_UNICODE["eye makeup"] = ["U+3631"]
UNICODE_TO_BLISS["U+3631"] = ["eye makeup"]
BLISS_TO_UNICODE["plus"] = ["U+3632"]
UNICODE_TO_BLISS["U+3632"] = ["plus"]
BLISS_TO_UNICODE["butcher"] = ["U+3633"]
UNICODE_TO_BLISS["U+3633"] = ["butcher"]
BLISS_TO_UNICODE["meat"] = ["U+3634"]
UNICODE_TO_BLISS["U+3634"] = ["meat"]
BLISS_TO_UNICODE["fidelity"] = ["U+3635"]
UNICODE_TO_BLISS["U+3635"] = ["fidelity"]
BLISS_TO_UNICODE["loyalty"] = ["U+3635"]
UNICODE_TO_BLISS["U+3635"].append("loyalty")
BLISS_TO_UNICODE["solidarity"] = ["U+3635"]
UNICODE_TO_BLISS["U+3635"].append("solidarity")
BLISS_TO_UNICODE["fidelity,loyalty,solidarity"] = ["U+3635"]
UNICODE_TO_BLISS["U+3635"].append("fidelity,loyalty,solidarity")
BLISS_TO_UNICODE["attachment"] = ["U+3636"]
UNICODE_TO_BLISS["U+3636"] = ["attachment"]
BLISS_TO_UNICODE["cotton fabric"] = ["U+3637"]
UNICODE_TO_BLISS["U+3637"] = ["cotton fabric"]
BLISS_TO_UNICODE["playhouse"] = ["U+3638"]
UNICODE_TO_BLISS["U+3638"] = ["playhouse"]
BLISS_TO_UNICODE["play house"] = ["U+3638"]
UNICODE_TO_BLISS["U+3638"].append("play house")
BLISS_TO_UNICODE["playhouse,play house"] = ["U+3638"]
UNICODE_TO_BLISS["U+3638"].append("playhouse,play house")
BLISS_TO_UNICODE["house"] = ["U+3639"]
UNICODE_TO_BLISS["U+3639"] = ["house"]
BLISS_TO_UNICODE["play"] = ["U+363a"]
UNICODE_TO_BLISS["U+363a"] = ["play"]
BLISS_TO_UNICODE["spruce"] = ["U+3321"]
UNICODE_TO_BLISS["U+3321"].append("spruce")
BLISS_TO_UNICODE["fir"] = ["U+3321"]
UNICODE_TO_BLISS["U+3321"].append("fir")
BLISS_TO_UNICODE["fir tree"] = ["U+3321"]
UNICODE_TO_BLISS["U+3321"].append("fir tree")
BLISS_TO_UNICODE["evergreen tree,spruce,fir,fir tree"] = ["U+3321"]
UNICODE_TO_BLISS["U+3321"].append("evergreen tree,spruce,fir,fir tree")
BLISS_TO_UNICODE["pictograph of spruce branches"] = ["U+363b"]
UNICODE_TO_BLISS["U+363b"] = ["pictograph of spruce branches"]
BLISS_TO_UNICODE["lifeline"] = ["U+363c"]
UNICODE_TO_BLISS["U+363c"] = ["lifeline"]
BLISS_TO_UNICODE["strap"] = ["U+363d"]
UNICODE_TO_BLISS["U+363d"] = ["strap"]
BLISS_TO_UNICODE["string"] = ["U+363e"]
UNICODE_TO_BLISS["U+363e"] = ["string"]
BLISS_TO_UNICODE["velcro"] = ["U+363f"]
UNICODE_TO_BLISS["U+363f"] = ["velcro"]
BLISS_TO_UNICODE["rope"] = ["U+3640"]
UNICODE_TO_BLISS["U+3640"] = ["rope"]
BLISS_TO_UNICODE["cord"] = ["U+3641"]
UNICODE_TO_BLISS["U+3641"] = ["cord"]
BLISS_TO_UNICODE["backpack"] = ["U+3642"]
UNICODE_TO_BLISS["U+3642"] = ["backpack"]
BLISS_TO_UNICODE["rucksack"] = ["U+3642"]
UNICODE_TO_BLISS["U+3642"].append("rucksack")
BLISS_TO_UNICODE["backpack,rucksack"] = ["U+3642"]
UNICODE_TO_BLISS["U+3642"].append("backpack,rucksack")
BLISS_TO_UNICODE["back"] = ["U+3643"]
UNICODE_TO_BLISS["U+3643"] = ["back"]
BLISS_TO_UNICODE["covered"] = ["U+3644"]
UNICODE_TO_BLISS["U+3644"] = ["covered"]
BLISS_TO_UNICODE["hidden"] = ["U+3644"]
UNICODE_TO_BLISS["U+3644"].append("hidden")
BLISS_TO_UNICODE["covered,hidden"] = ["U+3644"]
UNICODE_TO_BLISS["U+3644"].append("covered,hidden")
BLISS_TO_UNICODE["invisible"] = ["U+3645"]
UNICODE_TO_BLISS["U+3645"] = ["invisible"]
BLISS_TO_UNICODE["repetition"] = ["U+3646"]
UNICODE_TO_BLISS["U+3646"] = ["repetition"]
BLISS_TO_UNICODE["copying"] = ["U+3646"]
UNICODE_TO_BLISS["U+3646"].append("copying")
BLISS_TO_UNICODE["duplication"] = ["U+3646"]
UNICODE_TO_BLISS["U+3646"].append("duplication")
BLISS_TO_UNICODE["replication"] = ["U+3646"]
UNICODE_TO_BLISS["U+3646"].append("replication")
BLISS_TO_UNICODE["repetition,copying,duplication,replication"] = ["U+3646"]
UNICODE_TO_BLISS["U+3646"].append("repetition,copying,duplication,replication")
BLISS_TO_UNICODE["diagonal arrow"] = ["U+3647"]
UNICODE_TO_BLISS["U+3647"] = ["diagonal arrow"]
BLISS_TO_UNICODE[" pointing upward and backward"] = ["U+3648"]
UNICODE_TO_BLISS["U+3648"] = [" pointing upward and backward"]
BLISS_TO_UNICODE["blanket"] = ["U+3649"]
UNICODE_TO_BLISS["U+3649"] = ["blanket"]
BLISS_TO_UNICODE["duvet"] = ["U+3649"]
UNICODE_TO_BLISS["U+3649"].append("duvet")
BLISS_TO_UNICODE["quilt"] = ["U+3649"]
UNICODE_TO_BLISS["U+3649"].append("quilt")
BLISS_TO_UNICODE["blanket,duvet,quilt"] = ["U+3649"]
UNICODE_TO_BLISS["U+3649"].append("blanket,duvet,quilt")
BLISS_TO_UNICODE["detachment"] = ["U+364a"]
UNICODE_TO_BLISS["U+364a"] = ["detachment"]
BLISS_TO_UNICODE["separation"] = ["U+364a"]
UNICODE_TO_BLISS["U+364a"].append("separation")
BLISS_TO_UNICODE["breakup"] = ["U+364a"]
UNICODE_TO_BLISS["U+364a"].append("breakup")
BLISS_TO_UNICODE["detachment,separation,breakup"] = ["U+364a"]
UNICODE_TO_BLISS["U+364a"].append("detachment,separation,breakup")
BLISS_TO_UNICODE["minus"] = ["U+364b"]
UNICODE_TO_BLISS["U+364b"] = ["minus"]
BLISS_TO_UNICODE["fastener"] = ["U+364c"]
UNICODE_TO_BLISS["U+364c"] = ["fastener"]
BLISS_TO_UNICODE["gripper"] = ["U+364c"]
UNICODE_TO_BLISS["U+364c"].append("gripper")
BLISS_TO_UNICODE["velcro"].append("U+364c")
UNICODE_TO_BLISS["U+364c"].append("velcro")
BLISS_TO_UNICODE["zipper"] = ["U+364c"]
UNICODE_TO_BLISS["U+364c"].append("zipper")
BLISS_TO_UNICODE["fastener,gripper,velcro,zipper"] = ["U+364c"]
UNICODE_TO_BLISS["U+364c"].append("fastener,gripper,velcro,zipper")
BLISS_TO_UNICODE["to fasten"] = ["U+364e"]
UNICODE_TO_BLISS["U+364e"] = ["to fasten"]
BLISS_TO_UNICODE["clothing)"] = ["U+364f"]
UNICODE_TO_BLISS["U+364f"] = ["clothing)"]
BLISS_TO_UNICODE["string"].append("U+363d")
UNICODE_TO_BLISS["U+363d"].append("string")
BLISS_TO_UNICODE["velcro"].append("U+363d")
UNICODE_TO_BLISS["U+363d"].append("velcro")
BLISS_TO_UNICODE["rope"].append("U+363d")
UNICODE_TO_BLISS["U+363d"].append("rope")
BLISS_TO_UNICODE["cord"].append("U+363d")
UNICODE_TO_BLISS["U+363d"].append("cord")
BLISS_TO_UNICODE["strap,string,velcro,rope,cord"] = ["U+363d"]
UNICODE_TO_BLISS["U+363d"].append("strap,string,velcro,rope,cord")
BLISS_TO_UNICODE["interrupt"] = ["U+3650"]
UNICODE_TO_BLISS["U+3650"] = ["interrupt"]
BLISS_TO_UNICODE["interruption"] = ["U+3651"]
UNICODE_TO_BLISS["U+3651"] = ["interruption"]
BLISS_TO_UNICODE["you"] = ["U+3652"]
UNICODE_TO_BLISS["U+3652"] = ["you"]
BLISS_TO_UNICODE["yourself"] = ["U+3652"]
UNICODE_TO_BLISS["U+3652"].append("yourself")
BLISS_TO_UNICODE["you,yourself"] = ["U+3652"]
UNICODE_TO_BLISS["U+3652"].append("you,yourself")
BLISS_TO_UNICODE["silver"] = ["U+3653"]
UNICODE_TO_BLISS["U+3653"] = ["silver"]
BLISS_TO_UNICODE["metal"] = ["U+3654"]
UNICODE_TO_BLISS["U+3654"] = ["metal"]
BLISS_TO_UNICODE["be caused by"] = ["U+3655"]
UNICODE_TO_BLISS["U+3655"] = ["be caused by"]
BLISS_TO_UNICODE["move bowels"] = ["U+3656"]
UNICODE_TO_BLISS["U+3656"] = ["move bowels"]
BLISS_TO_UNICODE["defecate"] = ["U+3656"]
UNICODE_TO_BLISS["U+3656"].append("defecate")
BLISS_TO_UNICODE["stool"] = ["U+3656"]
UNICODE_TO_BLISS["U+3656"].append("stool")
BLISS_TO_UNICODE["shit"] = ["U+3656"]
UNICODE_TO_BLISS["U+3656"].append("shit")
BLISS_TO_UNICODE["ca ca"] = ["U+3656"]
UNICODE_TO_BLISS["U+3656"].append("ca ca")
BLISS_TO_UNICODE["move bowels,defecate,stool,shit,ca-ca"] = ["U+3656"]
UNICODE_TO_BLISS["U+3656"].append("move bowels,defecate,stool,shit,ca-ca")
BLISS_TO_UNICODE["bowel movement"] = ["U+3657"]
UNICODE_TO_BLISS["U+3657"] = ["bowel movement"]
BLISS_TO_UNICODE["rouge"] = ["U+3658"]
UNICODE_TO_BLISS["U+3658"] = ["rouge"]
BLISS_TO_UNICODE["blusher"] = ["U+3658"]
UNICODE_TO_BLISS["U+3658"].append("blusher")
BLISS_TO_UNICODE["rouge,blusher"] = ["U+3658"]
UNICODE_TO_BLISS["U+3658"].append("rouge,blusher")
BLISS_TO_UNICODE["arrow"] = ["U+3659"]
UNICODE_TO_BLISS["U+3659"] = ["arrow"]
BLISS_TO_UNICODE["volcano"] = ["U+365a"]
UNICODE_TO_BLISS["U+365a"] = ["volcano"]
BLISS_TO_UNICODE["burial"] = ["U+365b"]
UNICODE_TO_BLISS["U+365b"] = ["burial"]
BLISS_TO_UNICODE["ceremony"] = ["U+365c"]
UNICODE_TO_BLISS["U+365c"] = ["ceremony"]
BLISS_TO_UNICODE["religious ceremony"] = ["U+365d"]
UNICODE_TO_BLISS["U+365d"] = ["religious ceremony"]
BLISS_TO_UNICODE["telescope"] = ["U+365e"]
UNICODE_TO_BLISS["U+365e"] = ["telescope"]
BLISS_TO_UNICODE["to see"] = ["U+365f"]
UNICODE_TO_BLISS["U+365f"] = ["to see"]
BLISS_TO_UNICODE["harmony"] = ["U+3660"]
UNICODE_TO_BLISS["U+3660"] = ["harmony"]
BLISS_TO_UNICODE["harmoniousness"] = ["U+3660"]
UNICODE_TO_BLISS["U+3660"].append("harmoniousness")
BLISS_TO_UNICODE["concord"] = ["U+3660"]
UNICODE_TO_BLISS["U+3660"].append("concord")
BLISS_TO_UNICODE["concordance"] = ["U+3660"]
UNICODE_TO_BLISS["U+3660"].append("concordance")
BLISS_TO_UNICODE["harmony,harmoniousness,concord,concordance"] = ["U+3660"]
UNICODE_TO_BLISS["U+3660"].append("harmony,harmoniousness,concord,concordance")
BLISS_TO_UNICODE["clothes"] = ["U+33f7"]
UNICODE_TO_BLISS["U+33f7"].append("clothes")
BLISS_TO_UNICODE["garment"] = ["U+33f7"]
UNICODE_TO_BLISS["U+33f7"].append("garment")
BLISS_TO_UNICODE["clothing,clothes,garment"] = ["U+33f7"]
UNICODE_TO_BLISS["U+33f7"].append("clothing,clothes,garment")
BLISS_TO_UNICODE["lawn bowling"] = ["U+3661"]
UNICODE_TO_BLISS["U+3661"] = ["lawn bowling"]
BLISS_TO_UNICODE["bowls"] = ["U+3661"]
UNICODE_TO_BLISS["U+3661"].append("bowls")
BLISS_TO_UNICODE["lawn bowling,bowls"] = ["U+3661"]
UNICODE_TO_BLISS["U+3661"].append("lawn bowling,bowls")
BLISS_TO_UNICODE["bowling"] = ["U+3662"]
UNICODE_TO_BLISS["U+3662"] = ["bowling"]
BLISS_TO_UNICODE["rutabaga"] = ["U+3340"]
UNICODE_TO_BLISS["U+3340"].append("rutabaga")
BLISS_TO_UNICODE["vegetable"] = ["U+3340"]
UNICODE_TO_BLISS["U+3340"].append("vegetable")
BLISS_TO_UNICODE["turnip,rutabaga,vegetable"] = ["U+3340"]
UNICODE_TO_BLISS["U+3340"].append("turnip,rutabaga,vegetable")
BLISS_TO_UNICODE["sukkah"] = ["U+3663"]
UNICODE_TO_BLISS["U+3663"] = ["sukkah"]
BLISS_TO_UNICODE["roof"] = ["U+3664"]
UNICODE_TO_BLISS["U+3664"] = ["roof"]
BLISS_TO_UNICODE["existence"] = ["U+3666"]
UNICODE_TO_BLISS["U+3666"] = ["existence"]
BLISS_TO_UNICODE["being"] = ["U+3667"]
UNICODE_TO_BLISS["U+3667"] = ["being"]
BLISS_TO_UNICODE["message"] = ["U+3668"]
UNICODE_TO_BLISS["U+3668"] = ["message"]
BLISS_TO_UNICODE["information"] = ["U+3669"]
UNICODE_TO_BLISS["U+3669"] = ["information"]
BLISS_TO_UNICODE["content"] = ["U+3668"]
UNICODE_TO_BLISS["U+3668"].append("content")
BLISS_TO_UNICODE["message,content"] = ["U+3668"]
UNICODE_TO_BLISS["U+3668"].append("message,content")
BLISS_TO_UNICODE["communication"] = ["U+366a"]
UNICODE_TO_BLISS["U+366a"] = ["communication"]
BLISS_TO_UNICODE["ball sports"] = ["U+366b"]
UNICODE_TO_BLISS["U+366b"] = ["ball sports"]
BLISS_TO_UNICODE["lymph node"] = ["U+366c"]
UNICODE_TO_BLISS["U+366c"] = ["lymph node"]
BLISS_TO_UNICODE["lymph gland"] = ["U+366c"]
UNICODE_TO_BLISS["U+366c"].append("lymph gland")
BLISS_TO_UNICODE["lymph node,lymph gland"] = ["U+366c"]
UNICODE_TO_BLISS["U+366c"].append("lymph node,lymph gland")
BLISS_TO_UNICODE["organ"] = ["U+366d"]
UNICODE_TO_BLISS["U+366d"] = ["organ"]
BLISS_TO_UNICODE["lymph"] = ["U+366e"]
UNICODE_TO_BLISS["U+366e"] = ["lymph"]
BLISS_TO_UNICODE["vascular system"] = ["U+366f"]
UNICODE_TO_BLISS["U+366f"] = ["vascular system"]
BLISS_TO_UNICODE["generalisation"] = ["U+3670"]
UNICODE_TO_BLISS["U+3670"] = ["generalisation"]
BLISS_TO_UNICODE["blood"] = ["U+3671"]
UNICODE_TO_BLISS["U+3671"] = ["blood"]
BLISS_TO_UNICODE["encourage"] = ["U+3672"]
UNICODE_TO_BLISS["U+3672"] = ["encourage"]
BLISS_TO_UNICODE["encouragement"] = ["U+3673"]
UNICODE_TO_BLISS["U+3673"] = ["encouragement"]
BLISS_TO_UNICODE["foundation"] = ["U+3674"]
UNICODE_TO_BLISS["U+3674"] = ["foundation"]
BLISS_TO_UNICODE["base"] = ["U+3674"]
UNICODE_TO_BLISS["U+3674"].append("base")
BLISS_TO_UNICODE["fundament"] = ["U+3674"]
UNICODE_TO_BLISS["U+3674"].append("fundament")
BLISS_TO_UNICODE["foundation,base,fundament"] = ["U+3674"]
UNICODE_TO_BLISS["U+3674"].append("foundation,base,fundament")
BLISS_TO_UNICODE["four leaf clover"] = ["U+3675"]
UNICODE_TO_BLISS["U+3675"] = ["four leaf clover"]
BLISS_TO_UNICODE["four-leaf clover"] = ["U+3675"]
UNICODE_TO_BLISS["U+3675"].append("four-leaf clover")
BLISS_TO_UNICODE["sheet"] = ["U+3676"]
UNICODE_TO_BLISS["U+3676"] = ["sheet"]
BLISS_TO_UNICODE["bedclothes"] = ["U+3676"]
UNICODE_TO_BLISS["U+3676"].append("bedclothes")
BLISS_TO_UNICODE["bed linen"] = ["U+3676"]
UNICODE_TO_BLISS["U+3676"].append("bed linen")
BLISS_TO_UNICODE["guess"] = ["U+3677"]
UNICODE_TO_BLISS["U+3677"] = ["guess"]
BLISS_TO_UNICODE["estimate"] = ["U+3677"]
UNICODE_TO_BLISS["U+3677"].append("estimate")
BLISS_TO_UNICODE["guess,estimate"] = ["U+3677"]
UNICODE_TO_BLISS["U+3677"].append("guess,estimate")
BLISS_TO_UNICODE["plus minus"] = ["U+3678"]
UNICODE_TO_BLISS["U+3678"] = ["plus minus"]
BLISS_TO_UNICODE["knit"] = ["U+3679"]
UNICODE_TO_BLISS["U+3679"] = ["knit"]
BLISS_TO_UNICODE["enormous"] = ["U+367b"]
UNICODE_TO_BLISS["U+367b"] = ["enormous"]
BLISS_TO_UNICODE["huge"] = ["U+367c"]
UNICODE_TO_BLISS["U+367c"] = ["huge"]
BLISS_TO_UNICODE["shuttlecock"] = ["U+367d"]
UNICODE_TO_BLISS["U+367d"] = ["shuttlecock"]
BLISS_TO_UNICODE["birdie"] = ["U+367d"]
UNICODE_TO_BLISS["U+367d"].append("birdie")
BLISS_TO_UNICODE["shuttlecock,birdie"] = ["U+367d"]
UNICODE_TO_BLISS["U+367d"].append("shuttlecock,birdie")
BLISS_TO_UNICODE["next month"] = ["U+367e"]
UNICODE_TO_BLISS["U+367e"] = ["next month"]
BLISS_TO_UNICODE["this year"] = ["U+367f"]
UNICODE_TO_BLISS["U+367f"] = ["this year"]
BLISS_TO_UNICODE["stripe"] = ["U+34cf"]
UNICODE_TO_BLISS["U+34cf"].append("stripe")
BLISS_TO_UNICODE["line,stripe"] = ["U+34cf"]
UNICODE_TO_BLISS["U+34cf"].append("line,stripe")
BLISS_TO_UNICODE["symbol is a fullsized vertical line"] = ["U+3680"]
UNICODE_TO_BLISS["U+3680"] = ["symbol is a fullsized vertical line"]
BLISS_TO_UNICODE["wash"] = ["U+3681"]
UNICODE_TO_BLISS["U+3681"] = ["wash"]
BLISS_TO_UNICODE["bathe"] = ["U+3681"]
UNICODE_TO_BLISS["U+3681"].append("bathe")
BLISS_TO_UNICODE["bath"] = ["U+3681"]
UNICODE_TO_BLISS["U+3681"].append("bath")
BLISS_TO_UNICODE["wash,bathe,bath"] = ["U+3681"]
UNICODE_TO_BLISS["U+3681"].append("wash,bathe,bath")
BLISS_TO_UNICODE["teach"] = ["U+3682"]
UNICODE_TO_BLISS["U+3682"] = ["teach"]
BLISS_TO_UNICODE["instruct"] = ["U+3682"]
UNICODE_TO_BLISS["U+3682"].append("instruct")
BLISS_TO_UNICODE["teach,instruct"] = ["U+3682"]
UNICODE_TO_BLISS["U+3682"].append("teach,instruct")
BLISS_TO_UNICODE["to give"] = ["U+3683"]
UNICODE_TO_BLISS["U+3683"] = ["to give"]
BLISS_TO_UNICODE["pound sterling"] = ["U+3684"]
UNICODE_TO_BLISS["U+3684"] = ["pound sterling"]
BLISS_TO_UNICODE["international symbol for British pound sterling"] = ["U+3685"]
UNICODE_TO_BLISS["U+3685"] = ["international symbol for British pound sterling"]
BLISS_TO_UNICODE["single parent"] = ["U+3686"]
UNICODE_TO_BLISS["U+3686"] = ["single parent"]
BLISS_TO_UNICODE["clearness"] = ["U+3687"]
UNICODE_TO_BLISS["U+3687"] = ["clearness"]
BLISS_TO_UNICODE["clarity"] = ["U+3687"]
UNICODE_TO_BLISS["U+3687"].append("clarity")
BLISS_TO_UNICODE["transparency"] = ["U+3687"]
UNICODE_TO_BLISS["U+3687"].append("transparency")
BLISS_TO_UNICODE["transparence"] = ["U+3687"]
UNICODE_TO_BLISS["U+3687"].append("transparence")
BLISS_TO_UNICODE["clearness,clarity,transparency,transparence"] = ["U+3687"]
UNICODE_TO_BLISS["U+3687"].append("clearness,clarity,transparency,transparence")
BLISS_TO_UNICODE["basketball"] = ["U+3688"]
UNICODE_TO_BLISS["U+3688"] = ["basketball"]
BLISS_TO_UNICODE["service"] = ["U+3689"]
UNICODE_TO_BLISS["U+3689"] = ["service"]
BLISS_TO_UNICODE["plan"] = ["U+368a"]
UNICODE_TO_BLISS["U+368a"] = ["plan"]
BLISS_TO_UNICODE["constructional blocks"] = ["U+368b"]
UNICODE_TO_BLISS["U+368b"] = ["constructional blocks"]
BLISS_TO_UNICODE["lego"] = ["U+368b"]
UNICODE_TO_BLISS["U+368b"].append("lego")
BLISS_TO_UNICODE["constructional blocks,lego"] = ["U+368b"]
UNICODE_TO_BLISS["U+368b"].append("constructional blocks,lego")
BLISS_TO_UNICODE["together"] = ["U+368c"]
UNICODE_TO_BLISS["U+368c"] = ["together"]
BLISS_TO_UNICODE["engagement"] = ["U+368d"]
UNICODE_TO_BLISS["U+368d"] = ["engagement"]
BLISS_TO_UNICODE["Roman Catholicism"] = ["U+368e"]
UNICODE_TO_BLISS["U+368e"] = ["Roman Catholicism"]
BLISS_TO_UNICODE["Roman Catholic Church"] = ["U+368e"]
UNICODE_TO_BLISS["U+368e"].append("Roman Catholic Church")
BLISS_TO_UNICODE["Roman Catholicism,Roman Catholic Church"] = ["U+368e"]
UNICODE_TO_BLISS["U+368e"].append("Roman Catholicism,Roman Catholic Church")
BLISS_TO_UNICODE["religion"] = ["U+368f"]
UNICODE_TO_BLISS["U+368f"] = ["religion"]
BLISS_TO_UNICODE["Vatican"] = ["U+3690"]
UNICODE_TO_BLISS["U+3690"] = ["Vatican"]
BLISS_TO_UNICODE["hijacker"] = ["U+3691"]
UNICODE_TO_BLISS["U+3691"] = ["hijacker"]
BLISS_TO_UNICODE["coup maker"] = ["U+3691"]
UNICODE_TO_BLISS["U+3691"].append("coup maker")
BLISS_TO_UNICODE["hijacker,coup maker"] = ["U+3691"]
UNICODE_TO_BLISS["U+3691"].append("hijacker,coup maker")
BLISS_TO_UNICODE["coup"] = ["U+3692"]
UNICODE_TO_BLISS["U+3692"] = ["coup"]
BLISS_TO_UNICODE["hijack"] = ["U+3693"]
UNICODE_TO_BLISS["U+3693"] = ["hijack"]
BLISS_TO_UNICODE["takeover"] = ["U+3694"]
UNICODE_TO_BLISS["U+3694"] = ["takeover"]
BLISS_TO_UNICODE["necessary"] = ["U+3695"]
UNICODE_TO_BLISS["U+3695"] = ["necessary"]
BLISS_TO_UNICODE["necessarily"] = ["U+3695"]
UNICODE_TO_BLISS["U+3695"].append("necessarily")
BLISS_TO_UNICODE["needed"] = ["U+3695"]
UNICODE_TO_BLISS["U+3695"].append("needed")
BLISS_TO_UNICODE["necessary,necessarily,needed"] = ["U+3695"]
UNICODE_TO_BLISS["U+3695"].append("necessary,necessarily,needed")
BLISS_TO_UNICODE["need"] = ["U+3696"]
UNICODE_TO_BLISS["U+3696"] = ["need"]
BLISS_TO_UNICODE["linoleum"] = ["U+339d"]
UNICODE_TO_BLISS["U+339d"].append("linoleum")
BLISS_TO_UNICODE["floor covering,linoleum"] = ["U+339d"]
UNICODE_TO_BLISS["U+339d"].append("floor covering,linoleum")
BLISS_TO_UNICODE["bitter"] = ["U+3697"]
UNICODE_TO_BLISS["U+3697"] = ["bitter"]
BLISS_TO_UNICODE["down"] = ["U+3698"]
UNICODE_TO_BLISS["U+3698"] = ["down"]
BLISS_TO_UNICODE["hear"] = ["U+3699"]
UNICODE_TO_BLISS["U+3699"] = ["hear"]
BLISS_TO_UNICODE["listen"] = ["U+3699"]
UNICODE_TO_BLISS["U+3699"].append("listen")
BLISS_TO_UNICODE["hear,listen"] = ["U+3699"]
UNICODE_TO_BLISS["U+3699"].append("hear,listen")
BLISS_TO_UNICODE["infiniteness"] = ["U+369a"]
UNICODE_TO_BLISS["U+369a"] = ["infiniteness"]
BLISS_TO_UNICODE["boundlessness"] = ["U+369a"]
UNICODE_TO_BLISS["U+369a"].append("boundlessness")
BLISS_TO_UNICODE["limitlessness"] = ["U+369a"]
UNICODE_TO_BLISS["U+369a"].append("limitlessness")
BLISS_TO_UNICODE["infiniteness,boundlessness,limitlessness"] = ["U+369a"]
UNICODE_TO_BLISS["U+369a"].append("infiniteness,boundlessness,limitlessness")
BLISS_TO_UNICODE["get engaged"] = ["U+369b"]
UNICODE_TO_BLISS["U+369b"] = ["get engaged"]
BLISS_TO_UNICODE["potholder"] = ["U+369c"]
UNICODE_TO_BLISS["U+369c"] = ["potholder"]
BLISS_TO_UNICODE["oven mitt"] = ["U+369c"]
UNICODE_TO_BLISS["U+369c"].append("oven mitt")
BLISS_TO_UNICODE["potholder,oven mitt"] = ["U+369c"]
UNICODE_TO_BLISS["U+369c"].append("potholder,oven mitt")
BLISS_TO_UNICODE["crawl"] = ["U+369d"]
UNICODE_TO_BLISS["U+369d"] = ["crawl"]
BLISS_TO_UNICODE["kneeling person"] = ["U+369e"]
UNICODE_TO_BLISS["U+369e"] = ["kneeling person"]
BLISS_TO_UNICODE["raw material"].append("U+35cb")
UNICODE_TO_BLISS["U+35cb"].append("raw material")
BLISS_TO_UNICODE["stuff"] = ["U+35cb"]
UNICODE_TO_BLISS["U+35cb"].append("stuff")
BLISS_TO_UNICODE["material,raw material,stuff"] = ["U+35cb"]
UNICODE_TO_BLISS["U+35cb"].append("material,raw material,stuff")
BLISS_TO_UNICODE["coward"] = ["U+369f"]
UNICODE_TO_BLISS["U+369f"] = ["coward"]
BLISS_TO_UNICODE["cowardice"] = ["U+36a0"]
UNICODE_TO_BLISS["U+36a0"] = ["cowardice"]
BLISS_TO_UNICODE["werewolf"] = ["U+36a1"]
UNICODE_TO_BLISS["U+36a1"] = ["werewolf"]
BLISS_TO_UNICODE["imaginary person"] = ["U+36a2"]
UNICODE_TO_BLISS["U+36a2"] = ["imaginary person"]
BLISS_TO_UNICODE["wolf"] = ["U+36a3"]
UNICODE_TO_BLISS["U+36a3"] = ["wolf"]
BLISS_TO_UNICODE["quickness"] = ["U+36a4"]
UNICODE_TO_BLISS["U+36a4"] = ["quickness"]
BLISS_TO_UNICODE["rapidity"] = ["U+36a4"]
UNICODE_TO_BLISS["U+36a4"].append("rapidity")
BLISS_TO_UNICODE["speediness"] = ["U+36a4"]
UNICODE_TO_BLISS["U+36a4"].append("speediness")
BLISS_TO_UNICODE["quickness,rapidity,speediness"] = ["U+36a4"]
UNICODE_TO_BLISS["U+36a4"].append("quickness,rapidity,speediness")
BLISS_TO_UNICODE["emotion"] = ["U+321f"]
UNICODE_TO_BLISS["U+321f"].append("emotion")
BLISS_TO_UNICODE["sensation"] = ["U+321f"]
UNICODE_TO_BLISS["U+321f"].append("sensation")
BLISS_TO_UNICODE["feeling,emotion,sensation"] = ["U+321f"]
UNICODE_TO_BLISS["U+321f"].append("feeling,emotion,sensation")
BLISS_TO_UNICODE["symbol is the familiar heart shape"] = ["U+36a5"]
UNICODE_TO_BLISS["U+36a5"] = ["symbol is the familiar heart shape"]
BLISS_TO_UNICODE["serving spoon"] = ["U+36a6"]
UNICODE_TO_BLISS["U+36a6"] = ["serving spoon"]
BLISS_TO_UNICODE["Moomintroll"] = ["U+36a7"]
UNICODE_TO_BLISS["U+36a7"] = ["Moomintroll"]
BLISS_TO_UNICODE["imprint"] = ["U+36a8"]
UNICODE_TO_BLISS["U+36a8"] = ["imprint"]
BLISS_TO_UNICODE["depression"] = ["U+36a9"]
UNICODE_TO_BLISS["U+36a9"] = ["depression"]
BLISS_TO_UNICODE["M"] = ["U+36aa"]
UNICODE_TO_BLISS["U+36aa"] = ["M"]
BLISS_TO_UNICODE["eagerness"] = ["U+36ab"]
UNICODE_TO_BLISS["U+36ab"] = ["eagerness"]
BLISS_TO_UNICODE["keenness"] = ["U+36ab"]
UNICODE_TO_BLISS["U+36ab"].append("keenness")
BLISS_TO_UNICODE["willingness"] = ["U+36ab"]
UNICODE_TO_BLISS["U+36ab"].append("willingness")
BLISS_TO_UNICODE["eagerness,keenness,willingness"] = ["U+36ab"]
UNICODE_TO_BLISS["U+36ab"].append("eagerness,keenness,willingness")
BLISS_TO_UNICODE["runner"] = ["U+34b1"]
UNICODE_TO_BLISS["U+34b1"].append("runner")
BLISS_TO_UNICODE["ski,runner"] = ["U+34b1"]
UNICODE_TO_BLISS["U+34b1"].append("ski,runner")
BLISS_TO_UNICODE["pictograph of a ski"] = ["U+36ac"]
UNICODE_TO_BLISS["U+36ac"] = ["pictograph of a ski"]
BLISS_TO_UNICODE["altruism"] = ["U+36ad"]
UNICODE_TO_BLISS["U+36ad"] = ["altruism"]
BLISS_TO_UNICODE["selflessness"] = ["U+36ad"]
UNICODE_TO_BLISS["U+36ad"].append("selflessness")
BLISS_TO_UNICODE["altruism,selflessness"] = ["U+36ad"]
UNICODE_TO_BLISS["U+36ad"].append("altruism,selflessness")
BLISS_TO_UNICODE["lymphatic system"] = ["U+36ae"]
UNICODE_TO_BLISS["U+36ae"] = ["lymphatic system"]
BLISS_TO_UNICODE["urinate"] = ["U+36af"]
UNICODE_TO_BLISS["U+36af"] = ["urinate"]
BLISS_TO_UNICODE["make water"] = ["U+36af"]
UNICODE_TO_BLISS["U+36af"].append("make water")
BLISS_TO_UNICODE["pass water"] = ["U+36af"]
UNICODE_TO_BLISS["U+36af"].append("pass water")
BLISS_TO_UNICODE["micturate"] = ["U+36af"]
UNICODE_TO_BLISS["U+36af"].append("micturate")
BLISS_TO_UNICODE["pee"] = ["U+36af"]
UNICODE_TO_BLISS["U+36af"].append("pee")
BLISS_TO_UNICODE["piddle"] = ["U+36af"]
UNICODE_TO_BLISS["U+36af"].append("piddle")
BLISS_TO_UNICODE["piss"] = ["U+36af"]
UNICODE_TO_BLISS["U+36af"].append("piss")
BLISS_TO_UNICODE["wee"] = ["U+36af"]
UNICODE_TO_BLISS["U+36af"].append("wee")
BLISS_TO_UNICODE["urinate,make water,pass water,micturate,pee,piddle,piss,wee"] = ["U+36af"]
UNICODE_TO_BLISS["U+36af"].append("urinate,make water,pass water,micturate,pee,piddle,piss,wee")
BLISS_TO_UNICODE["urine"] = ["U+36b0"]
UNICODE_TO_BLISS["U+36b0"] = ["urine"]
BLISS_TO_UNICODE["kidnap"] = ["U+36b1"]
UNICODE_TO_BLISS["U+36b1"] = ["kidnap"]
BLISS_TO_UNICODE["theft"] = ["U+36b2"]
UNICODE_TO_BLISS["U+36b2"] = ["theft"]
BLISS_TO_UNICODE["escalator"] = ["U+36b3"]
UNICODE_TO_BLISS["U+36b3"] = ["escalator"]
BLISS_TO_UNICODE["moving stairs"] = ["U+36b3"]
UNICODE_TO_BLISS["U+36b3"].append("moving stairs")
BLISS_TO_UNICODE["escalator,moving stairs"] = ["U+36b3"]
UNICODE_TO_BLISS["U+36b3"].append("escalator,moving stairs")
BLISS_TO_UNICODE["stairs"] = ["U+36b4"]
UNICODE_TO_BLISS["U+36b4"] = ["stairs"]
BLISS_TO_UNICODE["up and down"] = ["U+36b5"]
UNICODE_TO_BLISS["U+36b5"] = ["up and down"]
BLISS_TO_UNICODE["concrete"] = ["U+36b6"]
UNICODE_TO_BLISS["U+36b6"] = ["concrete"]
BLISS_TO_UNICODE["cement"] = ["U+36b6"]
UNICODE_TO_BLISS["U+36b6"].append("cement")
BLISS_TO_UNICODE["concrete,cement"] = ["U+36b6"]
UNICODE_TO_BLISS["U+36b6"].append("concrete,cement")
BLISS_TO_UNICODE["man-made"] = ["U+36b7"]
UNICODE_TO_BLISS["U+36b7"] = ["man-made"]
BLISS_TO_UNICODE["sport lesson"] = ["U+36b8"]
UNICODE_TO_BLISS["U+36b8"] = ["sport lesson"]
BLISS_TO_UNICODE["lesson"] = ["U+36b9"]
UNICODE_TO_BLISS["U+36b9"] = ["lesson"]
BLISS_TO_UNICODE["responsible"] = ["U+36ba"]
UNICODE_TO_BLISS["U+36ba"] = ["responsible"]
BLISS_TO_UNICODE["responsibility"] = ["U+36bb"]
UNICODE_TO_BLISS["U+36bb"] = ["responsibility"]
BLISS_TO_UNICODE["hum"] = ["U+36bc"]
UNICODE_TO_BLISS["U+36bc"] = ["hum"]
BLISS_TO_UNICODE["to sing"] = ["U+36bd"]
UNICODE_TO_BLISS["U+36bd"] = ["to sing"]
BLISS_TO_UNICODE["word"] = ["U+36be"]
UNICODE_TO_BLISS["U+36be"] = ["word"]
BLISS_TO_UNICODE["Lakshmi"] = ["U+36bf"]
UNICODE_TO_BLISS["U+36bf"] = ["Lakshmi"]
BLISS_TO_UNICODE["stirrup"] = ["U+36c0"]
UNICODE_TO_BLISS["U+36c0"] = ["stirrup"]
BLISS_TO_UNICODE["support"] = ["U+36c1"]
UNICODE_TO_BLISS["U+36c1"] = ["support"]
BLISS_TO_UNICODE["riding"] = ["U+36c2"]
UNICODE_TO_BLISS["U+36c2"] = ["riding"]
BLISS_TO_UNICODE["shall"] = ["U+36c3"]
UNICODE_TO_BLISS["U+36c3"] = ["shall"]
BLISS_TO_UNICODE["will"] = ["U+36c3"]
UNICODE_TO_BLISS["U+36c3"].append("will")
BLISS_TO_UNICODE["shall,will"] = ["U+36c3"]
UNICODE_TO_BLISS["U+36c3"].append("shall,will")
BLISS_TO_UNICODE["constructional toy"] = ["U+36c4"]
UNICODE_TO_BLISS["U+36c4"] = ["constructional toy"]
BLISS_TO_UNICODE["toy"] = ["U+36c5"]
UNICODE_TO_BLISS["U+36c5"] = ["toy"]
BLISS_TO_UNICODE["infinite"] = ["U+36c6"]
UNICODE_TO_BLISS["U+36c6"] = ["infinite"]
BLISS_TO_UNICODE["limitless"] = ["U+36c6"]
UNICODE_TO_BLISS["U+36c6"].append("limitless")
BLISS_TO_UNICODE["infinite,limitless"] = ["U+36c6"]
UNICODE_TO_BLISS["U+36c6"].append("infinite,limitless")
BLISS_TO_UNICODE["open mouth"] = ["U+3297"]
UNICODE_TO_BLISS["U+3297"].append("open mouth")
BLISS_TO_UNICODE["gape"] = ["U+3297"]
UNICODE_TO_BLISS["U+3297"].append("gape")
BLISS_TO_UNICODE["open"] = ["U+36c7"]
UNICODE_TO_BLISS["U+36c7"] = ["open"]
BLISS_TO_UNICODE["addict"] = ["U+36c8"]
UNICODE_TO_BLISS["U+36c8"] = ["addict"]
BLISS_TO_UNICODE["addiction"] = ["U+36c9"]
UNICODE_TO_BLISS["U+36c9"] = ["addiction"]
BLISS_TO_UNICODE["mail"] = ["U+3586"]
UNICODE_TO_BLISS["U+3586"].append("mail")
BLISS_TO_UNICODE["post"].append("U+3586")
UNICODE_TO_BLISS["U+3586"].append("post")
BLISS_TO_UNICODE["letter,mail,post"] = ["U+3586"]
UNICODE_TO_BLISS["U+3586"].append("letter,mail,post")
BLISS_TO_UNICODE["dryness"] = ["U+36ca"]
UNICODE_TO_BLISS["U+36ca"] = ["dryness"]
BLISS_TO_UNICODE["drought"] = ["U+36ca"]
UNICODE_TO_BLISS["U+36ca"].append("drought")
BLISS_TO_UNICODE["dryness,drought"] = ["U+36ca"]
UNICODE_TO_BLISS["U+36ca"].append("dryness,drought")
BLISS_TO_UNICODE["to delete"] = ["U+36cb"]
UNICODE_TO_BLISS["U+36cb"] = ["to delete"]
BLISS_TO_UNICODE["dried meat"] = ["U+3634"]
UNICODE_TO_BLISS["U+3634"].append("dried meat")
BLISS_TO_UNICODE["dry"] = ["U+36cc"]
UNICODE_TO_BLISS["U+36cc"] = ["dry"]
BLISS_TO_UNICODE["bedbug"] = ["U+36cd"]
UNICODE_TO_BLISS["U+36cd"] = ["bedbug"]
BLISS_TO_UNICODE["wall louse"] = ["U+36cd"]
UNICODE_TO_BLISS["U+36cd"].append("wall louse")
BLISS_TO_UNICODE["bedbug,wall louse"] = ["U+36cd"]
UNICODE_TO_BLISS["U+36cd"].append("bedbug,wall louse")
BLISS_TO_UNICODE["louse"] = ["U+36ce"]
UNICODE_TO_BLISS["U+36ce"] = ["louse"]
BLISS_TO_UNICODE["stinging insect"] = ["U+36cf"]
UNICODE_TO_BLISS["U+36cf"] = ["stinging insect"]
BLISS_TO_UNICODE["indoor"] = ["U+36d0"]
UNICODE_TO_BLISS["U+36d0"] = ["indoor"]
BLISS_TO_UNICODE["pacifier"] = ["U+36d1"]
UNICODE_TO_BLISS["U+36d1"] = ["pacifier"]
BLISS_TO_UNICODE["dummy"] = ["U+36d1"]
UNICODE_TO_BLISS["U+36d1"].append("dummy")
BLISS_TO_UNICODE["pacifier,dummy"] = ["U+36d1"]
UNICODE_TO_BLISS["U+36d1"].append("pacifier,dummy")
BLISS_TO_UNICODE["singer"] = ["U+36d2"]
UNICODE_TO_BLISS["U+36d2"] = ["singer"]
BLISS_TO_UNICODE["Christian love"] = ["U+36d3"]
UNICODE_TO_BLISS["U+36d3"] = ["Christian love"]
BLISS_TO_UNICODE["Christian"] = ["U+36d4"]
UNICODE_TO_BLISS["U+36d4"] = ["Christian"]
BLISS_TO_UNICODE["group of"] = ["U+36d5"]
UNICODE_TO_BLISS["U+36d5"] = ["group of"]
BLISS_TO_UNICODE["camp"] = ["U+36d6"]
UNICODE_TO_BLISS["U+36d6"] = ["camp"]
BLISS_TO_UNICODE["yell"] = ["U+36d7"]
UNICODE_TO_BLISS["U+36d7"] = ["yell"]
BLISS_TO_UNICODE["scream"] = ["U+36d7"]
UNICODE_TO_BLISS["U+36d7"].append("scream")
BLISS_TO_UNICODE["yell,scream"] = ["U+36d7"]
UNICODE_TO_BLISS["U+36d7"].append("yell,scream")
BLISS_TO_UNICODE["three intensity symbols"] = ["U+36d8"]
UNICODE_TO_BLISS["U+36d8"] = ["three intensity symbols"]
BLISS_TO_UNICODE["plus sign"] = ["U+36d9"]
UNICODE_TO_BLISS["U+36d9"] = ["plus sign"]
BLISS_TO_UNICODE["bomb"] = ["U+36da"]
UNICODE_TO_BLISS["U+36da"] = ["bomb"]
BLISS_TO_UNICODE["explosive"].append("U+36da")
UNICODE_TO_BLISS["U+36da"].append("explosive")
BLISS_TO_UNICODE["bomb,explosive"] = ["U+36da"]
UNICODE_TO_BLISS["U+36da"].append("bomb,explosive")
BLISS_TO_UNICODE["explosion"] = ["U+36db"]
UNICODE_TO_BLISS["U+36db"] = ["explosion"]
BLISS_TO_UNICODE["gauge"] = ["U+36dc"]
UNICODE_TO_BLISS["U+36dc"] = ["gauge"]
BLISS_TO_UNICODE["scale"] = ["U+36dd"]
UNICODE_TO_BLISS["U+36dd"] = ["scale"]
BLISS_TO_UNICODE["participate"] = ["U+36de"]
UNICODE_TO_BLISS["U+36de"] = ["participate"]
BLISS_TO_UNICODE["participation"] = ["U+36df"]
UNICODE_TO_BLISS["U+36df"] = ["participation"]
BLISS_TO_UNICODE["indicator activity"] = ["U+36e0"]
UNICODE_TO_BLISS["U+36e0"] = ["indicator activity"]
BLISS_TO_UNICODE["fatal"] = ["U+36e1"]
UNICODE_TO_BLISS["U+36e1"] = ["fatal"]
BLISS_TO_UNICODE["lethal"] = ["U+36e1"]
UNICODE_TO_BLISS["U+36e1"].append("lethal")
BLISS_TO_UNICODE["fatal,lethal"] = ["U+36e1"]
UNICODE_TO_BLISS["U+36e1"].append("fatal,lethal")
BLISS_TO_UNICODE["drug addict"] = ["U+36e2"]
UNICODE_TO_BLISS["U+36e2"] = ["drug addict"]
BLISS_TO_UNICODE["drug addiction"] = ["U+36e3"]
UNICODE_TO_BLISS["U+36e3"] = ["drug addiction"]
BLISS_TO_UNICODE["vasectomy"] = ["U+36e4"]
UNICODE_TO_BLISS["U+36e4"] = ["vasectomy"]
BLISS_TO_UNICODE["operation"] = ["U+36e5"]
UNICODE_TO_BLISS["U+36e5"] = ["operation"]
BLISS_TO_UNICODE["vas deferens"] = ["U+36e6"]
UNICODE_TO_BLISS["U+36e6"] = ["vas deferens"]
BLISS_TO_UNICODE["grunt"] = ["U+36e7"]
UNICODE_TO_BLISS["U+36e7"] = ["grunt"]
BLISS_TO_UNICODE["to talk"] = ["U+36e8"]
UNICODE_TO_BLISS["U+36e8"] = ["to talk"]
BLISS_TO_UNICODE["excavator"] = ["U+36e9"]
UNICODE_TO_BLISS["U+36e9"] = ["excavator"]
BLISS_TO_UNICODE["digger"] = ["U+36e9"]
UNICODE_TO_BLISS["U+36e9"].append("digger")
BLISS_TO_UNICODE["power shovel"] = ["U+36e9"]
UNICODE_TO_BLISS["U+36e9"].append("power shovel")
BLISS_TO_UNICODE["excavator,digger,power shovel"] = ["U+36e9"]
UNICODE_TO_BLISS["U+36e9"].append("excavator,digger,power shovel")
BLISS_TO_UNICODE["digging"] = ["U+36ea"]
UNICODE_TO_BLISS["U+36ea"] = ["digging"]
BLISS_TO_UNICODE["excavation"] = ["U+36eb"]
UNICODE_TO_BLISS["U+36eb"] = ["excavation"]
BLISS_TO_UNICODE["speed cycling"] = ["U+36ec"]
UNICODE_TO_BLISS["U+36ec"] = ["speed cycling"]
BLISS_TO_UNICODE["underpants"] = ["U+36ed"]
UNICODE_TO_BLISS["U+36ed"] = ["underpants"]
BLISS_TO_UNICODE["briefs"] = ["U+36ed"]
UNICODE_TO_BLISS["U+36ed"].append("briefs")
BLISS_TO_UNICODE["panties"] = ["U+36ed"]
UNICODE_TO_BLISS["U+36ed"].append("panties")
BLISS_TO_UNICODE["underpants,briefs,panties"] = ["U+36ed"]
UNICODE_TO_BLISS["U+36ed"].append("underpants,briefs,panties")
BLISS_TO_UNICODE["pants"] = ["U+36ee"]
UNICODE_TO_BLISS["U+36ee"] = ["pants"]
BLISS_TO_UNICODE["Mother's Day"] = ["U+36ef"]
UNICODE_TO_BLISS["U+36ef"] = ["Mother's Day"]
BLISS_TO_UNICODE["maturation"] = ["U+36f0"]
UNICODE_TO_BLISS["U+36f0"] = ["maturation"]
BLISS_TO_UNICODE["to advance"] = ["U+36f1"]
UNICODE_TO_BLISS["U+36f1"] = ["to advance"]
BLISS_TO_UNICODE["shrub"].append("U+357d")
UNICODE_TO_BLISS["U+357d"].append("shrub")
BLISS_TO_UNICODE["bush,shrub"] = ["U+357d"]
UNICODE_TO_BLISS["U+357d"].append("bush,shrub")
BLISS_TO_UNICODE["home run"] = ["U+36f2"]
UNICODE_TO_BLISS["U+36f2"] = ["home run"]
BLISS_TO_UNICODE["mend"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"].append("mend")
BLISS_TO_UNICODE["repair"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"].append("repair")
BLISS_TO_UNICODE["fix,mend,repair"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"].append("fix,mend,repair")
BLISS_TO_UNICODE["fixing"] = ["U+36f3"]
UNICODE_TO_BLISS["U+36f3"] = ["fixing"]
BLISS_TO_UNICODE["fix"].append("U+36f3")
UNICODE_TO_BLISS["U+36f3"].append("fix")
BLISS_TO_UNICODE["mending"] = ["U+36f3"]
UNICODE_TO_BLISS["U+36f3"].append("mending")
BLISS_TO_UNICODE["mend"].append("U+36f3")
UNICODE_TO_BLISS["U+36f3"].append("mend")
BLISS_TO_UNICODE["repair"].append("U+36f3")
UNICODE_TO_BLISS["U+36f3"].append("repair")
BLISS_TO_UNICODE["reparation"] = ["U+36f3"]
UNICODE_TO_BLISS["U+36f3"].append("reparation")
BLISS_TO_UNICODE["fixing,fix,mending,mend,repair,reparation"] = ["U+36f3"]
UNICODE_TO_BLISS["U+36f3"].append("fixing,fix,mending,mend,repair,reparation")
BLISS_TO_UNICODE["to work"] = ["U+36f4"]
UNICODE_TO_BLISS["U+36f4"] = ["to work"]
BLISS_TO_UNICODE["puddle"] = ["U+36f5"]
UNICODE_TO_BLISS["U+36f5"] = ["puddle"]
BLISS_TO_UNICODE["plate"] = ["U+3551"]
UNICODE_TO_BLISS["U+3551"].append("plate")
BLISS_TO_UNICODE["platter"] = ["U+3551"]
UNICODE_TO_BLISS["U+3551"].append("platter")
BLISS_TO_UNICODE["dish,plate,platter"] = ["U+3551"]
UNICODE_TO_BLISS["U+3551"].append("dish,plate,platter")
BLISS_TO_UNICODE["temporary home"] = ["U+36f6"]
UNICODE_TO_BLISS["U+36f6"] = ["temporary home"]
BLISS_TO_UNICODE["home"] = ["U+36f7"]
UNICODE_TO_BLISS["U+36f7"] = ["home"]
BLISS_TO_UNICODE["chick pea"] = ["U+333a"]
UNICODE_TO_BLISS["U+333a"].append("chick pea")
BLISS_TO_UNICODE["kidney bean"] = ["U+333a"]
UNICODE_TO_BLISS["U+333a"].append("kidney bean")
BLISS_TO_UNICODE["pinto bean"] = ["U+333a"]
UNICODE_TO_BLISS["U+333a"].append("pinto bean")
BLISS_TO_UNICODE["pocket"] = ["U+36f8"]
UNICODE_TO_BLISS["U+36f8"] = ["pocket"]
BLISS_TO_UNICODE["boathouse"] = ["U+36f9"]
UNICODE_TO_BLISS["U+36f9"] = ["boathouse"]
BLISS_TO_UNICODE["cushion"] = ["U+34ec"]
UNICODE_TO_BLISS["U+34ec"].append("cushion")
BLISS_TO_UNICODE["pillow,cushion"] = ["U+34ec"]
UNICODE_TO_BLISS["U+34ec"].append("pillow,cushion")
BLISS_TO_UNICODE["seat"] = ["U+36fa"]
UNICODE_TO_BLISS["U+36fa"] = ["seat"]
BLISS_TO_UNICODE["gravy"] = ["U+3603"]
UNICODE_TO_BLISS["U+3603"].append("gravy")
BLISS_TO_UNICODE["relish"] = ["U+3603"]
UNICODE_TO_BLISS["U+3603"].append("relish")
BLISS_TO_UNICODE["dressing"] = ["U+3603"]
UNICODE_TO_BLISS["U+3603"].append("dressing")
BLISS_TO_UNICODE["sauce,gravy,relish,dressing"] = ["U+3603"]
UNICODE_TO_BLISS["U+3603"].append("sauce,gravy,relish,dressing")
BLISS_TO_UNICODE["liquid"] = ["U+36fb"]
UNICODE_TO_BLISS["U+36fb"] = ["liquid"]
BLISS_TO_UNICODE["jaguar"] = ["U+36fc"]
UNICODE_TO_BLISS["U+36fc"] = ["jaguar"]
BLISS_TO_UNICODE["spot"] = ["U+36fd"]
UNICODE_TO_BLISS["U+36fd"] = ["spot"]
BLISS_TO_UNICODE["stocking"] = ["U+36fe"]
UNICODE_TO_BLISS["U+36fe"] = ["stocking"]
BLISS_TO_UNICODE["sock"] = ["U+36fe"]
UNICODE_TO_BLISS["U+36fe"].append("sock")
BLISS_TO_UNICODE["pantyhose"] = ["U+36fe"]
UNICODE_TO_BLISS["U+36fe"].append("pantyhose")
BLISS_TO_UNICODE["tights"] = ["U+36fe"]
UNICODE_TO_BLISS["U+36fe"].append("tights")
BLISS_TO_UNICODE["leg and foot"] = ["U+36ff"]
UNICODE_TO_BLISS["U+36ff"] = ["leg and foot"]
BLISS_TO_UNICODE["disaster"] = ["U+3700"]
UNICODE_TO_BLISS["U+3700"] = ["disaster"]
BLISS_TO_UNICODE["catastrophe"] = ["U+3700"]
UNICODE_TO_BLISS["U+3700"].append("catastrophe")
BLISS_TO_UNICODE["disaster,catastrophe"] = ["U+3700"]
UNICODE_TO_BLISS["U+3700"].append("disaster,catastrophe")
BLISS_TO_UNICODE["just"] = ["U+3701"]
UNICODE_TO_BLISS["U+3701"] = ["just"]
BLISS_TO_UNICODE["fair"].append("U+3701")
UNICODE_TO_BLISS["U+3701"].append("fair")
BLISS_TO_UNICODE["just,fair"] = ["U+3701"]
UNICODE_TO_BLISS["U+3701"].append("just,fair")
BLISS_TO_UNICODE["judgement"] = ["U+3702"]
UNICODE_TO_BLISS["U+3702"] = ["judgement"]
BLISS_TO_UNICODE["same/equal"] = ["U+3703"]
UNICODE_TO_BLISS["U+3703"] = ["same/equal"]
BLISS_TO_UNICODE["descr. ind"] = ["U+3704"]
UNICODE_TO_BLISS["U+3704"] = ["descr. ind"]
BLISS_TO_UNICODE["shipping forecast"] = ["U+3705"]
UNICODE_TO_BLISS["U+3705"] = ["shipping forecast"]
BLISS_TO_UNICODE["weather forecast"] = ["U+3706"]
UNICODE_TO_BLISS["U+3706"] = ["weather forecast"]
BLISS_TO_UNICODE["result"] = ["U+33b9"]
UNICODE_TO_BLISS["U+33b9"].append("result")
BLISS_TO_UNICODE["effect,result"] = ["U+33b9"]
UNICODE_TO_BLISS["U+33b9"].append("effect,result")
BLISS_TO_UNICODE["greater than"] = ["U+3707"]
UNICODE_TO_BLISS["U+3707"] = ["greater than"]
BLISS_TO_UNICODE["outcome"] = ["U+3708"]
UNICODE_TO_BLISS["U+3708"] = ["outcome"]
BLISS_TO_UNICODE["result"].append("U+3708")
UNICODE_TO_BLISS["U+3708"].append("result")
BLISS_TO_UNICODE["outcome,result"] = ["U+3708"]
UNICODE_TO_BLISS["U+3708"].append("outcome,result")
BLISS_TO_UNICODE["fail"] = ["U+3709"]
UNICODE_TO_BLISS["U+3709"] = ["fail"]
BLISS_TO_UNICODE["failure"] = ["U+370a"]
UNICODE_TO_BLISS["U+370a"] = ["failure"]
BLISS_TO_UNICODE["pot stand"] = ["U+370b"]
UNICODE_TO_BLISS["U+370b"] = ["pot stand"]
BLISS_TO_UNICODE["trivet"] = ["U+370b"]
UNICODE_TO_BLISS["U+370b"].append("trivet")
BLISS_TO_UNICODE["pot stand,trivet"] = ["U+370b"]
UNICODE_TO_BLISS["U+370b"].append("pot stand,trivet")
BLISS_TO_UNICODE["gavel"] = ["U+353f"]
UNICODE_TO_BLISS["U+353f"].append("gavel")
BLISS_TO_UNICODE["mallet"] = ["U+353f"]
UNICODE_TO_BLISS["U+353f"].append("mallet")
BLISS_TO_UNICODE["hammer,gavel,mallet"] = ["U+353f"]
UNICODE_TO_BLISS["U+353f"].append("hammer,gavel,mallet")
BLISS_TO_UNICODE["best"] = ["U+370c"]
UNICODE_TO_BLISS["U+370c"] = ["best"]
BLISS_TO_UNICODE["Purim"] = ["U+370d"]
UNICODE_TO_BLISS["U+370d"] = ["Purim"]
BLISS_TO_UNICODE["holiday"] = ["U+370e"]
UNICODE_TO_BLISS["U+370e"] = ["holiday"]
BLISS_TO_UNICODE["score"] = ["U+370f"]
UNICODE_TO_BLISS["U+370f"] = ["score"]
BLISS_TO_UNICODE["water tower"] = ["U+3710"]
UNICODE_TO_BLISS["U+3710"] = ["water tower"]
BLISS_TO_UNICODE["tower"] = ["U+3711"]
UNICODE_TO_BLISS["U+3711"] = ["tower"]
BLISS_TO_UNICODE["yogurt"] = ["U+3712"]
UNICODE_TO_BLISS["U+3712"] = ["yogurt"]
BLISS_TO_UNICODE["yoghurt"] = ["U+3712"]
UNICODE_TO_BLISS["U+3712"].append("yoghurt")
BLISS_TO_UNICODE["yogurt,yoghurt"] = ["U+3712"]
UNICODE_TO_BLISS["U+3712"].append("yogurt,yoghurt")
BLISS_TO_UNICODE["milk"] = ["U+3713"]
UNICODE_TO_BLISS["U+3713"] = ["milk"]
BLISS_TO_UNICODE["frozen"] = ["U+3714"]
UNICODE_TO_BLISS["U+3714"] = ["frozen"]
BLISS_TO_UNICODE["let us"] = ["U+3715"]
UNICODE_TO_BLISS["U+3715"] = ["let us"]
BLISS_TO_UNICODE["let's"] = ["U+3715"]
UNICODE_TO_BLISS["U+3715"].append("let's")
BLISS_TO_UNICODE["let us,let's"] = ["U+3715"]
UNICODE_TO_BLISS["U+3715"].append("let us,let's")
BLISS_TO_UNICODE["to let"] = ["U+3716"]
UNICODE_TO_BLISS["U+3716"] = ["to let"]
BLISS_TO_UNICODE["us"] = ["U+3717"]
UNICODE_TO_BLISS["U+3717"] = ["us"]
BLISS_TO_UNICODE["pirate"] = ["U+3719"]
UNICODE_TO_BLISS["U+3719"] = ["pirate"]
BLISS_TO_UNICODE["sailor"] = ["U+371a"]
UNICODE_TO_BLISS["U+371a"] = ["sailor"]
BLISS_TO_UNICODE["receiving"] = ["U+371b"]
UNICODE_TO_BLISS["U+371b"] = ["receiving"]
BLISS_TO_UNICODE["keep"] = ["U+371c"]
UNICODE_TO_BLISS["U+371c"] = ["keep"]
BLISS_TO_UNICODE["preserve"] = ["U+371c"]
UNICODE_TO_BLISS["U+371c"].append("preserve")
BLISS_TO_UNICODE["save"] = ["U+371c"]
UNICODE_TO_BLISS["U+371c"].append("save")
BLISS_TO_UNICODE["keep,preserve,save"] = ["U+371c"]
UNICODE_TO_BLISS["U+371c"].append("keep,preserve,save")
BLISS_TO_UNICODE["to hold"] = ["U+371d"]
UNICODE_TO_BLISS["U+371d"] = ["to hold"]
BLISS_TO_UNICODE["wage"] = ["U+371e"]
UNICODE_TO_BLISS["U+371e"] = ["wage"]
BLISS_TO_UNICODE["pay"] = ["U+371e"]
UNICODE_TO_BLISS["U+371e"].append("pay")
BLISS_TO_UNICODE["salary"] = ["U+371e"]
UNICODE_TO_BLISS["U+371e"].append("salary")
BLISS_TO_UNICODE["for"] = ["U+371f"]
UNICODE_TO_BLISS["U+371f"] = ["for"]
BLISS_TO_UNICODE["nature"] = ["U+344b"]
UNICODE_TO_BLISS["U+344b"].append("nature")
BLISS_TO_UNICODE["creation,nature"] = ["U+344b"]
UNICODE_TO_BLISS["U+344b"].append("creation,nature")
BLISS_TO_UNICODE["equal-sided triangle"] = ["U+3720"]
UNICODE_TO_BLISS["U+3720"] = ["equal-sided triangle"]
BLISS_TO_UNICODE["precious thing"] = ["U+3721"]
UNICODE_TO_BLISS["U+3721"] = ["precious thing"]
BLISS_TO_UNICODE["treasure"] = ["U+3721"]
UNICODE_TO_BLISS["U+3721"].append("treasure")
BLISS_TO_UNICODE["precious thing,treasure"] = ["U+3721"]
UNICODE_TO_BLISS["U+3721"].append("precious thing,treasure")
BLISS_TO_UNICODE["precious"] = ["U+3722"]
UNICODE_TO_BLISS["U+3722"] = ["precious"]
BLISS_TO_UNICODE["vestment"] = ["U+3723"]
UNICODE_TO_BLISS["U+3723"] = ["vestment"]
BLISS_TO_UNICODE["accident"] = ["U+3724"]
UNICODE_TO_BLISS["U+3724"] = ["accident"]
BLISS_TO_UNICODE["chance event"] = ["U+3724"]
UNICODE_TO_BLISS["U+3724"].append("chance event")
BLISS_TO_UNICODE["accident,chance event"] = ["U+3724"]
UNICODE_TO_BLISS["U+3724"].append("accident,chance event")
BLISS_TO_UNICODE["to expect"] = ["U+3725"]
UNICODE_TO_BLISS["U+3725"] = ["to expect"]
BLISS_TO_UNICODE["state"] = ["U+3516"]
UNICODE_TO_BLISS["U+3516"].append("state")
BLISS_TO_UNICODE["country,state"] = ["U+3516"]
UNICODE_TO_BLISS["U+3516"].append("country,state")
BLISS_TO_UNICODE["country"].append("U+3322")
UNICODE_TO_BLISS["U+3322"].append("country")
BLISS_TO_UNICODE["countryside,country"] = ["U+3322"]
UNICODE_TO_BLISS["U+3322"].append("countryside,country")
BLISS_TO_UNICODE["incense"] = ["U+3726"]
UNICODE_TO_BLISS["U+3726"] = ["incense"]
BLISS_TO_UNICODE["smoke"] = ["U+3727"]
UNICODE_TO_BLISS["U+3727"] = ["smoke"]
BLISS_TO_UNICODE["smell"] = ["U+3728"]
UNICODE_TO_BLISS["U+3728"] = ["smell"]
BLISS_TO_UNICODE["argue"] = ["U+3729"]
UNICODE_TO_BLISS["U+3729"] = ["argue"]
BLISS_TO_UNICODE["dispute"] = ["U+3729"]
UNICODE_TO_BLISS["U+3729"].append("dispute")
BLISS_TO_UNICODE["quarrel"] = ["U+3729"]
UNICODE_TO_BLISS["U+3729"].append("quarrel")
BLISS_TO_UNICODE["argue,dispute,quarrel"] = ["U+3729"]
UNICODE_TO_BLISS["U+3729"].append("argue,dispute,quarrel")
BLISS_TO_UNICODE["argument"] = ["U+372a"]
UNICODE_TO_BLISS["U+372a"] = ["argument"]
BLISS_TO_UNICODE["telephone card"] = ["U+372b"]
UNICODE_TO_BLISS["U+372b"] = ["telephone card"]
BLISS_TO_UNICODE["card"] = ["U+372c"]
UNICODE_TO_BLISS["U+372c"] = ["card"]
BLISS_TO_UNICODE["gopher"] = ["U+372d"]
UNICODE_TO_BLISS["U+372d"] = ["gopher"]
BLISS_TO_UNICODE["ground hog"] = ["U+372d"]
UNICODE_TO_BLISS["U+372d"].append("ground hog")
BLISS_TO_UNICODE["gopher,ground hog"] = ["U+372d"]
UNICODE_TO_BLISS["U+372d"].append("gopher,ground hog")
BLISS_TO_UNICODE["rodent"] = ["U+372e"]
UNICODE_TO_BLISS["U+372e"] = ["rodent"]
BLISS_TO_UNICODE["horse trailer"] = ["U+372f"]
UNICODE_TO_BLISS["U+372f"] = ["horse trailer"]
BLISS_TO_UNICODE["horsebox"] = ["U+372f"]
UNICODE_TO_BLISS["U+372f"].append("horsebox")
BLISS_TO_UNICODE["horse trailer,horsebox"] = ["U+372f"]
UNICODE_TO_BLISS["U+372f"].append("horse trailer,horsebox")
BLISS_TO_UNICODE["trailer"] = ["U+3730"]
UNICODE_TO_BLISS["U+3730"] = ["trailer"]
BLISS_TO_UNICODE["container transport"] = ["U+3731"]
UNICODE_TO_BLISS["U+3731"] = ["container transport"]
BLISS_TO_UNICODE["pregnancy"] = ["U+3732"]
UNICODE_TO_BLISS["U+3732"] = ["pregnancy"]
BLISS_TO_UNICODE["conception"] = ["U+3733"]
UNICODE_TO_BLISS["U+3733"] = ["conception"]
BLISS_TO_UNICODE["missal"] = ["U+3734"]
UNICODE_TO_BLISS["U+3734"] = ["missal"]
BLISS_TO_UNICODE["liturgical book"] = ["U+3734"]
UNICODE_TO_BLISS["U+3734"].append("liturgical book")
BLISS_TO_UNICODE["missal,liturgical book"] = ["U+3734"]
UNICODE_TO_BLISS["U+3734"].append("missal,liturgical book")
BLISS_TO_UNICODE["true"] = ["U+3735"]
UNICODE_TO_BLISS["U+3735"] = ["true"]
BLISS_TO_UNICODE["truly"] = ["U+3735"]
UNICODE_TO_BLISS["U+3735"].append("truly")
BLISS_TO_UNICODE["truthful"] = ["U+3735"]
UNICODE_TO_BLISS["U+3735"].append("truthful")
BLISS_TO_UNICODE["truthfully"] = ["U+3735"]
UNICODE_TO_BLISS["U+3735"].append("truthfully")
BLISS_TO_UNICODE["true,truly,truthful,truthfully"] = ["U+3735"]
UNICODE_TO_BLISS["U+3735"].append("true,truly,truthful,truthfully")
BLISS_TO_UNICODE["wind instrument"] = ["U+3736"]
UNICODE_TO_BLISS["U+3736"] = ["wind instrument"]
BLISS_TO_UNICODE["musical instrument"] = ["U+3737"]
UNICODE_TO_BLISS["U+3737"] = ["musical instrument"]
BLISS_TO_UNICODE["lighthouse"] = ["U+3738"]
UNICODE_TO_BLISS["U+3738"] = ["lighthouse"]
BLISS_TO_UNICODE["grocery store"] = ["U+3739"]
UNICODE_TO_BLISS["U+3739"] = ["grocery store"]
BLISS_TO_UNICODE["food store"] = ["U+3739"]
UNICODE_TO_BLISS["U+3739"].append("food store")
BLISS_TO_UNICODE["supermarket"] = ["U+3739"]
UNICODE_TO_BLISS["U+3739"].append("supermarket")
BLISS_TO_UNICODE["grocery store,food store,supermarket"] = ["U+3739"]
UNICODE_TO_BLISS["U+3739"].append("grocery store,food store,supermarket")
BLISS_TO_UNICODE["store"] = ["U+373a"]
UNICODE_TO_BLISS["U+373a"] = ["store"]
BLISS_TO_UNICODE["union"] = ["U+373b"]
UNICODE_TO_BLISS["U+373b"] = ["union"]
BLISS_TO_UNICODE["horseradish"] = ["U+373c"]
UNICODE_TO_BLISS["U+373c"] = ["horseradish"]
BLISS_TO_UNICODE["fry"] = ["U+373d"]
UNICODE_TO_BLISS["U+373d"] = ["fry"]
BLISS_TO_UNICODE["saute"] = ["U+373d"]
UNICODE_TO_BLISS["U+373d"].append("saute")
BLISS_TO_UNICODE["fry,saute"] = ["U+373d"]
UNICODE_TO_BLISS["U+373d"].append("fry,saute")
BLISS_TO_UNICODE["to cook"] = ["U+373e"]
UNICODE_TO_BLISS["U+373e"] = ["to cook"]
BLISS_TO_UNICODE["nail polish"] = ["U+373f"]
UNICODE_TO_BLISS["U+373f"] = ["nail polish"]
BLISS_TO_UNICODE["nail varnish"] = ["U+373f"]
UNICODE_TO_BLISS["U+373f"].append("nail varnish")
BLISS_TO_UNICODE["nail polish,nail varnish"] = ["U+373f"]
UNICODE_TO_BLISS["U+373f"].append("nail polish,nail varnish")
BLISS_TO_UNICODE["saliva"] = ["U+3740"]
UNICODE_TO_BLISS["U+3740"] = ["saliva"]
BLISS_TO_UNICODE["spit"].append("U+3740")
UNICODE_TO_BLISS["U+3740"].append("spit")
BLISS_TO_UNICODE["saliva,spit"] = ["U+3740"]
UNICODE_TO_BLISS["U+3740"].append("saliva,spit")
BLISS_TO_UNICODE["spitting"] = ["U+3741"]
UNICODE_TO_BLISS["U+3741"] = ["spitting"]
BLISS_TO_UNICODE["rotisserie"] = ["U+3742"]
UNICODE_TO_BLISS["U+3742"] = ["rotisserie"]
BLISS_TO_UNICODE["spit"].append("U+3742")
UNICODE_TO_BLISS["U+3742"].append("spit")
BLISS_TO_UNICODE["rotisserie,spit"] = ["U+3742"]
UNICODE_TO_BLISS["U+3742"].append("rotisserie,spit")
BLISS_TO_UNICODE["rotation"] = ["U+3743"]
UNICODE_TO_BLISS["U+3743"] = ["rotation"]
BLISS_TO_UNICODE["eastern"] = ["U+3744"]
UNICODE_TO_BLISS["U+3744"] = ["eastern"]
BLISS_TO_UNICODE["Poland"] = ["U+3745"]
UNICODE_TO_BLISS["U+3745"] = ["Poland"]
BLISS_TO_UNICODE["worker"] = ["U+3746"]
UNICODE_TO_BLISS["U+3746"] = ["worker"]
BLISS_TO_UNICODE["desire"].append("U+32cb")
UNICODE_TO_BLISS["U+32cb"].append("desire")
BLISS_TO_UNICODE["wish,desire"] = ["U+32cb"]
UNICODE_TO_BLISS["U+32cb"].append("wish,desire")
BLISS_TO_UNICODE["circumcision"] = ["U+3747"]
UNICODE_TO_BLISS["U+3747"] = ["circumcision"]
BLISS_TO_UNICODE["to remove"] = ["U+3748"]
UNICODE_TO_BLISS["U+3748"] = ["to remove"]
BLISS_TO_UNICODE["foreskin"] = ["U+3749"]
UNICODE_TO_BLISS["U+3749"] = ["foreskin"]
BLISS_TO_UNICODE["elevator"] = ["U+374a"]
UNICODE_TO_BLISS["U+374a"] = ["elevator"]
BLISS_TO_UNICODE["lift"] = ["U+374a"]
UNICODE_TO_BLISS["U+374a"].append("lift")
BLISS_TO_UNICODE["elevator,lift"] = ["U+374a"]
UNICODE_TO_BLISS["U+374a"].append("elevator,lift")
BLISS_TO_UNICODE["hoist"] = ["U+374b"]
UNICODE_TO_BLISS["U+374b"] = ["hoist"]
BLISS_TO_UNICODE["lift"].append("U+374b")
UNICODE_TO_BLISS["U+374b"].append("lift")
BLISS_TO_UNICODE["hoist,lift"] = ["U+374b"]
UNICODE_TO_BLISS["U+374b"].append("hoist,lift")
BLISS_TO_UNICODE["aid"] = ["U+374c"]
UNICODE_TO_BLISS["U+374c"] = ["aid"]
BLISS_TO_UNICODE["raise"] = ["U+374a"]
UNICODE_TO_BLISS["U+374a"].append("raise")
BLISS_TO_UNICODE["lift,raise"] = ["U+374a"]
UNICODE_TO_BLISS["U+374a"].append("lift,raise")
BLISS_TO_UNICODE["up"] = ["U+374d"]
UNICODE_TO_BLISS["U+374d"] = ["up"]
BLISS_TO_UNICODE["tail lift"] = ["U+374e"]
UNICODE_TO_BLISS["U+374e"] = ["tail lift"]
BLISS_TO_UNICODE["lift"].append("U+374e")
UNICODE_TO_BLISS["U+374e"].append("lift")
BLISS_TO_UNICODE["tail lift,lift"] = ["U+374e"]
UNICODE_TO_BLISS["U+374e"].append("tail lift,lift")
BLISS_TO_UNICODE["platform"] = ["U+374f"]
UNICODE_TO_BLISS["U+374f"] = ["platform"]
BLISS_TO_UNICODE["prostitution"] = ["U+3750"]
UNICODE_TO_BLISS["U+3750"] = ["prostitution"]
BLISS_TO_UNICODE["sexual intercourse"] = ["U+3751"]
UNICODE_TO_BLISS["U+3751"] = ["sexual intercourse"]
BLISS_TO_UNICODE["kid"] = ["U+328c"]
UNICODE_TO_BLISS["U+328c"].append("kid")
BLISS_TO_UNICODE["youngster"] = ["U+328c"]
UNICODE_TO_BLISS["U+328c"].append("youngster")
BLISS_TO_UNICODE["child,kid,youngster"] = ["U+328c"]
UNICODE_TO_BLISS["U+328c"].append("child,kid,youngster")
BLISS_TO_UNICODE["child"].append("U+33ff")
UNICODE_TO_BLISS["U+33ff"].append("child")
BLISS_TO_UNICODE["offspring,child"] = ["U+33ff"]
UNICODE_TO_BLISS["U+33ff"].append("offspring,child")
BLISS_TO_UNICODE["business"] = ["U+3752"]
UNICODE_TO_BLISS["U+3752"] = ["business"]
BLISS_TO_UNICODE["economy"] = ["U+3752"]
UNICODE_TO_BLISS["U+3752"].append("economy")
BLISS_TO_UNICODE["commerce"].append("U+3752")
UNICODE_TO_BLISS["U+3752"].append("commerce")
BLISS_TO_UNICODE["trade"] = ["U+3752"]
UNICODE_TO_BLISS["U+3752"].append("trade")
BLISS_TO_UNICODE["business,economy,commerce,trade"] = ["U+3752"]
UNICODE_TO_BLISS["U+3752"].append("business,economy,commerce,trade")
BLISS_TO_UNICODE["voltmeter"] = ["U+3753"]
UNICODE_TO_BLISS["U+3753"] = ["voltmeter"]
BLISS_TO_UNICODE["voltage"] = ["U+3754"]
UNICODE_TO_BLISS["U+3754"] = ["voltage"]
BLISS_TO_UNICODE["life jacket"] = ["U+3755"]
UNICODE_TO_BLISS["U+3755"] = ["life jacket"]
BLISS_TO_UNICODE["life-jacket"] = ["U+3755"]
UNICODE_TO_BLISS["U+3755"].append("life-jacket")
BLISS_TO_UNICODE["canoeing"] = ["U+3756"]
UNICODE_TO_BLISS["U+3756"] = ["canoeing"]
BLISS_TO_UNICODE["paddle"] = ["U+3757"]
UNICODE_TO_BLISS["U+3757"] = ["paddle"]
BLISS_TO_UNICODE["key guard"] = ["U+3758"]
UNICODE_TO_BLISS["U+3758"] = ["key guard"]
BLISS_TO_UNICODE["keyboard"] = ["U+3759"]
UNICODE_TO_BLISS["U+3759"] = ["keyboard"]
BLISS_TO_UNICODE["eyeliner"] = ["U+375a"]
UNICODE_TO_BLISS["U+375a"] = ["eyeliner"]
BLISS_TO_UNICODE["kohl"] = ["U+375a"]
UNICODE_TO_BLISS["U+375a"].append("kohl")
BLISS_TO_UNICODE["eyeliner,kohl"] = ["U+375a"]
UNICODE_TO_BLISS["U+375a"].append("eyeliner,kohl")
BLISS_TO_UNICODE["horse box"] = ["U+375b"]
UNICODE_TO_BLISS["U+375b"] = ["horse box"]
BLISS_TO_UNICODE["stall"] = ["U+375b"]
UNICODE_TO_BLISS["U+375b"].append("stall")
BLISS_TO_UNICODE["horse box,stall"] = ["U+375b"]
UNICODE_TO_BLISS["U+375b"].append("horse box,stall")
BLISS_TO_UNICODE["give off odour"] = ["U+3728"]
UNICODE_TO_BLISS["U+3728"].append("give off odour")
BLISS_TO_UNICODE["smell,give off odour"] = ["U+3728"]
UNICODE_TO_BLISS["U+3728"].append("smell,give off odour")
BLISS_TO_UNICODE["bricklayer"] = ["U+375c"]
UNICODE_TO_BLISS["U+375c"] = ["bricklayer"]
BLISS_TO_UNICODE["brick"] = ["U+375d"]
UNICODE_TO_BLISS["U+375d"] = ["brick"]
BLISS_TO_UNICODE["toaster"] = ["U+375e"]
UNICODE_TO_BLISS["U+375e"] = ["toaster"]
BLISS_TO_UNICODE["to toast"] = ["U+375f"]
UNICODE_TO_BLISS["U+375f"] = ["to toast"]
BLISS_TO_UNICODE["a"] = ["U+3760"]
UNICODE_TO_BLISS["U+3760"] = ["a"]
BLISS_TO_UNICODE["an"] = ["U+3760"]
UNICODE_TO_BLISS["U+3760"].append("an")
BLISS_TO_UNICODE["any"] = ["U+3760"]
UNICODE_TO_BLISS["U+3760"].append("any")
BLISS_TO_UNICODE["a,an,any"] = ["U+3760"]
UNICODE_TO_BLISS["U+3760"].append("a,an,any")
BLISS_TO_UNICODE["diagonal line suggests an index finger pointing at something unspecific. The diagonal line has the opposite orientation to the one used in the"] = ["U+3761"]
UNICODE_TO_BLISS["U+3761"] = ["diagonal line suggests an index finger pointing at something unspecific. The diagonal line has the opposite orientation to the one used in the"]
BLISS_TO_UNICODE[" this and that."] = ["U+3762"]
UNICODE_TO_BLISS["U+3762"] = [" this and that."]
BLISS_TO_UNICODE["some"] = ["U+3763"]
UNICODE_TO_BLISS["U+3763"] = ["some"]
BLISS_TO_UNICODE["any"].append("U+3763")
UNICODE_TO_BLISS["U+3763"].append("any")
BLISS_TO_UNICODE["some,any"] = ["U+3763"]
UNICODE_TO_BLISS["U+3763"].append("some,any")
BLISS_TO_UNICODE["occupational therapy"] = ["U+3764"]
UNICODE_TO_BLISS["U+3764"] = ["occupational therapy"]
BLISS_TO_UNICODE["therapy"] = ["U+3765"]
UNICODE_TO_BLISS["U+3765"] = ["therapy"]
BLISS_TO_UNICODE["kettle"] = ["U+33b5"]
UNICODE_TO_BLISS["U+33b5"].append("kettle")
BLISS_TO_UNICODE["boiler"] = ["U+33b5"]
UNICODE_TO_BLISS["U+33b5"].append("boiler")
BLISS_TO_UNICODE["pot,kettle,boiler"] = ["U+33b5"]
UNICODE_TO_BLISS["U+33b5"].append("pot,kettle,boiler")
BLISS_TO_UNICODE["ownership"] = ["U+3766"]
UNICODE_TO_BLISS["U+3766"] = ["ownership"]
BLISS_TO_UNICODE["possession"] = ["U+3766"]
UNICODE_TO_BLISS["U+3766"].append("possession")
BLISS_TO_UNICODE["ownership,possession"] = ["U+3766"]
UNICODE_TO_BLISS["U+3766"].append("ownership,possession")
BLISS_TO_UNICODE["supper"] = ["U+3767"]
UNICODE_TO_BLISS["U+3767"] = ["supper"]
BLISS_TO_UNICODE["dinner"] = ["U+3767"]
UNICODE_TO_BLISS["U+3767"].append("dinner")
BLISS_TO_UNICODE["supper,dinner"] = ["U+3767"]
UNICODE_TO_BLISS["U+3767"].append("supper,dinner")
BLISS_TO_UNICODE["meal"] = ["U+3768"]
UNICODE_TO_BLISS["U+3768"] = ["meal"]
BLISS_TO_UNICODE["underground station"] = ["U+3769"]
UNICODE_TO_BLISS["U+3769"] = ["underground station"]
BLISS_TO_UNICODE["subway station"] = ["U+3769"]
UNICODE_TO_BLISS["U+3769"].append("subway station")
BLISS_TO_UNICODE["underground station,subway station"] = ["U+3769"]
UNICODE_TO_BLISS["U+3769"].append("underground station,subway station")
BLISS_TO_UNICODE["station"] = ["U+376a"]
UNICODE_TO_BLISS["U+376a"] = ["station"]
BLISS_TO_UNICODE["tune"] = ["U+376b"]
UNICODE_TO_BLISS["U+376b"] = ["tune"]
BLISS_TO_UNICODE["melody"] = ["U+376b"]
UNICODE_TO_BLISS["U+376b"].append("melody")
BLISS_TO_UNICODE["tune,melody"] = ["U+376b"]
UNICODE_TO_BLISS["U+376b"].append("tune,melody")
BLISS_TO_UNICODE["bomb shelter"] = ["U+376c"]
UNICODE_TO_BLISS["U+376c"] = ["bomb shelter"]
BLISS_TO_UNICODE["shelter"] = ["U+376d"]
UNICODE_TO_BLISS["U+376d"] = ["shelter"]
BLISS_TO_UNICODE["scientist"] = ["U+376e"]
UNICODE_TO_BLISS["U+376e"] = ["scientist"]
BLISS_TO_UNICODE["academic"] = ["U+376e"]
UNICODE_TO_BLISS["U+376e"].append("academic")
BLISS_TO_UNICODE["scientist,academic"] = ["U+376e"]
UNICODE_TO_BLISS["U+376e"].append("scientist,academic")
BLISS_TO_UNICODE["coldness"] = ["U+376f"]
UNICODE_TO_BLISS["U+376f"] = ["coldness"]
BLISS_TO_UNICODE["cold"].append("U+376f")
UNICODE_TO_BLISS["U+376f"].append("cold")
BLISS_TO_UNICODE["coldness,cold"] = ["U+376f"]
UNICODE_TO_BLISS["U+376f"].append("coldness,cold")
BLISS_TO_UNICODE["juridical"] = ["U+3770"]
UNICODE_TO_BLISS["U+3770"] = ["juridical"]
BLISS_TO_UNICODE["melodica"] = ["U+3771"]
UNICODE_TO_BLISS["U+3771"] = ["melodica"]
BLISS_TO_UNICODE["blow organ"] = ["U+3771"]
UNICODE_TO_BLISS["U+3771"].append("blow organ")
BLISS_TO_UNICODE["melodica,blow-organ"] = ["U+3771"]
UNICODE_TO_BLISS["U+3771"].append("melodica,blow-organ")
BLISS_TO_UNICODE["moo"] = ["U+3772"]
UNICODE_TO_BLISS["U+3772"] = ["moo"]
BLISS_TO_UNICODE["bellow"] = ["U+3772"]
UNICODE_TO_BLISS["U+3772"].append("bellow")
BLISS_TO_UNICODE["moo,bellow"] = ["U+3772"]
UNICODE_TO_BLISS["U+3772"].append("moo,bellow")
BLISS_TO_UNICODE["cow"] = ["U+3773"]
UNICODE_TO_BLISS["U+3773"] = ["cow"]
BLISS_TO_UNICODE["dish gloves"] = ["U+3774"]
UNICODE_TO_BLISS["U+3774"] = ["dish gloves"]
BLISS_TO_UNICODE["rubber gloves"] = ["U+3774"]
UNICODE_TO_BLISS["U+3774"].append("rubber gloves")
BLISS_TO_UNICODE["dish gloves,rubber gloves"] = ["U+3774"]
UNICODE_TO_BLISS["U+3774"].append("dish gloves,rubber gloves")
BLISS_TO_UNICODE["sleepy"] = ["U+3775"]
UNICODE_TO_BLISS["U+3775"] = ["sleepy"]
BLISS_TO_UNICODE["costume"] = ["U+3776"]
UNICODE_TO_BLISS["U+3776"] = ["costume"]
BLISS_TO_UNICODE["disguise"] = ["U+3776"]
UNICODE_TO_BLISS["U+3776"].append("disguise")
BLISS_TO_UNICODE["costume,disguise"] = ["U+3776"]
UNICODE_TO_BLISS["U+3776"].append("costume,disguise")
BLISS_TO_UNICODE["make believe"] = ["U+3777"]
UNICODE_TO_BLISS["U+3777"] = ["make believe"]
BLISS_TO_UNICODE["dress up"] = ["U+3778"]
UNICODE_TO_BLISS["U+3778"] = ["dress up"]
BLISS_TO_UNICODE["disguise"].append("U+3778")
UNICODE_TO_BLISS["U+3778"].append("disguise")
BLISS_TO_UNICODE["dress up,disguise"] = ["U+3778"]
UNICODE_TO_BLISS["U+3778"].append("dress up,disguise")
BLISS_TO_UNICODE["caregiver"] = ["U+3779"]
UNICODE_TO_BLISS["U+3779"] = ["caregiver"]
BLISS_TO_UNICODE["protector"] = ["U+3779"]
UNICODE_TO_BLISS["U+3779"].append("protector")
BLISS_TO_UNICODE["defender"] = ["U+3779"]
UNICODE_TO_BLISS["U+3779"].append("defender")
BLISS_TO_UNICODE["caregiver,protector,defender"] = ["U+3779"]
UNICODE_TO_BLISS["U+3779"].append("caregiver,protector,defender")
BLISS_TO_UNICODE["care"] = ["U+377a"]
UNICODE_TO_BLISS["U+377a"] = ["care"]
BLISS_TO_UNICODE["preceding"] = ["U+377b"]
UNICODE_TO_BLISS["U+377b"] = ["preceding"]
BLISS_TO_UNICODE["previous"] = ["U+377b"]
UNICODE_TO_BLISS["U+377b"].append("previous")
BLISS_TO_UNICODE["former"] = ["U+377b"]
UNICODE_TO_BLISS["U+377b"].append("former")
BLISS_TO_UNICODE["earlier"] = ["U+377b"]
UNICODE_TO_BLISS["U+377b"].append("earlier")
BLISS_TO_UNICODE["preceding,previous,former,earlier"] = ["U+377b"]
UNICODE_TO_BLISS["U+377b"].append("preceding,previous,former,earlier")
BLISS_TO_UNICODE["first"] = ["U+377c"]
UNICODE_TO_BLISS["U+377c"] = ["first"]
BLISS_TO_UNICODE["in front of"] = ["U+377d"]
UNICODE_TO_BLISS["U+377d"] = ["in front of"]
BLISS_TO_UNICODE["point of view"] = ["U+377e"]
UNICODE_TO_BLISS["U+377e"] = ["point of view"]
BLISS_TO_UNICODE["position"] = ["U+377f"]
UNICODE_TO_BLISS["U+377f"] = ["position"]
BLISS_TO_UNICODE["boot"] = ["U+3780"]
UNICODE_TO_BLISS["U+3780"] = ["boot"]
BLISS_TO_UNICODE["trunk"].append("U+3780")
UNICODE_TO_BLISS["U+3780"].append("trunk")
BLISS_TO_UNICODE["roof box"] = ["U+3780"]
UNICODE_TO_BLISS["U+3780"].append("roof box")
BLISS_TO_UNICODE["luggage compartment"] = ["U+3780"]
UNICODE_TO_BLISS["U+3780"].append("luggage compartment")
BLISS_TO_UNICODE["boot,trunk,roof box,luggage compartment"] = ["U+3780"]
UNICODE_TO_BLISS["U+3780"].append("boot,trunk,roof box,luggage compartment")
BLISS_TO_UNICODE["ham"] = ["U+35a1"]
UNICODE_TO_BLISS["U+35a1"].append("ham")
BLISS_TO_UNICODE["pork,ham"] = ["U+35a1"]
UNICODE_TO_BLISS["U+35a1"].append("pork,ham")
BLISS_TO_UNICODE["ease"] = ["U+3781"]
UNICODE_TO_BLISS["U+3781"] = ["ease"]
BLISS_TO_UNICODE["easiness"] = ["U+3781"]
UNICODE_TO_BLISS["U+3781"].append("easiness")
BLISS_TO_UNICODE["simplicity"] = ["U+3781"]
UNICODE_TO_BLISS["U+3781"].append("simplicity")
BLISS_TO_UNICODE["ease,easiness,simplicity"] = ["U+3781"]
UNICODE_TO_BLISS["U+3781"].append("ease,easiness,simplicity")
BLISS_TO_UNICODE["landscape design"] = ["U+3782"]
UNICODE_TO_BLISS["U+3782"] = ["landscape design"]
BLISS_TO_UNICODE["design"] = ["U+3783"]
UNICODE_TO_BLISS["U+3783"] = ["design"]
BLISS_TO_UNICODE["hay"] = ["U+3784"]
UNICODE_TO_BLISS["U+3784"] = ["hay"]
BLISS_TO_UNICODE["innocent"] = ["U+3785"]
UNICODE_TO_BLISS["U+3785"] = ["innocent"]
BLISS_TO_UNICODE["not guilty"] = ["U+3785"]
UNICODE_TO_BLISS["U+3785"].append("not guilty")
BLISS_TO_UNICODE["innocent,not guilty"] = ["U+3785"]
UNICODE_TO_BLISS["U+3785"].append("innocent,not guilty")
BLISS_TO_UNICODE["innocence"] = ["U+3786"]
UNICODE_TO_BLISS["U+3786"] = ["innocence"]
BLISS_TO_UNICODE["prison"] = ["U+3787"]
UNICODE_TO_BLISS["U+3787"] = ["prison"]
BLISS_TO_UNICODE["jail"] = ["U+3787"]
UNICODE_TO_BLISS["U+3787"].append("jail")
BLISS_TO_UNICODE["prison,jail"] = ["U+3787"]
UNICODE_TO_BLISS["U+3787"].append("prison,jail")
BLISS_TO_UNICODE["barred window"] = ["U+3788"]
UNICODE_TO_BLISS["U+3788"] = ["barred window"]
BLISS_TO_UNICODE["hat"] = ["U+3789"]
UNICODE_TO_BLISS["U+3789"] = ["hat"]
BLISS_TO_UNICODE["cap"] = ["U+3789"]
UNICODE_TO_BLISS["U+3789"].append("cap")
BLISS_TO_UNICODE["hood"] = ["U+3789"]
UNICODE_TO_BLISS["U+3789"].append("hood")
BLISS_TO_UNICODE["hat,cap,hood"] = ["U+3789"]
UNICODE_TO_BLISS["U+3789"].append("hat,cap,hood")
BLISS_TO_UNICODE["Good morning"] = ["U+378a"]
UNICODE_TO_BLISS["U+378a"] = ["Good morning"]
BLISS_TO_UNICODE["goodbye"] = ["U+378b"]
UNICODE_TO_BLISS["U+378b"] = ["goodbye"]
BLISS_TO_UNICODE["hello"] = ["U+378c"]
UNICODE_TO_BLISS["U+378c"] = ["hello"]
BLISS_TO_UNICODE["at one's destination"] = ["U+378d"]
UNICODE_TO_BLISS["U+378d"] = ["at one's destination"]
BLISS_TO_UNICODE["there"].append("U+378d")
UNICODE_TO_BLISS["U+378d"].append("there")
BLISS_TO_UNICODE["at one's destination,there"] = ["U+378d"]
UNICODE_TO_BLISS["U+378d"].append("at one's destination,there")
BLISS_TO_UNICODE["scrotum"] = ["U+378e"]
UNICODE_TO_BLISS["U+378e"] = ["scrotum"]
BLISS_TO_UNICODE["testicle"] = ["U+378f"]
UNICODE_TO_BLISS["U+378f"] = ["testicle"]
BLISS_TO_UNICODE["sweet"] = ["U+3790"]
UNICODE_TO_BLISS["U+3790"] = ["sweet"]
BLISS_TO_UNICODE["confection"] = ["U+3790"]
UNICODE_TO_BLISS["U+3790"].append("confection")
BLISS_TO_UNICODE["sweet,confection"] = ["U+3790"]
UNICODE_TO_BLISS["U+3790"].append("sweet,confection")
BLISS_TO_UNICODE["disagreement"] = ["U+3791"]
UNICODE_TO_BLISS["U+3791"] = ["disagreement"]
BLISS_TO_UNICODE["discord"] = ["U+3791"]
UNICODE_TO_BLISS["U+3791"].append("discord")
BLISS_TO_UNICODE["disagreement,discord"] = ["U+3791"]
UNICODE_TO_BLISS["U+3791"].append("disagreement,discord")
BLISS_TO_UNICODE["possible"] = ["U+3792"]
UNICODE_TO_BLISS["U+3792"] = ["possible"]
BLISS_TO_UNICODE["possibility"] = ["U+3793"]
UNICODE_TO_BLISS["U+3793"] = ["possibility"]
BLISS_TO_UNICODE["maybe"] = ["U+3794"]
UNICODE_TO_BLISS["U+3794"] = ["maybe"]
BLISS_TO_UNICODE["perhaps"] = ["U+3794"]
UNICODE_TO_BLISS["U+3794"].append("perhaps")
BLISS_TO_UNICODE["possibly"] = ["U+3794"]
UNICODE_TO_BLISS["U+3794"].append("possibly")
BLISS_TO_UNICODE["maybe,perhaps,possibly"] = ["U+3794"]
UNICODE_TO_BLISS["U+3794"].append("maybe,perhaps,possibly")
BLISS_TO_UNICODE["fetus"] = ["U+3795"]
UNICODE_TO_BLISS["U+3795"] = ["fetus"]
BLISS_TO_UNICODE["shadow"] = ["U+3796"]
UNICODE_TO_BLISS["U+3796"] = ["shadow"]
BLISS_TO_UNICODE["shade"] = ["U+3796"]
UNICODE_TO_BLISS["U+3796"].append("shade")
BLISS_TO_UNICODE["shadow,shade"] = ["U+3796"]
UNICODE_TO_BLISS["U+3796"].append("shadow,shade")
BLISS_TO_UNICODE["shape"] = ["U+3797"]
UNICODE_TO_BLISS["U+3797"] = ["shape"]
BLISS_TO_UNICODE["ruin"] = ["U+3798"]
UNICODE_TO_BLISS["U+3798"] = ["ruin"]
BLISS_TO_UNICODE["wreck"] = ["U+3798"]
UNICODE_TO_BLISS["U+3798"].append("wreck")
BLISS_TO_UNICODE["wreckage"] = ["U+3798"]
UNICODE_TO_BLISS["U+3798"].append("wreckage")
BLISS_TO_UNICODE["ruin,wreck,wreckage"] = ["U+3798"]
UNICODE_TO_BLISS["U+3798"].append("ruin,wreck,wreckage")
BLISS_TO_UNICODE["destroyed"] = ["U+3799"]
UNICODE_TO_BLISS["U+3799"] = ["destroyed"]
BLISS_TO_UNICODE["church ruin"] = ["U+379a"]
UNICODE_TO_BLISS["U+379a"] = ["church ruin"]
BLISS_TO_UNICODE["temple ruin"] = ["U+379a"]
UNICODE_TO_BLISS["U+379a"].append("temple ruin")
BLISS_TO_UNICODE["wreck"].append("U+379a")
UNICODE_TO_BLISS["U+379a"].append("wreck")
BLISS_TO_UNICODE["wreckage"].append("U+379a")
UNICODE_TO_BLISS["U+379a"].append("wreckage")
BLISS_TO_UNICODE["temple"] = ["U+379a"]
UNICODE_TO_BLISS["U+379a"].append("temple")
BLISS_TO_UNICODE["mosque)"] = ["U+379a"]
UNICODE_TO_BLISS["U+379a"].append("mosque)")
BLISS_TO_UNICODE["church ruin,temple ruin,wreck,wreckage"] = ["U+379a"]
UNICODE_TO_BLISS["U+379a"].append("church ruin,temple ruin,wreck,wreckage")
BLISS_TO_UNICODE["church"] = ["U+379b"]
UNICODE_TO_BLISS["U+379b"] = ["church"]
BLISS_TO_UNICODE["mosque"] = ["U+379c"]
UNICODE_TO_BLISS["U+379c"] = ["mosque"]
BLISS_TO_UNICODE["wreck,wreckage"] = ["U+3798"]
UNICODE_TO_BLISS["U+3798"].append("wreck,wreckage")
BLISS_TO_UNICODE["sliced"] = ["U+379d"]
UNICODE_TO_BLISS["U+379d"] = ["sliced"]
BLISS_TO_UNICODE["slice"] = ["U+379e"]
UNICODE_TO_BLISS["U+379e"] = ["slice"]
BLISS_TO_UNICODE["feeding tube"] = ["U+379f"]
UNICODE_TO_BLISS["U+379f"] = ["feeding tube"]
BLISS_TO_UNICODE["medical tube"] = ["U+37a0"]
UNICODE_TO_BLISS["U+37a0"] = ["medical tube"]
BLISS_TO_UNICODE["catheter"] = ["U+37a1"]
UNICODE_TO_BLISS["U+37a1"] = ["catheter"]
BLISS_TO_UNICODE["cannula"] = ["U+37a2"]
UNICODE_TO_BLISS["U+37a2"] = ["cannula"]
BLISS_TO_UNICODE["pavement"] = ["U+37a3"]
UNICODE_TO_BLISS["U+37a3"] = ["pavement"]
BLISS_TO_UNICODE["sidewalk"] = ["U+37a3"]
UNICODE_TO_BLISS["U+37a3"].append("sidewalk")
BLISS_TO_UNICODE["pavement,sidewalk"] = ["U+37a3"]
UNICODE_TO_BLISS["U+37a3"].append("pavement,sidewalk")
BLISS_TO_UNICODE["steps"].append("U+36b4")
UNICODE_TO_BLISS["U+36b4"].append("steps")
BLISS_TO_UNICODE["stairs,steps"] = ["U+36b4"]
UNICODE_TO_BLISS["U+36b4"].append("stairs,steps")
BLISS_TO_UNICODE["opposite meaning"] = ["U+37a4"]
UNICODE_TO_BLISS["U+37a4"] = ["opposite meaning"]
BLISS_TO_UNICODE["opposite of"] = ["U+37a4"]
UNICODE_TO_BLISS["U+37a4"].append("opposite of")
BLISS_TO_UNICODE["opposite"].append("U+37a4")
UNICODE_TO_BLISS["U+37a4"].append("opposite")
BLISS_TO_UNICODE["opposite meaning,opposite of,opposite"] = ["U+37a4"]
UNICODE_TO_BLISS["U+37a4"].append("opposite meaning,opposite of,opposite")
BLISS_TO_UNICODE["combination of up and down"] = ["U+37a5"]
UNICODE_TO_BLISS["U+37a5"] = ["combination of up and down"]
BLISS_TO_UNICODE["even number"] = ["U+37a6"]
UNICODE_TO_BLISS["U+37a6"] = ["even number"]
BLISS_TO_UNICODE["Swedish"] = ["U+37a7"]
UNICODE_TO_BLISS["U+37a7"] = ["Swedish"]
BLISS_TO_UNICODE["class"] = ["U+37a8"]
UNICODE_TO_BLISS["U+37a8"] = ["class"]
BLISS_TO_UNICODE["correct"] = ["U+37a9"]
UNICODE_TO_BLISS["U+37a9"] = ["correct"]
BLISS_TO_UNICODE["accurate"] = ["U+37a9"]
UNICODE_TO_BLISS["U+37a9"].append("accurate")
BLISS_TO_UNICODE["good"].append("U+37a9")
UNICODE_TO_BLISS["U+37a9"].append("good")
BLISS_TO_UNICODE["right"].append("U+37a9")
UNICODE_TO_BLISS["U+37a9"].append("right")
BLISS_TO_UNICODE["correct,accurate,good,right"] = ["U+37a9"]
UNICODE_TO_BLISS["U+37a9"].append("correct,accurate,good,right")
BLISS_TO_UNICODE["positive"] = ["U+37aa"]
UNICODE_TO_BLISS["U+37aa"] = ["positive"]
BLISS_TO_UNICODE["good"].append("U+32c8")
UNICODE_TO_BLISS["U+32c8"].append("good")
BLISS_TO_UNICODE["right"].append("U+32c8")
UNICODE_TO_BLISS["U+32c8"].append("right")
BLISS_TO_UNICODE["moral,good,right"] = ["U+32c8"]
UNICODE_TO_BLISS["U+32c8"].append("moral,good,right")
BLISS_TO_UNICODE["good conscience"] = ["U+37ab"]
UNICODE_TO_BLISS["U+37ab"] = ["good conscience"]
BLISS_TO_UNICODE["old"] = ["U+37ac"]
UNICODE_TO_BLISS["U+37ac"] = ["old"]
BLISS_TO_UNICODE["elderly"] = ["U+37ac"]
UNICODE_TO_BLISS["U+37ac"].append("elderly")
BLISS_TO_UNICODE["old,elderly"] = ["U+37ac"]
UNICODE_TO_BLISS["U+37ac"].append("old,elderly")
BLISS_TO_UNICODE["young"] = ["U+37ad"]
UNICODE_TO_BLISS["U+37ad"] = ["young"]
BLISS_TO_UNICODE["people"] = ["U+37ae"]
UNICODE_TO_BLISS["U+37ae"] = ["people"]
BLISS_TO_UNICODE["tribe"] = ["U+37ae"]
UNICODE_TO_BLISS["U+37ae"].append("tribe")
BLISS_TO_UNICODE["clan"] = ["U+37ae"]
UNICODE_TO_BLISS["U+37ae"].append("clan")
BLISS_TO_UNICODE["folk"] = ["U+37ae"]
UNICODE_TO_BLISS["U+37ae"].append("folk")
BLISS_TO_UNICODE["people,tribe,clan,folk"] = ["U+37ae"]
UNICODE_TO_BLISS["U+37ae"].append("people,tribe,clan,folk")
BLISS_TO_UNICODE["view of life"] = ["U+37af"]
UNICODE_TO_BLISS["U+37af"] = ["view of life"]
BLISS_TO_UNICODE["go ashore"] = ["U+37b0"]
UNICODE_TO_BLISS["U+37b0"] = ["go ashore"]
BLISS_TO_UNICODE["debarkation"] = ["U+37b1"]
UNICODE_TO_BLISS["U+37b1"] = ["debarkation"]
BLISS_TO_UNICODE["disembarkation"] = ["U+37b2"]
UNICODE_TO_BLISS["U+37b2"] = ["disembarkation"]
BLISS_TO_UNICODE["rice noodle"] = ["U+37b3"]
UNICODE_TO_BLISS["U+37b3"] = ["rice noodle"]
BLISS_TO_UNICODE["rice flour"] = ["U+37b4"]
UNICODE_TO_BLISS["U+37b4"] = ["rice flour"]
BLISS_TO_UNICODE["elbow pad"] = ["U+37b5"]
UNICODE_TO_BLISS["U+37b5"] = ["elbow pad"]
BLISS_TO_UNICODE["trombone"] = ["U+37b6"]
UNICODE_TO_BLISS["U+37b6"] = ["trombone"]
BLISS_TO_UNICODE["brass instrument"] = ["U+37b7"]
UNICODE_TO_BLISS["U+37b7"] = ["brass instrument"]
BLISS_TO_UNICODE["religious leader"] = ["U+37b8"]
UNICODE_TO_BLISS["U+37b8"] = ["religious leader"]
BLISS_TO_UNICODE["leader"] = ["U+37b9"]
UNICODE_TO_BLISS["U+37b9"] = ["leader"]
BLISS_TO_UNICODE["harassment"] = ["U+37ba"]
UNICODE_TO_BLISS["U+37ba"] = ["harassment"]
BLISS_TO_UNICODE["Snork Maiden"] = ["U+37bb"]
UNICODE_TO_BLISS["U+37bb"] = ["Snork Maiden"]
BLISS_TO_UNICODE["sociology"] = ["U+37bc"]
UNICODE_TO_BLISS["U+37bc"] = ["sociology"]
BLISS_TO_UNICODE["okra"] = ["U+37bd"]
UNICODE_TO_BLISS["U+37bd"] = ["okra"]
BLISS_TO_UNICODE["lady's finger"] = ["U+37bd"]
UNICODE_TO_BLISS["U+37bd"].append("lady's finger")
BLISS_TO_UNICODE["okra,lady's finger"] = ["U+37bd"]
UNICODE_TO_BLISS["U+37bd"].append("okra,lady's finger")
BLISS_TO_UNICODE["to exchange"] = ["U+37be"]
UNICODE_TO_BLISS["U+37be"] = ["to exchange"]
BLISS_TO_UNICODE["in order to"] = ["U+371f"]
UNICODE_TO_BLISS["U+371f"].append("in order to")
BLISS_TO_UNICODE["base"].append("U+3364")
UNICODE_TO_BLISS["U+3364"].append("base")
BLISS_TO_UNICODE["bottom,base"] = ["U+3364"]
UNICODE_TO_BLISS["U+3364"].append("bottom,base")
BLISS_TO_UNICODE["bottom"].append("U+33eb")
UNICODE_TO_BLISS["U+33eb"].append("bottom")
BLISS_TO_UNICODE["bum"] = ["U+33eb"]
UNICODE_TO_BLISS["U+33eb"].append("bum")
BLISS_TO_UNICODE["rear"] = ["U+33eb"]
UNICODE_TO_BLISS["U+33eb"].append("rear")
BLISS_TO_UNICODE["ass"] = ["U+33eb"]
UNICODE_TO_BLISS["U+33eb"].append("ass")
BLISS_TO_UNICODE["buttocks,bottom,bum,rear,ass"] = ["U+33eb"]
UNICODE_TO_BLISS["U+33eb"].append("buttocks,bottom,bum,rear,ass")
BLISS_TO_UNICODE["standing person"] = ["U+37bf"]
UNICODE_TO_BLISS["U+37bf"] = ["standing person"]
BLISS_TO_UNICODE["bottom of a thing"] = ["U+3364"]
UNICODE_TO_BLISS["U+3364"].append("bottom of a thing")
BLISS_TO_UNICODE["bottom,bottom of a thing"] = ["U+3364"]
UNICODE_TO_BLISS["U+3364"].append("bottom,bottom of a thing")
BLISS_TO_UNICODE["practise"] = ["U+37c0"]
UNICODE_TO_BLISS["U+37c0"] = ["practise"]
BLISS_TO_UNICODE["practice"] = ["U+37c0"]
UNICODE_TO_BLISS["U+37c0"].append("practice")
BLISS_TO_UNICODE["drill"] = ["U+37c0"]
UNICODE_TO_BLISS["U+37c0"].append("drill")
BLISS_TO_UNICODE["exercise"] = ["U+37c0"]
UNICODE_TO_BLISS["U+37c0"].append("exercise")
BLISS_TO_UNICODE["rehearse"] = ["U+37c0"]
UNICODE_TO_BLISS["U+37c0"].append("rehearse")
BLISS_TO_UNICODE["practise,practice,drill,exercise,rehearse"] = ["U+37c0"]
UNICODE_TO_BLISS["U+37c0"].append("practise,practice,drill,exercise,rehearse")
BLISS_TO_UNICODE["fox"] = ["U+37c1"]
UNICODE_TO_BLISS["U+37c1"] = ["fox"]
BLISS_TO_UNICODE["canine"] = ["U+37c2"]
UNICODE_TO_BLISS["U+37c2"] = ["canine"]
BLISS_TO_UNICODE["correct thinking"] = ["U+37c3"]
UNICODE_TO_BLISS["U+37c3"] = ["correct thinking"]
BLISS_TO_UNICODE["creative"] = ["U+37c4"]
UNICODE_TO_BLISS["U+37c4"] = ["creative"]
BLISS_TO_UNICODE["e mail address"] = ["U+37c5"]
UNICODE_TO_BLISS["U+37c5"] = ["e mail address"]
BLISS_TO_UNICODE["email address"] = ["U+37c5"]
UNICODE_TO_BLISS["U+37c5"].append("email address")
BLISS_TO_UNICODE["e-mail address,email address"] = ["U+37c5"]
UNICODE_TO_BLISS["U+37c5"].append("e-mail address,email address")
BLISS_TO_UNICODE["e-mail"] = ["U+37c6"]
UNICODE_TO_BLISS["U+37c6"] = ["e-mail"]
BLISS_TO_UNICODE["tornado"] = ["U+37c7"]
UNICODE_TO_BLISS["U+37c7"] = ["tornado"]
BLISS_TO_UNICODE["gale"] = ["U+37c8"]
UNICODE_TO_BLISS["U+37c8"] = ["gale"]
BLISS_TO_UNICODE["apartment"] = ["U+37c9"]
UNICODE_TO_BLISS["U+37c9"] = ["apartment"]
BLISS_TO_UNICODE["flat"] = ["U+37c9"]
UNICODE_TO_BLISS["U+37c9"].append("flat")
BLISS_TO_UNICODE["unit"].append("U+37c9")
UNICODE_TO_BLISS["U+37c9"].append("unit")
BLISS_TO_UNICODE["apartment,flat,unit"] = ["U+37c9"]
UNICODE_TO_BLISS["U+37c9"].append("apartment,flat,unit")
BLISS_TO_UNICODE["sprout"] = ["U+37ca"]
UNICODE_TO_BLISS["U+37ca"] = ["sprout"]
BLISS_TO_UNICODE["germinate"] = ["U+37ca"]
UNICODE_TO_BLISS["U+37ca"].append("germinate")
BLISS_TO_UNICODE["sprout,germinate"] = ["U+37ca"]
UNICODE_TO_BLISS["U+37ca"].append("sprout,germinate")
BLISS_TO_UNICODE["start"] = ["U+37cb"]
UNICODE_TO_BLISS["U+37cb"] = ["start"]
BLISS_TO_UNICODE["growth"] = ["U+37cc"]
UNICODE_TO_BLISS["U+37cc"] = ["growth"]
BLISS_TO_UNICODE["growing"] = ["U+37cd"]
UNICODE_TO_BLISS["U+37cd"] = ["growing"]
BLISS_TO_UNICODE["trampoline"] = ["U+37ce"]
UNICODE_TO_BLISS["U+37ce"] = ["trampoline"]
BLISS_TO_UNICODE["to jump"] = ["U+37cf"]
UNICODE_TO_BLISS["U+37cf"] = ["to jump"]
BLISS_TO_UNICODE["tumble drier"] = ["U+37d0"]
UNICODE_TO_BLISS["U+37d0"] = ["tumble drier"]
BLISS_TO_UNICODE["tumble dryer"] = ["U+37d0"]
UNICODE_TO_BLISS["U+37d0"].append("tumble dryer")
BLISS_TO_UNICODE["tumble-drier,tumble-dryer"] = ["U+37d0"]
UNICODE_TO_BLISS["U+37d0"].append("tumble-drier,tumble-dryer")
BLISS_TO_UNICODE["rice pudding"] = ["U+37d1"]
UNICODE_TO_BLISS["U+37d1"] = ["rice pudding"]
BLISS_TO_UNICODE["rice porridge"] = ["U+37d1"]
UNICODE_TO_BLISS["U+37d1"].append("rice porridge")
BLISS_TO_UNICODE["rice pudding,rice porridge"] = ["U+37d1"]
UNICODE_TO_BLISS["U+37d1"].append("rice pudding,rice porridge")
BLISS_TO_UNICODE["pudding"] = ["U+37d2"]
UNICODE_TO_BLISS["U+37d2"] = ["pudding"]
BLISS_TO_UNICODE["gutter"] = ["U+37d3"]
UNICODE_TO_BLISS["U+37d3"] = ["gutter"]
BLISS_TO_UNICODE["eaves trough"] = ["U+37d3"]
UNICODE_TO_BLISS["U+37d3"].append("eaves trough")
BLISS_TO_UNICODE["gutter,eaves trough"] = ["U+37d3"]
UNICODE_TO_BLISS["U+37d3"].append("gutter,eaves trough")
BLISS_TO_UNICODE["eaves"] = ["U+37d4"]
UNICODE_TO_BLISS["U+37d4"] = ["eaves"]
BLISS_TO_UNICODE["mountain berry"] = ["U+37d5"]
UNICODE_TO_BLISS["U+37d5"] = ["mountain berry"]
BLISS_TO_UNICODE["cowberry"] = ["U+37d5"]
UNICODE_TO_BLISS["U+37d5"].append("cowberry")
BLISS_TO_UNICODE["lingonberry"] = ["U+37d5"]
UNICODE_TO_BLISS["U+37d5"].append("lingonberry")
BLISS_TO_UNICODE["mountain berry,cowberry,lingonberry"] = ["U+37d5"]
UNICODE_TO_BLISS["U+37d5"].append("mountain berry,cowberry,lingonberry")
BLISS_TO_UNICODE["fruit juice"] = ["U+37d6"]
UNICODE_TO_BLISS["U+37d6"] = ["fruit juice"]
BLISS_TO_UNICODE["juice"] = ["U+37d6"]
UNICODE_TO_BLISS["U+37d6"].append("juice")
BLISS_TO_UNICODE["fruit juice,juice"] = ["U+37d6"]
UNICODE_TO_BLISS["U+37d6"].append("fruit juice,juice")
BLISS_TO_UNICODE["drink"] = ["U+37d7"]
UNICODE_TO_BLISS["U+37d7"] = ["drink"]
BLISS_TO_UNICODE["Valentine"] = ["U+37d8"]
UNICODE_TO_BLISS["U+37d8"] = ["Valentine"]
BLISS_TO_UNICODE["hoof pick"] = ["U+37d9"]
UNICODE_TO_BLISS["U+37d9"] = ["hoof pick"]
BLISS_TO_UNICODE["hoof"] = ["U+37da"]
UNICODE_TO_BLISS["U+37da"] = ["hoof"]
BLISS_TO_UNICODE["storeroom"] = ["U+37db"]
UNICODE_TO_BLISS["U+37db"] = ["storeroom"]
BLISS_TO_UNICODE["seaplane"] = ["U+37dc"]
UNICODE_TO_BLISS["U+37dc"] = ["seaplane"]
BLISS_TO_UNICODE["roti"] = ["U+37dd"]
UNICODE_TO_BLISS["U+37dd"] = ["roti"]
BLISS_TO_UNICODE["chapati"] = ["U+37dd"]
UNICODE_TO_BLISS["U+37dd"].append("chapati")
BLISS_TO_UNICODE["flatbread"] = ["U+37dd"]
UNICODE_TO_BLISS["U+37dd"].append("flatbread")
BLISS_TO_UNICODE["roti,chapati,flatbread"] = ["U+37dd"]
UNICODE_TO_BLISS["U+37dd"].append("roti,chapati,flatbread")
BLISS_TO_UNICODE["disc"] = ["U+37de"]
UNICODE_TO_BLISS["U+37de"] = ["disc"]
BLISS_TO_UNICODE["yen"] = ["U+37df"]
UNICODE_TO_BLISS["U+37df"] = ["yen"]
BLISS_TO_UNICODE["international symbol for Japanese yen"] = ["U+37e0"]
UNICODE_TO_BLISS["U+37e0"] = ["international symbol for Japanese yen"]
BLISS_TO_UNICODE["teeter totter"] = ["U+352d"]
UNICODE_TO_BLISS["U+352d"].append("teeter totter")
BLISS_TO_UNICODE["teeter board"] = ["U+352d"]
UNICODE_TO_BLISS["U+352d"].append("teeter board")
BLISS_TO_UNICODE["seesaw,teeter-totter,teeter board"] = ["U+352d"]
UNICODE_TO_BLISS["U+352d"].append("seesaw,teeter-totter,teeter board")
BLISS_TO_UNICODE["Scotland"] = ["U+37e1"]
UNICODE_TO_BLISS["U+37e1"] = ["Scotland"]
BLISS_TO_UNICODE["sow"] = ["U+37e2"]
UNICODE_TO_BLISS["U+37e2"] = ["sow"]
BLISS_TO_UNICODE["Christian event"] = ["U+37e3"]
UNICODE_TO_BLISS["U+37e3"] = ["Christian event"]
BLISS_TO_UNICODE["fabric"] = ["U+3223"]
UNICODE_TO_BLISS["U+3223"].append("fabric")
BLISS_TO_UNICODE["material"].append("U+3223")
UNICODE_TO_BLISS["U+3223"].append("material")
BLISS_TO_UNICODE["textile"] = ["U+3223"]
UNICODE_TO_BLISS["U+3223"].append("textile")
BLISS_TO_UNICODE["net"] = ["U+3223"]
UNICODE_TO_BLISS["U+3223"].append("net")
BLISS_TO_UNICODE["cloth,fabric,material,textile,net"] = ["U+3223"]
UNICODE_TO_BLISS["U+3223"].append("cloth,fabric,material,textile,net")
BLISS_TO_UNICODE["Woden"] = ["U+37e4"]
UNICODE_TO_BLISS["U+37e4"] = ["Woden"]
BLISS_TO_UNICODE["Nordic God"] = ["U+37e5"]
UNICODE_TO_BLISS["U+37e5"] = ["Nordic God"]
BLISS_TO_UNICODE["watch tower"] = ["U+37e6"]
UNICODE_TO_BLISS["U+37e6"] = ["watch tower"]
BLISS_TO_UNICODE["observation tower"] = ["U+37e6"]
UNICODE_TO_BLISS["U+37e6"].append("observation tower")
BLISS_TO_UNICODE["watch tower,observation tower"] = ["U+37e6"]
UNICODE_TO_BLISS["U+37e6"].append("watch tower,observation tower")
BLISS_TO_UNICODE["observation"] = ["U+37e7"]
UNICODE_TO_BLISS["U+37e7"] = ["observation"]
BLISS_TO_UNICODE["happy"] = ["U+37e8"]
UNICODE_TO_BLISS["U+37e8"] = ["happy"]
BLISS_TO_UNICODE["glad"] = ["U+37e8"]
UNICODE_TO_BLISS["U+37e8"].append("glad")
BLISS_TO_UNICODE["gladly"] = ["U+37e8"]
UNICODE_TO_BLISS["U+37e8"].append("gladly")
BLISS_TO_UNICODE["happily"] = ["U+37e8"]
UNICODE_TO_BLISS["U+37e8"].append("happily")
BLISS_TO_UNICODE["happy,glad,gladly,happily"] = ["U+37e8"]
UNICODE_TO_BLISS["U+37e8"].append("happy,glad,gladly,happily")
BLISS_TO_UNICODE["ice hockey"] = ["U+37e9"]
UNICODE_TO_BLISS["U+37e9"] = ["ice hockey"]
BLISS_TO_UNICODE["sport stick and puck"] = ["U+37ea"]
UNICODE_TO_BLISS["U+37ea"] = ["sport stick and puck"]
BLISS_TO_UNICODE["oppressed"] = ["U+37eb"]
UNICODE_TO_BLISS["U+37eb"] = ["oppressed"]
BLISS_TO_UNICODE["unfree"] = ["U+37eb"]
UNICODE_TO_BLISS["U+37eb"].append("unfree")
BLISS_TO_UNICODE["oppressed,unfree"] = ["U+37eb"]
UNICODE_TO_BLISS["U+37eb"].append("oppressed,unfree")
BLISS_TO_UNICODE["oppression"] = ["U+37ec"]
UNICODE_TO_BLISS["U+37ec"] = ["oppression"]
BLISS_TO_UNICODE["captivity"] = ["U+37ed"]
UNICODE_TO_BLISS["U+37ed"] = ["captivity"]
BLISS_TO_UNICODE["slavery"] = ["U+37ee"]
UNICODE_TO_BLISS["U+37ee"] = ["slavery"]
BLISS_TO_UNICODE["offer"] = ["U+3233"]
UNICODE_TO_BLISS["U+3233"].append("offer")
BLISS_TO_UNICODE["provide"] = ["U+3233"]
UNICODE_TO_BLISS["U+3233"].append("provide")
BLISS_TO_UNICODE["give,offer,provide"] = ["U+3233"]
UNICODE_TO_BLISS["U+3233"].append("give,offer,provide")
BLISS_TO_UNICODE["giving"] = ["U+37ef"]
UNICODE_TO_BLISS["U+37ef"] = ["giving"]
BLISS_TO_UNICODE["sacrifice"] = ["U+3233"]
UNICODE_TO_BLISS["U+3233"].append("sacrifice")
BLISS_TO_UNICODE["offer,sacrifice"] = ["U+3233"]
UNICODE_TO_BLISS["U+3233"].append("offer,sacrifice")
BLISS_TO_UNICODE["shoot"] = ["U+37f0"]
UNICODE_TO_BLISS["U+37f0"] = ["shoot"]
BLISS_TO_UNICODE["tape recorder"] = ["U+37f1"]
UNICODE_TO_BLISS["U+37f1"] = ["tape recorder"]
BLISS_TO_UNICODE["to reproduce"] = ["U+37f2"]
UNICODE_TO_BLISS["U+37f2"] = ["to reproduce"]
BLISS_TO_UNICODE["congratulations"] = ["U+37f3"]
UNICODE_TO_BLISS["U+37f3"] = ["congratulations"]
BLISS_TO_UNICODE["best of luck"] = ["U+37f3"]
UNICODE_TO_BLISS["U+37f3"].append("best of luck")
BLISS_TO_UNICODE["mazel tov"] = ["U+37f3"]
UNICODE_TO_BLISS["U+37f3"].append("mazel tov")
BLISS_TO_UNICODE["congratulations,best of luck,mazel tov"] = ["U+37f3"]
UNICODE_TO_BLISS["U+37f3"].append("congratulations,best of luck,mazel tov")
BLISS_TO_UNICODE["luck"] = ["U+37f4"]
UNICODE_TO_BLISS["U+37f4"] = ["luck"]
BLISS_TO_UNICODE["in"] = ["U+37f5"]
UNICODE_TO_BLISS["U+37f5"] = ["in"]
BLISS_TO_UNICODE["inside"].append("U+37f5")
UNICODE_TO_BLISS["U+37f5"].append("inside")
BLISS_TO_UNICODE["interior"] = ["U+37f5"]
UNICODE_TO_BLISS["U+37f5"].append("interior")
BLISS_TO_UNICODE["internal"] = ["U+37f5"]
UNICODE_TO_BLISS["U+37f5"].append("internal")
BLISS_TO_UNICODE["in,inside,interior,internal"] = ["U+37f5"]
UNICODE_TO_BLISS["U+37f5"].append("in,inside,interior,internal")
BLISS_TO_UNICODE["tie"] = ["U+37f6"]
UNICODE_TO_BLISS["U+37f6"] = ["tie"]
BLISS_TO_UNICODE["bind together"] = ["U+37f6"]
UNICODE_TO_BLISS["U+37f6"].append("bind together")
BLISS_TO_UNICODE["lash"] = ["U+37f6"]
UNICODE_TO_BLISS["U+37f6"].append("lash")
BLISS_TO_UNICODE["tie,bind together,lash"] = ["U+37f6"]
UNICODE_TO_BLISS["U+37f6"].append("tie,bind together,lash")
BLISS_TO_UNICODE["knot"] = ["U+37f7"]
UNICODE_TO_BLISS["U+37f7"] = ["knot"]
BLISS_TO_UNICODE["powerful"] = ["U+37f9"]
UNICODE_TO_BLISS["U+37f9"] = ["powerful"]
BLISS_TO_UNICODE["mighty"] = ["U+37f9"]
UNICODE_TO_BLISS["U+37f9"].append("mighty")
BLISS_TO_UNICODE["powerful,mighty"] = ["U+37f9"]
UNICODE_TO_BLISS["U+37f9"].append("powerful,mighty")
BLISS_TO_UNICODE["passenger"] = ["U+37fa"]
UNICODE_TO_BLISS["U+37fa"] = ["passenger"]
BLISS_TO_UNICODE["to ride"] = ["U+37fb"]
UNICODE_TO_BLISS["U+37fb"] = ["to ride"]
BLISS_TO_UNICODE["adopt"] = ["U+37fc"]
UNICODE_TO_BLISS["U+37fc"] = ["adopt"]
BLISS_TO_UNICODE["adoption"] = ["U+37fd"]
UNICODE_TO_BLISS["U+37fd"] = ["adoption"]
BLISS_TO_UNICODE["kart racing"] = ["U+37fe"]
UNICODE_TO_BLISS["U+37fe"] = ["kart racing"]
BLISS_TO_UNICODE["karting"] = ["U+37fe"]
UNICODE_TO_BLISS["U+37fe"].append("karting")
BLISS_TO_UNICODE["go karting"] = ["U+37fe"]
UNICODE_TO_BLISS["U+37fe"].append("go karting")
BLISS_TO_UNICODE["kart racing,karting,go-karting"] = ["U+37fe"]
UNICODE_TO_BLISS["U+37fe"].append("kart racing,karting,go-karting")
BLISS_TO_UNICODE["anyone"] = ["U+37ff"]
UNICODE_TO_BLISS["U+37ff"] = ["anyone"]
BLISS_TO_UNICODE["anybody"] = ["U+37ff"]
UNICODE_TO_BLISS["U+37ff"].append("anybody")
BLISS_TO_UNICODE["somebody"] = ["U+37ff"]
UNICODE_TO_BLISS["U+37ff"].append("somebody")
BLISS_TO_UNICODE["someone"] = ["U+37ff"]
UNICODE_TO_BLISS["U+37ff"].append("someone")
BLISS_TO_UNICODE["anyone,anybody,somebody,someone"] = ["U+37ff"]
UNICODE_TO_BLISS["U+37ff"].append("anyone,anybody,somebody,someone")
BLISS_TO_UNICODE["am"] = ["U+32a4"]
UNICODE_TO_BLISS["U+32a4"].append("am")
BLISS_TO_UNICODE["are"] = ["U+32a4"]
UNICODE_TO_BLISS["U+32a4"].append("are")
BLISS_TO_UNICODE["is"] = ["U+32a4"]
UNICODE_TO_BLISS["U+32a4"].append("is")
BLISS_TO_UNICODE["exist"] = ["U+32a4"]
UNICODE_TO_BLISS["U+32a4"].append("exist")
BLISS_TO_UNICODE["be,am,are,is,exist"] = ["U+32a4"]
UNICODE_TO_BLISS["U+32a4"].append("be,am,are,is,exist")
BLISS_TO_UNICODE["to live"] = ["U+3800"]
UNICODE_TO_BLISS["U+3800"] = ["to live"]
BLISS_TO_UNICODE["Sif"] = ["U+3801"]
UNICODE_TO_BLISS["U+3801"] = ["Sif"]
BLISS_TO_UNICODE["Thor"] = ["U+3802"]
UNICODE_TO_BLISS["U+3802"] = ["Thor"]
BLISS_TO_UNICODE["occupational therapy room"] = ["U+3803"]
UNICODE_TO_BLISS["U+3803"] = ["occupational therapy room"]
BLISS_TO_UNICODE["crutches"] = ["U+3804"]
UNICODE_TO_BLISS["U+3804"] = ["crutches"]
BLISS_TO_UNICODE["tools"] = ["U+3805"]
UNICODE_TO_BLISS["U+3805"] = ["tools"]
BLISS_TO_UNICODE["medical"] = ["U+3806"]
UNICODE_TO_BLISS["U+3806"] = ["medical"]
BLISS_TO_UNICODE["relay"] = ["U+3807"]
UNICODE_TO_BLISS["U+3807"] = ["relay"]
BLISS_TO_UNICODE["to stop"] = ["U+3808"]
UNICODE_TO_BLISS["U+3808"] = ["to stop"]
BLISS_TO_UNICODE["to start"] = ["U+3809"]
UNICODE_TO_BLISS["U+3809"] = ["to start"]
BLISS_TO_UNICODE["dotted"] = ["U+380a"]
UNICODE_TO_BLISS["U+380a"] = ["dotted"]
BLISS_TO_UNICODE["storey"] = ["U+339c"]
UNICODE_TO_BLISS["U+339c"].append("storey")
BLISS_TO_UNICODE["level"] = ["U+339c"]
UNICODE_TO_BLISS["U+339c"].append("level")
BLISS_TO_UNICODE["etage"] = ["U+339c"]
UNICODE_TO_BLISS["U+339c"].append("etage")
BLISS_TO_UNICODE["floor,storey,level,etage"] = ["U+339c"]
UNICODE_TO_BLISS["U+339c"].append("floor,storey,level,etage")
BLISS_TO_UNICODE["42"] = ["U+380b"]
UNICODE_TO_BLISS["U+380b"] = ["42"]
BLISS_TO_UNICODE["glacier"] = ["U+380c"]
UNICODE_TO_BLISS["U+380c"] = ["glacier"]
BLISS_TO_UNICODE["actor"] = ["U+380d"]
UNICODE_TO_BLISS["U+380d"] = ["actor"]
BLISS_TO_UNICODE["flood"] = ["U+380e"]
UNICODE_TO_BLISS["U+380e"] = ["flood"]
BLISS_TO_UNICODE["water on ground"] = ["U+380f"]
UNICODE_TO_BLISS["U+380f"] = ["water on ground"]
BLISS_TO_UNICODE["republic"] = ["U+3810"]
UNICODE_TO_BLISS["U+3810"] = ["republic"]
BLISS_TO_UNICODE["crown princess"] = ["U+3811"]
UNICODE_TO_BLISS["U+3811"] = ["crown princess"]
BLISS_TO_UNICODE["princess"] = ["U+3812"]
UNICODE_TO_BLISS["U+3812"] = ["princess"]
BLISS_TO_UNICODE["odour"].append("U+3728")
UNICODE_TO_BLISS["U+3728"].append("odour")
BLISS_TO_UNICODE["smell,odour"] = ["U+3728"]
UNICODE_TO_BLISS["U+3728"].append("smell,odour")
BLISS_TO_UNICODE["sense of smell"] = ["U+3728"]
UNICODE_TO_BLISS["U+3728"].append("sense of smell")
BLISS_TO_UNICODE["olfaction"] = ["U+3728"]
UNICODE_TO_BLISS["U+3728"].append("olfaction")
BLISS_TO_UNICODE["smell,sense of smell,olfaction"] = ["U+3728"]
UNICODE_TO_BLISS["U+3728"].append("smell,sense of smell,olfaction")
BLISS_TO_UNICODE["leek"] = ["U+3813"]
UNICODE_TO_BLISS["U+3813"] = ["leek"]
BLISS_TO_UNICODE["steamship"] = ["U+3814"]
UNICODE_TO_BLISS["U+3814"] = ["steamship"]
BLISS_TO_UNICODE["height"] = ["U+3815"]
UNICODE_TO_BLISS["U+3815"] = ["height"]
BLISS_TO_UNICODE["tallness"] = ["U+3815"]
UNICODE_TO_BLISS["U+3815"].append("tallness")
BLISS_TO_UNICODE["height,tallness"] = ["U+3815"]
UNICODE_TO_BLISS["U+3815"].append("height,tallness")
BLISS_TO_UNICODE["two horizontal reference lines"] = ["U+3816"]
UNICODE_TO_BLISS["U+3816"] = ["two horizontal reference lines"]
BLISS_TO_UNICODE["taxi driver"] = ["U+3817"]
UNICODE_TO_BLISS["U+3817"] = ["taxi driver"]
BLISS_TO_UNICODE["cab driver"] = ["U+3817"]
UNICODE_TO_BLISS["U+3817"].append("cab driver")
BLISS_TO_UNICODE["taxi driver,cab driver"] = ["U+3817"]
UNICODE_TO_BLISS["U+3817"].append("taxi driver,cab driver")
BLISS_TO_UNICODE["taxi"] = ["U+3818"]
UNICODE_TO_BLISS["U+3818"] = ["taxi"]
BLISS_TO_UNICODE["lettuce"] = ["U+3819"]
UNICODE_TO_BLISS["U+3819"] = ["lettuce"]
BLISS_TO_UNICODE["leafy vegetable"].append("U+3819")
UNICODE_TO_BLISS["U+3819"].append("leafy vegetable")
BLISS_TO_UNICODE["lettuce,leafy vegetable"] = ["U+3819"]
UNICODE_TO_BLISS["U+3819"].append("lettuce,leafy vegetable")
BLISS_TO_UNICODE["outline of leaves"] = ["U+381a"]
UNICODE_TO_BLISS["U+381a"] = ["outline of leaves"]
BLISS_TO_UNICODE["attached"] = ["U+368c"]
UNICODE_TO_BLISS["U+368c"].append("attached")
BLISS_TO_UNICODE["appended"] = ["U+368c"]
UNICODE_TO_BLISS["U+368c"].append("appended")
BLISS_TO_UNICODE["fastened"] = ["U+368c"]
UNICODE_TO_BLISS["U+368c"].append("fastened")
BLISS_TO_UNICODE["joined"] = ["U+368c"]
UNICODE_TO_BLISS["U+368c"].append("joined")
BLISS_TO_UNICODE["together,attached,appended,fastened,joined"] = ["U+368c"]
UNICODE_TO_BLISS["U+368c"].append("together,attached,appended,fastened,joined")
BLISS_TO_UNICODE["electric circuit"] = ["U+381b"]
UNICODE_TO_BLISS["U+381b"] = ["electric circuit"]
BLISS_TO_UNICODE["tahini"] = ["U+381c"]
UNICODE_TO_BLISS["U+381c"] = ["tahini"]
BLISS_TO_UNICODE["sesame seed spread"] = ["U+381c"]
UNICODE_TO_BLISS["U+381c"].append("sesame seed spread")
BLISS_TO_UNICODE["tahini,sesame seed spread"] = ["U+381c"]
UNICODE_TO_BLISS["U+381c"].append("tahini,sesame seed spread")
BLISS_TO_UNICODE["white"] = ["U+381d"]
UNICODE_TO_BLISS["U+381d"] = ["white"]
BLISS_TO_UNICODE["mummy"] = ["U+381e"]
UNICODE_TO_BLISS["U+381e"] = ["mummy"]
BLISS_TO_UNICODE["dead"] = ["U+381f"]
UNICODE_TO_BLISS["U+381f"] = ["dead"]
BLISS_TO_UNICODE["all powerful"] = ["U+3821"]
UNICODE_TO_BLISS["U+3821"] = ["all powerful"]
BLISS_TO_UNICODE["ability"] = ["U+3822"]
UNICODE_TO_BLISS["U+3822"] = ["ability"]
BLISS_TO_UNICODE["symbol looks like a clock face"] = ["U+3823"]
UNICODE_TO_BLISS["U+3823"] = ["symbol looks like a clock face"]
BLISS_TO_UNICODE[" suggesting time"] = ["U+3824"]
UNICODE_TO_BLISS["U+3824"] = [" suggesting time"]
BLISS_TO_UNICODE["shove"] = ["U+3241"]
UNICODE_TO_BLISS["U+3241"].append("shove")
BLISS_TO_UNICODE["push,shove"] = ["U+3241"]
UNICODE_TO_BLISS["U+3241"].append("push,shove")
BLISS_TO_UNICODE["pushing"] = ["U+3241"]
UNICODE_TO_BLISS["U+3241"].append("pushing")
BLISS_TO_UNICODE["push,pushing"] = ["U+3241"]
UNICODE_TO_BLISS["U+3241"].append("push,pushing")
BLISS_TO_UNICODE["quantity"] = ["U+3825"]
UNICODE_TO_BLISS["U+3825"] = ["quantity"]
BLISS_TO_UNICODE["multitude"] = ["U+3826"]
UNICODE_TO_BLISS["U+3826"] = ["multitude"]
BLISS_TO_UNICODE["wind turbine"] = ["U+3827"]
UNICODE_TO_BLISS["U+3827"] = ["wind turbine"]
BLISS_TO_UNICODE["windmill"] = ["U+3828"]
UNICODE_TO_BLISS["U+3828"] = ["windmill"]
BLISS_TO_UNICODE["peacock"] = ["U+3829"]
UNICODE_TO_BLISS["U+3829"] = ["peacock"]
BLISS_TO_UNICODE["chain"] = ["U+382a"]
UNICODE_TO_BLISS["U+382a"] = ["chain"]
BLISS_TO_UNICODE["alligator"] = ["U+382b"]
UNICODE_TO_BLISS["U+382b"] = ["alligator"]
BLISS_TO_UNICODE["crocodile"] = ["U+382b"]
UNICODE_TO_BLISS["U+382b"].append("crocodile")
BLISS_TO_UNICODE["alligator,crocodile"] = ["U+382b"]
UNICODE_TO_BLISS["U+382b"].append("alligator,crocodile")
BLISS_TO_UNICODE["avalanche"] = ["U+382c"]
UNICODE_TO_BLISS["U+382c"] = ["avalanche"]
BLISS_TO_UNICODE["skiing"] = ["U+382d"]
UNICODE_TO_BLISS["U+382d"] = ["skiing"]
BLISS_TO_UNICODE["skis"] = ["U+382e"]
UNICODE_TO_BLISS["U+382e"] = ["skis"]
BLISS_TO_UNICODE["dogsled sport"] = ["U+382f"]
UNICODE_TO_BLISS["U+382f"] = ["dogsled sport"]
BLISS_TO_UNICODE["dogsled racing"] = ["U+382f"]
UNICODE_TO_BLISS["U+382f"].append("dogsled racing")
BLISS_TO_UNICODE["dogsled sport,dogsled racing"] = ["U+382f"]
UNICODE_TO_BLISS["U+382f"].append("dogsled sport,dogsled racing")
BLISS_TO_UNICODE["dog sled"] = ["U+3830"]
UNICODE_TO_BLISS["U+3830"] = ["dog sled"]
BLISS_TO_UNICODE["seat"].append("U+34e7")
UNICODE_TO_BLISS["U+34e7"].append("seat")
BLISS_TO_UNICODE["chair,seat"] = ["U+34e7"]
UNICODE_TO_BLISS["U+34e7"].append("chair,seat")
BLISS_TO_UNICODE["business idea"] = ["U+3831"]
UNICODE_TO_BLISS["U+3831"] = ["business idea"]
BLISS_TO_UNICODE["ballet"] = ["U+3832"]
UNICODE_TO_BLISS["U+3832"] = ["ballet"]
BLISS_TO_UNICODE["crater"] = ["U+3833"]
UNICODE_TO_BLISS["U+3833"] = ["crater"]
BLISS_TO_UNICODE["sunscreen"] = ["U+3834"]
UNICODE_TO_BLISS["U+3834"] = ["sunscreen"]
BLISS_TO_UNICODE["sunblock"] = ["U+3834"]
UNICODE_TO_BLISS["U+3834"].append("sunblock")
BLISS_TO_UNICODE["sun lotion"] = ["U+3834"]
UNICODE_TO_BLISS["U+3834"].append("sun lotion")
BLISS_TO_UNICODE["sunscreen,sunblock,sun lotion"] = ["U+3834"]
UNICODE_TO_BLISS["U+3834"].append("sunscreen,sunblock,sun lotion")
BLISS_TO_UNICODE["persevere"] = ["U+3835"]
UNICODE_TO_BLISS["U+3835"] = ["persevere"]
BLISS_TO_UNICODE["perseverance"] = ["U+3836"]
UNICODE_TO_BLISS["U+3836"] = ["perseverance"]
BLISS_TO_UNICODE["icing"] = ["U+3837"]
UNICODE_TO_BLISS["U+3837"] = ["icing"]
BLISS_TO_UNICODE["powdered sugar"] = ["U+3838"]
UNICODE_TO_BLISS["U+3838"] = ["powdered sugar"]
BLISS_TO_UNICODE["icing sugar"] = ["U+3839"]
UNICODE_TO_BLISS["U+3839"] = ["icing sugar"]
BLISS_TO_UNICODE["recipe"] = ["U+383a"]
UNICODE_TO_BLISS["U+383a"] = ["recipe"]
BLISS_TO_UNICODE["page"] = ["U+383b"]
UNICODE_TO_BLISS["U+383b"] = ["page"]
BLISS_TO_UNICODE["to prepare food"] = ["U+383c"]
UNICODE_TO_BLISS["U+383c"] = ["to prepare food"]
BLISS_TO_UNICODE["selection"] = ["U+343c"]
UNICODE_TO_BLISS["U+343c"].append("selection")
BLISS_TO_UNICODE["election"] = ["U+343c"]
UNICODE_TO_BLISS["U+343c"].append("election")
BLISS_TO_UNICODE["choice,selection,election"] = ["U+343c"]
UNICODE_TO_BLISS["U+343c"].append("choice,selection,election")
BLISS_TO_UNICODE["comparative more"] = ["U+383d"]
UNICODE_TO_BLISS["U+383d"] = ["comparative more"]
BLISS_TO_UNICODE["embark"] = ["U+383e"]
UNICODE_TO_BLISS["U+383e"] = ["embark"]
BLISS_TO_UNICODE["board"].append("U+383e")
UNICODE_TO_BLISS["U+383e"].append("board")
BLISS_TO_UNICODE["embark,board"] = ["U+383e"]
UNICODE_TO_BLISS["U+383e"].append("embark,board")
BLISS_TO_UNICODE["to enter"] = ["U+383f"]
UNICODE_TO_BLISS["U+383f"] = ["to enter"]
BLISS_TO_UNICODE["mourn"] = ["U+3840"]
UNICODE_TO_BLISS["U+3840"] = ["mourn"]
BLISS_TO_UNICODE["sadness"] = ["U+3841"]
UNICODE_TO_BLISS["U+3841"] = ["sadness"]
BLISS_TO_UNICODE["loss"] = ["U+3842"]
UNICODE_TO_BLISS["U+3842"] = ["loss"]
BLISS_TO_UNICODE["minute"] = ["U+3843"]
UNICODE_TO_BLISS["U+3843"] = ["minute"]
BLISS_TO_UNICODE["apostrophe"] = ["U+3844"]
UNICODE_TO_BLISS["U+3844"] = ["apostrophe"]
BLISS_TO_UNICODE[" used in astronomy to indicate a minute"] = ["U+3845"]
UNICODE_TO_BLISS["U+3845"] = [" used in astronomy to indicate a minute"]
BLISS_TO_UNICODE["digital processing"] = ["U+3846"]
UNICODE_TO_BLISS["U+3846"] = ["digital processing"]
BLISS_TO_UNICODE["artificial intelligence"] = ["U+3846"]
UNICODE_TO_BLISS["U+3846"].append("artificial intelligence")
BLISS_TO_UNICODE["AI"] = ["U+3846"]
UNICODE_TO_BLISS["U+3846"].append("AI")
BLISS_TO_UNICODE["digital processing,artificial intelligence,AI"] = ["U+3846"]
UNICODE_TO_BLISS["U+3846"].append("digital processing,artificial intelligence,AI")
BLISS_TO_UNICODE["digits"] = ["U+3847"]
UNICODE_TO_BLISS["U+3847"] = ["digits"]
BLISS_TO_UNICODE["young animal"] = ["U+3848"]
UNICODE_TO_BLISS["U+3848"] = ["young animal"]
BLISS_TO_UNICODE["tricycle"] = ["U+3849"]
UNICODE_TO_BLISS["U+3849"] = ["tricycle"]
BLISS_TO_UNICODE["crack"] = ["U+34c8"]
UNICODE_TO_BLISS["U+34c8"].append("crack")
BLISS_TO_UNICODE["fracture"] = ["U+34c8"]
UNICODE_TO_BLISS["U+34c8"].append("fracture")
BLISS_TO_UNICODE["tear"] = ["U+34c8"]
UNICODE_TO_BLISS["U+34c8"].append("tear")
BLISS_TO_UNICODE["break,crack,fracture,tear"] = ["U+34c8"]
UNICODE_TO_BLISS["U+34c8"].append("break,crack,fracture,tear")
BLISS_TO_UNICODE["teardrop"] = ["U+34c8"]
UNICODE_TO_BLISS["U+34c8"].append("teardrop")
BLISS_TO_UNICODE["tear,teardrop"] = ["U+34c8"]
UNICODE_TO_BLISS["U+34c8"].append("tear,teardrop")
BLISS_TO_UNICODE["drop"] = ["U+384a"]
UNICODE_TO_BLISS["U+384a"] = ["drop"]
BLISS_TO_UNICODE["Kali"] = ["U+384b"]
UNICODE_TO_BLISS["U+384b"] = ["Kali"]
BLISS_TO_UNICODE["black"] = ["U+384c"]
UNICODE_TO_BLISS["U+384c"] = ["black"]
BLISS_TO_UNICODE["bottle nipple"] = ["U+384d"]
UNICODE_TO_BLISS["U+384d"] = ["bottle nipple"]
BLISS_TO_UNICODE["teat"] = ["U+384d"]
UNICODE_TO_BLISS["U+384d"].append("teat")
BLISS_TO_UNICODE["bottle nipple,teat"] = ["U+384d"]
UNICODE_TO_BLISS["U+384d"].append("bottle nipple,teat")
BLISS_TO_UNICODE["bottleneck"] = ["U+384e"]
UNICODE_TO_BLISS["U+384e"] = ["bottleneck"]
BLISS_TO_UNICODE["bottle opening"] = ["U+384f"]
UNICODE_TO_BLISS["U+384f"] = ["bottle opening"]
BLISS_TO_UNICODE["go"] = ["U+3850"]
UNICODE_TO_BLISS["U+3850"] = ["go"]
BLISS_TO_UNICODE["depart"] = ["U+3850"]
UNICODE_TO_BLISS["U+3850"].append("depart")
BLISS_TO_UNICODE["leave"] = ["U+3850"]
UNICODE_TO_BLISS["U+3850"].append("leave")
BLISS_TO_UNICODE["go,depart,leave"] = ["U+3850"]
UNICODE_TO_BLISS["U+3850"].append("go,depart,leave")
BLISS_TO_UNICODE["departure"] = ["U+3851"]
UNICODE_TO_BLISS["U+3851"] = ["departure"]
BLISS_TO_UNICODE["subway"] = ["U+3852"]
UNICODE_TO_BLISS["U+3852"] = ["subway"]
BLISS_TO_UNICODE["metro"] = ["U+3852"]
UNICODE_TO_BLISS["U+3852"].append("metro")
BLISS_TO_UNICODE["underground"] = ["U+3852"]
UNICODE_TO_BLISS["U+3852"].append("underground")
BLISS_TO_UNICODE["tube"].append("U+3852")
UNICODE_TO_BLISS["U+3852"].append("tube")
BLISS_TO_UNICODE["subway,metro,underground,tube"] = ["U+3852"]
UNICODE_TO_BLISS["U+3852"].append("subway,metro,underground,tube")
BLISS_TO_UNICODE["tunnel"] = ["U+3853"]
UNICODE_TO_BLISS["U+3853"] = ["tunnel"]
BLISS_TO_UNICODE["subway"].append("U+3853")
UNICODE_TO_BLISS["U+3853"].append("subway")
BLISS_TO_UNICODE["underpass"] = ["U+3853"]
UNICODE_TO_BLISS["U+3853"].append("underpass")
BLISS_TO_UNICODE["tunnel,subway,underpass"] = ["U+3853"]
UNICODE_TO_BLISS["U+3853"].append("tunnel,subway,underpass")
BLISS_TO_UNICODE["team"] = ["U+3854"]
UNICODE_TO_BLISS["U+3854"] = ["team"]
BLISS_TO_UNICODE["bonfire"] = ["U+3855"]
UNICODE_TO_BLISS["U+3855"] = ["bonfire"]
BLISS_TO_UNICODE["barbeque"] = ["U+3855"]
UNICODE_TO_BLISS["U+3855"].append("barbeque")
BLISS_TO_UNICODE["campfire"] = ["U+3855"]
UNICODE_TO_BLISS["U+3855"].append("campfire")
BLISS_TO_UNICODE["bonfire,barbeque,campfire"] = ["U+3855"]
UNICODE_TO_BLISS["U+3855"].append("bonfire,barbeque,campfire")
BLISS_TO_UNICODE["rat"] = ["U+3856"]
UNICODE_TO_BLISS["U+3856"] = ["rat"]
BLISS_TO_UNICODE["rodent"].append("U+3856")
UNICODE_TO_BLISS["U+3856"].append("rodent")
BLISS_TO_UNICODE["gnawer"] = ["U+3856"]
UNICODE_TO_BLISS["U+3856"].append("gnawer")
BLISS_TO_UNICODE["gnawing animal"] = ["U+3856"]
UNICODE_TO_BLISS["U+3856"].append("gnawing animal")
BLISS_TO_UNICODE["rat,rodent,gnawer,gnawing animal"] = ["U+3856"]
UNICODE_TO_BLISS["U+3856"].append("rat,rodent,gnawer,gnawing animal")
BLISS_TO_UNICODE["meadow"] = ["U+34ac"]
UNICODE_TO_BLISS["U+34ac"].append("meadow")
BLISS_TO_UNICODE["lawn,meadow"] = ["U+34ac"]
UNICODE_TO_BLISS["U+34ac"].append("lawn,meadow")
BLISS_TO_UNICODE["attic"] = ["U+3857"]
UNICODE_TO_BLISS["U+3857"] = ["attic"]
BLISS_TO_UNICODE["fingernail"] = ["U+3858"]
UNICODE_TO_BLISS["U+3858"] = ["fingernail"]
BLISS_TO_UNICODE["nail"].append("U+3858")
UNICODE_TO_BLISS["U+3858"].append("nail")
BLISS_TO_UNICODE["fingernail,nail"] = ["U+3858"]
UNICODE_TO_BLISS["U+3858"].append("fingernail,nail")
BLISS_TO_UNICODE["farness"] = ["U+3859"]
UNICODE_TO_BLISS["U+3859"] = ["farness"]
BLISS_TO_UNICODE["remoteness"] = ["U+3859"]
UNICODE_TO_BLISS["U+3859"].append("remoteness")
BLISS_TO_UNICODE["farawayness"] = ["U+3859"]
UNICODE_TO_BLISS["U+3859"].append("farawayness")
BLISS_TO_UNICODE["farness,remoteness,farawayness"] = ["U+3859"]
UNICODE_TO_BLISS["U+3859"].append("farness,remoteness,farawayness")
BLISS_TO_UNICODE["sign"] = ["U+385a"]
UNICODE_TO_BLISS["U+385a"] = ["sign"]
BLISS_TO_UNICODE["advertisement"] = ["U+385a"]
UNICODE_TO_BLISS["U+385a"].append("advertisement")
BLISS_TO_UNICODE["sign,advertisement"] = ["U+385a"]
UNICODE_TO_BLISS["U+385a"].append("sign,advertisement")
BLISS_TO_UNICODE["attention"] = ["U+385b"]
UNICODE_TO_BLISS["U+385b"] = ["attention"]
BLISS_TO_UNICODE["sign language"] = ["U+385c"]
UNICODE_TO_BLISS["U+385c"] = ["sign language"]
BLISS_TO_UNICODE["signal"] = ["U+385a"]
UNICODE_TO_BLISS["U+385a"].append("signal")
BLISS_TO_UNICODE["sign,signal"] = ["U+385a"]
UNICODE_TO_BLISS["U+385a"].append("sign,signal")
BLISS_TO_UNICODE["high tide"] = ["U+385d"]
UNICODE_TO_BLISS["U+385d"] = ["high tide"]
BLISS_TO_UNICODE["crescent"] = ["U+385e"]
UNICODE_TO_BLISS["U+385e"] = ["crescent"]
BLISS_TO_UNICODE["crescent shape"] = ["U+385f"]
UNICODE_TO_BLISS["U+385f"] = ["crescent shape"]
BLISS_TO_UNICODE["hot dog"] = ["U+3860"]
UNICODE_TO_BLISS["U+3860"] = ["hot dog"]
BLISS_TO_UNICODE["frankfurter"] = ["U+3860"]
UNICODE_TO_BLISS["U+3860"].append("frankfurter")
BLISS_TO_UNICODE["hot dog,frankfurter"] = ["U+3860"]
UNICODE_TO_BLISS["U+3860"].append("hot dog,frankfurter")
BLISS_TO_UNICODE["long"] = ["U+3861"]
UNICODE_TO_BLISS["U+3861"] = ["long"]
BLISS_TO_UNICODE["sausage"] = ["U+3862"]
UNICODE_TO_BLISS["U+3862"] = ["sausage"]
BLISS_TO_UNICODE["frankfurter"].append("U+3862")
UNICODE_TO_BLISS["U+3862"].append("frankfurter")
BLISS_TO_UNICODE["hotdog"] = ["U+3862"]
UNICODE_TO_BLISS["U+3862"].append("hotdog")
BLISS_TO_UNICODE["hot dog"].append("U+3862")
UNICODE_TO_BLISS["U+3862"].append("hot dog")
BLISS_TO_UNICODE["sausage,frankfurter,hotdog,hot dog"] = ["U+3862"]
UNICODE_TO_BLISS["U+3862"].append("sausage,frankfurter,hotdog,hot dog")
BLISS_TO_UNICODE["parachuting"] = ["U+3863"]
UNICODE_TO_BLISS["U+3863"] = ["parachuting"]
BLISS_TO_UNICODE["parachute"] = ["U+3864"]
UNICODE_TO_BLISS["U+3864"] = ["parachute"]
BLISS_TO_UNICODE["headset"] = ["U+3865"]
UNICODE_TO_BLISS["U+3865"] = ["headset"]
BLISS_TO_UNICODE["earmuffs"] = ["U+3866"]
UNICODE_TO_BLISS["U+3866"] = ["earmuffs"]
BLISS_TO_UNICODE["thaw"] = ["U+3867"]
UNICODE_TO_BLISS["U+3867"] = ["thaw"]
BLISS_TO_UNICODE["melt"].append("U+3867")
UNICODE_TO_BLISS["U+3867"].append("melt")
BLISS_TO_UNICODE["thaw,melt"] = ["U+3867"]
UNICODE_TO_BLISS["U+3867"].append("thaw,melt")
BLISS_TO_UNICODE["thawing"] = ["U+3868"]
UNICODE_TO_BLISS["U+3868"] = ["thawing"]
BLISS_TO_UNICODE["melting"] = ["U+3869"]
UNICODE_TO_BLISS["U+3869"] = ["melting"]
BLISS_TO_UNICODE["current"] = ["U+386a"]
UNICODE_TO_BLISS["U+386a"] = ["current"]
BLISS_TO_UNICODE["stream"] = ["U+3239"]
UNICODE_TO_BLISS["U+3239"].append("stream")
BLISS_TO_UNICODE["current"].append("U+3239")
UNICODE_TO_BLISS["U+3239"].append("current")
BLISS_TO_UNICODE["river,stream,current"] = ["U+3239"]
UNICODE_TO_BLISS["U+3239"].append("river,stream,current")
BLISS_TO_UNICODE["geography"] = ["U+386b"]
UNICODE_TO_BLISS["U+386b"] = ["geography"]
BLISS_TO_UNICODE["body of learning"] = ["U+386c"]
UNICODE_TO_BLISS["U+386c"] = ["body of learning"]
BLISS_TO_UNICODE["shield"] = ["U+33a9"]
UNICODE_TO_BLISS["U+33a9"].append("shield")
BLISS_TO_UNICODE["badge,shield"] = ["U+33a9"]
UNICODE_TO_BLISS["U+33a9"].append("badge,shield")
BLISS_TO_UNICODE["jury"] = ["U+386d"]
UNICODE_TO_BLISS["U+386d"] = ["jury"]
BLISS_TO_UNICODE["peer"] = ["U+386e"]
UNICODE_TO_BLISS["U+386e"] = ["peer"]
BLISS_TO_UNICODE["legal"] = ["U+386f"]
UNICODE_TO_BLISS["U+386f"] = ["legal"]
BLISS_TO_UNICODE["funeral"] = ["U+3870"]
UNICODE_TO_BLISS["U+3870"] = ["funeral"]
BLISS_TO_UNICODE["empty"] = ["U+3871"]
UNICODE_TO_BLISS["U+3871"] = ["empty"]
BLISS_TO_UNICODE["evacuate"] = ["U+3871"]
UNICODE_TO_BLISS["U+3871"].append("evacuate")
BLISS_TO_UNICODE["throw away"] = ["U+3871"]
UNICODE_TO_BLISS["U+3871"].append("throw away")
BLISS_TO_UNICODE["void"] = ["U+3871"]
UNICODE_TO_BLISS["U+3871"].append("void")
BLISS_TO_UNICODE["empty,evacuate,throw away,void"] = ["U+3871"]
UNICODE_TO_BLISS["U+3871"].append("empty,evacuate,throw away,void")
BLISS_TO_UNICODE["emptying"] = ["U+3872"]
UNICODE_TO_BLISS["U+3872"] = ["emptying"]
BLISS_TO_UNICODE["voidance"] = ["U+3873"]
UNICODE_TO_BLISS["U+3873"] = ["voidance"]
BLISS_TO_UNICODE["evacuation"] = ["U+3874"]
UNICODE_TO_BLISS["U+3874"] = ["evacuation"]
BLISS_TO_UNICODE["understanding"] = ["U+3875"]
UNICODE_TO_BLISS["U+3875"] = ["understanding"]
BLISS_TO_UNICODE["comprehension"] = ["U+3875"]
UNICODE_TO_BLISS["U+3875"].append("comprehension")
BLISS_TO_UNICODE["understanding,comprehension"] = ["U+3875"]
UNICODE_TO_BLISS["U+3875"].append("understanding,comprehension")
BLISS_TO_UNICODE["magnetism"] = ["U+3876"]
UNICODE_TO_BLISS["U+3876"] = ["magnetism"]
BLISS_TO_UNICODE["metal bar"] = ["U+3877"]
UNICODE_TO_BLISS["U+3877"] = ["metal bar"]
BLISS_TO_UNICODE["pictorgraph of lines of flux"] = ["U+3878"]
UNICODE_TO_BLISS["U+3878"] = ["pictorgraph of lines of flux"]
BLISS_TO_UNICODE["address"] = ["U+3879"]
UNICODE_TO_BLISS["U+3879"] = ["address"]
BLISS_TO_UNICODE["alone"] = ["U+387a"]
UNICODE_TO_BLISS["U+387a"] = ["alone"]
BLISS_TO_UNICODE["just"].append("U+387a")
UNICODE_TO_BLISS["U+387a"].append("just")
BLISS_TO_UNICODE["only"] = ["U+387a"]
UNICODE_TO_BLISS["U+387a"].append("only")
BLISS_TO_UNICODE["solitary"] = ["U+387a"]
UNICODE_TO_BLISS["U+387a"].append("solitary")
BLISS_TO_UNICODE["alone,just,only,solitary"] = ["U+387a"]
UNICODE_TO_BLISS["U+387a"].append("alone,just,only,solitary")
BLISS_TO_UNICODE["to be"] = ["U+387b"]
UNICODE_TO_BLISS["U+387b"] = ["to be"]
BLISS_TO_UNICODE["bus station"] = ["U+387c"]
UNICODE_TO_BLISS["U+387c"] = ["bus station"]
BLISS_TO_UNICODE["queue"] = ["U+34cf"]
UNICODE_TO_BLISS["U+34cf"].append("queue")
BLISS_TO_UNICODE["line,queue"] = ["U+34cf"]
UNICODE_TO_BLISS["U+34cf"].append("line,queue")
BLISS_TO_UNICODE["reclaim"] = ["U+387d"]
UNICODE_TO_BLISS["U+387d"] = ["reclaim"]
BLISS_TO_UNICODE["to dry"] = ["U+387e"]
UNICODE_TO_BLISS["U+387e"] = ["to dry"]
BLISS_TO_UNICODE["land"] = ["U+387f"]
UNICODE_TO_BLISS["U+387f"] = ["land"]
BLISS_TO_UNICODE["canine"].append("U+330c")
UNICODE_TO_BLISS["U+330c"].append("canine")
BLISS_TO_UNICODE["canid"] = ["U+330c"]
UNICODE_TO_BLISS["U+330c"].append("canid")
BLISS_TO_UNICODE["dog,canine"] = ["U+330c"]
UNICODE_TO_BLISS["U+330c"].append("dog,canine")
BLISS_TO_UNICODE["curved line"] = ["U+3880"]
UNICODE_TO_BLISS["U+3880"] = ["curved line"]
BLISS_TO_UNICODE["fruit yogurt"] = ["U+3881"]
UNICODE_TO_BLISS["U+3881"] = ["fruit yogurt"]
BLISS_TO_UNICODE["fruit yoghurt"] = ["U+3881"]
UNICODE_TO_BLISS["U+3881"].append("fruit yoghurt")
BLISS_TO_UNICODE["fruit yogurt,fruit yoghurt"] = ["U+3881"]
UNICODE_TO_BLISS["U+3881"].append("fruit yogurt,fruit yoghurt")
BLISS_TO_UNICODE["affection"] = ["U+34c6"]
UNICODE_TO_BLISS["U+34c6"].append("affection")
BLISS_TO_UNICODE["love,affection"] = ["U+34c6"]
UNICODE_TO_BLISS["U+34c6"].append("love,affection")
BLISS_TO_UNICODE["radish"] = ["U+3882"]
UNICODE_TO_BLISS["U+3882"] = ["radish"]
BLISS_TO_UNICODE["August"] = ["U+3883"]
UNICODE_TO_BLISS["U+3883"] = ["August"]
BLISS_TO_UNICODE["8"] = ["U+3884"]
UNICODE_TO_BLISS["U+3884"] = ["8"]
BLISS_TO_UNICODE["employed"] = ["U+3885"]
UNICODE_TO_BLISS["U+3885"] = ["employed"]
BLISS_TO_UNICODE["working"] = ["U+3885"]
UNICODE_TO_BLISS["U+3885"].append("working")
BLISS_TO_UNICODE["employed,working"] = ["U+3885"]
UNICODE_TO_BLISS["U+3885"].append("employed,working")
BLISS_TO_UNICODE["angry"] = ["U+3886"]
UNICODE_TO_BLISS["U+3886"] = ["angry"]
BLISS_TO_UNICODE["angrily"] = ["U+3886"]
UNICODE_TO_BLISS["U+3886"].append("angrily")
BLISS_TO_UNICODE["mad"] = ["U+3886"]
UNICODE_TO_BLISS["U+3886"].append("mad")
BLISS_TO_UNICODE["angry,angrily,mad"] = ["U+3886"]
UNICODE_TO_BLISS["U+3886"].append("angry,angrily,mad")
BLISS_TO_UNICODE["wicket"] = ["U+3887"]
UNICODE_TO_BLISS["U+3887"] = ["wicket"]
BLISS_TO_UNICODE["lumber"] = ["U+357d"]
UNICODE_TO_BLISS["U+357d"].append("lumber")
BLISS_TO_UNICODE["timber"] = ["U+357d"]
UNICODE_TO_BLISS["U+357d"].append("timber")
BLISS_TO_UNICODE["wood,lumber,timber"] = ["U+357d"]
UNICODE_TO_BLISS["U+357d"].append("wood,lumber,timber")
BLISS_TO_UNICODE["prosecutor"] = ["U+3888"]
UNICODE_TO_BLISS["U+3888"] = ["prosecutor"]
BLISS_TO_UNICODE["legal person"] = ["U+3889"]
UNICODE_TO_BLISS["U+3889"] = ["legal person"]
BLISS_TO_UNICODE["to accuse"] = ["U+388a"]
UNICODE_TO_BLISS["U+388a"] = ["to accuse"]
BLISS_TO_UNICODE["dichotomy"] = ["U+388b"]
UNICODE_TO_BLISS["U+388b"] = ["dichotomy"]
BLISS_TO_UNICODE["duality"] = ["U+388b"]
UNICODE_TO_BLISS["U+388b"].append("duality")
BLISS_TO_UNICODE["dichotomy,duality"] = ["U+388b"]
UNICODE_TO_BLISS["U+388b"].append("dichotomy,duality")
BLISS_TO_UNICODE["clitoris"] = ["U+388c"]
UNICODE_TO_BLISS["U+388c"] = ["clitoris"]
BLISS_TO_UNICODE["part of"] = ["U+388d"]
UNICODE_TO_BLISS["U+388d"] = ["part of"]
BLISS_TO_UNICODE["female genitals"] = ["U+388e"]
UNICODE_TO_BLISS["U+388e"] = ["female genitals"]
BLISS_TO_UNICODE["apparent"] = ["U+388f"]
UNICODE_TO_BLISS["U+388f"] = ["apparent"]
BLISS_TO_UNICODE["clear"] = ["U+388f"]
UNICODE_TO_BLISS["U+388f"].append("clear")
BLISS_TO_UNICODE["evident"] = ["U+388f"]
UNICODE_TO_BLISS["U+388f"].append("evident")
BLISS_TO_UNICODE["obvious"] = ["U+388f"]
UNICODE_TO_BLISS["U+388f"].append("obvious")
BLISS_TO_UNICODE["plain"] = ["U+388f"]
UNICODE_TO_BLISS["U+388f"].append("plain")
BLISS_TO_UNICODE["bovine"] = ["U+3494"]
UNICODE_TO_BLISS["U+3494"].append("bovine")
BLISS_TO_UNICODE["ovine"] = ["U+3494"]
UNICODE_TO_BLISS["U+3494"].append("ovine")
BLISS_TO_UNICODE["appendix"] = ["U+3636"]
UNICODE_TO_BLISS["U+3636"].append("appendix")
BLISS_TO_UNICODE["annex"] = ["U+3636"]
UNICODE_TO_BLISS["U+3636"].append("annex")
BLISS_TO_UNICODE["attachment,appendix,annex"] = ["U+3636"]
UNICODE_TO_BLISS["U+3636"].append("attachment,appendix,annex")
BLISS_TO_UNICODE["cecum"] = ["U+3636"]
UNICODE_TO_BLISS["U+3636"].append("cecum")
BLISS_TO_UNICODE["caecum"] = ["U+3636"]
UNICODE_TO_BLISS["U+3636"].append("caecum")
BLISS_TO_UNICODE["appendix,cecum,caecum"] = ["U+3636"]
UNICODE_TO_BLISS["U+3636"].append("appendix,cecum,caecum")
BLISS_TO_UNICODE["intestine"] = ["U+3890"]
UNICODE_TO_BLISS["U+3890"] = ["intestine"]
BLISS_TO_UNICODE["bowel"] = ["U+3891"]
UNICODE_TO_BLISS["U+3891"] = ["bowel"]
BLISS_TO_UNICODE["gut"] = ["U+3892"]
UNICODE_TO_BLISS["U+3892"] = ["gut"]
BLISS_TO_UNICODE["Pope"] = ["U+3893"]
UNICODE_TO_BLISS["U+3893"] = ["Pope"]
BLISS_TO_UNICODE["lumberjack"] = ["U+3894"]
UNICODE_TO_BLISS["U+3894"] = ["lumberjack"]
BLISS_TO_UNICODE["to cut"] = ["U+3895"]
UNICODE_TO_BLISS["U+3895"] = ["to cut"]
BLISS_TO_UNICODE["pretend"].append("U+3777")
UNICODE_TO_BLISS["U+3777"].append("pretend")
BLISS_TO_UNICODE["imaginary"] = ["U+3777"]
UNICODE_TO_BLISS["U+3777"].append("imaginary")
BLISS_TO_UNICODE["make-believe,pretend,imaginary"] = ["U+3777"]
UNICODE_TO_BLISS["U+3777"].append("make-believe,pretend,imaginary")
BLISS_TO_UNICODE["fantasy"] = ["U+3896"]
UNICODE_TO_BLISS["U+3896"] = ["fantasy"]
BLISS_TO_UNICODE["phantasy"] = ["U+3897"]
UNICODE_TO_BLISS["U+3897"] = ["phantasy"]
BLISS_TO_UNICODE["imagination"] = ["U+3898"]
UNICODE_TO_BLISS["U+3898"] = ["imagination"]
BLISS_TO_UNICODE["illusion"] = ["U+3899"]
UNICODE_TO_BLISS["U+3899"] = ["illusion"]
BLISS_TO_UNICODE["make believe"].append("U+3287")
UNICODE_TO_BLISS["U+3287"].append("make believe")
BLISS_TO_UNICODE["pretend,make believe"] = ["U+3287"]
UNICODE_TO_BLISS["U+3287"].append("pretend,make believe")
BLISS_TO_UNICODE["abortion"] = ["U+389a"]
UNICODE_TO_BLISS["U+389a"] = ["abortion"]
BLISS_TO_UNICODE["miscarriage"] = ["U+389b"]
UNICODE_TO_BLISS["U+389b"] = ["miscarriage"]
BLISS_TO_UNICODE["abortion"].append("U+389b")
UNICODE_TO_BLISS["U+389b"].append("abortion")
BLISS_TO_UNICODE["miscarriage,abortion"] = ["U+389b"]
UNICODE_TO_BLISS["U+389b"].append("miscarriage,abortion")
BLISS_TO_UNICODE["to cancel"] = ["U+389c"]
UNICODE_TO_BLISS["U+389c"] = ["to cancel"]
BLISS_TO_UNICODE["believer"] = ["U+389d"]
UNICODE_TO_BLISS["U+389d"] = ["believer"]
BLISS_TO_UNICODE["agreed"] = ["U+389e"]
UNICODE_TO_BLISS["U+389e"] = ["agreed"]
BLISS_TO_UNICODE["in agreement"] = ["U+389e"]
UNICODE_TO_BLISS["U+389e"].append("in agreement")
BLISS_TO_UNICODE["harmonious"] = ["U+389e"]
UNICODE_TO_BLISS["U+389e"].append("harmonious")
BLISS_TO_UNICODE["agreed,in agreement,harmonious"] = ["U+389e"]
UNICODE_TO_BLISS["U+389e"].append("agreed,in agreement,harmonious")
BLISS_TO_UNICODE["financial support"] = ["U+389f"]
UNICODE_TO_BLISS["U+389f"] = ["financial support"]
BLISS_TO_UNICODE["with"] = ["U+38a0"]
UNICODE_TO_BLISS["U+38a0"] = ["with"]
BLISS_TO_UNICODE["meeting and parting"] = ["U+38a1"]
UNICODE_TO_BLISS["U+38a1"] = ["meeting and parting"]
BLISS_TO_UNICODE["meeting"] = ["U+38a2"]
UNICODE_TO_BLISS["U+38a2"] = ["meeting"]
BLISS_TO_UNICODE["encounter"] = ["U+38a3"]
UNICODE_TO_BLISS["U+38a3"] = ["encounter"]
BLISS_TO_UNICODE["parting"] = ["U+38a4"]
UNICODE_TO_BLISS["U+38a4"] = ["parting"]
BLISS_TO_UNICODE["from sky"] = ["U+38a5"]
UNICODE_TO_BLISS["U+38a5"] = ["from sky"]
BLISS_TO_UNICODE["matzo"] = ["U+38a6"]
UNICODE_TO_BLISS["U+38a6"] = ["matzo"]
BLISS_TO_UNICODE["sled"] = ["U+38a7"]
UNICODE_TO_BLISS["U+38a7"] = ["sled"]
BLISS_TO_UNICODE["boules"] = ["U+38a8"]
UNICODE_TO_BLISS["U+38a8"] = ["boules"]
BLISS_TO_UNICODE["ball field"] = ["U+38a9"]
UNICODE_TO_BLISS["U+38a9"] = ["ball field"]
BLISS_TO_UNICODE["winter"] = ["U+38aa"]
UNICODE_TO_BLISS["U+38aa"] = ["winter"]
BLISS_TO_UNICODE["lulav"] = ["U+38ab"]
UNICODE_TO_BLISS["U+38ab"] = ["lulav"]
BLISS_TO_UNICODE["Sukkot"] = ["U+38ac"]
UNICODE_TO_BLISS["U+38ac"] = ["Sukkot"]
BLISS_TO_UNICODE["divided"] = ["U+38ad"]
UNICODE_TO_BLISS["U+38ad"] = ["divided"]
BLISS_TO_UNICODE["file"] = ["U+38ae"]
UNICODE_TO_BLISS["U+38ae"] = ["file"]
BLISS_TO_UNICODE["data file"] = ["U+38ae"]
UNICODE_TO_BLISS["U+38ae"].append("data file")
BLISS_TO_UNICODE["file,data file"] = ["U+38ae"]
UNICODE_TO_BLISS["U+38ae"].append("file,data file")
BLISS_TO_UNICODE["elephant"] = ["U+38af"]
UNICODE_TO_BLISS["U+38af"] = ["elephant"]
BLISS_TO_UNICODE["bracha"] = ["U+38b0"]
UNICODE_TO_BLISS["U+38b0"] = ["bracha"]
BLISS_TO_UNICODE["berakah"] = ["U+38b0"]
UNICODE_TO_BLISS["U+38b0"].append("berakah")
BLISS_TO_UNICODE["prayer"] = ["U+38b0"]
UNICODE_TO_BLISS["U+38b0"].append("prayer")
BLISS_TO_UNICODE["bracha,berakah,prayer"] = ["U+38b0"]
UNICODE_TO_BLISS["U+38b0"].append("bracha,berakah,prayer")
BLISS_TO_UNICODE["laundromat"] = ["U+38b1"]
UNICODE_TO_BLISS["U+38b1"] = ["laundromat"]
BLISS_TO_UNICODE["launderette"] = ["U+38b1"]
UNICODE_TO_BLISS["U+38b1"].append("launderette")
BLISS_TO_UNICODE["laundry"] = ["U+38b1"]
UNICODE_TO_BLISS["U+38b1"].append("laundry")
BLISS_TO_UNICODE["laundromat,launderette,laundry"] = ["U+38b1"]
UNICODE_TO_BLISS["U+38b1"].append("laundromat,launderette,laundry")
BLISS_TO_UNICODE["explorer"] = ["U+38b2"]
UNICODE_TO_BLISS["U+38b2"] = ["explorer"]
BLISS_TO_UNICODE["enquirer"] = ["U+38b2"]
UNICODE_TO_BLISS["U+38b2"].append("enquirer")
BLISS_TO_UNICODE["explorer,enquirer"] = ["U+38b2"]
UNICODE_TO_BLISS["U+38b2"].append("explorer,enquirer")
BLISS_TO_UNICODE["explore"] = ["U+38b3"]
UNICODE_TO_BLISS["U+38b3"] = ["explore"]
BLISS_TO_UNICODE["mark"] = ["U+36fd"]
UNICODE_TO_BLISS["U+36fd"].append("mark")
BLISS_TO_UNICODE["spot,mark"] = ["U+36fd"]
UNICODE_TO_BLISS["U+36fd"].append("spot,mark")
BLISS_TO_UNICODE["bread with fruit"] = ["U+38b4"]
UNICODE_TO_BLISS["U+38b4"] = ["bread with fruit"]
BLISS_TO_UNICODE["data"] = ["U+38b5"]
UNICODE_TO_BLISS["U+38b5"] = ["data"]
BLISS_TO_UNICODE["stress"] = ["U+38b6"]
UNICODE_TO_BLISS["U+38b6"] = ["stress"]
BLISS_TO_UNICODE["table mat"] = ["U+38b7"]
UNICODE_TO_BLISS["U+38b7"] = ["table mat"]
BLISS_TO_UNICODE["placemat"] = ["U+38b7"]
UNICODE_TO_BLISS["U+38b7"].append("placemat")
BLISS_TO_UNICODE["table mat,placemat"] = ["U+38b7"]
UNICODE_TO_BLISS["U+38b7"].append("table mat,placemat")
BLISS_TO_UNICODE["sandbox"] = ["U+38b8"]
UNICODE_TO_BLISS["U+38b8"] = ["sandbox"]
BLISS_TO_UNICODE["sandpit"] = ["U+38b8"]
UNICODE_TO_BLISS["U+38b8"].append("sandpit")
BLISS_TO_UNICODE["sandtray"] = ["U+38b8"]
UNICODE_TO_BLISS["U+38b8"].append("sandtray")
BLISS_TO_UNICODE["sandbox,sandpit,sandtray"] = ["U+38b8"]
UNICODE_TO_BLISS["U+38b8"].append("sandbox,sandpit,sandtray")
BLISS_TO_UNICODE["sand"] = ["U+38b9"]
UNICODE_TO_BLISS["U+38b9"] = ["sand"]
BLISS_TO_UNICODE["so"].append("U+3354")
UNICODE_TO_BLISS["U+3354"].append("so")
BLISS_TO_UNICODE["later"] = ["U+3354"]
UNICODE_TO_BLISS["U+3354"].append("later")
BLISS_TO_UNICODE["then,so,later"] = ["U+3354"]
UNICODE_TO_BLISS["U+3354"].append("then,so,later")
BLISS_TO_UNICODE["detonation"] = ["U+36db"]
UNICODE_TO_BLISS["U+36db"].append("detonation")
BLISS_TO_UNICODE["blowup"] = ["U+36db"]
UNICODE_TO_BLISS["U+36db"].append("blowup")
BLISS_TO_UNICODE["explosion,detonation,blowup"] = ["U+36db"]
UNICODE_TO_BLISS["U+36db"].append("explosion,detonation,blowup")
BLISS_TO_UNICODE["four arrows"] = ["U+38ba"]
UNICODE_TO_BLISS["U+38ba"] = ["four arrows"]
BLISS_TO_UNICODE[" moving outwards"] = ["U+38bb"]
UNICODE_TO_BLISS["U+38bb"] = [" moving outwards"]
BLISS_TO_UNICODE["Islam"] = ["U+38bc"]
UNICODE_TO_BLISS["U+38bc"] = ["Islam"]
BLISS_TO_UNICODE["Muslim"] = ["U+38bd"]
UNICODE_TO_BLISS["U+38bd"] = ["Muslim"]
BLISS_TO_UNICODE["archeologist"] = ["U+38be"]
UNICODE_TO_BLISS["U+38be"] = ["archeologist"]
BLISS_TO_UNICODE["archeology"] = ["U+38bf"]
UNICODE_TO_BLISS["U+38bf"] = ["archeology"]
BLISS_TO_UNICODE["synthetic speech"] = ["U+38c0"]
UNICODE_TO_BLISS["U+38c0"] = ["synthetic speech"]
BLISS_TO_UNICODE["text to speech"] = ["U+38c0"]
UNICODE_TO_BLISS["U+38c0"].append("text to speech")
BLISS_TO_UNICODE["tts"] = ["U+38c0"]
UNICODE_TO_BLISS["U+38c0"].append("tts")
BLISS_TO_UNICODE["synthetic speech,text-to-speech,tts"] = ["U+38c0"]
UNICODE_TO_BLISS["U+38c0"].append("synthetic speech,text-to-speech,tts")
BLISS_TO_UNICODE["speech"] = ["U+38c1"]
UNICODE_TO_BLISS["U+38c1"] = ["speech"]
BLISS_TO_UNICODE["long for"] = ["U+38c2"]
UNICODE_TO_BLISS["U+38c2"] = ["long for"]
BLISS_TO_UNICODE["yearn"] = ["U+38c2"]
UNICODE_TO_BLISS["U+38c2"].append("yearn")
BLISS_TO_UNICODE["long for,yearn"] = ["U+38c2"]
UNICODE_TO_BLISS["U+38c2"].append("long for,yearn")
BLISS_TO_UNICODE["longing"] = ["U+38c3"]
UNICODE_TO_BLISS["U+38c3"] = ["longing"]
BLISS_TO_UNICODE["yearning"] = ["U+38c4"]
UNICODE_TO_BLISS["U+38c4"] = ["yearning"]
BLISS_TO_UNICODE["thoughtfulness"] = ["U+32e4"]
UNICODE_TO_BLISS["U+32e4"].append("thoughtfulness")
BLISS_TO_UNICODE["consideration,thoughtfulness"] = ["U+32e4"]
UNICODE_TO_BLISS["U+32e4"].append("consideration,thoughtfulness")
BLISS_TO_UNICODE["descend"] = ["U+38c5"]
UNICODE_TO_BLISS["U+38c5"] = ["descend"]
BLISS_TO_UNICODE["go down"] = ["U+38c5"]
UNICODE_TO_BLISS["U+38c5"].append("go down")
BLISS_TO_UNICODE["descend,go down"] = ["U+38c5"]
UNICODE_TO_BLISS["U+38c5"].append("descend,go down")
BLISS_TO_UNICODE["accordion"] = ["U+38c6"]
UNICODE_TO_BLISS["U+38c6"] = ["accordion"]
BLISS_TO_UNICODE["apron"] = ["U+38c7"]
UNICODE_TO_BLISS["U+38c7"] = ["apron"]
BLISS_TO_UNICODE["coverall"] = ["U+38c7"]
UNICODE_TO_BLISS["U+38c7"].append("coverall")
BLISS_TO_UNICODE["smock"] = ["U+38c7"]
UNICODE_TO_BLISS["U+38c7"].append("smock")
BLISS_TO_UNICODE["overall"] = ["U+38c7"]
UNICODE_TO_BLISS["U+38c7"].append("overall")
BLISS_TO_UNICODE["apron,coverall,smock,overall"] = ["U+38c7"]
UNICODE_TO_BLISS["U+38c7"].append("apron,coverall,smock,overall")
BLISS_TO_UNICODE["insomnia"] = ["U+38c8"]
UNICODE_TO_BLISS["U+38c8"] = ["insomnia"]
BLISS_TO_UNICODE["nation"] = ["U+38c9"]
UNICODE_TO_BLISS["U+38c9"] = ["nation"]
BLISS_TO_UNICODE["forced"] = ["U+38ca"]
UNICODE_TO_BLISS["U+38ca"] = ["forced"]
BLISS_TO_UNICODE["compelled"] = ["U+38ca"]
UNICODE_TO_BLISS["U+38ca"].append("compelled")
BLISS_TO_UNICODE["obliged"] = ["U+38ca"]
UNICODE_TO_BLISS["U+38ca"].append("obliged")
BLISS_TO_UNICODE["forced,compelled,obliged"] = ["U+38ca"]
UNICODE_TO_BLISS["U+38ca"].append("forced,compelled,obliged")
BLISS_TO_UNICODE["must"] = ["U+38cb"]
UNICODE_TO_BLISS["U+38cb"] = ["must"]
BLISS_TO_UNICODE["body fluid"] = ["U+38cc"]
UNICODE_TO_BLISS["U+38cc"] = ["body fluid"]
BLISS_TO_UNICODE["ketchup"] = ["U+38cd"]
UNICODE_TO_BLISS["U+38cd"] = ["ketchup"]
BLISS_TO_UNICODE["tomato sauce"] = ["U+38ce"]
UNICODE_TO_BLISS["U+38ce"] = ["tomato sauce"]
BLISS_TO_UNICODE["fisherman"] = ["U+38cf"]
UNICODE_TO_BLISS["U+38cf"] = ["fisherman"]
BLISS_TO_UNICODE["quarter"] = ["U+38d0"]
UNICODE_TO_BLISS["U+38d0"] = ["quarter"]
BLISS_TO_UNICODE["one quarter"] = ["U+38d0"]
UNICODE_TO_BLISS["U+38d0"].append("one quarter")
BLISS_TO_UNICODE["quarter,one quarter"] = ["U+38d0"]
UNICODE_TO_BLISS["U+38d0"].append("quarter,one quarter")
BLISS_TO_UNICODE["slash"] = ["U+38d1"]
UNICODE_TO_BLISS["U+38d1"] = ["slash"]
BLISS_TO_UNICODE["ironing board"] = ["U+38d2"]
UNICODE_TO_BLISS["U+38d2"] = ["ironing board"]
BLISS_TO_UNICODE["turtle"] = ["U+38d3"]
UNICODE_TO_BLISS["U+38d3"] = ["turtle"]
BLISS_TO_UNICODE["tortoise"].append("U+38d3")
UNICODE_TO_BLISS["U+38d3"].append("tortoise")
BLISS_TO_UNICODE["turtle,tortoise"] = ["U+38d3"]
UNICODE_TO_BLISS["U+38d3"].append("turtle,tortoise")
BLISS_TO_UNICODE["pictograph of head and protective shell"] = ["U+38d4"]
UNICODE_TO_BLISS["U+38d4"] = ["pictograph of head and protective shell"]
BLISS_TO_UNICODE["square"] = ["U+38d5"]
UNICODE_TO_BLISS["U+38d5"] = ["square"]
BLISS_TO_UNICODE["Tyrannosaurus Rex"] = ["U+38d6"]
UNICODE_TO_BLISS["U+38d6"] = ["Tyrannosaurus Rex"]
BLISS_TO_UNICODE["dinosaur"] = ["U+38d7"]
UNICODE_TO_BLISS["U+38d7"] = ["dinosaur"]
BLISS_TO_UNICODE["receipt"] = ["U+38d8"]
UNICODE_TO_BLISS["U+38d8"] = ["receipt"]
BLISS_TO_UNICODE["woodcraft"] = ["U+38d9"]
UNICODE_TO_BLISS["U+38d9"] = ["woodcraft"]
BLISS_TO_UNICODE["craft"] = ["U+38da"]
UNICODE_TO_BLISS["U+38da"] = ["craft"]
BLISS_TO_UNICODE["pictograph of wing cases"] = ["U+38db"]
UNICODE_TO_BLISS["U+38db"] = ["pictograph of wing cases"]
BLISS_TO_UNICODE["district"] = ["U+38dc"]
UNICODE_TO_BLISS["U+38dc"] = ["district"]
BLISS_TO_UNICODE["neighbourhood"] = ["U+38dc"]
UNICODE_TO_BLISS["U+38dc"].append("neighbourhood")
BLISS_TO_UNICODE["district,neighbourhood"] = ["U+38dc"]
UNICODE_TO_BLISS["U+38dc"].append("district,neighbourhood")
BLISS_TO_UNICODE["city district"] = ["U+38dc"]
UNICODE_TO_BLISS["U+38dc"].append("city district")
BLISS_TO_UNICODE["district,city district,neighbourhood"] = ["U+38dc"]
UNICODE_TO_BLISS["U+38dc"].append("district,city district,neighbourhood")
BLISS_TO_UNICODE["city"] = ["U+38dd"]
UNICODE_TO_BLISS["U+38dd"] = ["city"]
BLISS_TO_UNICODE["bowl"] = ["U+32f0"]
UNICODE_TO_BLISS["U+32f0"].append("bowl")
BLISS_TO_UNICODE["holder"] = ["U+32f0"]
UNICODE_TO_BLISS["U+32f0"].append("holder")
BLISS_TO_UNICODE["pouch"] = ["U+32f0"]
UNICODE_TO_BLISS["U+32f0"].append("pouch")
BLISS_TO_UNICODE["basket"] = ["U+32f0"]
UNICODE_TO_BLISS["U+32f0"].append("basket")
BLISS_TO_UNICODE["container,bowl,holder,pouch,basket"] = ["U+32f0"]
UNICODE_TO_BLISS["U+32f0"].append("container,bowl,holder,pouch,basket")
BLISS_TO_UNICODE["container,basket"] = ["U+32f0"]
UNICODE_TO_BLISS["U+32f0"].append("container,basket")
BLISS_TO_UNICODE["airforce"] = ["U+38de"]
UNICODE_TO_BLISS["U+38de"] = ["airforce"]
BLISS_TO_UNICODE["air force"] = ["U+38de"]
UNICODE_TO_BLISS["U+38de"].append("air force")
BLISS_TO_UNICODE["airforce,air force"] = ["U+38de"]
UNICODE_TO_BLISS["U+38de"].append("airforce,air force")
BLISS_TO_UNICODE["examination"] = ["U+38df"]
UNICODE_TO_BLISS["U+38df"] = ["examination"]
BLISS_TO_UNICODE["investigation"] = ["U+38df"]
UNICODE_TO_BLISS["U+38df"].append("investigation")
BLISS_TO_UNICODE["examination,investigation"] = ["U+38df"]
UNICODE_TO_BLISS["U+38df"].append("examination,investigation")
BLISS_TO_UNICODE["to observe"] = ["U+38e0"]
UNICODE_TO_BLISS["U+38e0"] = ["to observe"]
BLISS_TO_UNICODE["fundamental law"] = ["U+38e1"]
UNICODE_TO_BLISS["U+38e1"] = ["fundamental law"]
BLISS_TO_UNICODE["law"] = ["U+38e2"]
UNICODE_TO_BLISS["U+38e2"] = ["law"]
BLISS_TO_UNICODE["fundamental"] = ["U+38e3"]
UNICODE_TO_BLISS["U+38e3"] = ["fundamental"]
BLISS_TO_UNICODE["internet"] = ["U+38e4"]
UNICODE_TO_BLISS["U+38e4"] = ["internet"]
BLISS_TO_UNICODE["digital world"] = ["U+38e5"]
UNICODE_TO_BLISS["U+38e5"] = ["digital world"]
BLISS_TO_UNICODE["Saturn"] = ["U+38e6"]
UNICODE_TO_BLISS["U+38e6"] = ["Saturn"]
BLISS_TO_UNICODE["gas planet"] = ["U+38e7"]
UNICODE_TO_BLISS["U+38e7"] = ["gas planet"]
BLISS_TO_UNICODE["barber"] = ["U+38e8"]
UNICODE_TO_BLISS["U+38e8"] = ["barber"]
BLISS_TO_UNICODE["hairdresser"] = ["U+38e8"]
UNICODE_TO_BLISS["U+38e8"].append("hairdresser")
BLISS_TO_UNICODE["barber,hairdresser"] = ["U+38e8"]
UNICODE_TO_BLISS["U+38e8"].append("barber,hairdresser")
BLISS_TO_UNICODE["snooker"] = ["U+320f"]
UNICODE_TO_BLISS["U+320f"].append("snooker")
BLISS_TO_UNICODE["pool,snooker"] = ["U+320f"]
UNICODE_TO_BLISS["U+320f"].append("pool,snooker")
BLISS_TO_UNICODE["physical impairment"] = ["U+38e9"]
UNICODE_TO_BLISS["U+38e9"] = ["physical impairment"]
BLISS_TO_UNICODE["physical disability"] = ["U+38e9"]
UNICODE_TO_BLISS["U+38e9"].append("physical disability")
BLISS_TO_UNICODE["physical impairment,physical disability"] = ["U+38e9"]
UNICODE_TO_BLISS["U+38e9"].append("physical impairment,physical disability")
BLISS_TO_UNICODE["grandma"] = ["U+3409"]
UNICODE_TO_BLISS["U+3409"].append("grandma")
BLISS_TO_UNICODE["granny"] = ["U+3409"]
UNICODE_TO_BLISS["U+3409"].append("granny")
BLISS_TO_UNICODE["grandmother,grandma,granny"] = ["U+3409"]
UNICODE_TO_BLISS["U+3409"].append("grandmother,grandma,granny")
BLISS_TO_UNICODE["inhaler"] = ["U+38ea"]
UNICODE_TO_BLISS["U+38ea"] = ["inhaler"]
BLISS_TO_UNICODE["medical aid"] = ["U+38eb"]
UNICODE_TO_BLISS["U+38eb"] = ["medical aid"]
BLISS_TO_UNICODE["breath"] = ["U+38ec"]
UNICODE_TO_BLISS["U+38ec"] = ["breath"]
BLISS_TO_UNICODE["pennywhistle"] = ["U+38ed"]
UNICODE_TO_BLISS["U+38ed"] = ["pennywhistle"]
BLISS_TO_UNICODE["tin whistle"] = ["U+38ed"]
UNICODE_TO_BLISS["U+38ed"].append("tin whistle")
BLISS_TO_UNICODE["pennywhistle,tin whistle"] = ["U+38ed"]
UNICODE_TO_BLISS["U+38ed"].append("pennywhistle,tin whistle")
BLISS_TO_UNICODE["downwards"] = ["U+38ee"]
UNICODE_TO_BLISS["U+38ee"] = ["downwards"]
BLISS_TO_UNICODE["soprano"] = ["U+38ef"]
UNICODE_TO_BLISS["U+38ef"] = ["soprano"]
BLISS_TO_UNICODE["South Africa"] = ["U+38f0"]
UNICODE_TO_BLISS["U+38f0"] = ["South Africa"]
BLISS_TO_UNICODE["springbok"] = ["U+38f1"]
UNICODE_TO_BLISS["U+38f1"] = ["springbok"]
BLISS_TO_UNICODE["ostrich"] = ["U+38f2"]
UNICODE_TO_BLISS["U+38f2"] = ["ostrich"]
BLISS_TO_UNICODE["aboard"] = ["U+38f3"]
UNICODE_TO_BLISS["U+38f3"] = ["aboard"]
BLISS_TO_UNICODE["on board"] = ["U+38f3"]
UNICODE_TO_BLISS["U+38f3"].append("on board")
BLISS_TO_UNICODE["aboard,on board"] = ["U+38f3"]
UNICODE_TO_BLISS["U+38f3"].append("aboard,on board")
BLISS_TO_UNICODE["descr. ind."] = ["U+38f4"]
UNICODE_TO_BLISS["U+38f4"] = ["descr. ind."]
BLISS_TO_UNICODE["Brazil"] = ["U+38f5"]
UNICODE_TO_BLISS["U+38f5"] = ["Brazil"]
BLISS_TO_UNICODE["intuition"] = ["U+38f6"]
UNICODE_TO_BLISS["U+38f6"] = ["intuition"]
BLISS_TO_UNICODE["audiologist"] = ["U+38f7"]
UNICODE_TO_BLISS["U+38f7"] = ["audiologist"]
BLISS_TO_UNICODE["therapist"] = ["U+38f8"]
UNICODE_TO_BLISS["U+38f8"] = ["therapist"]
BLISS_TO_UNICODE["railway track"] = ["U+38f9"]
UNICODE_TO_BLISS["U+38f9"] = ["railway track"]
BLISS_TO_UNICODE["track"] = ["U+38fa"]
UNICODE_TO_BLISS["U+38fa"] = ["track"]
BLISS_TO_UNICODE["train"] = ["U+38fb"]
UNICODE_TO_BLISS["U+38fb"] = ["train"]
BLISS_TO_UNICODE["ATM"] = ["U+38fc"]
UNICODE_TO_BLISS["U+38fc"] = ["ATM"]
BLISS_TO_UNICODE["cash machine"] = ["U+38fc"]
UNICODE_TO_BLISS["U+38fc"].append("cash machine")
BLISS_TO_UNICODE["ATM,cash machine"] = ["U+38fc"]
UNICODE_TO_BLISS["U+38fc"].append("ATM,cash machine")
BLISS_TO_UNICODE["bank card"] = ["U+38fd"]
UNICODE_TO_BLISS["U+38fd"] = ["bank card"]
BLISS_TO_UNICODE["pushboat"] = ["U+38fe"]
UNICODE_TO_BLISS["U+38fe"] = ["pushboat"]
BLISS_TO_UNICODE["to push"] = ["U+38ff"]
UNICODE_TO_BLISS["U+38ff"] = ["to push"]
BLISS_TO_UNICODE["1"].append("U+3560")
UNICODE_TO_BLISS["U+3560"].append("1")
BLISS_TO_UNICODE["Arabic numeral 1"] = ["U+3900"]
UNICODE_TO_BLISS["U+3900"] = ["Arabic numeral 1"]
BLISS_TO_UNICODE["Arabic numeral 1 small"] = ["U+3901"]
UNICODE_TO_BLISS["U+3901"] = ["Arabic numeral 1 small"]
BLISS_TO_UNICODE["she"].append("U+35c6")
UNICODE_TO_BLISS["U+35c6"].append("she")
BLISS_TO_UNICODE["him"] = ["U+35c6"]
UNICODE_TO_BLISS["U+35c6"].append("him")
BLISS_TO_UNICODE["her"].append("U+35c6")
UNICODE_TO_BLISS["U+35c6"].append("her")
BLISS_TO_UNICODE["one"].append("U+35c6")
UNICODE_TO_BLISS["U+35c6"].append("one")
BLISS_TO_UNICODE["he,she,him,her,one"] = ["U+35c6"]
UNICODE_TO_BLISS["U+35c6"].append("he,she,him,her,one")
BLISS_TO_UNICODE["cloakroom"] = ["U+3902"]
UNICODE_TO_BLISS["U+3902"] = ["cloakroom"]
BLISS_TO_UNICODE["walk in closet"] = ["U+3902"]
UNICODE_TO_BLISS["U+3902"].append("walk in closet")
BLISS_TO_UNICODE["cloakroom,walk-in closet"] = ["U+3902"]
UNICODE_TO_BLISS["U+3902"].append("cloakroom,walk-in closet")
BLISS_TO_UNICODE["habitation"] = ["U+3903"]
UNICODE_TO_BLISS["U+3903"] = ["habitation"]
BLISS_TO_UNICODE["dwelling place"] = ["U+3903"]
UNICODE_TO_BLISS["U+3903"].append("dwelling place")
BLISS_TO_UNICODE["site"] = ["U+3903"]
UNICODE_TO_BLISS["U+3903"].append("site")
BLISS_TO_UNICODE["habitation,dwelling place,site"] = ["U+3903"]
UNICODE_TO_BLISS["U+3903"].append("habitation,dwelling place,site")
BLISS_TO_UNICODE["live"] = ["U+3904"]
UNICODE_TO_BLISS["U+3904"] = ["live"]
BLISS_TO_UNICODE["hard rock"] = ["U+3905"]
UNICODE_TO_BLISS["U+3905"] = ["hard rock"]
BLISS_TO_UNICODE["town"] = ["U+3906"]
UNICODE_TO_BLISS["U+3906"] = ["town"]
BLISS_TO_UNICODE["city"].append("U+3906")
UNICODE_TO_BLISS["U+3906"].append("city")
BLISS_TO_UNICODE["town,city"] = ["U+3906"]
UNICODE_TO_BLISS["U+3906"].append("town,city")
BLISS_TO_UNICODE["metropolis"] = ["U+38dd"]
UNICODE_TO_BLISS["U+38dd"].append("metropolis")
BLISS_TO_UNICODE["city,metropolis"] = ["U+38dd"]
UNICODE_TO_BLISS["U+38dd"].append("city,metropolis")
BLISS_TO_UNICODE["may"] = ["U+3907"]
UNICODE_TO_BLISS["U+3907"] = ["may"]
BLISS_TO_UNICODE["goldfish"] = ["U+3908"]
UNICODE_TO_BLISS["U+3908"] = ["goldfish"]
BLISS_TO_UNICODE["guppy"] = ["U+3908"]
UNICODE_TO_BLISS["U+3908"].append("guppy")
BLISS_TO_UNICODE["pet fish"] = ["U+3908"]
UNICODE_TO_BLISS["U+3908"].append("pet fish")
BLISS_TO_UNICODE["goldfish,guppy,pet fish"] = ["U+3908"]
UNICODE_TO_BLISS["U+3908"].append("goldfish,guppy,pet fish")
BLISS_TO_UNICODE["Monday"] = ["U+3909"]
UNICODE_TO_BLISS["U+3909"] = ["Monday"]
BLISS_TO_UNICODE["work day"] = ["U+390a"]
UNICODE_TO_BLISS["U+390a"] = ["work day"]
BLISS_TO_UNICODE["bite"] = ["U+390b"]
UNICODE_TO_BLISS["U+390b"] = ["bite"]
BLISS_TO_UNICODE["point"] = ["U+390c"]
UNICODE_TO_BLISS["U+390c"] = ["point"]
BLISS_TO_UNICODE["indicate"] = ["U+390c"]
UNICODE_TO_BLISS["U+390c"].append("indicate")
BLISS_TO_UNICODE["point,indicate"] = ["U+390c"]
UNICODE_TO_BLISS["U+390c"].append("point,indicate")
BLISS_TO_UNICODE["2"].append("U+3562")
UNICODE_TO_BLISS["U+3562"].append("2")
BLISS_TO_UNICODE["Arabic numeral 2"] = ["U+390d"]
UNICODE_TO_BLISS["U+390d"] = ["Arabic numeral 2"]
BLISS_TO_UNICODE["filled"] = ["U+390e"]
UNICODE_TO_BLISS["U+390e"] = ["filled"]
BLISS_TO_UNICODE["stuffed"] = ["U+390e"]
UNICODE_TO_BLISS["U+390e"].append("stuffed")
BLISS_TO_UNICODE["filled,stuffed"] = ["U+390e"]
UNICODE_TO_BLISS["U+390e"].append("filled,stuffed")
BLISS_TO_UNICODE["filling"] = ["U+390f"]
UNICODE_TO_BLISS["U+390f"] = ["filling"]
BLISS_TO_UNICODE["paper money"] = ["U+3910"]
UNICODE_TO_BLISS["U+3910"] = ["paper money"]
BLISS_TO_UNICODE["bill"] = ["U+3910"]
UNICODE_TO_BLISS["U+3910"].append("bill")
BLISS_TO_UNICODE["paper money,bill"] = ["U+3910"]
UNICODE_TO_BLISS["U+3910"].append("paper money,bill")
BLISS_TO_UNICODE["drugstore"] = ["U+3911"]
UNICODE_TO_BLISS["U+3911"] = ["drugstore"]
BLISS_TO_UNICODE["pharmacy"] = ["U+3911"]
UNICODE_TO_BLISS["U+3911"].append("pharmacy")
BLISS_TO_UNICODE["drugstore,pharmacy"] = ["U+3911"]
UNICODE_TO_BLISS["U+3911"].append("drugstore,pharmacy")
BLISS_TO_UNICODE["baking tin"] = ["U+3912"]
UNICODE_TO_BLISS["U+3912"] = ["baking tin"]
BLISS_TO_UNICODE["baking pan"] = ["U+3912"]
UNICODE_TO_BLISS["U+3912"].append("baking pan")
BLISS_TO_UNICODE["ovenware"] = ["U+3912"]
UNICODE_TO_BLISS["U+3912"].append("ovenware")
BLISS_TO_UNICODE["baking tin,baking pan,ovenware"] = ["U+3912"]
UNICODE_TO_BLISS["U+3912"].append("baking tin,baking pan,ovenware")
BLISS_TO_UNICODE["oven"] = ["U+3913"]
UNICODE_TO_BLISS["U+3913"] = ["oven"]
BLISS_TO_UNICODE["starfish"] = ["U+3914"]
UNICODE_TO_BLISS["U+3914"] = ["starfish"]
BLISS_TO_UNICODE["water creature"] = ["U+3915"]
UNICODE_TO_BLISS["U+3915"] = ["water creature"]
BLISS_TO_UNICODE["sniffer dog"] = ["U+3916"]
UNICODE_TO_BLISS["U+3916"] = ["sniffer dog"]
BLISS_TO_UNICODE["man made item"] = ["U+3917"]
UNICODE_TO_BLISS["U+3917"] = ["man made item"]
BLISS_TO_UNICODE["artefact"] = ["U+3917"]
UNICODE_TO_BLISS["U+3917"].append("artefact")
BLISS_TO_UNICODE["artifact"] = ["U+3917"]
UNICODE_TO_BLISS["U+3917"].append("artifact")
BLISS_TO_UNICODE["product"] = ["U+3917"]
UNICODE_TO_BLISS["U+3917"].append("product")
BLISS_TO_UNICODE["man-made item,artefact,artifact,product"] = ["U+3917"]
UNICODE_TO_BLISS["U+3917"].append("man-made item,artefact,artifact,product")
BLISS_TO_UNICODE["making"] = ["U+3918"]
UNICODE_TO_BLISS["U+3918"] = ["making"]
BLISS_TO_UNICODE["production"] = ["U+3919"]
UNICODE_TO_BLISS["U+3919"] = ["production"]
BLISS_TO_UNICODE["fashioning"] = ["U+391a"]
UNICODE_TO_BLISS["U+391a"] = ["fashioning"]
BLISS_TO_UNICODE["boyfriend"] = ["U+391b"]
UNICODE_TO_BLISS["U+391b"] = ["boyfriend"]
BLISS_TO_UNICODE["iceberg"] = ["U+391c"]
UNICODE_TO_BLISS["U+391c"] = ["iceberg"]
BLISS_TO_UNICODE["delicious"] = ["U+391d"]
UNICODE_TO_BLISS["U+391d"] = ["delicious"]
BLISS_TO_UNICODE["scrumptious"] = ["U+391d"]
UNICODE_TO_BLISS["U+391d"].append("scrumptious")
BLISS_TO_UNICODE["yummy"] = ["U+391d"]
UNICODE_TO_BLISS["U+391d"].append("yummy")
BLISS_TO_UNICODE["delicious,scrumptious,yummy"] = ["U+391d"]
UNICODE_TO_BLISS["U+391d"].append("delicious,scrumptious,yummy")
BLISS_TO_UNICODE["tasty"] = ["U+391e"]
UNICODE_TO_BLISS["U+391e"] = ["tasty"]
BLISS_TO_UNICODE["one intensity character"] = ["U+391f"]
UNICODE_TO_BLISS["U+391f"] = ["one intensity character"]
BLISS_TO_UNICODE["summary"] = ["U+3920"]
UNICODE_TO_BLISS["U+3920"] = ["summary"]
BLISS_TO_UNICODE["abstract"] = ["U+3920"]
UNICODE_TO_BLISS["U+3920"].append("abstract")
BLISS_TO_UNICODE["summary,abstract"] = ["U+3920"]
UNICODE_TO_BLISS["U+3920"].append("summary,abstract")
BLISS_TO_UNICODE["outline of parabolic mirror focused on what lies ahead of it"] = ["U+3921"]
UNICODE_TO_BLISS["U+3921"] = ["outline of parabolic mirror focused on what lies ahead of it"]
BLISS_TO_UNICODE["shiny"] = ["U+3922"]
UNICODE_TO_BLISS["U+3922"] = ["shiny"]
BLISS_TO_UNICODE["glossy"] = ["U+3922"]
UNICODE_TO_BLISS["U+3922"].append("glossy")
BLISS_TO_UNICODE["shiny,glossy"] = ["U+3922"]
UNICODE_TO_BLISS["U+3922"].append("shiny,glossy")
BLISS_TO_UNICODE["shine"] = ["U+3923"]
UNICODE_TO_BLISS["U+3923"] = ["shine"]
BLISS_TO_UNICODE["medical treatment"] = ["U+3924"]
UNICODE_TO_BLISS["U+3924"] = ["medical treatment"]
BLISS_TO_UNICODE["medical care"] = ["U+3924"]
UNICODE_TO_BLISS["U+3924"].append("medical care")
BLISS_TO_UNICODE["medical treatment,medical care"] = ["U+3924"]
UNICODE_TO_BLISS["U+3924"].append("medical treatment,medical care")
BLISS_TO_UNICODE["janitor"] = ["U+3925"]
UNICODE_TO_BLISS["U+3925"] = ["janitor"]
BLISS_TO_UNICODE["caretaker"] = ["U+3925"]
UNICODE_TO_BLISS["U+3925"].append("caretaker")
BLISS_TO_UNICODE["janitor,caretaker"] = ["U+3925"]
UNICODE_TO_BLISS["U+3925"].append("janitor,caretaker")
BLISS_TO_UNICODE["disease"] = ["U+3410"]
UNICODE_TO_BLISS["U+3410"].append("disease")
BLISS_TO_UNICODE["sickness"] = ["U+3410"]
UNICODE_TO_BLISS["U+3410"].append("sickness")
BLISS_TO_UNICODE["illness,disease,sickness"] = ["U+3410"]
UNICODE_TO_BLISS["U+3410"].append("illness,disease,sickness")
BLISS_TO_UNICODE["see"] = ["U+3926"]
UNICODE_TO_BLISS["U+3926"] = ["see"]
BLISS_TO_UNICODE["look"] = ["U+3926"]
UNICODE_TO_BLISS["U+3926"].append("look")
BLISS_TO_UNICODE["watch"] = ["U+3926"]
UNICODE_TO_BLISS["U+3926"].append("watch")
BLISS_TO_UNICODE["see,look,watch"] = ["U+3926"]
UNICODE_TO_BLISS["U+3926"].append("see,look,watch")
BLISS_TO_UNICODE["dispute"].append("U+372a")
UNICODE_TO_BLISS["U+372a"].append("dispute")
BLISS_TO_UNICODE["quarrel"].append("U+372a")
UNICODE_TO_BLISS["U+372a"].append("quarrel")
BLISS_TO_UNICODE["argument,dispute,quarrel"] = ["U+372a"]
UNICODE_TO_BLISS["U+372a"].append("argument,dispute,quarrel")
BLISS_TO_UNICODE["discussion"] = ["U+3927"]
UNICODE_TO_BLISS["U+3927"] = ["discussion"]
BLISS_TO_UNICODE["sad"] = ["U+3928"]
UNICODE_TO_BLISS["U+3928"] = ["sad"]
BLISS_TO_UNICODE["sadly"] = ["U+3928"]
UNICODE_TO_BLISS["U+3928"].append("sadly")
BLISS_TO_UNICODE["unhappily"] = ["U+3928"]
UNICODE_TO_BLISS["U+3928"].append("unhappily")
BLISS_TO_UNICODE["unhappy"] = ["U+3928"]
UNICODE_TO_BLISS["U+3928"].append("unhappy")
BLISS_TO_UNICODE["sad,sadly,unhappily,unhappy"] = ["U+3928"]
UNICODE_TO_BLISS["U+3928"].append("sad,sadly,unhappily,unhappy")
BLISS_TO_UNICODE["say"] = ["U+3929"]
UNICODE_TO_BLISS["U+3929"] = ["say"]
BLISS_TO_UNICODE["speak"] = ["U+3929"]
UNICODE_TO_BLISS["U+3929"].append("speak")
BLISS_TO_UNICODE["talk"] = ["U+3929"]
UNICODE_TO_BLISS["U+3929"].append("talk")
BLISS_TO_UNICODE["tell"] = ["U+3929"]
UNICODE_TO_BLISS["U+3929"].append("tell")
BLISS_TO_UNICODE["express"] = ["U+3929"]
UNICODE_TO_BLISS["U+3929"].append("express")
BLISS_TO_UNICODE["say,speak,talk,tell,express"] = ["U+3929"]
UNICODE_TO_BLISS["U+3929"].append("say,speak,talk,tell,express")
BLISS_TO_UNICODE["sap"] = ["U+392a"]
UNICODE_TO_BLISS["U+392a"] = ["sap"]
BLISS_TO_UNICODE["flavouring"] = ["U+392b"]
UNICODE_TO_BLISS["U+392b"] = ["flavouring"]
BLISS_TO_UNICODE["handmade object"] = ["U+392c"]
UNICODE_TO_BLISS["U+392c"] = ["handmade object"]
BLISS_TO_UNICODE["handicraft"] = ["U+392c"]
UNICODE_TO_BLISS["U+392c"].append("handicraft")
BLISS_TO_UNICODE["handmade object,handicraft"] = ["U+392c"]
UNICODE_TO_BLISS["U+392c"].append("handmade object,handicraft")
BLISS_TO_UNICODE["handmade figure"] = ["U+392d"]
UNICODE_TO_BLISS["U+392d"] = ["handmade figure"]
BLISS_TO_UNICODE["handicraft"].append("U+392d")
UNICODE_TO_BLISS["U+392d"].append("handicraft")
BLISS_TO_UNICODE["handmade figure,handicraft"] = ["U+392d"]
UNICODE_TO_BLISS["U+392d"].append("handmade figure,handicraft")
BLISS_TO_UNICODE["wink"] = ["U+392e"]
UNICODE_TO_BLISS["U+392e"] = ["wink"]
BLISS_TO_UNICODE["blink"] = ["U+392e"]
UNICODE_TO_BLISS["U+392e"].append("blink")
BLISS_TO_UNICODE["wink,blink"] = ["U+392e"]
UNICODE_TO_BLISS["U+392e"].append("wink,blink")
BLISS_TO_UNICODE["Jewish"] = ["U+392f"]
UNICODE_TO_BLISS["U+392f"] = ["Jewish"]
BLISS_TO_UNICODE["Star of David"] = ["U+3930"]
UNICODE_TO_BLISS["U+3930"] = ["Star of David"]
BLISS_TO_UNICODE["Tishri"] = ["U+3931"]
UNICODE_TO_BLISS["U+3931"] = ["Tishri"]
BLISS_TO_UNICODE["shofar"] = ["U+3932"]
UNICODE_TO_BLISS["U+3932"] = ["shofar"]
BLISS_TO_UNICODE["zoo"] = ["U+3933"]
UNICODE_TO_BLISS["U+3933"] = ["zoo"]
BLISS_TO_UNICODE["bring"] = ["U+32f3"]
UNICODE_TO_BLISS["U+32f3"].append("bring")
BLISS_TO_UNICODE["carry"] = ["U+32f3"]
UNICODE_TO_BLISS["U+32f3"].append("carry")
BLISS_TO_UNICODE["move"] = ["U+32f3"]
UNICODE_TO_BLISS["U+32f3"].append("move")
BLISS_TO_UNICODE["take,bring,carry,move"] = ["U+32f3"]
UNICODE_TO_BLISS["U+32f3"].append("take,bring,carry,move")
BLISS_TO_UNICODE["portability"] = ["U+3934"]
UNICODE_TO_BLISS["U+3934"] = ["portability"]
BLISS_TO_UNICODE["annul"] = ["U+3538"]
UNICODE_TO_BLISS["U+3538"].append("annul")
BLISS_TO_UNICODE["cancel"] = ["U+3538"]
UNICODE_TO_BLISS["U+3538"].append("cancel")
BLISS_TO_UNICODE["cross out"] = ["U+3538"]
UNICODE_TO_BLISS["U+3538"].append("cross out")
BLISS_TO_UNICODE["delete"] = ["U+3538"]
UNICODE_TO_BLISS["U+3538"].append("delete")
BLISS_TO_UNICODE["destroy,annul,cancel,cross out,delete"] = ["U+3538"]
UNICODE_TO_BLISS["U+3538"].append("destroy,annul,cancel,cross out,delete")
BLISS_TO_UNICODE["blemish"] = ["U+3279"]
UNICODE_TO_BLISS["U+3279"].append("blemish")
BLISS_TO_UNICODE["pimple,blemish"] = ["U+3279"]
UNICODE_TO_BLISS["U+3279"].append("pimple,blemish")
BLISS_TO_UNICODE["Hemulen"] = ["U+3935"]
UNICODE_TO_BLISS["U+3935"] = ["Hemulen"]
BLISS_TO_UNICODE["moth"] = ["U+3342"]
UNICODE_TO_BLISS["U+3342"].append("moth")
BLISS_TO_UNICODE["butterfly,moth"] = ["U+3342"]
UNICODE_TO_BLISS["U+3342"].append("butterfly,moth")
BLISS_TO_UNICODE["printer"] = ["U+3936"]
UNICODE_TO_BLISS["U+3936"] = ["printer"]
BLISS_TO_UNICODE["typewriter"] = ["U+3936"]
UNICODE_TO_BLISS["U+3936"].append("typewriter")
BLISS_TO_UNICODE["printer,typewriter"] = ["U+3936"]
UNICODE_TO_BLISS["U+3936"].append("printer,typewriter")
BLISS_TO_UNICODE["two storey building"] = ["U+3937"]
UNICODE_TO_BLISS["U+3937"] = ["two storey building"]
BLISS_TO_UNICODE["crochet"] = ["U+3938"]
UNICODE_TO_BLISS["U+3938"] = ["crochet"]
BLISS_TO_UNICODE["hook"] = ["U+3939"]
UNICODE_TO_BLISS["U+3939"] = ["hook"]
BLISS_TO_UNICODE["kneeling"] = ["U+393a"]
UNICODE_TO_BLISS["U+393a"] = ["kneeling"]
BLISS_TO_UNICODE["sacrament of baptism"] = ["U+393b"]
UNICODE_TO_BLISS["U+393b"] = ["sacrament of baptism"]
BLISS_TO_UNICODE["sacrament"] = ["U+393c"]
UNICODE_TO_BLISS["U+393c"] = ["sacrament"]
BLISS_TO_UNICODE["sale"] = ["U+393d"]
UNICODE_TO_BLISS["U+393d"] = ["sale"]
BLISS_TO_UNICODE["to sell"] = ["U+393e"]
UNICODE_TO_BLISS["U+393e"] = ["to sell"]
BLISS_TO_UNICODE["salt"] = ["U+393f"]
UNICODE_TO_BLISS["U+393f"] = ["salt"]
BLISS_TO_UNICODE["sea"] = ["U+3940"]
UNICODE_TO_BLISS["U+3940"] = ["sea"]
BLISS_TO_UNICODE["bright"] = ["U+3941"]
UNICODE_TO_BLISS["U+3941"] = ["bright"]
BLISS_TO_UNICODE["smart"] = ["U+3942"]
UNICODE_TO_BLISS["U+3942"] = ["smart"]
BLISS_TO_UNICODE["bright"].append("U+3942")
UNICODE_TO_BLISS["U+3942"].append("bright")
BLISS_TO_UNICODE["clever"] = ["U+3942"]
UNICODE_TO_BLISS["U+3942"].append("clever")
BLISS_TO_UNICODE["intelligent"] = ["U+3942"]
UNICODE_TO_BLISS["U+3942"].append("intelligent")
BLISS_TO_UNICODE["smart,bright,clever,intelligent"] = ["U+3942"]
UNICODE_TO_BLISS["U+3942"].append("smart,bright,clever,intelligent")
BLISS_TO_UNICODE["smartness"] = ["U+3943"]
UNICODE_TO_BLISS["U+3943"] = ["smartness"]
BLISS_TO_UNICODE["brightness"] = ["U+3944"]
UNICODE_TO_BLISS["U+3944"] = ["brightness"]
BLISS_TO_UNICODE["cleverness"] = ["U+3945"]
UNICODE_TO_BLISS["U+3945"] = ["cleverness"]
BLISS_TO_UNICODE["intelligence"] = ["U+3946"]
UNICODE_TO_BLISS["U+3946"] = ["intelligence"]
BLISS_TO_UNICODE["nuclear fallout"] = ["U+3947"]
UNICODE_TO_BLISS["U+3947"] = ["nuclear fallout"]
BLISS_TO_UNICODE["radioactive dust"] = ["U+3947"]
UNICODE_TO_BLISS["U+3947"].append("radioactive dust")
BLISS_TO_UNICODE["nuclear fallout,radioactive dust"] = ["U+3947"]
UNICODE_TO_BLISS["U+3947"].append("nuclear fallout,radioactive dust")
BLISS_TO_UNICODE["dust"] = ["U+3948"]
UNICODE_TO_BLISS["U+3948"] = ["dust"]
BLISS_TO_UNICODE["fiber"] = ["U+3949"]
UNICODE_TO_BLISS["U+3949"] = ["fiber"]
BLISS_TO_UNICODE["fibre"] = ["U+3949"]
UNICODE_TO_BLISS["U+3949"].append("fibre")
BLISS_TO_UNICODE["fibril"] = ["U+3949"]
UNICODE_TO_BLISS["U+3949"].append("fibril")
BLISS_TO_UNICODE["filament"] = ["U+3949"]
UNICODE_TO_BLISS["U+3949"].append("filament")
BLISS_TO_UNICODE["strand"] = ["U+3949"]
UNICODE_TO_BLISS["U+3949"].append("strand")
BLISS_TO_UNICODE["fiber,fibre,fibril,filament,strand"] = ["U+3949"]
UNICODE_TO_BLISS["U+3949"].append("fiber,fibre,fibril,filament,strand")
BLISS_TO_UNICODE["pictorial of a fiber"] = ["U+394a"]
UNICODE_TO_BLISS["U+394a"] = ["pictorial of a fiber"]
BLISS_TO_UNICODE["slow"] = ["U+394b"]
UNICODE_TO_BLISS["U+394b"] = ["slow"]
BLISS_TO_UNICODE["slowly"] = ["U+394b"]
UNICODE_TO_BLISS["U+394b"].append("slowly")
BLISS_TO_UNICODE["slow,slowly"] = ["U+394b"]
UNICODE_TO_BLISS["U+394b"].append("slow,slowly")
BLISS_TO_UNICODE["spill"] = ["U+394c"]
UNICODE_TO_BLISS["U+394c"] = ["spill"]
BLISS_TO_UNICODE["slop"] = ["U+394c"]
UNICODE_TO_BLISS["U+394c"].append("slop")
BLISS_TO_UNICODE["spill,slop"] = ["U+394c"]
UNICODE_TO_BLISS["U+394c"].append("spill,slop")
BLISS_TO_UNICODE["dirt"] = ["U+394d"]
UNICODE_TO_BLISS["U+394d"] = ["dirt"]
BLISS_TO_UNICODE["day before holiday"] = ["U+394e"]
UNICODE_TO_BLISS["U+394e"] = ["day before holiday"]
BLISS_TO_UNICODE["Tarzan"] = ["U+394f"]
UNICODE_TO_BLISS["U+394f"] = ["Tarzan"]
BLISS_TO_UNICODE["make-believe person"] = ["U+3950"]
UNICODE_TO_BLISS["U+3950"] = ["make-believe person"]
BLISS_TO_UNICODE["djungle"] = ["U+3951"]
UNICODE_TO_BLISS["U+3951"] = ["djungle"]
BLISS_TO_UNICODE["liberation"] = ["U+3952"]
UNICODE_TO_BLISS["U+3952"] = ["liberation"]
BLISS_TO_UNICODE["field hockey"] = ["U+3953"]
UNICODE_TO_BLISS["U+3953"] = ["field hockey"]
BLISS_TO_UNICODE["hockey"] = ["U+3953"]
UNICODE_TO_BLISS["U+3953"].append("hockey")
BLISS_TO_UNICODE["field hockey,hockey"] = ["U+3953"]
UNICODE_TO_BLISS["U+3953"].append("field hockey,hockey")
BLISS_TO_UNICODE["sport stick and ball"] = ["U+3954"]
UNICODE_TO_BLISS["U+3954"] = ["sport stick and ball"]
BLISS_TO_UNICODE["dressing gown"] = ["U+3955"]
UNICODE_TO_BLISS["U+3955"] = ["dressing gown"]
BLISS_TO_UNICODE["housecoat"] = ["U+3955"]
UNICODE_TO_BLISS["U+3955"].append("housecoat")
BLISS_TO_UNICODE["robe"] = ["U+3955"]
UNICODE_TO_BLISS["U+3955"].append("robe")
BLISS_TO_UNICODE["dressing gown,housecoat,robe"] = ["U+3955"]
UNICODE_TO_BLISS["U+3955"].append("dressing gown,housecoat,robe")
BLISS_TO_UNICODE["overpass"] = ["U+34cb"]
UNICODE_TO_BLISS["U+34cb"].append("overpass")
BLISS_TO_UNICODE["bridge,overpass"] = ["U+34cb"]
UNICODE_TO_BLISS["U+34cb"].append("bridge,overpass")
BLISS_TO_UNICODE["cleaning cloth"] = ["U+3956"]
UNICODE_TO_BLISS["U+3956"] = ["cleaning cloth"]
BLISS_TO_UNICODE["to clean"] = ["U+3957"]
UNICODE_TO_BLISS["U+3957"] = ["to clean"]
BLISS_TO_UNICODE["helper"] = ["U+3958"]
UNICODE_TO_BLISS["U+3958"] = ["helper"]
BLISS_TO_UNICODE["aide"] = ["U+3958"]
UNICODE_TO_BLISS["U+3958"].append("aide")
BLISS_TO_UNICODE["assistant"] = ["U+3958"]
UNICODE_TO_BLISS["U+3958"].append("assistant")
BLISS_TO_UNICODE["personal assistant"] = ["U+3958"]
UNICODE_TO_BLISS["U+3958"].append("personal assistant")
BLISS_TO_UNICODE["helper,aide,assistant,personal assistant"] = ["U+3958"]
UNICODE_TO_BLISS["U+3958"].append("helper,aide,assistant,personal assistant")
BLISS_TO_UNICODE["freezing"] = ["U+3959"]
UNICODE_TO_BLISS["U+3959"] = ["freezing"]
BLISS_TO_UNICODE["hardening"] = ["U+3959"]
UNICODE_TO_BLISS["U+3959"].append("hardening")
BLISS_TO_UNICODE["solidifying"] = ["U+3959"]
UNICODE_TO_BLISS["U+3959"].append("solidifying")
BLISS_TO_UNICODE["freezing,hardening,solidifying"] = ["U+3959"]
UNICODE_TO_BLISS["U+3959"].append("freezing,hardening,solidifying")
BLISS_TO_UNICODE["symbol is derived from the mathematical symbol for 'greater than'. This symbol in halfsize is the basis for about"] = ["U+395a"]
UNICODE_TO_BLISS["U+395a"] = ["symbol is derived from the mathematical symbol for 'greater than'. This symbol in halfsize is the basis for about"]
BLISS_TO_UNICODE[" at"] = ["U+395b"]
UNICODE_TO_BLISS["U+395b"] = [" at"]
BLISS_TO_UNICODE[" for"] = ["U+395c"]
UNICODE_TO_BLISS["U+395c"] = [" for"]
BLISS_TO_UNICODE[" here and on."] = ["U+395d"]
UNICODE_TO_BLISS["U+395d"] = [" here and on."]
BLISS_TO_UNICODE["wheelchair bike"] = ["U+395e"]
UNICODE_TO_BLISS["U+395e"] = ["wheelchair bike"]
BLISS_TO_UNICODE["swimming rule"] = ["U+395f"]
UNICODE_TO_BLISS["U+395f"] = ["swimming rule"]
BLISS_TO_UNICODE["rule"] = ["U+3960"]
UNICODE_TO_BLISS["U+3960"] = ["rule"]
BLISS_TO_UNICODE["regulation"] = ["U+3961"]
UNICODE_TO_BLISS["U+3961"] = ["regulation"]
BLISS_TO_UNICODE["swimming"] = ["U+3962"]
UNICODE_TO_BLISS["U+3962"] = ["swimming"]
BLISS_TO_UNICODE["artist"] = ["U+3963"]
UNICODE_TO_BLISS["U+3963"] = ["artist"]
BLISS_TO_UNICODE["art"] = ["U+3964"]
UNICODE_TO_BLISS["U+3964"] = ["art"]
BLISS_TO_UNICODE["borrow"] = ["U+3965"]
UNICODE_TO_BLISS["U+3965"] = ["borrow"]
BLISS_TO_UNICODE["to receive"] = ["U+3966"]
UNICODE_TO_BLISS["U+3966"] = ["to receive"]
BLISS_TO_UNICODE["filled leaf"] = ["U+3967"]
UNICODE_TO_BLISS["U+3967"] = ["filled leaf"]
BLISS_TO_UNICODE["dolma"] = ["U+3967"]
UNICODE_TO_BLISS["U+3967"].append("dolma")
BLISS_TO_UNICODE["filled leaf,dolma"] = ["U+3967"]
UNICODE_TO_BLISS["U+3967"].append("filled leaf,dolma")
BLISS_TO_UNICODE["snowsuit"] = ["U+3968"]
UNICODE_TO_BLISS["U+3968"] = ["snowsuit"]
BLISS_TO_UNICODE["winter clothing"] = ["U+3968"]
UNICODE_TO_BLISS["U+3968"].append("winter clothing")
BLISS_TO_UNICODE["snowsuit,winter clothing"] = ["U+3968"]
UNICODE_TO_BLISS["U+3968"].append("snowsuit,winter clothing")
BLISS_TO_UNICODE["bindi"] = ["U+3969"]
UNICODE_TO_BLISS["U+3969"] = ["bindi"]
BLISS_TO_UNICODE["tika"] = ["U+3969"]
UNICODE_TO_BLISS["U+3969"].append("tika")
BLISS_TO_UNICODE["bindi,tika"] = ["U+3969"]
UNICODE_TO_BLISS["U+3969"].append("bindi,tika")
BLISS_TO_UNICODE["pancake"] = ["U+396a"]
UNICODE_TO_BLISS["U+396a"] = ["pancake"]
BLISS_TO_UNICODE["crepe"] = ["U+396a"]
UNICODE_TO_BLISS["U+396a"].append("crepe")
BLISS_TO_UNICODE["tortilla"] = ["U+396a"]
UNICODE_TO_BLISS["U+396a"].append("tortilla")
BLISS_TO_UNICODE["pancake,crepe,tortilla"] = ["U+396a"]
UNICODE_TO_BLISS["U+396a"].append("pancake,crepe,tortilla")
BLISS_TO_UNICODE["vision"] = ["U+396b"]
UNICODE_TO_BLISS["U+396b"] = ["vision"]
BLISS_TO_UNICODE["apparition"] = ["U+396b"]
UNICODE_TO_BLISS["U+396b"].append("apparition")
BLISS_TO_UNICODE["vision,apparition"] = ["U+396b"]
UNICODE_TO_BLISS["U+396b"].append("vision,apparition")
BLISS_TO_UNICODE["supernatural"] = ["U+396c"]
UNICODE_TO_BLISS["U+396c"] = ["supernatural"]
BLISS_TO_UNICODE["sight"] = ["U+396d"]
UNICODE_TO_BLISS["U+396d"] = ["sight"]
BLISS_TO_UNICODE["vision"].append("U+396d")
UNICODE_TO_BLISS["U+396d"].append("vision")
BLISS_TO_UNICODE["visual sense"] = ["U+396d"]
UNICODE_TO_BLISS["U+396d"].append("visual sense")
BLISS_TO_UNICODE["sight,vision,visual sense"] = ["U+396d"]
UNICODE_TO_BLISS["U+396d"].append("sight,vision,visual sense")
BLISS_TO_UNICODE["electric conductor"] = ["U+396e"]
UNICODE_TO_BLISS["U+396e"] = ["electric conductor"]
BLISS_TO_UNICODE["bread knife"] = ["U+396f"]
UNICODE_TO_BLISS["U+396f"] = ["bread knife"]
BLISS_TO_UNICODE["masseur"] = ["U+3970"]
UNICODE_TO_BLISS["U+3970"] = ["masseur"]
BLISS_TO_UNICODE["upward"].append("U+374d")
UNICODE_TO_BLISS["U+374d"].append("upward")
BLISS_TO_UNICODE["up,upward"] = ["U+374d"]
UNICODE_TO_BLISS["U+374d"].append("up,upward")
BLISS_TO_UNICODE["we"] = ["U+3971"]
UNICODE_TO_BLISS["U+3971"] = ["we"]
BLISS_TO_UNICODE["us"].append("U+3971")
UNICODE_TO_BLISS["U+3971"].append("us")
BLISS_TO_UNICODE["ourselves"] = ["U+3971"]
UNICODE_TO_BLISS["U+3971"].append("ourselves")
BLISS_TO_UNICODE["we,us,ourselves"] = ["U+3971"]
UNICODE_TO_BLISS["U+3971"].append("we,us,ourselves")
BLISS_TO_UNICODE["diver"] = ["U+3972"]
UNICODE_TO_BLISS["U+3972"] = ["diver"]
BLISS_TO_UNICODE["diving"] = ["U+3973"]
UNICODE_TO_BLISS["U+3973"] = ["diving"]
BLISS_TO_UNICODE["reading lesson"] = ["U+3974"]
UNICODE_TO_BLISS["U+3974"] = ["reading lesson"]
BLISS_TO_UNICODE["reading"] = ["U+3975"]
UNICODE_TO_BLISS["U+3975"] = ["reading"]
BLISS_TO_UNICODE["towboat"] = ["U+3976"]
UNICODE_TO_BLISS["U+3976"] = ["towboat"]
BLISS_TO_UNICODE["tugboat"] = ["U+3976"]
UNICODE_TO_BLISS["U+3976"].append("tugboat")
BLISS_TO_UNICODE["towboat,tugboat"] = ["U+3976"]
UNICODE_TO_BLISS["U+3976"].append("towboat,tugboat")
BLISS_TO_UNICODE["fundamental rule"] = ["U+3977"]
UNICODE_TO_BLISS["U+3977"] = ["fundamental rule"]
BLISS_TO_UNICODE["lamb"] = ["U+3978"]
UNICODE_TO_BLISS["U+3978"] = ["lamb"]
BLISS_TO_UNICODE["mutton"] = ["U+3978"]
UNICODE_TO_BLISS["U+3978"].append("mutton")
BLISS_TO_UNICODE["lamb,mutton"] = ["U+3978"]
UNICODE_TO_BLISS["U+3978"].append("lamb,mutton")
BLISS_TO_UNICODE["sheep"] = ["U+3979"]
UNICODE_TO_BLISS["U+3979"] = ["sheep"]
BLISS_TO_UNICODE["drug dependency"] = ["U+397a"]
UNICODE_TO_BLISS["U+397a"] = ["drug dependency"]
BLISS_TO_UNICODE["negative dependency"] = ["U+397b"]
UNICODE_TO_BLISS["U+397b"] = ["negative dependency"]
BLISS_TO_UNICODE["drug"] = ["U+397c"]
UNICODE_TO_BLISS["U+397c"] = ["drug"]
BLISS_TO_UNICODE["bureau"] = ["U+3376"]
UNICODE_TO_BLISS["U+3376"].append("bureau")
BLISS_TO_UNICODE["dresser"] = ["U+3376"]
UNICODE_TO_BLISS["U+3376"].append("dresser")
BLISS_TO_UNICODE["chest of drawers,bureau,dresser"] = ["U+3376"]
UNICODE_TO_BLISS["U+3376"].append("chest of drawers,bureau,dresser")
BLISS_TO_UNICODE["rickshaw"] = ["U+397d"]
UNICODE_TO_BLISS["U+397d"] = ["rickshaw"]
BLISS_TO_UNICODE["Thai"] = ["U+397e"]
UNICODE_TO_BLISS["U+397e"] = ["Thai"]
BLISS_TO_UNICODE["Thailand"] = ["U+397f"]
UNICODE_TO_BLISS["U+397f"] = ["Thailand"]
BLISS_TO_UNICODE["jacket"] = ["U+3361"]
UNICODE_TO_BLISS["U+3361"].append("jacket")
BLISS_TO_UNICODE["jumper"] = ["U+3361"]
UNICODE_TO_BLISS["U+3361"].append("jumper")
BLISS_TO_UNICODE["sweater"] = ["U+3361"]
UNICODE_TO_BLISS["U+3361"].append("sweater")
BLISS_TO_UNICODE["coat,jacket,jumper,sweater"] = ["U+3361"]
UNICODE_TO_BLISS["U+3361"].append("coat,jacket,jumper,sweater")
BLISS_TO_UNICODE["Bible"] = ["U+3980"]
UNICODE_TO_BLISS["U+3980"] = ["Bible"]
BLISS_TO_UNICODE["holy book"] = ["U+3981"]
UNICODE_TO_BLISS["U+3981"] = ["holy book"]
BLISS_TO_UNICODE["bicycle helmet"] = ["U+3982"]
UNICODE_TO_BLISS["U+3982"] = ["bicycle helmet"]
BLISS_TO_UNICODE["crash helmet"] = ["U+3982"]
UNICODE_TO_BLISS["U+3982"].append("crash helmet")
BLISS_TO_UNICODE["bicycle helmet,crash helmet"] = ["U+3982"]
UNICODE_TO_BLISS["U+3982"].append("bicycle helmet,crash helmet")
BLISS_TO_UNICODE["helmet"] = ["U+3983"]
UNICODE_TO_BLISS["U+3983"] = ["helmet"]
BLISS_TO_UNICODE["vertical"] = ["U+3984"]
UNICODE_TO_BLISS["U+3984"] = ["vertical"]
BLISS_TO_UNICODE["spark"] = ["U+3985"]
UNICODE_TO_BLISS["U+3985"] = ["spark"]
BLISS_TO_UNICODE["flame"] = ["U+3986"]
UNICODE_TO_BLISS["U+3986"] = ["flame"]
BLISS_TO_UNICODE["building"].append("U+3639")
UNICODE_TO_BLISS["U+3639"].append("building")
BLISS_TO_UNICODE["dwelling"] = ["U+3639"]
UNICODE_TO_BLISS["U+3639"].append("dwelling")
BLISS_TO_UNICODE["residence"] = ["U+3639"]
UNICODE_TO_BLISS["U+3639"].append("residence")
BLISS_TO_UNICODE["house,building,dwelling,residence"] = ["U+3639"]
UNICODE_TO_BLISS["U+3639"].append("house,building,dwelling,residence")
BLISS_TO_UNICODE["defend"] = ["U+3987"]
UNICODE_TO_BLISS["U+3987"] = ["defend"]
BLISS_TO_UNICODE["legal)"] = ["U+3987"]
UNICODE_TO_BLISS["U+3987"].append("legal)")
BLISS_TO_UNICODE["defence"] = ["U+3988"]
UNICODE_TO_BLISS["U+3988"] = ["defence"]
BLISS_TO_UNICODE["mane"] = ["U+3989"]
UNICODE_TO_BLISS["U+3989"] = ["mane"]
BLISS_TO_UNICODE["horse neck"] = ["U+398a"]
UNICODE_TO_BLISS["U+398a"] = ["horse neck"]
BLISS_TO_UNICODE["credit card"] = ["U+398b"]
UNICODE_TO_BLISS["U+398b"] = ["credit card"]
BLISS_TO_UNICODE["credit"] = ["U+398c"]
UNICODE_TO_BLISS["U+398c"] = ["credit"]
BLISS_TO_UNICODE["electrical engineer"] = ["U+398d"]
UNICODE_TO_BLISS["U+398d"] = ["electrical engineer"]
BLISS_TO_UNICODE["designer"] = ["U+398e"]
UNICODE_TO_BLISS["U+398e"] = ["designer"]
BLISS_TO_UNICODE["Snufkin"] = ["U+398f"]
UNICODE_TO_BLISS["U+398f"] = ["Snufkin"]
BLISS_TO_UNICODE["ophthalmologist"] = ["U+3990"]
UNICODE_TO_BLISS["U+3990"] = ["ophthalmologist"]
BLISS_TO_UNICODE["oculist"] = ["U+3990"]
UNICODE_TO_BLISS["U+3990"].append("oculist")
BLISS_TO_UNICODE["ophthalmologist,oculist"] = ["U+3990"]
UNICODE_TO_BLISS["U+3990"].append("ophthalmologist,oculist")
BLISS_TO_UNICODE["homosexuality"] = ["U+3991"]
UNICODE_TO_BLISS["U+3991"] = ["homosexuality"]
BLISS_TO_UNICODE["lesbianism"] = ["U+3991"]
UNICODE_TO_BLISS["U+3991"].append("lesbianism")
BLISS_TO_UNICODE["couple"] = ["U+3992"]
UNICODE_TO_BLISS["U+3992"] = ["couple"]
BLISS_TO_UNICODE["slip"] = ["U+3993"]
UNICODE_TO_BLISS["U+3993"] = ["slip"]
BLISS_TO_UNICODE["petticoat"] = ["U+3993"]
UNICODE_TO_BLISS["U+3993"].append("petticoat")
BLISS_TO_UNICODE["half slip"] = ["U+3993"]
UNICODE_TO_BLISS["U+3993"].append("half slip")
BLISS_TO_UNICODE["underskirt"] = ["U+3993"]
UNICODE_TO_BLISS["U+3993"].append("underskirt")
BLISS_TO_UNICODE["slip,petticoat,half-slip,underskirt"] = ["U+3993"]
UNICODE_TO_BLISS["U+3993"].append("slip,petticoat,half-slip,underskirt")
BLISS_TO_UNICODE["dress"] = ["U+3994"]
UNICODE_TO_BLISS["U+3994"] = ["dress"]
BLISS_TO_UNICODE["boar"] = ["U+3995"]
UNICODE_TO_BLISS["U+3995"] = ["boar"]
BLISS_TO_UNICODE["boar"].append("U+3306")
UNICODE_TO_BLISS["U+3306"].append("boar")
BLISS_TO_UNICODE["boss"] = ["U+3996"]
UNICODE_TO_BLISS["U+3996"] = ["boss"]
BLISS_TO_UNICODE["supervisor"] = ["U+3996"]
UNICODE_TO_BLISS["U+3996"].append("supervisor")
BLISS_TO_UNICODE["boss,supervisor"] = ["U+3996"]
UNICODE_TO_BLISS["U+3996"].append("boss,supervisor")
BLISS_TO_UNICODE["ship"] = ["U+3500"]
UNICODE_TO_BLISS["U+3500"].append("ship")
BLISS_TO_UNICODE["boat,ship"] = ["U+3500"]
UNICODE_TO_BLISS["U+3500"].append("boat,ship")
BLISS_TO_UNICODE["fertilization"].append("U+3733")
UNICODE_TO_BLISS["U+3733"].append("fertilization")
BLISS_TO_UNICODE["fertilized egg"] = ["U+3733"]
UNICODE_TO_BLISS["U+3733"].append("fertilized egg")
BLISS_TO_UNICODE["conception,fertilization,fertilized egg"] = ["U+3733"]
UNICODE_TO_BLISS["U+3733"].append("conception,fertilization,fertilized egg")
BLISS_TO_UNICODE["stretch"] = ["U+3997"]
UNICODE_TO_BLISS["U+3997"] = ["stretch"]
BLISS_TO_UNICODE["fried egg"] = ["U+3271"]
UNICODE_TO_BLISS["U+3271"].append("fried egg")
BLISS_TO_UNICODE["to fry"] = ["U+3998"]
UNICODE_TO_BLISS["U+3998"] = ["to fry"]
BLISS_TO_UNICODE["vacation"] = ["U+3999"]
UNICODE_TO_BLISS["U+3999"] = ["vacation"]
BLISS_TO_UNICODE["holiday"].append("U+3999")
UNICODE_TO_BLISS["U+3999"].append("holiday")
BLISS_TO_UNICODE["vacation,holiday"] = ["U+3999"]
UNICODE_TO_BLISS["U+3999"].append("vacation,holiday")
BLISS_TO_UNICODE["unemployment"] = ["U+399a"]
UNICODE_TO_BLISS["U+399a"] = ["unemployment"]
BLISS_TO_UNICODE["singalong"] = ["U+399b"]
UNICODE_TO_BLISS["U+399b"] = ["singalong"]
BLISS_TO_UNICODE["song"] = ["U+399c"]
UNICODE_TO_BLISS["U+399c"] = ["song"]
BLISS_TO_UNICODE["carve"] = ["U+399d"]
UNICODE_TO_BLISS["U+399d"] = ["carve"]
BLISS_TO_UNICODE["mountain climbing"] = ["U+399e"]
UNICODE_TO_BLISS["U+399e"] = ["mountain climbing"]
BLISS_TO_UNICODE["to go up"] = ["U+399f"]
UNICODE_TO_BLISS["U+399f"] = ["to go up"]
BLISS_TO_UNICODE["clerk"] = ["U+39a0"]
UNICODE_TO_BLISS["U+39a0"] = ["clerk"]
BLISS_TO_UNICODE["legal aid"] = ["U+39a0"]
UNICODE_TO_BLISS["U+39a0"].append("legal aid")
BLISS_TO_UNICODE["clerk,legal aid"] = ["U+39a0"]
UNICODE_TO_BLISS["U+39a0"].append("clerk,legal aid")
BLISS_TO_UNICODE["Joseph"] = ["U+39a1"]
UNICODE_TO_BLISS["U+39a1"] = ["Joseph"]
BLISS_TO_UNICODE["Saint Joseph"] = ["U+39a1"]
UNICODE_TO_BLISS["U+39a1"].append("Saint Joseph")
BLISS_TO_UNICODE["Joseph,Saint Joseph"] = ["U+39a1"]
UNICODE_TO_BLISS["U+39a1"].append("Joseph,Saint Joseph")
BLISS_TO_UNICODE["Christ"] = ["U+39a2"]
UNICODE_TO_BLISS["U+39a2"] = ["Christ"]
BLISS_TO_UNICODE["newspaper"] = ["U+39a3"]
UNICODE_TO_BLISS["U+39a3"] = ["newspaper"]
BLISS_TO_UNICODE["bulletin"] = ["U+39a3"]
UNICODE_TO_BLISS["U+39a3"].append("bulletin")
BLISS_TO_UNICODE["newsletter"] = ["U+39a3"]
UNICODE_TO_BLISS["U+39a3"].append("newsletter")
BLISS_TO_UNICODE["newspaper,bulletin,newsletter"] = ["U+39a3"]
UNICODE_TO_BLISS["U+39a3"].append("newspaper,bulletin,newsletter")
BLISS_TO_UNICODE["girth"] = ["U+39a4"]
UNICODE_TO_BLISS["U+39a4"] = ["girth"]
BLISS_TO_UNICODE["cinch"] = ["U+39a4"]
UNICODE_TO_BLISS["U+39a4"].append("cinch")
BLISS_TO_UNICODE["girth,cinch"] = ["U+39a4"]
UNICODE_TO_BLISS["U+39a4"].append("girth,cinch")
BLISS_TO_UNICODE["canoe"] = ["U+39a5"]
UNICODE_TO_BLISS["U+39a5"] = ["canoe"]
BLISS_TO_UNICODE["touch screen"] = ["U+39a6"]
UNICODE_TO_BLISS["U+39a6"] = ["touch screen"]
BLISS_TO_UNICODE["computer screen"] = ["U+39a7"]
UNICODE_TO_BLISS["U+39a7"] = ["computer screen"]
BLISS_TO_UNICODE["monitor"] = ["U+39a8"]
UNICODE_TO_BLISS["U+39a8"] = ["monitor"]
BLISS_TO_UNICODE["engaged"] = ["U+39a9"]
UNICODE_TO_BLISS["U+39a9"] = ["engaged"]
BLISS_TO_UNICODE["technology"] = ["U+39aa"]
UNICODE_TO_BLISS["U+39aa"] = ["technology"]
BLISS_TO_UNICODE["make the bed"] = ["U+39ab"]
UNICODE_TO_BLISS["U+39ab"] = ["make the bed"]
BLISS_TO_UNICODE["to cover"] = ["U+39ac"]
UNICODE_TO_BLISS["U+39ac"] = ["to cover"]
BLISS_TO_UNICODE["cafe"] = ["U+39ad"]
UNICODE_TO_BLISS["U+39ad"] = ["cafe"]
BLISS_TO_UNICODE["coffee house"] = ["U+39ad"]
UNICODE_TO_BLISS["U+39ad"].append("coffee house")
BLISS_TO_UNICODE["snack bar"] = ["U+39ad"]
UNICODE_TO_BLISS["U+39ad"].append("snack bar")
BLISS_TO_UNICODE["cafe,coffee house,snack bar"] = ["U+39ad"]
UNICODE_TO_BLISS["U+39ad"].append("cafe,coffee house,snack bar")
BLISS_TO_UNICODE["snack"] = ["U+39ae"]
UNICODE_TO_BLISS["U+39ae"] = ["snack"]
BLISS_TO_UNICODE["hearing impaired"] = ["U+39af"]
UNICODE_TO_BLISS["U+39af"] = ["hearing impaired"]
BLISS_TO_UNICODE["hearing-impaired"] = ["U+39af"]
UNICODE_TO_BLISS["U+39af"].append("hearing-impaired")
BLISS_TO_UNICODE["hearing impairment"] = ["U+39b0"]
UNICODE_TO_BLISS["U+39b0"] = ["hearing impairment"]
BLISS_TO_UNICODE["gelding"] = ["U+39b1"]
UNICODE_TO_BLISS["U+39b1"] = ["gelding"]
BLISS_TO_UNICODE["stallion"] = ["U+39b2"]
UNICODE_TO_BLISS["U+39b2"] = ["stallion"]
BLISS_TO_UNICODE["sterilized"] = ["U+39b3"]
UNICODE_TO_BLISS["U+39b3"] = ["sterilized"]
BLISS_TO_UNICODE["I"] = ["U+39b4"]
UNICODE_TO_BLISS["U+39b4"] = ["I"]
BLISS_TO_UNICODE["me"] = ["U+39b4"]
UNICODE_TO_BLISS["U+39b4"].append("me")
BLISS_TO_UNICODE["myself"] = ["U+39b4"]
UNICODE_TO_BLISS["U+39b4"].append("myself")
BLISS_TO_UNICODE["I,me,myself"] = ["U+39b4"]
UNICODE_TO_BLISS["U+39b4"].append("I,me,myself")
BLISS_TO_UNICODE["l"] = ["U+39b5"]
UNICODE_TO_BLISS["U+39b5"] = ["l"]
BLISS_TO_UNICODE["deflate"] = ["U+39b6"]
UNICODE_TO_BLISS["U+39b6"] = ["deflate"]
BLISS_TO_UNICODE["let out air"] = ["U+39b6"]
UNICODE_TO_BLISS["U+39b6"].append("let out air")
BLISS_TO_UNICODE["deflate,let out air"] = ["U+39b6"]
UNICODE_TO_BLISS["U+39b6"].append("deflate,let out air")
BLISS_TO_UNICODE["cheers"] = ["U+39b7"]
UNICODE_TO_BLISS["U+39b7"] = ["cheers"]
BLISS_TO_UNICODE["money card"] = ["U+38fd"]
UNICODE_TO_BLISS["U+38fd"].append("money card")
BLISS_TO_UNICODE["bank card,money card"] = ["U+38fd"]
UNICODE_TO_BLISS["U+38fd"].append("bank card,money card")
BLISS_TO_UNICODE["teetotalism"] = ["U+39b8"]
UNICODE_TO_BLISS["U+39b8"] = ["teetotalism"]
BLISS_TO_UNICODE["alcohol"] = ["U+39b9"]
UNICODE_TO_BLISS["U+39b9"] = ["alcohol"]
BLISS_TO_UNICODE["motor sports"] = ["U+39ba"]
UNICODE_TO_BLISS["U+39ba"] = ["motor sports"]
BLISS_TO_UNICODE["Loki"] = ["U+39bb"]
UNICODE_TO_BLISS["U+39bb"] = ["Loki"]
BLISS_TO_UNICODE["lie"] = ["U+39bc"]
UNICODE_TO_BLISS["U+39bc"] = ["lie"]
BLISS_TO_UNICODE["veal"] = ["U+39bd"]
UNICODE_TO_BLISS["U+39bd"] = ["veal"]
BLISS_TO_UNICODE["calf"] = ["U+39be"]
UNICODE_TO_BLISS["U+39be"] = ["calf"]
BLISS_TO_UNICODE["dimension"] = ["U+33db"]
UNICODE_TO_BLISS["U+33db"].append("dimension")
BLISS_TO_UNICODE["space,dimension"] = ["U+33db"]
UNICODE_TO_BLISS["U+33db"].append("space,dimension")
BLISS_TO_UNICODE["three coordinates drawn in perspective"] = ["U+39bf"]
UNICODE_TO_BLISS["U+39bf"] = ["three coordinates drawn in perspective"]
BLISS_TO_UNICODE[" illustrating the three dimensions of space"] = ["U+39c0"]
UNICODE_TO_BLISS["U+39c0"] = [" illustrating the three dimensions of space"]
BLISS_TO_UNICODE["summer"] = ["U+39c1"]
UNICODE_TO_BLISS["U+39c1"] = ["summer"]
BLISS_TO_UNICODE["creature"] = ["U+39c2"]
UNICODE_TO_BLISS["U+39c2"] = ["creature"]
BLISS_TO_UNICODE["being"].append("U+39c2")
UNICODE_TO_BLISS["U+39c2"].append("being")
BLISS_TO_UNICODE["creature,being"] = ["U+39c2"]
UNICODE_TO_BLISS["U+39c2"].append("creature,being")
BLISS_TO_UNICODE["being"].append("U+3666")
UNICODE_TO_BLISS["U+3666"].append("being")
BLISS_TO_UNICODE["existence,being"] = ["U+3666"]
UNICODE_TO_BLISS["U+3666"].append("existence,being")
BLISS_TO_UNICODE["comfort"].append("U+359e")
UNICODE_TO_BLISS["U+359e"].append("comfort")
BLISS_TO_UNICODE["rest,comfort"] = ["U+359e"]
UNICODE_TO_BLISS["U+359e"].append("rest,comfort")
BLISS_TO_UNICODE["steamer"] = ["U+39c3"]
UNICODE_TO_BLISS["U+39c3"] = ["steamer"]
BLISS_TO_UNICODE["disperse"] = ["U+39c4"]
UNICODE_TO_BLISS["U+39c4"] = ["disperse"]
BLISS_TO_UNICODE["disseminate"] = ["U+39c4"]
UNICODE_TO_BLISS["U+39c4"].append("disseminate")
BLISS_TO_UNICODE["scatter"] = ["U+39c4"]
UNICODE_TO_BLISS["U+39c4"].append("scatter")
BLISS_TO_UNICODE["spread"].append("U+39c4")
UNICODE_TO_BLISS["U+39c4"].append("spread")
BLISS_TO_UNICODE["disperse,disseminate,scatter,spread"] = ["U+39c4"]
UNICODE_TO_BLISS["U+39c4"].append("disperse,disseminate,scatter,spread")
BLISS_TO_UNICODE["dispersion"] = ["U+39c5"]
UNICODE_TO_BLISS["U+39c5"] = ["dispersion"]
BLISS_TO_UNICODE["dissemination"] = ["U+39c6"]
UNICODE_TO_BLISS["U+39c6"] = ["dissemination"]
BLISS_TO_UNICODE["scattering"] = ["U+39c7"]
UNICODE_TO_BLISS["U+39c7"] = ["scattering"]
BLISS_TO_UNICODE["spreading"] = ["U+39c8"]
UNICODE_TO_BLISS["U+39c8"] = ["spreading"]
BLISS_TO_UNICODE["mandolin"] = ["U+39c9"]
UNICODE_TO_BLISS["U+39c9"] = ["mandolin"]
BLISS_TO_UNICODE["string instrument"] = ["U+39ca"]
UNICODE_TO_BLISS["U+39ca"] = ["string instrument"]
BLISS_TO_UNICODE["blissymbolics"] = ["U+39cb"]
UNICODE_TO_BLISS["U+39cb"] = ["blissymbolics"]
BLISS_TO_UNICODE["instrument"] = ["U+3477"]
UNICODE_TO_BLISS["U+3477"].append("instrument")
BLISS_TO_UNICODE["tool,instrument"] = ["U+3477"]
UNICODE_TO_BLISS["U+3477"].append("tool,instrument")
BLISS_TO_UNICODE["bioenergy"] = ["U+39cc"]
UNICODE_TO_BLISS["U+39cc"] = ["bioenergy"]
BLISS_TO_UNICODE["continuance"] = ["U+39cd"]
UNICODE_TO_BLISS["U+39cd"] = ["continuance"]
BLISS_TO_UNICODE["continuation"] = ["U+39cd"]
UNICODE_TO_BLISS["U+39cd"].append("continuation")
BLISS_TO_UNICODE["continuance,continuation"] = ["U+39cd"]
UNICODE_TO_BLISS["U+39cd"].append("continuance,continuation")
BLISS_TO_UNICODE["dart"] = ["U+39ce"]
UNICODE_TO_BLISS["U+39ce"] = ["dart"]
BLISS_TO_UNICODE["dark"] = ["U+39cf"]
UNICODE_TO_BLISS["U+39cf"] = ["dark"]
BLISS_TO_UNICODE["traffic"] = ["U+39d0"]
UNICODE_TO_BLISS["U+39d0"] = ["traffic"]
BLISS_TO_UNICODE["bandage"] = ["U+39d1"]
UNICODE_TO_BLISS["U+39d1"] = ["bandage"]
BLISS_TO_UNICODE["dressing"].append("U+39d1")
UNICODE_TO_BLISS["U+39d1"].append("dressing")
BLISS_TO_UNICODE["bandage,dressing"] = ["U+39d1"]
UNICODE_TO_BLISS["U+39d1"].append("bandage,dressing")
BLISS_TO_UNICODE["medical)"] = ["U+39d3"]
UNICODE_TO_BLISS["U+39d3"] = ["medical)"]
BLISS_TO_UNICODE["globe"] = ["U+35f6"]
UNICODE_TO_BLISS["U+35f6"].append("globe")
BLISS_TO_UNICODE["world"].append("U+35f6")
UNICODE_TO_BLISS["U+35f6"].append("world")
BLISS_TO_UNICODE["earth,globe,world"] = ["U+35f6"]
UNICODE_TO_BLISS["U+35f6"].append("earth,globe,world")
BLISS_TO_UNICODE["dare"] = ["U+39d4"]
UNICODE_TO_BLISS["U+39d4"] = ["dare"]
BLISS_TO_UNICODE["brave"] = ["U+39d5"]
UNICODE_TO_BLISS["U+39d5"] = ["brave"]
BLISS_TO_UNICODE["action ind."] = ["U+39d6"]
UNICODE_TO_BLISS["U+39d6"] = ["action ind."]
BLISS_TO_UNICODE["fiance"] = ["U+39d7"]
UNICODE_TO_BLISS["U+39d7"] = ["fiance"]
BLISS_TO_UNICODE["groom to be"] = ["U+39d7"]
UNICODE_TO_BLISS["U+39d7"].append("groom to be")
BLISS_TO_UNICODE["fiance,groom-to-be"] = ["U+39d7"]
UNICODE_TO_BLISS["U+39d7"].append("fiance,groom-to-be")
BLISS_TO_UNICODE["oyster"] = ["U+39d8"]
UNICODE_TO_BLISS["U+39d8"] = ["oyster"]
BLISS_TO_UNICODE["clam"] = ["U+39d8"]
UNICODE_TO_BLISS["U+39d8"].append("clam")
BLISS_TO_UNICODE["oyster,clam"] = ["U+39d8"]
UNICODE_TO_BLISS["U+39d8"].append("oyster,clam")
BLISS_TO_UNICODE["pictograph of shell"] = ["U+39d9"]
UNICODE_TO_BLISS["U+39d9"] = ["pictograph of shell"]
BLISS_TO_UNICODE["stranger"] = ["U+39da"]
UNICODE_TO_BLISS["U+39da"] = ["stranger"]
BLISS_TO_UNICODE["strange"] = ["U+39db"]
UNICODE_TO_BLISS["U+39db"] = ["strange"]
BLISS_TO_UNICODE["unknown"] = ["U+39da"]
UNICODE_TO_BLISS["U+39da"].append("unknown")
BLISS_TO_UNICODE["stranger,unknown"] = ["U+39da"]
UNICODE_TO_BLISS["U+39da"].append("stranger,unknown")
BLISS_TO_UNICODE["Halloween"] = ["U+39dc"]
UNICODE_TO_BLISS["U+39dc"] = ["Halloween"]
BLISS_TO_UNICODE["All Saint's Day"] = ["U+39dc"]
UNICODE_TO_BLISS["U+39dc"].append("All Saint's Day")
BLISS_TO_UNICODE["Halloween,All Saint's Day"] = ["U+39dc"]
UNICODE_TO_BLISS["U+39dc"].append("Halloween,All Saint's Day")
BLISS_TO_UNICODE["ghost"] = ["U+39dd"]
UNICODE_TO_BLISS["U+39dd"] = ["ghost"]
BLISS_TO_UNICODE["phantom"] = ["U+39de"]
UNICODE_TO_BLISS["U+39de"] = ["phantom"]
BLISS_TO_UNICODE["tsunami"] = ["U+39df"]
UNICODE_TO_BLISS["U+39df"] = ["tsunami"]
BLISS_TO_UNICODE["tidal wave"] = ["U+39e0"]
UNICODE_TO_BLISS["U+39e0"] = ["tidal wave"]
BLISS_TO_UNICODE["clay"] = ["U+3215"]
UNICODE_TO_BLISS["U+3215"].append("clay")
BLISS_TO_UNICODE["mud,clay"] = ["U+3215"]
UNICODE_TO_BLISS["U+3215"].append("mud,clay")
BLISS_TO_UNICODE["punctuation mark"] = ["U+39e1"]
UNICODE_TO_BLISS["U+39e1"] = ["punctuation mark"]
BLISS_TO_UNICODE["metal craft"] = ["U+39e2"]
UNICODE_TO_BLISS["U+39e2"] = ["metal craft"]
BLISS_TO_UNICODE["applaud"] = ["U+39e3"]
UNICODE_TO_BLISS["U+39e3"] = ["applaud"]
BLISS_TO_UNICODE["clap"] = ["U+39e3"]
UNICODE_TO_BLISS["U+39e3"].append("clap")
BLISS_TO_UNICODE["applaud,clap"] = ["U+39e3"]
UNICODE_TO_BLISS["U+39e3"].append("applaud,clap")
BLISS_TO_UNICODE["applause"] = ["U+39e4"]
UNICODE_TO_BLISS["U+39e4"] = ["applause"]
BLISS_TO_UNICODE["meeting room"] = ["U+39e5"]
UNICODE_TO_BLISS["U+39e5"] = ["meeting room"]
BLISS_TO_UNICODE["auditorium"] = ["U+39e5"]
UNICODE_TO_BLISS["U+39e5"].append("auditorium")
BLISS_TO_UNICODE["meeting room,auditorium"] = ["U+39e5"]
UNICODE_TO_BLISS["U+39e5"].append("meeting room,auditorium")
BLISS_TO_UNICODE["folding"] = ["U+33d9"]
UNICODE_TO_BLISS["U+33d9"].append("folding")
BLISS_TO_UNICODE["pleating"] = ["U+33d9"]
UNICODE_TO_BLISS["U+33d9"].append("pleating")
BLISS_TO_UNICODE["fold,folding,pleating"] = ["U+33d9"]
UNICODE_TO_BLISS["U+33d9"].append("fold,folding,pleating")
BLISS_TO_UNICODE["vertical reference line"] = ["U+39e6"]
UNICODE_TO_BLISS["U+39e6"] = ["vertical reference line"]
BLISS_TO_UNICODE["horizontal reference line"] = ["U+39e7"]
UNICODE_TO_BLISS["U+39e7"] = ["horizontal reference line"]
BLISS_TO_UNICODE["pickled"] = ["U+39e8"]
UNICODE_TO_BLISS["U+39e8"] = ["pickled"]
BLISS_TO_UNICODE["sharp"] = ["U+39e9"]
UNICODE_TO_BLISS["U+39e9"] = ["sharp"]
BLISS_TO_UNICODE["lava"] = ["U+39ea"]
UNICODE_TO_BLISS["U+39ea"] = ["lava"]
BLISS_TO_UNICODE["magma"] = ["U+39ea"]
UNICODE_TO_BLISS["U+39ea"].append("magma")
BLISS_TO_UNICODE["lava,magma"] = ["U+39ea"]
UNICODE_TO_BLISS["U+39ea"].append("lava,magma")
BLISS_TO_UNICODE["wireless connection"] = ["U+39eb"]
UNICODE_TO_BLISS["U+39eb"] = ["wireless connection"]
BLISS_TO_UNICODE["WiFi"] = ["U+39eb"]
UNICODE_TO_BLISS["U+39eb"].append("WiFi")
BLISS_TO_UNICODE["wireless connection,WiFi"] = ["U+39eb"]
UNICODE_TO_BLISS["U+39eb"].append("wireless connection,WiFi")
BLISS_TO_UNICODE["digital signal"] = ["U+39ec"]
UNICODE_TO_BLISS["U+39ec"] = ["digital signal"]
BLISS_TO_UNICODE["lobster"] = ["U+39ed"]
UNICODE_TO_BLISS["U+39ed"] = ["lobster"]
BLISS_TO_UNICODE["shellfish with claws"] = ["U+39ee"]
UNICODE_TO_BLISS["U+39ee"] = ["shellfish with claws"]
BLISS_TO_UNICODE["big"] = ["U+39ef"]
UNICODE_TO_BLISS["U+39ef"] = ["big"]
BLISS_TO_UNICODE["activity under water"] = ["U+3973"]
UNICODE_TO_BLISS["U+3973"].append("activity under water")
BLISS_TO_UNICODE["diving,activity under water"] = ["U+3973"]
UNICODE_TO_BLISS["U+3973"].append("diving,activity under water")
BLISS_TO_UNICODE["caries"] = ["U+3454"]
UNICODE_TO_BLISS["U+3454"].append("caries")
BLISS_TO_UNICODE["cavity,caries"] = ["U+3454"]
UNICODE_TO_BLISS["U+3454"].append("cavity,caries")
BLISS_TO_UNICODE["noon"] = ["U+39f0"]
UNICODE_TO_BLISS["U+39f0"] = ["noon"]
BLISS_TO_UNICODE["hour"] = ["U+39f1"]
UNICODE_TO_BLISS["U+39f1"] = ["hour"]
BLISS_TO_UNICODE["12"] = ["U+39f2"]
UNICODE_TO_BLISS["U+39f2"] = ["12"]
BLISS_TO_UNICODE["tuba"] = ["U+39f3"]
UNICODE_TO_BLISS["U+39f3"] = ["tuba"]
BLISS_TO_UNICODE["trumpet"] = ["U+39f4"]
UNICODE_TO_BLISS["U+39f4"] = ["trumpet"]
BLISS_TO_UNICODE["brass instument"] = ["U+39f5"]
UNICODE_TO_BLISS["U+39f5"] = ["brass instument"]
BLISS_TO_UNICODE["bass"] = ["U+39f6"]
UNICODE_TO_BLISS["U+39f6"] = ["bass"]
BLISS_TO_UNICODE["exit"].append("U+336a")
UNICODE_TO_BLISS["U+336a"].append("exit")
BLISS_TO_UNICODE["out of,exit"] = ["U+336a"]
UNICODE_TO_BLISS["U+336a"].append("out of,exit")
BLISS_TO_UNICODE["no speech"] = ["U+39f7"]
UNICODE_TO_BLISS["U+39f7"] = ["no speech"]
BLISS_TO_UNICODE["anarthria"] = ["U+39f8"]
UNICODE_TO_BLISS["U+39f8"] = ["anarthria"]
BLISS_TO_UNICODE["powerfulness"] = ["U+3533"]
UNICODE_TO_BLISS["U+3533"].append("powerfulness")
BLISS_TO_UNICODE["power,powerfulness"] = ["U+3533"]
UNICODE_TO_BLISS["U+3533"].append("power,powerfulness")
BLISS_TO_UNICODE["control"] = ["U+39f9"]
UNICODE_TO_BLISS["U+39f9"] = ["control"]
BLISS_TO_UNICODE["intimate"] = ["U+39fa"]
UNICODE_TO_BLISS["U+39fa"] = ["intimate"]
BLISS_TO_UNICODE["close"] = ["U+39fa"]
UNICODE_TO_BLISS["U+39fa"].append("close")
BLISS_TO_UNICODE["intimate,close"] = ["U+39fa"]
UNICODE_TO_BLISS["U+39fa"].append("intimate,close")
BLISS_TO_UNICODE["intimacy"] = ["U+39fb"]
UNICODE_TO_BLISS["U+39fb"] = ["intimacy"]
BLISS_TO_UNICODE["dad"] = ["U+3402"]
UNICODE_TO_BLISS["U+3402"].append("dad")
BLISS_TO_UNICODE["daddy"] = ["U+3402"]
UNICODE_TO_BLISS["U+3402"].append("daddy")
BLISS_TO_UNICODE["papa"] = ["U+3402"]
UNICODE_TO_BLISS["U+3402"].append("papa")
BLISS_TO_UNICODE["pa"] = ["U+3402"]
UNICODE_TO_BLISS["U+3402"].append("pa")
BLISS_TO_UNICODE["pop"] = ["U+3402"]
UNICODE_TO_BLISS["U+3402"].append("pop")
BLISS_TO_UNICODE["father,dad,daddy,papa,pa,pop"] = ["U+3402"]
UNICODE_TO_BLISS["U+3402"].append("father,dad,daddy,papa,pa,pop")
BLISS_TO_UNICODE["balance"] = ["U+39fc"]
UNICODE_TO_BLISS["U+39fc"] = ["balance"]
BLISS_TO_UNICODE["poise"] = ["U+39fc"]
UNICODE_TO_BLISS["U+39fc"].append("poise")
BLISS_TO_UNICODE["fall"] = ["U+39fd"]
UNICODE_TO_BLISS["U+39fd"] = ["fall"]
BLISS_TO_UNICODE["leadership"] = ["U+39fe"]
UNICODE_TO_BLISS["U+39fe"] = ["leadership"]
BLISS_TO_UNICODE["guidance"] = ["U+39fe"]
UNICODE_TO_BLISS["U+39fe"].append("guidance")
BLISS_TO_UNICODE["leadership,guidance"] = ["U+39fe"]
UNICODE_TO_BLISS["U+39fe"].append("leadership,guidance")
BLISS_TO_UNICODE["tear along"] = ["U+39ff"]
UNICODE_TO_BLISS["U+39ff"] = ["tear along"]
BLISS_TO_UNICODE["advance fast"] = ["U+39ff"]
UNICODE_TO_BLISS["U+39ff"].append("advance fast")
BLISS_TO_UNICODE["go fast"] = ["U+39ff"]
UNICODE_TO_BLISS["U+39ff"].append("go fast")
BLISS_TO_UNICODE["tear along,advance fast,go fast"] = ["U+39ff"]
UNICODE_TO_BLISS["U+39ff"].append("tear along,advance fast,go fast")
BLISS_TO_UNICODE["stone"].append("U+3362")
UNICODE_TO_BLISS["U+3362"].append("stone")
BLISS_TO_UNICODE["pit,stone"] = ["U+3362"]
UNICODE_TO_BLISS["U+3362"].append("pit,stone")
BLISS_TO_UNICODE["rock"] = ["U+33bf"]
UNICODE_TO_BLISS["U+33bf"].append("rock")
BLISS_TO_UNICODE["stone,rock"] = ["U+33bf"]
UNICODE_TO_BLISS["U+33bf"].append("stone,rock")
BLISS_TO_UNICODE["package"] = ["U+3395"]
UNICODE_TO_BLISS["U+3395"].append("package")
BLISS_TO_UNICODE["parcel,package"] = ["U+3395"]
UNICODE_TO_BLISS["U+3395"].append("parcel,package")
BLISS_TO_UNICODE["side"] = ["U+3a00"]
UNICODE_TO_BLISS["U+3a00"] = ["side"]
BLISS_TO_UNICODE["act"] = ["U+3457"]
UNICODE_TO_BLISS["U+3457"].append("act")
BLISS_TO_UNICODE["deed"] = ["U+3457"]
UNICODE_TO_BLISS["U+3457"].append("deed")
BLISS_TO_UNICODE["action,act,deed"] = ["U+3457"]
UNICODE_TO_BLISS["U+3457"].append("action,act,deed")
BLISS_TO_UNICODE["symbol suggests the shape of a volcano cone"] = ["U+3a01"]
UNICODE_TO_BLISS["U+3a01"] = ["symbol suggests the shape of a volcano cone"]
BLISS_TO_UNICODE["which CKB says represents 'one of the primeval actions of our earth'. The Action"] = ["U+3a02"]
UNICODE_TO_BLISS["U+3a02"] = ["which CKB says represents 'one of the primeval actions of our earth'. The Action"]
BLISS_TO_UNICODE["is used primarily as the source of activity action"] = ["U+3a03"]
UNICODE_TO_BLISS["U+3a03"] = ["is used primarily as the source of activity action"]
BLISS_TO_UNICODE["do"] = ["U+3a04"]
UNICODE_TO_BLISS["U+3a04"] = ["do"]
BLISS_TO_UNICODE["act"].append("U+3a04")
UNICODE_TO_BLISS["U+3a04"].append("act")
BLISS_TO_UNICODE["do,act"] = ["U+3a04"]
UNICODE_TO_BLISS["U+3a04"].append("do,act")
BLISS_TO_UNICODE["demonstrate"] = ["U+3457"]
UNICODE_TO_BLISS["U+3457"].append("demonstrate")
BLISS_TO_UNICODE["act,demonstrate"] = ["U+3457"]
UNICODE_TO_BLISS["U+3457"].append("act,demonstrate")
BLISS_TO_UNICODE["mean"] = ["U+3a05"]
UNICODE_TO_BLISS["U+3a05"] = ["mean"]
BLISS_TO_UNICODE["cruel"] = ["U+3a05"]
UNICODE_TO_BLISS["U+3a05"].append("cruel")
BLISS_TO_UNICODE["mean,cruel"] = ["U+3a05"]
UNICODE_TO_BLISS["U+3a05"].append("mean,cruel")
BLISS_TO_UNICODE["signify"] = ["U+3a05"]
UNICODE_TO_BLISS["U+3a05"].append("signify")
BLISS_TO_UNICODE["mean,signify"] = ["U+3a05"]
UNICODE_TO_BLISS["U+3a05"].append("mean,signify")
BLISS_TO_UNICODE["curling"] = ["U+3a06"]
UNICODE_TO_BLISS["U+3a06"] = ["curling"]
BLISS_TO_UNICODE["burning"] = ["U+3a07"]
UNICODE_TO_BLISS["U+3a07"] = ["burning"]
BLISS_TO_UNICODE["picture"] = ["U+3a08"]
UNICODE_TO_BLISS["U+3a08"] = ["picture"]
BLISS_TO_UNICODE["image"] = ["U+3a08"]
UNICODE_TO_BLISS["U+3a08"].append("image")
BLISS_TO_UNICODE["icon"] = ["U+3a08"]
UNICODE_TO_BLISS["U+3a08"].append("icon")
BLISS_TO_UNICODE["painting"] = ["U+3a08"]
UNICODE_TO_BLISS["U+3a08"].append("painting")
BLISS_TO_UNICODE["picture,image,icon,painting"] = ["U+3a08"]
UNICODE_TO_BLISS["U+3a08"].append("picture,image,icon,painting")
BLISS_TO_UNICODE["man doll"] = ["U+3a09"]
UNICODE_TO_BLISS["U+3a09"] = ["man doll"]
BLISS_TO_UNICODE["grass snake"] = ["U+3301"]
UNICODE_TO_BLISS["U+3301"].append("grass snake")
BLISS_TO_UNICODE["apologize"] = ["U+3a0a"]
UNICODE_TO_BLISS["U+3a0a"] = ["apologize"]
BLISS_TO_UNICODE["apologise"] = ["U+3a0a"]
UNICODE_TO_BLISS["U+3a0a"].append("apologise")
BLISS_TO_UNICODE["regret"] = ["U+3a0a"]
UNICODE_TO_BLISS["U+3a0a"].append("regret")
BLISS_TO_UNICODE["apologize,apologise,regret"] = ["U+3a0a"]
UNICODE_TO_BLISS["U+3a0a"].append("apologize,apologise,regret")
BLISS_TO_UNICODE["to speak"] = ["U+3a0b"]
UNICODE_TO_BLISS["U+3a0b"] = ["to speak"]
BLISS_TO_UNICODE["to regret"] = ["U+3a0c"]
UNICODE_TO_BLISS["U+3a0c"] = ["to regret"]
BLISS_TO_UNICODE["racket"] = ["U+3a0d"]
UNICODE_TO_BLISS["U+3a0d"] = ["racket"]
BLISS_TO_UNICODE["racquet"].append("U+3a0d")
UNICODE_TO_BLISS["U+3a0d"].append("racquet")
BLISS_TO_UNICODE["racket,racquet"] = ["U+3a0d"]
UNICODE_TO_BLISS["U+3a0d"].append("racket,racquet")
BLISS_TO_UNICODE["her"].append("U+35c4")
UNICODE_TO_BLISS["U+35c4"].append("her")
BLISS_TO_UNICODE["herself"] = ["U+35c4"]
UNICODE_TO_BLISS["U+35c4"].append("herself")
BLISS_TO_UNICODE["she,her,herself"] = ["U+35c4"]
UNICODE_TO_BLISS["U+35c4"].append("she,her,herself")
BLISS_TO_UNICODE["can opener"] = ["U+3a0e"]
UNICODE_TO_BLISS["U+3a0e"] = ["can opener"]
BLISS_TO_UNICODE["opener"] = ["U+3a0f"]
UNICODE_TO_BLISS["U+3a0f"] = ["opener"]
BLISS_TO_UNICODE["can"] = ["U+3a10"]
UNICODE_TO_BLISS["U+3a10"] = ["can"]
BLISS_TO_UNICODE["harpsichord"] = ["U+3a11"]
UNICODE_TO_BLISS["U+3a11"] = ["harpsichord"]
BLISS_TO_UNICODE["hen"] = ["U+3a12"]
UNICODE_TO_BLISS["U+3a12"] = ["hen"]
BLISS_TO_UNICODE["chicken"] = ["U+3a13"]
UNICODE_TO_BLISS["U+3a13"] = ["chicken"]
BLISS_TO_UNICODE["back up"] = ["U+3a14"]
UNICODE_TO_BLISS["U+3a14"] = ["back up"]
BLISS_TO_UNICODE["then"].append("U+3352")
UNICODE_TO_BLISS["U+3352"].append("then")
BLISS_TO_UNICODE["ago,then"] = ["U+3352"]
UNICODE_TO_BLISS["U+3352"].append("ago,then")
BLISS_TO_UNICODE["finish"] = ["U+3a15"]
UNICODE_TO_BLISS["U+3a15"] = ["finish"]
BLISS_TO_UNICODE["complete"] = ["U+3a15"]
UNICODE_TO_BLISS["U+3a15"].append("complete")
BLISS_TO_UNICODE["finish,complete"] = ["U+3a15"]
UNICODE_TO_BLISS["U+3a15"].append("finish,complete")
BLISS_TO_UNICODE["to do"] = ["U+3a16"]
UNICODE_TO_BLISS["U+3a16"] = ["to do"]
BLISS_TO_UNICODE["finished"] = ["U+3a17"]
UNICODE_TO_BLISS["U+3a17"] = ["finished"]
BLISS_TO_UNICODE["complete"].append("U+3a17")
UNICODE_TO_BLISS["U+3a17"].append("complete")
BLISS_TO_UNICODE["completed"] = ["U+3a17"]
UNICODE_TO_BLISS["U+3a17"].append("completed")
BLISS_TO_UNICODE["finished,complete,completed"] = ["U+3a17"]
UNICODE_TO_BLISS["U+3a17"].append("finished,complete,completed")
BLISS_TO_UNICODE["cake"] = ["U+3a18"]
UNICODE_TO_BLISS["U+3a18"] = ["cake"]
BLISS_TO_UNICODE["bread with sugar"] = ["U+3a18"]
UNICODE_TO_BLISS["U+3a18"].append("bread with sugar")
BLISS_TO_UNICODE["cake,bread with sugar"] = ["U+3a18"]
UNICODE_TO_BLISS["U+3a18"].append("cake,bread with sugar")
BLISS_TO_UNICODE["game rule"] = ["U+3a19"]
UNICODE_TO_BLISS["U+3a19"] = ["game rule"]
BLISS_TO_UNICODE["game"] = ["U+3a1a"]
UNICODE_TO_BLISS["U+3a1a"] = ["game"]
BLISS_TO_UNICODE["takeoff"] = ["U+3a1b"]
UNICODE_TO_BLISS["U+3a1b"] = ["takeoff"]
BLISS_TO_UNICODE["take off"] = ["U+3a1b"]
UNICODE_TO_BLISS["U+3a1b"].append("take off")
BLISS_TO_UNICODE["airplane take off"] = ["U+3a1b"]
UNICODE_TO_BLISS["U+3a1b"].append("airplane take off")
BLISS_TO_UNICODE["takeoff,take-off,airplane take-off"] = ["U+3a1b"]
UNICODE_TO_BLISS["U+3a1b"].append("takeoff,take-off,airplane take-off")
BLISS_TO_UNICODE["camper"] = ["U+3a1c"]
UNICODE_TO_BLISS["U+3a1c"] = ["camper"]
BLISS_TO_UNICODE["caravan"] = ["U+3a1c"]
UNICODE_TO_BLISS["U+3a1c"].append("caravan")
BLISS_TO_UNICODE["mobile home"].append("U+3a1c")
UNICODE_TO_BLISS["U+3a1c"].append("mobile home")
BLISS_TO_UNICODE["camper,caravan,mobile home"] = ["U+3a1c"]
UNICODE_TO_BLISS["U+3a1c"].append("camper,caravan,mobile home")
BLISS_TO_UNICODE["anti virus program"] = ["U+3a1d"]
UNICODE_TO_BLISS["U+3a1d"] = ["anti virus program"]
BLISS_TO_UNICODE["anti-virus program"] = ["U+3a1d"]
UNICODE_TO_BLISS["U+3a1d"].append("anti-virus program")
BLISS_TO_UNICODE["computer program"] = ["U+3a1e"]
UNICODE_TO_BLISS["U+3a1e"] = ["computer program"]
BLISS_TO_UNICODE["beautiful"] = ["U+3a1f"]
UNICODE_TO_BLISS["U+3a1f"] = ["beautiful"]
BLISS_TO_UNICODE["attractive"] = ["U+3a1f"]
UNICODE_TO_BLISS["U+3a1f"].append("attractive")
BLISS_TO_UNICODE["good looking"] = ["U+3a1f"]
UNICODE_TO_BLISS["U+3a1f"].append("good looking")
BLISS_TO_UNICODE["handsome"] = ["U+3a1f"]
UNICODE_TO_BLISS["U+3a1f"].append("handsome")
BLISS_TO_UNICODE["pretty"] = ["U+3a1f"]
UNICODE_TO_BLISS["U+3a1f"].append("pretty")
BLISS_TO_UNICODE["beautiful,attractive,good-looking,handsome,pretty"] = ["U+3a1f"]
UNICODE_TO_BLISS["U+3a1f"].append("beautiful,attractive,good-looking,handsome,pretty")
BLISS_TO_UNICODE["drag"] = ["U+338a"]
UNICODE_TO_BLISS["U+338a"].append("drag")
BLISS_TO_UNICODE["tow"] = ["U+338a"]
UNICODE_TO_BLISS["U+338a"].append("tow")
BLISS_TO_UNICODE["tug"] = ["U+338a"]
UNICODE_TO_BLISS["U+338a"].append("tug")
BLISS_TO_UNICODE["pull,drag,tow,tug"] = ["U+338a"]
UNICODE_TO_BLISS["U+338a"].append("pull,drag,tow,tug")
BLISS_TO_UNICODE["pulling"] = ["U+338a"]
UNICODE_TO_BLISS["U+338a"].append("pulling")
BLISS_TO_UNICODE["pull,pulling"] = ["U+338a"]
UNICODE_TO_BLISS["U+338a"].append("pull,pulling")
BLISS_TO_UNICODE["hurry"] = ["U+3a20"]
UNICODE_TO_BLISS["U+3a20"] = ["hurry"]
BLISS_TO_UNICODE["rush"] = ["U+3a20"]
UNICODE_TO_BLISS["U+3a20"].append("rush")
BLISS_TO_UNICODE["hurry,rush"] = ["U+3a20"]
UNICODE_TO_BLISS["U+3a20"].append("hurry,rush")
BLISS_TO_UNICODE["rags"] = ["U+3a21"]
UNICODE_TO_BLISS["U+3a21"] = ["rags"]
BLISS_TO_UNICODE["usage"] = ["U+3a22"]
UNICODE_TO_BLISS["U+3a22"] = ["usage"]
BLISS_TO_UNICODE["dirty"] = ["U+3a23"]
UNICODE_TO_BLISS["U+3a23"] = ["dirty"]
BLISS_TO_UNICODE["soiled"] = ["U+3a23"]
UNICODE_TO_BLISS["U+3a23"].append("soiled")
BLISS_TO_UNICODE["dirty,soiled"] = ["U+3a23"]
UNICODE_TO_BLISS["U+3a23"].append("dirty,soiled")
BLISS_TO_UNICODE["agree"] = ["U+3a24"]
UNICODE_TO_BLISS["U+3a24"] = ["agree"]
BLISS_TO_UNICODE["gong"] = ["U+3a25"]
UNICODE_TO_BLISS["U+3a25"] = ["gong"]
BLISS_TO_UNICODE["percussion instrument"] = ["U+3a26"]
UNICODE_TO_BLISS["U+3a26"] = ["percussion instrument"]
BLISS_TO_UNICODE["fear"] = ["U+3a27"]
UNICODE_TO_BLISS["U+3a27"] = ["fear"]
BLISS_TO_UNICODE["fright"] = ["U+3a27"]
UNICODE_TO_BLISS["U+3a27"].append("fright")
BLISS_TO_UNICODE["concern"] = ["U+3a27"]
UNICODE_TO_BLISS["U+3a27"].append("concern")
BLISS_TO_UNICODE["fear,fright,concern"] = ["U+3a27"]
UNICODE_TO_BLISS["U+3a27"].append("fear,fright,concern")
BLISS_TO_UNICODE["worn out"] = ["U+359d"]
UNICODE_TO_BLISS["U+359d"].append("worn out")
BLISS_TO_UNICODE["exhausted,worn out"] = ["U+359d"]
UNICODE_TO_BLISS["U+359d"].append("exhausted,worn out")
BLISS_TO_UNICODE["certain"] = ["U+3a28"]
UNICODE_TO_BLISS["U+3a28"] = ["certain"]
BLISS_TO_UNICODE["sure"] = ["U+3a28"]
UNICODE_TO_BLISS["U+3a28"].append("sure")
BLISS_TO_UNICODE["certain,sure"] = ["U+3a28"]
UNICODE_TO_BLISS["U+3a28"].append("certain,sure")
BLISS_TO_UNICODE["Thursday"] = ["U+3a29"]
UNICODE_TO_BLISS["U+3a29"] = ["Thursday"]
BLISS_TO_UNICODE["6"] = ["U+3a2a"]
UNICODE_TO_BLISS["U+3a2a"] = ["6"]
BLISS_TO_UNICODE["still"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"] = ["still"]
BLISS_TO_UNICODE["calm"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("calm")
BLISS_TO_UNICODE["peaceful"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("peaceful")
BLISS_TO_UNICODE["tranquil"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("tranquil")
BLISS_TO_UNICODE["still,calm,peaceful,tranquil"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("still,calm,peaceful,tranquil")
BLISS_TO_UNICODE["chocolate flavouring"] = ["U+3a2c"]
UNICODE_TO_BLISS["U+3a2c"] = ["chocolate flavouring"]
BLISS_TO_UNICODE["coconut"] = ["U+3a2d"]
UNICODE_TO_BLISS["U+3a2d"] = ["coconut"]
BLISS_TO_UNICODE["cream"] = ["U+3a2e"]
UNICODE_TO_BLISS["U+3a2e"] = ["cream"]
BLISS_TO_UNICODE["cream"].append("U+37d2")
UNICODE_TO_BLISS["U+37d2"].append("cream")
BLISS_TO_UNICODE["pudding,cream"] = ["U+37d2"]
UNICODE_TO_BLISS["U+37d2"].append("pudding,cream")
BLISS_TO_UNICODE["pictograph of pudding"] = ["U+3a2f"]
UNICODE_TO_BLISS["U+3a2f"] = ["pictograph of pudding"]
BLISS_TO_UNICODE["end of year"] = ["U+3a30"]
UNICODE_TO_BLISS["U+3a30"] = ["end of year"]
BLISS_TO_UNICODE["New Year's eve"] = ["U+3a31"]
UNICODE_TO_BLISS["U+3a31"] = ["New Year's eve"]
BLISS_TO_UNICODE["end of year"].append("U+3a31")
UNICODE_TO_BLISS["U+3a31"].append("end of year")
BLISS_TO_UNICODE["New Year's eve,end of year"] = ["U+3a31"]
UNICODE_TO_BLISS["U+3a31"].append("New Year's eve,end of year")
BLISS_TO_UNICODE["nutcracker"] = ["U+3a32"]
UNICODE_TO_BLISS["U+3a32"] = ["nutcracker"]
BLISS_TO_UNICODE["kitchen tool"] = ["U+3a33"]
UNICODE_TO_BLISS["U+3a33"] = ["kitchen tool"]
BLISS_TO_UNICODE["nut"] = ["U+3a34"]
UNICODE_TO_BLISS["U+3a34"] = ["nut"]
BLISS_TO_UNICODE["go by horse"] = ["U+3a35"]
UNICODE_TO_BLISS["U+3a35"] = ["go by horse"]
BLISS_TO_UNICODE["dense"] = ["U+3a36"]
UNICODE_TO_BLISS["U+3a36"] = ["dense"]
BLISS_TO_UNICODE["thick"].append("U+3a36")
UNICODE_TO_BLISS["U+3a36"].append("thick")
BLISS_TO_UNICODE["compact"] = ["U+3a36"]
UNICODE_TO_BLISS["U+3a36"].append("compact")
BLISS_TO_UNICODE["tight"] = ["U+3a36"]
UNICODE_TO_BLISS["U+3a36"].append("tight")
BLISS_TO_UNICODE["jammed"] = ["U+3a36"]
UNICODE_TO_BLISS["U+3a36"].append("jammed")
BLISS_TO_UNICODE["dense,thick,compact,tight,jammed"] = ["U+3a36"]
UNICODE_TO_BLISS["U+3a36"].append("dense,thick,compact,tight,jammed")
BLISS_TO_UNICODE["density"] = ["U+3a37"]
UNICODE_TO_BLISS["U+3a37"] = ["density"]
BLISS_TO_UNICODE["puppy"] = ["U+3a38"]
UNICODE_TO_BLISS["U+3a38"] = ["puppy"]
BLISS_TO_UNICODE["video phone"] = ["U+3a39"]
UNICODE_TO_BLISS["U+3a39"] = ["video phone"]
BLISS_TO_UNICODE["bruised"] = ["U+3a3a"]
UNICODE_TO_BLISS["U+3a3a"] = ["bruised"]
BLISS_TO_UNICODE["dented"] = ["U+3a3a"]
UNICODE_TO_BLISS["U+3a3a"].append("dented")
BLISS_TO_UNICODE["bruised,dented"] = ["U+3a3a"]
UNICODE_TO_BLISS["U+3a3a"].append("bruised,dented")
BLISS_TO_UNICODE["bruise"] = ["U+3a3b"]
UNICODE_TO_BLISS["U+3a3b"] = ["bruise"]
BLISS_TO_UNICODE["dent"] = ["U+3a3c"]
UNICODE_TO_BLISS["U+3a3c"] = ["dent"]
BLISS_TO_UNICODE["fresh"] = ["U+3a3d"]
UNICODE_TO_BLISS["U+3a3d"] = ["fresh"]
BLISS_TO_UNICODE["dwarf planet"] = ["U+3a3e"]
UNICODE_TO_BLISS["U+3a3e"] = ["dwarf planet"]
BLISS_TO_UNICODE["planet"] = ["U+3a3f"]
UNICODE_TO_BLISS["U+3a3f"] = ["planet"]
BLISS_TO_UNICODE["slang"] = ["U+3a40"]
UNICODE_TO_BLISS["U+3a40"] = ["slang"]
BLISS_TO_UNICODE["groom"] = ["U+3a41"]
UNICODE_TO_BLISS["U+3a41"] = ["groom"]
BLISS_TO_UNICODE["to protect"] = ["U+3a42"]
UNICODE_TO_BLISS["U+3a42"] = ["to protect"]
BLISS_TO_UNICODE["horse brush"] = ["U+3a43"]
UNICODE_TO_BLISS["U+3a43"] = ["horse brush"]
BLISS_TO_UNICODE["mask"] = ["U+3a44"]
UNICODE_TO_BLISS["U+3a44"] = ["mask"]
BLISS_TO_UNICODE["false face"] = ["U+3a44"]
UNICODE_TO_BLISS["U+3a44"].append("false face")
BLISS_TO_UNICODE["mask,false face"] = ["U+3a44"]
UNICODE_TO_BLISS["U+3a44"].append("mask,false face")
BLISS_TO_UNICODE["pictograph of mask"] = ["U+3a45"]
UNICODE_TO_BLISS["U+3a45"] = ["pictograph of mask"]
BLISS_TO_UNICODE["mash"] = ["U+3a46"]
UNICODE_TO_BLISS["U+3a46"] = ["mash"]
BLISS_TO_UNICODE["crush"].append("U+3a46")
UNICODE_TO_BLISS["U+3a46"].append("crush")
BLISS_TO_UNICODE["squeeze"].append("U+3a46")
UNICODE_TO_BLISS["U+3a46"].append("squeeze")
BLISS_TO_UNICODE["squash"] = ["U+3a46"]
UNICODE_TO_BLISS["U+3a46"].append("squash")
BLISS_TO_UNICODE["mash,crush,squeeze,squash"] = ["U+3a46"]
UNICODE_TO_BLISS["U+3a46"].append("mash,crush,squeeze,squash")
BLISS_TO_UNICODE["mush"] = ["U+3a46"]
UNICODE_TO_BLISS["U+3a46"].append("mush")
BLISS_TO_UNICODE["pulp"] = ["U+3a46"]
UNICODE_TO_BLISS["U+3a46"].append("pulp")
BLISS_TO_UNICODE["mash,mush,pulp"] = ["U+3a46"]
UNICODE_TO_BLISS["U+3a46"].append("mash,mush,pulp")
BLISS_TO_UNICODE["mast"] = ["U+3a48"]
UNICODE_TO_BLISS["U+3a48"] = ["mast"]
BLISS_TO_UNICODE["eye mouse"] = ["U+3a49"]
UNICODE_TO_BLISS["U+3a49"] = ["eye mouse"]
BLISS_TO_UNICODE["eye gaze"] = ["U+3a49"]
UNICODE_TO_BLISS["U+3a49"].append("eye gaze")
BLISS_TO_UNICODE["eye mouse,eye gaze"] = ["U+3a49"]
UNICODE_TO_BLISS["U+3a49"].append("eye mouse,eye gaze")
BLISS_TO_UNICODE["pointing device"] = ["U+3a4a"]
UNICODE_TO_BLISS["U+3a4a"] = ["pointing device"]
BLISS_TO_UNICODE["Canada"] = ["U+3a4b"]
UNICODE_TO_BLISS["U+3a4b"] = ["Canada"]
BLISS_TO_UNICODE["flu"] = ["U+3a4c"]
UNICODE_TO_BLISS["U+3a4c"] = ["flu"]
BLISS_TO_UNICODE["influenza"] = ["U+3a4c"]
UNICODE_TO_BLISS["U+3a4c"].append("influenza")
BLISS_TO_UNICODE["flu,influenza"] = ["U+3a4c"]
UNICODE_TO_BLISS["U+3a4c"].append("flu,influenza")
BLISS_TO_UNICODE["motorcycling"] = ["U+3a4d"]
UNICODE_TO_BLISS["U+3a4d"] = ["motorcycling"]
BLISS_TO_UNICODE["motocross"] = ["U+3a4d"]
UNICODE_TO_BLISS["U+3a4d"].append("motocross")
BLISS_TO_UNICODE["motorcycling,motocross"] = ["U+3a4d"]
UNICODE_TO_BLISS["U+3a4d"].append("motorcycling,motocross")
BLISS_TO_UNICODE["reflect"] = ["U+3a4e"]
UNICODE_TO_BLISS["U+3a4e"] = ["reflect"]
BLISS_TO_UNICODE["consider"] = ["U+3a4e"]
UNICODE_TO_BLISS["U+3a4e"].append("consider")
BLISS_TO_UNICODE["reflect,consider"] = ["U+3a4e"]
UNICODE_TO_BLISS["U+3a4e"].append("reflect,consider")
BLISS_TO_UNICODE["reflection"] = ["U+3a4f"]
UNICODE_TO_BLISS["U+3a4f"] = ["reflection"]
BLISS_TO_UNICODE["neigh"] = ["U+3a50"]
UNICODE_TO_BLISS["U+3a50"] = ["neigh"]
BLISS_TO_UNICODE["whinny"] = ["U+3a50"]
UNICODE_TO_BLISS["U+3a50"].append("whinny")
BLISS_TO_UNICODE["neigh,whinny"] = ["U+3a50"]
UNICODE_TO_BLISS["U+3a50"].append("neigh,whinny")
BLISS_TO_UNICODE["retirement pension"] = ["U+3a51"]
UNICODE_TO_BLISS["U+3a51"] = ["retirement pension"]
BLISS_TO_UNICODE["stop"] = ["U+3a52"]
UNICODE_TO_BLISS["U+3a52"] = ["stop"]
BLISS_TO_UNICODE["wart"] = ["U+3a53"]
UNICODE_TO_BLISS["U+3a53"] = ["wart"]
BLISS_TO_UNICODE["papilloma"] = ["U+3a53"]
UNICODE_TO_BLISS["U+3a53"].append("papilloma")
BLISS_TO_UNICODE["wart,papilloma"] = ["U+3a53"]
UNICODE_TO_BLISS["U+3a53"].append("wart,papilloma")
BLISS_TO_UNICODE["stoma"] = ["U+3a54"]
UNICODE_TO_BLISS["U+3a54"] = ["stoma"]
BLISS_TO_UNICODE["medical hole"] = ["U+3a54"]
UNICODE_TO_BLISS["U+3a54"].append("medical hole")
BLISS_TO_UNICODE["stoma,medical hole"] = ["U+3a54"]
UNICODE_TO_BLISS["U+3a54"].append("stoma,medical hole")
BLISS_TO_UNICODE["hunt"] = ["U+3a55"]
UNICODE_TO_BLISS["U+3a55"] = ["hunt"]
BLISS_TO_UNICODE["hunting"] = ["U+3a55"]
UNICODE_TO_BLISS["U+3a55"].append("hunting")
BLISS_TO_UNICODE["hunt,hunting"] = ["U+3a55"]
UNICODE_TO_BLISS["U+3a55"].append("hunt,hunting")
BLISS_TO_UNICODE["spirit"] = ["U+3a56"]
UNICODE_TO_BLISS["U+3a56"] = ["spirit"]
BLISS_TO_UNICODE["toward"] = ["U+3514"]
UNICODE_TO_BLISS["U+3514"].append("toward")
BLISS_TO_UNICODE["towards"].append("U+3514")
UNICODE_TO_BLISS["U+3514"].append("towards")
BLISS_TO_UNICODE["to,toward,towards"] = ["U+3514"]
UNICODE_TO_BLISS["U+3514"].append("to,toward,towards")
BLISS_TO_UNICODE["horse rump"] = ["U+3a57"]
UNICODE_TO_BLISS["U+3a57"] = ["horse rump"]
BLISS_TO_UNICODE["lottery"] = ["U+3a58"]
UNICODE_TO_BLISS["U+3a58"] = ["lottery"]
BLISS_TO_UNICODE["game of chance"] = ["U+3a58"]
UNICODE_TO_BLISS["U+3a58"].append("game of chance")
BLISS_TO_UNICODE["lottery,game of chance"] = ["U+3a58"]
UNICODE_TO_BLISS["U+3a58"].append("lottery,game of chance")
BLISS_TO_UNICODE["smile"] = ["U+3a5a"]
UNICODE_TO_BLISS["U+3a5a"] = ["smile"]
BLISS_TO_UNICODE["grin"] = ["U+3a5a"]
UNICODE_TO_BLISS["U+3a5a"].append("grin")
BLISS_TO_UNICODE["smile,grin"] = ["U+3a5a"]
UNICODE_TO_BLISS["U+3a5a"].append("smile,grin")
BLISS_TO_UNICODE["appointment"] = ["U+3a5b"]
UNICODE_TO_BLISS["U+3a5b"] = ["appointment"]
BLISS_TO_UNICODE["to meet"] = ["U+3a5c"]
UNICODE_TO_BLISS["U+3a5c"] = ["to meet"]
BLISS_TO_UNICODE["Capricorn"] = ["U+3a5d"]
UNICODE_TO_BLISS["U+3a5d"] = ["Capricorn"]
BLISS_TO_UNICODE["sexual activity"] = ["U+3a5e"]
UNICODE_TO_BLISS["U+3a5e"] = ["sexual activity"]
BLISS_TO_UNICODE["salesperson"] = ["U+3a5f"]
UNICODE_TO_BLISS["U+3a5f"] = ["salesperson"]
BLISS_TO_UNICODE["shop owner"] = ["U+3a5f"]
UNICODE_TO_BLISS["U+3a5f"].append("shop owner")
BLISS_TO_UNICODE["salesperson,shop owner"] = ["U+3a5f"]
UNICODE_TO_BLISS["U+3a5f"].append("salesperson,shop owner")
BLISS_TO_UNICODE["minced meat"] = ["U+3634"]
UNICODE_TO_BLISS["U+3634"].append("minced meat")
BLISS_TO_UNICODE["ground meat"] = ["U+3634"]
UNICODE_TO_BLISS["U+3634"].append("ground meat")
BLISS_TO_UNICODE["bits"] = ["U+3a60"]
UNICODE_TO_BLISS["U+3a60"] = ["bits"]
BLISS_TO_UNICODE["MP3 player"] = ["U+3a61"]
UNICODE_TO_BLISS["U+3a61"] = ["MP3 player"]
BLISS_TO_UNICODE["iPod"] = ["U+3a61"]
UNICODE_TO_BLISS["U+3a61"].append("iPod")
BLISS_TO_UNICODE["MP3 player,iPod"] = ["U+3a61"]
UNICODE_TO_BLISS["U+3a61"].append("MP3 player,iPod")
BLISS_TO_UNICODE["to listen"] = ["U+3a62"]
UNICODE_TO_BLISS["U+3a62"] = ["to listen"]
BLISS_TO_UNICODE["electric wire"] = ["U+3a63"]
UNICODE_TO_BLISS["U+3a63"] = ["electric wire"]
BLISS_TO_UNICODE["electric cord"] = ["U+3a63"]
UNICODE_TO_BLISS["U+3a63"].append("electric cord")
BLISS_TO_UNICODE["cord"].append("U+3a63")
UNICODE_TO_BLISS["U+3a63"].append("cord")
BLISS_TO_UNICODE["cable"] = ["U+3a63"]
UNICODE_TO_BLISS["U+3a63"].append("cable")
BLISS_TO_UNICODE["lead"].append("U+3a63")
UNICODE_TO_BLISS["U+3a63"].append("lead")
BLISS_TO_UNICODE["electric wire,electric cord,cord,cable,lead"] = ["U+3a63"]
UNICODE_TO_BLISS["U+3a63"].append("electric wire,electric cord,cord,cable,lead")
BLISS_TO_UNICODE["wire"] = ["U+3a64"]
UNICODE_TO_BLISS["U+3a64"] = ["wire"]
BLISS_TO_UNICODE["cable"].append("U+3a64")
UNICODE_TO_BLISS["U+3a64"].append("cable")
BLISS_TO_UNICODE["wire,cable"] = ["U+3a64"]
UNICODE_TO_BLISS["U+3a64"].append("wire,cable")
BLISS_TO_UNICODE["underwear"] = ["U+3a65"]
UNICODE_TO_BLISS["U+3a65"] = ["underwear"]
BLISS_TO_UNICODE["underclothes"] = ["U+3a65"]
UNICODE_TO_BLISS["U+3a65"].append("underclothes")
BLISS_TO_UNICODE["underwear,underclothes"] = ["U+3a65"]
UNICODE_TO_BLISS["U+3a65"].append("underwear,underclothes")
BLISS_TO_UNICODE["large"].append("U+39ef")
UNICODE_TO_BLISS["U+39ef"].append("large")
BLISS_TO_UNICODE["big,large"] = ["U+39ef"]
UNICODE_TO_BLISS["U+39ef"].append("big,large")
BLISS_TO_UNICODE["bigness"] = ["U+3a66"]
UNICODE_TO_BLISS["U+3a66"] = ["bigness"]
BLISS_TO_UNICODE["largeness"] = ["U+3a67"]
UNICODE_TO_BLISS["U+3a67"] = ["largeness"]
BLISS_TO_UNICODE["pictograph of dinosaur head and tail"] = ["U+3a68"]
UNICODE_TO_BLISS["U+3a68"] = ["pictograph of dinosaur head and tail"]
BLISS_TO_UNICODE["swimsuit"] = ["U+3a69"]
UNICODE_TO_BLISS["U+3a69"] = ["swimsuit"]
BLISS_TO_UNICODE["swimwear"] = ["U+3a69"]
UNICODE_TO_BLISS["U+3a69"].append("swimwear")
BLISS_TO_UNICODE["bathing suit"] = ["U+3a69"]
UNICODE_TO_BLISS["U+3a69"].append("bathing suit")
BLISS_TO_UNICODE["swimsuit,swimwear,bathing suit"] = ["U+3a69"]
UNICODE_TO_BLISS["U+3a69"].append("swimsuit,swimwear,bathing suit")
BLISS_TO_UNICODE["to swim"] = ["U+3a6a"]
UNICODE_TO_BLISS["U+3a6a"] = ["to swim"]
BLISS_TO_UNICODE["small"].append("U+35d9")
UNICODE_TO_BLISS["U+35d9"].append("small")
BLISS_TO_UNICODE["little,small"] = ["U+35d9"]
UNICODE_TO_BLISS["U+35d9"].append("little,small")
BLISS_TO_UNICODE["twin brother"] = ["U+3a6b"]
UNICODE_TO_BLISS["U+3a6b"] = ["twin brother"]
BLISS_TO_UNICODE["brother"] = ["U+3a6c"]
UNICODE_TO_BLISS["U+3a6c"] = ["brother"]
BLISS_TO_UNICODE["outline of parabolic mirror focused on what lies behind it"] = ["U+3a6d"]
UNICODE_TO_BLISS["U+3a6d"] = ["outline of parabolic mirror focused on what lies behind it"]
BLISS_TO_UNICODE["beyond"] = ["U+3a6e"]
UNICODE_TO_BLISS["U+3a6e"] = ["beyond"]
BLISS_TO_UNICODE["past"].append("U+3a6e")
UNICODE_TO_BLISS["U+3a6e"].append("past")
BLISS_TO_UNICODE["beyond,past"] = ["U+3a6e"]
UNICODE_TO_BLISS["U+3a6e"].append("beyond,past")
BLISS_TO_UNICODE["pass"] = ["U+322f"]
UNICODE_TO_BLISS["U+322f"].append("pass")
BLISS_TO_UNICODE["continue,pass"] = ["U+322f"]
UNICODE_TO_BLISS["U+322f"].append("continue,pass")
BLISS_TO_UNICODE["ticket"] = ["U+3a6f"]
UNICODE_TO_BLISS["U+3a6f"] = ["ticket"]
BLISS_TO_UNICODE["pass"].append("U+3a6f")
UNICODE_TO_BLISS["U+3a6f"].append("pass")
BLISS_TO_UNICODE["ticket,pass"] = ["U+3a6f"]
UNICODE_TO_BLISS["U+3a6f"].append("ticket,pass")
BLISS_TO_UNICODE["turning"] = ["U+325a"]
UNICODE_TO_BLISS["U+325a"].append("turning")
BLISS_TO_UNICODE["turn,turning"] = ["U+325a"]
UNICODE_TO_BLISS["U+325a"].append("turn,turning")
BLISS_TO_UNICODE["curved arrow"] = ["U+3a70"]
UNICODE_TO_BLISS["U+3a70"] = ["curved arrow"]
BLISS_TO_UNICODE["vanilla sauce"] = ["U+3a71"]
UNICODE_TO_BLISS["U+3a71"] = ["vanilla sauce"]
BLISS_TO_UNICODE["vanilla"] = ["U+3a72"]
UNICODE_TO_BLISS["U+3a72"] = ["vanilla"]
BLISS_TO_UNICODE["clock"] = ["U+3a73"]
UNICODE_TO_BLISS["U+3a73"] = ["clock"]
BLISS_TO_UNICODE["timepiece"] = ["U+3a73"]
UNICODE_TO_BLISS["U+3a73"].append("timepiece")
BLISS_TO_UNICODE["clock,timepiece"] = ["U+3a73"]
UNICODE_TO_BLISS["U+3a73"].append("clock,timepiece")
BLISS_TO_UNICODE["nurse"] = ["U+3a74"]
UNICODE_TO_BLISS["U+3a74"] = ["nurse"]
BLISS_TO_UNICODE["to care for"] = ["U+3a75"]
UNICODE_TO_BLISS["U+3a75"] = ["to care for"]
BLISS_TO_UNICODE["design"].append("U+368a")
UNICODE_TO_BLISS["U+368a"].append("design")
BLISS_TO_UNICODE["method"] = ["U+368a"]
UNICODE_TO_BLISS["U+368a"].append("method")
BLISS_TO_UNICODE["system"].append("U+368a")
UNICODE_TO_BLISS["U+368a"].append("system")
BLISS_TO_UNICODE["plan,design,method,system"] = ["U+368a"]
UNICODE_TO_BLISS["U+368a"].append("plan,design,method,system")
BLISS_TO_UNICODE["manmade"] = ["U+3a76"]
UNICODE_TO_BLISS["U+3a76"] = ["manmade"]
BLISS_TO_UNICODE["contrast"] = ["U+3a77"]
UNICODE_TO_BLISS["U+3a77"] = ["contrast"]
BLISS_TO_UNICODE["full"] = ["U+3a78"]
UNICODE_TO_BLISS["U+3a78"] = ["full"]
BLISS_TO_UNICODE["satisfied"] = ["U+3a78"]
UNICODE_TO_BLISS["U+3a78"].append("satisfied")
BLISS_TO_UNICODE["full,satisfied"] = ["U+3a78"]
UNICODE_TO_BLISS["U+3a78"].append("full,satisfied")
BLISS_TO_UNICODE["empower"] = ["U+3a79"]
UNICODE_TO_BLISS["U+3a79"] = ["empower"]
BLISS_TO_UNICODE["empowerment"] = ["U+3a7a"]
UNICODE_TO_BLISS["U+3a7a"] = ["empowerment"]
BLISS_TO_UNICODE["Finland"] = ["U+3a7b"]
UNICODE_TO_BLISS["U+3a7b"] = ["Finland"]
BLISS_TO_UNICODE["sauna"] = ["U+3a7c"]
UNICODE_TO_BLISS["U+3a7c"] = ["sauna"]
BLISS_TO_UNICODE["vomiting"] = ["U+3a7d"]
UNICODE_TO_BLISS["U+3a7d"] = ["vomiting"]
BLISS_TO_UNICODE["vomit"] = ["U+3a7d"]
UNICODE_TO_BLISS["U+3a7d"].append("vomit")
BLISS_TO_UNICODE["puking"] = ["U+3a7d"]
UNICODE_TO_BLISS["U+3a7d"].append("puking")
BLISS_TO_UNICODE["vomiting,vomit,puking"] = ["U+3a7d"]
UNICODE_TO_BLISS["U+3a7d"].append("vomiting,vomit,puking")
BLISS_TO_UNICODE["Latvian"] = ["U+3a7e"]
UNICODE_TO_BLISS["U+3a7e"] = ["Latvian"]
BLISS_TO_UNICODE["Latvia"] = ["U+3a7f"]
UNICODE_TO_BLISS["U+3a7f"] = ["Latvia"]
BLISS_TO_UNICODE["grow"] = ["U+374a"]
UNICODE_TO_BLISS["U+374a"].append("grow")
BLISS_TO_UNICODE["bring up"] = ["U+374a"]
UNICODE_TO_BLISS["U+374a"].append("bring up")
BLISS_TO_UNICODE["cultivate"] = ["U+374a"]
UNICODE_TO_BLISS["U+374a"].append("cultivate")
BLISS_TO_UNICODE["raise,grow,bring up,cultivate"] = ["U+374a"]
UNICODE_TO_BLISS["U+374a"].append("raise,grow,bring up,cultivate")
BLISS_TO_UNICODE["to grow"] = ["U+3a80"]
UNICODE_TO_BLISS["U+3a80"] = ["to grow"]
BLISS_TO_UNICODE["folk tale"] = ["U+3a81"]
UNICODE_TO_BLISS["U+3a81"] = ["folk tale"]
BLISS_TO_UNICODE["legend"] = ["U+3a81"]
UNICODE_TO_BLISS["U+3a81"].append("legend")
BLISS_TO_UNICODE["folk tale,legend"] = ["U+3a81"]
UNICODE_TO_BLISS["U+3a81"].append("folk tale,legend")
BLISS_TO_UNICODE["story"] = ["U+3a82"]
UNICODE_TO_BLISS["U+3a82"] = ["story"]
BLISS_TO_UNICODE[" tale"] = ["U+3a83"]
UNICODE_TO_BLISS["U+3a83"] = [" tale"]
BLISS_TO_UNICODE["criminality"] = ["U+3a84"]
UNICODE_TO_BLISS["U+3a84"] = ["criminality"]
BLISS_TO_UNICODE["crime"] = ["U+3a84"]
UNICODE_TO_BLISS["U+3a84"].append("crime")
BLISS_TO_UNICODE["criminality,crime"] = ["U+3a84"]
UNICODE_TO_BLISS["U+3a84"].append("criminality,crime")
BLISS_TO_UNICODE["illegal"] = ["U+3a85"]
UNICODE_TO_BLISS["U+3a85"] = ["illegal"]
BLISS_TO_UNICODE["criminal"] = ["U+3a86"]
UNICODE_TO_BLISS["U+3a86"] = ["criminal"]
BLISS_TO_UNICODE["experience"] = ["U+3a87"]
UNICODE_TO_BLISS["U+3a87"] = ["experience"]
BLISS_TO_UNICODE["gerbil"] = ["U+3a88"]
UNICODE_TO_BLISS["U+3a88"] = ["gerbil"]
BLISS_TO_UNICODE["guinea pig"] = ["U+3a88"]
UNICODE_TO_BLISS["U+3a88"].append("guinea pig")
BLISS_TO_UNICODE["hamster"] = ["U+3a88"]
UNICODE_TO_BLISS["U+3a88"].append("hamster")
BLISS_TO_UNICODE["gerbil,guinea pig,hamster"] = ["U+3a88"]
UNICODE_TO_BLISS["U+3a88"].append("gerbil,guinea pig,hamster")
BLISS_TO_UNICODE["social"] = ["U+3a89"]
UNICODE_TO_BLISS["U+3a89"] = ["social"]
BLISS_TO_UNICODE["society"] = ["U+3a8a"]
UNICODE_TO_BLISS["U+3a8a"] = ["society"]
BLISS_TO_UNICODE["demonstration"] = ["U+3457"]
UNICODE_TO_BLISS["U+3457"].append("demonstration")
BLISS_TO_UNICODE["action,demonstration"] = ["U+3457"]
UNICODE_TO_BLISS["U+3457"].append("action,demonstration")
BLISS_TO_UNICODE["scepticism"] = ["U+3a8b"]
UNICODE_TO_BLISS["U+3a8b"] = ["scepticism"]
BLISS_TO_UNICODE["skepticism"] = ["U+3a8b"]
UNICODE_TO_BLISS["U+3a8b"].append("skepticism")
BLISS_TO_UNICODE["scepticism,skepticism"] = ["U+3a8b"]
UNICODE_TO_BLISS["U+3a8b"].append("scepticism,skepticism")
BLISS_TO_UNICODE["sweetness"] = ["U+3a8c"]
UNICODE_TO_BLISS["U+3a8c"] = ["sweetness"]
BLISS_TO_UNICODE["sweet"].append("U+3a8c")
UNICODE_TO_BLISS["U+3a8c"].append("sweet")
BLISS_TO_UNICODE["sweetness,sweet"] = ["U+3a8c"]
UNICODE_TO_BLISS["U+3a8c"].append("sweetness,sweet")
BLISS_TO_UNICODE["spray bottle"] = ["U+3a8d"]
UNICODE_TO_BLISS["U+3a8d"] = ["spray bottle"]
BLISS_TO_UNICODE["vaporizer"] = ["U+3a8d"]
UNICODE_TO_BLISS["U+3a8d"].append("vaporizer")
BLISS_TO_UNICODE["spray can"] = ["U+3a8d"]
UNICODE_TO_BLISS["U+3a8d"].append("spray can")
BLISS_TO_UNICODE["spray bottle,vaporizer,spray can"] = ["U+3a8d"]
UNICODE_TO_BLISS["U+3a8d"].append("spray bottle,vaporizer,spray can")
BLISS_TO_UNICODE["spray"] = ["U+3a8e"]
UNICODE_TO_BLISS["U+3a8e"] = ["spray"]
BLISS_TO_UNICODE["vaporization"] = ["U+3a8f"]
UNICODE_TO_BLISS["U+3a8f"] = ["vaporization"]
BLISS_TO_UNICODE["period"] = ["U+3a90"]
UNICODE_TO_BLISS["U+3a90"] = ["period"]
BLISS_TO_UNICODE["point"].append("U+3a90")
UNICODE_TO_BLISS["U+3a90"].append("point")
BLISS_TO_UNICODE["full stop"].append("U+3a90")
UNICODE_TO_BLISS["U+3a90"].append("full stop")
BLISS_TO_UNICODE["decimal point"].append("U+3a90")
UNICODE_TO_BLISS["U+3a90"].append("decimal point")
BLISS_TO_UNICODE["period,point,full stop,decimal point"] = ["U+3a90"]
UNICODE_TO_BLISS["U+3a90"].append("period,point,full stop,decimal point")
BLISS_TO_UNICODE["punctuation mark 1. used as punctuation in symbol sentences"] = ["U+3a91"]
UNICODE_TO_BLISS["U+3a91"] = ["punctuation mark 1. used as punctuation in symbol sentences"]
BLISS_TO_UNICODE["Scorpio"] = ["U+3a92"]
UNICODE_TO_BLISS["U+3a92"] = ["Scorpio"]
BLISS_TO_UNICODE["scorpion"] = ["U+3a93"]
UNICODE_TO_BLISS["U+3a93"] = ["scorpion"]
BLISS_TO_UNICODE["ice cream"] = ["U+3a94"]
UNICODE_TO_BLISS["U+3a94"] = ["ice cream"]
BLISS_TO_UNICODE["sherbet"] = ["U+3a94"]
UNICODE_TO_BLISS["U+3a94"].append("sherbet")
BLISS_TO_UNICODE["sorbet"] = ["U+3a94"]
UNICODE_TO_BLISS["U+3a94"].append("sorbet")
BLISS_TO_UNICODE["ice cream,sherbet,sorbet"] = ["U+3a94"]
UNICODE_TO_BLISS["U+3a94"].append("ice cream,sherbet,sorbet")
BLISS_TO_UNICODE["potty"] = ["U+3a95"]
UNICODE_TO_BLISS["U+3a95"] = ["potty"]
BLISS_TO_UNICODE["chamber pot"] = ["U+3a95"]
UNICODE_TO_BLISS["U+3a95"].append("chamber pot")
BLISS_TO_UNICODE["bedpan"] = ["U+3a95"]
UNICODE_TO_BLISS["U+3a95"].append("bedpan")
BLISS_TO_UNICODE["potty,chamber pot,bedpan"] = ["U+3a95"]
UNICODE_TO_BLISS["U+3a95"].append("potty,chamber pot,bedpan")
BLISS_TO_UNICODE["pictograph of a handle"] = ["U+3a96"]
UNICODE_TO_BLISS["U+3a96"] = ["pictograph of a handle"]
BLISS_TO_UNICODE["indoors"] = ["U+36d0"]
UNICODE_TO_BLISS["U+36d0"].append("indoors")
BLISS_TO_UNICODE["indoor,indoors"] = ["U+36d0"]
UNICODE_TO_BLISS["U+36d0"].append("indoor,indoors")
BLISS_TO_UNICODE["choose"] = ["U+3a97"]
UNICODE_TO_BLISS["U+3a97"] = ["choose"]
BLISS_TO_UNICODE["pick"] = ["U+3a97"]
UNICODE_TO_BLISS["U+3a97"].append("pick")
BLISS_TO_UNICODE["select"] = ["U+3a97"]
UNICODE_TO_BLISS["U+3a97"].append("select")
BLISS_TO_UNICODE["choose,pick,select"] = ["U+3a97"]
UNICODE_TO_BLISS["U+3a97"].append("choose,pick,select")
BLISS_TO_UNICODE["pole vaulting"] = ["U+3a98"]
UNICODE_TO_BLISS["U+3a98"] = ["pole vaulting"]
BLISS_TO_UNICODE["stander"] = ["U+3a99"]
UNICODE_TO_BLISS["U+3a99"] = ["stander"]
BLISS_TO_UNICODE["to stand"] = ["U+3a9a"]
UNICODE_TO_BLISS["U+3a9a"] = ["to stand"]
BLISS_TO_UNICODE["standing"] = ["U+3a9b"]
UNICODE_TO_BLISS["U+3a9b"] = ["standing"]
BLISS_TO_UNICODE["odometer"] = ["U+3a9c"]
UNICODE_TO_BLISS["U+3a9c"] = ["odometer"]
BLISS_TO_UNICODE["largeness"].append("U+3a66")
UNICODE_TO_BLISS["U+3a66"].append("largeness")
BLISS_TO_UNICODE["bigness,largeness"] = ["U+3a66"]
UNICODE_TO_BLISS["U+3a66"].append("bigness,largeness")
BLISS_TO_UNICODE["vertical line bounded by two horizontal reference lines"] = ["U+3a9d"]
UNICODE_TO_BLISS["U+3a9d"] = ["vertical line bounded by two horizontal reference lines"]
BLISS_TO_UNICODE["perfume"] = ["U+3a9e"]
UNICODE_TO_BLISS["U+3a9e"] = ["perfume"]
BLISS_TO_UNICODE["fragrance"] = ["U+3a9e"]
UNICODE_TO_BLISS["U+3a9e"].append("fragrance")
BLISS_TO_UNICODE["aroma"] = ["U+3a9e"]
UNICODE_TO_BLISS["U+3a9e"].append("aroma")
BLISS_TO_UNICODE["scent"] = ["U+3a9e"]
UNICODE_TO_BLISS["U+3a9e"].append("scent")
BLISS_TO_UNICODE["perfume,fragrance,aroma,scent"] = ["U+3a9e"]
UNICODE_TO_BLISS["U+3a9e"].append("perfume,fragrance,aroma,scent")
BLISS_TO_UNICODE["6"].append("U+3566")
UNICODE_TO_BLISS["U+3566"].append("6")
BLISS_TO_UNICODE["Arabic numeral 6"] = ["U+3a9f"]
UNICODE_TO_BLISS["U+3a9f"] = ["Arabic numeral 6"]
BLISS_TO_UNICODE["Russian"] = ["U+3aa0"]
UNICODE_TO_BLISS["U+3aa0"] = ["Russian"]
BLISS_TO_UNICODE["Russia"] = ["U+3aa1"]
UNICODE_TO_BLISS["U+3aa1"] = ["Russia"]
BLISS_TO_UNICODE["homework"] = ["U+3aa2"]
UNICODE_TO_BLISS["U+3aa2"] = ["homework"]
BLISS_TO_UNICODE["home studying"] = ["U+3aa2"]
UNICODE_TO_BLISS["U+3aa2"].append("home studying")
BLISS_TO_UNICODE["homework,home studying"] = ["U+3aa2"]
UNICODE_TO_BLISS["U+3aa2"].append("homework,home studying")
BLISS_TO_UNICODE["right triangle"] = ["U+3aa3"]
UNICODE_TO_BLISS["U+3aa3"] = ["right triangle"]
BLISS_TO_UNICODE["triangle"] = ["U+3aa4"]
UNICODE_TO_BLISS["U+3aa4"] = ["triangle"]
BLISS_TO_UNICODE["curiosity"] = ["U+3aa5"]
UNICODE_TO_BLISS["U+3aa5"] = ["curiosity"]
BLISS_TO_UNICODE["curiousness"] = ["U+3aa5"]
UNICODE_TO_BLISS["U+3aa5"].append("curiousness")
BLISS_TO_UNICODE["inquisitiveness"] = ["U+3aa5"]
UNICODE_TO_BLISS["U+3aa5"].append("inquisitiveness")
BLISS_TO_UNICODE["curiosity,curiousness,inquisitiveness"] = ["U+3aa5"]
UNICODE_TO_BLISS["U+3aa5"].append("curiosity,curiousness,inquisitiveness")
BLISS_TO_UNICODE["discount store"] = ["U+3aa6"]
UNICODE_TO_BLISS["U+3aa6"] = ["discount store"]
BLISS_TO_UNICODE["discount"] = ["U+3aa7"]
UNICODE_TO_BLISS["U+3aa7"] = ["discount"]
BLISS_TO_UNICODE["woodwind instrument"] = ["U+3aa8"]
UNICODE_TO_BLISS["U+3aa8"] = ["woodwind instrument"]
BLISS_TO_UNICODE["body of learning"].append("U+32dc")
UNICODE_TO_BLISS["U+32dc"].append("body of learning")
BLISS_TO_UNICODE["science,body of learning"] = ["U+32dc"]
UNICODE_TO_BLISS["U+32dc"].append("science,body of learning")
BLISS_TO_UNICODE["causality"] = ["U+3aa9"]
UNICODE_TO_BLISS["U+3aa9"] = ["causality"]
BLISS_TO_UNICODE["shopping centre"] = ["U+3aaa"]
UNICODE_TO_BLISS["U+3aaa"] = ["shopping centre"]
BLISS_TO_UNICODE["mall"] = ["U+3aaa"]
UNICODE_TO_BLISS["U+3aaa"].append("mall")
BLISS_TO_UNICODE["plaza"] = ["U+3aaa"]
UNICODE_TO_BLISS["U+3aaa"].append("plaza")
BLISS_TO_UNICODE["shopping centre,mall,plaza"] = ["U+3aaa"]
UNICODE_TO_BLISS["U+3aaa"].append("shopping centre,mall,plaza")
BLISS_TO_UNICODE["roe deer"] = ["U+3aab"]
UNICODE_TO_BLISS["U+3aab"] = ["roe deer"]
BLISS_TO_UNICODE["deer"] = ["U+3aac"]
UNICODE_TO_BLISS["U+3aac"] = ["deer"]
BLISS_TO_UNICODE["learn"] = ["U+3aad"]
UNICODE_TO_BLISS["U+3aad"] = ["learn"]
BLISS_TO_UNICODE["desk"] = ["U+3aae"]
UNICODE_TO_BLISS["U+3aae"] = ["desk"]
BLISS_TO_UNICODE["worktable"] = ["U+3aae"]
UNICODE_TO_BLISS["U+3aae"].append("worktable")
BLISS_TO_UNICODE["work table"] = ["U+3aae"]
UNICODE_TO_BLISS["U+3aae"].append("work table")
BLISS_TO_UNICODE["desk,worktable,work table"] = ["U+3aae"]
UNICODE_TO_BLISS["U+3aae"].append("desk,worktable,work table")
BLISS_TO_UNICODE["gull"] = ["U+3aaf"]
UNICODE_TO_BLISS["U+3aaf"] = ["gull"]
BLISS_TO_UNICODE["seagull"] = ["U+3aaf"]
UNICODE_TO_BLISS["U+3aaf"].append("seagull")
BLISS_TO_UNICODE["sea gull"] = ["U+3aaf"]
UNICODE_TO_BLISS["U+3aaf"].append("sea gull")
BLISS_TO_UNICODE["gull,seagull,sea gull"] = ["U+3aaf"]
UNICODE_TO_BLISS["U+3aaf"].append("gull,seagull,sea gull")
BLISS_TO_UNICODE["water bird"] = ["U+3ab0"]
UNICODE_TO_BLISS["U+3ab0"] = ["water bird"]
BLISS_TO_UNICODE["masculine"] = ["U+33ee"]
UNICODE_TO_BLISS["U+33ee"].append("masculine")
BLISS_TO_UNICODE["male,masculine"] = ["U+33ee"]
UNICODE_TO_BLISS["U+33ee"].append("male,masculine")
BLISS_TO_UNICODE["male"].append("U+34f4")
UNICODE_TO_BLISS["U+34f4"].append("male")
BLISS_TO_UNICODE["man,male"] = ["U+34f4"]
UNICODE_TO_BLISS["U+34f4"].append("man,male")
BLISS_TO_UNICODE["speech therapy room"] = ["U+3ab1"]
UNICODE_TO_BLISS["U+3ab1"] = ["speech therapy room"]
BLISS_TO_UNICODE["speech therapy"] = ["U+3ab2"]
UNICODE_TO_BLISS["U+3ab2"] = ["speech therapy"]
BLISS_TO_UNICODE["gallop"] = ["U+3ab3"]
UNICODE_TO_BLISS["U+3ab3"] = ["gallop"]
BLISS_TO_UNICODE["canter"] = ["U+3ab4"]
UNICODE_TO_BLISS["U+3ab4"] = ["canter"]
BLISS_TO_UNICODE["autumn"] = ["U+3ab5"]
UNICODE_TO_BLISS["U+3ab5"] = ["autumn"]
BLISS_TO_UNICODE["fall"].append("U+3ab5")
UNICODE_TO_BLISS["U+3ab5"].append("fall")
BLISS_TO_UNICODE["autumn,fall"] = ["U+3ab5"]
UNICODE_TO_BLISS["U+3ab5"].append("autumn,fall")
BLISS_TO_UNICODE["salty"] = ["U+3ab6"]
UNICODE_TO_BLISS["U+3ab6"] = ["salty"]
BLISS_TO_UNICODE["hearing"] = ["U+3ab7"]
UNICODE_TO_BLISS["U+3ab7"] = ["hearing"]
BLISS_TO_UNICODE["wear"] = ["U+3994"]
UNICODE_TO_BLISS["U+3994"].append("wear")
BLISS_TO_UNICODE["dress,wear"] = ["U+3994"]
UNICODE_TO_BLISS["U+3994"].append("dress,wear")
BLISS_TO_UNICODE["sentence"] = ["U+3ab8"]
UNICODE_TO_BLISS["U+3ab8"] = ["sentence"]
BLISS_TO_UNICODE["condemn"] = ["U+3ab8"]
UNICODE_TO_BLISS["U+3ab8"].append("condemn")
BLISS_TO_UNICODE["sentence,condemn"] = ["U+3ab8"]
UNICODE_TO_BLISS["U+3ab8"].append("sentence,condemn")
BLISS_TO_UNICODE["guilty"] = ["U+3ab9"]
UNICODE_TO_BLISS["U+3ab9"] = ["guilty"]
BLISS_TO_UNICODE["increase"] = ["U+3aba"]
UNICODE_TO_BLISS["U+3aba"] = ["increase"]
BLISS_TO_UNICODE["enlarge"] = ["U+3aba"]
UNICODE_TO_BLISS["U+3aba"].append("enlarge")
BLISS_TO_UNICODE["increase,enlarge"] = ["U+3aba"]
UNICODE_TO_BLISS["U+3aba"].append("increase,enlarge")
BLISS_TO_UNICODE["sacked"] = ["U+3abb"]
UNICODE_TO_BLISS["U+3abb"] = ["sacked"]
BLISS_TO_UNICODE["dismissed"] = ["U+3abb"]
UNICODE_TO_BLISS["U+3abb"].append("dismissed")
BLISS_TO_UNICODE["sacked,dismissed"] = ["U+3abb"]
UNICODE_TO_BLISS["U+3abb"].append("sacked,dismissed")
BLISS_TO_UNICODE["dismissal"] = ["U+3abc"]
UNICODE_TO_BLISS["U+3abc"] = ["dismissal"]
BLISS_TO_UNICODE["work method"] = ["U+3abd"]
UNICODE_TO_BLISS["U+3abd"] = ["work method"]
BLISS_TO_UNICODE["factory"] = ["U+3abe"]
UNICODE_TO_BLISS["U+3abe"] = ["factory"]
BLISS_TO_UNICODE["plant"].append("U+3abe")
UNICODE_TO_BLISS["U+3abe"].append("plant")
BLISS_TO_UNICODE["factory,plant"] = ["U+3abe"]
UNICODE_TO_BLISS["U+3abe"].append("factory,plant")
BLISS_TO_UNICODE["Israel"] = ["U+3abf"]
UNICODE_TO_BLISS["U+3abf"] = ["Israel"]
BLISS_TO_UNICODE["aeroplane"] = ["U+3312"]
UNICODE_TO_BLISS["U+3312"].append("aeroplane")
BLISS_TO_UNICODE["plane"] = ["U+3312"]
UNICODE_TO_BLISS["U+3312"].append("plane")
BLISS_TO_UNICODE["airplane,aeroplane,plane"] = ["U+3312"]
UNICODE_TO_BLISS["U+3312"].append("airplane,aeroplane,plane")
BLISS_TO_UNICODE["soft cheese"] = ["U+3ac0"]
UNICODE_TO_BLISS["U+3ac0"] = ["soft cheese"]
BLISS_TO_UNICODE["rowdy"] = ["U+3ac1"]
UNICODE_TO_BLISS["U+3ac1"] = ["rowdy"]
BLISS_TO_UNICODE["row"] = ["U+3ac2"]
UNICODE_TO_BLISS["U+3ac2"] = ["row"]
BLISS_TO_UNICODE["niece or nephew"] = ["U+3ac3"]
UNICODE_TO_BLISS["U+3ac3"] = ["niece or nephew"]
BLISS_TO_UNICODE["sibling"] = ["U+3ac4"]
UNICODE_TO_BLISS["U+3ac4"] = ["sibling"]
BLISS_TO_UNICODE["volleyball"] = ["U+3ac5"]
UNICODE_TO_BLISS["U+3ac5"] = ["volleyball"]
BLISS_TO_UNICODE["to hit"] = ["U+3ac6"]
UNICODE_TO_BLISS["U+3ac6"] = ["to hit"]
BLISS_TO_UNICODE["duck"] = ["U+3ac7"]
UNICODE_TO_BLISS["U+3ac7"] = ["duck"]
BLISS_TO_UNICODE["bird"].append("U+3ac7")
UNICODE_TO_BLISS["U+3ac7"].append("bird")
BLISS_TO_UNICODE["waterbird"].append("U+3ac7")
UNICODE_TO_BLISS["U+3ac7"].append("waterbird")
BLISS_TO_UNICODE["waterfowl"] = ["U+3ac7"]
UNICODE_TO_BLISS["U+3ac7"].append("waterfowl")
BLISS_TO_UNICODE["seabird"] = ["U+3ac7"]
UNICODE_TO_BLISS["U+3ac7"].append("seabird")
BLISS_TO_UNICODE["seafowl"] = ["U+3ac7"]
UNICODE_TO_BLISS["U+3ac7"].append("seafowl")
BLISS_TO_UNICODE["duck,bird"] = ["U+3ac7"]
UNICODE_TO_BLISS["U+3ac7"].append("duck,bird")
BLISS_TO_UNICODE["basic"] = ["U+38e3"]
UNICODE_TO_BLISS["U+38e3"].append("basic")
BLISS_TO_UNICODE["fundamental,basic"] = ["U+38e3"]
UNICODE_TO_BLISS["U+38e3"].append("fundamental,basic")
BLISS_TO_UNICODE["Hebrew"] = ["U+3ac8"]
UNICODE_TO_BLISS["U+3ac8"] = ["Hebrew"]
BLISS_TO_UNICODE["asparagus"] = ["U+3ac9"]
UNICODE_TO_BLISS["U+3ac9"] = ["asparagus"]
BLISS_TO_UNICODE["root"] = ["U+3aca"]
UNICODE_TO_BLISS["U+3aca"] = ["root"]
BLISS_TO_UNICODE["foam"] = ["U+3acb"]
UNICODE_TO_BLISS["U+3acb"] = ["foam"]
BLISS_TO_UNICODE["mousse"] = ["U+3acb"]
UNICODE_TO_BLISS["U+3acb"].append("mousse")
BLISS_TO_UNICODE["foam,mousse"] = ["U+3acb"]
UNICODE_TO_BLISS["U+3acb"].append("foam,mousse")
BLISS_TO_UNICODE["substitute"] = ["U+3234"]
UNICODE_TO_BLISS["U+3234"].append("substitute")
BLISS_TO_UNICODE["trade"].append("U+3234")
UNICODE_TO_BLISS["U+3234"].append("trade")
BLISS_TO_UNICODE["exchange,substitute,trade"] = ["U+3234"]
UNICODE_TO_BLISS["U+3234"].append("exchange,substitute,trade")
BLISS_TO_UNICODE["card"].append("U+3396")
UNICODE_TO_BLISS["U+3396"].append("card")
BLISS_TO_UNICODE["page"].append("U+3396")
UNICODE_TO_BLISS["U+3396"].append("page")
BLISS_TO_UNICODE["paper,card,page"] = ["U+3396"]
UNICODE_TO_BLISS["U+3396"].append("paper,card,page")
BLISS_TO_UNICODE["its"] = ["U+3acc"]
UNICODE_TO_BLISS["U+3acc"] = ["its"]
BLISS_TO_UNICODE["astrology"] = ["U+3acd"]
UNICODE_TO_BLISS["U+3acd"] = ["astrology"]
BLISS_TO_UNICODE["quick"] = ["U+3ace"]
UNICODE_TO_BLISS["U+3ace"] = ["quick"]
BLISS_TO_UNICODE["fast"].append("U+3ace")
UNICODE_TO_BLISS["U+3ace"].append("fast")
BLISS_TO_UNICODE["quickly"] = ["U+3ace"]
UNICODE_TO_BLISS["U+3ace"].append("quickly")
BLISS_TO_UNICODE["rapid"] = ["U+3ace"]
UNICODE_TO_BLISS["U+3ace"].append("rapid")
BLISS_TO_UNICODE["rapidly"] = ["U+3ace"]
UNICODE_TO_BLISS["U+3ace"].append("rapidly")
BLISS_TO_UNICODE["quick,fast,quickly,rapid,rapidly"] = ["U+3ace"]
UNICODE_TO_BLISS["U+3ace"].append("quick,fast,quickly,rapid,rapidly")
BLISS_TO_UNICODE["child care"] = ["U+3acf"]
UNICODE_TO_BLISS["U+3acf"] = ["child care"]
BLISS_TO_UNICODE["civil engineer"] = ["U+3ad0"]
UNICODE_TO_BLISS["U+3ad0"] = ["civil engineer"]
BLISS_TO_UNICODE["colleague"] = ["U+3ad1"]
UNICODE_TO_BLISS["U+3ad1"] = ["colleague"]
BLISS_TO_UNICODE["equal"] = ["U+3ad2"]
UNICODE_TO_BLISS["U+3ad2"] = ["equal"]
BLISS_TO_UNICODE["hysterectomy"] = ["U+3ad3"]
UNICODE_TO_BLISS["U+3ad3"] = ["hysterectomy"]
BLISS_TO_UNICODE["fire place"] = ["U+3ad4"]
UNICODE_TO_BLISS["U+3ad4"] = ["fire place"]
BLISS_TO_UNICODE["campfire site"] = ["U+3ad4"]
UNICODE_TO_BLISS["U+3ad4"].append("campfire site")
BLISS_TO_UNICODE["fire place,campfire site"] = ["U+3ad4"]
UNICODE_TO_BLISS["U+3ad4"].append("fire place,campfire site")
BLISS_TO_UNICODE["stove"] = ["U+3ad5"]
UNICODE_TO_BLISS["U+3ad5"] = ["stove"]
BLISS_TO_UNICODE["suggest"] = ["U+3ad6"]
UNICODE_TO_BLISS["U+3ad6"] = ["suggest"]
BLISS_TO_UNICODE["propose"] = ["U+3ad6"]
UNICODE_TO_BLISS["U+3ad6"].append("propose")
BLISS_TO_UNICODE["suggest,propose"] = ["U+3ad6"]
UNICODE_TO_BLISS["U+3ad6"].append("suggest,propose")
BLISS_TO_UNICODE["suggestion"] = ["U+3ad7"]
UNICODE_TO_BLISS["U+3ad7"] = ["suggestion"]
BLISS_TO_UNICODE["hot spring"] = ["U+3ad8"]
UNICODE_TO_BLISS["U+3ad8"] = ["hot spring"]
BLISS_TO_UNICODE["spring water"] = ["U+3ad9"]
UNICODE_TO_BLISS["U+3ad9"] = ["spring water"]
BLISS_TO_UNICODE["snowball"] = ["U+3ada"]
UNICODE_TO_BLISS["U+3ada"] = ["snowball"]
BLISS_TO_UNICODE["sea captain"] = ["U+3adb"]
UNICODE_TO_BLISS["U+3adb"] = ["sea captain"]
BLISS_TO_UNICODE["skipper"] = ["U+3adb"]
UNICODE_TO_BLISS["U+3adb"].append("skipper")
BLISS_TO_UNICODE["sea captain,skipper"] = ["U+3adb"]
UNICODE_TO_BLISS["U+3adb"].append("sea captain,skipper")
BLISS_TO_UNICODE["misuse"] = ["U+3adc"]
UNICODE_TO_BLISS["U+3adc"] = ["misuse"]
BLISS_TO_UNICODE["reflexologist"] = ["U+3add"]
UNICODE_TO_BLISS["U+3add"] = ["reflexologist"]
BLISS_TO_UNICODE["always"] = ["U+3ade"]
UNICODE_TO_BLISS["U+3ade"] = ["always"]
BLISS_TO_UNICODE["ever"] = ["U+3ade"]
UNICODE_TO_BLISS["U+3ade"].append("ever")
BLISS_TO_UNICODE["forever"] = ["U+3ade"]
UNICODE_TO_BLISS["U+3ade"].append("forever")
BLISS_TO_UNICODE["always,ever,forever"] = ["U+3ade"]
UNICODE_TO_BLISS["U+3ade"].append("always,ever,forever")
BLISS_TO_UNICODE["knight"] = ["U+3adf"]
UNICODE_TO_BLISS["U+3adf"] = ["knight"]
BLISS_TO_UNICODE["Bliss"] = ["U+3ae0"]
UNICODE_TO_BLISS["U+3ae0"] = ["Bliss"]
BLISS_TO_UNICODE["Bliss language"] = ["U+3ae0"]
UNICODE_TO_BLISS["U+3ae0"].append("Bliss language")
BLISS_TO_UNICODE["Blissymbolics"] = ["U+3ae0"]
UNICODE_TO_BLISS["U+3ae0"].append("Blissymbolics")
BLISS_TO_UNICODE["Bliss,Bliss language,Blissymbolics"] = ["U+3ae0"]
UNICODE_TO_BLISS["U+3ae0"].append("Bliss,Bliss language,Blissymbolics")
BLISS_TO_UNICODE["Blissymbol"] = ["U+3ae1"]
UNICODE_TO_BLISS["U+3ae1"] = ["Blissymbol"]
BLISS_TO_UNICODE["flashlight"] = ["U+3ae2"]
UNICODE_TO_BLISS["U+3ae2"] = ["flashlight"]
BLISS_TO_UNICODE["lantern"] = ["U+3ae2"]
UNICODE_TO_BLISS["U+3ae2"].append("lantern")
BLISS_TO_UNICODE["flashlight,lantern"] = ["U+3ae2"]
UNICODE_TO_BLISS["U+3ae2"].append("flashlight,lantern")
BLISS_TO_UNICODE["burned out"] = ["U+3ae3"]
UNICODE_TO_BLISS["U+3ae3"] = ["burned out"]
BLISS_TO_UNICODE["burnt out"] = ["U+3ae3"]
UNICODE_TO_BLISS["U+3ae3"].append("burnt out")
BLISS_TO_UNICODE["burned-out,burnt-out"] = ["U+3ae3"]
UNICODE_TO_BLISS["U+3ae3"].append("burned-out,burnt-out")
BLISS_TO_UNICODE["decrease"] = ["U+3ae4"]
UNICODE_TO_BLISS["U+3ae4"] = ["decrease"]
BLISS_TO_UNICODE["reduce"] = ["U+3ae4"]
UNICODE_TO_BLISS["U+3ae4"].append("reduce")
BLISS_TO_UNICODE["decrease,reduce"] = ["U+3ae4"]
UNICODE_TO_BLISS["U+3ae4"].append("decrease,reduce")
BLISS_TO_UNICODE["Sabbath"] = ["U+3ae5"]
UNICODE_TO_BLISS["U+3ae5"] = ["Sabbath"]
BLISS_TO_UNICODE["day of rest"] = ["U+3ae5"]
UNICODE_TO_BLISS["U+3ae5"].append("day of rest")
BLISS_TO_UNICODE["Sabbath,day of rest"] = ["U+3ae5"]
UNICODE_TO_BLISS["U+3ae5"].append("Sabbath,day of rest")
BLISS_TO_UNICODE["measure"] = ["U+350e"]
UNICODE_TO_BLISS["U+350e"].append("measure")
BLISS_TO_UNICODE["measurement,measure"] = ["U+350e"]
UNICODE_TO_BLISS["U+350e"].append("measurement,measure")
BLISS_TO_UNICODE["shortness"] = ["U+3ae6"]
UNICODE_TO_BLISS["U+3ae6"] = ["shortness"]
BLISS_TO_UNICODE["measurement"].append("U+36dd")
UNICODE_TO_BLISS["U+36dd"].append("measurement")
BLISS_TO_UNICODE["scale,measurement"] = ["U+36dd"]
UNICODE_TO_BLISS["U+36dd"].append("scale,measurement")
BLISS_TO_UNICODE["lowness"] = ["U+3ae7"]
UNICODE_TO_BLISS["U+3ae7"] = ["lowness"]
BLISS_TO_UNICODE["real"] = ["U+3ae8"]
UNICODE_TO_BLISS["U+3ae8"] = ["real"]
BLISS_TO_UNICODE["really"] = ["U+3ae8"]
UNICODE_TO_BLISS["U+3ae8"].append("really")
BLISS_TO_UNICODE["real,really"] = ["U+3ae8"]
UNICODE_TO_BLISS["U+3ae8"].append("real,really")
BLISS_TO_UNICODE["try"] = ["U+3ae9"]
UNICODE_TO_BLISS["U+3ae9"] = ["try"]
BLISS_TO_UNICODE["attempt"] = ["U+3ae9"]
UNICODE_TO_BLISS["U+3ae9"].append("attempt")
BLISS_TO_UNICODE["try,attempt"] = ["U+3ae9"]
UNICODE_TO_BLISS["U+3ae9"].append("try,attempt")
BLISS_TO_UNICODE["psychology"] = ["U+3aea"]
UNICODE_TO_BLISS["U+3aea"] = ["psychology"]
BLISS_TO_UNICODE["body of knowledge"] = ["U+3aeb"]
UNICODE_TO_BLISS["U+3aeb"] = ["body of knowledge"]
BLISS_TO_UNICODE["research"] = ["U+3aec"]
UNICODE_TO_BLISS["U+3aec"] = ["research"]
BLISS_TO_UNICODE["belief"] = ["U+3aed"]
UNICODE_TO_BLISS["U+3aed"] = ["belief"]
BLISS_TO_UNICODE["hypothesis"] = ["U+3aee"]
UNICODE_TO_BLISS["U+3aee"] = ["hypothesis"]
BLISS_TO_UNICODE["theory"] = ["U+3aef"]
UNICODE_TO_BLISS["U+3aef"] = ["theory"]
BLISS_TO_UNICODE["racket sport"] = ["U+3296"]
UNICODE_TO_BLISS["U+3296"].append("racket sport")
BLISS_TO_UNICODE["racquet sport"] = ["U+3296"]
UNICODE_TO_BLISS["U+3296"].append("racquet sport")
BLISS_TO_UNICODE["tennis,racket sport,racquet sport"] = ["U+3296"]
UNICODE_TO_BLISS["U+3296"].append("tennis,racket sport,racquet sport")
BLISS_TO_UNICODE["table tennis"] = ["U+3af0"]
UNICODE_TO_BLISS["U+3af0"] = ["table tennis"]
BLISS_TO_UNICODE["ping pong"] = ["U+3af0"]
UNICODE_TO_BLISS["U+3af0"].append("ping pong")
BLISS_TO_UNICODE["table tennis,ping-pong"] = ["U+3af0"]
UNICODE_TO_BLISS["U+3af0"].append("table tennis,ping-pong")
BLISS_TO_UNICODE["flight deck"] = ["U+3af1"]
UNICODE_TO_BLISS["U+3af1"] = ["flight deck"]
BLISS_TO_UNICODE["cockpit"] = ["U+3af1"]
UNICODE_TO_BLISS["U+3af1"].append("cockpit")
BLISS_TO_UNICODE["flight deck,cockpit"] = ["U+3af1"]
UNICODE_TO_BLISS["U+3af1"].append("flight deck,cockpit")
BLISS_TO_UNICODE["pilot"] = ["U+3af2"]
UNICODE_TO_BLISS["U+3af2"] = ["pilot"]
BLISS_TO_UNICODE["old age pension"] = ["U+3af3"]
UNICODE_TO_BLISS["U+3af3"] = ["old age pension"]
BLISS_TO_UNICODE["old-age pension"] = ["U+3af3"]
UNICODE_TO_BLISS["U+3af3"].append("old-age pension")
BLISS_TO_UNICODE["suntan"] = ["U+3af4"]
UNICODE_TO_BLISS["U+3af4"] = ["suntan"]
BLISS_TO_UNICODE["definition"] = ["U+3af5"]
UNICODE_TO_BLISS["U+3af5"] = ["definition"]
BLISS_TO_UNICODE["explanation"] = ["U+3af6"]
UNICODE_TO_BLISS["U+3af6"] = ["explanation"]
BLISS_TO_UNICODE["dead person"] = ["U+3af7"]
UNICODE_TO_BLISS["U+3af7"] = ["dead person"]
BLISS_TO_UNICODE["media player"] = ["U+3af8"]
UNICODE_TO_BLISS["U+3af8"] = ["media player"]
BLISS_TO_UNICODE["digital device"] = ["U+3af9"]
UNICODE_TO_BLISS["U+3af9"] = ["digital device"]
BLISS_TO_UNICODE["repair shop"] = ["U+3afa"]
UNICODE_TO_BLISS["U+3afa"] = ["repair shop"]
BLISS_TO_UNICODE["to repair"] = ["U+3afb"]
UNICODE_TO_BLISS["U+3afb"] = ["to repair"]
BLISS_TO_UNICODE["porpoise"] = ["U+3304"]
UNICODE_TO_BLISS["U+3304"].append("porpoise")
BLISS_TO_UNICODE["dolphin,porpoise"] = ["U+3304"]
UNICODE_TO_BLISS["U+3304"].append("dolphin,porpoise")
BLISS_TO_UNICODE["pictograph of a tail fin"] = ["U+3afc"]
UNICODE_TO_BLISS["U+3afc"] = ["pictograph of a tail fin"]
BLISS_TO_UNICODE["suit of armour"] = ["U+3afd"]
UNICODE_TO_BLISS["U+3afd"] = ["suit of armour"]
BLISS_TO_UNICODE["international symbol"] = ["U+3afe"]
UNICODE_TO_BLISS["U+3afe"] = ["international symbol"]
BLISS_TO_UNICODE["slipper"] = ["U+3aff"]
UNICODE_TO_BLISS["U+3aff"] = ["slipper"]
BLISS_TO_UNICODE["shoe"] = ["U+3b00"]
UNICODE_TO_BLISS["U+3b00"] = ["shoe"]
BLISS_TO_UNICODE["florist"] = ["U+3b01"]
UNICODE_TO_BLISS["U+3b01"] = ["florist"]
BLISS_TO_UNICODE["glitter"] = ["U+3b02"]
UNICODE_TO_BLISS["U+3b02"] = ["glitter"]
BLISS_TO_UNICODE["lump"] = ["U+3b03"]
UNICODE_TO_BLISS["U+3b03"] = ["lump"]
BLISS_TO_UNICODE["estimation"] = ["U+3677"]
UNICODE_TO_BLISS["U+3677"].append("estimation")
BLISS_TO_UNICODE["guess,estimation"] = ["U+3677"]
UNICODE_TO_BLISS["U+3677"].append("guess,estimation")
BLISS_TO_UNICODE["visitor"] = ["U+3b04"]
UNICODE_TO_BLISS["U+3b04"] = ["visitor"]
BLISS_TO_UNICODE["guest"] = ["U+3b04"]
UNICODE_TO_BLISS["U+3b04"].append("guest")
BLISS_TO_UNICODE["visitor,guest"] = ["U+3b04"]
UNICODE_TO_BLISS["U+3b04"].append("visitor,guest")
BLISS_TO_UNICODE["jet"] = ["U+3b05"]
UNICODE_TO_BLISS["U+3b05"] = ["jet"]
BLISS_TO_UNICODE["jet plane"] = ["U+3b05"]
UNICODE_TO_BLISS["U+3b05"].append("jet plane")
BLISS_TO_UNICODE["jet,jet plane"] = ["U+3b05"]
UNICODE_TO_BLISS["U+3b05"].append("jet,jet plane")
BLISS_TO_UNICODE["hypodermic needlepoint"] = ["U+3b06"]
UNICODE_TO_BLISS["U+3b06"] = ["hypodermic needlepoint"]
BLISS_TO_UNICODE["saint"] = ["U+3b07"]
UNICODE_TO_BLISS["U+3b07"] = ["saint"]
BLISS_TO_UNICODE["lawn mower"] = ["U+3b08"]
UNICODE_TO_BLISS["U+3b08"] = ["lawn mower"]
BLISS_TO_UNICODE["mower"] = ["U+3b08"]
UNICODE_TO_BLISS["U+3b08"].append("mower")
BLISS_TO_UNICODE["lawn mower,mower"] = ["U+3b08"]
UNICODE_TO_BLISS["U+3b08"].append("lawn mower,mower")
BLISS_TO_UNICODE["fossil fuel"] = ["U+3b09"]
UNICODE_TO_BLISS["U+3b09"] = ["fossil fuel"]
BLISS_TO_UNICODE["coal"] = ["U+3b09"]
UNICODE_TO_BLISS["U+3b09"].append("coal")
BLISS_TO_UNICODE["fossil fuel,coal"] = ["U+3b09"]
UNICODE_TO_BLISS["U+3b09"].append("fossil fuel,coal")
BLISS_TO_UNICODE["passed time"] = ["U+3b0a"]
UNICODE_TO_BLISS["U+3b0a"] = ["passed time"]
BLISS_TO_UNICODE["be afraid"] = ["U+3a27"]
UNICODE_TO_BLISS["U+3a27"].append("be afraid")
BLISS_TO_UNICODE["dread"] = ["U+3a27"]
UNICODE_TO_BLISS["U+3a27"].append("dread")
BLISS_TO_UNICODE["fear,be afraid,dread"] = ["U+3a27"]
UNICODE_TO_BLISS["U+3a27"].append("fear,be afraid,dread")
BLISS_TO_UNICODE["afraid"] = ["U+3b0b"]
UNICODE_TO_BLISS["U+3b0b"] = ["afraid"]
BLISS_TO_UNICODE["sailing boat"] = ["U+3491"]
UNICODE_TO_BLISS["U+3491"].append("sailing boat")
BLISS_TO_UNICODE["yacht"] = ["U+3491"]
UNICODE_TO_BLISS["U+3491"].append("yacht")
BLISS_TO_UNICODE["sailboat,sailing boat,yacht"] = ["U+3491"]
UNICODE_TO_BLISS["U+3491"].append("sailboat,sailing boat,yacht")
BLISS_TO_UNICODE["interviewer"] = ["U+3b0c"]
UNICODE_TO_BLISS["U+3b0c"] = ["interviewer"]
BLISS_TO_UNICODE["interview"] = ["U+3b0d"]
UNICODE_TO_BLISS["U+3b0d"] = ["interview"]
BLISS_TO_UNICODE["grace"] = ["U+3b0e"]
UNICODE_TO_BLISS["U+3b0e"] = ["grace"]
BLISS_TO_UNICODE["melting"].append("U+3868")
UNICODE_TO_BLISS["U+3868"].append("melting")
BLISS_TO_UNICODE["thawing,melting"] = ["U+3868"]
UNICODE_TO_BLISS["U+3868"].append("thawing,melting")
BLISS_TO_UNICODE["Cancer"] = ["U+3b0f"]
UNICODE_TO_BLISS["U+3b0f"] = ["Cancer"]
BLISS_TO_UNICODE["tummy"] = ["U+334b"]
UNICODE_TO_BLISS["U+334b"].append("tummy")
BLISS_TO_UNICODE["tum"] = ["U+334b"]
UNICODE_TO_BLISS["U+334b"].append("tum")
BLISS_TO_UNICODE["stomach,tummy,tum"] = ["U+334b"]
UNICODE_TO_BLISS["U+334b"].append("stomach,tummy,tum")
BLISS_TO_UNICODE["wedding"] = ["U+33f8"]
UNICODE_TO_BLISS["U+33f8"].append("wedding")
BLISS_TO_UNICODE["marriage,wedding"] = ["U+33f8"]
UNICODE_TO_BLISS["U+33f8"].append("marriage,wedding")
BLISS_TO_UNICODE["knee pad"] = ["U+3b10"]
UNICODE_TO_BLISS["U+3b10"] = ["knee pad"]
BLISS_TO_UNICODE["brightness"].append("U+3943")
UNICODE_TO_BLISS["U+3943"].append("brightness")
BLISS_TO_UNICODE["cleverness"].append("U+3943")
UNICODE_TO_BLISS["U+3943"].append("cleverness")
BLISS_TO_UNICODE["intelligence"].append("U+3943")
UNICODE_TO_BLISS["U+3943"].append("intelligence")
BLISS_TO_UNICODE["smartness,brightness,cleverness,intelligence"] = ["U+3943"]
UNICODE_TO_BLISS["U+3943"].append("smartness,brightness,cleverness,intelligence")
BLISS_TO_UNICODE["mother's milk"] = ["U+3b11"]
UNICODE_TO_BLISS["U+3b11"] = ["mother's milk"]
BLISS_TO_UNICODE["sell"] = ["U+3b12"]
UNICODE_TO_BLISS["U+3b12"] = ["sell"]
BLISS_TO_UNICODE["heterosexual"] = ["U+3b13"]
UNICODE_TO_BLISS["U+3b13"] = ["heterosexual"]
BLISS_TO_UNICODE["heterosexuality"] = ["U+3b14"]
UNICODE_TO_BLISS["U+3b14"] = ["heterosexuality"]
BLISS_TO_UNICODE["also"] = ["U+3434"]
UNICODE_TO_BLISS["U+3434"].append("also")
BLISS_TO_UNICODE["plus"].append("U+3434")
UNICODE_TO_BLISS["U+3434"].append("plus")
BLISS_TO_UNICODE["too"] = ["U+3434"]
UNICODE_TO_BLISS["U+3434"].append("too")
BLISS_TO_UNICODE["and,also,plus,too"] = ["U+3434"]
UNICODE_TO_BLISS["U+3434"].append("and,also,plus,too")
BLISS_TO_UNICODE["mood"] = ["U+3b15"]
UNICODE_TO_BLISS["U+3b15"] = ["mood"]
BLISS_TO_UNICODE["depression"].append("U+36a8")
UNICODE_TO_BLISS["U+36a8"].append("depression")
BLISS_TO_UNICODE["imprint,depression"] = ["U+36a8"]
UNICODE_TO_BLISS["U+36a8"].append("imprint,depression")
BLISS_TO_UNICODE["pictograph of impression"] = ["U+3b16"]
UNICODE_TO_BLISS["U+3b16"] = ["pictograph of impression"]
BLISS_TO_UNICODE[" like made by a thumb pressed into something soft"] = ["U+3b17"]
UNICODE_TO_BLISS["U+3b17"] = [" like made by a thumb pressed into something soft"]
BLISS_TO_UNICODE["recreation"] = ["U+363a"]
UNICODE_TO_BLISS["U+363a"].append("recreation")
BLISS_TO_UNICODE["play,recreation"] = ["U+363a"]
UNICODE_TO_BLISS["U+363a"].append("play,recreation")
BLISS_TO_UNICODE["play"].append("U+325a")
UNICODE_TO_BLISS["U+325a"].append("play")
BLISS_TO_UNICODE["turn,play"] = ["U+325a"]
UNICODE_TO_BLISS["U+325a"].append("turn,play")
BLISS_TO_UNICODE["blackboard"] = ["U+3b18"]
UNICODE_TO_BLISS["U+3b18"] = ["blackboard"]
BLISS_TO_UNICODE["chalkboard"] = ["U+3b18"]
UNICODE_TO_BLISS["U+3b18"].append("chalkboard")
BLISS_TO_UNICODE["whiteboard"] = ["U+3b18"]
UNICODE_TO_BLISS["U+3b18"].append("whiteboard")
BLISS_TO_UNICODE["writing board"] = ["U+3b18"]
UNICODE_TO_BLISS["U+3b18"].append("writing board")
BLISS_TO_UNICODE["blackboard,chalkboard,whiteboard,writing board"] = ["U+3b18"]
UNICODE_TO_BLISS["U+3b18"].append("blackboard,chalkboard,whiteboard,writing board")
BLISS_TO_UNICODE["yawn"] = ["U+3b19"]
UNICODE_TO_BLISS["U+3b19"] = ["yawn"]
BLISS_TO_UNICODE["to sleep"] = ["U+3b1a"]
UNICODE_TO_BLISS["U+3b1a"] = ["to sleep"]
BLISS_TO_UNICODE["program"] = ["U+3b1b"]
UNICODE_TO_BLISS["U+3b1b"] = ["program"]
BLISS_TO_UNICODE["to destroy"] = ["U+3b1c"]
UNICODE_TO_BLISS["U+3b1c"] = ["to destroy"]
BLISS_TO_UNICODE["micro-organism"] = ["U+3b1d"]
UNICODE_TO_BLISS["U+3b1d"] = ["micro-organism"]
BLISS_TO_UNICODE["duplicate"] = ["U+3b1e"]
UNICODE_TO_BLISS["U+3b1e"] = ["duplicate"]
BLISS_TO_UNICODE["plan,design"] = ["U+368a"]
UNICODE_TO_BLISS["U+368a"].append("plan,design")
BLISS_TO_UNICODE["darts"] = ["U+3b1f"]
UNICODE_TO_BLISS["U+3b1f"] = ["darts"]
BLISS_TO_UNICODE["capture"] = ["U+3b20"]
UNICODE_TO_BLISS["U+3b20"] = ["capture"]
BLISS_TO_UNICODE["catch"] = ["U+3b20"]
UNICODE_TO_BLISS["U+3b20"].append("catch")
BLISS_TO_UNICODE["seize"] = ["U+3b20"]
UNICODE_TO_BLISS["U+3b20"].append("seize")
BLISS_TO_UNICODE["capture,catch,seize"] = ["U+3b20"]
UNICODE_TO_BLISS["U+3b20"].append("capture,catch,seize")
BLISS_TO_UNICODE["to get"] = ["U+3b21"]
UNICODE_TO_BLISS["U+3b21"] = ["to get"]
BLISS_TO_UNICODE["protect"] = ["U+3b22"]
UNICODE_TO_BLISS["U+3b22"] = ["protect"]
BLISS_TO_UNICODE["cover"] = ["U+3b22"]
UNICODE_TO_BLISS["U+3b22"].append("cover")
BLISS_TO_UNICODE["shelter"].append("U+3b22")
UNICODE_TO_BLISS["U+3b22"].append("shelter")
BLISS_TO_UNICODE["take care of"] = ["U+3b22"]
UNICODE_TO_BLISS["U+3b22"].append("take care of")
BLISS_TO_UNICODE["protect,cover,shelter,take care of"] = ["U+3b22"]
UNICODE_TO_BLISS["U+3b22"].append("protect,cover,shelter,take care of")
BLISS_TO_UNICODE["cover"].append("U+3664")
UNICODE_TO_BLISS["U+3664"].append("cover")
BLISS_TO_UNICODE["roof,cover"] = ["U+3664"]
UNICODE_TO_BLISS["U+3664"].append("roof,cover")
BLISS_TO_UNICODE["Saehrimnir"] = ["U+3b23"]
UNICODE_TO_BLISS["U+3b23"] = ["Saehrimnir"]
BLISS_TO_UNICODE["pig/boar"] = ["U+3b24"]
UNICODE_TO_BLISS["U+3b24"] = ["pig/boar"]
BLISS_TO_UNICODE["ugh"] = ["U+3b25"]
UNICODE_TO_BLISS["U+3b25"] = ["ugh"]
BLISS_TO_UNICODE["yuk"] = ["U+3b25"]
UNICODE_TO_BLISS["U+3b25"].append("yuk")
BLISS_TO_UNICODE["ugh,yuk"] = ["U+3b25"]
UNICODE_TO_BLISS["U+3b25"].append("ugh,yuk")
BLISS_TO_UNICODE["golf"] = ["U+3b26"]
UNICODE_TO_BLISS["U+3b26"] = ["golf"]
BLISS_TO_UNICODE["gold"] = ["U+3b27"]
UNICODE_TO_BLISS["U+3b27"] = ["gold"]
BLISS_TO_UNICODE["mixer"] = ["U+3b28"]
UNICODE_TO_BLISS["U+3b28"] = ["mixer"]
BLISS_TO_UNICODE["blender"] = ["U+3b28"]
UNICODE_TO_BLISS["U+3b28"].append("blender")
BLISS_TO_UNICODE["mixer,blender"] = ["U+3b28"]
UNICODE_TO_BLISS["U+3b28"].append("mixer,blender")
BLISS_TO_UNICODE["mixture"] = ["U+3b29"]
UNICODE_TO_BLISS["U+3b29"] = ["mixture"]
BLISS_TO_UNICODE["impact"] = ["U+3b2a"]
UNICODE_TO_BLISS["U+3b2a"] = ["impact"]
BLISS_TO_UNICODE["heap of sand"] = ["U+3b2b"]
UNICODE_TO_BLISS["U+3b2b"] = ["heap of sand"]
BLISS_TO_UNICODE["indicator"] = ["U+3b2c"]
UNICODE_TO_BLISS["U+3b2c"] = ["indicator"]
BLISS_TO_UNICODE[" turned on its side and pointing forward"] = ["U+3b2e"]
UNICODE_TO_BLISS["U+3b2e"] = [" turned on its side and pointing forward"]
BLISS_TO_UNICODE[" turned on its side and pointing backward"] = ["U+3b34"]
UNICODE_TO_BLISS["U+3b34"] = [" turned on its side and pointing backward"]
BLISS_TO_UNICODE["circle"] = ["U+3b3a"]
UNICODE_TO_BLISS["U+3b3a"] = ["circle"]
BLISS_TO_UNICODE["indicator present action"] = ["U+3b3c"]
UNICODE_TO_BLISS["U+3b3c"] = ["indicator present action"]
BLISS_TO_UNICODE["Moslem"] = ["U+38bd"]
UNICODE_TO_BLISS["U+38bd"].append("Moslem")
BLISS_TO_UNICODE["Islamic"] = ["U+38bd"]
UNICODE_TO_BLISS["U+38bd"].append("Islamic")
BLISS_TO_UNICODE["Muslim,Moslem,Islamic"] = ["U+38bd"]
UNICODE_TO_BLISS["U+38bd"].append("Muslim,Moslem,Islamic")
BLISS_TO_UNICODE["crescent moon"] = ["U+3b3d"]
UNICODE_TO_BLISS["U+3b3d"] = ["crescent moon"]
BLISS_TO_UNICODE["Muslim,Moslem"] = ["U+38bd"]
UNICODE_TO_BLISS["U+38bd"].append("Muslim,Moslem")
BLISS_TO_UNICODE["cassette"] = ["U+3b3e"]
UNICODE_TO_BLISS["U+3b3e"] = ["cassette"]
BLISS_TO_UNICODE["audiocassette"] = ["U+3b3e"]
UNICODE_TO_BLISS["U+3b3e"].append("audiocassette")
BLISS_TO_UNICODE["videocassette"] = ["U+3b3e"]
UNICODE_TO_BLISS["U+3b3e"].append("videocassette")
BLISS_TO_UNICODE["cassette,audiocassette,videocassette"] = ["U+3b3e"]
UNICODE_TO_BLISS["U+3b3e"].append("cassette,audiocassette,videocassette")
BLISS_TO_UNICODE["condom"] = ["U+3b3f"]
UNICODE_TO_BLISS["U+3b3f"] = ["condom"]
BLISS_TO_UNICODE["molasses"] = ["U+3b40"]
UNICODE_TO_BLISS["U+3b40"] = ["molasses"]
BLISS_TO_UNICODE["dark syrup"] = ["U+3b40"]
UNICODE_TO_BLISS["U+3b40"].append("dark syrup")
BLISS_TO_UNICODE["black treacle"] = ["U+3b40"]
UNICODE_TO_BLISS["U+3b40"].append("black treacle")
BLISS_TO_UNICODE["molasses,dark syrup,black treacle"] = ["U+3b40"]
UNICODE_TO_BLISS["U+3b40"].append("molasses,dark syrup,black treacle")
BLISS_TO_UNICODE["syrup"] = ["U+3b41"]
UNICODE_TO_BLISS["U+3b41"] = ["syrup"]
BLISS_TO_UNICODE["free of charge"] = ["U+3b42"]
UNICODE_TO_BLISS["U+3b42"] = ["free of charge"]
BLISS_TO_UNICODE["gratis"] = ["U+3b42"]
UNICODE_TO_BLISS["U+3b42"].append("gratis")
BLISS_TO_UNICODE["for free"] = ["U+3b42"]
UNICODE_TO_BLISS["U+3b42"].append("for free")
BLISS_TO_UNICODE["free of charge,gratis,for free"] = ["U+3b42"]
UNICODE_TO_BLISS["U+3b42"].append("free of charge,gratis,for free")
BLISS_TO_UNICODE["cost"] = ["U+3b43"]
UNICODE_TO_BLISS["U+3b43"] = ["cost"]
BLISS_TO_UNICODE["distance"] = ["U+3b44"]
UNICODE_TO_BLISS["U+3b44"] = ["distance"]
BLISS_TO_UNICODE["dependent"] = ["U+3b45"]
UNICODE_TO_BLISS["U+3b45"] = ["dependent"]
BLISS_TO_UNICODE["sunny"] = ["U+3b46"]
UNICODE_TO_BLISS["U+3b46"] = ["sunny"]
BLISS_TO_UNICODE["resent"] = ["U+3b47"]
UNICODE_TO_BLISS["U+3b47"] = ["resent"]
BLISS_TO_UNICODE["compass"] = ["U+3b48"]
UNICODE_TO_BLISS["U+3b48"] = ["compass"]
BLISS_TO_UNICODE["cry"] = ["U+3b49"]
UNICODE_TO_BLISS["U+3b49"] = ["cry"]
BLISS_TO_UNICODE["weep"] = ["U+3b49"]
UNICODE_TO_BLISS["U+3b49"].append("weep")
BLISS_TO_UNICODE["cry,weep"] = ["U+3b49"]
UNICODE_TO_BLISS["U+3b49"].append("cry,weep")
BLISS_TO_UNICODE["proclaim"] = ["U+3b4a"]
UNICODE_TO_BLISS["U+3b4a"] = ["proclaim"]
BLISS_TO_UNICODE["announce"] = ["U+3b4a"]
UNICODE_TO_BLISS["U+3b4a"].append("announce")
BLISS_TO_UNICODE["proclaim,announce"] = ["U+3b4a"]
UNICODE_TO_BLISS["U+3b4a"].append("proclaim,announce")
BLISS_TO_UNICODE["proclamation"] = ["U+3b4b"]
UNICODE_TO_BLISS["U+3b4b"] = ["proclamation"]
BLISS_TO_UNICODE["greetings"] = ["U+378c"]
UNICODE_TO_BLISS["U+378c"].append("greetings")
BLISS_TO_UNICODE["hello,greetings"] = ["U+378c"]
UNICODE_TO_BLISS["U+378c"].append("hello,greetings")
BLISS_TO_UNICODE["evening before holiday"] = ["U+3b4c"]
UNICODE_TO_BLISS["U+3b4c"] = ["evening before holiday"]
BLISS_TO_UNICODE["evening of Sabbath"] = ["U+3b4c"]
UNICODE_TO_BLISS["U+3b4c"].append("evening of Sabbath")
BLISS_TO_UNICODE["evening before holiday,evening of Sabbath"] = ["U+3b4c"]
UNICODE_TO_BLISS["U+3b4c"].append("evening before holiday,evening of Sabbath")
BLISS_TO_UNICODE["much of"] = ["U+36d5"]
UNICODE_TO_BLISS["U+36d5"].append("much of")
BLISS_TO_UNICODE["many of"] = ["U+36d5"]
UNICODE_TO_BLISS["U+36d5"].append("many of")
BLISS_TO_UNICODE["quantity of"] = ["U+36d5"]
UNICODE_TO_BLISS["U+36d5"].append("quantity of")
BLISS_TO_UNICODE["group of,much of,many of,quantity of"] = ["U+36d5"]
UNICODE_TO_BLISS["U+36d5"].append("group of,much of,many of,quantity of")
BLISS_TO_UNICODE["sex"] = ["U+3465"]
UNICODE_TO_BLISS["U+3465"].append("sex")
BLISS_TO_UNICODE["gender,sex"] = ["U+3465"]
UNICODE_TO_BLISS["U+3465"].append("gender,sex")
BLISS_TO_UNICODE["encounter"].append("U+3237")
UNICODE_TO_BLISS["U+3237"].append("encounter")
BLISS_TO_UNICODE["see"].append("U+3237")
UNICODE_TO_BLISS["U+3237"].append("see")
BLISS_TO_UNICODE["meet,encounter,see"] = ["U+3237"]
UNICODE_TO_BLISS["U+3237"].append("meet,encounter,see")
BLISS_TO_UNICODE["see"].append("U+323e")
UNICODE_TO_BLISS["U+323e"].append("see")
BLISS_TO_UNICODE["understand,see"] = ["U+323e"]
UNICODE_TO_BLISS["U+323e"].append("understand,see")
BLISS_TO_UNICODE["ocean"] = ["U+3b4d"]
UNICODE_TO_BLISS["U+3b4d"] = ["ocean"]
BLISS_TO_UNICODE["sea"].append("U+3b4d")
UNICODE_TO_BLISS["U+3b4d"].append("sea")
BLISS_TO_UNICODE["ocean,sea"] = ["U+3b4d"]
UNICODE_TO_BLISS["U+3b4d"].append("ocean,sea")
BLISS_TO_UNICODE["movie"] = ["U+3b4e"]
UNICODE_TO_BLISS["U+3b4e"] = ["movie"]
BLISS_TO_UNICODE["film"] = ["U+3b4e"]
UNICODE_TO_BLISS["U+3b4e"].append("film")
BLISS_TO_UNICODE["movie,film"] = ["U+3b4e"]
UNICODE_TO_BLISS["U+3b4e"].append("movie,film")
BLISS_TO_UNICODE["cylinder"] = ["U+3b4f"]
UNICODE_TO_BLISS["U+3b4f"] = ["cylinder"]
BLISS_TO_UNICODE["nuclear energy"] = ["U+3b50"]
UNICODE_TO_BLISS["U+3b50"] = ["nuclear energy"]
BLISS_TO_UNICODE["kneel"] = ["U+3b51"]
UNICODE_TO_BLISS["U+3b51"] = ["kneel"]
BLISS_TO_UNICODE["adversity"] = ["U+3b52"]
UNICODE_TO_BLISS["U+3b52"] = ["adversity"]
BLISS_TO_UNICODE["hardship"] = ["U+3b52"]
UNICODE_TO_BLISS["U+3b52"].append("hardship")
BLISS_TO_UNICODE["setback"] = ["U+3b52"]
UNICODE_TO_BLISS["U+3b52"].append("setback")
BLISS_TO_UNICODE["adversity,hardship,setback"] = ["U+3b52"]
UNICODE_TO_BLISS["U+3b52"].append("adversity,hardship,setback")
BLISS_TO_UNICODE["half"] = ["U+3b53"]
UNICODE_TO_BLISS["U+3b53"] = ["half"]
BLISS_TO_UNICODE["one half"] = ["U+3b53"]
UNICODE_TO_BLISS["U+3b53"].append("one half")
BLISS_TO_UNICODE["half,one-half"] = ["U+3b53"]
UNICODE_TO_BLISS["U+3b53"].append("half,one-half")
BLISS_TO_UNICODE["fish bone"] = ["U+3b54"]
UNICODE_TO_BLISS["U+3b54"] = ["fish bone"]
BLISS_TO_UNICODE["last"] = ["U+3b55"]
UNICODE_TO_BLISS["U+3b55"] = ["last"]
BLISS_TO_UNICODE["final"] = ["U+3b55"]
UNICODE_TO_BLISS["U+3b55"].append("final")
BLISS_TO_UNICODE["last,final"] = ["U+3b55"]
UNICODE_TO_BLISS["U+3b55"].append("last,final")
BLISS_TO_UNICODE["etc)"] = ["U+3b55"]
UNICODE_TO_BLISS["U+3b55"].append("etc)")
BLISS_TO_UNICODE["magnetic pole"] = ["U+3b56"]
UNICODE_TO_BLISS["U+3b56"] = ["magnetic pole"]
BLISS_TO_UNICODE["South Pole"] = ["U+3b57"]
UNICODE_TO_BLISS["U+3b57"] = ["South Pole"]
BLISS_TO_UNICODE["connection"] = ["U+32a9"]
UNICODE_TO_BLISS["U+32a9"].append("connection")
BLISS_TO_UNICODE["combination,connection"] = ["U+32a9"]
UNICODE_TO_BLISS["U+32a9"].append("combination,connection")
BLISS_TO_UNICODE["entrance"] = ["U+3b58"]
UNICODE_TO_BLISS["U+3b58"] = ["entrance"]
BLISS_TO_UNICODE["let"] = ["U+3b5a"]
UNICODE_TO_BLISS["U+3b5a"] = ["let"]
BLISS_TO_UNICODE["allow"].append("U+3b5a")
UNICODE_TO_BLISS["U+3b5a"].append("allow")
BLISS_TO_UNICODE["permit"] = ["U+3b5a"]
UNICODE_TO_BLISS["U+3b5a"].append("permit")
BLISS_TO_UNICODE["let,allow,permit"] = ["U+3b5a"]
UNICODE_TO_BLISS["U+3b5a"].append("let,allow,permit")
BLISS_TO_UNICODE["let"].append("U+359a")
UNICODE_TO_BLISS["U+359a"].append("let")
BLISS_TO_UNICODE["rent,lease,let"] = ["U+359a"]
UNICODE_TO_BLISS["U+359a"].append("rent,lease,let")
BLISS_TO_UNICODE["similar sound"] = ["U+3b5b"]
UNICODE_TO_BLISS["U+3b5b"] = ["similar sound"]
BLISS_TO_UNICODE["sounds like"] = ["U+3b5b"]
UNICODE_TO_BLISS["U+3b5b"].append("sounds like")
BLISS_TO_UNICODE["similar sound,sounds like"] = ["U+3b5b"]
UNICODE_TO_BLISS["U+3b5b"].append("similar sound,sounds like")
BLISS_TO_UNICODE["similar"] = ["U+3b5c"]
UNICODE_TO_BLISS["U+3b5c"] = ["similar"]
BLISS_TO_UNICODE["approve"] = ["U+3b5d"]
UNICODE_TO_BLISS["U+3b5d"] = ["approve"]
BLISS_TO_UNICODE["load"] = ["U+3b5e"]
UNICODE_TO_BLISS["U+3b5e"] = ["load"]
BLISS_TO_UNICODE["much/many"] = ["U+3b5f"]
UNICODE_TO_BLISS["U+3b5f"] = ["much/many"]
BLISS_TO_UNICODE["loaf of bread"] = ["U+3358"]
UNICODE_TO_BLISS["U+3358"].append("loaf of bread")
BLISS_TO_UNICODE["loaf"] = ["U+3358"]
UNICODE_TO_BLISS["U+3358"].append("loaf")
BLISS_TO_UNICODE["bread,loaf of bread,loaf"] = ["U+3358"]
UNICODE_TO_BLISS["U+3358"].append("bread,loaf of bread,loaf")
BLISS_TO_UNICODE["bell"] = ["U+3b60"]
UNICODE_TO_BLISS["U+3b60"] = ["bell"]
BLISS_TO_UNICODE["chime bar"] = ["U+3b60"]
UNICODE_TO_BLISS["U+3b60"].append("chime bar")
BLISS_TO_UNICODE["bell,chime bar"] = ["U+3b60"]
UNICODE_TO_BLISS["U+3b60"].append("bell,chime bar")
BLISS_TO_UNICODE["lend"] = ["U+3b61"]
UNICODE_TO_BLISS["U+3b61"] = ["lend"]
BLISS_TO_UNICODE["loan"] = ["U+3b61"]
UNICODE_TO_BLISS["U+3b61"].append("loan")
BLISS_TO_UNICODE["lend,loan"] = ["U+3b61"]
UNICODE_TO_BLISS["U+3b61"].append("lend,loan")
BLISS_TO_UNICODE["mosque"].append("U+379b")
UNICODE_TO_BLISS["U+379b"].append("mosque")
BLISS_TO_UNICODE["temple"].append("U+379b")
UNICODE_TO_BLISS["U+379b"].append("temple")
BLISS_TO_UNICODE["church,mosque,temple"] = ["U+379b"]
UNICODE_TO_BLISS["U+379b"].append("church,mosque,temple")
BLISS_TO_UNICODE["indefinite"] = ["U+3b62"]
UNICODE_TO_BLISS["U+3b62"] = ["indefinite"]
BLISS_TO_UNICODE["belt"] = ["U+3b63"]
UNICODE_TO_BLISS["U+3b63"] = ["belt"]
BLISS_TO_UNICODE["sash"] = ["U+3b63"]
UNICODE_TO_BLISS["U+3b63"].append("sash")
BLISS_TO_UNICODE["belt,sash"] = ["U+3b63"]
UNICODE_TO_BLISS["U+3b63"].append("belt,sash")
BLISS_TO_UNICODE["devil"] = ["U+3b64"]
UNICODE_TO_BLISS["U+3b64"] = ["devil"]
BLISS_TO_UNICODE["horns"] = ["U+3b65"]
UNICODE_TO_BLISS["U+3b65"] = ["horns"]
BLISS_TO_UNICODE["electro magnet"] = ["U+3b66"]
UNICODE_TO_BLISS["U+3b66"] = ["electro magnet"]
BLISS_TO_UNICODE["hard"] = ["U+3b67"]
UNICODE_TO_BLISS["U+3b67"] = ["hard"]
BLISS_TO_UNICODE["firm"] = ["U+3b67"]
UNICODE_TO_BLISS["U+3b67"].append("firm")
BLISS_TO_UNICODE["hard,firm"] = ["U+3b67"]
UNICODE_TO_BLISS["U+3b67"].append("hard,firm")
BLISS_TO_UNICODE["sweetheart"] = ["U+3b68"]
UNICODE_TO_BLISS["U+3b68"] = ["sweetheart"]
BLISS_TO_UNICODE["lover"] = ["U+3b68"]
UNICODE_TO_BLISS["U+3b68"].append("lover")
BLISS_TO_UNICODE["sweetheart,lover"] = ["U+3b68"]
UNICODE_TO_BLISS["U+3b68"].append("sweetheart,lover")
BLISS_TO_UNICODE["to love"] = ["U+3b69"]
UNICODE_TO_BLISS["U+3b69"] = ["to love"]
BLISS_TO_UNICODE["coup d'etat"] = ["U+3692"]
UNICODE_TO_BLISS["U+3692"].append("coup d'etat")
BLISS_TO_UNICODE["coup,coup d'etat"] = ["U+3692"]
UNICODE_TO_BLISS["U+3692"].append("coup,coup d'etat")
BLISS_TO_UNICODE["board and lodging"] = ["U+3b6a"]
UNICODE_TO_BLISS["U+3b6a"] = ["board and lodging"]
BLISS_TO_UNICODE["room and board"] = ["U+3b6a"]
UNICODE_TO_BLISS["U+3b6a"].append("room and board")
BLISS_TO_UNICODE["board and lodging,room and board"] = ["U+3b6a"]
UNICODE_TO_BLISS["U+3b6a"].append("board and lodging,room and board")
BLISS_TO_UNICODE["symbol looks like a flame"] = ["U+3b6b"]
UNICODE_TO_BLISS["U+3b6b"] = ["symbol looks like a flame"]
BLISS_TO_UNICODE[" suggesting fire"] = ["U+3b6c"]
UNICODE_TO_BLISS["U+3b6c"] = [" suggesting fire"]
BLISS_TO_UNICODE["infect"] = ["U+3b6d"]
UNICODE_TO_BLISS["U+3b6d"] = ["infect"]
BLISS_TO_UNICODE["infection"] = ["U+3b6e"]
UNICODE_TO_BLISS["U+3b6e"] = ["infection"]
BLISS_TO_UNICODE["wakefulness"] = ["U+3b70"]
UNICODE_TO_BLISS["U+3b70"] = ["wakefulness"]
BLISS_TO_UNICODE["alertness"] = ["U+3b71"]
UNICODE_TO_BLISS["U+3b71"] = ["alertness"]
BLISS_TO_UNICODE["cellular fluid"] = ["U+3b72"]
UNICODE_TO_BLISS["U+3b72"] = ["cellular fluid"]
BLISS_TO_UNICODE["cell"] = ["U+3b73"]
UNICODE_TO_BLISS["U+3b73"] = ["cell"]
BLISS_TO_UNICODE["shooting sports"] = ["U+3b74"]
UNICODE_TO_BLISS["U+3b74"] = ["shooting sports"]
BLISS_TO_UNICODE["protective mask"] = ["U+3b75"]
UNICODE_TO_BLISS["U+3b75"] = ["protective mask"]
BLISS_TO_UNICODE["uncertain"] = ["U+3b76"]
UNICODE_TO_BLISS["U+3b76"] = ["uncertain"]
BLISS_TO_UNICODE["unsure"] = ["U+3b76"]
UNICODE_TO_BLISS["U+3b76"].append("unsure")
BLISS_TO_UNICODE["uncertain,unsure"] = ["U+3b76"]
UNICODE_TO_BLISS["U+3b76"].append("uncertain,unsure")
BLISS_TO_UNICODE["linear"] = ["U+3b77"]
UNICODE_TO_BLISS["U+3b77"] = ["linear"]
BLISS_TO_UNICODE["straight"] = ["U+3b77"]
UNICODE_TO_BLISS["U+3b77"].append("straight")
BLISS_TO_UNICODE["linear,straight"] = ["U+3b77"]
UNICODE_TO_BLISS["U+3b77"].append("linear,straight")
BLISS_TO_UNICODE["budget"] = ["U+3b78"]
UNICODE_TO_BLISS["U+3b78"] = ["budget"]
BLISS_TO_UNICODE["business plan"] = ["U+3b78"]
UNICODE_TO_BLISS["U+3b78"].append("business plan")
BLISS_TO_UNICODE["budget,business plan"] = ["U+3b78"]
UNICODE_TO_BLISS["U+3b78"].append("budget,business plan")
BLISS_TO_UNICODE["medically"] = ["U+3806"]
UNICODE_TO_BLISS["U+3806"].append("medically")
BLISS_TO_UNICODE["medical,medically"] = ["U+3806"]
UNICODE_TO_BLISS["U+3806"].append("medical,medically")
BLISS_TO_UNICODE["wave power"] = ["U+3b79"]
UNICODE_TO_BLISS["U+3b79"] = ["wave power"]
BLISS_TO_UNICODE["wave energy"] = ["U+3b79"]
UNICODE_TO_BLISS["U+3b79"].append("wave energy")
BLISS_TO_UNICODE["wave power,wave energy"] = ["U+3b79"]
UNICODE_TO_BLISS["U+3b79"].append("wave power,wave energy")
BLISS_TO_UNICODE["wave"] = ["U+3b7a"]
UNICODE_TO_BLISS["U+3b7a"] = ["wave"]
BLISS_TO_UNICODE["mistake"] = ["U+3b7b"]
UNICODE_TO_BLISS["U+3b7b"] = ["mistake"]
BLISS_TO_UNICODE["error"] = ["U+3b7b"]
UNICODE_TO_BLISS["U+3b7b"].append("error")
BLISS_TO_UNICODE["fault"] = ["U+3b7b"]
UNICODE_TO_BLISS["U+3b7b"].append("fault")
BLISS_TO_UNICODE["mistake,error,fault"] = ["U+3b7b"]
UNICODE_TO_BLISS["U+3b7b"].append("mistake,error,fault")
BLISS_TO_UNICODE["mishap"] = ["U+3b7b"]
UNICODE_TO_BLISS["U+3b7b"].append("mishap")
BLISS_TO_UNICODE["error,mishap"] = ["U+3b7b"]
UNICODE_TO_BLISS["U+3b7b"].append("error,mishap")
BLISS_TO_UNICODE["sea urchin"] = ["U+3b7c"]
UNICODE_TO_BLISS["U+3b7c"] = ["sea urchin"]
BLISS_TO_UNICODE["quills"] = ["U+3b7d"]
UNICODE_TO_BLISS["U+3b7d"] = ["quills"]
BLISS_TO_UNICODE["mountain sports"] = ["U+3b7e"]
UNICODE_TO_BLISS["U+3b7e"] = ["mountain sports"]
BLISS_TO_UNICODE["swim"] = ["U+3b7f"]
UNICODE_TO_BLISS["U+3b7f"] = ["swim"]
BLISS_TO_UNICODE["swim"].append("U+3962")
UNICODE_TO_BLISS["U+3962"].append("swim")
BLISS_TO_UNICODE["swimming,swim"] = ["U+3962"]
UNICODE_TO_BLISS["U+3962"].append("swimming,swim")
BLISS_TO_UNICODE["upset"] = ["U+3b80"]
UNICODE_TO_BLISS["U+3b80"] = ["upset"]
BLISS_TO_UNICODE["disturbance"].append("U+3b80")
UNICODE_TO_BLISS["U+3b80"].append("disturbance")
BLISS_TO_UNICODE["agitation"] = ["U+3b80"]
UNICODE_TO_BLISS["U+3b80"].append("agitation")
BLISS_TO_UNICODE["upset,disturbance,agitation"] = ["U+3b80"]
UNICODE_TO_BLISS["U+3b80"].append("upset,disturbance,agitation")
BLISS_TO_UNICODE["calculator"] = ["U+3b81"]
UNICODE_TO_BLISS["U+3b81"] = ["calculator"]
BLISS_TO_UNICODE["to calculate"] = ["U+3b82"]
UNICODE_TO_BLISS["U+3b82"] = ["to calculate"]
BLISS_TO_UNICODE["chase"] = ["U+3b83"]
UNICODE_TO_BLISS["U+3b83"] = ["chase"]
BLISS_TO_UNICODE["funny"] = ["U+3b84"]
UNICODE_TO_BLISS["U+3b84"] = ["funny"]
BLISS_TO_UNICODE["humorous"] = ["U+3b84"]
UNICODE_TO_BLISS["U+3b84"].append("humorous")
BLISS_TO_UNICODE["funny,humorous"] = ["U+3b84"]
UNICODE_TO_BLISS["U+3b84"].append("funny,humorous")
BLISS_TO_UNICODE["laugh"] = ["U+3b85"]
UNICODE_TO_BLISS["U+3b85"] = ["laugh"]
BLISS_TO_UNICODE["laughter"] = ["U+3b86"]
UNICODE_TO_BLISS["U+3b86"] = ["laughter"]
BLISS_TO_UNICODE["guest room"] = ["U+3b87"]
UNICODE_TO_BLISS["U+3b87"] = ["guest room"]
BLISS_TO_UNICODE["forgiveness"] = ["U+3b88"]
UNICODE_TO_BLISS["U+3b88"] = ["forgiveness"]
BLISS_TO_UNICODE["pardon"] = ["U+3b88"]
UNICODE_TO_BLISS["U+3b88"].append("pardon")
BLISS_TO_UNICODE["forgiveness,pardon"] = ["U+3b88"]
UNICODE_TO_BLISS["U+3b88"].append("forgiveness,pardon")
BLISS_TO_UNICODE["watchful"] = ["U+3b89"]
UNICODE_TO_BLISS["U+3b89"] = ["watchful"]
BLISS_TO_UNICODE["alert"] = ["U+3b89"]
UNICODE_TO_BLISS["U+3b89"].append("alert")
BLISS_TO_UNICODE["watchful,alert"] = ["U+3b89"]
UNICODE_TO_BLISS["U+3b89"].append("watchful,alert")
BLISS_TO_UNICODE["cucumber"] = ["U+3b8a"]
UNICODE_TO_BLISS["U+3b8a"] = ["cucumber"]
BLISS_TO_UNICODE["tobacco"] = ["U+3b8b"]
UNICODE_TO_BLISS["U+3b8b"] = ["tobacco"]
BLISS_TO_UNICODE["to smoke"] = ["U+3b8c"]
UNICODE_TO_BLISS["U+3b8c"] = ["to smoke"]
BLISS_TO_UNICODE["recent"] = ["U+3b8d"]
UNICODE_TO_BLISS["U+3b8d"] = ["recent"]
BLISS_TO_UNICODE["recently"] = ["U+3b8d"]
UNICODE_TO_BLISS["U+3b8d"].append("recently")
BLISS_TO_UNICODE["recent,recently"] = ["U+3b8d"]
UNICODE_TO_BLISS["U+3b8d"].append("recent,recently")
BLISS_TO_UNICODE["swimming hall"] = ["U+3b8e"]
UNICODE_TO_BLISS["U+3b8e"] = ["swimming hall"]
BLISS_TO_UNICODE["indoor swimming pool"] = ["U+3b8e"]
UNICODE_TO_BLISS["U+3b8e"].append("indoor swimming pool")
BLISS_TO_UNICODE["swimming hall,indoor swimming pool"] = ["U+3b8e"]
UNICODE_TO_BLISS["U+3b8e"].append("swimming hall,indoor swimming pool")
BLISS_TO_UNICODE["greenhouse"] = ["U+3b8f"]
UNICODE_TO_BLISS["U+3b8f"] = ["greenhouse"]
BLISS_TO_UNICODE["glasshouse"] = ["U+3b8f"]
UNICODE_TO_BLISS["U+3b8f"].append("glasshouse")
BLISS_TO_UNICODE["hothouse"] = ["U+3b8f"]
UNICODE_TO_BLISS["U+3b8f"].append("hothouse")
BLISS_TO_UNICODE["greenhouse,glasshouse,hothouse"] = ["U+3b8f"]
UNICODE_TO_BLISS["U+3b8f"].append("greenhouse,glasshouse,hothouse")
BLISS_TO_UNICODE["human being"] = ["U+3428"]
UNICODE_TO_BLISS["U+3428"].append("human being")
BLISS_TO_UNICODE["individual"] = ["U+3428"]
UNICODE_TO_BLISS["U+3428"].append("individual")
BLISS_TO_UNICODE["human"] = ["U+3428"]
UNICODE_TO_BLISS["U+3428"].append("human")
BLISS_TO_UNICODE["person,human being,individual,human"] = ["U+3428"]
UNICODE_TO_BLISS["U+3428"].append("person,human being,individual,human")
BLISS_TO_UNICODE["symbol suggests a human being standing"] = ["U+3b90"]
UNICODE_TO_BLISS["U+3b90"] = ["symbol suggests a human being standing"]
BLISS_TO_UNICODE[" with feet turned out"] = ["U+3b91"]
UNICODE_TO_BLISS["U+3b91"] = [" with feet turned out"]
BLISS_TO_UNICODE["defecation"] = ["U+3657"]
UNICODE_TO_BLISS["U+3657"].append("defecation")
BLISS_TO_UNICODE["shitting"] = ["U+3657"]
UNICODE_TO_BLISS["U+3657"].append("shitting")
BLISS_TO_UNICODE["feces"] = ["U+3657"]
UNICODE_TO_BLISS["U+3657"].append("feces")
BLISS_TO_UNICODE["shit"].append("U+3657")
UNICODE_TO_BLISS["U+3657"].append("shit")
BLISS_TO_UNICODE["poop"] = ["U+3657"]
UNICODE_TO_BLISS["U+3657"].append("poop")
BLISS_TO_UNICODE["bowel movement,defecation,shitting,feces,shit,poop"] = ["U+3657"]
UNICODE_TO_BLISS["U+3657"].append("bowel movement,defecation,shitting,feces,shit,poop")
BLISS_TO_UNICODE["crayfish"] = ["U+3b92"]
UNICODE_TO_BLISS["U+3b92"] = ["crayfish"]
BLISS_TO_UNICODE["poached egg"] = ["U+3271"]
UNICODE_TO_BLISS["U+3271"].append("poached egg")
BLISS_TO_UNICODE["to heat"] = ["U+3b93"]
UNICODE_TO_BLISS["U+3b93"] = ["to heat"]
BLISS_TO_UNICODE["horse cloth"] = ["U+3b94"]
UNICODE_TO_BLISS["U+3b94"] = ["horse cloth"]
BLISS_TO_UNICODE["make sign of the cross"] = ["U+3b95"]
UNICODE_TO_BLISS["U+3b95"] = ["make sign of the cross"]
BLISS_TO_UNICODE["sign of the cross"] = ["U+3b96"]
UNICODE_TO_BLISS["U+3b96"] = ["sign of the cross"]
BLISS_TO_UNICODE["javelin throw"] = ["U+3b97"]
UNICODE_TO_BLISS["U+3b97"] = ["javelin throw"]
BLISS_TO_UNICODE["javelin"] = ["U+3b98"]
UNICODE_TO_BLISS["U+3b98"] = ["javelin"]
BLISS_TO_UNICODE["barge"] = ["U+3b99"]
UNICODE_TO_BLISS["U+3b99"] = ["barge"]
BLISS_TO_UNICODE["river boat"] = ["U+3b99"]
UNICODE_TO_BLISS["U+3b99"].append("river boat")
BLISS_TO_UNICODE["barge,river boat"] = ["U+3b99"]
UNICODE_TO_BLISS["U+3b99"].append("barge,river boat")
BLISS_TO_UNICODE["freighter"] = ["U+3b9a"]
UNICODE_TO_BLISS["U+3b9a"] = ["freighter"]
BLISS_TO_UNICODE["abstention"] = ["U+3b9b"]
UNICODE_TO_BLISS["U+3b9b"] = ["abstention"]
BLISS_TO_UNICODE["sandal"] = ["U+3b9c"]
UNICODE_TO_BLISS["U+3b9c"] = ["sandal"]
BLISS_TO_UNICODE["goblet"] = ["U+3b9d"]
UNICODE_TO_BLISS["U+3b9d"] = ["goblet"]
BLISS_TO_UNICODE["wineglass"] = ["U+3b9d"]
UNICODE_TO_BLISS["U+3b9d"].append("wineglass")
BLISS_TO_UNICODE["goblet,wineglass"] = ["U+3b9d"]
UNICODE_TO_BLISS["U+3b9d"].append("goblet,wineglass")
BLISS_TO_UNICODE["eager"] = ["U+3b9e"]
UNICODE_TO_BLISS["U+3b9e"] = ["eager"]
BLISS_TO_UNICODE["keen"] = ["U+3b9e"]
UNICODE_TO_BLISS["U+3b9e"].append("keen")
BLISS_TO_UNICODE["willing"] = ["U+3b9e"]
UNICODE_TO_BLISS["U+3b9e"].append("willing")
BLISS_TO_UNICODE["eager,keen,willing"] = ["U+3b9e"]
UNICODE_TO_BLISS["U+3b9e"].append("eager,keen,willing")
BLISS_TO_UNICODE["grapefruit"] = ["U+3b9f"]
UNICODE_TO_BLISS["U+3b9f"] = ["grapefruit"]
BLISS_TO_UNICODE["area"] = ["U+34a3"]
UNICODE_TO_BLISS["U+34a3"].append("area")
BLISS_TO_UNICODE["location"] = ["U+34a3"]
UNICODE_TO_BLISS["U+34a3"].append("location")
BLISS_TO_UNICODE["space"].append("U+34a3")
UNICODE_TO_BLISS["U+34a3"].append("space")
BLISS_TO_UNICODE["place,area,location,space"] = ["U+34a3"]
UNICODE_TO_BLISS["U+34a3"].append("place,area,location,space")
BLISS_TO_UNICODE["surprised"] = ["U+3ba0"]
UNICODE_TO_BLISS["U+3ba0"] = ["surprised"]
BLISS_TO_UNICODE["surprise"] = ["U+3ba1"]
UNICODE_TO_BLISS["U+3ba1"] = ["surprise"]
BLISS_TO_UNICODE["niece"] = ["U+3ba2"]
UNICODE_TO_BLISS["U+3ba2"] = ["niece"]
BLISS_TO_UNICODE["emergency"] = ["U+3ba3"]
UNICODE_TO_BLISS["U+3ba3"] = ["emergency"]
BLISS_TO_UNICODE["chest hair"] = ["U+3ba4"]
UNICODE_TO_BLISS["U+3ba4"] = ["chest hair"]
BLISS_TO_UNICODE["family"] = ["U+3ba5"]
UNICODE_TO_BLISS["U+3ba5"] = ["family"]
BLISS_TO_UNICODE["couple"].append("U+3ba5")
UNICODE_TO_BLISS["U+3ba5"].append("couple")
BLISS_TO_UNICODE["family,couple"] = ["U+3ba5"]
UNICODE_TO_BLISS["U+3ba5"].append("family,couple")
BLISS_TO_UNICODE["suffering"] = ["U+35f1"]
UNICODE_TO_BLISS["U+35f1"].append("suffering")
BLISS_TO_UNICODE["pain,suffering"] = ["U+35f1"]
UNICODE_TO_BLISS["U+35f1"].append("pain,suffering")
BLISS_TO_UNICODE["sick"] = ["U+3ba6"]
UNICODE_TO_BLISS["U+3ba6"] = ["sick"]
BLISS_TO_UNICODE["urine bottle"] = ["U+3ba7"]
UNICODE_TO_BLISS["U+3ba7"] = ["urine bottle"]
BLISS_TO_UNICODE["washcloth"] = ["U+3ba8"]
UNICODE_TO_BLISS["U+3ba8"] = ["washcloth"]
BLISS_TO_UNICODE["washrag"] = ["U+3ba8"]
UNICODE_TO_BLISS["U+3ba8"].append("washrag")
BLISS_TO_UNICODE["flannel"] = ["U+3ba8"]
UNICODE_TO_BLISS["U+3ba8"].append("flannel")
BLISS_TO_UNICODE["washcloth,washrag,flannel"] = ["U+3ba8"]
UNICODE_TO_BLISS["U+3ba8"].append("washcloth,washrag,flannel")
BLISS_TO_UNICODE["jackfruit"] = ["U+3ba9"]
UNICODE_TO_BLISS["U+3ba9"] = ["jackfruit"]
BLISS_TO_UNICODE["heavy"] = ["U+3baa"]
UNICODE_TO_BLISS["U+3baa"] = ["heavy"]
BLISS_TO_UNICODE["maple syrup"] = ["U+3bab"]
UNICODE_TO_BLISS["U+3bab"] = ["maple syrup"]
BLISS_TO_UNICODE["OK"] = ["U+3bac"]
UNICODE_TO_BLISS["U+3bac"] = ["OK"]
BLISS_TO_UNICODE["alright"] = ["U+3bac"]
UNICODE_TO_BLISS["U+3bac"].append("alright")
BLISS_TO_UNICODE["OK,alright"] = ["U+3bac"]
UNICODE_TO_BLISS["U+3bac"].append("OK,alright")
BLISS_TO_UNICODE["enough"] = ["U+3bad"]
UNICODE_TO_BLISS["U+3bad"] = ["enough"]
BLISS_TO_UNICODE["mouse"] = ["U+3bae"]
UNICODE_TO_BLISS["U+3bae"] = ["mouse"]
BLISS_TO_UNICODE["pointing device"].append("U+3bae")
UNICODE_TO_BLISS["U+3bae"].append("pointing device")
BLISS_TO_UNICODE["mouse,pointing device"] = ["U+3bae"]
UNICODE_TO_BLISS["U+3bae"].append("mouse,pointing device")
BLISS_TO_UNICODE["choir"] = ["U+3baf"]
UNICODE_TO_BLISS["U+3baf"] = ["choir"]
BLISS_TO_UNICODE["chorus"] = ["U+3baf"]
UNICODE_TO_BLISS["U+3baf"].append("chorus")
BLISS_TO_UNICODE["choir,chorus"] = ["U+3baf"]
UNICODE_TO_BLISS["U+3baf"].append("choir,chorus")
BLISS_TO_UNICODE["bathing rule"] = ["U+3bb0"]
UNICODE_TO_BLISS["U+3bb0"] = ["bathing rule"]
BLISS_TO_UNICODE["spring"] = ["U+3bb1"]
UNICODE_TO_BLISS["U+3bb1"] = ["spring"]
BLISS_TO_UNICODE["palm"] = ["U+3bb2"]
UNICODE_TO_BLISS["U+3bb2"] = ["palm"]
BLISS_TO_UNICODE["curious"] = ["U+3bb3"]
UNICODE_TO_BLISS["U+3bb3"] = ["curious"]
BLISS_TO_UNICODE["inquisitive"] = ["U+3bb3"]
UNICODE_TO_BLISS["U+3bb3"].append("inquisitive")
BLISS_TO_UNICODE["curious,inquisitive"] = ["U+3bb3"]
UNICODE_TO_BLISS["U+3bb3"].append("curious,inquisitive")
BLISS_TO_UNICODE["naming ceremony"] = ["U+3bb4"]
UNICODE_TO_BLISS["U+3bb4"] = ["naming ceremony"]
BLISS_TO_UNICODE["twinkle"] = ["U+3bb5"]
UNICODE_TO_BLISS["U+3bb5"] = ["twinkle"]
BLISS_TO_UNICODE["shine"].append("U+3bb5")
UNICODE_TO_BLISS["U+3bb5"].append("shine")
BLISS_TO_UNICODE["sparkle"] = ["U+3bb5"]
UNICODE_TO_BLISS["U+3bb5"].append("sparkle")
BLISS_TO_UNICODE["twinkle,shine,sparkle"] = ["U+3bb5"]
UNICODE_TO_BLISS["U+3bb5"].append("twinkle,shine,sparkle")
BLISS_TO_UNICODE["broadband"] = ["U+3bb6"]
UNICODE_TO_BLISS["U+3bb6"] = ["broadband"]
BLISS_TO_UNICODE["band"] = ["U+3bb7"]
UNICODE_TO_BLISS["U+3bb7"] = ["band"]
BLISS_TO_UNICODE["newness"] = ["U+3bb8"]
UNICODE_TO_BLISS["U+3bb8"] = ["newness"]
BLISS_TO_UNICODE["novelty"] = ["U+3bb8"]
UNICODE_TO_BLISS["U+3bb8"].append("novelty")
BLISS_TO_UNICODE["newness,novelty"] = ["U+3bb8"]
UNICODE_TO_BLISS["U+3bb8"].append("newness,novelty")
BLISS_TO_UNICODE["naturalism"] = ["U+368f"]
UNICODE_TO_BLISS["U+368f"].append("naturalism")
BLISS_TO_UNICODE["religion,naturalism"] = ["U+368f"]
UNICODE_TO_BLISS["U+368f"].append("religion,naturalism")
BLISS_TO_UNICODE["theology"] = ["U+368f"]
UNICODE_TO_BLISS["U+368f"].append("theology")
BLISS_TO_UNICODE["protest"] = ["U+3bb9"]
UNICODE_TO_BLISS["U+3bb9"] = ["protest"]
BLISS_TO_UNICODE["object"] = ["U+3bb9"]
UNICODE_TO_BLISS["U+3bb9"].append("object")
BLISS_TO_UNICODE["oppose"] = ["U+3bb9"]
UNICODE_TO_BLISS["U+3bb9"].append("oppose")
BLISS_TO_UNICODE["protest,object,oppose"] = ["U+3bb9"]
UNICODE_TO_BLISS["U+3bb9"].append("protest,object,oppose")
BLISS_TO_UNICODE["object"].append("U+3382")
UNICODE_TO_BLISS["U+3382"].append("object")
BLISS_TO_UNICODE["thing,object"] = ["U+3382"]
UNICODE_TO_BLISS["U+3382"].append("thing,object")
BLISS_TO_UNICODE["symbol suggests the two dimensional outline of a crystal"] = ["U+3bba"]
UNICODE_TO_BLISS["U+3bba"] = ["symbol suggests the two dimensional outline of a crystal"]
BLISS_TO_UNICODE["two parallel arrows"] = ["U+3bbb"]
UNICODE_TO_BLISS["U+3bbb"] = ["two parallel arrows"]
BLISS_TO_UNICODE["contract"] = ["U+323a"]
UNICODE_TO_BLISS["U+323a"].append("contract")
BLISS_TO_UNICODE["elementary school"] = ["U+3bbc"]
UNICODE_TO_BLISS["U+3bbc"] = ["elementary school"]
BLISS_TO_UNICODE["primary school"] = ["U+3bbc"]
UNICODE_TO_BLISS["U+3bbc"].append("primary school")
BLISS_TO_UNICODE["elementary school,primary school"] = ["U+3bbc"]
UNICODE_TO_BLISS["U+3bbc"].append("elementary school,primary school")
BLISS_TO_UNICODE["school"] = ["U+3bbd"]
UNICODE_TO_BLISS["U+3bbd"] = ["school"]
BLISS_TO_UNICODE["no place"] = ["U+34c2"]
UNICODE_TO_BLISS["U+34c2"].append("no place")
BLISS_TO_UNICODE["nowhere,no place"] = ["U+34c2"]
UNICODE_TO_BLISS["U+34c2"].append("nowhere,no place")
BLISS_TO_UNICODE["Christmas song"] = ["U+3bbe"]
UNICODE_TO_BLISS["U+3bbe"] = ["Christmas song"]
BLISS_TO_UNICODE["carol"] = ["U+3bbe"]
UNICODE_TO_BLISS["U+3bbe"].append("carol")
BLISS_TO_UNICODE["Christmas song,carol"] = ["U+3bbe"]
UNICODE_TO_BLISS["U+3bbe"].append("Christmas song,carol")
BLISS_TO_UNICODE["Christmas"] = ["U+3bbf"]
UNICODE_TO_BLISS["U+3bbf"] = ["Christmas"]
BLISS_TO_UNICODE["by"] = ["U+3bc0"]
UNICODE_TO_BLISS["U+3bc0"] = ["by"]
BLISS_TO_UNICODE["by means of"].append("U+3bc0")
UNICODE_TO_BLISS["U+3bc0"].append("by means of")
BLISS_TO_UNICODE["of"] = ["U+3bc0"]
UNICODE_TO_BLISS["U+3bc0"].append("of")
BLISS_TO_UNICODE["by,by means of,of"] = ["U+3bc0"]
UNICODE_TO_BLISS["U+3bc0"].append("by,by means of,of")
BLISS_TO_UNICODE["relation"] = ["U+3bc1"]
UNICODE_TO_BLISS["U+3bc1"] = ["relation"]
BLISS_TO_UNICODE[" pointing backwards"] = ["U+3bc2"]
UNICODE_TO_BLISS["U+3bc2"] = [" pointing backwards"]
BLISS_TO_UNICODE["anything"] = ["U+3bc3"]
UNICODE_TO_BLISS["U+3bc3"] = ["anything"]
BLISS_TO_UNICODE["something"] = ["U+3bc3"]
UNICODE_TO_BLISS["U+3bc3"].append("something")
BLISS_TO_UNICODE["anything,something"] = ["U+3bc3"]
UNICODE_TO_BLISS["U+3bc3"].append("anything,something")
BLISS_TO_UNICODE["movie theatre"] = ["U+3bc4"]
UNICODE_TO_BLISS["U+3bc4"] = ["movie theatre"]
BLISS_TO_UNICODE["cinema"] = ["U+3bc4"]
UNICODE_TO_BLISS["U+3bc4"].append("cinema")
BLISS_TO_UNICODE["movie theatre,cinema"] = ["U+3bc4"]
UNICODE_TO_BLISS["U+3bc4"].append("movie theatre,cinema")
BLISS_TO_UNICODE["hockey stick"].append("U+37ea")
UNICODE_TO_BLISS["U+37ea"].append("hockey stick")
BLISS_TO_UNICODE["sport stick and puck,hockey stick"] = ["U+37ea"]
UNICODE_TO_BLISS["U+37ea"].append("sport stick and puck,hockey stick")
BLISS_TO_UNICODE["garbage"] = ["U+3385"]
UNICODE_TO_BLISS["U+3385"].append("garbage")
BLISS_TO_UNICODE["rubbish"] = ["U+3385"]
UNICODE_TO_BLISS["U+3385"].append("rubbish")
BLISS_TO_UNICODE["trash"] = ["U+3385"]
UNICODE_TO_BLISS["U+3385"].append("trash")
BLISS_TO_UNICODE["waste,garbage,rubbish,trash"] = ["U+3385"]
UNICODE_TO_BLISS["U+3385"].append("waste,garbage,rubbish,trash")
BLISS_TO_UNICODE["Mjolnir"] = ["U+3bc5"]
UNICODE_TO_BLISS["U+3bc5"] = ["Mjolnir"]
BLISS_TO_UNICODE["chewing gum"] = ["U+3bc6"]
UNICODE_TO_BLISS["U+3bc6"] = ["chewing gum"]
BLISS_TO_UNICODE["chewing-gum"] = ["U+3bc6"]
UNICODE_TO_BLISS["U+3bc6"].append("chewing-gum")
BLISS_TO_UNICODE["candy"] = ["U+3bc7"]
UNICODE_TO_BLISS["U+3bc7"] = ["candy"]
BLISS_TO_UNICODE["tour"] = ["U+3bc8"]
UNICODE_TO_BLISS["U+3bc8"] = ["tour"]
BLISS_TO_UNICODE["sightseeing"] = ["U+3bc8"]
UNICODE_TO_BLISS["U+3bc8"].append("sightseeing")
BLISS_TO_UNICODE["tour,sightseeing"] = ["U+3bc8"]
UNICODE_TO_BLISS["U+3bc8"].append("tour,sightseeing")
BLISS_TO_UNICODE["habit"] = ["U+3bc9"]
UNICODE_TO_BLISS["U+3bc9"] = ["habit"]
BLISS_TO_UNICODE["custom"] = ["U+3bc9"]
UNICODE_TO_BLISS["U+3bc9"].append("custom")
BLISS_TO_UNICODE["habit,custom"] = ["U+3bc9"]
UNICODE_TO_BLISS["U+3bc9"].append("habit,custom")
BLISS_TO_UNICODE["usually"] = ["U+3bca"]
UNICODE_TO_BLISS["U+3bca"] = ["usually"]
BLISS_TO_UNICODE["tanker truck"] = ["U+3bcb"]
UNICODE_TO_BLISS["U+3bcb"] = ["tanker truck"]
BLISS_TO_UNICODE["tank lorry"] = ["U+3bcb"]
UNICODE_TO_BLISS["U+3bcb"].append("tank lorry")
BLISS_TO_UNICODE["tanker truck,tank lorry"] = ["U+3bcb"]
UNICODE_TO_BLISS["U+3bcb"].append("tanker truck,tank lorry")
BLISS_TO_UNICODE["suit"] = ["U+3bcc"]
UNICODE_TO_BLISS["U+3bcc"] = ["suit"]
BLISS_TO_UNICODE["minister"] = ["U+3bcd"]
UNICODE_TO_BLISS["U+3bcd"] = ["minister"]
BLISS_TO_UNICODE["pastor"] = ["U+3bcd"]
UNICODE_TO_BLISS["U+3bcd"].append("pastor")
BLISS_TO_UNICODE["preacher"] = ["U+3bcd"]
UNICODE_TO_BLISS["U+3bcd"].append("preacher")
BLISS_TO_UNICODE["priest"] = ["U+3bcd"]
UNICODE_TO_BLISS["U+3bcd"].append("priest")
BLISS_TO_UNICODE["rabbi"] = ["U+3bcd"]
UNICODE_TO_BLISS["U+3bcd"].append("rabbi")
BLISS_TO_UNICODE["minister,pastor,preacher,priest,rabbi"] = ["U+3bcd"]
UNICODE_TO_BLISS["U+3bcd"].append("minister,pastor,preacher,priest,rabbi")
BLISS_TO_UNICODE["to teach"] = ["U+3bce"]
UNICODE_TO_BLISS["U+3bce"] = ["to teach"]
BLISS_TO_UNICODE["combine"] = ["U+3bcf"]
UNICODE_TO_BLISS["U+3bcf"] = ["combine"]
BLISS_TO_UNICODE["connect"] = ["U+3bcf"]
UNICODE_TO_BLISS["U+3bcf"].append("connect")
BLISS_TO_UNICODE["link"] = ["U+3bcf"]
UNICODE_TO_BLISS["U+3bcf"].append("link")
BLISS_TO_UNICODE["combine,connect,link"] = ["U+3bcf"]
UNICODE_TO_BLISS["U+3bcf"].append("combine,connect,link")
BLISS_TO_UNICODE["pictograph of an atom with inner nucleus"] = ["U+3bd0"]
UNICODE_TO_BLISS["U+3bd0"] = ["pictograph of an atom with inner nucleus"]
BLISS_TO_UNICODE["pointer showing the movement of a circling electron"] = ["U+3bd1"]
UNICODE_TO_BLISS["U+3bd1"] = ["pointer showing the movement of a circling electron"]
BLISS_TO_UNICODE["army"] = ["U+3bd2"]
UNICODE_TO_BLISS["U+3bd2"] = ["army"]
BLISS_TO_UNICODE["regular army"] = ["U+3bd2"]
UNICODE_TO_BLISS["U+3bd2"].append("regular army")
BLISS_TO_UNICODE["ground forces"] = ["U+3bd2"]
UNICODE_TO_BLISS["U+3bd2"].append("ground forces")
BLISS_TO_UNICODE["army,regular army,ground forces"] = ["U+3bd2"]
UNICODE_TO_BLISS["U+3bd2"].append("army,regular army,ground forces")
BLISS_TO_UNICODE["Africa"] = ["U+3bd3"]
UNICODE_TO_BLISS["U+3bd3"] = ["Africa"]
BLISS_TO_UNICODE["erect penis"] = ["U+33ed"]
UNICODE_TO_BLISS["U+33ed"].append("erect penis")
BLISS_TO_UNICODE["erection,erect penis"] = ["U+33ed"]
UNICODE_TO_BLISS["U+33ed"].append("erection,erect penis")
BLISS_TO_UNICODE["mature"] = ["U+34b4"]
UNICODE_TO_BLISS["U+34b4"].append("mature")
BLISS_TO_UNICODE["adult,mature"] = ["U+34b4"]
UNICODE_TO_BLISS["U+34b4"].append("adult,mature")
BLISS_TO_UNICODE["curry sauce"] = ["U+3bd4"]
UNICODE_TO_BLISS["U+3bd4"] = ["curry sauce"]
BLISS_TO_UNICODE["continuously"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("continuously")
BLISS_TO_UNICODE["still,continuously"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("still,continuously")
BLISS_TO_UNICODE["to continue"] = ["U+3bd5"]
UNICODE_TO_BLISS["U+3bd5"] = ["to continue"]
BLISS_TO_UNICODE["child harness"] = ["U+3bd6"]
UNICODE_TO_BLISS["U+3bd6"] = ["child harness"]
BLISS_TO_UNICODE["walking reins"] = ["U+3bd6"]
UNICODE_TO_BLISS["U+3bd6"].append("walking reins")
BLISS_TO_UNICODE["child harness,walking reins"] = ["U+3bd6"]
UNICODE_TO_BLISS["U+3bd6"].append("child harness,walking reins")
BLISS_TO_UNICODE["harness"] = ["U+3bd7"]
UNICODE_TO_BLISS["U+3bd7"] = ["harness"]
BLISS_TO_UNICODE["aerial"] = ["U+3bd8"]
UNICODE_TO_BLISS["U+3bd8"] = ["aerial"]
BLISS_TO_UNICODE["antenna"] = ["U+3bd8"]
UNICODE_TO_BLISS["U+3bd8"].append("antenna")
BLISS_TO_UNICODE["aerial,antenna"] = ["U+3bd8"]
UNICODE_TO_BLISS["U+3bd8"].append("aerial,antenna")
BLISS_TO_UNICODE["skullcap"] = ["U+3bd9"]
UNICODE_TO_BLISS["U+3bd9"] = ["skullcap"]
BLISS_TO_UNICODE["kipa"] = ["U+3bd9"]
UNICODE_TO_BLISS["U+3bd9"].append("kipa")
BLISS_TO_UNICODE["yarmulke"] = ["U+3bd9"]
UNICODE_TO_BLISS["U+3bd9"].append("yarmulke")
BLISS_TO_UNICODE["skullcap,kipa,yarmulke"] = ["U+3bd9"]
UNICODE_TO_BLISS["U+3bd9"].append("skullcap,kipa,yarmulke")
BLISS_TO_UNICODE["burnable"] = ["U+3bda"]
UNICODE_TO_BLISS["U+3bda"] = ["burnable"]
BLISS_TO_UNICODE["combustible"] = ["U+3bda"]
UNICODE_TO_BLISS["U+3bda"].append("combustible")
BLISS_TO_UNICODE["ignitable"] = ["U+3bda"]
UNICODE_TO_BLISS["U+3bda"].append("ignitable")
BLISS_TO_UNICODE["burnable,combustible,ignitable"] = ["U+3bda"]
UNICODE_TO_BLISS["U+3bda"].append("burnable,combustible,ignitable")
BLISS_TO_UNICODE["influence"] = ["U+3bdb"]
UNICODE_TO_BLISS["U+3bdb"] = ["influence"]
BLISS_TO_UNICODE["affect"] = ["U+3bdb"]
UNICODE_TO_BLISS["U+3bdb"].append("affect")
BLISS_TO_UNICODE["influence,affect"] = ["U+3bdb"]
UNICODE_TO_BLISS["U+3bdb"].append("influence,affect")
BLISS_TO_UNICODE["conversation"] = ["U+3927"]
UNICODE_TO_BLISS["U+3927"].append("conversation")
BLISS_TO_UNICODE["debate"] = ["U+3927"]
UNICODE_TO_BLISS["U+3927"].append("debate")
BLISS_TO_UNICODE["chat"] = ["U+3927"]
UNICODE_TO_BLISS["U+3927"].append("chat")
BLISS_TO_UNICODE["discussion,conversation,debate,chat"] = ["U+3927"]
UNICODE_TO_BLISS["U+3927"].append("discussion,conversation,debate,chat")
BLISS_TO_UNICODE["phantom"].append("U+39dd")
UNICODE_TO_BLISS["U+39dd"].append("phantom")
BLISS_TO_UNICODE["ghost,phantom"] = ["U+39dd"]
UNICODE_TO_BLISS["U+39dd"].append("ghost,phantom")
BLISS_TO_UNICODE["transparent"] = ["U+3bdc"]
UNICODE_TO_BLISS["U+3bdc"] = ["transparent"]
BLISS_TO_UNICODE["country music"] = ["U+3bdd"]
UNICODE_TO_BLISS["U+3bdd"] = ["country music"]
BLISS_TO_UNICODE["parakeet"] = ["U+3bde"]
UNICODE_TO_BLISS["U+3bde"] = ["parakeet"]
BLISS_TO_UNICODE["budgie"] = ["U+3bde"]
UNICODE_TO_BLISS["U+3bde"].append("budgie")
BLISS_TO_UNICODE["parakeet,budgie"] = ["U+3bde"]
UNICODE_TO_BLISS["U+3bde"].append("parakeet,budgie")
BLISS_TO_UNICODE["parrot"] = ["U+3bdf"]
UNICODE_TO_BLISS["U+3bdf"] = ["parrot"]
BLISS_TO_UNICODE["pie"] = ["U+3be0"]
UNICODE_TO_BLISS["U+3be0"] = ["pie"]
BLISS_TO_UNICODE["tart"] = ["U+3be0"]
UNICODE_TO_BLISS["U+3be0"].append("tart")
BLISS_TO_UNICODE["pie,tart"] = ["U+3be0"]
UNICODE_TO_BLISS["U+3be0"].append("pie,tart")
BLISS_TO_UNICODE["rabies"] = ["U+3be1"]
UNICODE_TO_BLISS["U+3be1"] = ["rabies"]
BLISS_TO_UNICODE["to bite"] = ["U+3be2"]
UNICODE_TO_BLISS["U+3be2"] = ["to bite"]
BLISS_TO_UNICODE["Tisha B'Av"] = ["U+3be3"]
UNICODE_TO_BLISS["U+3be3"] = ["Tisha B'Av"]
BLISS_TO_UNICODE["humerus"] = ["U+3be4"]
UNICODE_TO_BLISS["U+3be4"] = ["humerus"]
BLISS_TO_UNICODE["upper arm bone"] = ["U+3be4"]
UNICODE_TO_BLISS["U+3be4"].append("upper arm bone")
BLISS_TO_UNICODE["humerus,upper arm bone"] = ["U+3be4"]
UNICODE_TO_BLISS["U+3be4"].append("humerus,upper arm bone")
BLISS_TO_UNICODE["upper arm"] = ["U+3be5"]
UNICODE_TO_BLISS["U+3be5"] = ["upper arm"]
BLISS_TO_UNICODE["accusation"] = ["U+3be6"]
UNICODE_TO_BLISS["U+3be6"] = ["accusation"]
BLISS_TO_UNICODE["charge"] = ["U+3be6"]
UNICODE_TO_BLISS["U+3be6"].append("charge")
BLISS_TO_UNICODE["prosecution"] = ["U+3be6"]
UNICODE_TO_BLISS["U+3be6"].append("prosecution")
BLISS_TO_UNICODE["myna"] = ["U+3bdf"]
UNICODE_TO_BLISS["U+3bdf"].append("myna")
BLISS_TO_UNICODE["talking bird"] = ["U+3bdf"]
UNICODE_TO_BLISS["U+3bdf"].append("talking bird")
BLISS_TO_UNICODE["parrot,myna,talking bird"] = ["U+3bdf"]
UNICODE_TO_BLISS["U+3bdf"].append("parrot,myna,talking bird")
BLISS_TO_UNICODE["parking ticket"] = ["U+3be7"]
UNICODE_TO_BLISS["U+3be7"] = ["parking ticket"]
BLISS_TO_UNICODE["parking place"] = ["U+3be8"]
UNICODE_TO_BLISS["U+3be8"] = ["parking place"]
BLISS_TO_UNICODE["ground"].append("U+35f6")
UNICODE_TO_BLISS["U+35f6"].append("ground")
BLISS_TO_UNICODE["land"].append("U+35f6")
UNICODE_TO_BLISS["U+35f6"].append("land")
BLISS_TO_UNICODE["earth,ground,land"] = ["U+35f6"]
UNICODE_TO_BLISS["U+35f6"].append("earth,ground,land")
BLISS_TO_UNICODE["landing"] = ["U+3be9"]
UNICODE_TO_BLISS["U+3be9"] = ["landing"]
BLISS_TO_UNICODE["Host"] = ["U+3bea"]
UNICODE_TO_BLISS["U+3bea"] = ["Host"]
BLISS_TO_UNICODE["wafer"] = ["U+3bea"]
UNICODE_TO_BLISS["U+3bea"].append("wafer")
BLISS_TO_UNICODE["Host,wafer"] = ["U+3bea"]
UNICODE_TO_BLISS["U+3bea"].append("Host,wafer")
BLISS_TO_UNICODE["age"] = ["U+3beb"]
UNICODE_TO_BLISS["U+3beb"] = ["age"]
BLISS_TO_UNICODE["satellite"] = ["U+3bec"]
UNICODE_TO_BLISS["U+3bec"] = ["satellite"]
BLISS_TO_UNICODE["beverage"].append("U+37d7")
UNICODE_TO_BLISS["U+37d7"].append("beverage")
BLISS_TO_UNICODE["drink,beverage"] = ["U+37d7"]
UNICODE_TO_BLISS["U+37d7"].append("drink,beverage")
BLISS_TO_UNICODE["Aegir"] = ["U+3bed"]
UNICODE_TO_BLISS["U+3bed"] = ["Aegir"]
BLISS_TO_UNICODE["walker"] = ["U+3bee"]
UNICODE_TO_BLISS["U+3bee"] = ["walker"]
BLISS_TO_UNICODE["grownup"] = ["U+34b4"]
UNICODE_TO_BLISS["U+34b4"].append("grownup")
BLISS_TO_UNICODE["adult,grownup"] = ["U+34b4"]
UNICODE_TO_BLISS["U+34b4"].append("adult,grownup")
BLISS_TO_UNICODE["away"] = ["U+3bef"]
UNICODE_TO_BLISS["U+3bef"] = ["away"]
BLISS_TO_UNICODE["at a distance"].append("U+3bef")
UNICODE_TO_BLISS["U+3bef"].append("at a distance")
BLISS_TO_UNICODE["off"] = ["U+3bef"]
UNICODE_TO_BLISS["U+3bef"].append("off")
BLISS_TO_UNICODE["away,at a distance,off"] = ["U+3bef"]
UNICODE_TO_BLISS["U+3bef"].append("away,at a distance,off")
BLISS_TO_UNICODE["permeable material"] = ["U+3bf0"]
UNICODE_TO_BLISS["U+3bf0"] = ["permeable material"]
BLISS_TO_UNICODE["Mercury"] = ["U+3bf1"]
UNICODE_TO_BLISS["U+3bf1"] = ["Mercury"]
BLISS_TO_UNICODE["rock planet"] = ["U+3bf2"]
UNICODE_TO_BLISS["U+3bf2"] = ["rock planet"]
BLISS_TO_UNICODE["code"] = ["U+3bf3"]
UNICODE_TO_BLISS["U+3bf3"] = ["code"]
BLISS_TO_UNICODE["password"] = ["U+3bf3"]
UNICODE_TO_BLISS["U+3bf3"].append("password")
BLISS_TO_UNICODE["code,password"] = ["U+3bf3"]
UNICODE_TO_BLISS["U+3bf3"].append("code,password")
BLISS_TO_UNICODE["piss"].append("U+36b0")
UNICODE_TO_BLISS["U+36b0"].append("piss")
BLISS_TO_UNICODE["pee"].append("U+36b0")
UNICODE_TO_BLISS["U+36b0"].append("pee")
BLISS_TO_UNICODE["piddle"].append("U+36b0")
UNICODE_TO_BLISS["U+36b0"].append("piddle")
BLISS_TO_UNICODE["weewee"] = ["U+36b0"]
UNICODE_TO_BLISS["U+36b0"].append("weewee")
BLISS_TO_UNICODE["water"].append("U+36b0")
UNICODE_TO_BLISS["U+36b0"].append("water")
BLISS_TO_UNICODE["urine,piss,pee,piddle,weewee,water"] = ["U+36b0"]
UNICODE_TO_BLISS["U+36b0"].append("urine,piss,pee,piddle,weewee,water")
BLISS_TO_UNICODE["scratch"] = ["U+3bf4"]
UNICODE_TO_BLISS["U+3bf4"] = ["scratch"]
BLISS_TO_UNICODE["illustrated"] = ["U+3bf5"]
UNICODE_TO_BLISS["U+3bf5"] = ["illustrated"]
BLISS_TO_UNICODE["illustrating"] = ["U+3bf5"]
UNICODE_TO_BLISS["U+3bf5"].append("illustrating")
BLISS_TO_UNICODE["illustrated,illustrating"] = ["U+3bf5"]
UNICODE_TO_BLISS["U+3bf5"].append("illustrated,illustrating")
BLISS_TO_UNICODE["illustrtion"] = ["U+3bf6"]
UNICODE_TO_BLISS["U+3bf6"] = ["illustrtion"]
BLISS_TO_UNICODE["hammer throw"] = ["U+3bf7"]
UNICODE_TO_BLISS["U+3bf7"] = ["hammer throw"]
BLISS_TO_UNICODE["leisure time"] = ["U+3bf8"]
UNICODE_TO_BLISS["U+3bf8"] = ["leisure time"]
BLISS_TO_UNICODE["free"] = ["U+3bf9"]
UNICODE_TO_BLISS["U+3bf9"] = ["free"]
BLISS_TO_UNICODE["send"] = ["U+3bfa"]
UNICODE_TO_BLISS["U+3bfa"] = ["send"]
BLISS_TO_UNICODE["to carry"] = ["U+3bfb"]
UNICODE_TO_BLISS["U+3bfb"] = ["to carry"]
BLISS_TO_UNICODE["light switch"] = ["U+3bfc"]
UNICODE_TO_BLISS["U+3bfc"] = ["light switch"]
BLISS_TO_UNICODE["artificial insemination"] = ["U+3bfd"]
UNICODE_TO_BLISS["U+3bfd"] = ["artificial insemination"]
BLISS_TO_UNICODE["dislike"] = ["U+3bfe"]
UNICODE_TO_BLISS["U+3bfe"] = ["dislike"]
BLISS_TO_UNICODE["Netherlands"] = ["U+3bff"]
UNICODE_TO_BLISS["U+3bff"] = ["Netherlands"]
BLISS_TO_UNICODE["Holland"] = ["U+3bff"]
UNICODE_TO_BLISS["U+3bff"].append("Holland")
BLISS_TO_UNICODE["Chanukah"] = ["U+3c00"]
UNICODE_TO_BLISS["U+3c00"] = ["Chanukah"]
BLISS_TO_UNICODE["Hanukkah"] = ["U+3c00"]
UNICODE_TO_BLISS["U+3c00"].append("Hanukkah")
BLISS_TO_UNICODE["Chanukah,Hanukkah"] = ["U+3c00"]
UNICODE_TO_BLISS["U+3c00"].append("Chanukah,Hanukkah")
BLISS_TO_UNICODE["work of art"] = ["U+3c01"]
UNICODE_TO_BLISS["U+3c01"] = ["work of art"]
BLISS_TO_UNICODE["art object"] = ["U+3c01"]
UNICODE_TO_BLISS["U+3c01"].append("art object")
BLISS_TO_UNICODE["work of art,art object"] = ["U+3c01"]
UNICODE_TO_BLISS["U+3c01"].append("work of art,art object")
BLISS_TO_UNICODE["pictograph of a snowshoe"] = ["U+3c02"]
UNICODE_TO_BLISS["U+3c02"] = ["pictograph of a snowshoe"]
BLISS_TO_UNICODE["wipe"] = ["U+3c03"]
UNICODE_TO_BLISS["U+3c03"] = ["wipe"]
BLISS_TO_UNICODE["dust"].append("U+3c03")
UNICODE_TO_BLISS["U+3c03"].append("dust")
BLISS_TO_UNICODE["polish"] = ["U+3c03"]
UNICODE_TO_BLISS["U+3c03"].append("polish")
BLISS_TO_UNICODE["wipe,dust,polish"] = ["U+3c03"]
UNICODE_TO_BLISS["U+3c03"].append("wipe,dust,polish")
BLISS_TO_UNICODE["magic"] = ["U+3c04"]
UNICODE_TO_BLISS["U+3c04"] = ["magic"]
BLISS_TO_UNICODE["mystery"] = ["U+3c05"]
UNICODE_TO_BLISS["U+3c05"] = ["mystery"]
BLISS_TO_UNICODE["marry"] = ["U+3c06"]
UNICODE_TO_BLISS["U+3c06"] = ["marry"]
BLISS_TO_UNICODE["fewer"] = ["U+3c07"]
UNICODE_TO_BLISS["U+3c07"] = ["fewer"]
BLISS_TO_UNICODE["less"] = ["U+3c07"]
UNICODE_TO_BLISS["U+3c07"].append("less")
BLISS_TO_UNICODE["fewer,less"] = ["U+3c07"]
UNICODE_TO_BLISS["U+3c07"].append("fewer,less")
BLISS_TO_UNICODE["anxious"] = ["U+3c08"]
UNICODE_TO_BLISS["U+3c08"] = ["anxious"]
BLISS_TO_UNICODE["anxiously"] = ["U+3c08"]
UNICODE_TO_BLISS["U+3c08"].append("anxiously")
BLISS_TO_UNICODE["anxious,anxiously"] = ["U+3c08"]
UNICODE_TO_BLISS["U+3c08"].append("anxious,anxiously")
BLISS_TO_UNICODE["anxiety"] = ["U+3c09"]
UNICODE_TO_BLISS["U+3c09"] = ["anxiety"]
BLISS_TO_UNICODE["compete"] = ["U+3c0a"]
UNICODE_TO_BLISS["U+3c0a"] = ["compete"]
BLISS_TO_UNICODE["race"].append("U+3c0a")
UNICODE_TO_BLISS["U+3c0a"].append("race")
BLISS_TO_UNICODE["compete,race"] = ["U+3c0a"]
UNICODE_TO_BLISS["U+3c0a"].append("compete,race")
BLISS_TO_UNICODE["competition"].append("U+3244")
UNICODE_TO_BLISS["U+3244"].append("competition")
BLISS_TO_UNICODE["contest"] = ["U+3244"]
UNICODE_TO_BLISS["U+3244"].append("contest")
BLISS_TO_UNICODE["race,competition,contest"] = ["U+3244"]
UNICODE_TO_BLISS["U+3244"].append("race,competition,contest")
BLISS_TO_UNICODE["rack"] = ["U+3c0b"]
UNICODE_TO_BLISS["U+3c0b"] = ["rack"]
BLISS_TO_UNICODE["single foot"] = ["U+3c0b"]
UNICODE_TO_BLISS["U+3c0b"].append("single foot")
BLISS_TO_UNICODE["rack,single-foot"] = ["U+3c0b"]
UNICODE_TO_BLISS["U+3c0b"].append("rack,single-foot")
BLISS_TO_UNICODE["Iceland"] = ["U+3c0c"]
UNICODE_TO_BLISS["U+3c0c"] = ["Iceland"]
BLISS_TO_UNICODE["promise"] = ["U+3c0d"]
UNICODE_TO_BLISS["U+3c0d"] = ["promise"]
BLISS_TO_UNICODE["pledge"] = ["U+3c0d"]
UNICODE_TO_BLISS["U+3c0d"].append("pledge")
BLISS_TO_UNICODE["promise,pledge"] = ["U+3c0d"]
UNICODE_TO_BLISS["U+3c0d"].append("promise,pledge")
BLISS_TO_UNICODE["sweet shop"] = ["U+3c0e"]
UNICODE_TO_BLISS["U+3c0e"] = ["sweet shop"]
BLISS_TO_UNICODE["candy store"] = ["U+3c0e"]
UNICODE_TO_BLISS["U+3c0e"].append("candy store")
BLISS_TO_UNICODE["sweet shop,candy store"] = ["U+3c0e"]
UNICODE_TO_BLISS["U+3c0e"].append("sweet shop,candy store")
BLISS_TO_UNICODE["touch"] = ["U+3c0f"]
UNICODE_TO_BLISS["U+3c0f"] = ["touch"]
BLISS_TO_UNICODE["sense of touch"] = ["U+3c0f"]
UNICODE_TO_BLISS["U+3c0f"].append("sense of touch")
BLISS_TO_UNICODE["tactile sense"] = ["U+3c0f"]
UNICODE_TO_BLISS["U+3c0f"].append("tactile sense")
BLISS_TO_UNICODE["touch,sense of touch,tactile sense"] = ["U+3c0f"]
UNICODE_TO_BLISS["U+3c0f"].append("touch,sense of touch,tactile sense")
BLISS_TO_UNICODE["skin"] = ["U+3c10"]
UNICODE_TO_BLISS["U+3c10"] = ["skin"]
BLISS_TO_UNICODE["biomass"] = ["U+3c11"]
UNICODE_TO_BLISS["U+3c11"] = ["biomass"]
BLISS_TO_UNICODE["biofuel"] = ["U+3c11"]
UNICODE_TO_BLISS["U+3c11"].append("biofuel")
BLISS_TO_UNICODE["biomass,biofuel"] = ["U+3c11"]
UNICODE_TO_BLISS["U+3c11"].append("biomass,biofuel")
BLISS_TO_UNICODE["trackball"] = ["U+3c12"]
UNICODE_TO_BLISS["U+3c12"] = ["trackball"]
BLISS_TO_UNICODE["wheat"] = ["U+3c13"]
UNICODE_TO_BLISS["U+3c13"] = ["wheat"]
BLISS_TO_UNICODE["spaghetti"] = ["U+3c14"]
UNICODE_TO_BLISS["U+3c14"] = ["spaghetti"]
BLISS_TO_UNICODE["pasta"] = ["U+3c15"]
UNICODE_TO_BLISS["U+3c15"] = ["pasta"]
BLISS_TO_UNICODE["Durga"] = ["U+3c16"]
UNICODE_TO_BLISS["U+3c16"] = ["Durga"]
BLISS_TO_UNICODE["goddess"] = ["U+3c17"]
UNICODE_TO_BLISS["U+3c17"] = ["goddess"]
BLISS_TO_UNICODE["10"] = ["U+3c18"]
UNICODE_TO_BLISS["U+3c18"] = ["10"]
BLISS_TO_UNICODE["index"] = ["U+3c19"]
UNICODE_TO_BLISS["U+3c19"] = ["index"]
BLISS_TO_UNICODE["list of contents"] = ["U+3c19"]
UNICODE_TO_BLISS["U+3c19"].append("list of contents")
BLISS_TO_UNICODE["index,list of contents"] = ["U+3c19"]
UNICODE_TO_BLISS["U+3c19"].append("index,list of contents")
BLISS_TO_UNICODE["sauerkraut"] = ["U+3c1a"]
UNICODE_TO_BLISS["U+3c1a"] = ["sauerkraut"]
BLISS_TO_UNICODE["sour"] = ["U+3c1b"]
UNICODE_TO_BLISS["U+3c1b"] = ["sour"]
BLISS_TO_UNICODE["disembarkation"].append("U+37b1")
UNICODE_TO_BLISS["U+37b1"].append("disembarkation")
BLISS_TO_UNICODE["debarkation,disembarkation"] = ["U+37b1"]
UNICODE_TO_BLISS["U+37b1"].append("debarkation,disembarkation")
BLISS_TO_UNICODE["twins"] = ["U+3c1c"]
UNICODE_TO_BLISS["U+3c1c"] = ["twins"]
BLISS_TO_UNICODE["switch off"] = ["U+3c1d"]
UNICODE_TO_BLISS["U+3c1d"] = ["switch off"]
BLISS_TO_UNICODE["turn off"] = ["U+3c1d"]
UNICODE_TO_BLISS["U+3c1d"].append("turn off")
BLISS_TO_UNICODE["switch off,turn off"] = ["U+3c1d"]
UNICODE_TO_BLISS["U+3c1d"].append("switch off,turn off")
BLISS_TO_UNICODE["switch"] = ["U+3c1e"]
UNICODE_TO_BLISS["U+3c1e"] = ["switch"]
BLISS_TO_UNICODE["scenery"] = ["U+3c20"]
UNICODE_TO_BLISS["U+3c20"] = ["scenery"]
BLISS_TO_UNICODE["landscape"] = ["U+3c20"]
UNICODE_TO_BLISS["U+3c20"].append("landscape")
BLISS_TO_UNICODE["scenery,landscape"] = ["U+3c20"]
UNICODE_TO_BLISS["U+3c20"].append("scenery,landscape")
BLISS_TO_UNICODE["lee"] = ["U+3c21"]
UNICODE_TO_BLISS["U+3c21"] = ["lee"]
BLISS_TO_UNICODE["shelter"].append("U+3c21")
UNICODE_TO_BLISS["U+3c21"].append("shelter")
BLISS_TO_UNICODE["lee,shelter"] = ["U+3c21"]
UNICODE_TO_BLISS["U+3c21"].append("lee,shelter")
BLISS_TO_UNICODE["poverty"] = ["U+3c22"]
UNICODE_TO_BLISS["U+3c22"] = ["poverty"]
BLISS_TO_UNICODE["consideration"].append("U+3a4f")
UNICODE_TO_BLISS["U+3a4f"].append("consideration")
BLISS_TO_UNICODE["vinegar"] = ["U+3c23"]
UNICODE_TO_BLISS["U+3c23"] = ["vinegar"]
BLISS_TO_UNICODE["combination of flavouring and sharp"] = ["U+3c24"]
UNICODE_TO_BLISS["U+3c24"] = ["combination of flavouring and sharp"]
BLISS_TO_UNICODE["wow"] = ["U+3c25"]
UNICODE_TO_BLISS["U+3c25"] = ["wow"]
BLISS_TO_UNICODE["super"] = ["U+3c25"]
UNICODE_TO_BLISS["U+3c25"].append("super")
BLISS_TO_UNICODE["great"] = ["U+3c25"]
UNICODE_TO_BLISS["U+3c25"].append("great")
BLISS_TO_UNICODE["neat"] = ["U+3c25"]
UNICODE_TO_BLISS["U+3c25"].append("neat")
BLISS_TO_UNICODE["cool"] = ["U+3c25"]
UNICODE_TO_BLISS["U+3c25"].append("cool")
BLISS_TO_UNICODE["wow,super,great,neat,cool"] = ["U+3c25"]
UNICODE_TO_BLISS["U+3c25"].append("wow,super,great,neat,cool")
BLISS_TO_UNICODE["wonderful"] = ["U+3c25"]
UNICODE_TO_BLISS["U+3c25"].append("wonderful")
BLISS_TO_UNICODE["fantastic"] = ["U+3c25"]
UNICODE_TO_BLISS["U+3c25"].append("fantastic")
BLISS_TO_UNICODE["great,wonderful,fantastic"] = ["U+3c25"]
UNICODE_TO_BLISS["U+3c25"].append("great,wonderful,fantastic")
BLISS_TO_UNICODE["well"] = ["U+3c26"]
UNICODE_TO_BLISS["U+3c26"] = ["well"]
BLISS_TO_UNICODE["fine"] = ["U+3c27"]
UNICODE_TO_BLISS["U+3c27"] = ["fine"]
BLISS_TO_UNICODE["ok"] = ["U+3c28"]
UNICODE_TO_BLISS["U+3c28"] = ["ok"]
BLISS_TO_UNICODE["okay"] = ["U+3c29"]
UNICODE_TO_BLISS["U+3c29"] = ["okay"]
BLISS_TO_UNICODE["all right"] = ["U+3c2a"]
UNICODE_TO_BLISS["U+3c2a"] = ["all right"]
BLISS_TO_UNICODE["case"] = ["U+3c2b"]
UNICODE_TO_BLISS["U+3c2b"] = ["case"]
BLISS_TO_UNICODE["casing"] = ["U+3c2b"]
UNICODE_TO_BLISS["U+3c2b"].append("casing")
BLISS_TO_UNICODE["case,casing"] = ["U+3c2b"]
UNICODE_TO_BLISS["U+3c2b"].append("case,casing")
BLISS_TO_UNICODE["acquire"] = ["U+3247"]
UNICODE_TO_BLISS["U+3247"].append("acquire")
BLISS_TO_UNICODE["receive"] = ["U+3247"]
UNICODE_TO_BLISS["U+3247"].append("receive")
BLISS_TO_UNICODE["get,acquire,receive"] = ["U+3247"]
UNICODE_TO_BLISS["U+3247"].append("get,acquire,receive")
BLISS_TO_UNICODE["coffin"] = ["U+3c2c"]
UNICODE_TO_BLISS["U+3c2c"] = ["coffin"]
BLISS_TO_UNICODE["reclining"] = ["U+3c2d"]
UNICODE_TO_BLISS["U+3c2d"] = ["reclining"]
BLISS_TO_UNICODE["lying"] = ["U+3c2e"]
UNICODE_TO_BLISS["U+3c2e"] = ["lying"]
BLISS_TO_UNICODE["grandchild"] = ["U+3c2f"]
UNICODE_TO_BLISS["U+3c2f"] = ["grandchild"]
BLISS_TO_UNICODE["grandparents"] = ["U+3c30"]
UNICODE_TO_BLISS["U+3c30"] = ["grandparents"]
BLISS_TO_UNICODE["popcorn"] = ["U+3c31"]
UNICODE_TO_BLISS["U+3c31"] = ["popcorn"]
BLISS_TO_UNICODE["castle ruin"] = ["U+3798"]
UNICODE_TO_BLISS["U+3798"].append("castle ruin")
BLISS_TO_UNICODE["castle"] = ["U+3c32"]
UNICODE_TO_BLISS["U+3c32"] = ["castle"]
BLISS_TO_UNICODE["maker"] = ["U+3c33"]
UNICODE_TO_BLISS["U+3c33"] = ["maker"]
BLISS_TO_UNICODE["manufacturer"] = ["U+3c33"]
UNICODE_TO_BLISS["U+3c33"].append("manufacturer")
BLISS_TO_UNICODE["producer"] = ["U+3c33"]
UNICODE_TO_BLISS["U+3c33"].append("producer")
BLISS_TO_UNICODE["maker,manufacturer,producer"] = ["U+3c33"]
UNICODE_TO_BLISS["U+3c33"].append("maker,manufacturer,producer")
BLISS_TO_UNICODE["sun lounger"] = ["U+3c34"]
UNICODE_TO_BLISS["U+3c34"] = ["sun lounger"]
BLISS_TO_UNICODE["deck chair"] = ["U+3c34"]
UNICODE_TO_BLISS["U+3c34"].append("deck chair")
BLISS_TO_UNICODE["sun lounger,deck chair"] = ["U+3c34"]
UNICODE_TO_BLISS["U+3c34"].append("sun lounger,deck chair")
BLISS_TO_UNICODE["sofa"] = ["U+3c35"]
UNICODE_TO_BLISS["U+3c35"] = ["sofa"]
BLISS_TO_UNICODE["self control"] = ["U+3c36"]
UNICODE_TO_BLISS["U+3c36"] = ["self control"]
BLISS_TO_UNICODE["self-control"] = ["U+3c36"]
UNICODE_TO_BLISS["U+3c36"].append("self-control")
BLISS_TO_UNICODE["to lead"] = ["U+3c37"]
UNICODE_TO_BLISS["U+3c37"] = ["to lead"]
BLISS_TO_UNICODE["dormouse"] = ["U+3c38"]
UNICODE_TO_BLISS["U+3c38"] = ["dormouse"]
BLISS_TO_UNICODE["Vatican City"] = ["U+3690"]
UNICODE_TO_BLISS["U+3690"].append("Vatican City")
BLISS_TO_UNICODE["Vatican,Vatican City"] = ["U+3690"]
UNICODE_TO_BLISS["U+3690"].append("Vatican,Vatican City")
BLISS_TO_UNICODE["samosa"] = ["U+3c39"]
UNICODE_TO_BLISS["U+3c39"] = ["samosa"]
BLISS_TO_UNICODE["pirogue"] = ["U+3c39"]
UNICODE_TO_BLISS["U+3c39"].append("pirogue")
BLISS_TO_UNICODE["samosa,pirogue"] = ["U+3c39"]
UNICODE_TO_BLISS["U+3c39"].append("samosa,pirogue")
BLISS_TO_UNICODE["trust"] = ["U+3c3a"]
UNICODE_TO_BLISS["U+3c3a"] = ["trust"]
BLISS_TO_UNICODE["confidence"] = ["U+3c3a"]
UNICODE_TO_BLISS["U+3c3a"].append("confidence")
BLISS_TO_UNICODE["trust,confidence"] = ["U+3c3a"]
UNICODE_TO_BLISS["U+3c3a"].append("trust,confidence")
BLISS_TO_UNICODE["exciting"] = ["U+3c3b"]
UNICODE_TO_BLISS["U+3c3b"] = ["exciting"]
BLISS_TO_UNICODE["excitingly"] = ["U+3c3b"]
UNICODE_TO_BLISS["U+3c3b"].append("excitingly")
BLISS_TO_UNICODE["excited"] = ["U+3c3b"]
UNICODE_TO_BLISS["U+3c3b"].append("excited")
BLISS_TO_UNICODE["excitedly"] = ["U+3c3b"]
UNICODE_TO_BLISS["U+3c3b"].append("excitedly")
BLISS_TO_UNICODE["exciting,excitingly,excited,excitedly"] = ["U+3c3b"]
UNICODE_TO_BLISS["U+3c3b"].append("exciting,excitingly,excited,excitedly")
BLISS_TO_UNICODE["excitement"] = ["U+3c3c"]
UNICODE_TO_BLISS["U+3c3c"] = ["excitement"]
BLISS_TO_UNICODE["criminal"].append("U+3a85")
UNICODE_TO_BLISS["U+3a85"].append("criminal")
BLISS_TO_UNICODE["illegal,criminal"] = ["U+3a85"]
UNICODE_TO_BLISS["U+3a85"].append("illegal,criminal")
BLISS_TO_UNICODE["next"] = ["U+3c3d"]
UNICODE_TO_BLISS["U+3c3d"] = ["next"]
BLISS_TO_UNICODE["duplicate"].append("U+34d6")
UNICODE_TO_BLISS["U+34d6"].append("duplicate")
BLISS_TO_UNICODE["copy,duplicate"] = ["U+34d6"]
UNICODE_TO_BLISS["U+34d6"].append("copy,duplicate")
BLISS_TO_UNICODE["to repeat"] = ["U+3c3e"]
UNICODE_TO_BLISS["U+3c3e"] = ["to repeat"]
BLISS_TO_UNICODE["repeat"] = ["U+3c3f"]
UNICODE_TO_BLISS["U+3c3f"] = ["repeat"]
BLISS_TO_UNICODE["copy"].append("U+3c3f")
UNICODE_TO_BLISS["U+3c3f"].append("copy")
BLISS_TO_UNICODE["duplicate"].append("U+3c3f")
UNICODE_TO_BLISS["U+3c3f"].append("duplicate")
BLISS_TO_UNICODE["reproduce"] = ["U+3c3f"]
UNICODE_TO_BLISS["U+3c3f"].append("reproduce")
BLISS_TO_UNICODE["repeat,copy,duplicate,reproduce"] = ["U+3c3f"]
UNICODE_TO_BLISS["U+3c3f"].append("repeat,copy,duplicate,reproduce")
BLISS_TO_UNICODE["doubt 22911"] = ["U+3c40"]
UNICODE_TO_BLISS["U+3c40"] = ["doubt 22911"]
BLISS_TO_UNICODE["whatquestion mark)"] = ["U+3c41"]
UNICODE_TO_BLISS["U+3c41"] = ["whatquestion mark)"]
BLISS_TO_UNICODE["uncertainty"] = ["U+32e5"]
UNICODE_TO_BLISS["U+32e5"].append("uncertainty")
BLISS_TO_UNICODE["doubt,uncertainty"] = ["U+32e5"]
UNICODE_TO_BLISS["U+32e5"].append("doubt,uncertainty")
BLISS_TO_UNICODE["be sceptical"] = ["U+33a6"]
UNICODE_TO_BLISS["U+33a6"].append("be sceptical")
BLISS_TO_UNICODE["doubt"].append("U+33a6")
UNICODE_TO_BLISS["U+33a6"].append("doubt")
BLISS_TO_UNICODE["question,be sceptical,doubt"] = ["U+33a6"]
UNICODE_TO_BLISS["U+33a6"].append("question,be sceptical,doubt")
BLISS_TO_UNICODE["filled cabbage"] = ["U+3c42"]
UNICODE_TO_BLISS["U+3c42"] = ["filled cabbage"]
BLISS_TO_UNICODE["stuffed cabbage"] = ["U+3c42"]
UNICODE_TO_BLISS["U+3c42"].append("stuffed cabbage")
BLISS_TO_UNICODE["filled cabbage,stuffed cabbage"] = ["U+3c42"]
UNICODE_TO_BLISS["U+3c42"].append("filled cabbage,stuffed cabbage")
BLISS_TO_UNICODE["pencil"] = ["U+3545"]
UNICODE_TO_BLISS["U+3545"].append("pencil")
BLISS_TO_UNICODE["pen,pencil"] = ["U+3545"]
UNICODE_TO_BLISS["U+3545"].append("pen,pencil")
BLISS_TO_UNICODE["fish finger"] = ["U+3c43"]
UNICODE_TO_BLISS["U+3c43"] = ["fish finger"]
BLISS_TO_UNICODE["concerning"] = ["U+341c"]
UNICODE_TO_BLISS["U+341c"].append("concerning")
BLISS_TO_UNICODE["in relation to"] = ["U+341c"]
UNICODE_TO_BLISS["U+341c"].append("in relation to")
BLISS_TO_UNICODE["of"].append("U+341c")
UNICODE_TO_BLISS["U+341c"].append("of")
BLISS_TO_UNICODE["on"].append("U+341c")
UNICODE_TO_BLISS["U+341c"].append("on")
BLISS_TO_UNICODE["about,concerning,in relation to,of,on"] = ["U+341c"]
UNICODE_TO_BLISS["U+341c"].append("about,concerning,in relation to,of,on")
BLISS_TO_UNICODE["protected water"] = ["U+3c44"]
UNICODE_TO_BLISS["U+3c44"] = ["protected water"]
BLISS_TO_UNICODE["Take your time"] = ["U+3c45"]
UNICODE_TO_BLISS["U+3c45"] = ["Take your time"]
BLISS_TO_UNICODE["Take your time!"] = ["U+3c45"]
UNICODE_TO_BLISS["U+3c45"].append("Take your time!")
BLISS_TO_UNICODE["infant"] = ["U+32c1"]
UNICODE_TO_BLISS["U+32c1"].append("infant")
BLISS_TO_UNICODE["baby,infant"] = ["U+32c1"]
UNICODE_TO_BLISS["U+32c1"].append("baby,infant")
BLISS_TO_UNICODE[" turned on its side"] = ["U+3c46"]
UNICODE_TO_BLISS["U+3c46"] = [" turned on its side"]
BLISS_TO_UNICODE["candy bar"] = ["U+3c47"]
UNICODE_TO_BLISS["U+3c47"] = ["candy bar"]
BLISS_TO_UNICODE["bar"] = ["U+3c48"]
UNICODE_TO_BLISS["U+3c48"] = ["bar"]
BLISS_TO_UNICODE["casserole"] = ["U+3c49"]
UNICODE_TO_BLISS["U+3c49"] = ["casserole"]
BLISS_TO_UNICODE["charity"] = ["U+3c4a"]
UNICODE_TO_BLISS["U+3c4a"] = ["charity"]
BLISS_TO_UNICODE["needy person"] = ["U+3c4b"]
UNICODE_TO_BLISS["U+3c4b"] = ["needy person"]
BLISS_TO_UNICODE["client"] = ["U+3c4c"]
UNICODE_TO_BLISS["U+3c4c"] = ["client"]
BLISS_TO_UNICODE["customer"] = ["U+3c4c"]
UNICODE_TO_BLISS["U+3c4c"].append("customer")
BLISS_TO_UNICODE["client,customer"] = ["U+3c4c"]
UNICODE_TO_BLISS["U+3c4c"].append("client,customer")
BLISS_TO_UNICODE["pop music"] = ["U+3c4d"]
UNICODE_TO_BLISS["U+3c4d"] = ["pop music"]
BLISS_TO_UNICODE["challenge"] = ["U+3c4e"]
UNICODE_TO_BLISS["U+3c4e"] = ["challenge"]
BLISS_TO_UNICODE["slim"] = ["U+34d7"]
UNICODE_TO_BLISS["U+34d7"].append("slim")
BLISS_TO_UNICODE["narrow"] = ["U+34d7"]
UNICODE_TO_BLISS["U+34d7"].append("narrow")
BLISS_TO_UNICODE["thin,slim,narrow"] = ["U+34d7"]
UNICODE_TO_BLISS["U+34d7"].append("thin,slim,narrow")
BLISS_TO_UNICODE["thinness"] = ["U+3c4f"]
UNICODE_TO_BLISS["U+3c4f"] = ["thinness"]
BLISS_TO_UNICODE["narrowness"] = ["U+3c50"]
UNICODE_TO_BLISS["U+3c50"] = ["narrowness"]
BLISS_TO_UNICODE["worksheet"] = ["U+3c51"]
UNICODE_TO_BLISS["U+3c51"] = ["worksheet"]
BLISS_TO_UNICODE["bend"] = ["U+3c52"]
UNICODE_TO_BLISS["U+3c52"] = ["bend"]
BLISS_TO_UNICODE["lock"] = ["U+3c53"]
UNICODE_TO_BLISS["U+3c53"] = ["lock"]
BLISS_TO_UNICODE["tall"] = ["U+34ba"]
UNICODE_TO_BLISS["U+34ba"].append("tall")
BLISS_TO_UNICODE["high,tall"] = ["U+34ba"]
UNICODE_TO_BLISS["U+34ba"].append("high,tall")
BLISS_TO_UNICODE["ginger sauce"] = ["U+3c54"]
UNICODE_TO_BLISS["U+3c54"] = ["ginger sauce"]
BLISS_TO_UNICODE["ginger"] = ["U+3c55"]
UNICODE_TO_BLISS["U+3c55"] = ["ginger"]
BLISS_TO_UNICODE["slide"] = ["U+3c56"]
UNICODE_TO_BLISS["U+3c56"] = ["slide"]
BLISS_TO_UNICODE["skid"] = ["U+3c56"]
UNICODE_TO_BLISS["U+3c56"].append("skid")
BLISS_TO_UNICODE["slip"].append("U+3c56")
UNICODE_TO_BLISS["U+3c56"].append("slip")
BLISS_TO_UNICODE["slide,skid,slip"] = ["U+3c56"]
UNICODE_TO_BLISS["U+3c56"].append("slide,skid,slip")
BLISS_TO_UNICODE["horn"].append("U+39f4")
UNICODE_TO_BLISS["U+39f4"].append("horn")
BLISS_TO_UNICODE["cornet"] = ["U+39f4"]
UNICODE_TO_BLISS["U+39f4"].append("cornet")
BLISS_TO_UNICODE["trumpet,horn,cornet"] = ["U+39f4"]
UNICODE_TO_BLISS["U+39f4"].append("trumpet,horn,cornet")
BLISS_TO_UNICODE["birthday"] = ["U+3c57"]
UNICODE_TO_BLISS["U+3c57"] = ["birthday"]
BLISS_TO_UNICODE["I need more time"] = ["U+3c58"]
UNICODE_TO_BLISS["U+3c58"] = ["I need more time"]
BLISS_TO_UNICODE["give me time"] = ["U+3c58"]
UNICODE_TO_BLISS["U+3c58"].append("give me time")
BLISS_TO_UNICODE["I need more time,give me time"] = ["U+3c58"]
UNICODE_TO_BLISS["U+3c58"].append("I need more time,give me time")
BLISS_TO_UNICODE["beast"] = ["U+3494"]
UNICODE_TO_BLISS["U+3494"].append("beast")
BLISS_TO_UNICODE["animal,beast"] = ["U+3494"]
UNICODE_TO_BLISS["U+3494"].append("animal,beast")
BLISS_TO_UNICODE["frying pan"] = ["U+3c59"]
UNICODE_TO_BLISS["U+3c59"] = ["frying pan"]
BLISS_TO_UNICODE["pan"] = ["U+3c5a"]
UNICODE_TO_BLISS["U+3c5a"] = ["pan"]
BLISS_TO_UNICODE["comedy"] = ["U+3c5b"]
UNICODE_TO_BLISS["U+3c5b"] = ["comedy"]
BLISS_TO_UNICODE["wristwatch"] = ["U+3926"]
UNICODE_TO_BLISS["U+3926"].append("wristwatch")
BLISS_TO_UNICODE["watch,wristwatch"] = ["U+3926"]
UNICODE_TO_BLISS["U+3926"].append("watch,wristwatch")
BLISS_TO_UNICODE["notebook"] = ["U+3c5c"]
UNICODE_TO_BLISS["U+3c5c"] = ["notebook"]
BLISS_TO_UNICODE["writing book"] = ["U+3c5c"]
UNICODE_TO_BLISS["U+3c5c"].append("writing book")
BLISS_TO_UNICODE["notebook,writing book"] = ["U+3c5c"]
UNICODE_TO_BLISS["U+3c5c"].append("notebook,writing book")
BLISS_TO_UNICODE["pictograph incorporating leafy vegetable"] = ["U+3c5d"]
UNICODE_TO_BLISS["U+3c5d"] = ["pictograph incorporating leafy vegetable"]
BLISS_TO_UNICODE["beach"] = ["U+3c5e"]
UNICODE_TO_BLISS["U+3c5e"] = ["beach"]
BLISS_TO_UNICODE["bank"] = ["U+3c5e"]
UNICODE_TO_BLISS["U+3c5e"].append("bank")
BLISS_TO_UNICODE["coast"] = ["U+3c5e"]
UNICODE_TO_BLISS["U+3c5e"].append("coast")
BLISS_TO_UNICODE["shore"].append("U+3c5e")
UNICODE_TO_BLISS["U+3c5e"].append("shore")
BLISS_TO_UNICODE["beach,bank,coast,shore"] = ["U+3c5e"]
UNICODE_TO_BLISS["U+3c5e"].append("beach,bank,coast,shore")
BLISS_TO_UNICODE["tomato"] = ["U+3c5f"]
UNICODE_TO_BLISS["U+3c5f"] = ["tomato"]
BLISS_TO_UNICODE["red"] = ["U+3c60"]
UNICODE_TO_BLISS["U+3c60"] = ["red"]
BLISS_TO_UNICODE["dependency"] = ["U+3c61"]
UNICODE_TO_BLISS["U+3c61"] = ["dependency"]
BLISS_TO_UNICODE["robot"] = ["U+3c62"]
UNICODE_TO_BLISS["U+3c62"] = ["robot"]
BLISS_TO_UNICODE["punctuation mark used as punctuation in symbol sentences"] = ["U+3c63"]
UNICODE_TO_BLISS["U+3c63"] = ["punctuation mark used as punctuation in symbol sentences"]
BLISS_TO_UNICODE["question mark"].append("U+3555")
UNICODE_TO_BLISS["U+3555"].append("question mark")
BLISS_TO_UNICODE["what,question mark"] = ["U+3555"]
UNICODE_TO_BLISS["U+3555"].append("what,question mark")
BLISS_TO_UNICODE["Greece"] = ["U+3c64"]
UNICODE_TO_BLISS["U+3c64"] = ["Greece"]
BLISS_TO_UNICODE["prison officer"] = ["U+3c65"]
UNICODE_TO_BLISS["U+3c65"] = ["prison officer"]
BLISS_TO_UNICODE["thigh"] = ["U+3c66"]
UNICODE_TO_BLISS["U+3c66"] = ["thigh"]
BLISS_TO_UNICODE["upper leg"] = ["U+3c66"]
UNICODE_TO_BLISS["U+3c66"].append("upper leg")
BLISS_TO_UNICODE["thigh,upper leg"] = ["U+3c66"]
UNICODE_TO_BLISS["U+3c66"].append("thigh,upper leg")
BLISS_TO_UNICODE["insight"] = ["U+3c67"]
UNICODE_TO_BLISS["U+3c67"] = ["insight"]
BLISS_TO_UNICODE["motorcycle"] = ["U+3c68"]
UNICODE_TO_BLISS["U+3c68"] = ["motorcycle"]
BLISS_TO_UNICODE["scooter"] = ["U+3c68"]
UNICODE_TO_BLISS["U+3c68"].append("scooter")
BLISS_TO_UNICODE["motorcycle,scooter"] = ["U+3c68"]
UNICODE_TO_BLISS["U+3c68"].append("motorcycle,scooter")
BLISS_TO_UNICODE["volte"] = ["U+3c69"]
UNICODE_TO_BLISS["U+3c69"] = ["volte"]
BLISS_TO_UNICODE["perfect"] = ["U+3c6a"]
UNICODE_TO_BLISS["U+3c6a"] = ["perfect"]
BLISS_TO_UNICODE["perfection"] = ["U+3c6b"]
UNICODE_TO_BLISS["U+3c6b"] = ["perfection"]
BLISS_TO_UNICODE["cease fire"] = ["U+3c6c"]
UNICODE_TO_BLISS["U+3c6c"] = ["cease fire"]
BLISS_TO_UNICODE["armistice"] = ["U+3c6c"]
UNICODE_TO_BLISS["U+3c6c"].append("armistice")
BLISS_TO_UNICODE["cease-fire,armistice"] = ["U+3c6c"]
UNICODE_TO_BLISS["U+3c6c"].append("cease-fire,armistice")
BLISS_TO_UNICODE["dump"] = ["U+3c6d"]
UNICODE_TO_BLISS["U+3c6d"] = ["dump"]
BLISS_TO_UNICODE["dispose"] = ["U+3c6d"]
UNICODE_TO_BLISS["U+3c6d"].append("dispose")
BLISS_TO_UNICODE["dump,dispose"] = ["U+3c6d"]
UNICODE_TO_BLISS["U+3c6d"].append("dump,dispose")
BLISS_TO_UNICODE["horse sled sport"] = ["U+3c6e"]
UNICODE_TO_BLISS["U+3c6e"] = ["horse sled sport"]
BLISS_TO_UNICODE["horse sled"] = ["U+3c6f"]
UNICODE_TO_BLISS["U+3c6f"] = ["horse sled"]
BLISS_TO_UNICODE["smoking addiction"] = ["U+3c70"]
UNICODE_TO_BLISS["U+3c70"] = ["smoking addiction"]
BLISS_TO_UNICODE["self harm"] = ["U+3c71"]
UNICODE_TO_BLISS["U+3c71"] = ["self harm"]
BLISS_TO_UNICODE["self-harm"] = ["U+3c71"]
UNICODE_TO_BLISS["U+3c71"].append("self-harm")
BLISS_TO_UNICODE["hobby"] = ["U+3c72"]
UNICODE_TO_BLISS["U+3c72"] = ["hobby"]
BLISS_TO_UNICODE["pastime"] = ["U+3c72"]
UNICODE_TO_BLISS["U+3c72"].append("pastime")
BLISS_TO_UNICODE["hobby,pastime"] = ["U+3c72"]
UNICODE_TO_BLISS["U+3c72"].append("hobby,pastime")
BLISS_TO_UNICODE["interesting"] = ["U+3c73"]
UNICODE_TO_BLISS["U+3c73"] = ["interesting"]
BLISS_TO_UNICODE["burp"] = ["U+3c74"]
UNICODE_TO_BLISS["U+3c74"] = ["burp"]
BLISS_TO_UNICODE["belch"] = ["U+3c74"]
UNICODE_TO_BLISS["U+3c74"].append("belch")
BLISS_TO_UNICODE["burp,belch"] = ["U+3c74"]
UNICODE_TO_BLISS["U+3c74"].append("burp,belch")
BLISS_TO_UNICODE["out of body"] = ["U+3c75"]
UNICODE_TO_BLISS["U+3c75"] = ["out of body"]
BLISS_TO_UNICODE["earn"] = ["U+3c76"]
UNICODE_TO_BLISS["U+3c76"] = ["earn"]
BLISS_TO_UNICODE["icing sugar"].append("U+3838")
UNICODE_TO_BLISS["U+3838"].append("icing sugar")
BLISS_TO_UNICODE["powdered sugar,icing sugar"] = ["U+3838"]
UNICODE_TO_BLISS["U+3838"].append("powdered sugar,icing sugar")
BLISS_TO_UNICODE["sugar"] = ["U+3c77"]
UNICODE_TO_BLISS["U+3c77"] = ["sugar"]
BLISS_TO_UNICODE["viper"] = ["U+3301"]
UNICODE_TO_BLISS["U+3301"].append("viper")
BLISS_TO_UNICODE["boa"] = ["U+3301"]
UNICODE_TO_BLISS["U+3301"].append("boa")
BLISS_TO_UNICODE["circulation"] = ["U+3743"]
UNICODE_TO_BLISS["U+3743"].append("circulation")
BLISS_TO_UNICODE["orbit"].append("U+3743")
UNICODE_TO_BLISS["U+3743"].append("orbit")
BLISS_TO_UNICODE["lap"] = ["U+3743"]
UNICODE_TO_BLISS["U+3743"].append("lap")
BLISS_TO_UNICODE["circle"].append("U+3743")
UNICODE_TO_BLISS["U+3743"].append("circle")
BLISS_TO_UNICODE["round"] = ["U+3743"]
UNICODE_TO_BLISS["U+3743"].append("round")
BLISS_TO_UNICODE["rotation,circulation,orbit,lap,circle,round"] = ["U+3743"]
UNICODE_TO_BLISS["U+3743"].append("rotation,circulation,orbit,lap,circle,round")
BLISS_TO_UNICODE["curved arrow suggesting circular motion"] = ["U+3c78"]
UNICODE_TO_BLISS["U+3c78"] = ["curved arrow suggesting circular motion"]
BLISS_TO_UNICODE["cage"] = ["U+3c79"]
UNICODE_TO_BLISS["U+3c79"] = ["cage"]
BLISS_TO_UNICODE["pictograph of a barred window"] = ["U+3c7a"]
UNICODE_TO_BLISS["U+3c7a"] = ["pictograph of a barred window"]
BLISS_TO_UNICODE["transparent"].append("U+388f")
UNICODE_TO_BLISS["U+388f"].append("transparent")
BLISS_TO_UNICODE["clear,transparent"] = ["U+388f"]
UNICODE_TO_BLISS["U+388f"].append("clear,transparent")
BLISS_TO_UNICODE["bridle"] = ["U+3c7b"]
UNICODE_TO_BLISS["U+3c7b"] = ["bridle"]
BLISS_TO_UNICODE["headstall"] = ["U+3c7b"]
UNICODE_TO_BLISS["U+3c7b"].append("headstall")
BLISS_TO_UNICODE["bridle,headstall"] = ["U+3c7b"]
UNICODE_TO_BLISS["U+3c7b"].append("bridle,headstall")
BLISS_TO_UNICODE["muzzle"] = ["U+3c7c"]
UNICODE_TO_BLISS["U+3c7c"] = ["muzzle"]
BLISS_TO_UNICODE["day centre"] = ["U+3c7d"]
UNICODE_TO_BLISS["U+3c7d"] = ["day centre"]
BLISS_TO_UNICODE["activity centre"] = ["U+3c7e"]
UNICODE_TO_BLISS["U+3c7e"] = ["activity centre"]
BLISS_TO_UNICODE["glasses"] = ["U+3c7f"]
UNICODE_TO_BLISS["U+3c7f"] = ["glasses"]
BLISS_TO_UNICODE["eyeglasses"].append("U+3c7f")
UNICODE_TO_BLISS["U+3c7f"].append("eyeglasses")
BLISS_TO_UNICODE["glasses,eyeglasses"] = ["U+3c7f"]
UNICODE_TO_BLISS["U+3c7f"].append("glasses,eyeglasses")
BLISS_TO_UNICODE["buttocks and genitals"] = ["U+3c80"]
UNICODE_TO_BLISS["U+3c80"] = ["buttocks and genitals"]
BLISS_TO_UNICODE["bump"] = ["U+3c81"]
UNICODE_TO_BLISS["U+3c81"] = ["bump"]
BLISS_TO_UNICODE["press"] = ["U+3c81"]
UNICODE_TO_BLISS["U+3c81"].append("press")
BLISS_TO_UNICODE["pressing"] = ["U+3c81"]
UNICODE_TO_BLISS["U+3c81"].append("pressing")
BLISS_TO_UNICODE["bump,press,pressing"] = ["U+3c81"]
UNICODE_TO_BLISS["U+3c81"].append("bump,press,pressing")
BLISS_TO_UNICODE["bump,press"] = ["U+3c81"]
UNICODE_TO_BLISS["U+3c81"].append("bump,press")
BLISS_TO_UNICODE["skin disease"] = ["U+3c82"]
UNICODE_TO_BLISS["U+3c82"] = ["skin disease"]
BLISS_TO_UNICODE["eczema"] = ["U+3c82"]
UNICODE_TO_BLISS["U+3c82"].append("eczema")
BLISS_TO_UNICODE["skin disease,eczema"] = ["U+3c82"]
UNICODE_TO_BLISS["U+3c82"].append("skin disease,eczema")
BLISS_TO_UNICODE["jigsaw puzzle"] = ["U+3c83"]
UNICODE_TO_BLISS["U+3c83"] = ["jigsaw puzzle"]
BLISS_TO_UNICODE["frequency"] = ["U+3c84"]
UNICODE_TO_BLISS["U+3c84"] = ["frequency"]
BLISS_TO_UNICODE["historic story"] = ["U+3a82"]
UNICODE_TO_BLISS["U+3a82"].append("historic story")
BLISS_TO_UNICODE["watchdog"] = ["U+3c85"]
UNICODE_TO_BLISS["U+3c85"] = ["watchdog"]
BLISS_TO_UNICODE["witness"] = ["U+3c86"]
UNICODE_TO_BLISS["U+3c86"] = ["witness"]
BLISS_TO_UNICODE["henhouse"] = ["U+3c87"]
UNICODE_TO_BLISS["U+3c87"] = ["henhouse"]
BLISS_TO_UNICODE["chicken coop"] = ["U+3c87"]
UNICODE_TO_BLISS["U+3c87"].append("chicken coop")
BLISS_TO_UNICODE["henhouse,chicken coop"] = ["U+3c87"]
UNICODE_TO_BLISS["U+3c87"].append("henhouse,chicken coop")
BLISS_TO_UNICODE["grid"] = ["U+3c88"]
UNICODE_TO_BLISS["U+3c88"] = ["grid"]
BLISS_TO_UNICODE["matrix"] = ["U+3c88"]
UNICODE_TO_BLISS["U+3c88"].append("matrix")
BLISS_TO_UNICODE["grid,matrix"] = ["U+3c88"]
UNICODE_TO_BLISS["U+3c88"].append("grid,matrix")
BLISS_TO_UNICODE["sacking"] = ["U+3c89"]
UNICODE_TO_BLISS["U+3c89"] = ["sacking"]
BLISS_TO_UNICODE["dismissal"].append("U+3c89")
UNICODE_TO_BLISS["U+3c89"].append("dismissal")
BLISS_TO_UNICODE["sacking,dismissal"] = ["U+3c89"]
UNICODE_TO_BLISS["U+3c89"].append("sacking,dismissal")
BLISS_TO_UNICODE["resignation"] = ["U+3c8a"]
UNICODE_TO_BLISS["U+3c8a"] = ["resignation"]
BLISS_TO_UNICODE["force"] = ["U+3c8b"]
UNICODE_TO_BLISS["U+3c8b"] = ["force"]
BLISS_TO_UNICODE["microscope"] = ["U+3c8c"]
UNICODE_TO_BLISS["U+3c8c"] = ["microscope"]
BLISS_TO_UNICODE["to look"] = ["U+3c8d"]
UNICODE_TO_BLISS["U+3c8d"] = ["to look"]
BLISS_TO_UNICODE["voidance"].append("U+3872")
UNICODE_TO_BLISS["U+3872"].append("voidance")
BLISS_TO_UNICODE["evacuation"].append("U+3872")
UNICODE_TO_BLISS["U+3872"].append("evacuation")
BLISS_TO_UNICODE["emptying,voidance,evacuation"] = ["U+3872"]
UNICODE_TO_BLISS["U+3872"].append("emptying,voidance,evacuation")
BLISS_TO_UNICODE["oblong"] = ["U+3394"]
UNICODE_TO_BLISS["U+3394"].append("oblong")
BLISS_TO_UNICODE["rectangle,oblong"] = ["U+3394"]
UNICODE_TO_BLISS["U+3394"].append("rectangle,oblong")
BLISS_TO_UNICODE["rectangular shape"] = ["U+3c8e"]
UNICODE_TO_BLISS["U+3c8e"] = ["rectangular shape"]
BLISS_TO_UNICODE["rectangular"] = ["U+3c8f"]
UNICODE_TO_BLISS["U+3c8f"] = ["rectangular"]
BLISS_TO_UNICODE["oblong"].append("U+3c8f")
UNICODE_TO_BLISS["U+3c8f"].append("oblong")
BLISS_TO_UNICODE["rectangular,oblong"] = ["U+3c8f"]
UNICODE_TO_BLISS["U+3c8f"].append("rectangular,oblong")
BLISS_TO_UNICODE["enclose"] = ["U+39fa"]
UNICODE_TO_BLISS["U+39fa"].append("enclose")
BLISS_TO_UNICODE["shut"] = ["U+39fa"]
UNICODE_TO_BLISS["U+39fa"].append("shut")
BLISS_TO_UNICODE["close,enclose,shut"] = ["U+39fa"]
UNICODE_TO_BLISS["U+39fa"].append("close,enclose,shut")
BLISS_TO_UNICODE["songbird"] = ["U+3c90"]
UNICODE_TO_BLISS["U+3c90"] = ["songbird"]
BLISS_TO_UNICODE["finch"] = ["U+3c90"]
UNICODE_TO_BLISS["U+3c90"].append("finch")
BLISS_TO_UNICODE["thrush"] = ["U+3c90"]
UNICODE_TO_BLISS["U+3c90"].append("thrush")
BLISS_TO_UNICODE["songbird,finch,thrush"] = ["U+3c90"]
UNICODE_TO_BLISS["U+3c90"].append("songbird,finch,thrush")
BLISS_TO_UNICODE["bliss name"] = ["U+3c91"]
UNICODE_TO_BLISS["U+3c91"] = ["bliss name"]
BLISS_TO_UNICODE["bliss-name"] = ["U+3c91"]
UNICODE_TO_BLISS["U+3c91"].append("bliss-name")
BLISS_TO_UNICODE["graze"] = ["U+3c92"]
UNICODE_TO_BLISS["U+3c92"] = ["graze"]
BLISS_TO_UNICODE["eat"] = ["U+3c93"]
UNICODE_TO_BLISS["U+3c93"] = ["eat"]
BLISS_TO_UNICODE["action Indicator"] = ["U+3c94"]
UNICODE_TO_BLISS["U+3c94"] = ["action Indicator"]
BLISS_TO_UNICODE["thrilling"] = ["U+3c95"]
UNICODE_TO_BLISS["U+3c95"] = ["thrilling"]
BLISS_TO_UNICODE["scary"] = ["U+3c95"]
UNICODE_TO_BLISS["U+3c95"].append("scary")
BLISS_TO_UNICODE["thrilling,scary"] = ["U+3c95"]
UNICODE_TO_BLISS["U+3c95"].append("thrilling,scary")
BLISS_TO_UNICODE["fruit cream"] = ["U+3c96"]
UNICODE_TO_BLISS["U+3c96"] = ["fruit cream"]
BLISS_TO_UNICODE["compote"] = ["U+3c96"]
UNICODE_TO_BLISS["U+3c96"].append("compote")
BLISS_TO_UNICODE["fruit cream,compote"] = ["U+3c96"]
UNICODE_TO_BLISS["U+3c96"].append("fruit cream,compote")
BLISS_TO_UNICODE["drop"].append("U+39fd")
UNICODE_TO_BLISS["U+39fd"].append("drop")
BLISS_TO_UNICODE["spill"].append("U+39fd")
UNICODE_TO_BLISS["U+39fd"].append("spill")
BLISS_TO_UNICODE["tumble"] = ["U+39fd"]
UNICODE_TO_BLISS["U+39fd"].append("tumble")
BLISS_TO_UNICODE["fall,drop,spill,tumble"] = ["U+39fd"]
UNICODE_TO_BLISS["U+39fd"].append("fall,drop,spill,tumble")
BLISS_TO_UNICODE["digital memory"] = ["U+3c97"]
UNICODE_TO_BLISS["U+3c97"] = ["digital memory"]
BLISS_TO_UNICODE["digital storage"] = ["U+3c97"]
UNICODE_TO_BLISS["U+3c97"].append("digital storage")
BLISS_TO_UNICODE["digital memory,digital storage"] = ["U+3c97"]
UNICODE_TO_BLISS["U+3c97"].append("digital memory,digital storage")
BLISS_TO_UNICODE["RAM"] = ["U+3c97"]
UNICODE_TO_BLISS["U+3c97"].append("RAM")
BLISS_TO_UNICODE["digital memory,RAM"] = ["U+3c97"]
UNICODE_TO_BLISS["U+3c97"].append("digital memory,RAM")
BLISS_TO_UNICODE["memory"] = ["U+3c98"]
UNICODE_TO_BLISS["U+3c98"] = ["memory"]
BLISS_TO_UNICODE["chilly"] = ["U+3c25"]
UNICODE_TO_BLISS["U+3c25"].append("chilly")
BLISS_TO_UNICODE["cool,chilly"] = ["U+3c25"]
UNICODE_TO_BLISS["U+3c25"].append("cool,chilly")
BLISS_TO_UNICODE["warm"] = ["U+3c99"]
UNICODE_TO_BLISS["U+3c99"] = ["warm"]
BLISS_TO_UNICODE["longness"] = ["U+350d"]
UNICODE_TO_BLISS["U+350d"].append("longness")
BLISS_TO_UNICODE["length,longness"] = ["U+350d"]
UNICODE_TO_BLISS["U+350d"].append("length,longness")
BLISS_TO_UNICODE["horizontal line bounded by two reference lines"] = ["U+3c9a"]
UNICODE_TO_BLISS["U+3c9a"] = ["horizontal line bounded by two reference lines"]
BLISS_TO_UNICODE["peace of mind"] = ["U+3485"]
UNICODE_TO_BLISS["U+3485"].append("peace of mind")
BLISS_TO_UNICODE["serenity"] = ["U+3485"]
UNICODE_TO_BLISS["U+3485"].append("serenity")
BLISS_TO_UNICODE["peace,peace of mind,serenity"] = ["U+3485"]
UNICODE_TO_BLISS["U+3485"].append("peace,peace of mind,serenity")
BLISS_TO_UNICODE["scarf"] = ["U+3c9b"]
UNICODE_TO_BLISS["U+3c9b"] = ["scarf"]
BLISS_TO_UNICODE["neck"] = ["U+3c9c"]
UNICODE_TO_BLISS["U+3c9c"] = ["neck"]
BLISS_TO_UNICODE["advocate"] = ["U+3c9d"]
UNICODE_TO_BLISS["U+3c9d"] = ["advocate"]
BLISS_TO_UNICODE["speaking)"] = ["U+3c9d"]
UNICODE_TO_BLISS["U+3c9d"].append("speaking)")
BLISS_TO_UNICODE["feet and legs"] = ["U+3c9e"]
UNICODE_TO_BLISS["U+3c9e"] = ["feet and legs"]
BLISS_TO_UNICODE["single mother"] = ["U+3c9f"]
UNICODE_TO_BLISS["U+3c9f"] = ["single mother"]
BLISS_TO_UNICODE["spider web"] = ["U+3ca0"]
UNICODE_TO_BLISS["U+3ca0"] = ["spider web"]
BLISS_TO_UNICODE["cobweb"] = ["U+3ca0"]
UNICODE_TO_BLISS["U+3ca0"].append("cobweb")
BLISS_TO_UNICODE["orb web"] = ["U+3ca0"]
UNICODE_TO_BLISS["U+3ca0"].append("orb web")
BLISS_TO_UNICODE["spider web,cobweb,orb web"] = ["U+3ca0"]
UNICODE_TO_BLISS["U+3ca0"].append("spider web,cobweb,orb web")
BLISS_TO_UNICODE["parsnip"] = ["U+3ca1"]
UNICODE_TO_BLISS["U+3ca1"] = ["parsnip"]
BLISS_TO_UNICODE["Iran"] = ["U+3ca2"]
UNICODE_TO_BLISS["U+3ca2"] = ["Iran"]
BLISS_TO_UNICODE["festival"] = ["U+370e"]
UNICODE_TO_BLISS["U+370e"].append("festival")
BLISS_TO_UNICODE["holiday,festival"] = ["U+370e"]
UNICODE_TO_BLISS["U+370e"].append("holiday,festival")
BLISS_TO_UNICODE["party"] = ["U+3ca3"]
UNICODE_TO_BLISS["U+3ca3"] = ["party"]
BLISS_TO_UNICODE["festival"].append("U+3ca3")
UNICODE_TO_BLISS["U+3ca3"].append("festival")
BLISS_TO_UNICODE["party,festival"] = ["U+3ca3"]
UNICODE_TO_BLISS["U+3ca3"].append("party,festival")
BLISS_TO_UNICODE["traveller"] = ["U+3ca4"]
UNICODE_TO_BLISS["U+3ca4"] = ["traveller"]
BLISS_TO_UNICODE["Iraq"] = ["U+3ca5"]
UNICODE_TO_BLISS["U+3ca5"] = ["Iraq"]
BLISS_TO_UNICODE["spaceship"] = ["U+3450"]
UNICODE_TO_BLISS["U+3450"].append("spaceship")
BLISS_TO_UNICODE["rocket,spaceship"] = ["U+3450"]
UNICODE_TO_BLISS["U+3450"].append("rocket,spaceship")
BLISS_TO_UNICODE["projectile"] = ["U+3ca6"]
UNICODE_TO_BLISS["U+3ca6"] = ["projectile"]
BLISS_TO_UNICODE["painful"] = ["U+3ca7"]
UNICODE_TO_BLISS["U+3ca7"] = ["painful"]
BLISS_TO_UNICODE["painfully"] = ["U+3ca7"]
UNICODE_TO_BLISS["U+3ca7"].append("painfully")
BLISS_TO_UNICODE["sore"] = ["U+3ca7"]
UNICODE_TO_BLISS["U+3ca7"].append("sore")
BLISS_TO_UNICODE["painful,painfully,sore"] = ["U+3ca7"]
UNICODE_TO_BLISS["U+3ca7"].append("painful,painfully,sore")
BLISS_TO_UNICODE["abdomen"] = ["U+334b"]
UNICODE_TO_BLISS["U+334b"].append("abdomen")
BLISS_TO_UNICODE["belly"] = ["U+334b"]
UNICODE_TO_BLISS["U+334b"].append("belly")
BLISS_TO_UNICODE["stomach,abdomen,belly"] = ["U+334b"]
UNICODE_TO_BLISS["U+334b"].append("stomach,abdomen,belly")
BLISS_TO_UNICODE["pointer to stomach"] = ["U+3ca8"]
UNICODE_TO_BLISS["U+3ca8"] = ["pointer to stomach"]
BLISS_TO_UNICODE["shorts"] = ["U+3ca9"]
UNICODE_TO_BLISS["U+3ca9"] = ["shorts"]
BLISS_TO_UNICODE["trousers"] = ["U+3caa"]
UNICODE_TO_BLISS["U+3caa"] = ["trousers"]
BLISS_TO_UNICODE["water snake"] = ["U+3cab"]
UNICODE_TO_BLISS["U+3cab"] = ["water snake"]
BLISS_TO_UNICODE["boring"] = ["U+3cac"]
UNICODE_TO_BLISS["U+3cac"] = ["boring"]
BLISS_TO_UNICODE["dull"] = ["U+3cac"]
UNICODE_TO_BLISS["U+3cac"].append("dull")
BLISS_TO_UNICODE["depressing"] = ["U+3cac"]
UNICODE_TO_BLISS["U+3cac"].append("depressing")
BLISS_TO_UNICODE["boring,dull,depressing"] = ["U+3cac"]
UNICODE_TO_BLISS["U+3cac"].append("boring,dull,depressing")
BLISS_TO_UNICODE["monotheism"] = ["U+3cad"]
UNICODE_TO_BLISS["U+3cad"] = ["monotheism"]
BLISS_TO_UNICODE["granddad"] = ["U+340c"]
UNICODE_TO_BLISS["U+340c"].append("granddad")
BLISS_TO_UNICODE["grandpa"] = ["U+340c"]
UNICODE_TO_BLISS["U+340c"].append("grandpa")
BLISS_TO_UNICODE["grandfather,granddad,grandpa"] = ["U+340c"]
UNICODE_TO_BLISS["U+340c"].append("grandfather,granddad,grandpa")
BLISS_TO_UNICODE["steel"] = ["U+3cae"]
UNICODE_TO_BLISS["U+3cae"] = ["steel"]
BLISS_TO_UNICODE["hymn"] = ["U+3caf"]
UNICODE_TO_BLISS["U+3caf"] = ["hymn"]
BLISS_TO_UNICODE["psalm"] = ["U+3caf"]
UNICODE_TO_BLISS["U+3caf"].append("psalm")
BLISS_TO_UNICODE["gospel song"] = ["U+3caf"]
UNICODE_TO_BLISS["U+3caf"].append("gospel song")
BLISS_TO_UNICODE["hymn,psalm,gospel song"] = ["U+3caf"]
UNICODE_TO_BLISS["U+3caf"].append("hymn,psalm,gospel song")
BLISS_TO_UNICODE["reproduction"] = ["U+3cb0"]
UNICODE_TO_BLISS["U+3cb0"] = ["reproduction"]
BLISS_TO_UNICODE["devotion"] = ["U+3cb1"]
UNICODE_TO_BLISS["U+3cb1"] = ["devotion"]
BLISS_TO_UNICODE["important"] = ["U+3cb2"]
UNICODE_TO_BLISS["U+3cb2"] = ["important"]
BLISS_TO_UNICODE["beggar"] = ["U+3cb3"]
UNICODE_TO_BLISS["U+3cb3"] = ["beggar"]
BLISS_TO_UNICODE["ask"] = ["U+3cb4"]
UNICODE_TO_BLISS["U+3cb4"] = ["ask"]
BLISS_TO_UNICODE["very much"] = ["U+3cb5"]
UNICODE_TO_BLISS["U+3cb5"] = ["very much"]
BLISS_TO_UNICODE["very many"] = ["U+3cb5"]
UNICODE_TO_BLISS["U+3cb5"].append("very many")
BLISS_TO_UNICODE["very much,very many"] = ["U+3cb5"]
UNICODE_TO_BLISS["U+3cb5"].append("very much,very many")
BLISS_TO_UNICODE["very"] = ["U+3cb6"]
UNICODE_TO_BLISS["U+3cb6"] = ["very"]
BLISS_TO_UNICODE["row house"] = ["U+3cb7"]
UNICODE_TO_BLISS["U+3cb7"] = ["row house"]
BLISS_TO_UNICODE["attached houses"] = ["U+3cb7"]
UNICODE_TO_BLISS["U+3cb7"].append("attached houses")
BLISS_TO_UNICODE["row house,attached houses"] = ["U+3cb7"]
UNICODE_TO_BLISS["U+3cb7"].append("row house,attached houses")
BLISS_TO_UNICODE["semidetached house"] = ["U+3cb8"]
UNICODE_TO_BLISS["U+3cb8"] = ["semidetached house"]
BLISS_TO_UNICODE["deodorant"] = ["U+3cb9"]
UNICODE_TO_BLISS["U+3cb9"] = ["deodorant"]
BLISS_TO_UNICODE["connector"] = ["U+3cba"]
UNICODE_TO_BLISS["U+3cba"] = ["connector"]
BLISS_TO_UNICODE["interface box"] = ["U+3cba"]
UNICODE_TO_BLISS["U+3cba"].append("interface box")
BLISS_TO_UNICODE["connector,interface box"] = ["U+3cba"]
UNICODE_TO_BLISS["U+3cba"].append("connector,interface box")
BLISS_TO_UNICODE["tonight"] = ["U+3cbb"]
UNICODE_TO_BLISS["U+3cbb"] = ["tonight"]
BLISS_TO_UNICODE["football rule"] = ["U+3cbc"]
UNICODE_TO_BLISS["U+3cbc"] = ["football rule"]
BLISS_TO_UNICODE["football"] = ["U+3cbd"]
UNICODE_TO_BLISS["U+3cbd"] = ["football"]
BLISS_TO_UNICODE["Sleipnir"] = ["U+3cbe"]
UNICODE_TO_BLISS["U+3cbe"] = ["Sleipnir"]
BLISS_TO_UNICODE["bacterium"] = ["U+3cbf"]
UNICODE_TO_BLISS["U+3cbf"] = ["bacterium"]
BLISS_TO_UNICODE["bassoon"] = ["U+3cc0"]
UNICODE_TO_BLISS["U+3cc0"] = ["bassoon"]
BLISS_TO_UNICODE["oboe"] = ["U+3cc1"]
UNICODE_TO_BLISS["U+3cc1"] = ["oboe"]
BLISS_TO_UNICODE["tenor"] = ["U+3cc2"]
UNICODE_TO_BLISS["U+3cc2"] = ["tenor"]
BLISS_TO_UNICODE["cry out"] = ["U+3cc3"]
UNICODE_TO_BLISS["U+3cc3"] = ["cry out"]
BLISS_TO_UNICODE["call"] = ["U+3cc3"]
UNICODE_TO_BLISS["U+3cc3"].append("call")
BLISS_TO_UNICODE["cry out,call"] = ["U+3cc3"]
UNICODE_TO_BLISS["U+3cc3"].append("cry out,call")
BLISS_TO_UNICODE["ruined"] = ["U+3799"]
UNICODE_TO_BLISS["U+3799"].append("ruined")
BLISS_TO_UNICODE["demolished"] = ["U+3799"]
UNICODE_TO_BLISS["U+3799"].append("demolished")
BLISS_TO_UNICODE["deleted"] = ["U+3799"]
UNICODE_TO_BLISS["U+3799"].append("deleted")
BLISS_TO_UNICODE["erased"] = ["U+3799"]
UNICODE_TO_BLISS["U+3799"].append("erased")
BLISS_TO_UNICODE["cancelled"] = ["U+3799"]
UNICODE_TO_BLISS["U+3799"].append("cancelled")
BLISS_TO_UNICODE["destroyed,ruined,demolished,deleted,erased,cancelled"] = ["U+3799"]
UNICODE_TO_BLISS["U+3799"].append("destroyed,ruined,demolished,deleted,erased,cancelled")
BLISS_TO_UNICODE["ashore"] = ["U+3cc4"]
UNICODE_TO_BLISS["U+3cc4"] = ["ashore"]
BLISS_TO_UNICODE["wideness"] = ["U+3cc5"]
UNICODE_TO_BLISS["U+3cc5"] = ["wideness"]
BLISS_TO_UNICODE["broadness"] = ["U+3cc5"]
UNICODE_TO_BLISS["U+3cc5"].append("broadness")
BLISS_TO_UNICODE["wideness,broadness"] = ["U+3cc5"]
UNICODE_TO_BLISS["U+3cc5"].append("wideness,broadness")
BLISS_TO_UNICODE["soap"] = ["U+3cc6"]
UNICODE_TO_BLISS["U+3cc6"] = ["soap"]
BLISS_TO_UNICODE["detergent"] = ["U+3cc6"]
UNICODE_TO_BLISS["U+3cc6"].append("detergent")
BLISS_TO_UNICODE["soap,detergent"] = ["U+3cc6"]
UNICODE_TO_BLISS["U+3cc6"].append("soap,detergent")
BLISS_TO_UNICODE["recumbent bicycle"] = ["U+3cc7"]
UNICODE_TO_BLISS["U+3cc7"] = ["recumbent bicycle"]
BLISS_TO_UNICODE["raindrop"] = ["U+3cc8"]
UNICODE_TO_BLISS["U+3cc8"] = ["raindrop"]
BLISS_TO_UNICODE["cipher"] = ["U+3cc9"]
UNICODE_TO_BLISS["U+3cc9"] = ["cipher"]
BLISS_TO_UNICODE["device"] = ["U+374c"]
UNICODE_TO_BLISS["U+374c"].append("device")
BLISS_TO_UNICODE["support"].append("U+374c")
UNICODE_TO_BLISS["U+374c"].append("support")
BLISS_TO_UNICODE["aid,device,support"] = ["U+374c"]
UNICODE_TO_BLISS["U+374c"].append("aid,device,support")
BLISS_TO_UNICODE["in front of"].append("U+33cf")
UNICODE_TO_BLISS["U+33cf"].append("in front of")
BLISS_TO_UNICODE["prior to"] = ["U+33cf"]
UNICODE_TO_BLISS["U+33cf"].append("prior to")
BLISS_TO_UNICODE["before,in front of,prior to"] = ["U+33cf"]
UNICODE_TO_BLISS["U+33cf"].append("before,in front of,prior to")
BLISS_TO_UNICODE["thanksgiving"] = ["U+3cca"]
UNICODE_TO_BLISS["U+3cca"] = ["thanksgiving"]
BLISS_TO_UNICODE["thanks"] = ["U+3ccb"]
UNICODE_TO_BLISS["U+3ccb"] = ["thanks"]
BLISS_TO_UNICODE["measuring cup"] = ["U+3ccc"]
UNICODE_TO_BLISS["U+3ccc"] = ["measuring cup"]
BLISS_TO_UNICODE["sheep shed"] = ["U+3ccd"]
UNICODE_TO_BLISS["U+3ccd"] = ["sheep shed"]
BLISS_TO_UNICODE["sheep barn"] = ["U+3ccd"]
UNICODE_TO_BLISS["U+3ccd"].append("sheep barn")
BLISS_TO_UNICODE["sheep shed,sheep barn"] = ["U+3ccd"]
UNICODE_TO_BLISS["U+3ccd"].append("sheep shed,sheep barn")
BLISS_TO_UNICODE["atmosphere"] = ["U+348a"]
UNICODE_TO_BLISS["U+348a"].append("atmosphere")
BLISS_TO_UNICODE["air,atmosphere"] = ["U+348a"]
UNICODE_TO_BLISS["U+348a"].append("air,atmosphere")
BLISS_TO_UNICODE["economist"] = ["U+3cce"]
UNICODE_TO_BLISS["U+3cce"] = ["economist"]
BLISS_TO_UNICODE["economics"] = ["U+3ccf"]
UNICODE_TO_BLISS["U+3ccf"] = ["economics"]
BLISS_TO_UNICODE["principal"] = ["U+3cd0"]
UNICODE_TO_BLISS["U+3cd0"] = ["principal"]
BLISS_TO_UNICODE["headteacher"] = ["U+3cd0"]
UNICODE_TO_BLISS["U+3cd0"].append("headteacher")
BLISS_TO_UNICODE["principal,headteacher"] = ["U+3cd0"]
UNICODE_TO_BLISS["U+3cd0"].append("principal,headteacher")
BLISS_TO_UNICODE["tin"] = ["U+3a10"]
UNICODE_TO_BLISS["U+3a10"].append("tin")
BLISS_TO_UNICODE["jar"] = ["U+3a10"]
UNICODE_TO_BLISS["U+3a10"].append("jar")
BLISS_TO_UNICODE["can,tin,jar"] = ["U+3a10"]
UNICODE_TO_BLISS["U+3a10"].append("can,tin,jar")
BLISS_TO_UNICODE["police officer"] = ["U+3cd1"]
UNICODE_TO_BLISS["U+3cd1"] = ["police officer"]
BLISS_TO_UNICODE["policeman"] = ["U+3cd1"]
UNICODE_TO_BLISS["U+3cd1"].append("policeman")
BLISS_TO_UNICODE["policewoman"] = ["U+3cd1"]
UNICODE_TO_BLISS["U+3cd1"].append("policewoman")
BLISS_TO_UNICODE["police officer,policeman,policewoman"] = ["U+3cd1"]
UNICODE_TO_BLISS["U+3cd1"].append("police officer,policeman,policewoman")
BLISS_TO_UNICODE["should"] = ["U+3cd2"]
UNICODE_TO_BLISS["U+3cd2"] = ["should"]
BLISS_TO_UNICODE["would"] = ["U+3cd2"]
UNICODE_TO_BLISS["U+3cd2"].append("would")
BLISS_TO_UNICODE["should,would"] = ["U+3cd2"]
UNICODE_TO_BLISS["U+3cd2"].append("should,would")
BLISS_TO_UNICODE["jam"] = ["U+3cd3"]
UNICODE_TO_BLISS["U+3cd3"] = ["jam"]
BLISS_TO_UNICODE["jelly"] = ["U+3cd3"]
UNICODE_TO_BLISS["U+3cd3"].append("jelly")
BLISS_TO_UNICODE["marmalade"] = ["U+3cd3"]
UNICODE_TO_BLISS["U+3cd3"].append("marmalade")
BLISS_TO_UNICODE["preserves"] = ["U+3cd3"]
UNICODE_TO_BLISS["U+3cd3"].append("preserves")
BLISS_TO_UNICODE["jam,jelly,marmalade,preserves"] = ["U+3cd3"]
UNICODE_TO_BLISS["U+3cd3"].append("jam,jelly,marmalade,preserves")
BLISS_TO_UNICODE["ribbon"] = ["U+3cd4"]
UNICODE_TO_BLISS["U+3cd4"] = ["ribbon"]
BLISS_TO_UNICODE["tape"] = ["U+3cd4"]
UNICODE_TO_BLISS["U+3cd4"].append("tape")
BLISS_TO_UNICODE["ribbon,tape"] = ["U+3cd4"]
UNICODE_TO_BLISS["U+3cd4"].append("ribbon,tape")
BLISS_TO_UNICODE["horseback riding"] = ["U+36c2"]
UNICODE_TO_BLISS["U+36c2"].append("horseback riding")
BLISS_TO_UNICODE["riding,horseback riding"] = ["U+36c2"]
UNICODE_TO_BLISS["U+36c2"].append("riding,horseback riding")
BLISS_TO_UNICODE["hope"] = ["U+3cd5"]
UNICODE_TO_BLISS["U+3cd5"] = ["hope"]
BLISS_TO_UNICODE["transport"].append("U+32f3")
UNICODE_TO_BLISS["U+32f3"].append("transport")
BLISS_TO_UNICODE["carry,move,transport"] = ["U+32f3"]
UNICODE_TO_BLISS["U+32f3"].append("carry,move,transport")
BLISS_TO_UNICODE["transportation"] = ["U+3cd6"]
UNICODE_TO_BLISS["U+3cd6"] = ["transportation"]
BLISS_TO_UNICODE["movement"] = ["U+3cd7"]
UNICODE_TO_BLISS["U+3cd7"] = ["movement"]
BLISS_TO_UNICODE["motion"] = ["U+3cd8"]
UNICODE_TO_BLISS["U+3cd8"] = ["motion"]
BLISS_TO_UNICODE["movement"].append("U+32f3")
UNICODE_TO_BLISS["U+32f3"].append("movement")
BLISS_TO_UNICODE["move,movement"] = ["U+32f3"]
UNICODE_TO_BLISS["U+32f3"].append("move,movement")
BLISS_TO_UNICODE["handle"] = ["U+3cd9"]
UNICODE_TO_BLISS["U+3cd9"] = ["handle"]
BLISS_TO_UNICODE["lucky"] = ["U+3cda"]
UNICODE_TO_BLISS["U+3cda"] = ["lucky"]
BLISS_TO_UNICODE["fortunate"] = ["U+3cda"]
UNICODE_TO_BLISS["U+3cda"].append("fortunate")
BLISS_TO_UNICODE["lucky,fortunate"] = ["U+3cda"]
UNICODE_TO_BLISS["U+3cda"].append("lucky,fortunate")
BLISS_TO_UNICODE["wiggle"] = ["U+3cdb"]
UNICODE_TO_BLISS["U+3cdb"] = ["wiggle"]
BLISS_TO_UNICODE["squirm"] = ["U+3cdb"]
UNICODE_TO_BLISS["U+3cdb"].append("squirm")
BLISS_TO_UNICODE["wiggle,squirm"] = ["U+3cdb"]
UNICODE_TO_BLISS["U+3cdb"].append("wiggle,squirm")
BLISS_TO_UNICODE["string bean"] = ["U+3cdc"]
UNICODE_TO_BLISS["U+3cdc"] = ["string bean"]
BLISS_TO_UNICODE["green bean"] = ["U+3cdc"]
UNICODE_TO_BLISS["U+3cdc"].append("green bean")
BLISS_TO_UNICODE["runner bean"] = ["U+3cdc"]
UNICODE_TO_BLISS["U+3cdc"].append("runner bean")
BLISS_TO_UNICODE["wax bean"] = ["U+3cdc"]
UNICODE_TO_BLISS["U+3cdc"].append("wax bean")
BLISS_TO_UNICODE["string bean,green bean,runner bean,wax bean"] = ["U+3cdc"]
UNICODE_TO_BLISS["U+3cdc"].append("string bean,green bean,runner bean,wax bean")
BLISS_TO_UNICODE["exchanger"] = ["U+3cdd"]
UNICODE_TO_BLISS["U+3cdd"] = ["exchanger"]
BLISS_TO_UNICODE["dance music"] = ["U+3cde"]
UNICODE_TO_BLISS["U+3cde"] = ["dance music"]
BLISS_TO_UNICODE["rein"] = ["U+3cdf"]
UNICODE_TO_BLISS["U+3cdf"] = ["rein"]
BLISS_TO_UNICODE["season of darkness"] = ["U+3ce0"]
UNICODE_TO_BLISS["U+3ce0"] = ["season of darkness"]
BLISS_TO_UNICODE["season"] = ["U+3ce1"]
UNICODE_TO_BLISS["U+3ce1"] = ["season"]
BLISS_TO_UNICODE["darkness"] = ["U+3ce2"]
UNICODE_TO_BLISS["U+3ce2"] = ["darkness"]
BLISS_TO_UNICODE["oven tray"] = ["U+3ce3"]
UNICODE_TO_BLISS["U+3ce3"] = ["oven tray"]
BLISS_TO_UNICODE["pail"] = ["U+3ce4"]
UNICODE_TO_BLISS["U+3ce4"] = ["pail"]
BLISS_TO_UNICODE["bucket"].append("U+3ce4")
UNICODE_TO_BLISS["U+3ce4"].append("bucket")
BLISS_TO_UNICODE["pail,bucket"] = ["U+3ce4"]
UNICODE_TO_BLISS["U+3ce4"].append("pail,bucket")
BLISS_TO_UNICODE["sexual arousal"] = ["U+3ce5"]
UNICODE_TO_BLISS["U+3ce5"] = ["sexual arousal"]
BLISS_TO_UNICODE["sexual excitement"] = ["U+3ce5"]
UNICODE_TO_BLISS["U+3ce5"].append("sexual excitement")
BLISS_TO_UNICODE["sexual arousal,sexual excitement"] = ["U+3ce5"]
UNICODE_TO_BLISS["U+3ce5"].append("sexual arousal,sexual excitement")
BLISS_TO_UNICODE["finger spelling"] = ["U+3ce6"]
UNICODE_TO_BLISS["U+3ce6"] = ["finger spelling"]
BLISS_TO_UNICODE["finger alphabet"] = ["U+3ce6"]
UNICODE_TO_BLISS["U+3ce6"].append("finger alphabet")
BLISS_TO_UNICODE["finger spelling,finger alphabet"] = ["U+3ce6"]
UNICODE_TO_BLISS["U+3ce6"].append("finger spelling,finger alphabet")
BLISS_TO_UNICODE["pencil case"] = ["U+3ce7"]
UNICODE_TO_BLISS["U+3ce7"] = ["pencil case"]
BLISS_TO_UNICODE["pencil box"] = ["U+3ce7"]
UNICODE_TO_BLISS["U+3ce7"].append("pencil box")
BLISS_TO_UNICODE["pencil case,pencil box"] = ["U+3ce7"]
UNICODE_TO_BLISS["U+3ce7"].append("pencil case,pencil box")
BLISS_TO_UNICODE["handgun"] = ["U+3ce8"]
UNICODE_TO_BLISS["U+3ce8"] = ["handgun"]
BLISS_TO_UNICODE["pistol"] = ["U+3ce8"]
UNICODE_TO_BLISS["U+3ce8"].append("pistol")
BLISS_TO_UNICODE["handgun,pistol"] = ["U+3ce8"]
UNICODE_TO_BLISS["U+3ce8"].append("handgun,pistol")
BLISS_TO_UNICODE["e mail"] = ["U+3ce9"]
UNICODE_TO_BLISS["U+3ce9"] = ["e mail"]
BLISS_TO_UNICODE["email"] = ["U+3ce9"]
UNICODE_TO_BLISS["U+3ce9"].append("email")
BLISS_TO_UNICODE["e-mail,email"] = ["U+3ce9"]
UNICODE_TO_BLISS["U+3ce9"].append("e-mail,email")
BLISS_TO_UNICODE["toy shop"] = ["U+3ceb"]
UNICODE_TO_BLISS["U+3ceb"] = ["toy shop"]
BLISS_TO_UNICODE["geothermal energy"] = ["U+3cec"]
UNICODE_TO_BLISS["U+3cec"] = ["geothermal energy"]
BLISS_TO_UNICODE["drum"] = ["U+3ced"]
UNICODE_TO_BLISS["U+3ced"] = ["drum"]
BLISS_TO_UNICODE["ramp"] = ["U+3cee"]
UNICODE_TO_BLISS["U+3cee"] = ["ramp"]
BLISS_TO_UNICODE["mind altering drug"] = ["U+397c"]
UNICODE_TO_BLISS["U+397c"].append("mind altering drug")
BLISS_TO_UNICODE["drug,mind-altering drug"] = ["U+397c"]
UNICODE_TO_BLISS["U+397c"].append("drug,mind-altering drug")
BLISS_TO_UNICODE["doorway"] = ["U+3cef"]
UNICODE_TO_BLISS["U+3cef"] = ["doorway"]
BLISS_TO_UNICODE["gate"] = ["U+3cef"]
UNICODE_TO_BLISS["U+3cef"].append("gate")
BLISS_TO_UNICODE["doorway,gate"] = ["U+3cef"]
UNICODE_TO_BLISS["U+3cef"].append("doorway,gate")
BLISS_TO_UNICODE["Jesus"] = ["U+3cf0"]
UNICODE_TO_BLISS["U+3cf0"] = ["Jesus"]
BLISS_TO_UNICODE["Jesus Christ"] = ["U+3cf0"]
UNICODE_TO_BLISS["U+3cf0"].append("Jesus Christ")
BLISS_TO_UNICODE["Christ"].append("U+3cf0")
UNICODE_TO_BLISS["U+3cf0"].append("Christ")
BLISS_TO_UNICODE["semi detached house"] = ["U+3cf1"]
UNICODE_TO_BLISS["U+3cf1"] = ["semi detached house"]
BLISS_TO_UNICODE["semi-detached house"] = ["U+3cf1"]
UNICODE_TO_BLISS["U+3cf1"].append("semi-detached house")
BLISS_TO_UNICODE["spear"] = ["U+3b98"]
UNICODE_TO_BLISS["U+3b98"].append("spear")
BLISS_TO_UNICODE["javelin,spear"] = ["U+3b98"]
UNICODE_TO_BLISS["U+3b98"].append("javelin,spear")
BLISS_TO_UNICODE["letter carrier"] = ["U+3cf2"]
UNICODE_TO_BLISS["U+3cf2"] = ["letter carrier"]
BLISS_TO_UNICODE["postman"] = ["U+3cf2"]
UNICODE_TO_BLISS["U+3cf2"].append("postman")
BLISS_TO_UNICODE["mailman"] = ["U+3cf2"]
UNICODE_TO_BLISS["U+3cf2"].append("mailman")
BLISS_TO_UNICODE["letter carrier,postman,mailman"] = ["U+3cf2"]
UNICODE_TO_BLISS["U+3cf2"].append("letter carrier,postman,mailman")
BLISS_TO_UNICODE["backward and forward"] = ["U+323b"]
UNICODE_TO_BLISS["U+323b"].append("backward and forward")
BLISS_TO_UNICODE["to and fro"] = ["U+323b"]
UNICODE_TO_BLISS["U+323b"].append("to and fro")
BLISS_TO_UNICODE["back and forth,backward and forward,to and fro"] = ["U+323b"]
UNICODE_TO_BLISS["U+323b"].append("back and forth,backward and forward,to and fro")
BLISS_TO_UNICODE["feather"] = ["U+3cf3"]
UNICODE_TO_BLISS["U+3cf3"] = ["feather"]
BLISS_TO_UNICODE["homosexual"] = ["U+3cf4"]
UNICODE_TO_BLISS["U+3cf4"] = ["homosexual"]
BLISS_TO_UNICODE["lesbian"] = ["U+3cf4"]
UNICODE_TO_BLISS["U+3cf4"].append("lesbian")
BLISS_TO_UNICODE["gay"] = ["U+3cf4"]
UNICODE_TO_BLISS["U+3cf4"].append("gay")
BLISS_TO_UNICODE["New Testament"] = ["U+3cf5"]
UNICODE_TO_BLISS["U+3cf5"] = ["New Testament"]
BLISS_TO_UNICODE["neighbour"] = ["U+3cf6"]
UNICODE_TO_BLISS["U+3cf6"] = ["neighbour"]
BLISS_TO_UNICODE["Epiphany"] = ["U+3cf7"]
UNICODE_TO_BLISS["U+3cf7"] = ["Epiphany"]
BLISS_TO_UNICODE["planner"] = ["U+398e"]
UNICODE_TO_BLISS["U+398e"].append("planner")
BLISS_TO_UNICODE["designer,planner"] = ["U+398e"]
UNICODE_TO_BLISS["U+398e"].append("designer,planner")
BLISS_TO_UNICODE["runway"] = ["U+3cf8"]
UNICODE_TO_BLISS["U+3cf8"] = ["runway"]
BLISS_TO_UNICODE["ascending and descending"] = ["U+3cf9"]
UNICODE_TO_BLISS["U+3cf9"] = ["ascending and descending"]
BLISS_TO_UNICODE["intranet"] = ["U+3cfa"]
UNICODE_TO_BLISS["U+3cfa"] = ["intranet"]
BLISS_TO_UNICODE["digital space"] = ["U+3cfb"]
UNICODE_TO_BLISS["U+3cfb"] = ["digital space"]
BLISS_TO_UNICODE["bathtub"] = ["U+3cfc"]
UNICODE_TO_BLISS["U+3cfc"] = ["bathtub"]
BLISS_TO_UNICODE["bath"].append("U+3cfc")
UNICODE_TO_BLISS["U+3cfc"].append("bath")
BLISS_TO_UNICODE["tub"] = ["U+3cfc"]
UNICODE_TO_BLISS["U+3cfc"].append("tub")
BLISS_TO_UNICODE["bathtub,bath,tub"] = ["U+3cfc"]
UNICODE_TO_BLISS["U+3cfc"].append("bathtub,bath,tub")
BLISS_TO_UNICODE["sink"] = ["U+3cfd"]
UNICODE_TO_BLISS["U+3cfd"] = ["sink"]
BLISS_TO_UNICODE["lust"] = ["U+3cfe"]
UNICODE_TO_BLISS["U+3cfe"] = ["lust"]
BLISS_TO_UNICODE["sex drive"] = ["U+3cff"]
UNICODE_TO_BLISS["U+3cff"] = ["sex drive"]
BLISS_TO_UNICODE["sexual urge"] = ["U+3d00"]
UNICODE_TO_BLISS["U+3d00"] = ["sexual urge"]
BLISS_TO_UNICODE["libido"] = ["U+3d01"]
UNICODE_TO_BLISS["U+3d01"] = ["libido"]
BLISS_TO_UNICODE["birth control"] = ["U+3d02"]
UNICODE_TO_BLISS["U+3d02"] = ["birth control"]
BLISS_TO_UNICODE["mountain biking"] = ["U+3d03"]
UNICODE_TO_BLISS["U+3d03"] = ["mountain biking"]
BLISS_TO_UNICODE["mountain bike"] = ["U+3d04"]
UNICODE_TO_BLISS["U+3d04"] = ["mountain bike"]
BLISS_TO_UNICODE["overspend"] = ["U+3d05"]
UNICODE_TO_BLISS["U+3d05"] = ["overspend"]
BLISS_TO_UNICODE["buy over budget"] = ["U+3d05"]
UNICODE_TO_BLISS["U+3d05"].append("buy over budget")
BLISS_TO_UNICODE["overspend,buy over budget"] = ["U+3d05"]
UNICODE_TO_BLISS["U+3d05"].append("overspend,buy over budget")
BLISS_TO_UNICODE["money on a regular basis"] = ["U+3d06"]
UNICODE_TO_BLISS["U+3d06"] = ["money on a regular basis"]
BLISS_TO_UNICODE["often"] = ["U+3d07"]
UNICODE_TO_BLISS["U+3d07"] = ["often"]
BLISS_TO_UNICODE["cremation"] = ["U+3d08"]
UNICODE_TO_BLISS["U+3d08"] = ["cremation"]
BLISS_TO_UNICODE["terrorist"] = ["U+3d09"]
UNICODE_TO_BLISS["U+3d09"] = ["terrorist"]
BLISS_TO_UNICODE["terrorism"] = ["U+3d0a"]
UNICODE_TO_BLISS["U+3d0a"] = ["terrorism"]
BLISS_TO_UNICODE["production"].append("U+3918")
UNICODE_TO_BLISS["U+3918"].append("production")
BLISS_TO_UNICODE["fashioning"].append("U+3918")
UNICODE_TO_BLISS["U+3918"].append("fashioning")
BLISS_TO_UNICODE["making,production,fashioning"] = ["U+3918"]
UNICODE_TO_BLISS["U+3918"].append("making,production,fashioning")
BLISS_TO_UNICODE["woman doll"] = ["U+3d0b"]
UNICODE_TO_BLISS["U+3d0b"] = ["woman doll"]
BLISS_TO_UNICODE["excavation"].append("U+36ea")
UNICODE_TO_BLISS["U+36ea"].append("excavation")
BLISS_TO_UNICODE["digging,excavation"] = ["U+36ea"]
UNICODE_TO_BLISS["U+36ea"].append("digging,excavation")
BLISS_TO_UNICODE["terror"] = ["U+3d0c"]
UNICODE_TO_BLISS["U+3d0c"] = ["terror"]
BLISS_TO_UNICODE["panic"] = ["U+3d0d"]
UNICODE_TO_BLISS["U+3d0d"] = ["panic"]
BLISS_TO_UNICODE["nervous system"] = ["U+3d0e"]
UNICODE_TO_BLISS["U+3d0e"] = ["nervous system"]
BLISS_TO_UNICODE["neuron"] = ["U+3d0f"]
UNICODE_TO_BLISS["U+3d0f"] = ["neuron"]
BLISS_TO_UNICODE["eternity"] = ["U+3d10"]
UNICODE_TO_BLISS["U+3d10"] = ["eternity"]
BLISS_TO_UNICODE["infinity"] = ["U+3d10"]
UNICODE_TO_BLISS["U+3d10"].append("infinity")
BLISS_TO_UNICODE["eternity,infinity"] = ["U+3d10"]
UNICODE_TO_BLISS["U+3d10"].append("eternity,infinity")
BLISS_TO_UNICODE["swordfish"] = ["U+3d11"]
UNICODE_TO_BLISS["U+3d11"] = ["swordfish"]
BLISS_TO_UNICODE["sword"] = ["U+3d12"]
UNICODE_TO_BLISS["U+3d12"] = ["sword"]
BLISS_TO_UNICODE["broccoli"] = ["U+3d13"]
UNICODE_TO_BLISS["U+3d13"] = ["broccoli"]
BLISS_TO_UNICODE["green"] = ["U+3d14"]
UNICODE_TO_BLISS["U+3d14"] = ["green"]
BLISS_TO_UNICODE["audition"] = ["U+3ab7"]
UNICODE_TO_BLISS["U+3ab7"].append("audition")
BLISS_TO_UNICODE["auditory sense"] = ["U+3ab7"]
UNICODE_TO_BLISS["U+3ab7"].append("auditory sense")
BLISS_TO_UNICODE["hearing,audition,auditory sense"] = ["U+3ab7"]
UNICODE_TO_BLISS["U+3ab7"].append("hearing,audition,auditory sense")
BLISS_TO_UNICODE["be cold"] = ["U+3d15"]
UNICODE_TO_BLISS["U+3d15"] = ["be cold"]
BLISS_TO_UNICODE["to feel"] = ["U+3d16"]
UNICODE_TO_BLISS["U+3d16"] = ["to feel"]
BLISS_TO_UNICODE["rifle"] = ["U+3d17"]
UNICODE_TO_BLISS["U+3d17"] = ["rifle"]
BLISS_TO_UNICODE["shotgun"] = ["U+3d17"]
UNICODE_TO_BLISS["U+3d17"].append("shotgun")
BLISS_TO_UNICODE["rifle,shotgun"] = ["U+3d17"]
UNICODE_TO_BLISS["U+3d17"].append("rifle,shotgun")
BLISS_TO_UNICODE["order"] = ["U+3557"]
UNICODE_TO_BLISS["U+3557"].append("order")
BLISS_TO_UNICODE["command,order"] = ["U+3557"]
UNICODE_TO_BLISS["U+3557"].append("command,order")
BLISS_TO_UNICODE["glue"] = ["U+3d18"]
UNICODE_TO_BLISS["U+3d18"] = ["glue"]
BLISS_TO_UNICODE["adhesive"] = ["U+3d18"]
UNICODE_TO_BLISS["U+3d18"].append("adhesive")
BLISS_TO_UNICODE["paste"] = ["U+3d18"]
UNICODE_TO_BLISS["U+3d18"].append("paste")
BLISS_TO_UNICODE["glue,adhesive,paste"] = ["U+3d18"]
UNICODE_TO_BLISS["U+3d18"].append("glue,adhesive,paste")
BLISS_TO_UNICODE["stick"] = ["U+3d18"]
UNICODE_TO_BLISS["U+3d18"].append("stick")
BLISS_TO_UNICODE["glue,paste,stick"] = ["U+3d18"]
UNICODE_TO_BLISS["U+3d18"].append("glue,paste,stick")
BLISS_TO_UNICODE["bread surface"] = ["U+3d19"]
UNICODE_TO_BLISS["U+3d19"] = ["bread surface"]
BLISS_TO_UNICODE["noisemaker"] = ["U+3d1a"]
UNICODE_TO_BLISS["U+3d1a"] = ["noisemaker"]
BLISS_TO_UNICODE["musical toy"] = ["U+3d1a"]
UNICODE_TO_BLISS["U+3d1a"].append("musical toy")
BLISS_TO_UNICODE["noisemaker,musical toy"] = ["U+3d1a"]
UNICODE_TO_BLISS["U+3d1a"].append("noisemaker,musical toy")
BLISS_TO_UNICODE["arrest"] = ["U+3d1b"]
UNICODE_TO_BLISS["U+3d1b"] = ["arrest"]
BLISS_TO_UNICODE["cookie jar"] = ["U+3d1c"]
UNICODE_TO_BLISS["U+3d1c"] = ["cookie jar"]
BLISS_TO_UNICODE["biscuit tin"] = ["U+3d1c"]
UNICODE_TO_BLISS["U+3d1c"].append("biscuit tin")
BLISS_TO_UNICODE["cookie jar,biscuit tin"] = ["U+3d1c"]
UNICODE_TO_BLISS["U+3d1c"].append("cookie jar,biscuit tin")
BLISS_TO_UNICODE["cookie/biscuit"] = ["U+3d1d"]
UNICODE_TO_BLISS["U+3d1d"] = ["cookie/biscuit"]
BLISS_TO_UNICODE["gap"] = ["U+34c8"]
UNICODE_TO_BLISS["U+34c8"].append("gap")
BLISS_TO_UNICODE["cleft"] = ["U+34c8"]
UNICODE_TO_BLISS["U+34c8"].append("cleft")
BLISS_TO_UNICODE["crack,gap,cleft"] = ["U+34c8"]
UNICODE_TO_BLISS["U+34c8"].append("crack,gap,cleft")
BLISS_TO_UNICODE["scoundrel"] = ["U+3d1e"]
UNICODE_TO_BLISS["U+3d1e"] = ["scoundrel"]
BLISS_TO_UNICODE["villain"] = ["U+3d1e"]
UNICODE_TO_BLISS["U+3d1e"].append("villain")
BLISS_TO_UNICODE["scoundrel,villain"] = ["U+3d1e"]
UNICODE_TO_BLISS["U+3d1e"].append("scoundrel,villain")
BLISS_TO_UNICODE["pill box"] = ["U+3d1f"]
UNICODE_TO_BLISS["U+3d1f"] = ["pill box"]
BLISS_TO_UNICODE["pill"] = ["U+3d20"]
UNICODE_TO_BLISS["U+3d20"] = ["pill"]
BLISS_TO_UNICODE["tablet"] = ["U+3d21"]
UNICODE_TO_BLISS["U+3d21"] = ["tablet"]
BLISS_TO_UNICODE["government"] = ["U+3d22"]
UNICODE_TO_BLISS["U+3d22"] = ["government"]
BLISS_TO_UNICODE["board of directors"] = ["U+3d23"]
UNICODE_TO_BLISS["U+3d23"] = ["board of directors"]
BLISS_TO_UNICODE["executive"] = ["U+3d24"]
UNICODE_TO_BLISS["U+3d24"] = ["executive"]
BLISS_TO_UNICODE["hiding place"] = ["U+3d25"]
UNICODE_TO_BLISS["U+3d25"] = ["hiding place"]
BLISS_TO_UNICODE["cache"] = ["U+3d25"]
UNICODE_TO_BLISS["U+3d25"].append("cache")
BLISS_TO_UNICODE["hiding place,cache"] = ["U+3d25"]
UNICODE_TO_BLISS["U+3d25"].append("hiding place,cache")
BLISS_TO_UNICODE["bacterial infection"] = ["U+3d26"]
UNICODE_TO_BLISS["U+3d26"] = ["bacterial infection"]
BLISS_TO_UNICODE["5"].append("U+3565")
UNICODE_TO_BLISS["U+3565"].append("5")
BLISS_TO_UNICODE["Arabic numeral 5"] = ["U+3d27"]
UNICODE_TO_BLISS["U+3d27"] = ["Arabic numeral 5"]
BLISS_TO_UNICODE["Arabic numeral 5 small"] = ["U+3d28"]
UNICODE_TO_BLISS["U+3d28"] = ["Arabic numeral 5 small"]
BLISS_TO_UNICODE["placenta"] = ["U+3d29"]
UNICODE_TO_BLISS["U+3d29"] = ["placenta"]
BLISS_TO_UNICODE["you are welcome"] = ["U+3d2a"]
UNICODE_TO_BLISS["U+3d2a"] = ["you are welcome"]
BLISS_TO_UNICODE["you're welcome"] = ["U+3d2a"]
UNICODE_TO_BLISS["U+3d2a"].append("you're welcome")
BLISS_TO_UNICODE["you are welcome,you're welcome"] = ["U+3d2a"]
UNICODE_TO_BLISS["U+3d2a"].append("you are welcome,you're welcome")
BLISS_TO_UNICODE["to help"] = ["U+3d2b"]
UNICODE_TO_BLISS["U+3d2b"] = ["to help"]
BLISS_TO_UNICODE["potato chip"] = ["U+3d2c"]
UNICODE_TO_BLISS["U+3d2c"] = ["potato chip"]
BLISS_TO_UNICODE["chip"] = ["U+3d2c"]
UNICODE_TO_BLISS["U+3d2c"].append("chip")
BLISS_TO_UNICODE["crisp"] = ["U+3d2c"]
UNICODE_TO_BLISS["U+3d2c"].append("crisp")
BLISS_TO_UNICODE["vegetable"].append("U+34a6")
UNICODE_TO_BLISS["U+34a6"].append("vegetable")
BLISS_TO_UNICODE["onion,vegetable"] = ["U+34a6"]
UNICODE_TO_BLISS["U+34a6"].append("onion,vegetable")
BLISS_TO_UNICODE["dove"] = ["U+3d2d"]
UNICODE_TO_BLISS["U+3d2d"] = ["dove"]
BLISS_TO_UNICODE["become"] = ["U+3d2e"]
UNICODE_TO_BLISS["U+3d2e"] = ["become"]
BLISS_TO_UNICODE["thief"] = ["U+3d2f"]
UNICODE_TO_BLISS["U+3d2f"] = ["thief"]
BLISS_TO_UNICODE["electric current"] = ["U+3d30"]
UNICODE_TO_BLISS["U+3d30"] = ["electric current"]
BLISS_TO_UNICODE["gymnastics"] = ["U+3d31"]
UNICODE_TO_BLISS["U+3d31"] = ["gymnastics"]
BLISS_TO_UNICODE["ballot"] = ["U+3d32"]
UNICODE_TO_BLISS["U+3d32"] = ["ballot"]
BLISS_TO_UNICODE["voting slip"] = ["U+3d32"]
UNICODE_TO_BLISS["U+3d32"].append("voting slip")
BLISS_TO_UNICODE["ballot,voting slip"] = ["U+3d32"]
UNICODE_TO_BLISS["U+3d32"].append("ballot,voting slip")
BLISS_TO_UNICODE["transportation"].append("U+337f")
UNICODE_TO_BLISS["U+337f"].append("transportation")
BLISS_TO_UNICODE["transport,transportation"] = ["U+337f"]
UNICODE_TO_BLISS["U+337f"].append("transport,transportation")
BLISS_TO_UNICODE["CNS"] = ["U+35d2"]
UNICODE_TO_BLISS["U+35d2"].append("CNS")
BLISS_TO_UNICODE["central nervous system,CNS"] = ["U+35d2"]
UNICODE_TO_BLISS["U+35d2"].append("central nervous system,CNS")
BLISS_TO_UNICODE["brain signal"] = ["U+3d33"]
UNICODE_TO_BLISS["U+3d33"] = ["brain signal"]
BLISS_TO_UNICODE["contusion"] = ["U+3a3b"]
UNICODE_TO_BLISS["U+3a3b"].append("contusion")
BLISS_TO_UNICODE["haematoma"] = ["U+3a3b"]
UNICODE_TO_BLISS["U+3a3b"].append("haematoma")
BLISS_TO_UNICODE["bruise,contusion,haematoma"] = ["U+3a3b"]
UNICODE_TO_BLISS["U+3a3b"].append("bruise,contusion,haematoma")
BLISS_TO_UNICODE["blue"] = ["U+3d34"]
UNICODE_TO_BLISS["U+3d34"] = ["blue"]
BLISS_TO_UNICODE["public transport"] = ["U+3d35"]
UNICODE_TO_BLISS["U+3d35"] = ["public transport"]
BLISS_TO_UNICODE["history"] = ["U+3d36"]
UNICODE_TO_BLISS["U+3d36"] = ["history"]
BLISS_TO_UNICODE["saucepan"] = ["U+3d37"]
UNICODE_TO_BLISS["U+3d37"] = ["saucepan"]
BLISS_TO_UNICODE["forgiven"] = ["U+3d38"]
UNICODE_TO_BLISS["U+3d38"] = ["forgiven"]
BLISS_TO_UNICODE["biology"] = ["U+3d39"]
UNICODE_TO_BLISS["U+3d39"] = ["biology"]
BLISS_TO_UNICODE["combination of chemical product and life"] = ["U+3d3a"]
UNICODE_TO_BLISS["U+3d3a"] = ["combination of chemical product and life"]
BLISS_TO_UNICODE["schedule"] = ["U+3d3b"]
UNICODE_TO_BLISS["U+3d3b"] = ["schedule"]
BLISS_TO_UNICODE["timetable"] = ["U+3d3b"]
UNICODE_TO_BLISS["U+3d3b"].append("timetable")
BLISS_TO_UNICODE["schedule,timetable"] = ["U+3d3b"]
UNICODE_TO_BLISS["U+3d3b"].append("schedule,timetable")
BLISS_TO_UNICODE["pressure"] = ["U+3d3c"]
UNICODE_TO_BLISS["U+3d3c"] = ["pressure"]
BLISS_TO_UNICODE["Yahrzeit"] = ["U+3d3d"]
UNICODE_TO_BLISS["U+3d3d"] = ["Yahrzeit"]
BLISS_TO_UNICODE["anniversary"] = ["U+3d3e"]
UNICODE_TO_BLISS["U+3d3e"] = ["anniversary"]
BLISS_TO_UNICODE["stage"] = ["U+374f"]
UNICODE_TO_BLISS["U+374f"].append("stage")
BLISS_TO_UNICODE["platform,stage"] = ["U+374f"]
UNICODE_TO_BLISS["U+374f"].append("platform,stage")
BLISS_TO_UNICODE["iris"] = ["U+3d3f"]
UNICODE_TO_BLISS["U+3d3f"] = ["iris"]
BLISS_TO_UNICODE["sister"] = ["U+3d40"]
UNICODE_TO_BLISS["U+3d40"] = ["sister"]
BLISS_TO_UNICODE["conductor"] = ["U+3d41"]
UNICODE_TO_BLISS["U+3d41"] = ["conductor"]
BLISS_TO_UNICODE["therapist)"] = ["U+3d41"]
UNICODE_TO_BLISS["U+3d41"].append("therapist)")
BLISS_TO_UNICODE["conductive education"] = ["U+3d42"]
UNICODE_TO_BLISS["U+3d42"] = ["conductive education"]
BLISS_TO_UNICODE["software"] = ["U+3d43"]
UNICODE_TO_BLISS["U+3d43"] = ["software"]
BLISS_TO_UNICODE["computer program"].append("U+3d43")
UNICODE_TO_BLISS["U+3d43"].append("computer program")
BLISS_TO_UNICODE["application"] = ["U+3d43"]
UNICODE_TO_BLISS["U+3d43"].append("application")
BLISS_TO_UNICODE["app"] = ["U+3d43"]
UNICODE_TO_BLISS["U+3d43"].append("app")
BLISS_TO_UNICODE["software,computer program,application,app"] = ["U+3d43"]
UNICODE_TO_BLISS["U+3d43"].append("software,computer program,application,app")
BLISS_TO_UNICODE["Virgo"] = ["U+3d44"]
UNICODE_TO_BLISS["U+3d44"] = ["Virgo"]
BLISS_TO_UNICODE["lung"] = ["U+3d45"]
UNICODE_TO_BLISS["U+3d45"] = ["lung"]
BLISS_TO_UNICODE["body brush"] = ["U+3a43"]
UNICODE_TO_BLISS["U+3a43"].append("body brush")
BLISS_TO_UNICODE["horse brush,body brush"] = ["U+3a43"]
UNICODE_TO_BLISS["U+3a43"].append("horse brush,body brush")
BLISS_TO_UNICODE["many"].append("U+343e")
UNICODE_TO_BLISS["U+343e"].append("many")
BLISS_TO_UNICODE["very"].append("U+343e")
UNICODE_TO_BLISS["U+343e"].append("very")
BLISS_TO_UNICODE["much,many,very"] = ["U+343e"]
UNICODE_TO_BLISS["U+343e"].append("much,many,very")
BLISS_TO_UNICODE["frustration"] = ["U+3d46"]
UNICODE_TO_BLISS["U+3d46"] = ["frustration"]
BLISS_TO_UNICODE["catamaran"] = ["U+3d47"]
UNICODE_TO_BLISS["U+3d47"] = ["catamaran"]
BLISS_TO_UNICODE["pontoon boat"] = ["U+3d47"]
UNICODE_TO_BLISS["U+3d47"].append("pontoon boat")
BLISS_TO_UNICODE["catamaran,pontoon boat"] = ["U+3d47"]
UNICODE_TO_BLISS["U+3d47"].append("catamaran,pontoon boat")
BLISS_TO_UNICODE["hull"] = ["U+3d48"]
UNICODE_TO_BLISS["U+3d48"] = ["hull"]
BLISS_TO_UNICODE["circulatory system"] = ["U+3d49"]
UNICODE_TO_BLISS["U+3d49"] = ["circulatory system"]
BLISS_TO_UNICODE["function"] = ["U+3d4a"]
UNICODE_TO_BLISS["U+3d4a"] = ["function"]
BLISS_TO_UNICODE["funnel"] = ["U+3d4b"]
UNICODE_TO_BLISS["U+3d4b"] = ["funnel"]
BLISS_TO_UNICODE["be named"] = ["U+3d4c"]
UNICODE_TO_BLISS["U+3d4c"] = ["be named"]
BLISS_TO_UNICODE["be called"] = ["U+3d4c"]
UNICODE_TO_BLISS["U+3d4c"].append("be called")
BLISS_TO_UNICODE["be named,be called"] = ["U+3d4c"]
UNICODE_TO_BLISS["U+3d4c"].append("be named,be called")
BLISS_TO_UNICODE["construction"] = ["U+33c6"]
UNICODE_TO_BLISS["U+33c6"].append("construction")
BLISS_TO_UNICODE["structure,construction"] = ["U+33c6"]
UNICODE_TO_BLISS["U+33c6"].append("structure,construction")
BLISS_TO_UNICODE["enclosure formed of lines and dots"] = ["U+3d4d"]
UNICODE_TO_BLISS["U+3d4d"] = ["enclosure formed of lines and dots"]
BLISS_TO_UNICODE["rectum"] = ["U+3d4e"]
UNICODE_TO_BLISS["U+3d4e"] = ["rectum"]
BLISS_TO_UNICODE["count"] = ["U+3d4f"]
UNICODE_TO_BLISS["U+3d4f"] = ["count"]
BLISS_TO_UNICODE["community centre"] = ["U+3d50"]
UNICODE_TO_BLISS["U+3d50"] = ["community centre"]
BLISS_TO_UNICODE["town hall"] = ["U+3d50"]
UNICODE_TO_BLISS["U+3d50"].append("town hall")
BLISS_TO_UNICODE["village hall"] = ["U+3d50"]
UNICODE_TO_BLISS["U+3d50"].append("village hall")
BLISS_TO_UNICODE["community centre,town hall,village hall"] = ["U+3d50"]
UNICODE_TO_BLISS["U+3d50"].append("community centre,town hall,village hall")
BLISS_TO_UNICODE["smooth"] = ["U+3d51"]
UNICODE_TO_BLISS["U+3d51"] = ["smooth"]
BLISS_TO_UNICODE["persuade"] = ["U+3d52"]
UNICODE_TO_BLISS["U+3d52"] = ["persuade"]
BLISS_TO_UNICODE["convince"] = ["U+3d52"]
UNICODE_TO_BLISS["U+3d52"].append("convince")
BLISS_TO_UNICODE["persuade,convince"] = ["U+3d52"]
UNICODE_TO_BLISS["U+3d52"].append("persuade,convince")
BLISS_TO_UNICODE["persuasion"] = ["U+3d53"]
UNICODE_TO_BLISS["U+3d53"] = ["persuasion"]
BLISS_TO_UNICODE["monument"] = ["U+3d54"]
UNICODE_TO_BLISS["U+3d54"] = ["monument"]
BLISS_TO_UNICODE["commemorative work"] = ["U+3d54"]
UNICODE_TO_BLISS["U+3d54"].append("commemorative work")
BLISS_TO_UNICODE["monument,commemorative work"] = ["U+3d54"]
UNICODE_TO_BLISS["U+3d54"].append("monument,commemorative work")
BLISS_TO_UNICODE["problem"] = ["U+3d55"]
UNICODE_TO_BLISS["U+3d55"] = ["problem"]
BLISS_TO_UNICODE["make believe woman"] = ["U+3d56"]
UNICODE_TO_BLISS["U+3d56"] = ["make believe woman"]
BLISS_TO_UNICODE["make-believe woman"] = ["U+3d56"]
UNICODE_TO_BLISS["U+3d56"].append("make-believe woman")
BLISS_TO_UNICODE["menstruation"] = ["U+3d57"]
UNICODE_TO_BLISS["U+3d57"] = ["menstruation"]
BLISS_TO_UNICODE["menstrual period"] = ["U+3d57"]
UNICODE_TO_BLISS["U+3d57"].append("menstrual period")
BLISS_TO_UNICODE["period"].append("U+3d57")
UNICODE_TO_BLISS["U+3d57"].append("period")
BLISS_TO_UNICODE["menstruation,menstrual period,period"] = ["U+3d57"]
UNICODE_TO_BLISS["U+3d57"].append("menstruation,menstrual period,period")
BLISS_TO_UNICODE["dissemination"].append("U+39c5")
UNICODE_TO_BLISS["U+39c5"].append("dissemination")
BLISS_TO_UNICODE["scattering"].append("U+39c5")
UNICODE_TO_BLISS["U+39c5"].append("scattering")
BLISS_TO_UNICODE["spread"].append("U+39c5")
UNICODE_TO_BLISS["U+39c5"].append("spread")
BLISS_TO_UNICODE["spreading"].append("U+39c5")
UNICODE_TO_BLISS["U+39c5"].append("spreading")
BLISS_TO_UNICODE["dispersion,dissemination,scattering,spread,spreading"] = ["U+39c5"]
UNICODE_TO_BLISS["U+39c5"].append("dispersion,dissemination,scattering,spread,spreading")
BLISS_TO_UNICODE["spiritual awareness"] = ["U+3d58"]
UNICODE_TO_BLISS["U+3d58"] = ["spiritual awareness"]
BLISS_TO_UNICODE["speech impaired"] = ["U+3d59"]
UNICODE_TO_BLISS["U+3d59"] = ["speech impaired"]
BLISS_TO_UNICODE["speech impairment"] = ["U+3d5a"]
UNICODE_TO_BLISS["U+3d5a"] = ["speech impairment"]
BLISS_TO_UNICODE["dysarthria"] = ["U+3d5b"]
UNICODE_TO_BLISS["U+3d5b"] = ["dysarthria"]
BLISS_TO_UNICODE["sexual harassment"] = ["U+3d5c"]
UNICODE_TO_BLISS["U+3d5c"] = ["sexual harassment"]
BLISS_TO_UNICODE["phantasy"].append("U+3896")
UNICODE_TO_BLISS["U+3896"].append("phantasy")
BLISS_TO_UNICODE["imagination"].append("U+3896")
UNICODE_TO_BLISS["U+3896"].append("imagination")
BLISS_TO_UNICODE["illusion"].append("U+3896")
UNICODE_TO_BLISS["U+3896"].append("illusion")
BLISS_TO_UNICODE["fantasy,phantasy,imagination,illusion"] = ["U+3896"]
UNICODE_TO_BLISS["U+3896"].append("fantasy,phantasy,imagination,illusion")
BLISS_TO_UNICODE["February"] = ["U+3d5d"]
UNICODE_TO_BLISS["U+3d5d"] = ["February"]
BLISS_TO_UNICODE["captivity"].append("U+37ec")
UNICODE_TO_BLISS["U+37ec"].append("captivity")
BLISS_TO_UNICODE["slavery"].append("U+37ec")
UNICODE_TO_BLISS["U+37ec"].append("slavery")
BLISS_TO_UNICODE["oppression,captivity,slavery"] = ["U+37ec"]
UNICODE_TO_BLISS["U+37ec"].append("oppression,captivity,slavery")
BLISS_TO_UNICODE["chance"] = ["U+3d5e"]
UNICODE_TO_BLISS["U+3d5e"] = ["chance"]
BLISS_TO_UNICODE["risk"] = ["U+3d5e"]
UNICODE_TO_BLISS["U+3d5e"].append("risk")
BLISS_TO_UNICODE["chance,risk"] = ["U+3d5e"]
UNICODE_TO_BLISS["U+3d5e"].append("chance,risk")
BLISS_TO_UNICODE["maracas"] = ["U+3d5f"]
UNICODE_TO_BLISS["U+3d5f"] = ["maracas"]
BLISS_TO_UNICODE["calabash"] = ["U+3d5f"]
UNICODE_TO_BLISS["U+3d5f"].append("calabash")
BLISS_TO_UNICODE["maracas,calabash"] = ["U+3d5f"]
UNICODE_TO_BLISS["U+3d5f"].append("maracas,calabash")
BLISS_TO_UNICODE["rythm instrument"] = ["U+3d60"]
UNICODE_TO_BLISS["U+3d60"] = ["rythm instrument"]
BLISS_TO_UNICODE["veil"] = ["U+3d61"]
UNICODE_TO_BLISS["U+3d61"] = ["veil"]
BLISS_TO_UNICODE["inspiration"] = ["U+3d62"]
UNICODE_TO_BLISS["U+3d62"] = ["inspiration"]
BLISS_TO_UNICODE["fruit salad"] = ["U+3d63"]
UNICODE_TO_BLISS["U+3d63"] = ["fruit salad"]
BLISS_TO_UNICODE["govern"] = ["U+3d64"]
UNICODE_TO_BLISS["U+3d64"] = ["govern"]
BLISS_TO_UNICODE["rule"].append("U+3d64")
UNICODE_TO_BLISS["U+3d64"].append("rule")
BLISS_TO_UNICODE["govern,rule"] = ["U+3d64"]
UNICODE_TO_BLISS["U+3d64"].append("govern,rule")
BLISS_TO_UNICODE["regulation"].append("U+3960")
UNICODE_TO_BLISS["U+3960"].append("regulation")
BLISS_TO_UNICODE["rule,regulation"] = ["U+3960"]
UNICODE_TO_BLISS["U+3960"].append("rule,regulation")
BLISS_TO_UNICODE["to guide"] = ["U+3d65"]
UNICODE_TO_BLISS["U+3d65"] = ["to guide"]
BLISS_TO_UNICODE["post office"] = ["U+3d66"]
UNICODE_TO_BLISS["U+3d66"] = ["post office"]
BLISS_TO_UNICODE["write"] = ["U+3d67"]
UNICODE_TO_BLISS["U+3d67"] = ["write"]
BLISS_TO_UNICODE["measuring spoon"] = ["U+3d68"]
UNICODE_TO_BLISS["U+3d68"] = ["measuring spoon"]
BLISS_TO_UNICODE["to measure"] = ["U+3d69"]
UNICODE_TO_BLISS["U+3d69"] = ["to measure"]
BLISS_TO_UNICODE["sledge"].append("U+38a7")
UNICODE_TO_BLISS["U+38a7"].append("sledge")
BLISS_TO_UNICODE["sleigh"] = ["U+38a7"]
UNICODE_TO_BLISS["U+38a7"].append("sleigh")
BLISS_TO_UNICODE["toboggan"] = ["U+38a7"]
UNICODE_TO_BLISS["U+38a7"].append("toboggan")
BLISS_TO_UNICODE["sled,sledge,sleigh,toboggan"] = ["U+38a7"]
UNICODE_TO_BLISS["U+38a7"].append("sled,sledge,sleigh,toboggan")
BLISS_TO_UNICODE["front"] = ["U+3d6a"]
UNICODE_TO_BLISS["U+3d6a"] = ["front"]
BLISS_TO_UNICODE["front of a thing"] = ["U+3d6a"]
UNICODE_TO_BLISS["U+3d6a"].append("front of a thing")
BLISS_TO_UNICODE["front,front of a thing"] = ["U+3d6a"]
UNICODE_TO_BLISS["U+3d6a"].append("front,front of a thing")
BLISS_TO_UNICODE["desirable"] = ["U+3d6b"]
UNICODE_TO_BLISS["U+3d6b"] = ["desirable"]
BLISS_TO_UNICODE["to want"] = ["U+3d6c"]
UNICODE_TO_BLISS["U+3d6c"] = ["to want"]
BLISS_TO_UNICODE["kindergarten"] = ["U+3d6d"]
UNICODE_TO_BLISS["U+3d6d"] = ["kindergarten"]
BLISS_TO_UNICODE["preschool"] = ["U+3d6d"]
UNICODE_TO_BLISS["U+3d6d"].append("preschool")
BLISS_TO_UNICODE["nursery"] = ["U+3d6d"]
UNICODE_TO_BLISS["U+3d6d"].append("nursery")
BLISS_TO_UNICODE["play group"] = ["U+3d6d"]
UNICODE_TO_BLISS["U+3d6d"].append("play group")
BLISS_TO_UNICODE["kindergarten,preschool,nursery,play group"] = ["U+3d6d"]
UNICODE_TO_BLISS["U+3d6d"].append("kindergarten,preschool,nursery,play group")
BLISS_TO_UNICODE["protected"] = ["U+3d6e"]
UNICODE_TO_BLISS["U+3d6e"] = ["protected"]
BLISS_TO_UNICODE["saved"] = ["U+3d6e"]
UNICODE_TO_BLISS["U+3d6e"].append("saved")
BLISS_TO_UNICODE["protected,saved"] = ["U+3d6e"]
UNICODE_TO_BLISS["U+3d6e"].append("protected,saved")
BLISS_TO_UNICODE["voter"] = ["U+3d6f"]
UNICODE_TO_BLISS["U+3d6f"] = ["voter"]
BLISS_TO_UNICODE["elector"] = ["U+3d6f"]
UNICODE_TO_BLISS["U+3d6f"].append("elector")
BLISS_TO_UNICODE["voter,elector"] = ["U+3d6f"]
UNICODE_TO_BLISS["U+3d6f"].append("voter,elector")
BLISS_TO_UNICODE["to choose"] = ["U+3d70"]
UNICODE_TO_BLISS["U+3d70"] = ["to choose"]
BLISS_TO_UNICODE["firecraft"] = ["U+3d71"]
UNICODE_TO_BLISS["U+3d71"] = ["firecraft"]
BLISS_TO_UNICODE["alternating"] = ["U+3d72"]
UNICODE_TO_BLISS["U+3d72"] = ["alternating"]
BLISS_TO_UNICODE["alternation"] = ["U+3d73"]
UNICODE_TO_BLISS["U+3d73"] = ["alternation"]
BLISS_TO_UNICODE["geology"] = ["U+3d74"]
UNICODE_TO_BLISS["U+3d74"] = ["geology"]
BLISS_TO_UNICODE["paper craft"] = ["U+3d75"]
UNICODE_TO_BLISS["U+3d75"] = ["paper craft"]
BLISS_TO_UNICODE["venereal papilloma"] = ["U+3d76"]
UNICODE_TO_BLISS["U+3d76"] = ["venereal papilloma"]
BLISS_TO_UNICODE["whisk"] = ["U+3d77"]
UNICODE_TO_BLISS["U+3d77"] = ["whisk"]
BLISS_TO_UNICODE["beater"] = ["U+3d77"]
UNICODE_TO_BLISS["U+3d77"].append("beater")
BLISS_TO_UNICODE["whisk,beater"] = ["U+3d77"]
UNICODE_TO_BLISS["U+3d77"].append("whisk,beater")
BLISS_TO_UNICODE["to mix"] = ["U+3d78"]
UNICODE_TO_BLISS["U+3d78"] = ["to mix"]
BLISS_TO_UNICODE["detective"] = ["U+3d79"]
UNICODE_TO_BLISS["U+3d79"] = ["detective"]
BLISS_TO_UNICODE["investigator"] = ["U+3d79"]
UNICODE_TO_BLISS["U+3d79"].append("investigator")
BLISS_TO_UNICODE["detective,investigator"] = ["U+3d79"]
UNICODE_TO_BLISS["U+3d79"].append("detective,investigator")
BLISS_TO_UNICODE["humidity"] = ["U+3d7a"]
UNICODE_TO_BLISS["U+3d7a"] = ["humidity"]
BLISS_TO_UNICODE["arithmetic"] = ["U+32de"]
UNICODE_TO_BLISS["U+32de"].append("arithmetic")
BLISS_TO_UNICODE["math"] = ["U+32de"]
UNICODE_TO_BLISS["U+32de"].append("math")
BLISS_TO_UNICODE["mathematics,arithmetic,math"] = ["U+32de"]
UNICODE_TO_BLISS["U+32de"].append("mathematics,arithmetic,math")
BLISS_TO_UNICODE["math,mathematics"] = ["U+32de"]
UNICODE_TO_BLISS["U+32de"].append("math,mathematics")
BLISS_TO_UNICODE["subject"] = ["U+3d7b"]
UNICODE_TO_BLISS["U+3d7b"] = ["subject"]
BLISS_TO_UNICODE["chew"] = ["U+3d7c"]
UNICODE_TO_BLISS["U+3d7c"] = ["chew"]
BLISS_TO_UNICODE["fish cage"] = ["U+3d7d"]
UNICODE_TO_BLISS["U+3d7d"] = ["fish cage"]
BLISS_TO_UNICODE["midsummer"] = ["U+3d7e"]
UNICODE_TO_BLISS["U+3d7e"] = ["midsummer"]
BLISS_TO_UNICODE["antler"] = ["U+34a0"]
UNICODE_TO_BLISS["U+34a0"].append("antler")
BLISS_TO_UNICODE["cook"] = ["U+3d7f"]
UNICODE_TO_BLISS["U+3d7f"] = ["cook"]
BLISS_TO_UNICODE["chef"] = ["U+3d7f"]
UNICODE_TO_BLISS["U+3d7f"].append("chef")
BLISS_TO_UNICODE["cook,chef"] = ["U+3d7f"]
UNICODE_TO_BLISS["U+3d7f"].append("cook,chef")
BLISS_TO_UNICODE["bongo drum"] = ["U+3d80"]
UNICODE_TO_BLISS["U+3d80"] = ["bongo drum"]
BLISS_TO_UNICODE["hand drum"] = ["U+3d80"]
UNICODE_TO_BLISS["U+3d80"].append("hand drum")
BLISS_TO_UNICODE["bongo drum,hand drum"] = ["U+3d80"]
UNICODE_TO_BLISS["U+3d80"].append("bongo drum,hand drum")
BLISS_TO_UNICODE["lizard"] = ["U+3d81"]
UNICODE_TO_BLISS["U+3d81"] = ["lizard"]
BLISS_TO_UNICODE["reptile"] = ["U+3d81"]
UNICODE_TO_BLISS["U+3d81"].append("reptile")
BLISS_TO_UNICODE["lizard,reptile"] = ["U+3d81"]
UNICODE_TO_BLISS["U+3d81"].append("lizard,reptile")
BLISS_TO_UNICODE["cervine"] = ["U+3aac"]
UNICODE_TO_BLISS["U+3aac"].append("cervine")
BLISS_TO_UNICODE["cervid"] = ["U+3aac"]
UNICODE_TO_BLISS["U+3aac"].append("cervid")
BLISS_TO_UNICODE["deer,cervine"] = ["U+3aac"]
UNICODE_TO_BLISS["U+3aac"].append("deer,cervine")
BLISS_TO_UNICODE["above"] = ["U+33c9"]
UNICODE_TO_BLISS["U+33c9"].append("above")
BLISS_TO_UNICODE["superior"] = ["U+33c9"]
UNICODE_TO_BLISS["U+33c9"].append("superior")
BLISS_TO_UNICODE["over,above,superior"] = ["U+33c9"]
UNICODE_TO_BLISS["U+33c9"].append("over,above,superior")
BLISS_TO_UNICODE["horse droppings"] = ["U+3d82"]
UNICODE_TO_BLISS["U+3d82"] = ["horse droppings"]
BLISS_TO_UNICODE["radioactivity"] = ["U+3425"]
UNICODE_TO_BLISS["U+3425"].append("radioactivity")
BLISS_TO_UNICODE["nuclear radiation,radioactivity"] = ["U+3425"]
UNICODE_TO_BLISS["U+3425"].append("nuclear radiation,radioactivity")
BLISS_TO_UNICODE["plug in"] = ["U+3d83"]
UNICODE_TO_BLISS["U+3d83"] = ["plug in"]
BLISS_TO_UNICODE["connect"].append("U+3d83")
UNICODE_TO_BLISS["U+3d83"].append("connect")
BLISS_TO_UNICODE["plug in,connect"] = ["U+3d83"]
UNICODE_TO_BLISS["U+3d83"].append("plug in,connect")
BLISS_TO_UNICODE["plug"] = ["U+3d84"]
UNICODE_TO_BLISS["U+3d84"] = ["plug"]
BLISS_TO_UNICODE["shelter"].append("U+33f5")
UNICODE_TO_BLISS["U+33f5"].append("shelter")
BLISS_TO_UNICODE["protection,shelter"] = ["U+33f5"]
UNICODE_TO_BLISS["U+33f5"].append("protection,shelter")
BLISS_TO_UNICODE["symbol looks like a roof"] = ["U+3d85"]
UNICODE_TO_BLISS["U+3d85"] = ["symbol looks like a roof"]
BLISS_TO_UNICODE[" suggesting the protection provided by a roof"] = ["U+3d86"]
UNICODE_TO_BLISS["U+3d86"] = [" suggesting the protection provided by a roof"]
BLISS_TO_UNICODE["protection"].append("U+377a")
UNICODE_TO_BLISS["U+377a"].append("protection")
BLISS_TO_UNICODE["defence"].append("U+377a")
UNICODE_TO_BLISS["U+377a"].append("defence")
BLISS_TO_UNICODE["care,protection,defence"] = ["U+377a"]
UNICODE_TO_BLISS["U+377a"].append("care,protection,defence")
BLISS_TO_UNICODE["celebration"] = ["U+3d87"]
UNICODE_TO_BLISS["U+3d87"] = ["celebration"]
BLISS_TO_UNICODE["Tuesday"] = ["U+3d88"]
UNICODE_TO_BLISS["U+3d88"] = ["Tuesday"]
BLISS_TO_UNICODE["Simchat Torah"] = ["U+3d89"]
UNICODE_TO_BLISS["U+3d89"] = ["Simchat Torah"]
BLISS_TO_UNICODE["Torah"] = ["U+3d8a"]
UNICODE_TO_BLISS["U+3d8a"] = ["Torah"]
BLISS_TO_UNICODE["double bass"] = ["U+3d8b"]
UNICODE_TO_BLISS["U+3d8b"] = ["double bass"]
BLISS_TO_UNICODE["bass fiddle"] = ["U+3d8b"]
UNICODE_TO_BLISS["U+3d8b"].append("bass fiddle")
BLISS_TO_UNICODE["contrabass"] = ["U+3d8b"]
UNICODE_TO_BLISS["U+3d8b"].append("contrabass")
BLISS_TO_UNICODE["double bass,bass fiddle,contrabass"] = ["U+3d8b"]
UNICODE_TO_BLISS["U+3d8b"].append("double bass,bass fiddle,contrabass")
BLISS_TO_UNICODE["string and bow instrument"] = ["U+3d8c"]
UNICODE_TO_BLISS["U+3d8c"] = ["string and bow instrument"]
BLISS_TO_UNICODE["stressed"] = ["U+3d8d"]
UNICODE_TO_BLISS["U+3d8d"] = ["stressed"]
BLISS_TO_UNICODE["lonely"] = ["U+3d8e"]
UNICODE_TO_BLISS["U+3d8e"] = ["lonely"]
BLISS_TO_UNICODE["lonesome"] = ["U+3d8e"]
UNICODE_TO_BLISS["U+3d8e"].append("lonesome")
BLISS_TO_UNICODE["lonely,lonesome"] = ["U+3d8e"]
UNICODE_TO_BLISS["U+3d8e"].append("lonely,lonesome")
BLISS_TO_UNICODE["envious"] = ["U+3d8f"]
UNICODE_TO_BLISS["U+3d8f"] = ["envious"]
BLISS_TO_UNICODE["to have"] = ["U+3d90"]
UNICODE_TO_BLISS["U+3d90"] = ["to have"]
BLISS_TO_UNICODE["Jew"] = ["U+3d91"]
UNICODE_TO_BLISS["U+3d91"] = ["Jew"]
BLISS_TO_UNICODE["stomach flu"] = ["U+3d92"]
UNICODE_TO_BLISS["U+3d92"] = ["stomach flu"]
BLISS_TO_UNICODE["every"] = ["U+3374"]
UNICODE_TO_BLISS["U+3374"].append("every")
BLISS_TO_UNICODE["everything"] = ["U+3374"]
UNICODE_TO_BLISS["U+3374"].append("everything")
BLISS_TO_UNICODE["total"] = ["U+3374"]
UNICODE_TO_BLISS["U+3374"].append("total")
BLISS_TO_UNICODE["whole"] = ["U+3374"]
UNICODE_TO_BLISS["U+3374"].append("whole")
BLISS_TO_UNICODE["all,every,everything,total,whole"] = ["U+3374"]
UNICODE_TO_BLISS["U+3374"].append("all,every,everything,total,whole")
BLISS_TO_UNICODE["bra"] = ["U+3d93"]
UNICODE_TO_BLISS["U+3d93"] = ["bra"]
BLISS_TO_UNICODE["brassiere"] = ["U+3d93"]
UNICODE_TO_BLISS["U+3d93"].append("brassiere")
BLISS_TO_UNICODE["bra,brassiere"] = ["U+3d93"]
UNICODE_TO_BLISS["U+3d93"].append("bra,brassiere")
BLISS_TO_UNICODE["motivate"] = ["U+3d94"]
UNICODE_TO_BLISS["U+3d94"] = ["motivate"]
BLISS_TO_UNICODE["motivation"] = ["U+3d95"]
UNICODE_TO_BLISS["U+3d95"] = ["motivation"]
BLISS_TO_UNICODE["negative"].append("U+34c1")
UNICODE_TO_BLISS["U+34c1"].append("negative")
BLISS_TO_UNICODE["no"] = ["U+34c1"]
UNICODE_TO_BLISS["U+34c1"].append("no")
BLISS_TO_UNICODE["don't"] = ["U+34c1"]
UNICODE_TO_BLISS["U+34c1"].append("don't")
BLISS_TO_UNICODE["doesn't"] = ["U+34c1"]
UNICODE_TO_BLISS["U+34c1"].append("doesn't")
BLISS_TO_UNICODE["not,negative,no,don't,doesn't"] = ["U+34c1"]
UNICODE_TO_BLISS["U+34c1"].append("not,negative,no,don't,doesn't")
BLISS_TO_UNICODE["blueberry"] = ["U+3d97"]
UNICODE_TO_BLISS["U+3d97"] = ["blueberry"]
BLISS_TO_UNICODE["terrestrial planet"] = ["U+3bf2"]
UNICODE_TO_BLISS["U+3bf2"].append("terrestrial planet")
BLISS_TO_UNICODE["rock planet,terrestrial planet"] = ["U+3bf2"]
UNICODE_TO_BLISS["U+3bf2"].append("rock planet,terrestrial planet")
BLISS_TO_UNICODE["stickball"] = ["U+3d98"]
UNICODE_TO_BLISS["U+3d98"] = ["stickball"]
BLISS_TO_UNICODE["geographer"] = ["U+3d99"]
UNICODE_TO_BLISS["U+3d99"] = ["geographer"]
BLISS_TO_UNICODE["employment"] = ["U+3463"]
UNICODE_TO_BLISS["U+3463"].append("employment")
BLISS_TO_UNICODE["job"] = ["U+3463"]
UNICODE_TO_BLISS["U+3463"].append("job")
BLISS_TO_UNICODE["work,employment,job"] = ["U+3463"]
UNICODE_TO_BLISS["U+3463"].append("work,employment,job")
BLISS_TO_UNICODE["hug"] = ["U+3d9a"]
UNICODE_TO_BLISS["U+3d9a"] = ["hug"]
BLISS_TO_UNICODE["cuddle"] = ["U+3d9a"]
UNICODE_TO_BLISS["U+3d9a"].append("cuddle")
BLISS_TO_UNICODE["embrace"] = ["U+3d9a"]
UNICODE_TO_BLISS["U+3d9a"].append("embrace")
BLISS_TO_UNICODE["hug,cuddle,embrace"] = ["U+3d9a"]
UNICODE_TO_BLISS["U+3d9a"].append("hug,cuddle,embrace")
BLISS_TO_UNICODE["mechanic"] = ["U+3d9b"]
UNICODE_TO_BLISS["U+3d9b"] = ["mechanic"]
BLISS_TO_UNICODE["technician"] = ["U+3d9b"]
UNICODE_TO_BLISS["U+3d9b"].append("technician")
BLISS_TO_UNICODE["mechanic,technician"] = ["U+3d9b"]
UNICODE_TO_BLISS["U+3d9b"].append("mechanic,technician")
BLISS_TO_UNICODE["document"] = ["U+3d9c"]
UNICODE_TO_BLISS["U+3d9c"] = ["document"]
BLISS_TO_UNICODE["written record"] = ["U+3d9c"]
UNICODE_TO_BLISS["U+3d9c"].append("written record")
BLISS_TO_UNICODE["document,written record"] = ["U+3d9c"]
UNICODE_TO_BLISS["U+3d9c"].append("document,written record")
BLISS_TO_UNICODE["violin"] = ["U+3d9d"]
UNICODE_TO_BLISS["U+3d9d"] = ["violin"]
BLISS_TO_UNICODE["bow and string instrument"] = ["U+3d9e"]
UNICODE_TO_BLISS["U+3d9e"] = ["bow and string instrument"]
BLISS_TO_UNICODE["CD player"] = ["U+3d9f"]
UNICODE_TO_BLISS["U+3d9f"] = ["CD player"]
BLISS_TO_UNICODE["record player"] = ["U+3d9f"]
UNICODE_TO_BLISS["U+3d9f"].append("record player")
BLISS_TO_UNICODE["stereo"] = ["U+3d9f"]
UNICODE_TO_BLISS["U+3d9f"].append("stereo")
BLISS_TO_UNICODE["CD player,record player,stereo"] = ["U+3d9f"]
UNICODE_TO_BLISS["U+3d9f"].append("CD player,record player,stereo")
BLISS_TO_UNICODE["record"] = ["U+3da0"]
UNICODE_TO_BLISS["U+3da0"] = ["record"]
BLISS_TO_UNICODE["meat sauce"] = ["U+3da1"]
UNICODE_TO_BLISS["U+3da1"] = ["meat sauce"]
BLISS_TO_UNICODE["tattoo"] = ["U+3da2"]
UNICODE_TO_BLISS["U+3da2"] = ["tattoo"]
BLISS_TO_UNICODE["picture on skin"] = ["U+3da2"]
UNICODE_TO_BLISS["U+3da2"].append("picture on skin")
BLISS_TO_UNICODE["tattoo,picture on skin"] = ["U+3da2"]
UNICODE_TO_BLISS["U+3da2"].append("tattoo,picture on skin")
BLISS_TO_UNICODE["gamble"] = ["U+3da3"]
UNICODE_TO_BLISS["U+3da3"] = ["gamble"]
BLISS_TO_UNICODE["pizza slice"] = ["U+3da4"]
UNICODE_TO_BLISS["U+3da4"] = ["pizza slice"]
BLISS_TO_UNICODE["sector"] = ["U+3da5"]
UNICODE_TO_BLISS["U+3da5"] = ["sector"]
BLISS_TO_UNICODE["circle sector"] = ["U+3da6"]
UNICODE_TO_BLISS["U+3da6"] = ["circle sector"]
BLISS_TO_UNICODE["sugar lump"] = ["U+3da7"]
UNICODE_TO_BLISS["U+3da7"] = ["sugar lump"]
BLISS_TO_UNICODE["cube"].append("U+3da7")
UNICODE_TO_BLISS["U+3da7"].append("cube")
BLISS_TO_UNICODE["sugar lump,cube"] = ["U+3da7"]
UNICODE_TO_BLISS["U+3da7"].append("sugar lump,cube")
BLISS_TO_UNICODE["fever"] = ["U+3da8"]
UNICODE_TO_BLISS["U+3da8"] = ["fever"]
BLISS_TO_UNICODE["temperature"].append("U+3da8")
UNICODE_TO_BLISS["U+3da8"].append("temperature")
BLISS_TO_UNICODE["fever,temperature"] = ["U+3da8"]
UNICODE_TO_BLISS["U+3da8"].append("fever,temperature")
BLISS_TO_UNICODE["body temperature"] = ["U+3da9"]
UNICODE_TO_BLISS["U+3da9"] = ["body temperature"]
BLISS_TO_UNICODE["day care centre"] = ["U+3daa"]
UNICODE_TO_BLISS["U+3daa"] = ["day care centre"]
BLISS_TO_UNICODE["day care"] = ["U+3dab"]
UNICODE_TO_BLISS["U+3dab"] = ["day care"]
BLISS_TO_UNICODE["lad"] = ["U+328b"]
UNICODE_TO_BLISS["U+328b"].append("lad")
BLISS_TO_UNICODE["boy,lad"] = ["U+328b"]
UNICODE_TO_BLISS["U+328b"].append("boy,lad")
BLISS_TO_UNICODE["behind"] = ["U+34d1"]
UNICODE_TO_BLISS["U+34d1"].append("behind")
BLISS_TO_UNICODE["after,behind"] = ["U+34d1"]
UNICODE_TO_BLISS["U+34d1"].append("after,behind")
BLISS_TO_UNICODE["birth control pill"] = ["U+3dac"]
UNICODE_TO_BLISS["U+3dac"] = ["birth control pill"]
BLISS_TO_UNICODE["pill"].append("U+3dac")
UNICODE_TO_BLISS["U+3dac"].append("pill")
BLISS_TO_UNICODE["birth control pill,pill"] = ["U+3dac"]
UNICODE_TO_BLISS["U+3dac"].append("birth control pill,pill")
BLISS_TO_UNICODE["law"].append("U+3702")
UNICODE_TO_BLISS["U+3702"].append("law")
BLISS_TO_UNICODE["judgement,law"] = ["U+3702"]
UNICODE_TO_BLISS["U+3702"].append("judgement,law")
BLISS_TO_UNICODE["The Law"] = ["U+38e2"]
UNICODE_TO_BLISS["U+38e2"].append("The Law")
BLISS_TO_UNICODE["law,The Law"] = ["U+38e2"]
UNICODE_TO_BLISS["U+38e2"].append("law,The Law")
BLISS_TO_UNICODE["single father"] = ["U+3dad"]
UNICODE_TO_BLISS["U+3dad"] = ["single father"]
BLISS_TO_UNICODE["astronaut"] = ["U+3dae"]
UNICODE_TO_BLISS["U+3dae"] = ["astronaut"]
BLISS_TO_UNICODE["cosmonaut"] = ["U+3dae"]
UNICODE_TO_BLISS["U+3dae"].append("cosmonaut")
BLISS_TO_UNICODE["astronaut,cosmonaut"] = ["U+3dae"]
UNICODE_TO_BLISS["U+3dae"].append("astronaut,cosmonaut")
BLISS_TO_UNICODE["appreciate"] = ["U+3daf"]
UNICODE_TO_BLISS["U+3daf"] = ["appreciate"]
BLISS_TO_UNICODE["value"] = ["U+3daf"]
UNICODE_TO_BLISS["U+3daf"].append("value")
BLISS_TO_UNICODE["treasure"].append("U+3daf")
UNICODE_TO_BLISS["U+3daf"].append("treasure")
BLISS_TO_UNICODE["appreciate,value,treasure"] = ["U+3daf"]
UNICODE_TO_BLISS["U+3daf"].append("appreciate,value,treasure")
BLISS_TO_UNICODE["to evaluate"] = ["U+3db0"]
UNICODE_TO_BLISS["U+3db0"] = ["to evaluate"]
BLISS_TO_UNICODE["waiter"] = ["U+3db1"]
UNICODE_TO_BLISS["U+3db1"] = ["waiter"]
BLISS_TO_UNICODE["waitress"] = ["U+3db1"]
UNICODE_TO_BLISS["U+3db1"].append("waitress")
BLISS_TO_UNICODE["waiter,waitress"] = ["U+3db1"]
UNICODE_TO_BLISS["U+3db1"].append("waiter,waitress")
BLISS_TO_UNICODE["ambulance"] = ["U+3db2"]
UNICODE_TO_BLISS["U+3db2"] = ["ambulance"]
BLISS_TO_UNICODE["popsicle"] = ["U+3db3"]
UNICODE_TO_BLISS["U+3db3"] = ["popsicle"]
BLISS_TO_UNICODE["office"] = ["U+3db4"]
UNICODE_TO_BLISS["U+3db4"] = ["office"]
BLISS_TO_UNICODE["muffin"] = ["U+3db5"]
UNICODE_TO_BLISS["U+3db5"] = ["muffin"]
BLISS_TO_UNICODE["bun"] = ["U+3db5"]
UNICODE_TO_BLISS["U+3db5"].append("bun")
BLISS_TO_UNICODE["muffin,bun"] = ["U+3db5"]
UNICODE_TO_BLISS["U+3db5"].append("muffin,bun")
BLISS_TO_UNICODE["lower body"] = ["U+3db6"]
UNICODE_TO_BLISS["U+3db6"] = ["lower body"]
BLISS_TO_UNICODE["below"] = ["U+3db7"]
UNICODE_TO_BLISS["U+3db7"] = ["below"]
BLISS_TO_UNICODE["board of directors"].append("U+33ab")
UNICODE_TO_BLISS["U+33ab"].append("board of directors")
BLISS_TO_UNICODE["executive"].append("U+33ab")
UNICODE_TO_BLISS["U+33ab"].append("executive")
BLISS_TO_UNICODE["board,board of directors,executive"] = ["U+33ab"]
UNICODE_TO_BLISS["U+33ab"].append("board,board of directors,executive")
BLISS_TO_UNICODE["adolescence"] = ["U+3db8"]
UNICODE_TO_BLISS["U+3db8"] = ["adolescence"]
BLISS_TO_UNICODE["adolescent"] = ["U+3db9"]
UNICODE_TO_BLISS["U+3db9"] = ["adolescent"]
BLISS_TO_UNICODE["anywhere"] = ["U+3dba"]
UNICODE_TO_BLISS["U+3dba"] = ["anywhere"]
BLISS_TO_UNICODE["anyplace"] = ["U+3dba"]
UNICODE_TO_BLISS["U+3dba"].append("anyplace")
BLISS_TO_UNICODE["someplace"] = ["U+3dba"]
UNICODE_TO_BLISS["U+3dba"].append("someplace")
BLISS_TO_UNICODE["somewhere"].append("U+3dba")
UNICODE_TO_BLISS["U+3dba"].append("somewhere")
BLISS_TO_UNICODE["anywhere,anyplace,someplace,somewhere"] = ["U+3dba"]
UNICODE_TO_BLISS["U+3dba"].append("anywhere,anyplace,someplace,somewhere")
BLISS_TO_UNICODE["interval"].append("U+359b")
UNICODE_TO_BLISS["U+359b"].append("interval")
BLISS_TO_UNICODE["period"].append("U+359b")
UNICODE_TO_BLISS["U+359b"].append("period")
BLISS_TO_UNICODE["awhile"] = ["U+359b"]
UNICODE_TO_BLISS["U+359b"].append("awhile")
BLISS_TO_UNICODE["for a while"] = ["U+359b"]
UNICODE_TO_BLISS["U+359b"].append("for a while")
BLISS_TO_UNICODE["limited time,interval,period,awhile,for a while"] = ["U+359b"]
UNICODE_TO_BLISS["U+359b"].append("limited time,interval,period,awhile,for a while")
BLISS_TO_UNICODE["male friend"] = ["U+3dbb"]
UNICODE_TO_BLISS["U+3dbb"] = ["male friend"]
BLISS_TO_UNICODE["friend"] = ["U+3dbc"]
UNICODE_TO_BLISS["U+3dbc"] = ["friend"]
BLISS_TO_UNICODE["owl"] = ["U+3dbd"]
UNICODE_TO_BLISS["U+3dbd"] = ["owl"]
BLISS_TO_UNICODE["night bird"] = ["U+3dbd"]
UNICODE_TO_BLISS["U+3dbd"].append("night bird")
BLISS_TO_UNICODE["owl,night bird"] = ["U+3dbd"]
UNICODE_TO_BLISS["U+3dbd"].append("owl,night bird")
BLISS_TO_UNICODE["medical examination"] = ["U+3dbe"]
UNICODE_TO_BLISS["U+3dbe"] = ["medical examination"]
BLISS_TO_UNICODE["coffee"] = ["U+3dbf"]
UNICODE_TO_BLISS["U+3dbf"] = ["coffee"]
BLISS_TO_UNICODE["scatter ashes"] = ["U+3dc0"]
UNICODE_TO_BLISS["U+3dc0"] = ["scatter ashes"]
BLISS_TO_UNICODE["to scatter"] = ["U+3dc1"]
UNICODE_TO_BLISS["U+3dc1"] = ["to scatter"]
BLISS_TO_UNICODE["ashes"] = ["U+3dc2"]
UNICODE_TO_BLISS["U+3dc2"] = ["ashes"]
BLISS_TO_UNICODE["influenced"] = ["U+3dc3"]
UNICODE_TO_BLISS["U+3dc3"] = ["influenced"]
BLISS_TO_UNICODE["affected"] = ["U+3dc3"]
UNICODE_TO_BLISS["U+3dc3"].append("affected")
BLISS_TO_UNICODE["influenced,affected"] = ["U+3dc3"]
UNICODE_TO_BLISS["U+3dc3"].append("influenced,affected")
BLISS_TO_UNICODE["smoothing iron"] = ["U+3331"]
UNICODE_TO_BLISS["U+3331"].append("smoothing iron")
BLISS_TO_UNICODE["iron,smoothing iron"] = ["U+3331"]
UNICODE_TO_BLISS["U+3331"].append("iron,smoothing iron")
BLISS_TO_UNICODE["safe"] = ["U+3dc4"]
UNICODE_TO_BLISS["U+3dc4"] = ["safe"]
BLISS_TO_UNICODE["safely"] = ["U+3dc4"]
UNICODE_TO_BLISS["U+3dc4"].append("safely")
BLISS_TO_UNICODE["secure"] = ["U+3dc4"]
UNICODE_TO_BLISS["U+3dc4"].append("secure")
BLISS_TO_UNICODE["securely"] = ["U+3dc4"]
UNICODE_TO_BLISS["U+3dc4"].append("securely")
BLISS_TO_UNICODE["safe,safely,secure,securely"] = ["U+3dc4"]
UNICODE_TO_BLISS["U+3dc4"].append("safe,safely,secure,securely")
BLISS_TO_UNICODE["safety"] = ["U+3dc5"]
UNICODE_TO_BLISS["U+3dc5"] = ["safety"]
BLISS_TO_UNICODE["rest period"] = ["U+3dc6"]
UNICODE_TO_BLISS["U+3dc6"] = ["rest period"]
BLISS_TO_UNICODE["break"].append("U+3dc6")
UNICODE_TO_BLISS["U+3dc6"].append("break")
BLISS_TO_UNICODE["rest period,break"] = ["U+3dc6"]
UNICODE_TO_BLISS["U+3dc6"].append("rest period,break")
BLISS_TO_UNICODE["break,fracture"] = ["U+34c8"]
UNICODE_TO_BLISS["U+34c8"].append("break,fracture")
BLISS_TO_UNICODE["orchestra"] = ["U+3bb7"]
UNICODE_TO_BLISS["U+3bb7"].append("orchestra")
BLISS_TO_UNICODE["band,orchestra"] = ["U+3bb7"]
UNICODE_TO_BLISS["U+3bb7"].append("band,orchestra")
BLISS_TO_UNICODE["pictograph of head and long neck"] = ["U+3dc7"]
UNICODE_TO_BLISS["U+3dc7"] = ["pictograph of head and long neck"]
BLISS_TO_UNICODE["hydrotherapist"] = ["U+3dc8"]
UNICODE_TO_BLISS["U+3dc8"] = ["hydrotherapist"]
BLISS_TO_UNICODE["sliced bread"] = ["U+3358"]
UNICODE_TO_BLISS["U+3358"].append("sliced bread")
BLISS_TO_UNICODE["frozen meat"] = ["U+3634"]
UNICODE_TO_BLISS["U+3634"].append("frozen meat")
BLISS_TO_UNICODE["aport"] = ["U+3dc9"]
UNICODE_TO_BLISS["U+3dc9"] = ["aport"]
BLISS_TO_UNICODE["port"] = ["U+3dca"]
UNICODE_TO_BLISS["U+3dca"] = ["port"]
BLISS_TO_UNICODE["dingo"] = ["U+36a3"]
UNICODE_TO_BLISS["U+36a3"].append("dingo")
BLISS_TO_UNICODE["wild dog"] = ["U+36a3"]
UNICODE_TO_BLISS["U+36a3"].append("wild dog")
BLISS_TO_UNICODE["wolf,dingo,wild dog"] = ["U+36a3"]
UNICODE_TO_BLISS["U+36a3"].append("wolf,dingo,wild dog")
BLISS_TO_UNICODE["biathlon"] = ["U+3dcb"]
UNICODE_TO_BLISS["U+3dcb"] = ["biathlon"]
BLISS_TO_UNICODE["skies"] = ["U+3dcc"]
UNICODE_TO_BLISS["U+3dcc"] = ["skies"]
BLISS_TO_UNICODE["cartography"] = ["U+3dcd"]
UNICODE_TO_BLISS["U+3dcd"] = ["cartography"]
BLISS_TO_UNICODE["map"] = ["U+3dce"]
UNICODE_TO_BLISS["U+3dce"] = ["map"]
BLISS_TO_UNICODE["prawn"] = ["U+3dcf"]
UNICODE_TO_BLISS["U+3dcf"] = ["prawn"]
BLISS_TO_UNICODE["shellfish without claws"] = ["U+3dd0"]
UNICODE_TO_BLISS["U+3dd0"] = ["shellfish without claws"]
BLISS_TO_UNICODE["residential institution"] = ["U+3dd1"]
UNICODE_TO_BLISS["U+3dd1"] = ["residential institution"]
BLISS_TO_UNICODE["group home"] = ["U+3dd1"]
UNICODE_TO_BLISS["U+3dd1"].append("group home")
BLISS_TO_UNICODE["hostel"] = ["U+3dd1"]
UNICODE_TO_BLISS["U+3dd1"].append("hostel")
BLISS_TO_UNICODE["residential home"] = ["U+3dd1"]
UNICODE_TO_BLISS["U+3dd1"].append("residential home")
BLISS_TO_UNICODE["residential institution,group home,hostel,residential home"] = ["U+3dd1"]
UNICODE_TO_BLISS["U+3dd1"].append("residential institution,group home,hostel,residential home")
BLISS_TO_UNICODE["Bliss fanatic"] = ["U+3dd2"]
UNICODE_TO_BLISS["U+3dd2"] = ["Bliss fanatic"]
BLISS_TO_UNICODE["fanatic"] = ["U+3dd3"]
UNICODE_TO_BLISS["U+3dd3"] = ["fanatic"]
BLISS_TO_UNICODE["medication"] = ["U+3219"]
UNICODE_TO_BLISS["U+3219"].append("medication")
BLISS_TO_UNICODE["medicine,medication"] = ["U+3219"]
UNICODE_TO_BLISS["U+3219"].append("medicine,medication")
BLISS_TO_UNICODE["medical practice"] = ["U+3219"]
UNICODE_TO_BLISS["U+3219"].append("medical practice")
BLISS_TO_UNICODE["medicine,medical practice"] = ["U+3219"]
UNICODE_TO_BLISS["U+3219"].append("medicine,medical practice")
BLISS_TO_UNICODE["symbol suggests a modified caduceus"] = ["U+3dd4"]
UNICODE_TO_BLISS["U+3dd4"] = ["symbol suggests a modified caduceus"]
BLISS_TO_UNICODE[" the traditional medical symbol"] = ["U+3dd5"]
UNICODE_TO_BLISS["U+3dd5"] = [" the traditional medical symbol"]
BLISS_TO_UNICODE["barrier"] = ["U+3dd6"]
UNICODE_TO_BLISS["U+3dd6"] = ["barrier"]
BLISS_TO_UNICODE["venereal disease"] = ["U+3dd7"]
UNICODE_TO_BLISS["U+3dd7"] = ["venereal disease"]
BLISS_TO_UNICODE["large intestine"] = ["U+3dd8"]
UNICODE_TO_BLISS["U+3dd8"] = ["large intestine"]
BLISS_TO_UNICODE["female friend"] = ["U+3dd9"]
UNICODE_TO_BLISS["U+3dd9"] = ["female friend"]
BLISS_TO_UNICODE["September"] = ["U+3dda"]
UNICODE_TO_BLISS["U+3dda"] = ["September"]
BLISS_TO_UNICODE["9"] = ["U+3ddb"]
UNICODE_TO_BLISS["U+3ddb"] = ["9"]
BLISS_TO_UNICODE["pictograph of a scroll on two posts"] = ["U+3ddc"]
UNICODE_TO_BLISS["U+3ddc"] = ["pictograph of a scroll on two posts"]
BLISS_TO_UNICODE["organize"] = ["U+3ddd"]
UNICODE_TO_BLISS["U+3ddd"] = ["organize"]
BLISS_TO_UNICODE["arrange"] = ["U+3ddd"]
UNICODE_TO_BLISS["U+3ddd"].append("arrange")
BLISS_TO_UNICODE["organize,arrange"] = ["U+3ddd"]
UNICODE_TO_BLISS["U+3ddd"].append("organize,arrange")
BLISS_TO_UNICODE["to plan"] = ["U+3dde"]
UNICODE_TO_BLISS["U+3dde"] = ["to plan"]
BLISS_TO_UNICODE["single parent family"] = ["U+3ddf"]
UNICODE_TO_BLISS["U+3ddf"] = ["single parent family"]
BLISS_TO_UNICODE["another"] = ["U+34d5"]
UNICODE_TO_BLISS["U+34d5"].append("another")
BLISS_TO_UNICODE["other,another"] = ["U+34d5"]
UNICODE_TO_BLISS["U+34d5"].append("other,another")
BLISS_TO_UNICODE["disembark"] = ["U+3de0"]
UNICODE_TO_BLISS["U+3de0"] = ["disembark"]
BLISS_TO_UNICODE["to exit"] = ["U+3de1"]
UNICODE_TO_BLISS["U+3de1"] = ["to exit"]
BLISS_TO_UNICODE["fat"] = ["U+3de2"]
UNICODE_TO_BLISS["U+3de2"] = ["fat"]
BLISS_TO_UNICODE["thick"].append("U+3de2")
UNICODE_TO_BLISS["U+3de2"].append("thick")
BLISS_TO_UNICODE["fat,thick"] = ["U+3de2"]
UNICODE_TO_BLISS["U+3de2"].append("fat,thick")
BLISS_TO_UNICODE["fatness"] = ["U+3de3"]
UNICODE_TO_BLISS["U+3de3"] = ["fatness"]
BLISS_TO_UNICODE["thickness"] = ["U+3de4"]
UNICODE_TO_BLISS["U+3de4"] = ["thickness"]
BLISS_TO_UNICODE["illustrate"] = ["U+3de5"]
UNICODE_TO_BLISS["U+3de5"] = ["illustrate"]
BLISS_TO_UNICODE["symbol display"] = ["U+3de6"]
UNICODE_TO_BLISS["U+3de6"] = ["symbol display"]
BLISS_TO_UNICODE["symbol board"] = ["U+3de6"]
UNICODE_TO_BLISS["U+3de6"].append("symbol board")
BLISS_TO_UNICODE["symbol chart"] = ["U+3de6"]
UNICODE_TO_BLISS["U+3de6"].append("symbol chart")
BLISS_TO_UNICODE["symbol display,symbol board,symbol chart"] = ["U+3de6"]
UNICODE_TO_BLISS["U+3de6"].append("symbol display,symbol board,symbol chart")
BLISS_TO_UNICODE["inflate"] = ["U+3de7"]
UNICODE_TO_BLISS["U+3de7"] = ["inflate"]
BLISS_TO_UNICODE["catheter"].append("U+37a0")
UNICODE_TO_BLISS["U+37a0"].append("catheter")
BLISS_TO_UNICODE["cannula"].append("U+37a0")
UNICODE_TO_BLISS["U+37a0"].append("cannula")
BLISS_TO_UNICODE["medical tube,catheter,cannula"] = ["U+37a0"]
UNICODE_TO_BLISS["U+37a0"].append("medical tube,catheter,cannula")
BLISS_TO_UNICODE["carriage"].append("U+348d")
UNICODE_TO_BLISS["U+348d"].append("carriage")
BLISS_TO_UNICODE["railway car"] = ["U+348d"]
UNICODE_TO_BLISS["U+348d"].append("railway car")
BLISS_TO_UNICODE["vehicle,carriage,railway car"] = ["U+348d"]
UNICODE_TO_BLISS["U+348d"].append("vehicle,carriage,railway car")
BLISS_TO_UNICODE["bowel"].append("U+3890")
UNICODE_TO_BLISS["U+3890"].append("bowel")
BLISS_TO_UNICODE["gut"].append("U+3890")
UNICODE_TO_BLISS["U+3890"].append("gut")
BLISS_TO_UNICODE["cereal"].append("U+332f")
UNICODE_TO_BLISS["U+332f"].append("cereal")
BLISS_TO_UNICODE["grain,cereal"] = ["U+332f"]
UNICODE_TO_BLISS["U+332f"].append("grain,cereal")
BLISS_TO_UNICODE["van"] = ["U+3de8"]
UNICODE_TO_BLISS["U+3de8"] = ["van"]
BLISS_TO_UNICODE["minibus"] = ["U+3de8"]
UNICODE_TO_BLISS["U+3de8"].append("minibus")
BLISS_TO_UNICODE["van,minibus"] = ["U+3de8"]
UNICODE_TO_BLISS["U+3de8"].append("van,minibus")
BLISS_TO_UNICODE["hike"] = ["U+3de9"]
UNICODE_TO_BLISS["U+3de9"] = ["hike"]
BLISS_TO_UNICODE["hiking"] = ["U+3dea"]
UNICODE_TO_BLISS["U+3dea"] = ["hiking"]
BLISS_TO_UNICODE["Allah"] = ["U+3deb"]
UNICODE_TO_BLISS["U+3deb"] = ["Allah"]
BLISS_TO_UNICODE["ALLAH"] = ["U+3dec"]
UNICODE_TO_BLISS["U+3dec"] = ["ALLAH"]
BLISS_TO_UNICODE["guilt"] = ["U+3ded"]
UNICODE_TO_BLISS["U+3ded"] = ["guilt"]
BLISS_TO_UNICODE["soda pop"] = ["U+3dee"]
UNICODE_TO_BLISS["U+3dee"] = ["soda pop"]
BLISS_TO_UNICODE["pop"].append("U+3dee")
UNICODE_TO_BLISS["U+3dee"].append("pop")
BLISS_TO_UNICODE["soft drink"] = ["U+3dee"]
UNICODE_TO_BLISS["U+3dee"].append("soft drink")
BLISS_TO_UNICODE["soda pop,pop,soft drink"] = ["U+3dee"]
UNICODE_TO_BLISS["U+3dee"].append("soda pop,pop,soft drink")
BLISS_TO_UNICODE["no"].append("U+364b")
UNICODE_TO_BLISS["U+364b"].append("no")
BLISS_TO_UNICODE["without"].append("U+364b")
UNICODE_TO_BLISS["U+364b"].append("without")
BLISS_TO_UNICODE["minus,no,without"] = ["U+364b"]
UNICODE_TO_BLISS["U+364b"].append("minus,no,without")
BLISS_TO_UNICODE["domestic science"] = ["U+3def"]
UNICODE_TO_BLISS["U+3def"] = ["domestic science"]
BLISS_TO_UNICODE["home economics"] = ["U+3def"]
UNICODE_TO_BLISS["U+3def"].append("home economics")
BLISS_TO_UNICODE["domestic science,home economics"] = ["U+3def"]
UNICODE_TO_BLISS["U+3def"].append("domestic science,home economics")
BLISS_TO_UNICODE["house work"] = ["U+3df0"]
UNICODE_TO_BLISS["U+3df0"] = ["house work"]
BLISS_TO_UNICODE["housekeeping"] = ["U+3df1"]
UNICODE_TO_BLISS["U+3df1"] = ["housekeeping"]
BLISS_TO_UNICODE["housework"] = ["U+3df2"]
UNICODE_TO_BLISS["U+3df2"] = ["housework"]
BLISS_TO_UNICODE["prediction"] = ["U+3df3"]
UNICODE_TO_BLISS["U+3df3"] = ["prediction"]
BLISS_TO_UNICODE["lull"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("lull")
BLISS_TO_UNICODE["calm,lull"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("calm,lull")
BLISS_TO_UNICODE["contents"] = ["U+3383"]
UNICODE_TO_BLISS["U+3383"].append("contents")
BLISS_TO_UNICODE["goods,contents"] = ["U+3383"]
UNICODE_TO_BLISS["U+3383"].append("goods,contents")
BLISS_TO_UNICODE["Shavuot"] = ["U+3df4"]
UNICODE_TO_BLISS["U+3df4"] = ["Shavuot"]
BLISS_TO_UNICODE["Christianity"] = ["U+3df5"]
UNICODE_TO_BLISS["U+3df5"] = ["Christianity"]
BLISS_TO_UNICODE["necktie"] = ["U+37f6"]
UNICODE_TO_BLISS["U+37f6"].append("necktie")
BLISS_TO_UNICODE["tie,necktie"] = ["U+37f6"]
UNICODE_TO_BLISS["U+37f6"].append("tie,necktie")
BLISS_TO_UNICODE["silversmith"] = ["U+3df6"]
UNICODE_TO_BLISS["U+3df6"] = ["silversmith"]
BLISS_TO_UNICODE["alcoholism"] = ["U+3df7"]
UNICODE_TO_BLISS["U+3df7"] = ["alcoholism"]
BLISS_TO_UNICODE["alcohol addiction"] = ["U+3df7"]
UNICODE_TO_BLISS["U+3df7"].append("alcohol addiction")
BLISS_TO_UNICODE["alcoholism,alcohol addiction"] = ["U+3df7"]
UNICODE_TO_BLISS["U+3df7"].append("alcoholism,alcohol addiction")
BLISS_TO_UNICODE["alcohol abuse"] = ["U+3df8"]
UNICODE_TO_BLISS["U+3df8"] = ["alcohol abuse"]
BLISS_TO_UNICODE["alcohol addiction"].append("U+3df8")
UNICODE_TO_BLISS["U+3df8"].append("alcohol addiction")
BLISS_TO_UNICODE["alcohol abuse,alcohol addiction"] = ["U+3df8"]
UNICODE_TO_BLISS["U+3df8"].append("alcohol abuse,alcohol addiction")
BLISS_TO_UNICODE["podiatrist"] = ["U+3df9"]
UNICODE_TO_BLISS["U+3df9"] = ["podiatrist"]
BLISS_TO_UNICODE["chiropodist"] = ["U+3df9"]
UNICODE_TO_BLISS["U+3df9"].append("chiropodist")
BLISS_TO_UNICODE["podiatrist,chiropodist"] = ["U+3df9"]
UNICODE_TO_BLISS["U+3df9"].append("podiatrist,chiropodist")
BLISS_TO_UNICODE["broadcast"] = ["U+3dfa"]
UNICODE_TO_BLISS["U+3dfa"] = ["broadcast"]
BLISS_TO_UNICODE["transmit"] = ["U+3dfa"]
UNICODE_TO_BLISS["U+3dfa"].append("transmit")
BLISS_TO_UNICODE["broadcast,transmit"] = ["U+3dfa"]
UNICODE_TO_BLISS["U+3dfa"].append("broadcast,transmit")
BLISS_TO_UNICODE["cordless phone"] = ["U+3dfb"]
UNICODE_TO_BLISS["U+3dfb"] = ["cordless phone"]
BLISS_TO_UNICODE["drying room"] = ["U+3dfc"]
UNICODE_TO_BLISS["U+3dfc"] = ["drying room"]
BLISS_TO_UNICODE["drying chamber"] = ["U+3dfc"]
UNICODE_TO_BLISS["U+3dfc"].append("drying chamber")
BLISS_TO_UNICODE["drying room,drying chamber"] = ["U+3dfc"]
UNICODE_TO_BLISS["U+3dfc"].append("drying room,drying chamber")
BLISS_TO_UNICODE["bog"] = ["U+3216"]
UNICODE_TO_BLISS["U+3216"].append("bog")
BLISS_TO_UNICODE["marsh"] = ["U+3216"]
UNICODE_TO_BLISS["U+3216"].append("marsh")
BLISS_TO_UNICODE["swamp,bog,marsh"] = ["U+3216"]
UNICODE_TO_BLISS["U+3216"].append("swamp,bog,marsh")
BLISS_TO_UNICODE["foster home"] = ["U+3dfd"]
UNICODE_TO_BLISS["U+3dfd"] = ["foster home"]
BLISS_TO_UNICODE["landing gear"] = ["U+3dfe"]
UNICODE_TO_BLISS["U+3dfe"] = ["landing gear"]
BLISS_TO_UNICODE["glove"] = ["U+3dff"]
UNICODE_TO_BLISS["U+3dff"] = ["glove"]
BLISS_TO_UNICODE["mitt"] = ["U+3dff"]
UNICODE_TO_BLISS["U+3dff"].append("mitt")
BLISS_TO_UNICODE["mitten"] = ["U+3dff"]
UNICODE_TO_BLISS["U+3dff"].append("mitten")
BLISS_TO_UNICODE["cane"] = ["U+3e00"]
UNICODE_TO_BLISS["U+3e00"] = ["cane"]
BLISS_TO_UNICODE["stick"].append("U+3e00")
UNICODE_TO_BLISS["U+3e00"].append("stick")
BLISS_TO_UNICODE["walking stick"] = ["U+3e00"]
UNICODE_TO_BLISS["U+3e00"].append("walking stick")
BLISS_TO_UNICODE["cane,stick,walking stick"] = ["U+3e00"]
UNICODE_TO_BLISS["U+3e00"].append("cane,stick,walking stick")
BLISS_TO_UNICODE["nephew"] = ["U+3e01"]
UNICODE_TO_BLISS["U+3e01"] = ["nephew"]
BLISS_TO_UNICODE["thickness"].append("U+3de3")
UNICODE_TO_BLISS["U+3de3"].append("thickness")
BLISS_TO_UNICODE["fatness,thickness"] = ["U+3de3"]
UNICODE_TO_BLISS["U+3de3"].append("fatness,thickness")
BLISS_TO_UNICODE["city tour"] = ["U+3e02"]
UNICODE_TO_BLISS["U+3e02"] = ["city tour"]
BLISS_TO_UNICODE["village"] = ["U+3e03"]
UNICODE_TO_BLISS["U+3e03"] = ["village"]
BLISS_TO_UNICODE["geyser"] = ["U+3e04"]
UNICODE_TO_BLISS["U+3e04"] = ["geyser"]
BLISS_TO_UNICODE["biochemical product"] = ["U+3e05"]
UNICODE_TO_BLISS["U+3e05"] = ["biochemical product"]
BLISS_TO_UNICODE["organic compound"] = ["U+3e05"]
UNICODE_TO_BLISS["U+3e05"].append("organic compound")
BLISS_TO_UNICODE["biochemical product,organic compound"] = ["U+3e05"]
UNICODE_TO_BLISS["U+3e05"].append("biochemical product,organic compound")
BLISS_TO_UNICODE["synthetic fabric"] = ["U+3e06"]
UNICODE_TO_BLISS["U+3e06"] = ["synthetic fabric"]
BLISS_TO_UNICODE["geologist"] = ["U+3e07"]
UNICODE_TO_BLISS["U+3e07"] = ["geologist"]
BLISS_TO_UNICODE["Elul"] = ["U+3e08"]
UNICODE_TO_BLISS["U+3e08"] = ["Elul"]
BLISS_TO_UNICODE["personality"] = ["U+3e09"]
UNICODE_TO_BLISS["U+3e09"] = ["personality"]
BLISS_TO_UNICODE["cylinder for breathing"] = ["U+3e0a"]
UNICODE_TO_BLISS["U+3e0a"] = ["cylinder for breathing"]
BLISS_TO_UNICODE["breathing"] = ["U+3e0b"]
UNICODE_TO_BLISS["U+3e0b"] = ["breathing"]
BLISS_TO_UNICODE["steak"] = ["U+3e0c"]
UNICODE_TO_BLISS["U+3e0c"] = ["steak"]
BLISS_TO_UNICODE["steal"] = ["U+3e0d"]
UNICODE_TO_BLISS["U+3e0d"] = ["steal"]
BLISS_TO_UNICODE["to take"] = ["U+3e0e"]
UNICODE_TO_BLISS["U+3e0e"] = ["to take"]
BLISS_TO_UNICODE["manager"] = ["U+3e0f"]
UNICODE_TO_BLISS["U+3e0f"] = ["manager"]
BLISS_TO_UNICODE["secretary"] = ["U+3e0f"]
UNICODE_TO_BLISS["U+3e0f"].append("secretary")
BLISS_TO_UNICODE["manager,secretary"] = ["U+3e0f"]
UNICODE_TO_BLISS["U+3e0f"].append("manager,secretary")
BLISS_TO_UNICODE["fill"].append("U+390f")
UNICODE_TO_BLISS["U+390f"].append("fill")
BLISS_TO_UNICODE["fullness"] = ["U+390f"]
UNICODE_TO_BLISS["U+390f"].append("fullness")
BLISS_TO_UNICODE["filling,fill,fullness"] = ["U+390f"]
UNICODE_TO_BLISS["U+390f"].append("filling,fill,fullness")
BLISS_TO_UNICODE["uninhabited"] = ["U+3e10"]
UNICODE_TO_BLISS["U+3e10"] = ["uninhabited"]
BLISS_TO_UNICODE["lemonade"] = ["U+3e11"]
UNICODE_TO_BLISS["U+3e11"] = ["lemonade"]
BLISS_TO_UNICODE["termite"] = ["U+3e12"]
UNICODE_TO_BLISS["U+3e12"] = ["termite"]
BLISS_TO_UNICODE["tree or wood destruction"] = ["U+3e13"]
UNICODE_TO_BLISS["U+3e13"] = ["tree or wood destruction"]
BLISS_TO_UNICODE["diced meat"] = ["U+3634"]
UNICODE_TO_BLISS["U+3634"].append("diced meat")
BLISS_TO_UNICODE["chunks of meat"] = ["U+3634"]
UNICODE_TO_BLISS["U+3634"].append("chunks of meat")
BLISS_TO_UNICODE["Christian hope"] = ["U+3e14"]
UNICODE_TO_BLISS["U+3e14"] = ["Christian hope"]
BLISS_TO_UNICODE["unfold"] = ["U+3e15"]
UNICODE_TO_BLISS["U+3e15"] = ["unfold"]
BLISS_TO_UNICODE["unfolding"] = ["U+3e16"]
UNICODE_TO_BLISS["U+3e16"] = ["unfolding"]
BLISS_TO_UNICODE["horsehair"] = ["U+3e17"]
UNICODE_TO_BLISS["U+3e17"] = ["horsehair"]
BLISS_TO_UNICODE["kitchen"] = ["U+3e18"]
UNICODE_TO_BLISS["U+3e18"] = ["kitchen"]
BLISS_TO_UNICODE["climate"] = ["U+3e19"]
UNICODE_TO_BLISS["U+3e19"] = ["climate"]
BLISS_TO_UNICODE["speech therapist"] = ["U+3e1a"]
UNICODE_TO_BLISS["U+3e1a"] = ["speech therapist"]
BLISS_TO_UNICODE["ill"] = ["U+3ba6"]
UNICODE_TO_BLISS["U+3ba6"].append("ill")
BLISS_TO_UNICODE["sick,ill"] = ["U+3ba6"]
UNICODE_TO_BLISS["U+3ba6"].append("sick,ill")
BLISS_TO_UNICODE["hummus"] = ["U+3e1b"]
UNICODE_TO_BLISS["U+3e1b"] = ["hummus"]
BLISS_TO_UNICODE["cod"] = ["U+3e1c"]
UNICODE_TO_BLISS["U+3e1c"] = ["cod"]
BLISS_TO_UNICODE["pictograph of beard"] = ["U+3e1d"]
UNICODE_TO_BLISS["U+3e1d"] = ["pictograph of beard"]
BLISS_TO_UNICODE["receiver"] = ["U+3e1e"]
UNICODE_TO_BLISS["U+3e1e"] = ["receiver"]
BLISS_TO_UNICODE["dish"].append("U+3e1e")
UNICODE_TO_BLISS["U+3e1e"].append("dish")
BLISS_TO_UNICODE["receiver,dish"] = ["U+3e1e"]
UNICODE_TO_BLISS["U+3e1e"].append("receiver,dish")
BLISS_TO_UNICODE["selfish"] = ["U+3e1f"]
UNICODE_TO_BLISS["U+3e1f"] = ["selfish"]
BLISS_TO_UNICODE["self centred"] = ["U+3e1f"]
UNICODE_TO_BLISS["U+3e1f"].append("self centred")
BLISS_TO_UNICODE["self centered"] = ["U+3e1f"]
UNICODE_TO_BLISS["U+3e1f"].append("self centered")
BLISS_TO_UNICODE["egoistic"] = ["U+3e1f"]
UNICODE_TO_BLISS["U+3e1f"].append("egoistic")
BLISS_TO_UNICODE["egoistical"] = ["U+3e1f"]
UNICODE_TO_BLISS["U+3e1f"].append("egoistical")
BLISS_TO_UNICODE["egocentric"] = ["U+3e1f"]
UNICODE_TO_BLISS["U+3e1f"].append("egocentric")
BLISS_TO_UNICODE["selfish,self-centred,self-centered,egoistic,egoistical,egocentric"] = ["U+3e1f"]
UNICODE_TO_BLISS["U+3e1f"].append("selfish,self-centred,self-centered,egoistic,egoistical,egocentric")
BLISS_TO_UNICODE["sweet drink"] = ["U+3e20"]
UNICODE_TO_BLISS["U+3e20"] = ["sweet drink"]
BLISS_TO_UNICODE["Ireland"] = ["U+3e21"]
UNICODE_TO_BLISS["U+3e21"] = ["Ireland"]
BLISS_TO_UNICODE["alertness"].append("U+3b70")
UNICODE_TO_BLISS["U+3b70"].append("alertness")
BLISS_TO_UNICODE["wakefulness,alertness"] = ["U+3b70"]
UNICODE_TO_BLISS["U+3b70"].append("wakefulness,alertness")
BLISS_TO_UNICODE["in love"] = ["U+3e22"]
UNICODE_TO_BLISS["U+3e22"] = ["in love"]
BLISS_TO_UNICODE["matching game"] = ["U+3e23"]
UNICODE_TO_BLISS["U+3e23"] = ["matching game"]
BLISS_TO_UNICODE["one storey home"] = ["U+3e24"]
UNICODE_TO_BLISS["U+3e24"] = ["one storey home"]
BLISS_TO_UNICODE["easy"] = ["U+3e25"]
UNICODE_TO_BLISS["U+3e25"] = ["easy"]
BLISS_TO_UNICODE["easily"] = ["U+3e25"]
UNICODE_TO_BLISS["U+3e25"].append("easily")
BLISS_TO_UNICODE["easy,easily"] = ["U+3e25"]
UNICODE_TO_BLISS["U+3e25"].append("easy,easily")
BLISS_TO_UNICODE["general practitioner"] = ["U+3e26"]
UNICODE_TO_BLISS["U+3e26"] = ["general practitioner"]
BLISS_TO_UNICODE["all knowing"] = ["U+3e27"]
UNICODE_TO_BLISS["U+3e27"] = ["all knowing"]
BLISS_TO_UNICODE["physician"] = ["U+35d1"]
UNICODE_TO_BLISS["U+35d1"].append("physician")
BLISS_TO_UNICODE["doctor,physician"] = ["U+35d1"]
UNICODE_TO_BLISS["U+35d1"].append("doctor,physician")
BLISS_TO_UNICODE["suddenly"] = ["U+3e28"]
UNICODE_TO_BLISS["U+3e28"] = ["suddenly"]
BLISS_TO_UNICODE["abrupt"] = ["U+3e28"]
UNICODE_TO_BLISS["U+3e28"].append("abrupt")
BLISS_TO_UNICODE["sudden"] = ["U+3e28"]
UNICODE_TO_BLISS["U+3e28"].append("sudden")
BLISS_TO_UNICODE["suddenly,abrupt,sudden"] = ["U+3e28"]
UNICODE_TO_BLISS["U+3e28"].append("suddenly,abrupt,sudden")
BLISS_TO_UNICODE["ear mold"] = ["U+3e29"]
UNICODE_TO_BLISS["U+3e29"] = ["ear mold"]
BLISS_TO_UNICODE["aid"].append("U+3524")
UNICODE_TO_BLISS["U+3524"].append("aid")
BLISS_TO_UNICODE["assistance"] = ["U+3524"]
UNICODE_TO_BLISS["U+3524"].append("assistance")
BLISS_TO_UNICODE["support"].append("U+3524")
UNICODE_TO_BLISS["U+3524"].append("support")
BLISS_TO_UNICODE["help,aid,assistance,support"] = ["U+3524"]
UNICODE_TO_BLISS["U+3524"].append("help,aid,assistance,support")
BLISS_TO_UNICODE["assist"] = ["U+3524"]
UNICODE_TO_BLISS["U+3524"].append("assist")
BLISS_TO_UNICODE["serve"] = ["U+3524"]
UNICODE_TO_BLISS["U+3524"].append("serve")
BLISS_TO_UNICODE["help,aid,assist,serve,support"] = ["U+3524"]
UNICODE_TO_BLISS["U+3524"].append("help,aid,assist,serve,support")
BLISS_TO_UNICODE["voice"] = ["U+3e2a"]
UNICODE_TO_BLISS["U+3e2a"] = ["voice"]
BLISS_TO_UNICODE["usually do"] = ["U+3e2b"]
UNICODE_TO_BLISS["U+3e2b"] = ["usually do"]
BLISS_TO_UNICODE["habitually do"] = ["U+3e2b"]
UNICODE_TO_BLISS["U+3e2b"].append("habitually do")
BLISS_TO_UNICODE["usually do,habitually do"] = ["U+3e2b"]
UNICODE_TO_BLISS["U+3e2b"].append("usually do,habitually do")
BLISS_TO_UNICODE["can"].append("U+3b4f")
UNICODE_TO_BLISS["U+3b4f"].append("can")
BLISS_TO_UNICODE["cylinder,can"] = ["U+3b4f"]
UNICODE_TO_BLISS["U+3b4f"].append("cylinder,can")
BLISS_TO_UNICODE["dizzy"] = ["U+3e2c"]
UNICODE_TO_BLISS["U+3e2c"] = ["dizzy"]
BLISS_TO_UNICODE["brake"] = ["U+3e2d"]
UNICODE_TO_BLISS["U+3e2d"] = ["brake"]
BLISS_TO_UNICODE["to move"] = ["U+3e2e"]
UNICODE_TO_BLISS["U+3e2e"] = ["to move"]
BLISS_TO_UNICODE["conifer cone"] = ["U+33f9"]
UNICODE_TO_BLISS["U+33f9"].append("conifer cone")
BLISS_TO_UNICODE["strobilus"] = ["U+33f9"]
UNICODE_TO_BLISS["U+33f9"].append("strobilus")
BLISS_TO_UNICODE["cone,conifer cone,strobilus"] = ["U+33f9"]
UNICODE_TO_BLISS["U+33f9"].append("cone,conifer cone,strobilus")
BLISS_TO_UNICODE["dump truck"] = ["U+3e2f"]
UNICODE_TO_BLISS["U+3e2f"] = ["dump truck"]
BLISS_TO_UNICODE["dumper"] = ["U+3e2f"]
UNICODE_TO_BLISS["U+3e2f"].append("dumper")
BLISS_TO_UNICODE["tipper lorry"] = ["U+3e2f"]
UNICODE_TO_BLISS["U+3e2f"].append("tipper lorry")
BLISS_TO_UNICODE["tipper"] = ["U+3e2f"]
UNICODE_TO_BLISS["U+3e2f"].append("tipper")
BLISS_TO_UNICODE["dump truck,dumper,tipper lorry,tipper"] = ["U+3e2f"]
UNICODE_TO_BLISS["U+3e2f"].append("dump truck,dumper,tipper lorry,tipper")
BLISS_TO_UNICODE["perform"] = ["U+3e30"]
UNICODE_TO_BLISS["U+3e30"] = ["perform"]
BLISS_TO_UNICODE["performance"] = ["U+3e31"]
UNICODE_TO_BLISS["U+3e31"] = ["performance"]
BLISS_TO_UNICODE["water ice lollipop"] = ["U+3e32"]
UNICODE_TO_BLISS["U+3e32"] = ["water ice lollipop"]
BLISS_TO_UNICODE["baking powder"] = ["U+3e33"]
UNICODE_TO_BLISS["U+3e33"] = ["baking powder"]
BLISS_TO_UNICODE["independent"] = ["U+3e34"]
UNICODE_TO_BLISS["U+3e34"] = ["independent"]
BLISS_TO_UNICODE["hang"] = ["U+3e35"]
UNICODE_TO_BLISS["U+3e35"] = ["hang"]
BLISS_TO_UNICODE["hook"].append("U+3e35")
UNICODE_TO_BLISS["U+3e35"].append("hook")
BLISS_TO_UNICODE["hang,hook"] = ["U+3e35"]
UNICODE_TO_BLISS["U+3e35"].append("hang,hook")
BLISS_TO_UNICODE["fuse"] = ["U+3e36"]
UNICODE_TO_BLISS["U+3e36"] = ["fuse"]
BLISS_TO_UNICODE["rootage"] = ["U+3aca"]
UNICODE_TO_BLISS["U+3aca"].append("rootage")
BLISS_TO_UNICODE["root system"] = ["U+3aca"]
UNICODE_TO_BLISS["U+3aca"].append("root system")
BLISS_TO_UNICODE["humble"] = ["U+3e37"]
UNICODE_TO_BLISS["U+3e37"] = ["humble"]
BLISS_TO_UNICODE["meek"] = ["U+3e37"]
UNICODE_TO_BLISS["U+3e37"].append("meek")
BLISS_TO_UNICODE["humble,meek"] = ["U+3e37"]
UNICODE_TO_BLISS["U+3e37"].append("humble,meek")
BLISS_TO_UNICODE["inferior"] = ["U+3e38"]
UNICODE_TO_BLISS["U+3e38"] = ["inferior"]
BLISS_TO_UNICODE["talcum powder"] = ["U+3e39"]
UNICODE_TO_BLISS["U+3e39"] = ["talcum powder"]
BLISS_TO_UNICODE["diagonal line suggests an index finger pointing at something specific. The diagonal line has the same orientation as the one used in this and that."] = ["U+3e3a"]
UNICODE_TO_BLISS["U+3e3a"] = ["diagonal line suggests an index finger pointing at something specific. The diagonal line has the same orientation as the one used in this and that."]
BLISS_TO_UNICODE["musical"] = ["U+3e3b"]
UNICODE_TO_BLISS["U+3e3b"] = ["musical"]
BLISS_TO_UNICODE["indigo"] = ["U+3e3c"]
UNICODE_TO_BLISS["U+3e3c"] = ["indigo"]
BLISS_TO_UNICODE["photograph"] = ["U+3e3d"]
UNICODE_TO_BLISS["U+3e3d"] = ["photograph"]
BLISS_TO_UNICODE["photo"] = ["U+3e3d"]
UNICODE_TO_BLISS["U+3e3d"].append("photo")
BLISS_TO_UNICODE["pic"] = ["U+3e3d"]
UNICODE_TO_BLISS["U+3e3d"].append("pic")
BLISS_TO_UNICODE["photograph,photo,pic"] = ["U+3e3d"]
UNICODE_TO_BLISS["U+3e3d"].append("photograph,photo,pic")
BLISS_TO_UNICODE["smoking pipe"] = ["U+32bc"]
UNICODE_TO_BLISS["U+32bc"].append("smoking pipe")
BLISS_TO_UNICODE["pipe,smoking pipe"] = ["U+32bc"]
UNICODE_TO_BLISS["U+32bc"].append("pipe,smoking pipe")
BLISS_TO_UNICODE["thank you"] = ["U+3ccb"]
UNICODE_TO_BLISS["U+3ccb"].append("thank you")
BLISS_TO_UNICODE["thanks,thank you"] = ["U+3ccb"]
UNICODE_TO_BLISS["U+3ccb"].append("thanks,thank you")
BLISS_TO_UNICODE["stepdaughter"] = ["U+3e3e"]
UNICODE_TO_BLISS["U+3e3e"] = ["stepdaughter"]
BLISS_TO_UNICODE["step-parent"] = ["U+3e3f"]
UNICODE_TO_BLISS["U+3e3f"] = ["step-parent"]
BLISS_TO_UNICODE["cervix"] = ["U+3e40"]
UNICODE_TO_BLISS["U+3e40"] = ["cervix"]
BLISS_TO_UNICODE["starboard"] = ["U+3e41"]
UNICODE_TO_BLISS["U+3e41"] = ["starboard"]
BLISS_TO_UNICODE["passive"] = ["U+3e42"]
UNICODE_TO_BLISS["U+3e42"] = ["passive"]
BLISS_TO_UNICODE["passivity"] = ["U+3e43"]
UNICODE_TO_BLISS["U+3e43"] = ["passivity"]
BLISS_TO_UNICODE["shout"] = ["U+3e44"]
UNICODE_TO_BLISS["U+3e44"] = ["shout"]
BLISS_TO_UNICODE["two intensity symbols"] = ["U+3e45"]
UNICODE_TO_BLISS["U+3e45"] = ["two intensity symbols"]
BLISS_TO_UNICODE["paste"].append("U+32a3")
UNICODE_TO_BLISS["U+32a3"].append("paste")
BLISS_TO_UNICODE["spread,paste"] = ["U+32a3"]
UNICODE_TO_BLISS["U+32a3"].append("spread,paste")
BLISS_TO_UNICODE["ski boot"] = ["U+3e46"]
UNICODE_TO_BLISS["U+3e46"] = ["ski boot"]
BLISS_TO_UNICODE["ski pole"] = ["U+3e47"]
UNICODE_TO_BLISS["U+3e47"] = ["ski pole"]
BLISS_TO_UNICODE["Alice"] = ["U+3e48"]
UNICODE_TO_BLISS["U+3e48"] = ["Alice"]
BLISS_TO_UNICODE["blissname"] = ["U+3e49"]
UNICODE_TO_BLISS["U+3e49"] = ["blissname"]
BLISS_TO_UNICODE["double bassoon"] = ["U+3e4a"]
UNICODE_TO_BLISS["U+3e4a"] = ["double bassoon"]
BLISS_TO_UNICODE["fingerspell"] = ["U+3e4b"]
UNICODE_TO_BLISS["U+3e4b"] = ["fingerspell"]
BLISS_TO_UNICODE["thermos"] = ["U+3e4c"]
UNICODE_TO_BLISS["U+3e4c"] = ["thermos"]
BLISS_TO_UNICODE["cooler"] = ["U+3e4c"]
UNICODE_TO_BLISS["U+3e4c"].append("cooler")
BLISS_TO_UNICODE["flask"] = ["U+3e4c"]
UNICODE_TO_BLISS["U+3e4c"].append("flask")
BLISS_TO_UNICODE["thermos,cooler,flask"] = ["U+3e4c"]
UNICODE_TO_BLISS["U+3e4c"].append("thermos,cooler,flask")
BLISS_TO_UNICODE["security"] = ["U+3dc5"]
UNICODE_TO_BLISS["U+3dc5"].append("security")
BLISS_TO_UNICODE["safety,security"] = ["U+3dc5"]
UNICODE_TO_BLISS["U+3dc5"].append("safety,security")
BLISS_TO_UNICODE["starvation"] = ["U+3e4d"]
UNICODE_TO_BLISS["U+3e4d"] = ["starvation"]
BLISS_TO_UNICODE["Bangladesh"] = ["U+3e4e"]
UNICODE_TO_BLISS["U+3e4e"] = ["Bangladesh"]
BLISS_TO_UNICODE["tiger"] = ["U+3e4f"]
UNICODE_TO_BLISS["U+3e4f"] = ["tiger"]
BLISS_TO_UNICODE["collarbone"] = ["U+3e50"]
UNICODE_TO_BLISS["U+3e50"] = ["collarbone"]
BLISS_TO_UNICODE["clavicle"] = ["U+3e50"]
UNICODE_TO_BLISS["U+3e50"].append("clavicle")
BLISS_TO_UNICODE["collarbone,clavicle"] = ["U+3e50"]
UNICODE_TO_BLISS["U+3e50"].append("collarbone,clavicle")
BLISS_TO_UNICODE["congratulate"] = ["U+3e51"]
UNICODE_TO_BLISS["U+3e51"] = ["congratulate"]
BLISS_TO_UNICODE["purple"] = ["U+3e52"]
UNICODE_TO_BLISS["U+3e52"] = ["purple"]
BLISS_TO_UNICODE["violet"] = ["U+3e52"]
UNICODE_TO_BLISS["U+3e52"].append("violet")
BLISS_TO_UNICODE["purple,violet"] = ["U+3e52"]
UNICODE_TO_BLISS["U+3e52"].append("purple,violet")
BLISS_TO_UNICODE["7"] = ["U+3e53"]
UNICODE_TO_BLISS["U+3e53"] = ["7"]
BLISS_TO_UNICODE["Leo"] = ["U+3e54"]
UNICODE_TO_BLISS["U+3e54"] = ["Leo"]
BLISS_TO_UNICODE["lion"] = ["U+3e55"]
UNICODE_TO_BLISS["U+3e55"] = ["lion"]
BLISS_TO_UNICODE["Shevat"] = ["U+3e56"]
UNICODE_TO_BLISS["U+3e56"] = ["Shevat"]
BLISS_TO_UNICODE["Shvat"] = ["U+3e56"]
UNICODE_TO_BLISS["U+3e56"].append("Shvat")
BLISS_TO_UNICODE["Shevat,Shvat"] = ["U+3e56"]
UNICODE_TO_BLISS["U+3e56"].append("Shevat,Shvat")
BLISS_TO_UNICODE["involvement"] = ["U+36df"]
UNICODE_TO_BLISS["U+36df"].append("involvement")
BLISS_TO_UNICODE["participation,involvement"] = ["U+36df"]
UNICODE_TO_BLISS["U+36df"].append("participation,involvement")
BLISS_TO_UNICODE["play football"] = ["U+3e57"]
UNICODE_TO_BLISS["U+3e57"] = ["play football"]
BLISS_TO_UNICODE["peel"] = ["U+3e59"]
UNICODE_TO_BLISS["U+3e59"] = ["peel"]
BLISS_TO_UNICODE["deflation"] = ["U+3e5a"]
UNICODE_TO_BLISS["U+3e5a"] = ["deflation"]
BLISS_TO_UNICODE["illustration"] = ["U+3e5b"]
UNICODE_TO_BLISS["U+3e5b"] = ["illustration"]
BLISS_TO_UNICODE["substitution"] = ["U+3234"]
UNICODE_TO_BLISS["U+3234"].append("substitution")
BLISS_TO_UNICODE["exchange,substitution"] = ["U+3234"]
UNICODE_TO_BLISS["U+3234"].append("exchange,substitution")
BLISS_TO_UNICODE["mail,post"] = ["U+3586"]
UNICODE_TO_BLISS["U+3586"].append("mail,post")
BLISS_TO_UNICODE["filled vegetable"] = ["U+3e5c"]
UNICODE_TO_BLISS["U+3e5c"] = ["filled vegetable"]
BLISS_TO_UNICODE["stuffed vegetable"] = ["U+3e5c"]
UNICODE_TO_BLISS["U+3e5c"].append("stuffed vegetable")
BLISS_TO_UNICODE["filled vegetable,stuffed vegetable"] = ["U+3e5c"]
UNICODE_TO_BLISS["U+3e5c"].append("filled vegetable,stuffed vegetable")
BLISS_TO_UNICODE["coral"] = ["U+3e5d"]
UNICODE_TO_BLISS["U+3e5d"] = ["coral"]
BLISS_TO_UNICODE["visa"] = ["U+3e5e"]
UNICODE_TO_BLISS["U+3e5e"] = ["visa"]
BLISS_TO_UNICODE["early morning"] = ["U+3e5f"]
UNICODE_TO_BLISS["U+3e5f"] = ["early morning"]
BLISS_TO_UNICODE["leprechaun"] = ["U+3e60"]
UNICODE_TO_BLISS["U+3e60"] = ["leprechaun"]
BLISS_TO_UNICODE["little person"] = ["U+3e61"]
UNICODE_TO_BLISS["U+3e61"] = ["little person"]
BLISS_TO_UNICODE["octopus"] = ["U+3e62"]
UNICODE_TO_BLISS["U+3e62"] = ["octopus"]
BLISS_TO_UNICODE["croak"] = ["U+3e63"]
UNICODE_TO_BLISS["U+3e63"] = ["croak"]
BLISS_TO_UNICODE["frog"] = ["U+3e64"]
UNICODE_TO_BLISS["U+3e64"] = ["frog"]
BLISS_TO_UNICODE["glass material"] = ["U+3e65"]
UNICODE_TO_BLISS["U+3e65"] = ["glass material"]
BLISS_TO_UNICODE["Icelandic"] = ["U+3e66"]
UNICODE_TO_BLISS["U+3e66"] = ["Icelandic"]
BLISS_TO_UNICODE["dilemma"] = ["U+3e67"]
UNICODE_TO_BLISS["U+3e67"] = ["dilemma"]
BLISS_TO_UNICODE["green onion"] = ["U+3e68"]
UNICODE_TO_BLISS["U+3e68"] = ["green onion"]
BLISS_TO_UNICODE["scallion"] = ["U+3e68"]
UNICODE_TO_BLISS["U+3e68"].append("scallion")
BLISS_TO_UNICODE["spring onion"] = ["U+3e68"]
UNICODE_TO_BLISS["U+3e68"].append("spring onion")
BLISS_TO_UNICODE["green onion,scallion,spring onion"] = ["U+3e68"]
UNICODE_TO_BLISS["U+3e68"].append("green onion,scallion,spring onion")
BLISS_TO_UNICODE["floating container"] = ["U+3e69"]
UNICODE_TO_BLISS["U+3e69"] = ["floating container"]
BLISS_TO_UNICODE["profession"] = ["U+35f0"]
UNICODE_TO_BLISS["U+35f0"].append("profession")
BLISS_TO_UNICODE["career"] = ["U+35f0"]
UNICODE_TO_BLISS["U+35f0"].append("career")
BLISS_TO_UNICODE["calling,profession,career"] = ["U+35f0"]
UNICODE_TO_BLISS["U+35f0"].append("calling,profession,career")
BLISS_TO_UNICODE["intellectual impairment"] = ["U+3e6a"]
UNICODE_TO_BLISS["U+3e6a"] = ["intellectual impairment"]
BLISS_TO_UNICODE["cognitive impairment"] = ["U+3e6a"]
UNICODE_TO_BLISS["U+3e6a"].append("cognitive impairment")
BLISS_TO_UNICODE["mental impairment"] = ["U+3e6a"]
UNICODE_TO_BLISS["U+3e6a"].append("mental impairment")
BLISS_TO_UNICODE["intellectual impairment,cognitive impairment,mental impairment"] = ["U+3e6a"]
UNICODE_TO_BLISS["U+3e6a"].append("intellectual impairment,cognitive impairment,mental impairment")
BLISS_TO_UNICODE["compression"] = ["U+3e6b"]
UNICODE_TO_BLISS["U+3e6b"] = ["compression"]
BLISS_TO_UNICODE["compressing"] = ["U+3e6b"]
UNICODE_TO_BLISS["U+3e6b"].append("compressing")
BLISS_TO_UNICODE["squeezing"] = ["U+3e6b"]
UNICODE_TO_BLISS["U+3e6b"].append("squeezing")
BLISS_TO_UNICODE["compression,compressing,squeezing"] = ["U+3e6b"]
UNICODE_TO_BLISS["U+3e6b"].append("compression,compressing,squeezing")
BLISS_TO_UNICODE["combat"] = ["U+351a"]
UNICODE_TO_BLISS["U+351a"].append("combat")
BLISS_TO_UNICODE["fight,combat"] = ["U+351a"]
UNICODE_TO_BLISS["U+351a"].append("fight,combat")
BLISS_TO_UNICODE["way"] = ["U+3e6c"]
UNICODE_TO_BLISS["U+3e6c"] = ["way"]
BLISS_TO_UNICODE["knife sword"] = ["U+3e6d"]
UNICODE_TO_BLISS["U+3e6d"] = ["knife sword"]
BLISS_TO_UNICODE["satellite signal"] = ["U+3e6e"]
UNICODE_TO_BLISS["U+3e6e"] = ["satellite signal"]
BLISS_TO_UNICODE["discuss"] = ["U+3e6f"]
UNICODE_TO_BLISS["U+3e6f"] = ["discuss"]
BLISS_TO_UNICODE["converse"] = ["U+3e6f"]
UNICODE_TO_BLISS["U+3e6f"].append("converse")
BLISS_TO_UNICODE["debate"].append("U+3e6f")
UNICODE_TO_BLISS["U+3e6f"].append("debate")
BLISS_TO_UNICODE["discuss,converse,debate"] = ["U+3e6f"]
UNICODE_TO_BLISS["U+3e6f"].append("discuss,converse,debate")
BLISS_TO_UNICODE["throw"] = ["U+3e70"]
UNICODE_TO_BLISS["U+3e70"] = ["throw"]
BLISS_TO_UNICODE["road sign"] = ["U+3e71"]
UNICODE_TO_BLISS["U+3e71"] = ["road sign"]
BLISS_TO_UNICODE["absorbent material"] = ["U+3e72"]
UNICODE_TO_BLISS["U+3e72"] = ["absorbent material"]
BLISS_TO_UNICODE["sponge"] = ["U+3e72"]
UNICODE_TO_BLISS["U+3e72"].append("sponge")
BLISS_TO_UNICODE["absorbent material,sponge"] = ["U+3e72"]
UNICODE_TO_BLISS["U+3e72"].append("absorbent material,sponge")
BLISS_TO_UNICODE["maximum"] = ["U+34b9"]
UNICODE_TO_BLISS["U+34b9"].append("maximum")
BLISS_TO_UNICODE["most,maximum"] = ["U+34b9"]
UNICODE_TO_BLISS["U+34b9"].append("most,maximum")
BLISS_TO_UNICODE["superlative most"] = ["U+3e73"]
UNICODE_TO_BLISS["U+3e73"] = ["superlative most"]
BLISS_TO_UNICODE["veterinarian"] = ["U+3e74"]
UNICODE_TO_BLISS["U+3e74"] = ["veterinarian"]
BLISS_TO_UNICODE["evidence"] = ["U+3e75"]
UNICODE_TO_BLISS["U+3e75"] = ["evidence"]
BLISS_TO_UNICODE["manure"] = ["U+3e76"]
UNICODE_TO_BLISS["U+3e76"] = ["manure"]
BLISS_TO_UNICODE["fertilizer"] = ["U+3e76"]
UNICODE_TO_BLISS["U+3e76"].append("fertilizer")
BLISS_TO_UNICODE["manure,fertilizer"] = ["U+3e76"]
UNICODE_TO_BLISS["U+3e76"].append("manure,fertilizer")
BLISS_TO_UNICODE["Ascension Day"] = ["U+3e77"]
UNICODE_TO_BLISS["U+3e77"] = ["Ascension Day"]
BLISS_TO_UNICODE["Ascension"] = ["U+3e78"]
UNICODE_TO_BLISS["U+3e78"] = ["Ascension"]
BLISS_TO_UNICODE["cocoa"] = ["U+3604"]
UNICODE_TO_BLISS["U+3604"].append("cocoa")
BLISS_TO_UNICODE["cacao"] = ["U+3604"]
UNICODE_TO_BLISS["U+3604"].append("cacao")
BLISS_TO_UNICODE["chocolate,cocoa,cacao"] = ["U+3604"]
UNICODE_TO_BLISS["U+3604"].append("chocolate,cocoa,cacao")
BLISS_TO_UNICODE["baguette"] = ["U+3e79"]
UNICODE_TO_BLISS["U+3e79"] = ["baguette"]
BLISS_TO_UNICODE["pressure gauge"] = ["U+3e7a"]
UNICODE_TO_BLISS["U+3e7a"] = ["pressure gauge"]
BLISS_TO_UNICODE["Pterosaur"] = ["U+3e7b"]
UNICODE_TO_BLISS["U+3e7b"] = ["Pterosaur"]
BLISS_TO_UNICODE["Pterodactyl"] = ["U+3e7b"]
UNICODE_TO_BLISS["U+3e7b"].append("Pterodactyl")
BLISS_TO_UNICODE["Pterosaur,Pterodactyl"] = ["U+3e7b"]
UNICODE_TO_BLISS["U+3e7b"].append("Pterosaur,Pterodactyl")
BLISS_TO_UNICODE["flute"] = ["U+3e7c"]
UNICODE_TO_BLISS["U+3e7c"] = ["flute"]
BLISS_TO_UNICODE["recorder"] = ["U+3e7d"]
UNICODE_TO_BLISS["U+3e7d"] = ["recorder"]
BLISS_TO_UNICODE["reed"] = ["U+3e7e"]
UNICODE_TO_BLISS["U+3e7e"] = ["reed"]
BLISS_TO_UNICODE["reality"] = ["U+3e7f"]
UNICODE_TO_BLISS["U+3e7f"] = ["reality"]
BLISS_TO_UNICODE["interested"] = ["U+3c73"]
UNICODE_TO_BLISS["U+3c73"].append("interested")
BLISS_TO_UNICODE["interesting,interested"] = ["U+3c73"]
UNICODE_TO_BLISS["U+3c73"].append("interesting,interested")
BLISS_TO_UNICODE["holding"] = ["U+3e80"]
UNICODE_TO_BLISS["U+3e80"] = ["holding"]
BLISS_TO_UNICODE["test"] = ["U+3e81"]
UNICODE_TO_BLISS["U+3e81"] = ["test"]
BLISS_TO_UNICODE["assessment"] = ["U+3e81"]
UNICODE_TO_BLISS["U+3e81"].append("assessment")
BLISS_TO_UNICODE["exam"] = ["U+3e81"]
UNICODE_TO_BLISS["U+3e81"].append("exam")
BLISS_TO_UNICODE["test,assessment,exam"] = ["U+3e81"]
UNICODE_TO_BLISS["U+3e81"].append("test,assessment,exam")
BLISS_TO_UNICODE["common cold"] = ["U+3424"]
UNICODE_TO_BLISS["U+3424"].append("common cold")
BLISS_TO_UNICODE["cold,common cold"] = ["U+3424"]
UNICODE_TO_BLISS["U+3424"].append("cold,common cold")
BLISS_TO_UNICODE["alpana"] = ["U+3e82"]
UNICODE_TO_BLISS["U+3e82"] = ["alpana"]
BLISS_TO_UNICODE["rangoli"] = ["U+3e82"]
UNICODE_TO_BLISS["U+3e82"].append("rangoli")
BLISS_TO_UNICODE["alpana,rangoli"] = ["U+3e82"]
UNICODE_TO_BLISS["U+3e82"].append("alpana,rangoli")
BLISS_TO_UNICODE["o'clock"] = ["U+39f1"]
UNICODE_TO_BLISS["U+39f1"].append("o'clock")
BLISS_TO_UNICODE["hour,o'clock"] = ["U+39f1"]
UNICODE_TO_BLISS["U+39f1"].append("hour,o'clock")
BLISS_TO_UNICODE["degree"] = ["U+3e83"]
UNICODE_TO_BLISS["U+3e83"] = ["degree"]
BLISS_TO_UNICODE[" to indicate an hour"] = ["U+3e84"]
UNICODE_TO_BLISS["U+3e84"] = [" to indicate an hour"]
BLISS_TO_UNICODE["welcome"] = ["U+3e85"]
UNICODE_TO_BLISS["U+3e85"] = ["welcome"]
BLISS_TO_UNICODE["Koran"] = ["U+3e86"]
UNICODE_TO_BLISS["U+3e86"] = ["Koran"]
BLISS_TO_UNICODE["reception"] = ["U+3e87"]
UNICODE_TO_BLISS["U+3e87"] = ["reception"]
BLISS_TO_UNICODE["dance"] = ["U+3e88"]
UNICODE_TO_BLISS["U+3e88"] = ["dance"]
BLISS_TO_UNICODE["dancing"] = ["U+3e88"]
UNICODE_TO_BLISS["U+3e88"].append("dancing")
BLISS_TO_UNICODE["dance,dancing"] = ["U+3e88"]
UNICODE_TO_BLISS["U+3e88"].append("dance,dancing")
BLISS_TO_UNICODE["devoted"] = ["U+3e89"]
UNICODE_TO_BLISS["U+3e89"] = ["devoted"]
BLISS_TO_UNICODE["devotee"] = ["U+3e8a"]
UNICODE_TO_BLISS["U+3e8a"] = ["devotee"]
BLISS_TO_UNICODE["fan"].append("U+3e8a")
UNICODE_TO_BLISS["U+3e8a"].append("fan")
BLISS_TO_UNICODE["devotee,fan"] = ["U+3e8a"]
UNICODE_TO_BLISS["U+3e8a"].append("devotee,fan")
BLISS_TO_UNICODE["flask"].append("U+34ed")
UNICODE_TO_BLISS["U+34ed"].append("flask")
BLISS_TO_UNICODE["bottle,flask"] = ["U+34ed"]
UNICODE_TO_BLISS["U+34ed"].append("bottle,flask")
BLISS_TO_UNICODE["splurge"] = ["U+3e8b"]
UNICODE_TO_BLISS["U+3e8b"] = ["splurge"]
BLISS_TO_UNICODE["spending"] = ["U+3e8c"]
UNICODE_TO_BLISS["U+3e8c"] = ["spending"]
BLISS_TO_UNICODE["panic"].append("U+3d0c")
UNICODE_TO_BLISS["U+3d0c"].append("panic")
BLISS_TO_UNICODE["terror,panic"] = ["U+3d0c"]
UNICODE_TO_BLISS["U+3d0c"].append("terror,panic")
BLISS_TO_UNICODE["brown"] = ["U+3e8d"]
UNICODE_TO_BLISS["U+3e8d"] = ["brown"]
BLISS_TO_UNICODE["0"] = ["U+3e8e"]
UNICODE_TO_BLISS["U+3e8e"] = ["0"]
BLISS_TO_UNICODE["personal measurement"] = ["U+3e8f"]
UNICODE_TO_BLISS["U+3e8f"] = ["personal measurement"]
BLISS_TO_UNICODE["Formula One"] = ["U+3e90"]
UNICODE_TO_BLISS["U+3e90"] = ["Formula One"]
BLISS_TO_UNICODE["NASCAR Kart"] = ["U+3e90"]
UNICODE_TO_BLISS["U+3e90"].append("NASCAR Kart")
BLISS_TO_UNICODE["Formula One,NASCAR Kart"] = ["U+3e90"]
UNICODE_TO_BLISS["U+3e90"].append("Formula One,NASCAR Kart")
BLISS_TO_UNICODE["brownie"] = ["U+3e91"]
UNICODE_TO_BLISS["U+3e91"] = ["brownie"]
BLISS_TO_UNICODE["house elf"] = ["U+3e91"]
UNICODE_TO_BLISS["U+3e91"].append("house elf")
BLISS_TO_UNICODE["brownie,house elf"] = ["U+3e91"]
UNICODE_TO_BLISS["U+3e91"].append("brownie,house elf")
BLISS_TO_UNICODE["sunbathe"] = ["U+3e92"]
UNICODE_TO_BLISS["U+3e92"] = ["sunbathe"]
BLISS_TO_UNICODE["to rest"] = ["U+3e93"]
UNICODE_TO_BLISS["U+3e93"] = ["to rest"]
BLISS_TO_UNICODE["kitten"] = ["U+3e94"]
UNICODE_TO_BLISS["U+3e94"] = ["kitten"]
BLISS_TO_UNICODE["cat"] = ["U+3e95"]
UNICODE_TO_BLISS["U+3e95"] = ["cat"]
BLISS_TO_UNICODE["select all"] = ["U+3e96"]
UNICODE_TO_BLISS["U+3e96"] = ["select all"]
BLISS_TO_UNICODE["mark all"] = ["U+3e96"]
UNICODE_TO_BLISS["U+3e96"].append("mark all")
BLISS_TO_UNICODE["select all,mark all"] = ["U+3e96"]
UNICODE_TO_BLISS["U+3e96"].append("select all,mark all")
BLISS_TO_UNICODE["to select"] = ["U+3e97"]
UNICODE_TO_BLISS["U+3e97"] = ["to select"]
BLISS_TO_UNICODE["fresh cheese"] = ["U+3e98"]
UNICODE_TO_BLISS["U+3e98"] = ["fresh cheese"]
BLISS_TO_UNICODE["inflammable"] = ["U+3e99"]
UNICODE_TO_BLISS["U+3e99"] = ["inflammable"]
BLISS_TO_UNICODE["flammable"] = ["U+3e99"]
UNICODE_TO_BLISS["U+3e99"].append("flammable")
BLISS_TO_UNICODE["inflammable,flammable"] = ["U+3e99"]
UNICODE_TO_BLISS["U+3e99"].append("inflammable,flammable")
BLISS_TO_UNICODE["body hair"] = ["U+3e9a"]
UNICODE_TO_BLISS["U+3e9a"] = ["body hair"]
BLISS_TO_UNICODE["breakable"] = ["U+3e9b"]
UNICODE_TO_BLISS["U+3e9b"] = ["breakable"]
BLISS_TO_UNICODE["fragile"] = ["U+3e9b"]
UNICODE_TO_BLISS["U+3e9b"].append("fragile")
BLISS_TO_UNICODE["breakable,fragile"] = ["U+3e9b"]
UNICODE_TO_BLISS["U+3e9b"].append("breakable,fragile")
BLISS_TO_UNICODE["gun"].append("U+353a")
UNICODE_TO_BLISS["U+353a"].append("gun")
BLISS_TO_UNICODE["cannon,gun"] = ["U+353a"]
UNICODE_TO_BLISS["U+353a"].append("cannon,gun")
BLISS_TO_UNICODE["pictograph incorporating wheel and to destroy"] = ["U+3e9c"]
UNICODE_TO_BLISS["U+3e9c"] = ["pictograph incorporating wheel and to destroy"]
BLISS_TO_UNICODE["firearm"] = ["U+3309"]
UNICODE_TO_BLISS["U+3309"].append("firearm")
BLISS_TO_UNICODE["gun,firearm"] = ["U+3309"]
UNICODE_TO_BLISS["U+3309"].append("gun,firearm")
BLISS_TO_UNICODE["electric field"] = ["U+3e9d"]
UNICODE_TO_BLISS["U+3e9d"] = ["electric field"]
BLISS_TO_UNICODE["diarrhea"] = ["U+3e9e"]
UNICODE_TO_BLISS["U+3e9e"] = ["diarrhea"]
BLISS_TO_UNICODE["diarrhoea"] = ["U+3e9e"]
UNICODE_TO_BLISS["U+3e9e"].append("diarrhoea")
BLISS_TO_UNICODE["diarrhea,diarrhoea"] = ["U+3e9e"]
UNICODE_TO_BLISS["U+3e9e"].append("diarrhea,diarrhoea")
BLISS_TO_UNICODE["courageous"] = ["U+39d5"]
UNICODE_TO_BLISS["U+39d5"].append("courageous")
BLISS_TO_UNICODE["brave,courageous"] = ["U+39d5"]
UNICODE_TO_BLISS["U+39d5"].append("brave,courageous")
BLISS_TO_UNICODE["courage"] = ["U+3e9f"]
UNICODE_TO_BLISS["U+3e9f"] = ["courage"]
BLISS_TO_UNICODE["sorry"] = ["U+3ea0"]
UNICODE_TO_BLISS["U+3ea0"] = ["sorry"]
BLISS_TO_UNICODE["bedroom"] = ["U+3ea1"]
UNICODE_TO_BLISS["U+3ea1"] = ["bedroom"]
BLISS_TO_UNICODE["to sleep)"] = ["U+3ea3"]
UNICODE_TO_BLISS["U+3ea3"] = ["to sleep)"]
BLISS_TO_UNICODE["price"] = ["U+3b43"]
UNICODE_TO_BLISS["U+3b43"].append("price")
BLISS_TO_UNICODE["cost,price"] = ["U+3b43"]
UNICODE_TO_BLISS["U+3b43"].append("cost,price")
BLISS_TO_UNICODE["God the son"] = ["U+3ea4"]
UNICODE_TO_BLISS["U+3ea4"] = ["God the son"]
BLISS_TO_UNICODE["continental drift"] = ["U+3ea5"]
UNICODE_TO_BLISS["U+3ea5"] = ["continental drift"]
BLISS_TO_UNICODE["continent"] = ["U+3ea6"]
UNICODE_TO_BLISS["U+3ea6"] = ["continent"]
BLISS_TO_UNICODE["appear"] = ["U+3ea7"]
UNICODE_TO_BLISS["U+3ea7"] = ["appear"]
BLISS_TO_UNICODE["appearance"] = ["U+3ea8"]
UNICODE_TO_BLISS["U+3ea8"] = ["appearance"]
BLISS_TO_UNICODE["fan club"] = ["U+3ea9"]
UNICODE_TO_BLISS["U+3ea9"] = ["fan club"]
BLISS_TO_UNICODE["club"] = ["U+3eaa"]
UNICODE_TO_BLISS["U+3eaa"] = ["club"]
BLISS_TO_UNICODE["uniform"] = ["U+3eab"]
UNICODE_TO_BLISS["U+3eab"] = ["uniform"]
BLISS_TO_UNICODE["crew"] = ["U+3eac"]
UNICODE_TO_BLISS["U+3eac"] = ["crew"]
BLISS_TO_UNICODE["staff"] = ["U+3ead"]
UNICODE_TO_BLISS["U+3ead"] = ["staff"]
BLISS_TO_UNICODE["decade"] = ["U+3eae"]
UNICODE_TO_BLISS["U+3eae"] = ["decade"]
BLISS_TO_UNICODE["common"] = ["U+3eaf"]
UNICODE_TO_BLISS["U+3eaf"] = ["common"]
BLISS_TO_UNICODE["mutual"] = ["U+3eaf"]
UNICODE_TO_BLISS["U+3eaf"].append("mutual")
BLISS_TO_UNICODE["shared"] = ["U+3eaf"]
UNICODE_TO_BLISS["U+3eaf"].append("shared")
BLISS_TO_UNICODE["common,mutual,shared"] = ["U+3eaf"]
UNICODE_TO_BLISS["U+3eaf"].append("common,mutual,shared")
BLISS_TO_UNICODE["English"] = ["U+3eb0"]
UNICODE_TO_BLISS["U+3eb0"] = ["English"]
BLISS_TO_UNICODE["England"] = ["U+3eb1"]
UNICODE_TO_BLISS["U+3eb1"] = ["England"]
BLISS_TO_UNICODE["colander"] = ["U+32f2"]
UNICODE_TO_BLISS["U+32f2"].append("colander")
BLISS_TO_UNICODE["strainer"] = ["U+32f2"]
UNICODE_TO_BLISS["U+32f2"].append("strainer")
BLISS_TO_UNICODE["sieve,colander,strainer"] = ["U+32f2"]
UNICODE_TO_BLISS["U+32f2"].append("sieve,colander,strainer")
BLISS_TO_UNICODE["teacher"] = ["U+3eb2"]
UNICODE_TO_BLISS["U+3eb2"] = ["teacher"]
BLISS_TO_UNICODE["instructor"] = ["U+3eb2"]
UNICODE_TO_BLISS["U+3eb2"].append("instructor")
BLISS_TO_UNICODE["teacher,instructor"] = ["U+3eb2"]
UNICODE_TO_BLISS["U+3eb2"].append("teacher,instructor")
BLISS_TO_UNICODE["pedagogue"] = ["U+3eb2"]
UNICODE_TO_BLISS["U+3eb2"].append("pedagogue")
BLISS_TO_UNICODE["educator"] = ["U+3eb2"]
UNICODE_TO_BLISS["U+3eb2"].append("educator")
BLISS_TO_UNICODE["teacher,pedagogue,educator"] = ["U+3eb2"]
UNICODE_TO_BLISS["U+3eb2"].append("teacher,pedagogue,educator")
BLISS_TO_UNICODE["alteration"] = ["U+326b"]
UNICODE_TO_BLISS["U+326b"].append("alteration")
BLISS_TO_UNICODE["change,alteration"] = ["U+326b"]
UNICODE_TO_BLISS["U+326b"].append("change,alteration")
BLISS_TO_UNICODE["alter"] = ["U+326b"]
UNICODE_TO_BLISS["U+326b"].append("alter")
BLISS_TO_UNICODE["change,alter"] = ["U+326b"]
UNICODE_TO_BLISS["U+326b"].append("change,alter")
BLISS_TO_UNICODE["prayer book"] = ["U+3eb3"]
UNICODE_TO_BLISS["U+3eb3"] = ["prayer book"]
BLISS_TO_UNICODE["Siddur"] = ["U+3eb3"]
UNICODE_TO_BLISS["U+3eb3"].append("Siddur")
BLISS_TO_UNICODE["prayer book,Siddur"] = ["U+3eb3"]
UNICODE_TO_BLISS["U+3eb3"].append("prayer book,Siddur")
BLISS_TO_UNICODE["Portugal"] = ["U+3eb4"]
UNICODE_TO_BLISS["U+3eb4"] = ["Portugal"]
BLISS_TO_UNICODE["drain"] = ["U+3eb5"]
UNICODE_TO_BLISS["U+3eb5"] = ["drain"]
BLISS_TO_UNICODE["sift"] = ["U+3eb5"]
UNICODE_TO_BLISS["U+3eb5"].append("sift")
BLISS_TO_UNICODE["strain"] = ["U+3eb5"]
UNICODE_TO_BLISS["U+3eb5"].append("strain")
BLISS_TO_UNICODE["drain,sift,strain"] = ["U+3eb5"]
UNICODE_TO_BLISS["U+3eb5"].append("drain,sift,strain")
BLISS_TO_UNICODE["explode"] = ["U+3eb6"]
UNICODE_TO_BLISS["U+3eb6"] = ["explode"]
BLISS_TO_UNICODE["blow up"] = ["U+3eb6"]
UNICODE_TO_BLISS["U+3eb6"].append("blow up")
BLISS_TO_UNICODE["detonate"] = ["U+3eb6"]
UNICODE_TO_BLISS["U+3eb6"].append("detonate")
BLISS_TO_UNICODE["burst"] = ["U+3eb6"]
UNICODE_TO_BLISS["U+3eb6"].append("burst")
BLISS_TO_UNICODE["explode,blow up,detonate,burst"] = ["U+3eb6"]
UNICODE_TO_BLISS["U+3eb6"].append("explode,blow up,detonate,burst")
BLISS_TO_UNICODE["trial"] = ["U+3eb7"]
UNICODE_TO_BLISS["U+3eb7"] = ["trial"]
BLISS_TO_UNICODE["usual"] = ["U+3bca"]
UNICODE_TO_BLISS["U+3bca"].append("usual")
BLISS_TO_UNICODE["usually,usual"] = ["U+3bca"]
UNICODE_TO_BLISS["U+3bca"].append("usually,usual")
BLISS_TO_UNICODE["chesterfield"] = ["U+3547"]
UNICODE_TO_BLISS["U+3547"].append("chesterfield")
BLISS_TO_UNICODE["sofa"].append("U+3547")
UNICODE_TO_BLISS["U+3547"].append("sofa")
BLISS_TO_UNICODE["couch,chesterfield,sofa"] = ["U+3547"]
UNICODE_TO_BLISS["U+3547"].append("couch,chesterfield,sofa")
BLISS_TO_UNICODE["paddle boat"] = ["U+3eb8"]
UNICODE_TO_BLISS["U+3eb8"] = ["paddle boat"]
BLISS_TO_UNICODE["pedal boat"] = ["U+3eb8"]
UNICODE_TO_BLISS["U+3eb8"].append("pedal boat")
BLISS_TO_UNICODE["water bike"] = ["U+3eb8"]
UNICODE_TO_BLISS["U+3eb8"].append("water bike")
BLISS_TO_UNICODE["pedalo"] = ["U+3eb8"]
UNICODE_TO_BLISS["U+3eb8"].append("pedalo")
BLISS_TO_UNICODE["paddle boat,pedal boat,water bike,pedalo"] = ["U+3eb8"]
UNICODE_TO_BLISS["U+3eb8"].append("paddle boat,pedal boat,water bike,pedalo")
BLISS_TO_UNICODE["sky sports"] = ["U+3eb9"]
UNICODE_TO_BLISS["U+3eb9"] = ["sky sports"]
BLISS_TO_UNICODE["retired"] = ["U+3eba"]
UNICODE_TO_BLISS["U+3eba"] = ["retired"]
BLISS_TO_UNICODE["retirement"] = ["U+3ebb"]
UNICODE_TO_BLISS["U+3ebb"] = ["retirement"]
BLISS_TO_UNICODE["berth"] = ["U+3ebc"]
UNICODE_TO_BLISS["U+3ebc"] = ["berth"]
BLISS_TO_UNICODE["bunk"] = ["U+3ebc"]
UNICODE_TO_BLISS["U+3ebc"].append("bunk")
BLISS_TO_UNICODE["berth,bunk"] = ["U+3ebc"]
UNICODE_TO_BLISS["U+3ebc"].append("berth,bunk")
BLISS_TO_UNICODE["snowboard"] = ["U+3ebd"]
UNICODE_TO_BLISS["U+3ebd"] = ["snowboard"]
BLISS_TO_UNICODE["living room"] = ["U+3ebe"]
UNICODE_TO_BLISS["U+3ebe"] = ["living room"]
BLISS_TO_UNICODE["lounge"] = ["U+3ebe"]
UNICODE_TO_BLISS["U+3ebe"].append("lounge")
BLISS_TO_UNICODE["sitting room"] = ["U+3ebe"]
UNICODE_TO_BLISS["U+3ebe"].append("sitting room")
BLISS_TO_UNICODE["front room"] = ["U+3ebe"]
UNICODE_TO_BLISS["U+3ebe"].append("front room")
BLISS_TO_UNICODE["parlor"] = ["U+3ebe"]
UNICODE_TO_BLISS["U+3ebe"].append("parlor")
BLISS_TO_UNICODE["parlour"] = ["U+3ebe"]
UNICODE_TO_BLISS["U+3ebe"].append("parlour")
BLISS_TO_UNICODE["waiting room"] = ["U+3ebe"]
UNICODE_TO_BLISS["U+3ebe"].append("waiting room")
BLISS_TO_UNICODE["living room,lounge,sitting room,front room,parlor,parlour,waiting room"] = ["U+3ebe"]
UNICODE_TO_BLISS["U+3ebe"].append("living room,lounge,sitting room,front room,parlor,parlour,waiting room")
BLISS_TO_UNICODE["crayon"] = ["U+3ebf"]
UNICODE_TO_BLISS["U+3ebf"] = ["crayon"]
BLISS_TO_UNICODE["coloured pencil"] = ["U+3ebf"]
UNICODE_TO_BLISS["U+3ebf"].append("coloured pencil")
BLISS_TO_UNICODE["marker"] = ["U+3ebf"]
UNICODE_TO_BLISS["U+3ebf"].append("marker")
BLISS_TO_UNICODE["crayon,coloured pencil,marker"] = ["U+3ebf"]
UNICODE_TO_BLISS["U+3ebf"].append("crayon,coloured pencil,marker")
BLISS_TO_UNICODE["market"] = ["U+3ec0"]
UNICODE_TO_BLISS["U+3ec0"] = ["market"]
BLISS_TO_UNICODE["dwell"] = ["U+3904"]
UNICODE_TO_BLISS["U+3904"].append("dwell")
BLISS_TO_UNICODE["reside"] = ["U+3904"]
UNICODE_TO_BLISS["U+3904"].append("reside")
BLISS_TO_UNICODE["live,dwell,reside"] = ["U+3904"]
UNICODE_TO_BLISS["U+3904"].append("live,dwell,reside")
BLISS_TO_UNICODE["clue"] = ["U+3ec1"]
UNICODE_TO_BLISS["U+3ec1"] = ["clue"]
BLISS_TO_UNICODE["electric insulator"] = ["U+3ec2"]
UNICODE_TO_BLISS["U+3ec2"] = ["electric insulator"]
BLISS_TO_UNICODE["electrical insulator"] = ["U+3ec2"]
UNICODE_TO_BLISS["U+3ec2"].append("electrical insulator")
BLISS_TO_UNICODE["electric insulator,electrical insulator"] = ["U+3ec2"]
UNICODE_TO_BLISS["U+3ec2"].append("electric insulator,electrical insulator")
BLISS_TO_UNICODE["impermeable material"] = ["U+3ec3"]
UNICODE_TO_BLISS["U+3ec3"] = ["impermeable material"]
BLISS_TO_UNICODE["insulation"] = ["U+3ec4"]
UNICODE_TO_BLISS["U+3ec4"] = ["insulation"]
BLISS_TO_UNICODE["automobile"].append("U+3599")
UNICODE_TO_BLISS["U+3599"].append("automobile")
BLISS_TO_UNICODE["motor vehicle"] = ["U+3599"]
UNICODE_TO_BLISS["U+3599"].append("motor vehicle")
BLISS_TO_UNICODE["car,automobile,motor vehicle"] = ["U+3599"]
UNICODE_TO_BLISS["U+3599"].append("car,automobile,motor vehicle")
BLISS_TO_UNICODE["pictograph of a steering wheel"] = ["U+3ec5"]
UNICODE_TO_BLISS["U+3ec5"] = ["pictograph of a steering wheel"]
BLISS_TO_UNICODE["MMS"] = ["U+3ec6"]
UNICODE_TO_BLISS["U+3ec6"] = ["MMS"]
BLISS_TO_UNICODE["feline"] = ["U+3e95"]
UNICODE_TO_BLISS["U+3e95"].append("feline")
BLISS_TO_UNICODE["felid"] = ["U+3e95"]
UNICODE_TO_BLISS["U+3e95"].append("felid")
BLISS_TO_UNICODE["cat,feline"] = ["U+3e95"]
UNICODE_TO_BLISS["U+3e95"].append("cat,feline")
BLISS_TO_UNICODE["small curved lines"] = ["U+3ec7"]
UNICODE_TO_BLISS["U+3ec7"] = ["small curved lines"]
BLISS_TO_UNICODE["mew"] = ["U+3ec8"]
UNICODE_TO_BLISS["U+3ec8"] = ["mew"]
BLISS_TO_UNICODE["meow"] = ["U+3ec8"]
UNICODE_TO_BLISS["U+3ec8"].append("meow")
BLISS_TO_UNICODE["mew,meow"] = ["U+3ec8"]
UNICODE_TO_BLISS["U+3ec8"].append("mew,meow")
BLISS_TO_UNICODE["bottle opening"].append("U+384e")
UNICODE_TO_BLISS["U+384e"].append("bottle opening")
BLISS_TO_UNICODE["bottleneck,bottle opening"] = ["U+384e"]
UNICODE_TO_BLISS["U+384e"].append("bottleneck,bottle opening")
BLISS_TO_UNICODE["cab"] = ["U+3818"]
UNICODE_TO_BLISS["U+3818"].append("cab")
BLISS_TO_UNICODE["taxi,cab"] = ["U+3818"]
UNICODE_TO_BLISS["U+3818"].append("taxi,cab")
BLISS_TO_UNICODE["heart"] = ["U+3ec9"]
UNICODE_TO_BLISS["U+3ec9"] = ["heart"]
BLISS_TO_UNICODE["exclude"] = ["U+3eca"]
UNICODE_TO_BLISS["U+3eca"] = ["exclude"]
BLISS_TO_UNICODE["bird nest"] = ["U+3ecb"]
UNICODE_TO_BLISS["U+3ecb"] = ["bird nest"]
BLISS_TO_UNICODE["birdnest"] = ["U+3ecb"]
UNICODE_TO_BLISS["U+3ecb"].append("birdnest")
BLISS_TO_UNICODE["bird nest,birdnest"] = ["U+3ecb"]
UNICODE_TO_BLISS["U+3ecb"].append("bird nest,birdnest")
BLISS_TO_UNICODE["visually impaired"] = ["U+3ecc"]
UNICODE_TO_BLISS["U+3ecc"] = ["visually impaired"]
BLISS_TO_UNICODE["visual impairment"] = ["U+3ecd"]
UNICODE_TO_BLISS["U+3ecd"] = ["visual impairment"]
BLISS_TO_UNICODE["Austria"] = ["U+3ece"]
UNICODE_TO_BLISS["U+3ece"] = ["Austria"]
BLISS_TO_UNICODE["freezer"] = ["U+3ecf"]
UNICODE_TO_BLISS["U+3ecf"] = ["freezer"]
BLISS_TO_UNICODE["throw up"] = ["U+3a7d"]
UNICODE_TO_BLISS["U+3a7d"].append("throw up")
BLISS_TO_UNICODE["puke"] = ["U+3a7d"]
UNICODE_TO_BLISS["U+3a7d"].append("puke")
BLISS_TO_UNICODE["vomit,throw up,puke"] = ["U+3a7d"]
UNICODE_TO_BLISS["U+3a7d"].append("vomit,throw up,puke")
BLISS_TO_UNICODE["deep fry"] = ["U+3ed0"]
UNICODE_TO_BLISS["U+3ed0"] = ["deep fry"]
BLISS_TO_UNICODE["deep-fry"] = ["U+3ed0"]
UNICODE_TO_BLISS["U+3ed0"].append("deep-fry")
BLISS_TO_UNICODE["gift"] = ["U+3ed1"]
UNICODE_TO_BLISS["U+3ed1"] = ["gift"]
BLISS_TO_UNICODE["southern"] = ["U+3ed2"]
UNICODE_TO_BLISS["U+3ed2"] = ["southern"]
BLISS_TO_UNICODE["wiggly"] = ["U+3ed3"]
UNICODE_TO_BLISS["U+3ed3"] = ["wiggly"]
BLISS_TO_UNICODE["manufacture"] = ["U+33ba"]
UNICODE_TO_BLISS["U+33ba"].append("manufacture")
BLISS_TO_UNICODE["produce"] = ["U+33ba"]
UNICODE_TO_BLISS["U+33ba"].append("produce")
BLISS_TO_UNICODE["make,manufacture,produce"] = ["U+33ba"]
UNICODE_TO_BLISS["U+33ba"].append("make,manufacture,produce")
BLISS_TO_UNICODE["toilet paper"] = ["U+3ed4"]
UNICODE_TO_BLISS["U+3ed4"] = ["toilet paper"]
BLISS_TO_UNICODE["fast day"] = ["U+3ed5"]
UNICODE_TO_BLISS["U+3ed5"] = ["fast day"]
BLISS_TO_UNICODE["remember"] = ["U+3ed6"]
UNICODE_TO_BLISS["U+3ed6"] = ["remember"]
BLISS_TO_UNICODE["recall"] = ["U+3ed6"]
UNICODE_TO_BLISS["U+3ed6"].append("recall")
BLISS_TO_UNICODE["remember,recall"] = ["U+3ed6"]
UNICODE_TO_BLISS["U+3ed6"].append("remember,recall")
BLISS_TO_UNICODE["whenever"] = ["U+3ade"]
UNICODE_TO_BLISS["U+3ade"].append("whenever")
BLISS_TO_UNICODE["ever,whenever"] = ["U+3ade"]
UNICODE_TO_BLISS["U+3ade"].append("ever,whenever")
BLISS_TO_UNICODE["anytime"] = ["U+3ed7"]
UNICODE_TO_BLISS["U+3ed7"] = ["anytime"]
BLISS_TO_UNICODE["manhole cover"] = ["U+3ed8"]
UNICODE_TO_BLISS["U+3ed8"] = ["manhole cover"]
BLISS_TO_UNICODE["lid"] = ["U+3ed9"]
UNICODE_TO_BLISS["U+3ed9"] = ["lid"]
BLISS_TO_UNICODE["counsellor"] = ["U+3eda"]
UNICODE_TO_BLISS["U+3eda"] = ["counsellor"]
BLISS_TO_UNICODE["adviser"] = ["U+3eda"]
UNICODE_TO_BLISS["U+3eda"].append("adviser")
BLISS_TO_UNICODE["counsellor,adviser"] = ["U+3eda"]
UNICODE_TO_BLISS["U+3eda"].append("counsellor,adviser")
BLISS_TO_UNICODE["brain"] = ["U+3edb"]
UNICODE_TO_BLISS["U+3edb"] = ["brain"]
BLISS_TO_UNICODE["be able"] = ["U+3a10"]
UNICODE_TO_BLISS["U+3a10"].append("be able")
BLISS_TO_UNICODE["can,be able"] = ["U+3a10"]
UNICODE_TO_BLISS["U+3a10"].append("can,be able")
BLISS_TO_UNICODE["braid"] = ["U+3edd"]
UNICODE_TO_BLISS["U+3edd"] = ["braid"]
BLISS_TO_UNICODE["plait"] = ["U+3edd"]
UNICODE_TO_BLISS["U+3edd"].append("plait")
BLISS_TO_UNICODE["braid,plait"] = ["U+3edd"]
UNICODE_TO_BLISS["U+3edd"].append("braid,plait")
BLISS_TO_UNICODE["pigtail"] = ["U+3edd"]
UNICODE_TO_BLISS["U+3edd"].append("pigtail")
BLISS_TO_UNICODE["braid,plait,pigtail"] = ["U+3edd"]
UNICODE_TO_BLISS["U+3edd"].append("braid,plait,pigtail")
BLISS_TO_UNICODE["camper van"] = ["U+3ede"]
UNICODE_TO_BLISS["U+3ede"] = ["camper van"]
BLISS_TO_UNICODE["RV"] = ["U+3ede"]
UNICODE_TO_BLISS["U+3ede"].append("RV")
BLISS_TO_UNICODE["camper van,RV"] = ["U+3ede"]
UNICODE_TO_BLISS["U+3ede"].append("camper van,RV")
BLISS_TO_UNICODE["tracheotomy tube"] = ["U+3edf"]
UNICODE_TO_BLISS["U+3edf"] = ["tracheotomy tube"]
BLISS_TO_UNICODE["tracheal tube"] = ["U+3edf"]
UNICODE_TO_BLISS["U+3edf"].append("tracheal tube")
BLISS_TO_UNICODE["tracheotomy tube,tracheal tube"] = ["U+3edf"]
UNICODE_TO_BLISS["U+3edf"].append("tracheotomy tube,tracheal tube")
BLISS_TO_UNICODE["air traffic controller"] = ["U+3ee0"]
UNICODE_TO_BLISS["U+3ee0"] = ["air traffic controller"]
BLISS_TO_UNICODE["eternal life"] = ["U+3ee1"]
UNICODE_TO_BLISS["U+3ee1"] = ["eternal life"]
BLISS_TO_UNICODE["immortality"] = ["U+3ee1"]
UNICODE_TO_BLISS["U+3ee1"].append("immortality")
BLISS_TO_UNICODE["eternal life,immortality"] = ["U+3ee1"]
UNICODE_TO_BLISS["U+3ee1"].append("eternal life,immortality")
BLISS_TO_UNICODE["sacrament of absolution"] = ["U+3ee2"]
UNICODE_TO_BLISS["U+3ee2"] = ["sacrament of absolution"]
BLISS_TO_UNICODE["to forgive"] = ["U+3ee3"]
UNICODE_TO_BLISS["U+3ee3"] = ["to forgive"]
BLISS_TO_UNICODE["Snork"] = ["U+3ee4"]
UNICODE_TO_BLISS["U+3ee4"] = ["Snork"]
BLISS_TO_UNICODE["rake"] = ["U+3ee5"]
UNICODE_TO_BLISS["U+3ee5"] = ["rake"]
BLISS_TO_UNICODE["introduce"] = ["U+3ee6"]
UNICODE_TO_BLISS["U+3ee6"] = ["introduce"]
BLISS_TO_UNICODE["present"].append("U+3ee6")
UNICODE_TO_BLISS["U+3ee6"].append("present")
BLISS_TO_UNICODE["introduce,present"] = ["U+3ee6"]
UNICODE_TO_BLISS["U+3ee6"].append("introduce,present")
BLISS_TO_UNICODE["fairy godmother"] = ["U+35b3"]
UNICODE_TO_BLISS["U+35b3"].append("fairy godmother")
BLISS_TO_UNICODE["fairy,fairy godmother"] = ["U+35b3"]
UNICODE_TO_BLISS["U+35b3"].append("fairy,fairy godmother")
BLISS_TO_UNICODE["what kind"] = ["U+3ee7"]
UNICODE_TO_BLISS["U+3ee7"] = ["what kind"]
BLISS_TO_UNICODE["type"] = ["U+3ee8"]
UNICODE_TO_BLISS["U+3ee8"] = ["type"]
BLISS_TO_UNICODE["jeans"] = ["U+36ee"]
UNICODE_TO_BLISS["U+36ee"].append("jeans")
BLISS_TO_UNICODE["slacks"] = ["U+36ee"]
UNICODE_TO_BLISS["U+36ee"].append("slacks")
BLISS_TO_UNICODE["trousers"].append("U+36ee")
UNICODE_TO_BLISS["U+36ee"].append("trousers")
BLISS_TO_UNICODE["pants,jeans,slacks,trousers"] = ["U+36ee"]
UNICODE_TO_BLISS["U+36ee"].append("pants,jeans,slacks,trousers")
BLISS_TO_UNICODE["corridor"] = ["U+3ee9"]
UNICODE_TO_BLISS["U+3ee9"] = ["corridor"]
BLISS_TO_UNICODE["hall"] = ["U+3ee9"]
UNICODE_TO_BLISS["U+3ee9"].append("hall")
BLISS_TO_UNICODE["corridor,hall"] = ["U+3ee9"]
UNICODE_TO_BLISS["U+3ee9"].append("corridor,hall")
BLISS_TO_UNICODE["nor"] = ["U+3eea"]
UNICODE_TO_BLISS["U+3eea"] = ["nor"]
BLISS_TO_UNICODE["barrow"] = ["U+3eeb"]
UNICODE_TO_BLISS["U+3eeb"] = ["barrow"]
BLISS_TO_UNICODE["grave mound"] = ["U+3eeb"]
UNICODE_TO_BLISS["U+3eeb"].append("grave mound")
BLISS_TO_UNICODE["barrow,grave mound"] = ["U+3eeb"]
UNICODE_TO_BLISS["U+3eeb"].append("barrow,grave mound")
BLISS_TO_UNICODE["let fall"] = ["U+3eec"]
UNICODE_TO_BLISS["U+3eec"] = ["let fall"]
BLISS_TO_UNICODE["drop"].append("U+3eec")
UNICODE_TO_BLISS["U+3eec"].append("drop")
BLISS_TO_UNICODE["let fall,drop"] = ["U+3eec"]
UNICODE_TO_BLISS["U+3eec"].append("let fall,drop")
BLISS_TO_UNICODE["fluid"] = ["U+3eed"]
UNICODE_TO_BLISS["U+3eed"] = ["fluid"]
BLISS_TO_UNICODE["hurried"] = ["U+3a20"]
UNICODE_TO_BLISS["U+3a20"].append("hurried")
BLISS_TO_UNICODE["rushed"] = ["U+3a20"]
UNICODE_TO_BLISS["U+3a20"].append("rushed")
BLISS_TO_UNICODE["goose"] = ["U+3eee"]
UNICODE_TO_BLISS["U+3eee"] = ["goose"]
BLISS_TO_UNICODE["prone board"] = ["U+3eef"]
UNICODE_TO_BLISS["U+3eef"] = ["prone board"]
BLISS_TO_UNICODE["scooter board"] = ["U+3eef"]
UNICODE_TO_BLISS["U+3eef"].append("scooter board")
BLISS_TO_UNICODE["prone board,scooter-board"] = ["U+3eef"]
UNICODE_TO_BLISS["U+3eef"].append("prone board,scooter-board")
BLISS_TO_UNICODE["sun with arrow head"] = ["U+3ef0"]
UNICODE_TO_BLISS["U+3ef0"] = ["sun with arrow head"]
BLISS_TO_UNICODE[" indicating movement around"] = ["U+3ef1"]
UNICODE_TO_BLISS["U+3ef1"] = [" indicating movement around"]
BLISS_TO_UNICODE["happen"] = ["U+3ef2"]
UNICODE_TO_BLISS["U+3ef2"] = ["happen"]
BLISS_TO_UNICODE["occur"] = ["U+3ef2"]
UNICODE_TO_BLISS["U+3ef2"].append("occur")
BLISS_TO_UNICODE["happen,occur"] = ["U+3ef2"]
UNICODE_TO_BLISS["U+3ef2"].append("happen,occur")
BLISS_TO_UNICODE["have a tea break"] = ["U+3ef3"]
UNICODE_TO_BLISS["U+3ef3"] = ["have a tea break"]
BLISS_TO_UNICODE["have a coffee break"] = ["U+3ef3"]
UNICODE_TO_BLISS["U+3ef3"].append("have a coffee break")
BLISS_TO_UNICODE["have a tea break,have a coffee break"] = ["U+3ef3"]
UNICODE_TO_BLISS["U+3ef3"].append("have a tea break,have a coffee break")
BLISS_TO_UNICODE["Norwegian"] = ["U+3ef4"]
UNICODE_TO_BLISS["U+3ef4"] = ["Norwegian"]
BLISS_TO_UNICODE["fjord"] = ["U+3ef5"]
UNICODE_TO_BLISS["U+3ef5"] = ["fjord"]
BLISS_TO_UNICODE["to open"] = ["U+3ef6"]
UNICODE_TO_BLISS["U+3ef6"] = ["to open"]
BLISS_TO_UNICODE["mental"] = ["U+3ef7"]
UNICODE_TO_BLISS["U+3ef7"] = ["mental"]
BLISS_TO_UNICODE["intellectual"] = ["U+3ef7"]
UNICODE_TO_BLISS["U+3ef7"].append("intellectual")
BLISS_TO_UNICODE["rational"] = ["U+3ef7"]
UNICODE_TO_BLISS["U+3ef7"].append("rational")
BLISS_TO_UNICODE["thinking"] = ["U+3ef7"]
UNICODE_TO_BLISS["U+3ef7"].append("thinking")
BLISS_TO_UNICODE["mental,intellectual,rational,thinking"] = ["U+3ef7"]
UNICODE_TO_BLISS["U+3ef7"].append("mental,intellectual,rational,thinking")
BLISS_TO_UNICODE["high jump"] = ["U+3ef8"]
UNICODE_TO_BLISS["U+3ef8"] = ["high jump"]
BLISS_TO_UNICODE["milkmaid"] = ["U+3ef9"]
UNICODE_TO_BLISS["U+3ef9"] = ["milkmaid"]
BLISS_TO_UNICODE["dairymaid"] = ["U+3ef9"]
UNICODE_TO_BLISS["U+3ef9"].append("dairymaid")
BLISS_TO_UNICODE["milkmaid,dairymaid"] = ["U+3ef9"]
UNICODE_TO_BLISS["U+3ef9"].append("milkmaid,dairymaid")
BLISS_TO_UNICODE["mountain pasture"] = ["U+3efa"]
UNICODE_TO_BLISS["U+3efa"] = ["mountain pasture"]
BLISS_TO_UNICODE["parking lot"] = ["U+3efb"]
UNICODE_TO_BLISS["U+3efb"] = ["parking lot"]
BLISS_TO_UNICODE["protect"].append("U+377a")
UNICODE_TO_BLISS["U+377a"].append("protect")
BLISS_TO_UNICODE["defend"].append("U+377a")
UNICODE_TO_BLISS["U+377a"].append("defend")
BLISS_TO_UNICODE["care,protect,defend"] = ["U+377a"]
UNICODE_TO_BLISS["U+377a"].append("care,protect,defend")
BLISS_TO_UNICODE["Eris"] = ["U+3efc"]
UNICODE_TO_BLISS["U+3efc"] = ["Eris"]
BLISS_TO_UNICODE["invitation"] = ["U+3efd"]
UNICODE_TO_BLISS["U+3efd"] = ["invitation"]
BLISS_TO_UNICODE["Hungary"] = ["U+3efe"]
UNICODE_TO_BLISS["U+3efe"] = ["Hungary"]
BLISS_TO_UNICODE["a country that is a bridge between East and West"] = ["U+3eff"]
UNICODE_TO_BLISS["U+3eff"] = ["a country that is a bridge between East and West"]
BLISS_TO_UNICODE["promotion"] = ["U+3f00"]
UNICODE_TO_BLISS["U+3f00"] = ["promotion"]
BLISS_TO_UNICODE["altitude"] = ["U+3815"]
UNICODE_TO_BLISS["U+3815"].append("altitude")
BLISS_TO_UNICODE["height,altitude"] = ["U+3815"]
UNICODE_TO_BLISS["U+3815"].append("height,altitude")
BLISS_TO_UNICODE["adventure"] = ["U+3f01"]
UNICODE_TO_BLISS["U+3f01"] = ["adventure"]
BLISS_TO_UNICODE["blindness"] = ["U+3f02"]
UNICODE_TO_BLISS["U+3f02"] = ["blindness"]
BLISS_TO_UNICODE["Afghanistan"] = ["U+3f03"]
UNICODE_TO_BLISS["U+3f03"] = ["Afghanistan"]
BLISS_TO_UNICODE["small pancake"] = ["U+3f04"]
UNICODE_TO_BLISS["U+3f04"] = ["small pancake"]
BLISS_TO_UNICODE["blini"] = ["U+3f04"]
UNICODE_TO_BLISS["U+3f04"].append("blini")
BLISS_TO_UNICODE["small pancake,blini"] = ["U+3f04"]
UNICODE_TO_BLISS["U+3f04"].append("small pancake,blini")
BLISS_TO_UNICODE["pancak"] = ["U+3f05"]
UNICODE_TO_BLISS["U+3f05"] = ["pancak"]
BLISS_TO_UNICODE["Asia"] = ["U+3f06"]
UNICODE_TO_BLISS["U+3f06"] = ["Asia"]
BLISS_TO_UNICODE["sanctify"] = ["U+3f07"]
UNICODE_TO_BLISS["U+3f07"] = ["sanctify"]
BLISS_TO_UNICODE["consecrate"] = ["U+3f07"]
UNICODE_TO_BLISS["U+3f07"].append("consecrate")
BLISS_TO_UNICODE["sanctify,consecrate"] = ["U+3f07"]
UNICODE_TO_BLISS["U+3f07"].append("sanctify,consecrate")
BLISS_TO_UNICODE["tomorrow"] = ["U+3f08"]
UNICODE_TO_BLISS["U+3f08"] = ["tomorrow"]
BLISS_TO_UNICODE["size"] = ["U+3f09"]
UNICODE_TO_BLISS["U+3f09"] = ["size"]
BLISS_TO_UNICODE["disabled"] = ["U+3f0a"]
UNICODE_TO_BLISS["U+3f0a"] = ["disabled"]
BLISS_TO_UNICODE["impaired"] = ["U+3f0a"]
UNICODE_TO_BLISS["U+3f0a"].append("impaired")
BLISS_TO_UNICODE["handicapped"] = ["U+3f0a"]
UNICODE_TO_BLISS["U+3f0a"].append("handicapped")
BLISS_TO_UNICODE["mentally)"] = ["U+3f0a"]
UNICODE_TO_BLISS["U+3f0a"].append("mentally)")
BLISS_TO_UNICODE["disabled,impaired,handicapped"] = ["U+3f0a"]
UNICODE_TO_BLISS["U+3f0a"].append("disabled,impaired,handicapped")
BLISS_TO_UNICODE["checked"] = ["U+3f0b"]
UNICODE_TO_BLISS["U+3f0b"] = ["checked"]
BLISS_TO_UNICODE["silent"] = ["U+3f0c"]
UNICODE_TO_BLISS["U+3f0c"] = ["silent"]
BLISS_TO_UNICODE["silence"] = ["U+3f0d"]
UNICODE_TO_BLISS["U+3f0d"] = ["silence"]
BLISS_TO_UNICODE["merry go round"] = ["U+3f0e"]
UNICODE_TO_BLISS["U+3f0e"] = ["merry go round"]
BLISS_TO_UNICODE["carousel"] = ["U+3f0e"]
UNICODE_TO_BLISS["U+3f0e"].append("carousel")
BLISS_TO_UNICODE["merry-go-round,carousel"] = ["U+3f0e"]
UNICODE_TO_BLISS["U+3f0e"].append("merry-go-round,carousel")
BLISS_TO_UNICODE["to circle"] = ["U+3f0f"]
UNICODE_TO_BLISS["U+3f0f"] = ["to circle"]
BLISS_TO_UNICODE["national"] = ["U+3f10"]
UNICODE_TO_BLISS["U+3f10"] = ["national"]
BLISS_TO_UNICODE["indicator descripton"] = ["U+3f11"]
UNICODE_TO_BLISS["U+3f11"] = ["indicator descripton"]
BLISS_TO_UNICODE["to like"] = ["U+3f12"]
UNICODE_TO_BLISS["U+3f12"] = ["to like"]
BLISS_TO_UNICODE["child abuse"] = ["U+3f13"]
UNICODE_TO_BLISS["U+3f13"] = ["child abuse"]
BLISS_TO_UNICODE["that"].append("U+360e")
UNICODE_TO_BLISS["U+360e"].append("that")
BLISS_TO_UNICODE["which"] = ["U+360e"]
UNICODE_TO_BLISS["U+360e"].append("which")
BLISS_TO_UNICODE["who,that,which"] = ["U+360e"]
UNICODE_TO_BLISS["U+360e"].append("who,that,which")
BLISS_TO_UNICODE["double commas or ditto marks"] = ["U+3f14"]
UNICODE_TO_BLISS["U+3f14"] = ["double commas or ditto marks"]
BLISS_TO_UNICODE["which,that"] = ["U+360e"]
UNICODE_TO_BLISS["U+360e"].append("which,that")
BLISS_TO_UNICODE["whom"] = ["U+360e"]
UNICODE_TO_BLISS["U+360e"].append("whom")
BLISS_TO_UNICODE["who,whom,that"] = ["U+360e"]
UNICODE_TO_BLISS["U+360e"].append("who,whom,that")
BLISS_TO_UNICODE["ideograph"] = ["U+3f15"]
UNICODE_TO_BLISS["U+3f15"] = ["ideograph"]
BLISS_TO_UNICODE["television"] = ["U+3f16"]
UNICODE_TO_BLISS["U+3f16"] = ["television"]
BLISS_TO_UNICODE["clarinet"] = ["U+3f17"]
UNICODE_TO_BLISS["U+3f17"] = ["clarinet"]
BLISS_TO_UNICODE["reed instrument"] = ["U+3f17"]
UNICODE_TO_BLISS["U+3f17"].append("reed instrument")
BLISS_TO_UNICODE["clarinet,reed instrument"] = ["U+3f17"]
UNICODE_TO_BLISS["U+3f17"].append("clarinet,reed instrument")
BLISS_TO_UNICODE["how much"] = ["U+3f18"]
UNICODE_TO_BLISS["U+3f18"] = ["how much"]
BLISS_TO_UNICODE["how many"] = ["U+3f18"]
UNICODE_TO_BLISS["U+3f18"].append("how many")
BLISS_TO_UNICODE["how much,how many"] = ["U+3f18"]
UNICODE_TO_BLISS["U+3f18"].append("how much,how many")
BLISS_TO_UNICODE["physiotherapist"] = ["U+3f19"]
UNICODE_TO_BLISS["U+3f19"] = ["physiotherapist"]
BLISS_TO_UNICODE["troublesome"] = ["U+3f1a"]
UNICODE_TO_BLISS["U+3f1a"] = ["troublesome"]
BLISS_TO_UNICODE["trouble"] = ["U+3f1b"]
UNICODE_TO_BLISS["U+3f1b"] = ["trouble"]
BLISS_TO_UNICODE["breakfast"] = ["U+3f1c"]
UNICODE_TO_BLISS["U+3f1c"] = ["breakfast"]
BLISS_TO_UNICODE["lumpy"] = ["U+3f1d"]
UNICODE_TO_BLISS["U+3f1d"] = ["lumpy"]
BLISS_TO_UNICODE["offering"] = ["U+3ed1"]
UNICODE_TO_BLISS["U+3ed1"].append("offering")
BLISS_TO_UNICODE["present"].append("U+3ed1")
UNICODE_TO_BLISS["U+3ed1"].append("present")
BLISS_TO_UNICODE["gift,offering,present"] = ["U+3ed1"]
UNICODE_TO_BLISS["U+3ed1"].append("gift,offering,present")
BLISS_TO_UNICODE["equipment"] = ["U+3f1e"]
UNICODE_TO_BLISS["U+3f1e"] = ["equipment"]
BLISS_TO_UNICODE["gear"] = ["U+3f1e"]
UNICODE_TO_BLISS["U+3f1e"].append("gear")
BLISS_TO_UNICODE["equipment,gear"] = ["U+3f1e"]
UNICODE_TO_BLISS["U+3f1e"].append("equipment,gear")
BLISS_TO_UNICODE["space travel"] = ["U+3f1f"]
UNICODE_TO_BLISS["U+3f1f"] = ["space travel"]
BLISS_TO_UNICODE["space voyage"] = ["U+3f1f"]
UNICODE_TO_BLISS["U+3f1f"].append("space voyage")
BLISS_TO_UNICODE["space flight"] = ["U+3f1f"]
UNICODE_TO_BLISS["U+3f1f"].append("space flight")
BLISS_TO_UNICODE["space travel,space voyage,space flight"] = ["U+3f1f"]
UNICODE_TO_BLISS["U+3f1f"].append("space travel,space voyage,space flight")
BLISS_TO_UNICODE["galaxy"] = ["U+3f20"]
UNICODE_TO_BLISS["U+3f20"] = ["galaxy"]
BLISS_TO_UNICODE["raddled"] = ["U+359d"]
UNICODE_TO_BLISS["U+359d"].append("raddled")
BLISS_TO_UNICODE["worn-out,raddled"] = ["U+359d"]
UNICODE_TO_BLISS["U+359d"].append("worn-out,raddled")
BLISS_TO_UNICODE["disability"] = ["U+3f21"]
UNICODE_TO_BLISS["U+3f21"] = ["disability"]
BLISS_TO_UNICODE["handicap"] = ["U+3f21"]
UNICODE_TO_BLISS["U+3f21"].append("handicap")
BLISS_TO_UNICODE["impairment"] = ["U+3f21"]
UNICODE_TO_BLISS["U+3f21"].append("impairment")
BLISS_TO_UNICODE["disability,handicap,impairment"] = ["U+3f21"]
UNICODE_TO_BLISS["U+3f21"].append("disability,handicap,impairment")
BLISS_TO_UNICODE["begin"] = ["U+3f22"]
UNICODE_TO_BLISS["U+3f22"] = ["begin"]
BLISS_TO_UNICODE["start"].append("U+3f22")
UNICODE_TO_BLISS["U+3f22"].append("start")
BLISS_TO_UNICODE["begin,start"] = ["U+3f22"]
UNICODE_TO_BLISS["U+3f22"].append("begin,start")
BLISS_TO_UNICODE["puncture"] = ["U+3f23"]
UNICODE_TO_BLISS["U+3f23"] = ["puncture"]
BLISS_TO_UNICODE["prick"] = ["U+3f23"]
UNICODE_TO_BLISS["U+3f23"].append("prick")
BLISS_TO_UNICODE["puncture,prick"] = ["U+3f23"]
UNICODE_TO_BLISS["U+3f23"].append("puncture,prick")
BLISS_TO_UNICODE["downhill skiing"] = ["U+3f24"]
UNICODE_TO_BLISS["U+3f24"] = ["downhill skiing"]
BLISS_TO_UNICODE["downward/forward"] = ["U+3f25"]
UNICODE_TO_BLISS["U+3f25"] = ["downward/forward"]
BLISS_TO_UNICODE["airplane landing"] = ["U+3be9"]
UNICODE_TO_BLISS["U+3be9"].append("airplane landing")
BLISS_TO_UNICODE["landing,airplane landing"] = ["U+3be9"]
UNICODE_TO_BLISS["U+3be9"].append("landing,airplane landing")
BLISS_TO_UNICODE["feminine"] = ["U+3451"]
UNICODE_TO_BLISS["U+3451"].append("feminine")
BLISS_TO_UNICODE["female,feminine"] = ["U+3451"]
UNICODE_TO_BLISS["U+3451"].append("female,feminine")
BLISS_TO_UNICODE["dream"] = ["U+3f26"]
UNICODE_TO_BLISS["U+3f26"] = ["dream"]
BLISS_TO_UNICODE["sunset"] = ["U+3f27"]
UNICODE_TO_BLISS["U+3f27"] = ["sunset"]
BLISS_TO_UNICODE["sand play"] = ["U+3f28"]
UNICODE_TO_BLISS["U+3f28"] = ["sand play"]
BLISS_TO_UNICODE["step"] = ["U+3f29"]
UNICODE_TO_BLISS["U+3f29"] = ["step"]
BLISS_TO_UNICODE["stair"] = ["U+3f29"]
UNICODE_TO_BLISS["U+3f29"].append("stair")
BLISS_TO_UNICODE["step,stair"] = ["U+3f29"]
UNICODE_TO_BLISS["U+3f29"].append("step,stair")
BLISS_TO_UNICODE["label"] = ["U+32a7"]
UNICODE_TO_BLISS["U+32a7"].append("label")
BLISS_TO_UNICODE["term"] = ["U+32a7"]
UNICODE_TO_BLISS["U+32a7"].append("term")
BLISS_TO_UNICODE["title"] = ["U+32a7"]
UNICODE_TO_BLISS["U+32a7"].append("title")
BLISS_TO_UNICODE["name,label,term,title"] = ["U+32a7"]
UNICODE_TO_BLISS["U+32a7"].append("name,label,term,title")
BLISS_TO_UNICODE["announcement"] = ["U+3b4b"]
UNICODE_TO_BLISS["U+3b4b"].append("announcement")
BLISS_TO_UNICODE["proclamation,announcement"] = ["U+3b4b"]
UNICODE_TO_BLISS["U+3b4b"].append("proclamation,announcement")
BLISS_TO_UNICODE["to disseminate"] = ["U+3f2a"]
UNICODE_TO_BLISS["U+3f2a"] = ["to disseminate"]
BLISS_TO_UNICODE["scalene triangle"] = ["U+3f2b"]
UNICODE_TO_BLISS["U+3f2b"] = ["scalene triangle"]
BLISS_TO_UNICODE["pumpkin"].append("U+3a46")
UNICODE_TO_BLISS["U+3a46"].append("pumpkin")
BLISS_TO_UNICODE["squash,pumpkin"] = ["U+3a46"]
UNICODE_TO_BLISS["U+3a46"].append("squash,pumpkin")
BLISS_TO_UNICODE["pictograph of thick rind"] = ["U+3f2c"]
UNICODE_TO_BLISS["U+3f2c"] = ["pictograph of thick rind"]
BLISS_TO_UNICODE["pipe organ"] = ["U+366d"]
UNICODE_TO_BLISS["U+366d"].append("pipe organ")
BLISS_TO_UNICODE["organ,pipe organ"] = ["U+366d"]
UNICODE_TO_BLISS["U+366d"].append("organ,pipe organ")
BLISS_TO_UNICODE["vaporization"].append("U+3a8e")
UNICODE_TO_BLISS["U+3a8e"].append("vaporization")
BLISS_TO_UNICODE["spray,vaporization"] = ["U+3a8e"]
UNICODE_TO_BLISS["U+3a8e"].append("spray,vaporization")
BLISS_TO_UNICODE["a cluster of seven dots"] = ["U+3f2d"]
UNICODE_TO_BLISS["U+3f2d"] = ["a cluster of seven dots"]
BLISS_TO_UNICODE["exhibitionism"] = ["U+3f2e"]
UNICODE_TO_BLISS["U+3f2e"] = ["exhibitionism"]
BLISS_TO_UNICODE["immodesty"] = ["U+3f2e"]
UNICODE_TO_BLISS["U+3f2e"].append("immodesty")
BLISS_TO_UNICODE["indecent exposure"] = ["U+3f2e"]
UNICODE_TO_BLISS["U+3f2e"].append("indecent exposure")
BLISS_TO_UNICODE["exhibitionism,immodesty,indecent exposure"] = ["U+3f2e"]
UNICODE_TO_BLISS["U+3f2e"].append("exhibitionism,immodesty,indecent exposure")
BLISS_TO_UNICODE["hose"] = ["U+32bc"]
UNICODE_TO_BLISS["U+32bc"].append("hose")
BLISS_TO_UNICODE["tube"].append("U+32bc")
UNICODE_TO_BLISS["U+32bc"].append("tube")
BLISS_TO_UNICODE["pipe,hose,tube"] = ["U+32bc"]
UNICODE_TO_BLISS["U+32bc"].append("pipe,hose,tube")
BLISS_TO_UNICODE["pipe,tube"] = ["U+32bc"]
UNICODE_TO_BLISS["U+32bc"].append("pipe,tube")
BLISS_TO_UNICODE["leather"] = ["U+3f2f"]
UNICODE_TO_BLISS["U+3f2f"] = ["leather"]
BLISS_TO_UNICODE["animal skin"] = ["U+3f30"]
UNICODE_TO_BLISS["U+3f30"] = ["animal skin"]
BLISS_TO_UNICODE["parking permit"] = ["U+3f31"]
UNICODE_TO_BLISS["U+3f31"] = ["parking permit"]
BLISS_TO_UNICODE["concert"] = ["U+3f32"]
UNICODE_TO_BLISS["U+3f32"] = ["concert"]
BLISS_TO_UNICODE["active"] = ["U+3f33"]
UNICODE_TO_BLISS["U+3f33"] = ["active"]
BLISS_TO_UNICODE["actively"] = ["U+3f33"]
UNICODE_TO_BLISS["U+3f33"].append("actively")
BLISS_TO_UNICODE["active,actively"] = ["U+3f33"]
UNICODE_TO_BLISS["U+3f33"].append("active,actively")
BLISS_TO_UNICODE["jump rope"] = ["U+3f34"]
UNICODE_TO_BLISS["U+3f34"] = ["jump rope"]
BLISS_TO_UNICODE["skipping rope"] = ["U+3f34"]
UNICODE_TO_BLISS["U+3f34"].append("skipping rope")
BLISS_TO_UNICODE["jump rope,skipping rope"] = ["U+3f34"]
UNICODE_TO_BLISS["U+3f34"].append("jump rope,skipping rope")
BLISS_TO_UNICODE["loudspeaker"] = ["U+3f35"]
UNICODE_TO_BLISS["U+3f35"] = ["loudspeaker"]
BLISS_TO_UNICODE["out"] = ["U+3f36"]
UNICODE_TO_BLISS["U+3f36"] = ["out"]
BLISS_TO_UNICODE["cohabitant"] = ["U+342d"]
UNICODE_TO_BLISS["U+342d"].append("cohabitant")
BLISS_TO_UNICODE["partner"] = ["U+342d"]
UNICODE_TO_BLISS["U+342d"].append("partner")
BLISS_TO_UNICODE["spouse,cohabitant,partner"] = ["U+342d"]
UNICODE_TO_BLISS["U+342d"].append("spouse,cohabitant,partner")
BLISS_TO_UNICODE["dressage"] = ["U+3f37"]
UNICODE_TO_BLISS["U+3f37"] = ["dressage"]
BLISS_TO_UNICODE["winter sports"] = ["U+3f38"]
UNICODE_TO_BLISS["U+3f38"] = ["winter sports"]
BLISS_TO_UNICODE["3"].append("U+3563")
UNICODE_TO_BLISS["U+3563"].append("3")
BLISS_TO_UNICODE["Arabic numeral 3"] = ["U+3f39"]
UNICODE_TO_BLISS["U+3f39"] = ["Arabic numeral 3"]
BLISS_TO_UNICODE["skyscraper"] = ["U+3f3a"]
UNICODE_TO_BLISS["U+3f3a"] = ["skyscraper"]
BLISS_TO_UNICODE["two reference lines"] = ["U+3f3b"]
UNICODE_TO_BLISS["U+3f3b"] = ["two reference lines"]
BLISS_TO_UNICODE["tangerine"] = ["U+3f3c"]
UNICODE_TO_BLISS["U+3f3c"] = ["tangerine"]
BLISS_TO_UNICODE["clementine"] = ["U+3f3c"]
UNICODE_TO_BLISS["U+3f3c"].append("clementine")
BLISS_TO_UNICODE["mandarin"] = ["U+3f3c"]
UNICODE_TO_BLISS["U+3f3c"].append("mandarin")
BLISS_TO_UNICODE["tangerine,clementine,mandarin"] = ["U+3f3c"]
UNICODE_TO_BLISS["U+3f3c"].append("tangerine,clementine,mandarin")
BLISS_TO_UNICODE["import"] = ["U+3f3d"]
UNICODE_TO_BLISS["U+3f3d"] = ["import"]
BLISS_TO_UNICODE["artificial respiration"] = ["U+3f3e"]
UNICODE_TO_BLISS["U+3f3e"] = ["artificial respiration"]
BLISS_TO_UNICODE["to breathe"] = ["U+3f3f"]
UNICODE_TO_BLISS["U+3f3f"] = ["to breathe"]
BLISS_TO_UNICODE["health goods shop"] = ["U+3f40"]
UNICODE_TO_BLISS["U+3f40"] = ["health goods shop"]
BLISS_TO_UNICODE["broil"] = ["U+3f41"]
UNICODE_TO_BLISS["U+3f41"] = ["broil"]
BLISS_TO_UNICODE["barbecue"] = ["U+3f41"]
UNICODE_TO_BLISS["U+3f41"].append("barbecue")
BLISS_TO_UNICODE["grill"] = ["U+3f41"]
UNICODE_TO_BLISS["U+3f41"].append("grill")
BLISS_TO_UNICODE["broil,barbecue,grill"] = ["U+3f41"]
UNICODE_TO_BLISS["U+3f41"].append("broil,barbecue,grill")
BLISS_TO_UNICODE["base camp"] = ["U+3f42"]
UNICODE_TO_BLISS["U+3f42"] = ["base camp"]
BLISS_TO_UNICODE["to gather"] = ["U+3f43"]
UNICODE_TO_BLISS["U+3f43"] = ["to gather"]
BLISS_TO_UNICODE["first aid"] = ["U+3f44"]
UNICODE_TO_BLISS["U+3f44"] = ["first aid"]
BLISS_TO_UNICODE["sulky"] = ["U+3f45"]
UNICODE_TO_BLISS["U+3f45"] = ["sulky"]
BLISS_TO_UNICODE["skull"] = ["U+3f46"]
UNICODE_TO_BLISS["U+3f46"] = ["skull"]
BLISS_TO_UNICODE["cranium"] = ["U+3f46"]
UNICODE_TO_BLISS["U+3f46"].append("cranium")
BLISS_TO_UNICODE["skull,cranium"] = ["U+3f46"]
UNICODE_TO_BLISS["U+3f46"].append("skull,cranium")
BLISS_TO_UNICODE["top of a thing"] = ["U+3366"]
UNICODE_TO_BLISS["U+3366"].append("top of a thing")
BLISS_TO_UNICODE["top,top of a thing"] = ["U+3366"]
UNICODE_TO_BLISS["U+3366"].append("top,top of a thing")
BLISS_TO_UNICODE["cycling"] = ["U+3f47"]
UNICODE_TO_BLISS["U+3f47"] = ["cycling"]
BLISS_TO_UNICODE["submerged rock"] = ["U+3f48"]
UNICODE_TO_BLISS["U+3f48"] = ["submerged rock"]
BLISS_TO_UNICODE["dictator"] = ["U+3f49"]
UNICODE_TO_BLISS["U+3f49"] = ["dictator"]
BLISS_TO_UNICODE["dictatorship"] = ["U+3f4a"]
UNICODE_TO_BLISS["U+3f4a"] = ["dictatorship"]
BLISS_TO_UNICODE["stovetop"] = ["U+3f4b"]
UNICODE_TO_BLISS["U+3f4b"] = ["stovetop"]
BLISS_TO_UNICODE["exterior"] = ["U+3f36"]
UNICODE_TO_BLISS["U+3f36"].append("exterior")
BLISS_TO_UNICODE["external"] = ["U+3f36"]
UNICODE_TO_BLISS["U+3f36"].append("external")
BLISS_TO_UNICODE["outside"].append("U+3f36")
UNICODE_TO_BLISS["U+3f36"].append("outside")
BLISS_TO_UNICODE["out,exterior,external,outside"] = ["U+3f36"]
UNICODE_TO_BLISS["U+3f36"].append("out,exterior,external,outside")
BLISS_TO_UNICODE["sand toy"] = ["U+3f4c"]
UNICODE_TO_BLISS["U+3f4c"] = ["sand toy"]
BLISS_TO_UNICODE["navigate airplane"] = ["U+3f4d"]
UNICODE_TO_BLISS["U+3f4d"] = ["navigate airplane"]
BLISS_TO_UNICODE["signsignal"] = ["U+3f4f"]
UNICODE_TO_BLISS["U+3f4f"] = ["signsignal"]
BLISS_TO_UNICODE["action indicator)"] = ["U+3f50"]
UNICODE_TO_BLISS["U+3f50"] = ["action indicator)"]
BLISS_TO_UNICODE["freely"] = ["U+3bf9"]
UNICODE_TO_BLISS["U+3bf9"].append("freely")
BLISS_TO_UNICODE["free,freely"] = ["U+3bf9"]
UNICODE_TO_BLISS["U+3bf9"].append("free,freely")
BLISS_TO_UNICODE["soil"] = ["U+394d"]
UNICODE_TO_BLISS["U+394d"].append("soil")
BLISS_TO_UNICODE["dirt,soil"] = ["U+394d"]
UNICODE_TO_BLISS["U+394d"].append("dirt,soil")
BLISS_TO_UNICODE["squeeze"].append("U+3d9a")
UNICODE_TO_BLISS["U+3d9a"].append("squeeze")
BLISS_TO_UNICODE["hug,squeeze,embrace"] = ["U+3d9a"]
UNICODE_TO_BLISS["U+3d9a"].append("hug,squeeze,embrace")
BLISS_TO_UNICODE["worry"] = ["U+3f51"]
UNICODE_TO_BLISS["U+3f51"] = ["worry"]
BLISS_TO_UNICODE["northward"] = ["U+3f52"]
UNICODE_TO_BLISS["U+3f52"] = ["northward"]
BLISS_TO_UNICODE["develop"] = ["U+3f53"]
UNICODE_TO_BLISS["U+3f53"] = ["develop"]
BLISS_TO_UNICODE["inquire"] = ["U+3cb4"]
UNICODE_TO_BLISS["U+3cb4"].append("inquire")
BLISS_TO_UNICODE["question"].append("U+3cb4")
UNICODE_TO_BLISS["U+3cb4"].append("question")
BLISS_TO_UNICODE["ask,inquire,question"] = ["U+3cb4"]
UNICODE_TO_BLISS["U+3cb4"].append("ask,inquire,question")
BLISS_TO_UNICODE["magnifier"] = ["U+3f54"]
UNICODE_TO_BLISS["U+3f54"] = ["magnifier"]
BLISS_TO_UNICODE["magnifying glass"] = ["U+3f54"]
UNICODE_TO_BLISS["U+3f54"].append("magnifying glass")
BLISS_TO_UNICODE["magnifier,magnifying glass"] = ["U+3f54"]
UNICODE_TO_BLISS["U+3f54"].append("magnifier,magnifying glass")
BLISS_TO_UNICODE["digital document"] = ["U+3d9c"]
UNICODE_TO_BLISS["U+3d9c"].append("digital document")
BLISS_TO_UNICODE["too bad"] = ["U+3f55"]
UNICODE_TO_BLISS["U+3f55"] = ["too bad"]
BLISS_TO_UNICODE["I'm sorry"] = ["U+3f55"]
UNICODE_TO_BLISS["U+3f55"].append("I'm sorry")
BLISS_TO_UNICODE["I'm so sorry"] = ["U+3f55"]
UNICODE_TO_BLISS["U+3f55"].append("I'm so sorry")
BLISS_TO_UNICODE["too bad,I'm sorry,I'm so sorry"] = ["U+3f55"]
UNICODE_TO_BLISS["U+3f55"].append("too bad,I'm sorry,I'm so sorry")
BLISS_TO_UNICODE["ruler"] = ["U+3f56"]
UNICODE_TO_BLISS["U+3f56"] = ["ruler"]
BLISS_TO_UNICODE["measuring stick"] = ["U+3f56"]
UNICODE_TO_BLISS["U+3f56"].append("measuring stick")
BLISS_TO_UNICODE["tapeline"] = ["U+3f56"]
UNICODE_TO_BLISS["U+3f56"].append("tapeline")
BLISS_TO_UNICODE["tape measure"] = ["U+3f56"]
UNICODE_TO_BLISS["U+3f56"].append("tape measure")
BLISS_TO_UNICODE["ruler,measuring stick,tapeline,tape measure"] = ["U+3f56"]
UNICODE_TO_BLISS["U+3f56"].append("ruler,measuring stick,tapeline,tape measure")
BLISS_TO_UNICODE["foal"] = ["U+3f57"]
UNICODE_TO_BLISS["U+3f57"] = ["foal"]
BLISS_TO_UNICODE["cymbal"] = ["U+3f58"]
UNICODE_TO_BLISS["U+3f58"] = ["cymbal"]
BLISS_TO_UNICODE["pictograph of wedge shape"] = ["U+3f59"]
UNICODE_TO_BLISS["U+3f59"] = ["pictograph of wedge shape"]
BLISS_TO_UNICODE["Arabic numeral 2 small"] = ["U+3f5a"]
UNICODE_TO_BLISS["U+3f5a"] = ["Arabic numeral 2 small"]
BLISS_TO_UNICODE["robot doll"] = ["U+3f5b"]
UNICODE_TO_BLISS["U+3f5b"] = ["robot doll"]
BLISS_TO_UNICODE["United Kingdom"] = ["U+3f5c"]
UNICODE_TO_BLISS["U+3f5c"] = ["United Kingdom"]
BLISS_TO_UNICODE["Union Jack pattern"] = ["U+3f5d"]
UNICODE_TO_BLISS["U+3f5d"] = ["Union Jack pattern"]
BLISS_TO_UNICODE["breeze"] = ["U+3f5e"]
UNICODE_TO_BLISS["U+3f5e"] = ["breeze"]
BLISS_TO_UNICODE["foremother"] = ["U+3f5f"]
UNICODE_TO_BLISS["U+3f5f"] = ["foremother"]
BLISS_TO_UNICODE["joystick"] = ["U+3f60"]
UNICODE_TO_BLISS["U+3f60"] = ["joystick"]
BLISS_TO_UNICODE["have a view"] = ["U+3f61"]
UNICODE_TO_BLISS["U+3f61"] = ["have a view"]
BLISS_TO_UNICODE["have an opinion"] = ["U+3f61"]
UNICODE_TO_BLISS["U+3f61"].append("have an opinion")
BLISS_TO_UNICODE["have a view,have an opinion"] = ["U+3f61"]
UNICODE_TO_BLISS["U+3f61"].append("have a view,have an opinion")
BLISS_TO_UNICODE["broadcast"].append("U+385a")
UNICODE_TO_BLISS["U+385a"].append("broadcast")
BLISS_TO_UNICODE["transmitting"] = ["U+385a"]
UNICODE_TO_BLISS["U+385a"].append("transmitting")
BLISS_TO_UNICODE["signal,broadcast,transmitting"] = ["U+385a"]
UNICODE_TO_BLISS["U+385a"].append("signal,broadcast,transmitting")
BLISS_TO_UNICODE["scabies"] = ["U+3f62"]
UNICODE_TO_BLISS["U+3f62"] = ["scabies"]
BLISS_TO_UNICODE["ammeter"] = ["U+3f63"]
UNICODE_TO_BLISS["U+3f63"] = ["ammeter"]
BLISS_TO_UNICODE["feel"] = ["U+3c0f"]
UNICODE_TO_BLISS["U+3c0f"].append("feel")
BLISS_TO_UNICODE["touch,feel"] = ["U+3c0f"]
UNICODE_TO_BLISS["U+3c0f"].append("touch,feel")
BLISS_TO_UNICODE["touching"] = ["U+3c0f"]
UNICODE_TO_BLISS["U+3c0f"].append("touching")
BLISS_TO_UNICODE["touch,touching"] = ["U+3c0f"]
UNICODE_TO_BLISS["U+3c0f"].append("touch,touching")
BLISS_TO_UNICODE["gastrointestinal system"] = ["U+3f64"]
UNICODE_TO_BLISS["U+3f64"] = ["gastrointestinal system"]
BLISS_TO_UNICODE["speed"] = ["U+3f65"]
UNICODE_TO_BLISS["U+3f65"] = ["speed"]
BLISS_TO_UNICODE["to cross out"] = ["U+3f66"]
UNICODE_TO_BLISS["U+3f66"] = ["to cross out"]
BLISS_TO_UNICODE["improvement"] = ["U+3f67"]
UNICODE_TO_BLISS["U+3f67"] = ["improvement"]
BLISS_TO_UNICODE["Family Day"] = ["U+3f68"]
UNICODE_TO_BLISS["U+3f68"] = ["Family Day"]
BLISS_TO_UNICODE["treatment"] = ["U+3f69"]
UNICODE_TO_BLISS["U+3f69"] = ["treatment"]
BLISS_TO_UNICODE["read"] = ["U+3f6a"]
UNICODE_TO_BLISS["U+3f6a"] = ["read"]
BLISS_TO_UNICODE["early"] = ["U+3f6b"]
UNICODE_TO_BLISS["U+3f6b"] = ["early"]
BLISS_TO_UNICODE["dust storm"] = ["U+3f6c"]
UNICODE_TO_BLISS["U+3f6c"] = ["dust storm"]
BLISS_TO_UNICODE["duster"] = ["U+3f6c"]
UNICODE_TO_BLISS["U+3f6c"].append("duster")
BLISS_TO_UNICODE["sirocco"] = ["U+3f6c"]
UNICODE_TO_BLISS["U+3f6c"].append("sirocco")
BLISS_TO_UNICODE["dust storm,duster,sirocco"] = ["U+3f6c"]
UNICODE_TO_BLISS["U+3f6c"].append("dust storm,duster,sirocco")
BLISS_TO_UNICODE["storm"] = ["U+3f6d"]
UNICODE_TO_BLISS["U+3f6d"] = ["storm"]
BLISS_TO_UNICODE["back of a thing"] = ["U+33eb"]
UNICODE_TO_BLISS["U+33eb"].append("back of a thing")
BLISS_TO_UNICODE["rear,back of a thing"] = ["U+33eb"]
UNICODE_TO_BLISS["U+33eb"].append("rear,back of a thing")
BLISS_TO_UNICODE["fortune"] = ["U+37f4"]
UNICODE_TO_BLISS["U+37f4"].append("fortune")
BLISS_TO_UNICODE["luck,fortune"] = ["U+37f4"]
UNICODE_TO_BLISS["U+37f4"].append("luck,fortune")
BLISS_TO_UNICODE["incest"] = ["U+3f6e"]
UNICODE_TO_BLISS["U+3f6e"] = ["incest"]
BLISS_TO_UNICODE["miracle"] = ["U+3f6f"]
UNICODE_TO_BLISS["U+3f6f"] = ["miracle"]
BLISS_TO_UNICODE["malodor"] = ["U+3f70"]
UNICODE_TO_BLISS["U+3f70"] = ["malodor"]
BLISS_TO_UNICODE["malodour"] = ["U+3f70"]
UNICODE_TO_BLISS["U+3f70"].append("malodour")
BLISS_TO_UNICODE["stench"] = ["U+3f70"]
UNICODE_TO_BLISS["U+3f70"].append("stench")
BLISS_TO_UNICODE["malodor,malodour,stench"] = ["U+3f70"]
UNICODE_TO_BLISS["U+3f70"].append("malodor,malodour,stench")
BLISS_TO_UNICODE["blackberry"] = ["U+32c4"]
UNICODE_TO_BLISS["U+32c4"].append("blackberry")
BLISS_TO_UNICODE["compound berry"] = ["U+32c4"]
UNICODE_TO_BLISS["U+32c4"].append("compound berry")
BLISS_TO_UNICODE["raspberry,blackberry,compound berry"] = ["U+32c4"]
UNICODE_TO_BLISS["U+32c4"].append("raspberry,blackberry,compound berry")
BLISS_TO_UNICODE["downward"].append("U+3698")
UNICODE_TO_BLISS["U+3698"].append("downward")
BLISS_TO_UNICODE["down,downward"] = ["U+3698"]
UNICODE_TO_BLISS["U+3698"].append("down,downward")
BLISS_TO_UNICODE["blog"] = ["U+3f71"]
UNICODE_TO_BLISS["U+3f71"] = ["blog"]
BLISS_TO_UNICODE["web blog"] = ["U+3f71"]
UNICODE_TO_BLISS["U+3f71"].append("web blog")
BLISS_TO_UNICODE["blog,web blog"] = ["U+3f71"]
UNICODE_TO_BLISS["U+3f71"].append("blog,web blog")
BLISS_TO_UNICODE["astronomer"] = ["U+3f72"]
UNICODE_TO_BLISS["U+3f72"] = ["astronomer"]
BLISS_TO_UNICODE["astronomy"] = ["U+3f73"]
UNICODE_TO_BLISS["U+3f73"] = ["astronomy"]
BLISS_TO_UNICODE["hab)"] = ["U+35d1"]
UNICODE_TO_BLISS["U+35d1"].append("hab)")
BLISS_TO_UNICODE["Mars"] = ["U+3f74"]
UNICODE_TO_BLISS["U+3f74"] = ["Mars"]
BLISS_TO_UNICODE["Mary"] = ["U+3f75"]
UNICODE_TO_BLISS["U+3f75"] = ["Mary"]
BLISS_TO_UNICODE["capability"] = ["U+3822"]
UNICODE_TO_BLISS["U+3822"].append("capability")
BLISS_TO_UNICODE["capacity"] = ["U+3822"]
UNICODE_TO_BLISS["U+3822"].append("capacity")
BLISS_TO_UNICODE["potential"] = ["U+3822"]
UNICODE_TO_BLISS["U+3822"].append("potential")
BLISS_TO_UNICODE["ability,capability,capacity,potential"] = ["U+3822"]
UNICODE_TO_BLISS["U+3822"].append("ability,capability,capacity,potential")
BLISS_TO_UNICODE["babysitter"] = ["U+3f76"]
UNICODE_TO_BLISS["U+3f76"] = ["babysitter"]
BLISS_TO_UNICODE["recorder"].append("U+3e7c")
UNICODE_TO_BLISS["U+3e7c"].append("recorder")
BLISS_TO_UNICODE["flute,recorder"] = ["U+3e7c"]
UNICODE_TO_BLISS["U+3e7c"].append("flute,recorder")
BLISS_TO_UNICODE["alto"] = ["U+3f77"]
UNICODE_TO_BLISS["U+3f77"] = ["alto"]
BLISS_TO_UNICODE["assembly"] = ["U+3251"]
UNICODE_TO_BLISS["U+3251"].append("assembly")
BLISS_TO_UNICODE["meeting"].append("U+3251")
UNICODE_TO_BLISS["U+3251"].append("meeting")
BLISS_TO_UNICODE["conference"] = ["U+3251"]
UNICODE_TO_BLISS["U+3251"].append("conference")
BLISS_TO_UNICODE["gathering,assembly,meeting,conference"] = ["U+3251"]
UNICODE_TO_BLISS["U+3251"].append("gathering,assembly,meeting,conference")
BLISS_TO_UNICODE["assembly"].append("U+38a2")
UNICODE_TO_BLISS["U+38a2"].append("assembly")
BLISS_TO_UNICODE["conference"].append("U+38a2")
UNICODE_TO_BLISS["U+38a2"].append("conference")
BLISS_TO_UNICODE["meeting,assembly,conference"] = ["U+38a2"]
UNICODE_TO_BLISS["U+38a2"].append("meeting,assembly,conference")
BLISS_TO_UNICODE["cleaning tool"] = ["U+3f78"]
UNICODE_TO_BLISS["U+3f78"] = ["cleaning tool"]
BLISS_TO_UNICODE["Frigg"] = ["U+3f79"]
UNICODE_TO_BLISS["U+3f79"] = ["Frigg"]
BLISS_TO_UNICODE["gather"] = ["U+3f7a"]
UNICODE_TO_BLISS["U+3f7a"] = ["gather"]
BLISS_TO_UNICODE["assemble"] = ["U+3f7a"]
UNICODE_TO_BLISS["U+3f7a"].append("assemble")
BLISS_TO_UNICODE["gather,assemble"] = ["U+3f7a"]
UNICODE_TO_BLISS["U+3f7a"].append("gather,assemble")
BLISS_TO_UNICODE["bazaar"] = ["U+3f7b"]
UNICODE_TO_BLISS["U+3f7b"] = ["bazaar"]
BLISS_TO_UNICODE["kite flying"] = ["U+3f7c"]
UNICODE_TO_BLISS["U+3f7c"] = ["kite flying"]
BLISS_TO_UNICODE["T shirt"] = ["U+3f7d"]
UNICODE_TO_BLISS["U+3f7d"] = ["T shirt"]
BLISS_TO_UNICODE["tee shirt"] = ["U+3f7d"]
UNICODE_TO_BLISS["U+3f7d"].append("tee shirt")
BLISS_TO_UNICODE["jersey"] = ["U+3f7d"]
UNICODE_TO_BLISS["U+3f7d"].append("jersey")
BLISS_TO_UNICODE["T-shirt,tee shirt,jersey"] = ["U+3f7d"]
UNICODE_TO_BLISS["U+3f7d"].append("T-shirt,tee shirt,jersey")
BLISS_TO_UNICODE["T"] = ["U+3f7e"]
UNICODE_TO_BLISS["U+3f7e"] = ["T"]
BLISS_TO_UNICODE["chop"] = ["U+3f7f"]
UNICODE_TO_BLISS["U+3f7f"] = ["chop"]
BLISS_TO_UNICODE["testimony"] = ["U+3f80"]
UNICODE_TO_BLISS["U+3f80"] = ["testimony"]
BLISS_TO_UNICODE["expose oneself indecently"] = ["U+3f81"]
UNICODE_TO_BLISS["U+3f81"] = ["expose oneself indecently"]
BLISS_TO_UNICODE["furnace"] = ["U+3ad5"]
UNICODE_TO_BLISS["U+3ad5"].append("furnace")
BLISS_TO_UNICODE["heater"].append("U+3ad5")
UNICODE_TO_BLISS["U+3ad5"].append("heater")
BLISS_TO_UNICODE["oven"].append("U+3ad5")
UNICODE_TO_BLISS["U+3ad5"].append("oven")
BLISS_TO_UNICODE["stove,furnace,heater,oven"] = ["U+3ad5"]
UNICODE_TO_BLISS["U+3ad5"].append("stove,furnace,heater,oven")
BLISS_TO_UNICODE["disinfectant"] = ["U+3f82"]
UNICODE_TO_BLISS["U+3f82"] = ["disinfectant"]
BLISS_TO_UNICODE["antiseptic"] = ["U+3f82"]
UNICODE_TO_BLISS["U+3f82"].append("antiseptic")
BLISS_TO_UNICODE["disinfectant,antiseptic"] = ["U+3f82"]
UNICODE_TO_BLISS["U+3f82"].append("disinfectant,antiseptic")
BLISS_TO_UNICODE["washing"] = ["U+3f83"]
UNICODE_TO_BLISS["U+3f83"] = ["washing"]
BLISS_TO_UNICODE["all gone"] = ["U+3f84"]
UNICODE_TO_BLISS["U+3f84"] = ["all gone"]
BLISS_TO_UNICODE["to take away"] = ["U+3f85"]
UNICODE_TO_BLISS["U+3f85"] = ["to take away"]
BLISS_TO_UNICODE["earring"] = ["U+3f86"]
UNICODE_TO_BLISS["U+3f86"] = ["earring"]
BLISS_TO_UNICODE["jewelry"] = ["U+3f87"]
UNICODE_TO_BLISS["U+3f87"] = ["jewelry"]
BLISS_TO_UNICODE["celeriac"] = ["U+3f88"]
UNICODE_TO_BLISS["U+3f88"] = ["celeriac"]
BLISS_TO_UNICODE["celery"].append("U+3f88")
UNICODE_TO_BLISS["U+3f88"].append("celery")
BLISS_TO_UNICODE["celeriac,celery"] = ["U+3f88"]
UNICODE_TO_BLISS["U+3f88"].append("celeriac,celery")
BLISS_TO_UNICODE["give artificial respiration"] = ["U+3f89"]
UNICODE_TO_BLISS["U+3f89"] = ["give artificial respiration"]
BLISS_TO_UNICODE["resuscitate"] = ["U+3f89"]
UNICODE_TO_BLISS["U+3f89"].append("resuscitate")
BLISS_TO_UNICODE["revive"] = ["U+3f89"]
UNICODE_TO_BLISS["U+3f89"].append("revive")
BLISS_TO_UNICODE["give artificial respiration,resuscitate,revive"] = ["U+3f89"]
UNICODE_TO_BLISS["U+3f89"].append("give artificial respiration,resuscitate,revive")
BLISS_TO_UNICODE["dancing therapy"] = ["U+3f8a"]
UNICODE_TO_BLISS["U+3f8a"] = ["dancing therapy"]
BLISS_TO_UNICODE["your"] = ["U+3f8b"]
UNICODE_TO_BLISS["U+3f8b"] = ["your"]
BLISS_TO_UNICODE["yours"] = ["U+3f8b"]
UNICODE_TO_BLISS["U+3f8b"].append("yours")
BLISS_TO_UNICODE["your,yours"] = ["U+3f8b"]
UNICODE_TO_BLISS["U+3f8b"].append("your,yours")
BLISS_TO_UNICODE["grater"] = ["U+3f8c"]
UNICODE_TO_BLISS["U+3f8c"] = ["grater"]
BLISS_TO_UNICODE["grinder"] = ["U+3f8c"]
UNICODE_TO_BLISS["U+3f8c"].append("grinder")
BLISS_TO_UNICODE["grater,grinder"] = ["U+3f8c"]
UNICODE_TO_BLISS["U+3f8c"].append("grater,grinder")
BLISS_TO_UNICODE["log"] = ["U+3d18"]
UNICODE_TO_BLISS["U+3d18"].append("log")
BLISS_TO_UNICODE["stick,log"] = ["U+3d18"]
UNICODE_TO_BLISS["U+3d18"].append("stick,log")
BLISS_TO_UNICODE["start"].append("U+34de")
UNICODE_TO_BLISS["U+34de"].append("start")
BLISS_TO_UNICODE["beginning,start"] = ["U+34de"]
UNICODE_TO_BLISS["U+34de"].append("beginning,start")
BLISS_TO_UNICODE["short"].append("U+34c3")
UNICODE_TO_BLISS["U+34c3"].append("short")
BLISS_TO_UNICODE["low,short"] = ["U+34c3"]
UNICODE_TO_BLISS["U+34c3"].append("low,short")
BLISS_TO_UNICODE["fashion designer"] = ["U+3f8d"]
UNICODE_TO_BLISS["U+3f8d"] = ["fashion designer"]
BLISS_TO_UNICODE["jug"] = ["U+3548"]
UNICODE_TO_BLISS["U+3548"].append("jug")
BLISS_TO_UNICODE["kettle"].append("U+3548")
UNICODE_TO_BLISS["U+3548"].append("kettle")
BLISS_TO_UNICODE["pot"].append("U+3548")
UNICODE_TO_BLISS["U+3548"].append("pot")
BLISS_TO_UNICODE["pitcher,jug,kettle,pot"] = ["U+3548"]
UNICODE_TO_BLISS["U+3548"].append("pitcher,jug,kettle,pot")
BLISS_TO_UNICODE["pictograph with handle and spout"] = ["U+3f8e"]
UNICODE_TO_BLISS["U+3f8e"] = ["pictograph with handle and spout"]
BLISS_TO_UNICODE["omelette"] = ["U+3f8f"]
UNICODE_TO_BLISS["U+3f8f"] = ["omelette"]
BLISS_TO_UNICODE["omelet"] = ["U+3f8f"]
UNICODE_TO_BLISS["U+3f8f"].append("omelet")
BLISS_TO_UNICODE["omelette,omelet"] = ["U+3f8f"]
UNICODE_TO_BLISS["U+3f8f"].append("omelette,omelet")
BLISS_TO_UNICODE["cabin"] = ["U+3f90"]
UNICODE_TO_BLISS["U+3f90"] = ["cabin"]
BLISS_TO_UNICODE["cottage"] = ["U+3f90"]
UNICODE_TO_BLISS["U+3f90"].append("cottage")
BLISS_TO_UNICODE["hut"] = ["U+3f90"]
UNICODE_TO_BLISS["U+3f90"].append("hut")
BLISS_TO_UNICODE["cabin,cottage,hut"] = ["U+3f90"]
UNICODE_TO_BLISS["U+3f90"].append("cabin,cottage,hut")
BLISS_TO_UNICODE["pictograph of head and neck and one hump"] = ["U+3f91"]
UNICODE_TO_BLISS["U+3f91"] = ["pictograph of head and neck and one hump"]
BLISS_TO_UNICODE["sorrow"] = ["U+3841"]
UNICODE_TO_BLISS["U+3841"].append("sorrow")
BLISS_TO_UNICODE["unhappiness"] = ["U+3841"]
UNICODE_TO_BLISS["U+3841"].append("unhappiness")
BLISS_TO_UNICODE["sadness,sorrow,unhappiness"] = ["U+3841"]
UNICODE_TO_BLISS["U+3841"].append("sadness,sorrow,unhappiness")
BLISS_TO_UNICODE["rowing boat"] = ["U+3f92"]
UNICODE_TO_BLISS["U+3f92"] = ["rowing boat"]
BLISS_TO_UNICODE["oar"] = ["U+3f93"]
UNICODE_TO_BLISS["U+3f93"] = ["oar"]
BLISS_TO_UNICODE["cornmeal"] = ["U+3f94"]
UNICODE_TO_BLISS["U+3f94"] = ["cornmeal"]
BLISS_TO_UNICODE["describe"] = ["U+3f95"]
UNICODE_TO_BLISS["U+3f95"] = ["describe"]
BLISS_TO_UNICODE["farfalle"] = ["U+3f96"]
UNICODE_TO_BLISS["U+3f96"] = ["farfalle"]
BLISS_TO_UNICODE["trace"] = ["U+36a8"]
UNICODE_TO_BLISS["U+36a8"].append("trace")
BLISS_TO_UNICODE["track"].append("U+36a8")
UNICODE_TO_BLISS["U+36a8"].append("track")
BLISS_TO_UNICODE["imprint,trace,track"] = ["U+36a8"]
UNICODE_TO_BLISS["U+36a8"].append("imprint,trace,track")
BLISS_TO_UNICODE["effekt"] = ["U+3f97"]
UNICODE_TO_BLISS["U+3f97"] = ["effekt"]
BLISS_TO_UNICODE["sheath"] = ["U+3f98"]
UNICODE_TO_BLISS["U+3f98"] = ["sheath"]
BLISS_TO_UNICODE["H"] = ["U+3f99"]
UNICODE_TO_BLISS["U+3f99"] = ["H"]
BLISS_TO_UNICODE["A"] = ["U+3f9a"]
UNICODE_TO_BLISS["U+3f9a"] = ["A"]
BLISS_TO_UNICODE["washing machine"] = ["U+3f9b"]
UNICODE_TO_BLISS["U+3f9b"] = ["washing machine"]
BLISS_TO_UNICODE["washer"] = ["U+3f9b"]
UNICODE_TO_BLISS["U+3f9b"].append("washer")
BLISS_TO_UNICODE["washing machine,washer"] = ["U+3f9b"]
UNICODE_TO_BLISS["U+3f9b"].append("washing machine,washer")
BLISS_TO_UNICODE["housekeeping"].append("U+3df0")
UNICODE_TO_BLISS["U+3df0"].append("housekeeping")
BLISS_TO_UNICODE["housework"].append("U+3df0")
UNICODE_TO_BLISS["U+3df0"].append("housework")
BLISS_TO_UNICODE["house work,housekeeping,housework"] = ["U+3df0"]
UNICODE_TO_BLISS["U+3df0"].append("house work,housekeeping,housework")
BLISS_TO_UNICODE["housekeep"] = ["U+3f9c"]
UNICODE_TO_BLISS["U+3f9c"] = ["housekeep"]
BLISS_TO_UNICODE["housework"].append("U+3f9c")
UNICODE_TO_BLISS["U+3f9c"].append("housework")
BLISS_TO_UNICODE["housekeep,housework"] = ["U+3f9c"]
UNICODE_TO_BLISS["U+3f9c"].append("housekeep,housework")
BLISS_TO_UNICODE["paten"] = ["U+3f9d"]
UNICODE_TO_BLISS["U+3f9d"] = ["paten"]
BLISS_TO_UNICODE["holy tray"] = ["U+3f9d"]
UNICODE_TO_BLISS["U+3f9d"].append("holy tray")
BLISS_TO_UNICODE["paten,holy tray"] = ["U+3f9d"]
UNICODE_TO_BLISS["U+3f9d"].append("paten,holy tray")
BLISS_TO_UNICODE["yourselves"] = ["U+3652"]
UNICODE_TO_BLISS["U+3652"].append("yourselves")
BLISS_TO_UNICODE["you,yourselves"] = ["U+3652"]
UNICODE_TO_BLISS["U+3652"].append("you,yourselves")
BLISS_TO_UNICODE["houseboat"] = ["U+3f9e"]
UNICODE_TO_BLISS["U+3f9e"] = ["houseboat"]
BLISS_TO_UNICODE["poor"] = ["U+3f9f"]
UNICODE_TO_BLISS["U+3f9f"] = ["poor"]
BLISS_TO_UNICODE["fledgeling"] = ["U+3fa0"]
UNICODE_TO_BLISS["U+3fa0"] = ["fledgeling"]
BLISS_TO_UNICODE["pictograph with stem"] = ["U+3fa1"]
UNICODE_TO_BLISS["U+3fa1"] = ["pictograph with stem"]
BLISS_TO_UNICODE["tip"] = ["U+390c"]
UNICODE_TO_BLISS["U+390c"].append("tip")
BLISS_TO_UNICODE["peak"] = ["U+390c"]
UNICODE_TO_BLISS["U+390c"].append("peak")
BLISS_TO_UNICODE["point,tip,peak"] = ["U+390c"]
UNICODE_TO_BLISS["U+390c"].append("point,tip,peak")
BLISS_TO_UNICODE["ugly"] = ["U+3fa2"]
UNICODE_TO_BLISS["U+3fa2"] = ["ugly"]
BLISS_TO_UNICODE["unattractive"] = ["U+3fa2"]
UNICODE_TO_BLISS["U+3fa2"].append("unattractive")
BLISS_TO_UNICODE["ugly,unattractive"] = ["U+3fa2"]
UNICODE_TO_BLISS["U+3fa2"].append("ugly,unattractive")
BLISS_TO_UNICODE["cupcake"] = ["U+3fa3"]
UNICODE_TO_BLISS["U+3fa3"] = ["cupcake"]
BLISS_TO_UNICODE["fancy cake"] = ["U+3fa3"]
UNICODE_TO_BLISS["U+3fa3"].append("fancy cake")
BLISS_TO_UNICODE["pastry"] = ["U+3fa3"]
UNICODE_TO_BLISS["U+3fa3"].append("pastry")
BLISS_TO_UNICODE["cupcake,fancy cake,pastry"] = ["U+3fa3"]
UNICODE_TO_BLISS["U+3fa3"].append("cupcake,fancy cake,pastry")
BLISS_TO_UNICODE["pool"].append("U+36f5")
UNICODE_TO_BLISS["U+36f5"].append("pool")
BLISS_TO_UNICODE["puddle,pool"] = ["U+36f5"]
UNICODE_TO_BLISS["U+36f5"].append("puddle,pool")
BLISS_TO_UNICODE["condensation"] = ["U+3fa4"]
UNICODE_TO_BLISS["U+3fa4"] = ["condensation"]
BLISS_TO_UNICODE["seven dots"] = ["U+3fa5"]
UNICODE_TO_BLISS["U+3fa5"] = ["seven dots"]
BLISS_TO_UNICODE["motorboat sport"] = ["U+3fa6"]
UNICODE_TO_BLISS["U+3fa6"] = ["motorboat sport"]
BLISS_TO_UNICODE["last month"] = ["U+3fa7"]
UNICODE_TO_BLISS["U+3fa7"] = ["last month"]
BLISS_TO_UNICODE["skeleton"] = ["U+3fa8"]
UNICODE_TO_BLISS["U+3fa8"] = ["skeleton"]
BLISS_TO_UNICODE["unrest"] = ["U+3486"]
UNICODE_TO_BLISS["U+3486"].append("unrest")
BLISS_TO_UNICODE["disturbance,unrest"] = ["U+3486"]
UNICODE_TO_BLISS["U+3486"].append("disturbance,unrest")
BLISS_TO_UNICODE["considerate"] = ["U+3fa9"]
UNICODE_TO_BLISS["U+3fa9"] = ["considerate"]
BLISS_TO_UNICODE["thoughtful"] = ["U+3fa9"]
UNICODE_TO_BLISS["U+3fa9"].append("thoughtful")
BLISS_TO_UNICODE["considerate,thoughtful"] = ["U+3fa9"]
UNICODE_TO_BLISS["U+3fa9"].append("considerate,thoughtful")
BLISS_TO_UNICODE["other)"] = ["U+3faa"]
UNICODE_TO_BLISS["U+3faa"] = ["other)"]
BLISS_TO_UNICODE["cardiologist"] = ["U+3fab"]
UNICODE_TO_BLISS["U+3fab"] = ["cardiologist"]
BLISS_TO_UNICODE["spike"] = ["U+322b"]
UNICODE_TO_BLISS["U+322b"].append("spike")
BLISS_TO_UNICODE["capitulum"] = ["U+322b"]
UNICODE_TO_BLISS["U+322b"].append("capitulum")
BLISS_TO_UNICODE["ear,spike,capitulum"] = ["U+322b"]
UNICODE_TO_BLISS["U+322b"].append("ear,spike,capitulum")
BLISS_TO_UNICODE["handball"] = ["U+3fac"]
UNICODE_TO_BLISS["U+3fac"] = ["handball"]
BLISS_TO_UNICODE["Moses"] = ["U+3fad"]
UNICODE_TO_BLISS["U+3fad"] = ["Moses"]
BLISS_TO_UNICODE["religious"] = ["U+3fae"]
UNICODE_TO_BLISS["U+3fae"] = ["religious"]
BLISS_TO_UNICODE["rug"] = ["U+3faf"]
UNICODE_TO_BLISS["U+3faf"] = ["rug"]
BLISS_TO_UNICODE["carpet"] = ["U+3faf"]
UNICODE_TO_BLISS["U+3faf"].append("carpet")
BLISS_TO_UNICODE["mat"] = ["U+3faf"]
UNICODE_TO_BLISS["U+3faf"].append("mat")
BLISS_TO_UNICODE["rug,carpet,mat"] = ["U+3faf"]
UNICODE_TO_BLISS["U+3faf"].append("rug,carpet,mat")
BLISS_TO_UNICODE["dumpling"] = ["U+3fb0"]
UNICODE_TO_BLISS["U+3fb0"] = ["dumpling"]
BLISS_TO_UNICODE["fountain"] = ["U+3fb1"]
UNICODE_TO_BLISS["U+3fb1"] = ["fountain"]
BLISS_TO_UNICODE["bathroom"] = ["U+3fb2"]
UNICODE_TO_BLISS["U+3fb2"] = ["bathroom"]
BLISS_TO_UNICODE["washroom"] = ["U+3fb2"]
UNICODE_TO_BLISS["U+3fb2"].append("washroom")
BLISS_TO_UNICODE["bathroom,washroom"] = ["U+3fb2"]
UNICODE_TO_BLISS["U+3fb2"].append("bathroom,washroom")
BLISS_TO_UNICODE["screwdriver"] = ["U+3fb3"]
UNICODE_TO_BLISS["U+3fb3"] = ["screwdriver"]
BLISS_TO_UNICODE["gift shop"] = ["U+3fb4"]
UNICODE_TO_BLISS["U+3fb4"] = ["gift shop"]
BLISS_TO_UNICODE["decide"] = ["U+3fb5"]
UNICODE_TO_BLISS["U+3fb5"] = ["decide"]
BLISS_TO_UNICODE["glass jar"] = ["U+3fb6"]
UNICODE_TO_BLISS["U+3fb6"] = ["glass jar"]
BLISS_TO_UNICODE["study"] = ["U+3fb7"]
UNICODE_TO_BLISS["U+3fb7"] = ["study"]
BLISS_TO_UNICODE["learning"] = ["U+3fb8"]
UNICODE_TO_BLISS["U+3fb8"] = ["learning"]
BLISS_TO_UNICODE["wall"].append("U+3229")
UNICODE_TO_BLISS["U+3229"].append("wall")
BLISS_TO_UNICODE["fence,wall"] = ["U+3229"]
UNICODE_TO_BLISS["U+3229"].append("fence,wall")
BLISS_TO_UNICODE["orgasm"] = ["U+3fb9"]
UNICODE_TO_BLISS["U+3fb9"] = ["orgasm"]
BLISS_TO_UNICODE["ecstacy"] = ["U+3fba"]
UNICODE_TO_BLISS["U+3fba"] = ["ecstacy"]
BLISS_TO_UNICODE["protractor"] = ["U+3fbb"]
UNICODE_TO_BLISS["U+3fbb"] = ["protractor"]
BLISS_TO_UNICODE["suicide"] = ["U+3fbc"]
UNICODE_TO_BLISS["U+3fbc"] = ["suicide"]
BLISS_TO_UNICODE["trunk"].append("U+3343")
UNICODE_TO_BLISS["U+3343"].append("trunk")
BLISS_TO_UNICODE["body,trunk"] = ["U+3343"]
UNICODE_TO_BLISS["U+3343"].append("body,trunk")
BLISS_TO_UNICODE["powerful"].append("U+33e0")
UNICODE_TO_BLISS["U+33e0"].append("powerful")
BLISS_TO_UNICODE["strong,powerful"] = ["U+33e0"]
UNICODE_TO_BLISS["U+33e0"].append("strong,powerful")
BLISS_TO_UNICODE["strength"] = ["U+3fbd"]
UNICODE_TO_BLISS["U+3fbd"] = ["strength"]
BLISS_TO_UNICODE["frustrating"] = ["U+3fbe"]
UNICODE_TO_BLISS["U+3fbe"] = ["frustrating"]
BLISS_TO_UNICODE["inspired"] = ["U+3fbf"]
UNICODE_TO_BLISS["U+3fbf"] = ["inspired"]
BLISS_TO_UNICODE["soldier"] = ["U+3fc0"]
UNICODE_TO_BLISS["U+3fc0"] = ["soldier"]
BLISS_TO_UNICODE["warrior"] = ["U+3fc0"]
UNICODE_TO_BLISS["U+3fc0"].append("warrior")
BLISS_TO_UNICODE["soldier,warrior"] = ["U+3fc0"]
UNICODE_TO_BLISS["U+3fc0"].append("soldier,warrior")
BLISS_TO_UNICODE["car mechanic"] = ["U+3fc1"]
UNICODE_TO_BLISS["U+3fc1"] = ["car mechanic"]
BLISS_TO_UNICODE["carriage racing"] = ["U+3fc2"]
UNICODE_TO_BLISS["U+3fc2"] = ["carriage racing"]
BLISS_TO_UNICODE["put"] = ["U+3fc3"]
UNICODE_TO_BLISS["U+3fc3"] = ["put"]
BLISS_TO_UNICODE["locate"] = ["U+3fc3"]
UNICODE_TO_BLISS["U+3fc3"].append("locate")
BLISS_TO_UNICODE["place"].append("U+3fc3")
UNICODE_TO_BLISS["U+3fc3"].append("place")
BLISS_TO_UNICODE["put,locate,place"] = ["U+3fc3"]
UNICODE_TO_BLISS["U+3fc3"].append("put,locate,place")
BLISS_TO_UNICODE["mysterious"] = ["U+3fc4"]
UNICODE_TO_BLISS["U+3fc4"] = ["mysterious"]
BLISS_TO_UNICODE["unknown"].append("U+3fc4")
UNICODE_TO_BLISS["U+3fc4"].append("unknown")
BLISS_TO_UNICODE["mysterious,unknown"] = ["U+3fc4"]
UNICODE_TO_BLISS["U+3fc4"].append("mysterious,unknown")
BLISS_TO_UNICODE["excuse"] = ["U+3fc5"]
UNICODE_TO_BLISS["U+3fc5"] = ["excuse"]
BLISS_TO_UNICODE["to allow"] = ["U+3fc6"]
UNICODE_TO_BLISS["U+3fc6"] = ["to allow"]
BLISS_TO_UNICODE["cruise ship"] = ["U+3fc7"]
UNICODE_TO_BLISS["U+3fc7"] = ["cruise ship"]
BLISS_TO_UNICODE["to travel"] = ["U+3fc8"]
UNICODE_TO_BLISS["U+3fc8"] = ["to travel"]
BLISS_TO_UNICODE["fishburger"] = ["U+3fc9"]
UNICODE_TO_BLISS["U+3fc9"] = ["fishburger"]
BLISS_TO_UNICODE["each other"] = ["U+3fca"]
UNICODE_TO_BLISS["U+3fca"] = ["each other"]
BLISS_TO_UNICODE["one another"] = ["U+3fca"]
UNICODE_TO_BLISS["U+3fca"].append("one another")
BLISS_TO_UNICODE["each other,one another"] = ["U+3fca"]
UNICODE_TO_BLISS["U+3fca"].append("each other,one another")
BLISS_TO_UNICODE["9"].append("U+3569")
UNICODE_TO_BLISS["U+3569"].append("9")
BLISS_TO_UNICODE["Arabic numeral 9"] = ["U+3fcb"]
UNICODE_TO_BLISS["U+3fcb"] = ["Arabic numeral 9"]
BLISS_TO_UNICODE["Arabic numeral 9 small"] = ["U+3fcc"]
UNICODE_TO_BLISS["U+3fcc"] = ["Arabic numeral 9 small"]
BLISS_TO_UNICODE["swash"] = ["U+3fcd"]
UNICODE_TO_BLISS["U+3fcd"] = ["swash"]
BLISS_TO_UNICODE["walk"] = ["U+3fce"]
UNICODE_TO_BLISS["U+3fce"] = ["walk"]
BLISS_TO_UNICODE["fundamentalist"] = ["U+3fcf"]
UNICODE_TO_BLISS["U+3fcf"] = ["fundamentalist"]
BLISS_TO_UNICODE["fundamentalism"] = ["U+3fd0"]
UNICODE_TO_BLISS["U+3fd0"] = ["fundamentalism"]
BLISS_TO_UNICODE["ballooning"] = ["U+3fd1"]
UNICODE_TO_BLISS["U+3fd1"] = ["ballooning"]
BLISS_TO_UNICODE["stave"] = ["U+3fd2"]
UNICODE_TO_BLISS["U+3fd2"] = ["stave"]
BLISS_TO_UNICODE["archipelago"] = ["U+3fd3"]
UNICODE_TO_BLISS["U+3fd3"] = ["archipelago"]
BLISS_TO_UNICODE["see you again"] = ["U+3fd4"]
UNICODE_TO_BLISS["U+3fd4"] = ["see you again"]
BLISS_TO_UNICODE["revelry"] = ["U+3fd5"]
UNICODE_TO_BLISS["U+3fd5"] = ["revelry"]
BLISS_TO_UNICODE["clause"] = ["U+3ab8"]
UNICODE_TO_BLISS["U+3ab8"].append("clause")
BLISS_TO_UNICODE["phrase"] = ["U+3ab8"]
UNICODE_TO_BLISS["U+3ab8"].append("phrase")
BLISS_TO_UNICODE["sentence,clause,phrase"] = ["U+3ab8"]
UNICODE_TO_BLISS["U+3ab8"].append("sentence,clause,phrase")
BLISS_TO_UNICODE["make a coup"] = ["U+3693"]
UNICODE_TO_BLISS["U+3693"].append("make a coup")
BLISS_TO_UNICODE["hijack,make a coup"] = ["U+3693"]
UNICODE_TO_BLISS["U+3693"].append("hijack,make a coup")
BLISS_TO_UNICODE["vase"] = ["U+3fd6"]
UNICODE_TO_BLISS["U+3fd6"] = ["vase"]
BLISS_TO_UNICODE["urn"] = ["U+3fd6"]
UNICODE_TO_BLISS["U+3fd6"].append("urn")
BLISS_TO_UNICODE["trophy cup"] = ["U+3fd6"]
UNICODE_TO_BLISS["U+3fd6"].append("trophy cup")
BLISS_TO_UNICODE["vase,urn,trophy cup"] = ["U+3fd6"]
UNICODE_TO_BLISS["U+3fd6"].append("vase,urn,trophy cup")
BLISS_TO_UNICODE["counter purpose"] = ["U+3417"]
UNICODE_TO_BLISS["U+3417"].append("counter purpose")
BLISS_TO_UNICODE["opposition,counter purpose"] = ["U+3417"]
UNICODE_TO_BLISS["U+3417"].append("opposition,counter purpose")
BLISS_TO_UNICODE["less than"] = ["U+3fd7"]
UNICODE_TO_BLISS["U+3fd7"] = ["less than"]
BLISS_TO_UNICODE["xylophone"] = ["U+3fd8"]
UNICODE_TO_BLISS["U+3fd8"] = ["xylophone"]
BLISS_TO_UNICODE["vibraphone"] = ["U+3fd8"]
UNICODE_TO_BLISS["U+3fd8"].append("vibraphone")
BLISS_TO_UNICODE["xylophone,vibraphone"] = ["U+3fd8"]
UNICODE_TO_BLISS["U+3fd8"].append("xylophone,vibraphone")
BLISS_TO_UNICODE["music therapist"] = ["U+3fd9"]
UNICODE_TO_BLISS["U+3fd9"] = ["music therapist"]
BLISS_TO_UNICODE["pictograph of bars of a lattice"] = ["U+3fda"]
UNICODE_TO_BLISS["U+3fda"] = ["pictograph of bars of a lattice"]
BLISS_TO_UNICODE["psychology teacher"] = ["U+3fdb"]
UNICODE_TO_BLISS["U+3fdb"] = ["psychology teacher"]
BLISS_TO_UNICODE["horizontal"] = ["U+3fdc"]
UNICODE_TO_BLISS["U+3fdc"] = ["horizontal"]
BLISS_TO_UNICODE["pointer to horizontal arm of angle"] = ["U+3fdd"]
UNICODE_TO_BLISS["U+3fdd"] = ["pointer to horizontal arm of angle"]
BLISS_TO_UNICODE["brother in law"] = ["U+3fde"]
UNICODE_TO_BLISS["U+3fde"] = ["brother in law"]
BLISS_TO_UNICODE["brother-in-law"] = ["U+3fde"]
UNICODE_TO_BLISS["U+3fde"].append("brother-in-law")
BLISS_TO_UNICODE["sometime"] = ["U+3ed7"]
UNICODE_TO_BLISS["U+3ed7"].append("sometime")
BLISS_TO_UNICODE["anytime,sometime"] = ["U+3ed7"]
UNICODE_TO_BLISS["U+3ed7"].append("anytime,sometime")
BLISS_TO_UNICODE["roller skate"] = ["U+3fdf"]
UNICODE_TO_BLISS["U+3fdf"] = ["roller skate"]
BLISS_TO_UNICODE["overlay keyboard"] = ["U+3fe0"]
UNICODE_TO_BLISS["U+3fe0"] = ["overlay keyboard"]
BLISS_TO_UNICODE["membrane keyboard"] = ["U+3fe0"]
UNICODE_TO_BLISS["U+3fe0"].append("membrane keyboard")
BLISS_TO_UNICODE["overlay keyboard,membrane keyboard"] = ["U+3fe0"]
UNICODE_TO_BLISS["U+3fe0"].append("overlay keyboard,membrane keyboard")
BLISS_TO_UNICODE["hobbit"] = ["U+3fe1"]
UNICODE_TO_BLISS["U+3fe1"] = ["hobbit"]
BLISS_TO_UNICODE["universal"] = ["U+3fe2"]
UNICODE_TO_BLISS["U+3fe2"] = ["universal"]
BLISS_TO_UNICODE["world wide"] = ["U+3fe2"]
UNICODE_TO_BLISS["U+3fe2"].append("world wide")
BLISS_TO_UNICODE["universal,world-wide"] = ["U+3fe2"]
UNICODE_TO_BLISS["U+3fe2"].append("universal,world-wide")
BLISS_TO_UNICODE["ovum"] = ["U+3271"]
UNICODE_TO_BLISS["U+3271"].append("ovum")
BLISS_TO_UNICODE["egg,ovum"] = ["U+3271"]
UNICODE_TO_BLISS["U+3271"].append("egg,ovum")
BLISS_TO_UNICODE["life) SYMBOL SYNONYM"] = ["U+3fe4"]
UNICODE_TO_BLISS["U+3fe4"] = ["life) SYMBOL SYNONYM"]
BLISS_TO_UNICODE["boiled egg"] = ["U+3271"]
UNICODE_TO_BLISS["U+3271"].append("boiled egg")
BLISS_TO_UNICODE["to boil"] = ["U+3fe5"]
UNICODE_TO_BLISS["U+3fe5"] = ["to boil"]
BLISS_TO_UNICODE["touchpad"] = ["U+3fe6"]
UNICODE_TO_BLISS["U+3fe6"] = ["touchpad"]
BLISS_TO_UNICODE["trackpad"] = ["U+3fe6"]
UNICODE_TO_BLISS["U+3fe6"].append("trackpad")
BLISS_TO_UNICODE["touchpad,trackpad"] = ["U+3fe6"]
UNICODE_TO_BLISS["U+3fe6"].append("touchpad,trackpad")
BLISS_TO_UNICODE["soon"] = ["U+3fe7"]
UNICODE_TO_BLISS["U+3fe7"] = ["soon"]
BLISS_TO_UNICODE["hell"] = ["U+3fe8"]
UNICODE_TO_BLISS["U+3fe8"] = ["hell"]
BLISS_TO_UNICODE["moshav"] = ["U+3fe9"]
UNICODE_TO_BLISS["U+3fe9"] = ["moshav"]
BLISS_TO_UNICODE["guitar"] = ["U+3fea"]
UNICODE_TO_BLISS["U+3fea"] = ["guitar"]
BLISS_TO_UNICODE["string instrument"].append("U+3fea")
UNICODE_TO_BLISS["U+3fea"].append("string instrument")
BLISS_TO_UNICODE["guitar,string instrument"] = ["U+3fea"]
UNICODE_TO_BLISS["U+3fea"].append("guitar,string instrument")
BLISS_TO_UNICODE["have to"].append("U+38cb")
UNICODE_TO_BLISS["U+38cb"].append("have to")
BLISS_TO_UNICODE["be forced to"] = ["U+38cb"]
UNICODE_TO_BLISS["U+38cb"].append("be forced to")
BLISS_TO_UNICODE["must,have to,be forced to"] = ["U+38cb"]
UNICODE_TO_BLISS["U+38cb"].append("must,have to,be forced to")
BLISS_TO_UNICODE["hang gliding"] = ["U+3feb"]
UNICODE_TO_BLISS["U+3feb"] = ["hang gliding"]
BLISS_TO_UNICODE["motivated"] = ["U+3fec"]
UNICODE_TO_BLISS["U+3fec"] = ["motivated"]
BLISS_TO_UNICODE["magnetic field"] = ["U+3fed"]
UNICODE_TO_BLISS["U+3fed"] = ["magnetic field"]
BLISS_TO_UNICODE["hidden thing"] = ["U+3fef"]
UNICODE_TO_BLISS["U+3fef"] = ["hidden thing"]
BLISS_TO_UNICODE["bless"] = ["U+3ff0"]
UNICODE_TO_BLISS["U+3ff0"] = ["bless"]
BLISS_TO_UNICODE["electricity meter"] = ["U+3ff1"]
UNICODE_TO_BLISS["U+3ff1"] = ["electricity meter"]
BLISS_TO_UNICODE["bass guitar"] = ["U+3ff2"]
UNICODE_TO_BLISS["U+3ff2"] = ["bass guitar"]
BLISS_TO_UNICODE["CD cover"] = ["U+3ff3"]
UNICODE_TO_BLISS["U+3ff3"] = ["CD cover"]
BLISS_TO_UNICODE["CD"] = ["U+3ff4"]
UNICODE_TO_BLISS["U+3ff4"] = ["CD"]
BLISS_TO_UNICODE["container transport"].append("U+3730")
UNICODE_TO_BLISS["U+3730"].append("container transport")
BLISS_TO_UNICODE["trailer,container transport"] = ["U+3730"]
UNICODE_TO_BLISS["U+3730"].append("trailer,container transport")
BLISS_TO_UNICODE["Czech Republic"] = ["U+3ff5"]
UNICODE_TO_BLISS["U+3ff5"] = ["Czech Republic"]
BLISS_TO_UNICODE["beer"] = ["U+3ff6"]
UNICODE_TO_BLISS["U+3ff6"] = ["beer"]
BLISS_TO_UNICODE["Lapps"] = ["U+3ff7"]
UNICODE_TO_BLISS["U+3ff7"] = ["Lapps"]
BLISS_TO_UNICODE["Lapplander"] = ["U+3ff7"]
UNICODE_TO_BLISS["U+3ff7"].append("Lapplander")
BLISS_TO_UNICODE["Sami"] = ["U+3ff7"]
UNICODE_TO_BLISS["U+3ff7"].append("Sami")
BLISS_TO_UNICODE["Lapps,Lapplander"] = ["U+3ff7"]
UNICODE_TO_BLISS["U+3ff7"].append("Lapps,Lapplander")
BLISS_TO_UNICODE["ethnic group"] = ["U+3ff8"]
UNICODE_TO_BLISS["U+3ff8"] = ["ethnic group"]
BLISS_TO_UNICODE["unharness"] = ["U+3ff9"]
UNICODE_TO_BLISS["U+3ff9"] = ["unharness"]
BLISS_TO_UNICODE["happening"] = ["U+32a5"]
UNICODE_TO_BLISS["U+32a5"].append("happening")
BLISS_TO_UNICODE["occasion"] = ["U+32a5"]
UNICODE_TO_BLISS["U+32a5"].append("occasion")
BLISS_TO_UNICODE["event,happening,occasion"] = ["U+32a5"]
UNICODE_TO_BLISS["U+32a5"].append("event,happening,occasion")
BLISS_TO_UNICODE["surrounded"] = ["U+3ffb"]
UNICODE_TO_BLISS["U+3ffb"] = ["surrounded"]
BLISS_TO_UNICODE["encircled"] = ["U+3ffb"]
UNICODE_TO_BLISS["U+3ffb"].append("encircled")
BLISS_TO_UNICODE["surrounding"] = ["U+3ffb"]
UNICODE_TO_BLISS["U+3ffb"].append("surrounding")
BLISS_TO_UNICODE["surrounded,encircled,surrounding"] = ["U+3ffb"]
UNICODE_TO_BLISS["U+3ffb"].append("surrounded,encircled,surrounding")
BLISS_TO_UNICODE["testify"] = ["U+3ffc"]
UNICODE_TO_BLISS["U+3ffc"] = ["testify"]
BLISS_TO_UNICODE["publish"] = ["U+3ffd"]
UNICODE_TO_BLISS["U+3ffd"] = ["publish"]
BLISS_TO_UNICODE["publication"] = ["U+3ffe"]
UNICODE_TO_BLISS["U+3ffe"] = ["publication"]
BLISS_TO_UNICODE["7"].append("U+3567")
UNICODE_TO_BLISS["U+3567"].append("7")
BLISS_TO_UNICODE["Arabic numeral 7"] = ["U+3fff"]
UNICODE_TO_BLISS["U+3fff"] = ["Arabic numeral 7"]
BLISS_TO_UNICODE["gathering of scouts"] = ["U+4000"]
UNICODE_TO_BLISS["U+4000"] = ["gathering of scouts"]
BLISS_TO_UNICODE["jamboree"] = ["U+4000"]
UNICODE_TO_BLISS["U+4000"].append("jamboree")
BLISS_TO_UNICODE["gathering of scouts,jamboree"] = ["U+4000"]
UNICODE_TO_BLISS["U+4000"].append("gathering of scouts,jamboree")
BLISS_TO_UNICODE["scouting"] = ["U+4001"]
UNICODE_TO_BLISS["U+4001"] = ["scouting"]
BLISS_TO_UNICODE["gardener"] = ["U+4002"]
UNICODE_TO_BLISS["U+4002"] = ["gardener"]
BLISS_TO_UNICODE["report"] = ["U+3a82"]
UNICODE_TO_BLISS["U+3a82"].append("report")
BLISS_TO_UNICODE["tale"] = ["U+3a82"]
UNICODE_TO_BLISS["U+3a82"].append("tale")
BLISS_TO_UNICODE["story,report,tale"] = ["U+3a82"]
UNICODE_TO_BLISS["U+3a82"].append("story,report,tale")
BLISS_TO_UNICODE["pub"] = ["U+3c48"]
UNICODE_TO_BLISS["U+3c48"].append("pub")
BLISS_TO_UNICODE["bar,pub"] = ["U+3c48"]
UNICODE_TO_BLISS["U+3c48"].append("bar,pub")
BLISS_TO_UNICODE["intellect"] = ["U+32ca"]
UNICODE_TO_BLISS["U+32ca"].append("intellect")
BLISS_TO_UNICODE["reason"] = ["U+32ca"]
UNICODE_TO_BLISS["U+32ca"].append("reason")
BLISS_TO_UNICODE["mind,intellect,reason"] = ["U+32ca"]
UNICODE_TO_BLISS["U+32ca"].append("mind,intellect,reason")
BLISS_TO_UNICODE["symbol suggests an outline of a skull"] = ["U+4003"]
UNICODE_TO_BLISS["U+4003"] = ["symbol suggests an outline of a skull"]
BLISS_TO_UNICODE["think"] = ["U+4004"]
UNICODE_TO_BLISS["U+4004"] = ["think"]
BLISS_TO_UNICODE["reason"].append("U+4004")
UNICODE_TO_BLISS["U+4004"].append("reason")
BLISS_TO_UNICODE["think,reason"] = ["U+4004"]
UNICODE_TO_BLISS["U+4004"].append("think,reason")
BLISS_TO_UNICODE["reason"].append("U+3af6")
UNICODE_TO_BLISS["U+3af6"].append("reason")
BLISS_TO_UNICODE["explanation,reason"] = ["U+3af6"]
UNICODE_TO_BLISS["U+3af6"].append("explanation,reason")
BLISS_TO_UNICODE["children's room"] = ["U+4005"]
UNICODE_TO_BLISS["U+4005"] = ["children's room"]
BLISS_TO_UNICODE["cheering"] = ["U+4006"]
UNICODE_TO_BLISS["U+4006"] = ["cheering"]
BLISS_TO_UNICODE["fuel gauge"] = ["U+4007"]
UNICODE_TO_BLISS["U+4007"] = ["fuel gauge"]
BLISS_TO_UNICODE["gasoline"] = ["U+4008"]
UNICODE_TO_BLISS["U+4008"] = ["gasoline"]
BLISS_TO_UNICODE["blush"] = ["U+4009"]
UNICODE_TO_BLISS["U+4009"] = ["blush"]
BLISS_TO_UNICODE["synchronized diving"] = ["U+400a"]
UNICODE_TO_BLISS["U+400a"] = ["synchronized diving"]
BLISS_TO_UNICODE["synchro diving"] = ["U+400a"]
UNICODE_TO_BLISS["U+400a"].append("synchro diving")
BLISS_TO_UNICODE["synchronized diving,synchro diving"] = ["U+400a"]
UNICODE_TO_BLISS["U+400a"].append("synchronized diving,synchro diving")
BLISS_TO_UNICODE["sufganiya"] = ["U+400b"]
UNICODE_TO_BLISS["U+400b"] = ["sufganiya"]
BLISS_TO_UNICODE["water sports"] = ["U+400c"]
UNICODE_TO_BLISS["U+400c"] = ["water sports"]
BLISS_TO_UNICODE["knocking"] = ["U+400d"]
UNICODE_TO_BLISS["U+400d"] = ["knocking"]
BLISS_TO_UNICODE["dust"].append("U+33d5")
UNICODE_TO_BLISS["U+33d5"].append("dust")
BLISS_TO_UNICODE["powder,dust"] = ["U+33d5"]
UNICODE_TO_BLISS["U+33d5"].append("powder,dust")
BLISS_TO_UNICODE["three powderlike dots"] = ["U+400e"]
UNICODE_TO_BLISS["U+400e"] = ["three powderlike dots"]
BLISS_TO_UNICODE["miss"] = ["U+400f"]
UNICODE_TO_BLISS["U+400f"] = ["miss"]
BLISS_TO_UNICODE["lose"] = ["U+400f"]
UNICODE_TO_BLISS["U+400f"].append("lose")
BLISS_TO_UNICODE["miss,lose"] = ["U+400f"]
UNICODE_TO_BLISS["U+400f"].append("miss,lose")
BLISS_TO_UNICODE["pictograph of horse's head and neck"] = ["U+4010"]
UNICODE_TO_BLISS["U+4010"] = ["pictograph of horse's head and neck"]
BLISS_TO_UNICODE["bloom"] = ["U+328f"]
UNICODE_TO_BLISS["U+328f"].append("bloom")
BLISS_TO_UNICODE["blossom"] = ["U+328f"]
UNICODE_TO_BLISS["U+328f"].append("blossom")
BLISS_TO_UNICODE["flower,bloom,blossom"] = ["U+328f"]
UNICODE_TO_BLISS["U+328f"].append("flower,bloom,blossom")
BLISS_TO_UNICODE["obedience"] = ["U+4011"]
UNICODE_TO_BLISS["U+4011"] = ["obedience"]
BLISS_TO_UNICODE["mind sports"] = ["U+4012"]
UNICODE_TO_BLISS["U+4012"] = ["mind sports"]
BLISS_TO_UNICODE["kindly"] = ["U+32d9"]
UNICODE_TO_BLISS["U+32d9"].append("kindly")
BLISS_TO_UNICODE["kind,kindly"] = ["U+32d9"]
UNICODE_TO_BLISS["U+32d9"].append("kind,kindly")
BLISS_TO_UNICODE["diamond"] = ["U+4013"]
UNICODE_TO_BLISS["U+4013"] = ["diamond"]
BLISS_TO_UNICODE["rhombus"] = ["U+4013"]
UNICODE_TO_BLISS["U+4013"].append("rhombus")
BLISS_TO_UNICODE["rhomb"] = ["U+4013"]
UNICODE_TO_BLISS["U+4013"].append("rhomb")
BLISS_TO_UNICODE["expect"] = ["U+4014"]
UNICODE_TO_BLISS["U+4014"] = ["expect"]
BLISS_TO_UNICODE["anticipate"] = ["U+4014"]
UNICODE_TO_BLISS["U+4014"].append("anticipate")
BLISS_TO_UNICODE["expect,anticipate"] = ["U+4014"]
UNICODE_TO_BLISS["U+4014"].append("expect,anticipate")
BLISS_TO_UNICODE["gray"] = ["U+4015"]
UNICODE_TO_BLISS["U+4015"] = ["gray"]
BLISS_TO_UNICODE["grey"] = ["U+4015"]
UNICODE_TO_BLISS["U+4015"].append("grey")
BLISS_TO_UNICODE["gray,grey"] = ["U+4015"]
UNICODE_TO_BLISS["U+4015"].append("gray,grey")
BLISS_TO_UNICODE["toy animal"] = ["U+4016"]
UNICODE_TO_BLISS["U+4016"] = ["toy animal"]
BLISS_TO_UNICODE["stuffed animal"] = ["U+4016"]
UNICODE_TO_BLISS["U+4016"].append("stuffed animal")
BLISS_TO_UNICODE["toy animal,stuffed animal"] = ["U+4016"]
UNICODE_TO_BLISS["U+4016"].append("toy animal,stuffed animal")
BLISS_TO_UNICODE["tonality"] = ["U+33f3"]
UNICODE_TO_BLISS["U+33f3"].append("tonality")
BLISS_TO_UNICODE["key,tonality"] = ["U+33f3"]
UNICODE_TO_BLISS["U+33f3"].append("key,tonality")
BLISS_TO_UNICODE["inner organ"] = ["U+366d"]
UNICODE_TO_BLISS["U+366d"].append("inner organ")
BLISS_TO_UNICODE["inner body part"] = ["U+366d"]
UNICODE_TO_BLISS["U+366d"].append("inner body part")
BLISS_TO_UNICODE["organ,inner organ,inner body part"] = ["U+366d"]
UNICODE_TO_BLISS["U+366d"].append("organ,inner organ,inner body part")
BLISS_TO_UNICODE["go kart"] = ["U+4017"]
UNICODE_TO_BLISS["U+4017"] = ["go kart"]
BLISS_TO_UNICODE["kart"] = ["U+4017"]
UNICODE_TO_BLISS["U+4017"].append("kart")
BLISS_TO_UNICODE["go-kart,kart"] = ["U+4017"]
UNICODE_TO_BLISS["U+4017"].append("go-kart,kart")
BLISS_TO_UNICODE["playroom"] = ["U+4018"]
UNICODE_TO_BLISS["U+4018"] = ["playroom"]
BLISS_TO_UNICODE["family room"] = ["U+4018"]
UNICODE_TO_BLISS["U+4018"].append("family room")
BLISS_TO_UNICODE["recreation room"] = ["U+4018"]
UNICODE_TO_BLISS["U+4018"].append("recreation room")
BLISS_TO_UNICODE["playroom,family room,recreation room"] = ["U+4018"]
UNICODE_TO_BLISS["U+4018"].append("playroom,family room,recreation room")
BLISS_TO_UNICODE["to play"] = ["U+4019"]
UNICODE_TO_BLISS["U+4019"] = ["to play"]
BLISS_TO_UNICODE["juicy"] = ["U+401a"]
UNICODE_TO_BLISS["U+401a"] = ["juicy"]
BLISS_TO_UNICODE["denseness"] = ["U+3a37"]
UNICODE_TO_BLISS["U+3a37"].append("denseness")
BLISS_TO_UNICODE["concentration"] = ["U+3a37"]
UNICODE_TO_BLISS["U+3a37"].append("concentration")
BLISS_TO_UNICODE["density,denseness,concentration"] = ["U+3a37"]
UNICODE_TO_BLISS["U+3a37"].append("density,denseness,concentration")
BLISS_TO_UNICODE["closeness"] = ["U+401b"]
UNICODE_TO_BLISS["U+401b"] = ["closeness"]
BLISS_TO_UNICODE["department store"] = ["U+401c"]
UNICODE_TO_BLISS["U+401c"] = ["department store"]
BLISS_TO_UNICODE["koala"] = ["U+401d"]
UNICODE_TO_BLISS["U+401d"] = ["koala"]
BLISS_TO_UNICODE["cave"] = ["U+401e"]
UNICODE_TO_BLISS["U+401e"] = ["cave"]
BLISS_TO_UNICODE["labour"] = ["U+401f"]
UNICODE_TO_BLISS["U+401f"] = ["labour"]
BLISS_TO_UNICODE["pyjama"] = ["U+4020"]
UNICODE_TO_BLISS["U+4020"] = ["pyjama"]
BLISS_TO_UNICODE["nightgown"] = ["U+4020"]
UNICODE_TO_BLISS["U+4020"].append("nightgown")
BLISS_TO_UNICODE["nightie"] = ["U+4020"]
UNICODE_TO_BLISS["U+4020"].append("nightie")
BLISS_TO_UNICODE["pajama"] = ["U+4020"]
UNICODE_TO_BLISS["U+4020"].append("pajama")
BLISS_TO_UNICODE["handcycle"] = ["U+4021"]
UNICODE_TO_BLISS["U+4021"] = ["handcycle"]
BLISS_TO_UNICODE["snuff"] = ["U+4022"]
UNICODE_TO_BLISS["U+4022"] = ["snuff"]
BLISS_TO_UNICODE["kat"] = ["U+4022"]
UNICODE_TO_BLISS["U+4022"].append("kat")
BLISS_TO_UNICODE["coca"] = ["U+4022"]
UNICODE_TO_BLISS["U+4022"].append("coca")
BLISS_TO_UNICODE["snuff,kat,coca"] = ["U+4022"]
UNICODE_TO_BLISS["U+4022"].append("snuff,kat,coca")
BLISS_TO_UNICODE["archery"] = ["U+4023"]
UNICODE_TO_BLISS["U+4023"] = ["archery"]
BLISS_TO_UNICODE["premature birth"] = ["U+4024"]
UNICODE_TO_BLISS["U+4024"] = ["premature birth"]
BLISS_TO_UNICODE["elbow splint"] = ["U+4025"]
UNICODE_TO_BLISS["U+4025"] = ["elbow splint"]
BLISS_TO_UNICODE["bones with joint"] = ["U+4026"]
UNICODE_TO_BLISS["U+4026"] = ["bones with joint"]
BLISS_TO_UNICODE["clean"] = ["U+4027"]
UNICODE_TO_BLISS["U+4027"] = ["clean"]
BLISS_TO_UNICODE["drying cupboard"] = ["U+4028"]
UNICODE_TO_BLISS["U+4028"] = ["drying cupboard"]
BLISS_TO_UNICODE["airing cupboard"] = ["U+4028"]
UNICODE_TO_BLISS["U+4028"].append("airing cupboard")
BLISS_TO_UNICODE["drying cupboard,airing cupboard"] = ["U+4028"]
UNICODE_TO_BLISS["U+4028"].append("drying cupboard,airing cupboard")
BLISS_TO_UNICODE["blend"] = ["U+3258"]
UNICODE_TO_BLISS["U+3258"].append("blend")
BLISS_TO_UNICODE["mix,blend"] = ["U+3258"]
UNICODE_TO_BLISS["U+3258"].append("mix,blend")
BLISS_TO_UNICODE["weather satellite"] = ["U+4029"]
UNICODE_TO_BLISS["U+4029"] = ["weather satellite"]
BLISS_TO_UNICODE["spy satellite"] = ["U+4029"]
UNICODE_TO_BLISS["U+4029"].append("spy satellite")
BLISS_TO_UNICODE["weather satellite,spy satellite"] = ["U+4029"]
UNICODE_TO_BLISS["U+4029"].append("weather satellite,spy satellite")
BLISS_TO_UNICODE["humid"] = ["U+402a"]
UNICODE_TO_BLISS["U+402a"] = ["humid"]
BLISS_TO_UNICODE["damp"] = ["U+402a"]
UNICODE_TO_BLISS["U+402a"].append("damp")
BLISS_TO_UNICODE["moist"] = ["U+402a"]
UNICODE_TO_BLISS["U+402a"].append("moist")
BLISS_TO_UNICODE["humid,damp,moist"] = ["U+402a"]
UNICODE_TO_BLISS["U+402a"].append("humid,damp,moist")
BLISS_TO_UNICODE["northern"] = ["U+402b"]
UNICODE_TO_BLISS["U+402b"] = ["northern"]
BLISS_TO_UNICODE["justice"] = ["U+402c"]
UNICODE_TO_BLISS["U+402c"] = ["justice"]
BLISS_TO_UNICODE["French"] = ["U+402d"]
UNICODE_TO_BLISS["U+402d"] = ["French"]
BLISS_TO_UNICODE["France"] = ["U+402e"]
UNICODE_TO_BLISS["U+402e"] = ["France"]
BLISS_TO_UNICODE["lunar eclipse"] = ["U+402f"]
UNICODE_TO_BLISS["U+402f"] = ["lunar eclipse"]
BLISS_TO_UNICODE["circular shape"] = ["U+4030"]
UNICODE_TO_BLISS["U+4030"] = ["circular shape"]
BLISS_TO_UNICODE["circle"].append("U+3257")
UNICODE_TO_BLISS["U+3257"].append("circle")
BLISS_TO_UNICODE["circulate"] = ["U+3257"]
UNICODE_TO_BLISS["U+3257"].append("circulate")
BLISS_TO_UNICODE["wind up"] = ["U+3257"]
UNICODE_TO_BLISS["U+3257"].append("wind up")
BLISS_TO_UNICODE["orbit"].append("U+3257")
UNICODE_TO_BLISS["U+3257"].append("orbit")
BLISS_TO_UNICODE["rotate,circle,circulate,wind up,orbit"] = ["U+3257"]
UNICODE_TO_BLISS["U+3257"].append("rotate,circle,circulate,wind up,orbit")
BLISS_TO_UNICODE["porcupine"] = ["U+4031"]
UNICODE_TO_BLISS["U+4031"] = ["porcupine"]
BLISS_TO_UNICODE["religious event"] = ["U+4032"]
UNICODE_TO_BLISS["U+4032"] = ["religious event"]
BLISS_TO_UNICODE["small intestine"] = ["U+4033"]
UNICODE_TO_BLISS["U+4033"] = ["small intestine"]
BLISS_TO_UNICODE["basement"] = ["U+4034"]
UNICODE_TO_BLISS["U+4034"] = ["basement"]
BLISS_TO_UNICODE["cellar"] = ["U+4034"]
UNICODE_TO_BLISS["U+4034"].append("cellar")
BLISS_TO_UNICODE["basement,cellar"] = ["U+4034"]
UNICODE_TO_BLISS["U+4034"].append("basement,cellar")
BLISS_TO_UNICODE["place to feed"] = ["U+4035"]
UNICODE_TO_BLISS["U+4035"] = ["place to feed"]
BLISS_TO_UNICODE["feeding place"] = ["U+4035"]
UNICODE_TO_BLISS["U+4035"].append("feeding place")
BLISS_TO_UNICODE["feeding ground"] = ["U+4035"]
UNICODE_TO_BLISS["U+4035"].append("feeding ground")
BLISS_TO_UNICODE["place to feed,feeding place,feeding ground"] = ["U+4035"]
UNICODE_TO_BLISS["U+4035"].append("place to feed,feeding place,feeding ground")
BLISS_TO_UNICODE["during"] = ["U+4036"]
UNICODE_TO_BLISS["U+4036"] = ["during"]
BLISS_TO_UNICODE["while"] = ["U+4036"]
UNICODE_TO_BLISS["U+4036"].append("while")
BLISS_TO_UNICODE["during,while"] = ["U+4036"]
UNICODE_TO_BLISS["U+4036"].append("during,while")
BLISS_TO_UNICODE["no one"] = ["U+4037"]
UNICODE_TO_BLISS["U+4037"] = ["no one"]
BLISS_TO_UNICODE["nobody"] = ["U+4037"]
UNICODE_TO_BLISS["U+4037"].append("nobody")
BLISS_TO_UNICODE["no one,nobody"] = ["U+4037"]
UNICODE_TO_BLISS["U+4037"].append("no one,nobody")
BLISS_TO_UNICODE["house with chimney"] = ["U+4038"]
UNICODE_TO_BLISS["U+4038"] = ["house with chimney"]
BLISS_TO_UNICODE["electric wheelchair"] = ["U+4039"]
UNICODE_TO_BLISS["U+4039"] = ["electric wheelchair"]
BLISS_TO_UNICODE["children's song"] = ["U+403a"]
UNICODE_TO_BLISS["U+403a"] = ["children's song"]
BLISS_TO_UNICODE["nursery rhyme"] = ["U+403a"]
UNICODE_TO_BLISS["U+403a"].append("nursery rhyme")
BLISS_TO_UNICODE["children's song,nursery rhyme"] = ["U+403a"]
UNICODE_TO_BLISS["U+403a"].append("children's song,nursery rhyme")
BLISS_TO_UNICODE["cramp"] = ["U+403b"]
UNICODE_TO_BLISS["U+403b"] = ["cramp"]
BLISS_TO_UNICODE["spasm"] = ["U+403b"]
UNICODE_TO_BLISS["U+403b"].append("spasm")
BLISS_TO_UNICODE["cramp,spasm"] = ["U+403b"]
UNICODE_TO_BLISS["U+403b"].append("cramp,spasm")
BLISS_TO_UNICODE["champagne"] = ["U+403c"]
UNICODE_TO_BLISS["U+403c"] = ["champagne"]
BLISS_TO_UNICODE["culture"] = ["U+403d"]
UNICODE_TO_BLISS["U+403d"] = ["culture"]
BLISS_TO_UNICODE["Kislev"] = ["U+403e"]
UNICODE_TO_BLISS["U+403e"] = ["Kislev"]
BLISS_TO_UNICODE["almost"] = ["U+3508"]
UNICODE_TO_BLISS["U+3508"].append("almost")
BLISS_TO_UNICODE["close"].append("U+3508")
UNICODE_TO_BLISS["U+3508"].append("close")
BLISS_TO_UNICODE["nearly"] = ["U+3508"]
UNICODE_TO_BLISS["U+3508"].append("nearly")
BLISS_TO_UNICODE["near,almost,close,nearly"] = ["U+3508"]
UNICODE_TO_BLISS["U+3508"].append("near,almost,close,nearly")
BLISS_TO_UNICODE["nearness"] = ["U+403f"]
UNICODE_TO_BLISS["U+403f"] = ["nearness"]
BLISS_TO_UNICODE["high water"] = ["U+4040"]
UNICODE_TO_BLISS["U+4040"] = ["high water"]
BLISS_TO_UNICODE["gravity"] = ["U+4041"]
UNICODE_TO_BLISS["U+4041"] = ["gravity"]
BLISS_TO_UNICODE["gravitation"] = ["U+4041"]
UNICODE_TO_BLISS["U+4041"].append("gravitation")
BLISS_TO_UNICODE["gravity,gravitation"] = ["U+4041"]
UNICODE_TO_BLISS["U+4041"].append("gravity,gravitation")
BLISS_TO_UNICODE["probable"] = ["U+4042"]
UNICODE_TO_BLISS["U+4042"] = ["probable"]
BLISS_TO_UNICODE["likely"] = ["U+4042"]
UNICODE_TO_BLISS["U+4042"].append("likely")
BLISS_TO_UNICODE["probably"] = ["U+4042"]
UNICODE_TO_BLISS["U+4042"].append("probably")
BLISS_TO_UNICODE["probable,likely,probably"] = ["U+4042"]
UNICODE_TO_BLISS["U+4042"].append("probable,likely,probably")
BLISS_TO_UNICODE["to doubt"] = ["U+4043"]
UNICODE_TO_BLISS["U+4043"] = ["to doubt"]
BLISS_TO_UNICODE["fishball"] = ["U+4044"]
UNICODE_TO_BLISS["U+4044"] = ["fishball"]
BLISS_TO_UNICODE["wok"] = ["U+4045"]
UNICODE_TO_BLISS["U+4045"] = ["wok"]
BLISS_TO_UNICODE["wok pan"] = ["U+4045"]
UNICODE_TO_BLISS["U+4045"].append("wok pan")
BLISS_TO_UNICODE["wok,wok pan"] = ["U+4045"]
UNICODE_TO_BLISS["U+4045"].append("wok,wok pan")
BLISS_TO_UNICODE["cartographer"] = ["U+4046"]
UNICODE_TO_BLISS["U+4046"] = ["cartographer"]
BLISS_TO_UNICODE["synthesizer"] = ["U+4047"]
UNICODE_TO_BLISS["U+4047"] = ["synthesizer"]
BLISS_TO_UNICODE["synthesiser"] = ["U+4047"]
UNICODE_TO_BLISS["U+4047"].append("synthesiser")
BLISS_TO_UNICODE["keyboard"].append("U+4047")
UNICODE_TO_BLISS["U+4047"].append("keyboard")
BLISS_TO_UNICODE["synthesizer,synthesiser,keyboard"] = ["U+4047"]
UNICODE_TO_BLISS["U+4047"].append("synthesizer,synthesiser,keyboard")
BLISS_TO_UNICODE["piano"] = ["U+4048"]
UNICODE_TO_BLISS["U+4048"] = ["piano"]
BLISS_TO_UNICODE["vaporize"] = ["U+3a8e"]
UNICODE_TO_BLISS["U+3a8e"].append("vaporize")
BLISS_TO_UNICODE["spray,vaporize"] = ["U+3a8e"]
UNICODE_TO_BLISS["U+3a8e"].append("spray,vaporize")
BLISS_TO_UNICODE["readying"] = ["U+35b7"]
UNICODE_TO_BLISS["U+35b7"].append("readying")
BLISS_TO_UNICODE["readiness"] = ["U+35b7"]
UNICODE_TO_BLISS["U+35b7"].append("readiness")
BLISS_TO_UNICODE["preparedness"] = ["U+35b7"]
UNICODE_TO_BLISS["U+35b7"].append("preparedness")
BLISS_TO_UNICODE["preparation,readying,readiness,preparedness"] = ["U+35b7"]
UNICODE_TO_BLISS["U+35b7"].append("preparation,readying,readiness,preparedness")
BLISS_TO_UNICODE["storage jar"] = ["U+4049"]
UNICODE_TO_BLISS["U+4049"] = ["storage jar"]
BLISS_TO_UNICODE["preserving jar"] = ["U+4049"]
UNICODE_TO_BLISS["U+4049"].append("preserving jar")
BLISS_TO_UNICODE["storage jar,preserving jar"] = ["U+4049"]
UNICODE_TO_BLISS["U+4049"].append("storage jar,preserving jar")
BLISS_TO_UNICODE["main course"] = ["U+404b"]
UNICODE_TO_BLISS["U+404b"] = ["main course"]
BLISS_TO_UNICODE["middle"] = ["U+404c"]
UNICODE_TO_BLISS["U+404c"] = ["middle"]
BLISS_TO_UNICODE["both"] = ["U+404d"]
UNICODE_TO_BLISS["U+404d"] = ["both"]
BLISS_TO_UNICODE["barbershop"] = ["U+404e"]
UNICODE_TO_BLISS["U+404e"] = ["barbershop"]
BLISS_TO_UNICODE["beauty shop"] = ["U+404e"]
UNICODE_TO_BLISS["U+404e"].append("beauty shop")
BLISS_TO_UNICODE["barbershop,beauty shop"] = ["U+404e"]
UNICODE_TO_BLISS["U+404e"].append("barbershop,beauty shop")
BLISS_TO_UNICODE["eggplant"] = ["U+404f"]
UNICODE_TO_BLISS["U+404f"] = ["eggplant"]
BLISS_TO_UNICODE["guard"] = ["U+3779"]
UNICODE_TO_BLISS["U+3779"].append("guard")
BLISS_TO_UNICODE["protector,guard"] = ["U+3779"]
UNICODE_TO_BLISS["U+3779"].append("protector,guard")
BLISS_TO_UNICODE["mausoleum"] = ["U+4050"]
UNICODE_TO_BLISS["U+4050"] = ["mausoleum"]
BLISS_TO_UNICODE["battery"] = ["U+4051"]
UNICODE_TO_BLISS["U+4051"] = ["battery"]
BLISS_TO_UNICODE["badminton"] = ["U+4052"]
UNICODE_TO_BLISS["U+4052"] = ["badminton"]
BLISS_TO_UNICODE["nature craft"] = ["U+4053"]
UNICODE_TO_BLISS["U+4053"] = ["nature craft"]
BLISS_TO_UNICODE["solar eclipse"] = ["U+4054"]
UNICODE_TO_BLISS["U+4054"] = ["solar eclipse"]
BLISS_TO_UNICODE["wet"] = ["U+4055"]
UNICODE_TO_BLISS["U+4055"] = ["wet"]
BLISS_TO_UNICODE["damp"].append("U+4055")
UNICODE_TO_BLISS["U+4055"].append("damp")
BLISS_TO_UNICODE["moist"].append("U+4055")
UNICODE_TO_BLISS["U+4055"].append("moist")
BLISS_TO_UNICODE["watery"] = ["U+4055"]
UNICODE_TO_BLISS["U+4055"].append("watery")
BLISS_TO_UNICODE["wet,damp,moist,watery"] = ["U+4055"]
UNICODE_TO_BLISS["U+4055"].append("wet,damp,moist,watery")
BLISS_TO_UNICODE["add"] = ["U+4056"]
UNICODE_TO_BLISS["U+4056"] = ["add"]
BLISS_TO_UNICODE["gain"] = ["U+4056"]
UNICODE_TO_BLISS["U+4056"].append("gain")
BLISS_TO_UNICODE["add,gain"] = ["U+4056"]
UNICODE_TO_BLISS["U+4056"].append("add,gain")
BLISS_TO_UNICODE["chipmunk"] = ["U+4057"]
UNICODE_TO_BLISS["U+4057"] = ["chipmunk"]
BLISS_TO_UNICODE["baby bottle"] = ["U+4058"]
UNICODE_TO_BLISS["U+4058"] = ["baby bottle"]
BLISS_TO_UNICODE["feeding bottle"] = ["U+4058"]
UNICODE_TO_BLISS["U+4058"].append("feeding bottle")
BLISS_TO_UNICODE["baby bottle,feeding bottle"] = ["U+4058"]
UNICODE_TO_BLISS["U+4058"].append("baby bottle,feeding bottle")
BLISS_TO_UNICODE["cube"].append("U+33b2")
UNICODE_TO_BLISS["U+33b2"].append("cube")
BLISS_TO_UNICODE["box,cube"] = ["U+33b2"]
UNICODE_TO_BLISS["U+33b2"].append("box,cube")
BLISS_TO_UNICODE["liver"] = ["U+4059"]
UNICODE_TO_BLISS["U+4059"] = ["liver"]
BLISS_TO_UNICODE["pram straps"] = ["U+405a"]
UNICODE_TO_BLISS["U+405a"] = ["pram straps"]
BLISS_TO_UNICODE["safety harness"] = ["U+405a"]
UNICODE_TO_BLISS["U+405a"].append("safety harness")
BLISS_TO_UNICODE["pram straps,safety harness"] = ["U+405a"]
UNICODE_TO_BLISS["U+405a"].append("pram straps,safety harness")
BLISS_TO_UNICODE["hawser"] = ["U+3640"]
UNICODE_TO_BLISS["U+3640"].append("hawser")
BLISS_TO_UNICODE["rope,hawser"] = ["U+3640"]
UNICODE_TO_BLISS["U+3640"].append("rope,hawser")
BLISS_TO_UNICODE["vaginal discharge"] = ["U+405b"]
UNICODE_TO_BLISS["U+405b"] = ["vaginal discharge"]
BLISS_TO_UNICODE["Spanish"] = ["U+405c"]
UNICODE_TO_BLISS["U+405c"] = ["Spanish"]
BLISS_TO_UNICODE["Castilian"] = ["U+405c"]
UNICODE_TO_BLISS["U+405c"].append("Castilian")
BLISS_TO_UNICODE["Spanish,Castilian"] = ["U+405c"]
UNICODE_TO_BLISS["U+405c"].append("Spanish,Castilian")
BLISS_TO_UNICODE["direct"] = ["U+32e9"]
UNICODE_TO_BLISS["U+32e9"].append("direct")
BLISS_TO_UNICODE["guide"] = ["U+32e9"]
UNICODE_TO_BLISS["U+32e9"].append("guide")
BLISS_TO_UNICODE["lead,direct,guide"] = ["U+32e9"]
UNICODE_TO_BLISS["U+32e9"].append("lead,direct,guide")
BLISS_TO_UNICODE["director"] = ["U+37b9"]
UNICODE_TO_BLISS["U+37b9"].append("director")
BLISS_TO_UNICODE["guide"].append("U+37b9")
UNICODE_TO_BLISS["U+37b9"].append("guide")
BLISS_TO_UNICODE["leader,director,guide"] = ["U+37b9"]
UNICODE_TO_BLISS["U+37b9"].append("leader,director,guide")
BLISS_TO_UNICODE["prepared"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"].append("prepared")
BLISS_TO_UNICODE["ready,prepared"] = ["U+35f8"]
UNICODE_TO_BLISS["U+35f8"].append("ready,prepared")
BLISS_TO_UNICODE["to prepare"] = ["U+405d"]
UNICODE_TO_BLISS["U+405d"] = ["to prepare"]
BLISS_TO_UNICODE["hair drier"] = ["U+405e"]
UNICODE_TO_BLISS["U+405e"] = ["hair drier"]
BLISS_TO_UNICODE["blow dryer"] = ["U+405e"]
UNICODE_TO_BLISS["U+405e"].append("blow dryer")
BLISS_TO_UNICODE["hair drier,blow dryer"] = ["U+405e"]
UNICODE_TO_BLISS["U+405e"].append("hair drier,blow dryer")
BLISS_TO_UNICODE["communication therapist"] = ["U+405f"]
UNICODE_TO_BLISS["U+405f"] = ["communication therapist"]
BLISS_TO_UNICODE["temporary"] = ["U+4060"]
UNICODE_TO_BLISS["U+4060"] = ["temporary"]
BLISS_TO_UNICODE["lie down"] = ["U+4061"]
UNICODE_TO_BLISS["U+4061"] = ["lie down"]
BLISS_TO_UNICODE["lie"].append("U+4061")
UNICODE_TO_BLISS["U+4061"].append("lie")
BLISS_TO_UNICODE["lie down,lie"] = ["U+4061"]
UNICODE_TO_BLISS["U+4061"].append("lie down,lie")
BLISS_TO_UNICODE["pasta salad"] = ["U+4062"]
UNICODE_TO_BLISS["U+4062"] = ["pasta salad"]
BLISS_TO_UNICODE["auditor"] = ["U+4063"]
UNICODE_TO_BLISS["U+4063"] = ["auditor"]
BLISS_TO_UNICODE["accountant"] = ["U+4063"]
UNICODE_TO_BLISS["U+4063"].append("accountant")
BLISS_TO_UNICODE["auditor,accountant"] = ["U+4063"]
UNICODE_TO_BLISS["U+4063"].append("auditor,accountant")
BLISS_TO_UNICODE["wheelchair straps"] = ["U+4064"]
UNICODE_TO_BLISS["U+4064"] = ["wheelchair straps"]
BLISS_TO_UNICODE["hijack"].append("U+3692")
UNICODE_TO_BLISS["U+3692"].append("hijack")
BLISS_TO_UNICODE["takeover"].append("U+3692")
UNICODE_TO_BLISS["U+3692"].append("takeover")
BLISS_TO_UNICODE["coup,hijack,takeover"] = ["U+3692"]
UNICODE_TO_BLISS["U+3692"].append("coup,hijack,takeover")
BLISS_TO_UNICODE["empowered"] = ["U+4065"]
UNICODE_TO_BLISS["U+4065"] = ["empowered"]
BLISS_TO_UNICODE["fiancee"] = ["U+4066"]
UNICODE_TO_BLISS["U+4066"] = ["fiancee"]
BLISS_TO_UNICODE["bride to be"] = ["U+4066"]
UNICODE_TO_BLISS["U+4066"].append("bride to be")
BLISS_TO_UNICODE["fiancee,bride-to-be"] = ["U+4066"]
UNICODE_TO_BLISS["U+4066"].append("fiancee,bride-to-be")
BLISS_TO_UNICODE["cemetery"] = ["U+4067"]
UNICODE_TO_BLISS["U+4067"] = ["cemetery"]
BLISS_TO_UNICODE["lip"] = ["U+4068"]
UNICODE_TO_BLISS["U+4068"] = ["lip"]
BLISS_TO_UNICODE["evaluate"] = ["U+4069"]
UNICODE_TO_BLISS["U+4069"] = ["evaluate"]
BLISS_TO_UNICODE["to enjoy"] = ["U+406b"]
UNICODE_TO_BLISS["U+406b"] = ["to enjoy"]
BLISS_TO_UNICODE["optician"] = ["U+406c"]
UNICODE_TO_BLISS["U+406c"] = ["optician"]
BLISS_TO_UNICODE["eel"] = ["U+406d"]
UNICODE_TO_BLISS["U+406d"] = ["eel"]
BLISS_TO_UNICODE["housekeeper"] = ["U+406e"]
UNICODE_TO_BLISS["U+406e"] = ["housekeeper"]
BLISS_TO_UNICODE["kazoo"] = ["U+406f"]
UNICODE_TO_BLISS["U+406f"] = ["kazoo"]
BLISS_TO_UNICODE["draw"] = ["U+4070"]
UNICODE_TO_BLISS["U+4070"] = ["draw"]
BLISS_TO_UNICODE["sketch"] = ["U+4070"]
UNICODE_TO_BLISS["U+4070"].append("sketch")
BLISS_TO_UNICODE["draw,sketch"] = ["U+4070"]
UNICODE_TO_BLISS["U+4070"].append("draw,sketch")
BLISS_TO_UNICODE["woking"] = ["U+4071"]
UNICODE_TO_BLISS["U+4071"] = ["woking"]
BLISS_TO_UNICODE["multi storey home"] = ["U+4072"]
UNICODE_TO_BLISS["U+4072"] = ["multi storey home"]
BLISS_TO_UNICODE["combination of storey and home"] = ["U+4073"]
UNICODE_TO_BLISS["U+4073"] = ["combination of storey and home"]
BLISS_TO_UNICODE["impoverish"] = ["U+4074"]
UNICODE_TO_BLISS["U+4074"] = ["impoverish"]
BLISS_TO_UNICODE["simmer"] = ["U+4075"]
UNICODE_TO_BLISS["U+4075"] = ["simmer"]
BLISS_TO_UNICODE["poach"] = ["U+4075"]
UNICODE_TO_BLISS["U+4075"].append("poach")
BLISS_TO_UNICODE["simmer,poach"] = ["U+4075"]
UNICODE_TO_BLISS["U+4075"].append("simmer,poach")
BLISS_TO_UNICODE["rain gauge"] = ["U+4076"]
UNICODE_TO_BLISS["U+4076"] = ["rain gauge"]
BLISS_TO_UNICODE["current events"] = ["U+4077"]
UNICODE_TO_BLISS["U+4077"] = ["current events"]
BLISS_TO_UNICODE["run"] = ["U+4078"]
UNICODE_TO_BLISS["U+4078"] = ["run"]
BLISS_TO_UNICODE["rub"] = ["U+4079"]
UNICODE_TO_BLISS["U+4079"] = ["rub"]
BLISS_TO_UNICODE["massage"] = ["U+4079"]
UNICODE_TO_BLISS["U+4079"].append("massage")
BLISS_TO_UNICODE["rub,massage"] = ["U+4079"]
UNICODE_TO_BLISS["U+4079"].append("rub,massage")
BLISS_TO_UNICODE["stalk"] = ["U+3290"]
UNICODE_TO_BLISS["U+3290"].append("stalk")
BLISS_TO_UNICODE["stem,stalk"] = ["U+3290"]
UNICODE_TO_BLISS["U+3290"].append("stem,stalk")
BLISS_TO_UNICODE["Ganesh"] = ["U+407a"]
UNICODE_TO_BLISS["U+407a"] = ["Ganesh"]
BLISS_TO_UNICODE["stew"] = ["U+407b"]
UNICODE_TO_BLISS["U+407b"] = ["stew"]
BLISS_TO_UNICODE["ache"] = ["U+407c"]
UNICODE_TO_BLISS["U+407c"] = ["ache"]
BLISS_TO_UNICODE["subtract"] = ["U+407d"]
UNICODE_TO_BLISS["U+407d"] = ["subtract"]
BLISS_TO_UNICODE["remove"] = ["U+407d"]
UNICODE_TO_BLISS["U+407d"].append("remove")
BLISS_TO_UNICODE["take away"] = ["U+407d"]
UNICODE_TO_BLISS["U+407d"].append("take away")
BLISS_TO_UNICODE["subtract,remove,take away"] = ["U+407d"]
UNICODE_TO_BLISS["U+407d"].append("subtract,remove,take away")
BLISS_TO_UNICODE["beam"] = ["U+3923"]
UNICODE_TO_BLISS["U+3923"].append("beam")
BLISS_TO_UNICODE["shine,beam"] = ["U+3923"]
UNICODE_TO_BLISS["U+3923"].append("shine,beam")
BLISS_TO_UNICODE["dwarf"] = ["U+407e"]
UNICODE_TO_BLISS["U+407e"] = ["dwarf"]
BLISS_TO_UNICODE["gnome"] = ["U+407e"]
UNICODE_TO_BLISS["U+407e"].append("gnome")
BLISS_TO_UNICODE["dwarf,gnome"] = ["U+407e"]
UNICODE_TO_BLISS["U+407e"].append("dwarf,gnome")
BLISS_TO_UNICODE["horse drawn sleigh"] = ["U+3c6f"]
UNICODE_TO_BLISS["U+3c6f"].append("horse drawn sleigh")
BLISS_TO_UNICODE["horse sled,horse-drawn sleigh"] = ["U+3c6f"]
UNICODE_TO_BLISS["U+3c6f"].append("horse sled,horse-drawn sleigh")
BLISS_TO_UNICODE["paper clip"] = ["U+407f"]
UNICODE_TO_BLISS["U+407f"] = ["paper clip"]
BLISS_TO_UNICODE["quiet"] = ["U+3f0d"]
UNICODE_TO_BLISS["U+3f0d"].append("quiet")
BLISS_TO_UNICODE["silence,quiet"] = ["U+3f0d"]
UNICODE_TO_BLISS["U+3f0d"].append("silence,quiet")
BLISS_TO_UNICODE["intensity symbol"] = ["U+4080"]
UNICODE_TO_BLISS["U+4080"] = ["intensity symbol"]
BLISS_TO_UNICODE["respiratory system"] = ["U+4081"]
UNICODE_TO_BLISS["U+4081"] = ["respiratory system"]
BLISS_TO_UNICODE["corn syrup"] = ["U+4082"]
UNICODE_TO_BLISS["U+4082"] = ["corn syrup"]
BLISS_TO_UNICODE["ball pool"] = ["U+4083"]
UNICODE_TO_BLISS["U+4083"] = ["ball pool"]
BLISS_TO_UNICODE["himself"] = ["U+35c6"]
UNICODE_TO_BLISS["U+35c6"].append("himself")
BLISS_TO_UNICODE["he,him,himself"] = ["U+35c6"]
UNICODE_TO_BLISS["U+35c6"].append("he,him,himself")
BLISS_TO_UNICODE["finally"] = ["U+4084"]
UNICODE_TO_BLISS["U+4084"] = ["finally"]
BLISS_TO_UNICODE["at last"] = ["U+4084"]
UNICODE_TO_BLISS["U+4084"].append("at last")
BLISS_TO_UNICODE["finally,at last"] = ["U+4084"]
UNICODE_TO_BLISS["U+4084"].append("finally,at last")
BLISS_TO_UNICODE["bamboo"] = ["U+3e7e"]
UNICODE_TO_BLISS["U+3e7e"].append("bamboo")
BLISS_TO_UNICODE["reed,bamboo"] = ["U+3e7e"]
UNICODE_TO_BLISS["U+3e7e"].append("reed,bamboo")
BLISS_TO_UNICODE["reef"] = ["U+4085"]
UNICODE_TO_BLISS["U+4085"] = ["reef"]
BLISS_TO_UNICODE["Switzerland"] = ["U+4086"]
UNICODE_TO_BLISS["U+4086"] = ["Switzerland"]
BLISS_TO_UNICODE["inoculation"] = ["U+350f"]
UNICODE_TO_BLISS["U+350f"].append("inoculation")
BLISS_TO_UNICODE["shot"] = ["U+350f"]
UNICODE_TO_BLISS["U+350f"].append("shot")
BLISS_TO_UNICODE["injection,inoculation,shot"] = ["U+350f"]
UNICODE_TO_BLISS["U+350f"].append("injection,inoculation,shot")
BLISS_TO_UNICODE["pictograph of hypodermic syringe"] = ["U+4087"]
UNICODE_TO_BLISS["U+4087"] = ["pictograph of hypodermic syringe"]
BLISS_TO_UNICODE["Irish"] = ["U+4088"]
UNICODE_TO_BLISS["U+4088"] = ["Irish"]
BLISS_TO_UNICODE["shortness"].append("U+3ae7")
UNICODE_TO_BLISS["U+3ae7"].append("shortness")
BLISS_TO_UNICODE["lowness,shortness"] = ["U+3ae7"]
UNICODE_TO_BLISS["U+3ae7"].append("lowness,shortness")
BLISS_TO_UNICODE["like"] = ["U+3b5c"]
UNICODE_TO_BLISS["U+3b5c"].append("like")
BLISS_TO_UNICODE["alike"] = ["U+3b5c"]
UNICODE_TO_BLISS["U+3b5c"].append("alike")
BLISS_TO_UNICODE["similar,like,alike"] = ["U+3b5c"]
UNICODE_TO_BLISS["U+3b5c"].append("similar,like,alike")
BLISS_TO_UNICODE["accessibility"] = ["U+4089"]
UNICODE_TO_BLISS["U+4089"] = ["accessibility"]
BLISS_TO_UNICODE["kidney"] = ["U+408a"]
UNICODE_TO_BLISS["U+408a"] = ["kidney"]
BLISS_TO_UNICODE["cotton"] = ["U+408b"]
UNICODE_TO_BLISS["U+408b"] = ["cotton"]
BLISS_TO_UNICODE["nag"] = ["U+408c"]
UNICODE_TO_BLISS["U+408c"] = ["nag"]
BLISS_TO_UNICODE["objection"] = ["U+3bb9"]
UNICODE_TO_BLISS["U+3bb9"].append("objection")
BLISS_TO_UNICODE["opposition"].append("U+3bb9")
UNICODE_TO_BLISS["U+3bb9"].append("opposition")
BLISS_TO_UNICODE["protest,objection,opposition"] = ["U+3bb9"]
UNICODE_TO_BLISS["U+3bb9"].append("protest,objection,opposition")
BLISS_TO_UNICODE["electric"] = ["U+408d"]
UNICODE_TO_BLISS["U+408d"] = ["electric"]
BLISS_TO_UNICODE["electrical"] = ["U+408d"]
UNICODE_TO_BLISS["U+408d"].append("electrical")
BLISS_TO_UNICODE["electric,electrical"] = ["U+408d"]
UNICODE_TO_BLISS["U+408d"].append("electric,electrical")
BLISS_TO_UNICODE["autoharp"] = ["U+408e"]
UNICODE_TO_BLISS["U+408e"] = ["autoharp"]
BLISS_TO_UNICODE["zither"] = ["U+408e"]
UNICODE_TO_BLISS["U+408e"].append("zither")
BLISS_TO_UNICODE["kantele"] = ["U+408e"]
UNICODE_TO_BLISS["U+408e"].append("kantele")
BLISS_TO_UNICODE["autoharp,zither,kantele"] = ["U+408e"]
UNICODE_TO_BLISS["U+408e"].append("autoharp,zither,kantele")
BLISS_TO_UNICODE["fewest"] = ["U+408f"]
UNICODE_TO_BLISS["U+408f"] = ["fewest"]
BLISS_TO_UNICODE["least"] = ["U+408f"]
UNICODE_TO_BLISS["U+408f"].append("least")
BLISS_TO_UNICODE["fewest,least"] = ["U+408f"]
UNICODE_TO_BLISS["U+408f"].append("fewest,least")
BLISS_TO_UNICODE["resign"] = ["U+4090"]
UNICODE_TO_BLISS["U+4090"] = ["resign"]
BLISS_TO_UNICODE["quit"] = ["U+4090"]
UNICODE_TO_BLISS["U+4090"].append("quit")
BLISS_TO_UNICODE["resign,quit"] = ["U+4090"]
UNICODE_TO_BLISS["U+4090"].append("resign,quit")
BLISS_TO_UNICODE["headphones"] = ["U+32b4"]
UNICODE_TO_BLISS["U+32b4"].append("headphones")
BLISS_TO_UNICODE["earphones,headphones"] = ["U+32b4"]
UNICODE_TO_BLISS["U+32b4"].append("earphones,headphones")
BLISS_TO_UNICODE["compactness"] = ["U+3a37"]
UNICODE_TO_BLISS["U+3a37"].append("compactness")
BLISS_TO_UNICODE["tightness"] = ["U+3a37"]
UNICODE_TO_BLISS["U+3a37"].append("tightness")
BLISS_TO_UNICODE["density,denseness,compactness,tightness"] = ["U+3a37"]
UNICODE_TO_BLISS["U+3a37"].append("density,denseness,compactness,tightness")
BLISS_TO_UNICODE["physics"] = ["U+4092"]
UNICODE_TO_BLISS["U+4092"] = ["physics"]
BLISS_TO_UNICODE["outing"] = ["U+4093"]
UNICODE_TO_BLISS["U+4093"] = ["outing"]
BLISS_TO_UNICODE["excursion"] = ["U+4093"]
UNICODE_TO_BLISS["U+4093"].append("excursion")
BLISS_TO_UNICODE["outing,excursion"] = ["U+4093"]
UNICODE_TO_BLISS["U+4093"].append("outing,excursion")
BLISS_TO_UNICODE["depth"] = ["U+4094"]
UNICODE_TO_BLISS["U+4094"] = ["depth"]
BLISS_TO_UNICODE["amenorrhea"] = ["U+4095"]
UNICODE_TO_BLISS["U+4095"] = ["amenorrhea"]
BLISS_TO_UNICODE["Av"] = ["U+4096"]
UNICODE_TO_BLISS["U+4096"] = ["Av"]
BLISS_TO_UNICODE["self harming"] = ["U+4097"]
UNICODE_TO_BLISS["U+4097"] = ["self harming"]
BLISS_TO_UNICODE["self-harming"] = ["U+4097"]
UNICODE_TO_BLISS["U+4097"].append("self-harming")
BLISS_TO_UNICODE["depending on"] = ["U+4098"]
UNICODE_TO_BLISS["U+4098"] = ["depending on"]
BLISS_TO_UNICODE["advance"] = ["U+4099"]
UNICODE_TO_BLISS["U+4099"] = ["advance"]
BLISS_TO_UNICODE["go"].append("U+4099")
UNICODE_TO_BLISS["U+4099"].append("go")
BLISS_TO_UNICODE["advance,go"] = ["U+4099"]
UNICODE_TO_BLISS["U+4099"].append("advance,go")
BLISS_TO_UNICODE["go"].append("U+3fce")
UNICODE_TO_BLISS["U+3fce"].append("go")
BLISS_TO_UNICODE["walk,go"] = ["U+3fce"]
UNICODE_TO_BLISS["U+3fce"].append("walk,go")
BLISS_TO_UNICODE["wizard"] = ["U+409a"]
UNICODE_TO_BLISS["U+409a"] = ["wizard"]
BLISS_TO_UNICODE["make-believe man"] = ["U+409b"]
UNICODE_TO_BLISS["U+409b"] = ["make-believe man"]
BLISS_TO_UNICODE["ice covering"] = ["U+409c"]
UNICODE_TO_BLISS["U+409c"] = ["ice covering"]
BLISS_TO_UNICODE["ice crust"] = ["U+409c"]
UNICODE_TO_BLISS["U+409c"].append("ice crust")
BLISS_TO_UNICODE["ice coating"] = ["U+409c"]
UNICODE_TO_BLISS["U+409c"].append("ice coating")
BLISS_TO_UNICODE["ice covering,ice crust,ice coating"] = ["U+409c"]
UNICODE_TO_BLISS["U+409c"].append("ice covering,ice crust,ice coating")
BLISS_TO_UNICODE["people in the north"] = ["U+409d"]
UNICODE_TO_BLISS["U+409d"] = ["people in the north"]
BLISS_TO_UNICODE["Eskimos)"] = ["U+409d"]
UNICODE_TO_BLISS["U+409d"].append("Eskimos)")
BLISS_TO_UNICODE["jet ski"] = ["U+409e"]
UNICODE_TO_BLISS["U+409e"] = ["jet ski"]
BLISS_TO_UNICODE["schooner"] = ["U+409f"]
UNICODE_TO_BLISS["U+409f"] = ["schooner"]
BLISS_TO_UNICODE["intercourse"] = ["U+3751"]
UNICODE_TO_BLISS["U+3751"].append("intercourse")
BLISS_TO_UNICODE["copulation"] = ["U+3751"]
UNICODE_TO_BLISS["U+3751"].append("copulation")
BLISS_TO_UNICODE["sexual intercourse,intercourse,copulation"] = ["U+3751"]
UNICODE_TO_BLISS["U+3751"].append("sexual intercourse,intercourse,copulation")
BLISS_TO_UNICODE["to combine"] = ["U+40a0"]
UNICODE_TO_BLISS["U+40a0"] = ["to combine"]
BLISS_TO_UNICODE["ukulele"] = ["U+40a1"]
UNICODE_TO_BLISS["U+40a1"] = ["ukulele"]
BLISS_TO_UNICODE["fishnet"] = ["U+40a2"]
UNICODE_TO_BLISS["U+40a2"] = ["fishnet"]
BLISS_TO_UNICODE["Hugin and Munin"] = ["U+40a3"]
UNICODE_TO_BLISS["U+40a3"] = ["Hugin and Munin"]
BLISS_TO_UNICODE["social network"] = ["U+40a4"]
UNICODE_TO_BLISS["U+40a4"] = ["social network"]
BLISS_TO_UNICODE["facebook"] = ["U+40a4"]
UNICODE_TO_BLISS["U+40a4"].append("facebook")
BLISS_TO_UNICODE["social network,facebook"] = ["U+40a4"]
UNICODE_TO_BLISS["U+40a4"].append("social network,facebook")
BLISS_TO_UNICODE["nuclear fuel"] = ["U+40a5"]
UNICODE_TO_BLISS["U+40a5"] = ["nuclear fuel"]
BLISS_TO_UNICODE["stinging insect"].append("U+36ce")
UNICODE_TO_BLISS["U+36ce"].append("stinging insect")
BLISS_TO_UNICODE["louse,stinging insect"] = ["U+36ce"]
UNICODE_TO_BLISS["U+36ce"].append("louse,stinging insect")
BLISS_TO_UNICODE["pictograph of two curved lines"] = ["U+40a6"]
UNICODE_TO_BLISS["U+40a6"] = ["pictograph of two curved lines"]
BLISS_TO_UNICODE[" suggesting skates"] = ["U+40a7"]
UNICODE_TO_BLISS["U+40a7"] = [" suggesting skates"]
BLISS_TO_UNICODE["button"] = ["U+40a8"]
UNICODE_TO_BLISS["U+40a8"] = ["button"]
BLISS_TO_UNICODE["gripper"].append("U+40a8")
UNICODE_TO_BLISS["U+40a8"].append("gripper")
BLISS_TO_UNICODE["snap"] = ["U+40a8"]
UNICODE_TO_BLISS["U+40a8"].append("snap")
BLISS_TO_UNICODE["button,gripper,snap"] = ["U+40a8"]
UNICODE_TO_BLISS["U+40a8"].append("button,gripper,snap")
BLISS_TO_UNICODE["Uranus"] = ["U+40a9"]
UNICODE_TO_BLISS["U+40a9"] = ["Uranus"]
BLISS_TO_UNICODE["traffic rule"] = ["U+40aa"]
UNICODE_TO_BLISS["U+40aa"] = ["traffic rule"]
BLISS_TO_UNICODE["electric light"] = ["U+40ab"]
UNICODE_TO_BLISS["U+40ab"] = ["electric light"]
BLISS_TO_UNICODE["lamp"].append("U+40ab")
UNICODE_TO_BLISS["U+40ab"].append("lamp")
BLISS_TO_UNICODE["electric light,lamp"] = ["U+40ab"]
UNICODE_TO_BLISS["U+40ab"].append("electric light,lamp")
BLISS_TO_UNICODE["micro organism"] = ["U+40ac"]
UNICODE_TO_BLISS["U+40ac"] = ["micro organism"]
BLISS_TO_UNICODE["micro-organism"].append("U+40ac")
UNICODE_TO_BLISS["U+40ac"].append("micro-organism")
BLISS_TO_UNICODE["purse"] = ["U+40ad"]
UNICODE_TO_BLISS["U+40ad"] = ["purse"]
BLISS_TO_UNICODE["pocketbook"] = ["U+40ad"]
UNICODE_TO_BLISS["U+40ad"].append("pocketbook")
BLISS_TO_UNICODE["wallet"] = ["U+40ad"]
UNICODE_TO_BLISS["U+40ad"].append("wallet")
BLISS_TO_UNICODE["purse,pocketbook,wallet"] = ["U+40ad"]
UNICODE_TO_BLISS["U+40ad"].append("purse,pocketbook,wallet")
BLISS_TO_UNICODE["vampire"] = ["U+40ae"]
UNICODE_TO_BLISS["U+40ae"] = ["vampire"]
BLISS_TO_UNICODE["experiment"] = ["U+40af"]
UNICODE_TO_BLISS["U+40af"] = ["experiment"]
BLISS_TO_UNICODE["kidnapper"] = ["U+40b0"]
UNICODE_TO_BLISS["U+40b0"] = ["kidnapper"]
BLISS_TO_UNICODE["brooch"] = ["U+40b1"]
UNICODE_TO_BLISS["U+40b1"] = ["brooch"]
BLISS_TO_UNICODE["convert"] = ["U+40b2"]
UNICODE_TO_BLISS["U+40b2"] = ["convert"]
BLISS_TO_UNICODE["conversion"] = ["U+40b3"]
UNICODE_TO_BLISS["U+40b3"] = ["conversion"]
BLISS_TO_UNICODE["toilet chair"] = ["U+40b4"]
UNICODE_TO_BLISS["U+40b4"] = ["toilet chair"]
BLISS_TO_UNICODE["commode chair"] = ["U+40b4"]
UNICODE_TO_BLISS["U+40b4"].append("commode chair")
BLISS_TO_UNICODE["toilet chair,commode chair"] = ["U+40b4"]
UNICODE_TO_BLISS["U+40b4"].append("toilet chair,commode chair")
BLISS_TO_UNICODE["Arabic"] = ["U+40b5"]
UNICODE_TO_BLISS["U+40b5"] = ["Arabic"]
BLISS_TO_UNICODE["salvation"] = ["U+40b6"]
UNICODE_TO_BLISS["U+40b6"] = ["salvation"]
BLISS_TO_UNICODE["pitch"] = ["U+40b7"]
UNICODE_TO_BLISS["U+40b7"] = ["pitch"]
BLISS_TO_UNICODE["satisfaction"] = ["U+40b8"]
UNICODE_TO_BLISS["U+40b8"] = ["satisfaction"]
BLISS_TO_UNICODE["contentment"] = ["U+40b8"]
UNICODE_TO_BLISS["U+40b8"].append("contentment")
BLISS_TO_UNICODE["satisfaction,contentment"] = ["U+40b8"]
UNICODE_TO_BLISS["U+40b8"].append("satisfaction,contentment")
BLISS_TO_UNICODE["shellfish"].append("U+3502")
UNICODE_TO_BLISS["U+3502"].append("shellfish")
BLISS_TO_UNICODE["crab,shellfish"] = ["U+3502"]
UNICODE_TO_BLISS["U+3502"].append("crab,shellfish")
BLISS_TO_UNICODE["Lent"] = ["U+40b9"]
UNICODE_TO_BLISS["U+40b9"] = ["Lent"]
BLISS_TO_UNICODE["Easter"] = ["U+40ba"]
UNICODE_TO_BLISS["U+40ba"] = ["Easter"]
BLISS_TO_UNICODE["Denmark"] = ["U+40bb"]
UNICODE_TO_BLISS["U+40bb"] = ["Denmark"]
BLISS_TO_UNICODE["Wednesday"] = ["U+40bc"]
UNICODE_TO_BLISS["U+40bc"] = ["Wednesday"]
BLISS_TO_UNICODE["crossed racquets"] = ["U+40bd"]
UNICODE_TO_BLISS["U+40bd"] = ["crossed racquets"]
BLISS_TO_UNICODE["senior citizen"] = ["U+40be"]
UNICODE_TO_BLISS["U+40be"] = ["senior citizen"]
BLISS_TO_UNICODE["appetizer"] = ["U+40bf"]
UNICODE_TO_BLISS["U+40bf"] = ["appetizer"]
BLISS_TO_UNICODE["starter"] = ["U+40bf"]
UNICODE_TO_BLISS["U+40bf"].append("starter")
BLISS_TO_UNICODE["entree"] = ["U+40bf"]
UNICODE_TO_BLISS["U+40bf"].append("entree")
BLISS_TO_UNICODE["appetizer,starter,entree"] = ["U+40bf"]
UNICODE_TO_BLISS["U+40bf"].append("appetizer,starter,entree")
BLISS_TO_UNICODE["Eastern Orthodox Church"] = ["U+40c1"]
UNICODE_TO_BLISS["U+40c1"] = ["Eastern Orthodox Church"]
BLISS_TO_UNICODE["drive"] = ["U+33e4"]
UNICODE_TO_BLISS["U+33e4"].append("drive")
BLISS_TO_UNICODE["ride,drive"] = ["U+33e4"]
UNICODE_TO_BLISS["U+33e4"].append("ride,drive")
BLISS_TO_UNICODE["sitting"] = ["U+40c2"]
UNICODE_TO_BLISS["U+40c2"] = ["sitting"]
BLISS_TO_UNICODE["orange"] = ["U+40c3"]
UNICODE_TO_BLISS["U+40c3"] = ["orange"]
BLISS_TO_UNICODE["citrus fruit"].append("U+40c3")
UNICODE_TO_BLISS["U+40c3"].append("citrus fruit")
BLISS_TO_UNICODE["orange,citrus fruit"] = ["U+40c3"]
UNICODE_TO_BLISS["U+40c3"].append("orange,citrus fruit")
BLISS_TO_UNICODE["pictograph of segments"] = ["U+40c4"]
UNICODE_TO_BLISS["U+40c4"] = ["pictograph of segments"]
BLISS_TO_UNICODE["wall climbing"] = ["U+40c5"]
UNICODE_TO_BLISS["U+40c5"] = ["wall climbing"]
BLISS_TO_UNICODE["tailor"] = ["U+40c6"]
UNICODE_TO_BLISS["U+40c6"] = ["tailor"]
BLISS_TO_UNICODE["dressmaker"] = ["U+40c6"]
UNICODE_TO_BLISS["U+40c6"].append("dressmaker")
BLISS_TO_UNICODE["seamstress"] = ["U+40c6"]
UNICODE_TO_BLISS["U+40c6"].append("seamstress")
BLISS_TO_UNICODE["tailor,dressmaker,seamstress"] = ["U+40c6"]
UNICODE_TO_BLISS["U+40c6"].append("tailor,dressmaker,seamstress")
BLISS_TO_UNICODE["any day"] = ["U+40c7"]
UNICODE_TO_BLISS["U+40c7"] = ["any day"]
BLISS_TO_UNICODE["someday"] = ["U+40c7"]
UNICODE_TO_BLISS["U+40c7"].append("someday")
BLISS_TO_UNICODE["any day,someday"] = ["U+40c7"]
UNICODE_TO_BLISS["U+40c7"].append("any day,someday")
BLISS_TO_UNICODE["skirt"] = ["U+40c8"]
UNICODE_TO_BLISS["U+40c8"] = ["skirt"]
BLISS_TO_UNICODE["sweat"] = ["U+40c9"]
UNICODE_TO_BLISS["U+40c9"] = ["sweat"]
BLISS_TO_UNICODE["perspire"] = ["U+40c9"]
UNICODE_TO_BLISS["U+40c9"].append("perspire")
BLISS_TO_UNICODE["sweat,perspire"] = ["U+40c9"]
UNICODE_TO_BLISS["U+40c9"].append("sweat,perspire")
BLISS_TO_UNICODE["oval"] = ["U+40ca"]
UNICODE_TO_BLISS["U+40ca"] = ["oval"]
BLISS_TO_UNICODE["elliptic"] = ["U+40ca"]
UNICODE_TO_BLISS["U+40ca"].append("elliptic")
BLISS_TO_UNICODE["elliptical"] = ["U+40ca"]
UNICODE_TO_BLISS["U+40ca"].append("elliptical")
BLISS_TO_UNICODE["oval,elliptic,elliptical"] = ["U+40ca"]
UNICODE_TO_BLISS["U+40ca"].append("oval,elliptic,elliptical")
BLISS_TO_UNICODE["mailbox"] = ["U+40cb"]
UNICODE_TO_BLISS["U+40cb"] = ["mailbox"]
BLISS_TO_UNICODE["letterbox"] = ["U+40cb"]
UNICODE_TO_BLISS["U+40cb"].append("letterbox")
BLISS_TO_UNICODE["postbox"] = ["U+40cb"]
UNICODE_TO_BLISS["U+40cb"].append("postbox")
BLISS_TO_UNICODE["mailbox,letterbox,postbox"] = ["U+40cb"]
UNICODE_TO_BLISS["U+40cb"].append("mailbox,letterbox,postbox")
BLISS_TO_UNICODE["circular"] = ["U+3743"]
UNICODE_TO_BLISS["U+3743"].append("circular")
BLISS_TO_UNICODE["round,circular"] = ["U+3743"]
UNICODE_TO_BLISS["U+3743"].append("round,circular")
BLISS_TO_UNICODE["pink"] = ["U+40cc"]
UNICODE_TO_BLISS["U+40cc"] = ["pink"]
BLISS_TO_UNICODE["bells"] = ["U+40cd"]
UNICODE_TO_BLISS["U+40cd"] = ["bells"]
BLISS_TO_UNICODE["chime bars"] = ["U+40cd"]
UNICODE_TO_BLISS["U+40cd"].append("chime bars")
BLISS_TO_UNICODE["tubular bells"] = ["U+40cd"]
UNICODE_TO_BLISS["U+40cd"].append("tubular bells")
BLISS_TO_UNICODE["bells,chime bars,tubular bells"] = ["U+40cd"]
UNICODE_TO_BLISS["U+40cd"].append("bells,chime bars,tubular bells")
BLISS_TO_UNICODE["cutlery"] = ["U+40ce"]
UNICODE_TO_BLISS["U+40ce"] = ["cutlery"]
BLISS_TO_UNICODE["tail wing"] = ["U+40cf"]
UNICODE_TO_BLISS["U+40cf"] = ["tail wing"]
BLISS_TO_UNICODE["bakery"] = ["U+40d0"]
UNICODE_TO_BLISS["U+40d0"] = ["bakery"]
BLISS_TO_UNICODE["agenda"] = ["U+40d1"]
UNICODE_TO_BLISS["U+40d1"] = ["agenda"]
BLISS_TO_UNICODE["memory stick"] = ["U+40d2"]
UNICODE_TO_BLISS["U+40d2"] = ["memory stick"]
BLISS_TO_UNICODE["USB memory"] = ["U+40d2"]
UNICODE_TO_BLISS["U+40d2"].append("USB memory")
BLISS_TO_UNICODE["memory stick,USB-memory"] = ["U+40d2"]
UNICODE_TO_BLISS["U+40d2"].append("memory stick,USB-memory")
BLISS_TO_UNICODE["digital storage device"] = ["U+40d3"]
UNICODE_TO_BLISS["U+40d3"] = ["digital storage device"]
BLISS_TO_UNICODE["make believe person"] = ["U+40d4"]
UNICODE_TO_BLISS["U+40d4"] = ["make believe person"]
BLISS_TO_UNICODE["imaginary person"].append("U+40d4")
UNICODE_TO_BLISS["U+40d4"].append("imaginary person")
BLISS_TO_UNICODE["make-believe person,imaginary person"] = ["U+40d4"]
UNICODE_TO_BLISS["U+40d4"].append("make-believe person,imaginary person")
BLISS_TO_UNICODE["make-believe person"].append("U+40d4")
UNICODE_TO_BLISS["U+40d4"].append("make-believe person")
BLISS_TO_UNICODE["water nymph"] = ["U+40d4"]
UNICODE_TO_BLISS["U+40d4"].append("water nymph")
BLISS_TO_UNICODE["stone age"] = ["U+40d5"]
UNICODE_TO_BLISS["U+40d5"] = ["stone age"]
BLISS_TO_UNICODE["hand splint"] = ["U+40d6"]
UNICODE_TO_BLISS["U+40d6"] = ["hand splint"]
BLISS_TO_UNICODE["salivary gland"] = ["U+40d7"]
UNICODE_TO_BLISS["U+40d7"] = ["salivary gland"]
BLISS_TO_UNICODE["menstrual blood"] = ["U+40d8"]
UNICODE_TO_BLISS["U+40d8"] = ["menstrual blood"]
BLISS_TO_UNICODE["sword"].append("U+3448")
UNICODE_TO_BLISS["U+3448"].append("sword")
BLISS_TO_UNICODE["knife,sword"] = ["U+3448"]
UNICODE_TO_BLISS["U+3448"].append("knife,sword")
BLISS_TO_UNICODE["functional"] = ["U+40d9"]
UNICODE_TO_BLISS["U+40d9"] = ["functional"]
BLISS_TO_UNICODE["sweets"] = ["U+3bc7"]
UNICODE_TO_BLISS["U+3bc7"].append("sweets")
BLISS_TO_UNICODE["candy,sweets"] = ["U+3bc7"]
UNICODE_TO_BLISS["U+3bc7"].append("candy,sweets")
BLISS_TO_UNICODE["loss"].append("U+348c")
UNICODE_TO_BLISS["U+348c"].append("loss")
BLISS_TO_UNICODE["subtraction,loss"] = ["U+348c"]
UNICODE_TO_BLISS["U+348c"].append("subtraction,loss")
BLISS_TO_UNICODE["based upon the international mathematical symbol"] = ["U+40da"]
UNICODE_TO_BLISS["U+40da"] = ["based upon the international mathematical symbol"]
BLISS_TO_UNICODE["sport fanatic"] = ["U+40db"]
UNICODE_TO_BLISS["U+40db"] = ["sport fanatic"]
BLISS_TO_UNICODE["Venus"] = ["U+40dc"]
UNICODE_TO_BLISS["U+40dc"] = ["Venus"]
BLISS_TO_UNICODE["tea break"] = ["U+40dd"]
UNICODE_TO_BLISS["U+40dd"] = ["tea break"]
BLISS_TO_UNICODE["coffee break"] = ["U+40dd"]
UNICODE_TO_BLISS["U+40dd"].append("coffee break")
BLISS_TO_UNICODE["tea break,coffee break"] = ["U+40dd"]
UNICODE_TO_BLISS["U+40dd"].append("tea break,coffee break")
BLISS_TO_UNICODE["Havdalah"] = ["U+40de"]
UNICODE_TO_BLISS["U+40de"] = ["Havdalah"]
BLISS_TO_UNICODE["university"] = ["U+40df"]
UNICODE_TO_BLISS["U+40df"] = ["university"]
BLISS_TO_UNICODE["armoured force"] = ["U+40e0"]
UNICODE_TO_BLISS["U+40e0"] = ["armoured force"]
BLISS_TO_UNICODE["tank force"] = ["U+40e0"]
UNICODE_TO_BLISS["U+40e0"].append("tank force")
BLISS_TO_UNICODE["armoured force,tank force"] = ["U+40e0"]
UNICODE_TO_BLISS["U+40e0"].append("armoured force,tank force")
BLISS_TO_UNICODE["female"].append("U+34ee")
UNICODE_TO_BLISS["U+34ee"].append("female")
BLISS_TO_UNICODE["woman,female"] = ["U+34ee"]
UNICODE_TO_BLISS["U+34ee"].append("woman,female")
BLISS_TO_UNICODE["cross country skiing"] = ["U+40e1"]
UNICODE_TO_BLISS["U+40e1"] = ["cross country skiing"]
BLISS_TO_UNICODE["special"] = ["U+40e2"]
UNICODE_TO_BLISS["U+40e2"] = ["special"]
BLISS_TO_UNICODE["particular"] = ["U+40e2"]
UNICODE_TO_BLISS["U+40e2"].append("particular")
BLISS_TO_UNICODE["special,particular"] = ["U+40e2"]
UNICODE_TO_BLISS["U+40e2"].append("special,particular")
BLISS_TO_UNICODE["confess"] = ["U+40e3"]
UNICODE_TO_BLISS["U+40e3"] = ["confess"]
BLISS_TO_UNICODE["foster mother"] = ["U+40e4"]
UNICODE_TO_BLISS["U+40e4"] = ["foster mother"]
BLISS_TO_UNICODE["have impact on"] = ["U+40e5"]
UNICODE_TO_BLISS["U+40e5"] = ["have impact on"]
BLISS_TO_UNICODE["wedge shape that incorporates relation"] = ["U+40e6"]
UNICODE_TO_BLISS["U+40e6"] = ["wedge shape that incorporates relation"]
BLISS_TO_UNICODE["pictograph of an umbrella handle"] = ["U+40e7"]
UNICODE_TO_BLISS["U+40e7"] = ["pictograph of an umbrella handle"]
BLISS_TO_UNICODE["wrist splint"] = ["U+40e8"]
UNICODE_TO_BLISS["U+40e8"] = ["wrist splint"]
BLISS_TO_UNICODE["wading pool"] = ["U+40e9"]
UNICODE_TO_BLISS["U+40e9"] = ["wading pool"]
BLISS_TO_UNICODE["paddling pool"] = ["U+40e9"]
UNICODE_TO_BLISS["U+40e9"].append("paddling pool")
BLISS_TO_UNICODE["wading pool,paddling pool"] = ["U+40e9"]
UNICODE_TO_BLISS["U+40e9"].append("wading pool,paddling pool")
BLISS_TO_UNICODE["water toy"] = ["U+40ea"]
UNICODE_TO_BLISS["U+40ea"] = ["water toy"]
BLISS_TO_UNICODE["undo"] = ["U+40eb"]
UNICODE_TO_BLISS["U+40eb"] = ["undo"]
BLISS_TO_UNICODE["shaving soap"] = ["U+40ec"]
UNICODE_TO_BLISS["U+40ec"] = ["shaving soap"]
BLISS_TO_UNICODE["shaving cream"] = ["U+40ec"]
UNICODE_TO_BLISS["U+40ec"].append("shaving cream")
BLISS_TO_UNICODE["shaving soap,shaving cream"] = ["U+40ec"]
UNICODE_TO_BLISS["U+40ec"].append("shaving soap,shaving cream")
BLISS_TO_UNICODE["drowning"] = ["U+40ed"]
UNICODE_TO_BLISS["U+40ed"] = ["drowning"]
BLISS_TO_UNICODE["Kabbalat Shabbat"] = ["U+40ee"]
UNICODE_TO_BLISS["U+40ee"] = ["Kabbalat Shabbat"]
BLISS_TO_UNICODE["greeting"] = ["U+40ef"]
UNICODE_TO_BLISS["U+40ef"] = ["greeting"]
BLISS_TO_UNICODE["timer"] = ["U+40f0"]
UNICODE_TO_BLISS["U+40f0"] = ["timer"]
BLISS_TO_UNICODE["keel"] = ["U+40f1"]
UNICODE_TO_BLISS["U+40f1"] = ["keel"]
BLISS_TO_UNICODE["rocket"].append("U+3ca6")
UNICODE_TO_BLISS["U+3ca6"].append("rocket")
BLISS_TO_UNICODE["spacecraft"] = ["U+3ca6"]
UNICODE_TO_BLISS["U+3ca6"].append("spacecraft")
BLISS_TO_UNICODE["projectile,rocket,spacecraft"] = ["U+3ca6"]
UNICODE_TO_BLISS["U+3ca6"].append("projectile,rocket,spacecraft")
BLISS_TO_UNICODE["pictograph of a pointed top"] = ["U+40f2"]
UNICODE_TO_BLISS["U+40f2"] = ["pictograph of a pointed top"]
BLISS_TO_UNICODE["date"] = ["U+40f3"]
UNICODE_TO_BLISS["U+40f3"] = ["date"]
BLISS_TO_UNICODE["pit)"] = ["U+40f4"]
UNICODE_TO_BLISS["U+40f4"] = ["pit)"]
BLISS_TO_UNICODE["quality"] = ["U+40f5"]
UNICODE_TO_BLISS["U+40f5"] = ["quality"]
BLISS_TO_UNICODE["protection with pointer"] = ["U+40f6"]
UNICODE_TO_BLISS["U+40f6"] = ["protection with pointer"]
BLISS_TO_UNICODE["headscarf"] = ["U+40f7"]
UNICODE_TO_BLISS["U+40f7"] = ["headscarf"]
BLISS_TO_UNICODE["flower fairy"] = ["U+40f8"]
UNICODE_TO_BLISS["U+40f8"] = ["flower fairy"]
BLISS_TO_UNICODE["fasten"] = ["U+40f9"]
UNICODE_TO_BLISS["U+40f9"] = ["fasten"]
BLISS_TO_UNICODE["attach"].append("U+40f9")
UNICODE_TO_BLISS["U+40f9"].append("attach")
BLISS_TO_UNICODE["join"] = ["U+40f9"]
UNICODE_TO_BLISS["U+40f9"].append("join")
BLISS_TO_UNICODE["append"] = ["U+40f9"]
UNICODE_TO_BLISS["U+40f9"].append("append")
BLISS_TO_UNICODE["connect"].append("U+40f9")
UNICODE_TO_BLISS["U+40f9"].append("connect")
BLISS_TO_UNICODE["fasten,attach,join,append,connect"] = ["U+40f9"]
UNICODE_TO_BLISS["U+40f9"].append("fasten,attach,join,append,connect")
BLISS_TO_UNICODE["attack"] = ["U+40fa"]
UNICODE_TO_BLISS["U+40fa"] = ["attack"]
BLISS_TO_UNICODE["of illness"] = ["U+40fb"]
UNICODE_TO_BLISS["U+40fb"] = ["of illness"]
BLISS_TO_UNICODE["manifestation"] = ["U+3ea8"]
UNICODE_TO_BLISS["U+3ea8"].append("manifestation")
BLISS_TO_UNICODE["appearance,manifestation"] = ["U+3ea8"]
UNICODE_TO_BLISS["U+3ea8"].append("appearance,manifestation")
BLISS_TO_UNICODE["facial hair"] = ["U+40fc"]
UNICODE_TO_BLISS["U+40fc"] = ["facial hair"]
BLISS_TO_UNICODE["beg"] = ["U+40fd"]
UNICODE_TO_BLISS["U+40fd"] = ["beg"]
BLISS_TO_UNICODE["plead"] = ["U+40fd"]
UNICODE_TO_BLISS["U+40fd"].append("plead")
BLISS_TO_UNICODE["beg,plead"] = ["U+40fd"]
UNICODE_TO_BLISS["U+40fd"].append("beg,plead")
BLISS_TO_UNICODE["to ask"] = ["U+40fe"]
UNICODE_TO_BLISS["U+40fe"] = ["to ask"]
BLISS_TO_UNICODE["please"] = ["U+40ff"]
UNICODE_TO_BLISS["U+40ff"] = ["please"]
BLISS_TO_UNICODE["bee"] = ["U+4100"]
UNICODE_TO_BLISS["U+4100"] = ["bee"]
BLISS_TO_UNICODE["saddle pad"] = ["U+4101"]
UNICODE_TO_BLISS["U+4101"] = ["saddle pad"]
BLISS_TO_UNICODE["saddle blanket"] = ["U+4101"]
UNICODE_TO_BLISS["U+4101"].append("saddle blanket")
BLISS_TO_UNICODE["saddle pad,saddle blanket"] = ["U+4101"]
UNICODE_TO_BLISS["U+4101"].append("saddle pad,saddle blanket")
BLISS_TO_UNICODE["saddle"] = ["U+4102"]
UNICODE_TO_BLISS["U+4102"] = ["saddle"]
BLISS_TO_UNICODE["firework"] = ["U+4103"]
UNICODE_TO_BLISS["U+4103"] = ["firework"]
BLISS_TO_UNICODE["bet"] = ["U+4104"]
UNICODE_TO_BLISS["U+4104"] = ["bet"]
BLISS_TO_UNICODE["symbol suggests the path made by the thread of a screw"] = ["U+4105"]
UNICODE_TO_BLISS["U+4105"] = ["symbol suggests the path made by the thread of a screw"]
BLISS_TO_UNICODE["microphone"] = ["U+4106"]
UNICODE_TO_BLISS["U+4106"] = ["microphone"]
BLISS_TO_UNICODE["carrycot"] = ["U+4107"]
UNICODE_TO_BLISS["U+4107"] = ["carrycot"]
BLISS_TO_UNICODE["bassinet"] = ["U+4107"]
UNICODE_TO_BLISS["U+4107"].append("bassinet")
BLISS_TO_UNICODE["carrycot,bassinet"] = ["U+4107"]
UNICODE_TO_BLISS["U+4107"].append("carrycot,bassinet")
BLISS_TO_UNICODE["Batman"] = ["U+4108"]
UNICODE_TO_BLISS["U+4108"] = ["Batman"]
BLISS_TO_UNICODE["gym mat"] = ["U+4109"]
UNICODE_TO_BLISS["U+4109"] = ["gym mat"]
BLISS_TO_UNICODE["lorry"].append("U+3549")
UNICODE_TO_BLISS["U+3549"].append("lorry")
BLISS_TO_UNICODE["truck,lorry"] = ["U+3549"]
UNICODE_TO_BLISS["U+3549"].append("truck,lorry")
BLISS_TO_UNICODE["speaker"] = ["U+410a"]
UNICODE_TO_BLISS["U+410a"] = ["speaker"]
BLISS_TO_UNICODE["lecturer"] = ["U+410a"]
UNICODE_TO_BLISS["U+410a"].append("lecturer")
BLISS_TO_UNICODE["speaker,lecturer"] = ["U+410a"]
UNICODE_TO_BLISS["U+410a"].append("speaker,lecturer")
BLISS_TO_UNICODE["orthoptist"] = ["U+410b"]
UNICODE_TO_BLISS["U+410b"] = ["orthoptist"]
BLISS_TO_UNICODE["Sniff"] = ["U+410c"]
UNICODE_TO_BLISS["U+410c"] = ["Sniff"]
BLISS_TO_UNICODE["scared"] = ["U+410d"]
UNICODE_TO_BLISS["U+410d"] = ["scared"]
BLISS_TO_UNICODE["odd number"] = ["U+410e"]
UNICODE_TO_BLISS["U+410e"] = ["odd number"]
BLISS_TO_UNICODE["acupuncturist"] = ["U+410f"]
UNICODE_TO_BLISS["U+410f"] = ["acupuncturist"]
BLISS_TO_UNICODE["art gallery"] = ["U+4110"]
UNICODE_TO_BLISS["U+4110"] = ["art gallery"]
BLISS_TO_UNICODE["gallery"] = ["U+4110"]
UNICODE_TO_BLISS["U+4110"].append("gallery")
BLISS_TO_UNICODE["art gallery,gallery"] = ["U+4110"]
UNICODE_TO_BLISS["U+4110"].append("art gallery,gallery")
BLISS_TO_UNICODE["mobile phone"] = ["U+4111"]
UNICODE_TO_BLISS["U+4111"] = ["mobile phone"]
BLISS_TO_UNICODE["cellphone"] = ["U+4111"]
UNICODE_TO_BLISS["U+4111"].append("cellphone")
BLISS_TO_UNICODE["mobile phone,cellphone"] = ["U+4111"]
UNICODE_TO_BLISS["U+4111"].append("mobile phone,cellphone")
BLISS_TO_UNICODE["spleen"] = ["U+4112"]
UNICODE_TO_BLISS["U+4112"] = ["spleen"]
BLISS_TO_UNICODE["parachute harness"] = ["U+4113"]
UNICODE_TO_BLISS["U+4113"] = ["parachute harness"]
BLISS_TO_UNICODE["skunk"] = ["U+4114"]
UNICODE_TO_BLISS["U+4114"] = ["skunk"]
BLISS_TO_UNICODE["to smell bad"] = ["U+4115"]
UNICODE_TO_BLISS["U+4115"] = ["to smell bad"]
BLISS_TO_UNICODE["mixing spoon"] = ["U+4116"]
UNICODE_TO_BLISS["U+4116"] = ["mixing spoon"]
BLISS_TO_UNICODE["tire"] = ["U+4117"]
UNICODE_TO_BLISS["U+4117"] = ["tire"]
BLISS_TO_UNICODE["tyre"].append("U+4117")
UNICODE_TO_BLISS["U+4117"].append("tyre")
BLISS_TO_UNICODE["tire,tyre"] = ["U+4117"]
UNICODE_TO_BLISS["U+4117"].append("tire,tyre")
BLISS_TO_UNICODE["hopeful"] = ["U+4118"]
UNICODE_TO_BLISS["U+4118"] = ["hopeful"]
BLISS_TO_UNICODE["rash"] = ["U+4119"]
UNICODE_TO_BLISS["U+4119"] = ["rash"]
BLISS_TO_UNICODE["achieve"] = ["U+411a"]
UNICODE_TO_BLISS["U+411a"] = ["achieve"]
BLISS_TO_UNICODE["achievement"] = ["U+411b"]
UNICODE_TO_BLISS["U+411b"] = ["achievement"]
BLISS_TO_UNICODE["riding clothes"] = ["U+411c"]
UNICODE_TO_BLISS["U+411c"] = ["riding clothes"]
BLISS_TO_UNICODE["pointer to the junction where they meet"] = ["U+411d"]
UNICODE_TO_BLISS["U+411d"] = ["pointer to the junction where they meet"]
BLISS_TO_UNICODE["roast"] = ["U+411e"]
UNICODE_TO_BLISS["U+411e"] = ["roast"]
BLISS_TO_UNICODE["joint"].append("U+411e")
UNICODE_TO_BLISS["U+411e"].append("joint")
BLISS_TO_UNICODE["roast,joint"] = ["U+411e"]
UNICODE_TO_BLISS["U+411e"].append("roast,joint")
BLISS_TO_UNICODE["Italian"] = ["U+411f"]
UNICODE_TO_BLISS["U+411f"] = ["Italian"]
BLISS_TO_UNICODE["opera"] = ["U+4120"]
UNICODE_TO_BLISS["U+4120"] = ["opera"]
BLISS_TO_UNICODE["legal {contr.]"] = ["U+4121"]
UNICODE_TO_BLISS["U+4121"] = ["legal {contr.]"]
BLISS_TO_UNICODE["blissymbol part"] = ["U+4122"]
UNICODE_TO_BLISS["U+4122"] = ["blissymbol part"]
BLISS_TO_UNICODE["DVD player"] = ["U+4123"]
UNICODE_TO_BLISS["U+4123"] = ["DVD player"]
BLISS_TO_UNICODE["DVD"] = ["U+4124"]
UNICODE_TO_BLISS["U+4124"] = ["DVD"]
BLISS_TO_UNICODE["movie disc"] = ["U+4125"]
UNICODE_TO_BLISS["U+4125"] = ["movie disc"]
BLISS_TO_UNICODE["motorboat"] = ["U+4126"]
UNICODE_TO_BLISS["U+4126"] = ["motorboat"]
BLISS_TO_UNICODE["grab"] = ["U+3b20"]
UNICODE_TO_BLISS["U+3b20"].append("grab")
BLISS_TO_UNICODE["catch,grab"] = ["U+3b20"]
UNICODE_TO_BLISS["U+3b20"].append("catch,grab")
BLISS_TO_UNICODE["body painting"] = ["U+4127"]
UNICODE_TO_BLISS["U+4127"] = ["body painting"]
BLISS_TO_UNICODE["preach"] = ["U+4128"]
UNICODE_TO_BLISS["U+4128"] = ["preach"]
BLISS_TO_UNICODE["to persuade"] = ["U+4129"]
UNICODE_TO_BLISS["U+4129"] = ["to persuade"]
BLISS_TO_UNICODE["riding helmet"] = ["U+412a"]
UNICODE_TO_BLISS["U+412a"] = ["riding helmet"]
BLISS_TO_UNICODE["solidify"] = ["U+3212"]
UNICODE_TO_BLISS["U+3212"].append("solidify")
BLISS_TO_UNICODE["freeze,solidify"] = ["U+3212"]
UNICODE_TO_BLISS["U+3212"].append("freeze,solidify")
BLISS_TO_UNICODE["computer"] = ["U+412b"]
UNICODE_TO_BLISS["U+412b"] = ["computer"]
BLISS_TO_UNICODE["overturn"] = ["U+412c"]
UNICODE_TO_BLISS["U+412c"] = ["overturn"]
BLISS_TO_UNICODE["turn over"] = ["U+412c"]
UNICODE_TO_BLISS["U+412c"].append("turn over")
BLISS_TO_UNICODE["tip over"] = ["U+412c"]
UNICODE_TO_BLISS["U+412c"].append("tip over")
BLISS_TO_UNICODE["overturn,turn over,tip over"] = ["U+412c"]
UNICODE_TO_BLISS["U+412c"].append("overturn,turn over,tip over")
BLISS_TO_UNICODE["direction"] = ["U+412d"]
UNICODE_TO_BLISS["U+412d"] = ["direction"]
BLISS_TO_UNICODE["cardinal point"] = ["U+412d"]
UNICODE_TO_BLISS["U+412d"].append("cardinal point")
BLISS_TO_UNICODE["direction,cardinal point"] = ["U+412d"]
UNICODE_TO_BLISS["U+412d"].append("direction,cardinal point")
BLISS_TO_UNICODE["washable"] = ["U+412e"]
UNICODE_TO_BLISS["U+412e"] = ["washable"]
BLISS_TO_UNICODE["freestyle skiing"] = ["U+412f"]
UNICODE_TO_BLISS["U+412f"] = ["freestyle skiing"]
BLISS_TO_UNICODE["southward"] = ["U+4130"]
UNICODE_TO_BLISS["U+4130"] = ["southward"]
BLISS_TO_UNICODE["text phone"] = ["U+4131"]
UNICODE_TO_BLISS["U+4131"] = ["text phone"]
BLISS_TO_UNICODE["province"] = ["U+4132"]
UNICODE_TO_BLISS["U+4132"] = ["province"]
BLISS_TO_UNICODE["county"] = ["U+4132"]
UNICODE_TO_BLISS["U+4132"].append("county")
BLISS_TO_UNICODE["region"] = ["U+4132"]
UNICODE_TO_BLISS["U+4132"].append("region")
BLISS_TO_UNICODE["state"].append("U+4132")
UNICODE_TO_BLISS["U+4132"].append("state")
BLISS_TO_UNICODE["province,county,region,state"] = ["U+4132"]
UNICODE_TO_BLISS["U+4132"].append("province,county,region,state")
BLISS_TO_UNICODE["tent"] = ["U+4133"]
UNICODE_TO_BLISS["U+4133"] = ["tent"]
BLISS_TO_UNICODE["police force"] = ["U+4134"]
UNICODE_TO_BLISS["U+4134"] = ["police force"]
BLISS_TO_UNICODE["police"] = ["U+4134"]
UNICODE_TO_BLISS["U+4134"].append("police")
BLISS_TO_UNICODE["police force,police"] = ["U+4134"]
UNICODE_TO_BLISS["U+4134"].append("police force,police")
BLISS_TO_UNICODE["treasured"] = ["U+3722"]
UNICODE_TO_BLISS["U+3722"].append("treasured")
BLISS_TO_UNICODE["precious,treasured"] = ["U+3722"]
UNICODE_TO_BLISS["U+3722"].append("precious,treasured")
BLISS_TO_UNICODE["thank"] = ["U+4135"]
UNICODE_TO_BLISS["U+4135"] = ["thank"]
BLISS_TO_UNICODE["condiment"] = ["U+392b"]
UNICODE_TO_BLISS["U+392b"].append("condiment")
BLISS_TO_UNICODE["seasoning"] = ["U+392b"]
UNICODE_TO_BLISS["U+392b"].append("seasoning")
BLISS_TO_UNICODE["flavouring,condiment,seasoning"] = ["U+392b"]
UNICODE_TO_BLISS["U+392b"].append("flavouring,condiment,seasoning")
BLISS_TO_UNICODE["succeed"] = ["U+4136"]
UNICODE_TO_BLISS["U+4136"] = ["succeed"]
BLISS_TO_UNICODE["peanut butter"] = ["U+4137"]
UNICODE_TO_BLISS["U+4137"] = ["peanut butter"]
BLISS_TO_UNICODE["hydrotherapy"] = ["U+4138"]
UNICODE_TO_BLISS["U+4138"] = ["hydrotherapy"]
BLISS_TO_UNICODE["sailboard"] = ["U+4139"]
UNICODE_TO_BLISS["U+4139"] = ["sailboard"]
BLISS_TO_UNICODE["sari"] = ["U+413b"]
UNICODE_TO_BLISS["U+413b"] = ["sari"]
BLISS_TO_UNICODE["gain"].append("U+3431")
UNICODE_TO_BLISS["U+3431"].append("gain")
BLISS_TO_UNICODE["addition,gain"] = ["U+3431"]
UNICODE_TO_BLISS["U+3431"].append("addition,gain")
BLISS_TO_UNICODE["ankle splint"] = ["U+413c"]
UNICODE_TO_BLISS["U+413c"] = ["ankle splint"]
BLISS_TO_UNICODE["sports centre"] = ["U+413d"]
UNICODE_TO_BLISS["U+413d"] = ["sports centre"]
BLISS_TO_UNICODE["cent"] = ["U+413e"]
UNICODE_TO_BLISS["U+413e"] = ["cent"]
BLISS_TO_UNICODE["international symbol for cent"] = ["U+413f"]
UNICODE_TO_BLISS["U+413f"] = ["international symbol for cent"]
BLISS_TO_UNICODE["sweet potato"] = ["U+4140"]
UNICODE_TO_BLISS["U+4140"] = ["sweet potato"]
BLISS_TO_UNICODE["yam"] = ["U+4140"]
UNICODE_TO_BLISS["U+4140"].append("yam")
BLISS_TO_UNICODE["sweet potato,yam"] = ["U+4140"]
UNICODE_TO_BLISS["U+4140"].append("sweet potato,yam")
BLISS_TO_UNICODE["high heeled shoes"] = ["U+4141"]
UNICODE_TO_BLISS["U+4141"] = ["high heeled shoes"]
BLISS_TO_UNICODE["high heels"] = ["U+4141"]
UNICODE_TO_BLISS["U+4141"].append("high heels")
BLISS_TO_UNICODE["high heeled shoes,high heels"] = ["U+4141"]
UNICODE_TO_BLISS["U+4141"].append("high heeled shoes,high heels")
BLISS_TO_UNICODE["treat"] = ["U+4142"]
UNICODE_TO_BLISS["U+4142"] = ["treat"]
BLISS_TO_UNICODE["care for"] = ["U+4142"]
UNICODE_TO_BLISS["U+4142"].append("care for")
BLISS_TO_UNICODE["treat,care for"] = ["U+4142"]
UNICODE_TO_BLISS["U+4142"].append("treat,care for")
BLISS_TO_UNICODE["circus"] = ["U+4143"]
UNICODE_TO_BLISS["U+4143"] = ["circus"]
BLISS_TO_UNICODE["showplace"] = ["U+4144"]
UNICODE_TO_BLISS["U+4144"] = ["showplace"]
BLISS_TO_UNICODE["working from home"] = ["U+4145"]
UNICODE_TO_BLISS["U+4145"] = ["working from home"]
BLISS_TO_UNICODE["our"] = ["U+4146"]
UNICODE_TO_BLISS["U+4146"] = ["our"]
BLISS_TO_UNICODE["ours"] = ["U+4146"]
UNICODE_TO_BLISS["U+4146"].append("ours")
BLISS_TO_UNICODE["our,ours"] = ["U+4146"]
UNICODE_TO_BLISS["U+4146"].append("our,ours")
BLISS_TO_UNICODE["respiratory illness"] = ["U+4147"]
UNICODE_TO_BLISS["U+4147"] = ["respiratory illness"]
BLISS_TO_UNICODE["breathe"] = ["U+4148"]
UNICODE_TO_BLISS["U+4148"] = ["breathe"]
BLISS_TO_UNICODE["sacrament of anointment of sick"] = ["U+4149"]
UNICODE_TO_BLISS["U+4149"] = ["sacrament of anointment of sick"]
BLISS_TO_UNICODE["kiddush"] = ["U+414a"]
UNICODE_TO_BLISS["U+414a"] = ["kiddush"]
BLISS_TO_UNICODE["blessing over wine"] = ["U+414a"]
UNICODE_TO_BLISS["U+414a"].append("blessing over wine")
BLISS_TO_UNICODE["kiddush,blessing over wine"] = ["U+414a"]
UNICODE_TO_BLISS["U+414a"].append("kiddush,blessing over wine")
BLISS_TO_UNICODE["resident"] = ["U+414b"]
UNICODE_TO_BLISS["U+414b"] = ["resident"]
BLISS_TO_UNICODE["swinging"] = ["U+325c"]
UNICODE_TO_BLISS["U+325c"].append("swinging")
BLISS_TO_UNICODE["swing,swinging"] = ["U+325c"]
UNICODE_TO_BLISS["U+325c"].append("swing,swinging")
BLISS_TO_UNICODE["twoheaded curved arrow suggests swinging motion"] = ["U+414c"]
UNICODE_TO_BLISS["U+414c"] = ["twoheaded curved arrow suggests swinging motion"]
BLISS_TO_UNICODE["transvestite"] = ["U+414d"]
UNICODE_TO_BLISS["U+414d"] = ["transvestite"]
BLISS_TO_UNICODE["to dress"] = ["U+414e"]
UNICODE_TO_BLISS["U+414e"] = ["to dress"]
BLISS_TO_UNICODE["Viking"] = ["U+414f"]
UNICODE_TO_BLISS["U+414f"] = ["Viking"]
BLISS_TO_UNICODE["firefighter"] = ["U+4150"]
UNICODE_TO_BLISS["U+4150"] = ["firefighter"]
BLISS_TO_UNICODE["fireman"] = ["U+4150"]
UNICODE_TO_BLISS["U+4150"].append("fireman")
BLISS_TO_UNICODE["firefighter,fireman"] = ["U+4150"]
UNICODE_TO_BLISS["U+4150"].append("firefighter,fireman")
BLISS_TO_UNICODE["extinction"] = ["U+4151"]
UNICODE_TO_BLISS["U+4151"] = ["extinction"]
BLISS_TO_UNICODE["extinguishing"] = ["U+4152"]
UNICODE_TO_BLISS["U+4152"] = ["extinguishing"]
BLISS_TO_UNICODE["hitchrack"] = ["U+4153"]
UNICODE_TO_BLISS["U+4153"] = ["hitchrack"]
BLISS_TO_UNICODE["hitching bar"] = ["U+4153"]
UNICODE_TO_BLISS["U+4153"].append("hitching bar")
BLISS_TO_UNICODE["hitchrack,hitching bar"] = ["U+4153"]
UNICODE_TO_BLISS["U+4153"].append("hitchrack,hitching bar")
BLISS_TO_UNICODE["millepede"] = ["U+4154"]
UNICODE_TO_BLISS["U+4154"] = ["millepede"]
BLISS_TO_UNICODE["frequent"] = ["U+3d07"]
UNICODE_TO_BLISS["U+3d07"].append("frequent")
BLISS_TO_UNICODE["frequently"] = ["U+3d07"]
UNICODE_TO_BLISS["U+3d07"].append("frequently")
BLISS_TO_UNICODE["often,frequent,frequently"] = ["U+3d07"]
UNICODE_TO_BLISS["U+3d07"].append("often,frequent,frequently")
BLISS_TO_UNICODE["magician"] = ["U+4155"]
UNICODE_TO_BLISS["U+4155"] = ["magician"]
BLISS_TO_UNICODE["poultry"] = ["U+3a13"]
UNICODE_TO_BLISS["U+3a13"].append("poultry")
BLISS_TO_UNICODE["sea cucumber"] = ["U+4156"]
UNICODE_TO_BLISS["U+4156"] = ["sea cucumber"]
BLISS_TO_UNICODE["oval shape"] = ["U+4157"]
UNICODE_TO_BLISS["U+4157"] = ["oval shape"]
BLISS_TO_UNICODE["shalom"] = ["U+4158"]
UNICODE_TO_BLISS["U+4158"] = ["shalom"]
BLISS_TO_UNICODE["well"].append("U+32db")
UNICODE_TO_BLISS["U+32db"].append("well")
BLISS_TO_UNICODE["fine"].append("U+32db")
UNICODE_TO_BLISS["U+32db"].append("fine")
BLISS_TO_UNICODE["ok"].append("U+32db")
UNICODE_TO_BLISS["U+32db"].append("ok")
BLISS_TO_UNICODE["okay"].append("U+32db")
UNICODE_TO_BLISS["U+32db"].append("okay")
BLISS_TO_UNICODE["all right"].append("U+32db")
UNICODE_TO_BLISS["U+32db"].append("all right")
BLISS_TO_UNICODE["good,well,fine,ok,okay,all right"] = ["U+32db"]
UNICODE_TO_BLISS["U+32db"].append("good,well,fine,ok,okay,all right")
BLISS_TO_UNICODE["goodness"] = ["U+4159"]
UNICODE_TO_BLISS["U+4159"] = ["goodness"]
BLISS_TO_UNICODE["healthy"] = ["U+415a"]
UNICODE_TO_BLISS["U+415a"] = ["healthy"]
BLISS_TO_UNICODE["well"].append("U+415a")
UNICODE_TO_BLISS["U+415a"].append("well")
BLISS_TO_UNICODE["healthy,well"] = ["U+415a"]
UNICODE_TO_BLISS["U+415a"].append("healthy,well")
BLISS_TO_UNICODE["water well"] = ["U+3c26"]
UNICODE_TO_BLISS["U+3c26"].append("water well")
BLISS_TO_UNICODE["well,water well"] = ["U+3c26"]
UNICODE_TO_BLISS["U+3c26"].append("well,water well")
BLISS_TO_UNICODE["coarse slang"] = ["U+415b"]
UNICODE_TO_BLISS["U+415b"] = ["coarse slang"]
BLISS_TO_UNICODE["these"] = ["U+415c"]
UNICODE_TO_BLISS["U+415c"] = ["these"]
BLISS_TO_UNICODE["polder"] = ["U+415d"]
UNICODE_TO_BLISS["U+415d"] = ["polder"]
BLISS_TO_UNICODE["disagree"] = ["U+415e"]
UNICODE_TO_BLISS["U+415e"] = ["disagree"]
BLISS_TO_UNICODE["discord"].append("U+415e")
UNICODE_TO_BLISS["U+415e"].append("discord")
BLISS_TO_UNICODE["disaccord"] = ["U+415e"]
UNICODE_TO_BLISS["U+415e"].append("disaccord")
BLISS_TO_UNICODE["disagree,discord,disaccord"] = ["U+415e"]
UNICODE_TO_BLISS["U+415e"].append("disagree,discord,disaccord")
BLISS_TO_UNICODE["football team"] = ["U+415f"]
UNICODE_TO_BLISS["U+415f"] = ["football team"]
BLISS_TO_UNICODE["Sunday"] = ["U+4160"]
UNICODE_TO_BLISS["U+4160"] = ["Sunday"]
BLISS_TO_UNICODE["distant"] = ["U+350a"]
UNICODE_TO_BLISS["U+350a"].append("distant")
BLISS_TO_UNICODE["far,distant"] = ["U+350a"]
UNICODE_TO_BLISS["U+350a"].append("far,distant")
BLISS_TO_UNICODE["religious gathering"] = ["U+4162"]
UNICODE_TO_BLISS["U+4162"] = ["religious gathering"]
BLISS_TO_UNICODE["trot"] = ["U+4163"]
UNICODE_TO_BLISS["U+4163"] = ["trot"]
BLISS_TO_UNICODE["disappearance"] = ["U+4164"]
UNICODE_TO_BLISS["U+4164"] = ["disappearance"]
BLISS_TO_UNICODE["ending"] = ["U+4165"]
UNICODE_TO_BLISS["U+4165"] = ["ending"]
BLISS_TO_UNICODE["propeller"] = ["U+4166"]
UNICODE_TO_BLISS["U+4166"] = ["propeller"]
BLISS_TO_UNICODE["rotor"] = ["U+4166"]
UNICODE_TO_BLISS["U+4166"].append("rotor")
BLISS_TO_UNICODE["propeller,rotor"] = ["U+4166"]
UNICODE_TO_BLISS["U+4166"].append("propeller,rotor")
BLISS_TO_UNICODE["telephone"].append("U+3cc3")
UNICODE_TO_BLISS["U+3cc3"].append("telephone")
BLISS_TO_UNICODE["ring"].append("U+3cc3")
UNICODE_TO_BLISS["U+3cc3"].append("ring")
BLISS_TO_UNICODE["call,telephone,ring"] = ["U+3cc3"]
UNICODE_TO_BLISS["U+3cc3"].append("call,telephone,ring")
BLISS_TO_UNICODE["clown"] = ["U+4167"]
UNICODE_TO_BLISS["U+4167"] = ["clown"]
BLISS_TO_UNICODE["protestantism"] = ["U+4168"]
UNICODE_TO_BLISS["U+4168"] = ["protestantism"]
BLISS_TO_UNICODE["to find"] = ["U+4169"]
UNICODE_TO_BLISS["U+4169"] = ["to find"]
BLISS_TO_UNICODE["barn"] = ["U+416a"]
UNICODE_TO_BLISS["U+416a"] = ["barn"]
BLISS_TO_UNICODE["stable"] = ["U+416a"]
UNICODE_TO_BLISS["U+416a"].append("stable")
BLISS_TO_UNICODE["shed"] = ["U+416a"]
UNICODE_TO_BLISS["U+416a"].append("shed")
BLISS_TO_UNICODE["barn,stable,shed"] = ["U+416a"]
UNICODE_TO_BLISS["U+416a"].append("barn,stable,shed")
BLISS_TO_UNICODE["chirp"] = ["U+416b"]
UNICODE_TO_BLISS["U+416b"] = ["chirp"]
BLISS_TO_UNICODE["twitter"] = ["U+416b"]
UNICODE_TO_BLISS["U+416b"].append("twitter")
BLISS_TO_UNICODE["chirp,twitter"] = ["U+416b"]
UNICODE_TO_BLISS["U+416b"].append("chirp,twitter")
BLISS_TO_UNICODE["library"] = ["U+416c"]
UNICODE_TO_BLISS["U+416c"] = ["library"]
BLISS_TO_UNICODE["next year"] = ["U+416d"]
UNICODE_TO_BLISS["U+416d"] = ["next year"]
BLISS_TO_UNICODE["overlay"] = ["U+416e"]
UNICODE_TO_BLISS["U+416e"] = ["overlay"]
BLISS_TO_UNICODE["broad"] = ["U+34db"]
UNICODE_TO_BLISS["U+34db"].append("broad")
BLISS_TO_UNICODE["wide,broad"] = ["U+34db"]
UNICODE_TO_BLISS["U+34db"].append("wide,broad")
BLISS_TO_UNICODE["cockerel"] = ["U+416f"]
UNICODE_TO_BLISS["U+416f"] = ["cockerel"]
BLISS_TO_UNICODE["tadpole"] = ["U+4170"]
UNICODE_TO_BLISS["U+4170"] = ["tadpole"]
BLISS_TO_UNICODE["fable"] = ["U+4171"]
UNICODE_TO_BLISS["U+4171"] = ["fable"]
BLISS_TO_UNICODE["allegory"] = ["U+4171"]
UNICODE_TO_BLISS["U+4171"].append("allegory")
BLISS_TO_UNICODE["parable"] = ["U+4171"]
UNICODE_TO_BLISS["U+4171"].append("parable")
BLISS_TO_UNICODE["fable,allegory,parable"] = ["U+4171"]
UNICODE_TO_BLISS["U+4171"].append("fable,allegory,parable")
BLISS_TO_UNICODE["orienteer"] = ["U+4172"]
UNICODE_TO_BLISS["U+4172"] = ["orienteer"]
BLISS_TO_UNICODE["read map"] = ["U+4172"]
UNICODE_TO_BLISS["U+4172"].append("read map")
BLISS_TO_UNICODE["orienteer,read map"] = ["U+4172"]
UNICODE_TO_BLISS["U+4172"].append("orienteer,read map")
BLISS_TO_UNICODE["map reading"] = ["U+4173"]
UNICODE_TO_BLISS["U+4173"] = ["map reading"]
BLISS_TO_UNICODE["magazine"] = ["U+4174"]
UNICODE_TO_BLISS["U+4174"] = ["magazine"]
BLISS_TO_UNICODE["journal"] = ["U+4174"]
UNICODE_TO_BLISS["U+4174"].append("journal")
BLISS_TO_UNICODE["magazine,journal"] = ["U+4174"]
UNICODE_TO_BLISS["U+4174"].append("magazine,journal")
BLISS_TO_UNICODE["narrowness"].append("U+3c4f")
UNICODE_TO_BLISS["U+3c4f"].append("narrowness")
BLISS_TO_UNICODE["thinness,narrowness"] = ["U+3c4f"]
UNICODE_TO_BLISS["U+3c4f"].append("thinness,narrowness")
BLISS_TO_UNICODE["two pointers"] = ["U+4175"]
UNICODE_TO_BLISS["U+4175"] = ["two pointers"]
BLISS_TO_UNICODE["refuge"] = ["U+376d"]
UNICODE_TO_BLISS["U+376d"].append("refuge")
BLISS_TO_UNICODE["shelter,refuge"] = ["U+376d"]
UNICODE_TO_BLISS["U+376d"].append("shelter,refuge")
BLISS_TO_UNICODE["computer game"] = ["U+4176"]
UNICODE_TO_BLISS["U+4176"] = ["computer game"]
BLISS_TO_UNICODE["liberty"] = ["U+33a4"]
UNICODE_TO_BLISS["U+33a4"].append("liberty")
BLISS_TO_UNICODE["freedom,liberty"] = ["U+33a4"]
UNICODE_TO_BLISS["U+33a4"].append("freedom,liberty")
BLISS_TO_UNICODE["beige"] = ["U+4177"]
UNICODE_TO_BLISS["U+4177"] = ["beige"]
BLISS_TO_UNICODE["cranberry"] = ["U+4178"]
UNICODE_TO_BLISS["U+4178"] = ["cranberry"]
BLISS_TO_UNICODE["tongue"] = ["U+4179"]
UNICODE_TO_BLISS["U+4179"] = ["tongue"]
BLISS_TO_UNICODE["seminal vesicle"] = ["U+417a"]
UNICODE_TO_BLISS["U+417a"] = ["seminal vesicle"]
BLISS_TO_UNICODE["semen"] = ["U+417b"]
UNICODE_TO_BLISS["U+417b"] = ["semen"]
BLISS_TO_UNICODE["electric piano"] = ["U+417c"]
UNICODE_TO_BLISS["U+417c"] = ["electric piano"]
BLISS_TO_UNICODE["snowplow"] = ["U+417d"]
UNICODE_TO_BLISS["U+417d"] = ["snowplow"]
BLISS_TO_UNICODE["snowplough"] = ["U+417d"]
UNICODE_TO_BLISS["U+417d"].append("snowplough")
BLISS_TO_UNICODE["snowplow,snowplough"] = ["U+417d"]
UNICODE_TO_BLISS["U+417d"].append("snowplow,snowplough")
BLISS_TO_UNICODE["museum"] = ["U+417e"]
UNICODE_TO_BLISS["U+417e"] = ["museum"]
BLISS_TO_UNICODE["pepper sauce"] = ["U+417f"]
UNICODE_TO_BLISS["U+417f"] = ["pepper sauce"]
BLISS_TO_UNICODE["drumstick"] = ["U+4180"]
UNICODE_TO_BLISS["U+4180"] = ["drumstick"]
BLISS_TO_UNICODE["showjumping"] = ["U+4181"]
UNICODE_TO_BLISS["U+4181"] = ["showjumping"]
BLISS_TO_UNICODE["cricket"] = ["U+4182"]
UNICODE_TO_BLISS["U+4182"] = ["cricket"]
BLISS_TO_UNICODE["sacrament of communion"] = ["U+4183"]
UNICODE_TO_BLISS["U+4183"] = ["sacrament of communion"]
BLISS_TO_UNICODE["triangular"] = ["U+4184"]
UNICODE_TO_BLISS["U+4184"] = ["triangular"]
BLISS_TO_UNICODE["Holy Family"] = ["U+4185"]
UNICODE_TO_BLISS["U+4185"] = ["Holy Family"]
BLISS_TO_UNICODE["palmtop"] = ["U+4186"]
UNICODE_TO_BLISS["U+4186"] = ["palmtop"]
BLISS_TO_UNICODE["PDA"] = ["U+4186"]
UNICODE_TO_BLISS["U+4186"].append("PDA")
BLISS_TO_UNICODE["palmtop,PDA"] = ["U+4186"]
UNICODE_TO_BLISS["U+4186"].append("palmtop,PDA")
BLISS_TO_UNICODE["TV studio"] = ["U+4187"]
UNICODE_TO_BLISS["U+4187"] = ["TV studio"]
BLISS_TO_UNICODE["radio studio"] = ["U+4187"]
UNICODE_TO_BLISS["U+4187"].append("radio studio")
BLISS_TO_UNICODE["TV studio,radio studio"] = ["U+4187"]
UNICODE_TO_BLISS["U+4187"].append("TV studio,radio studio")
BLISS_TO_UNICODE["abseiling"] = ["U+4188"]
UNICODE_TO_BLISS["U+4188"] = ["abseiling"]
BLISS_TO_UNICODE["rappelling"] = ["U+4188"]
UNICODE_TO_BLISS["U+4188"].append("rappelling")
BLISS_TO_UNICODE["abseiling,rappelling"] = ["U+4188"]
UNICODE_TO_BLISS["U+4188"].append("abseiling,rappelling")
BLISS_TO_UNICODE["to go down"] = ["U+4189"]
UNICODE_TO_BLISS["U+4189"] = ["to go down"]
BLISS_TO_UNICODE["restrict"] = ["U+362d"]
UNICODE_TO_BLISS["U+362d"].append("restrict")
BLISS_TO_UNICODE["restrain"] = ["U+362d"]
UNICODE_TO_BLISS["U+362d"].append("restrain")
BLISS_TO_UNICODE["confine"] = ["U+362d"]
UNICODE_TO_BLISS["U+362d"].append("confine")
BLISS_TO_UNICODE["limit,restrict,restrain,confine"] = ["U+362d"]
UNICODE_TO_BLISS["U+362d"].append("limit,restrict,restrain,confine")
BLISS_TO_UNICODE["cello"] = ["U+418a"]
UNICODE_TO_BLISS["U+418a"] = ["cello"]
BLISS_TO_UNICODE["bit"] = ["U+33cb"]
UNICODE_TO_BLISS["U+33cb"].append("bit")
BLISS_TO_UNICODE["piece"].append("U+33cb")
UNICODE_TO_BLISS["U+33cb"].append("piece")
BLISS_TO_UNICODE["portion"] = ["U+33cb"]
UNICODE_TO_BLISS["U+33cb"].append("portion")
BLISS_TO_UNICODE["part of"].append("U+33cb")
UNICODE_TO_BLISS["U+33cb"].append("part of")
BLISS_TO_UNICODE["part,bit,piece,portion,part of"] = ["U+33cb"]
UNICODE_TO_BLISS["U+33cb"].append("part,bit,piece,portion,part of")
BLISS_TO_UNICODE["Jerusalem Day"] = ["U+418c"]
UNICODE_TO_BLISS["U+418c"] = ["Jerusalem Day"]
BLISS_TO_UNICODE["utensils"] = ["U+3a33"]
UNICODE_TO_BLISS["U+3a33"].append("utensils")
BLISS_TO_UNICODE["kitchen tool,utensils"] = ["U+3a33"]
UNICODE_TO_BLISS["U+3a33"].append("kitchen tool,utensils")
BLISS_TO_UNICODE["education"] = ["U+418d"]
UNICODE_TO_BLISS["U+418d"] = ["education"]
BLISS_TO_UNICODE["didactics"] = ["U+418d"]
UNICODE_TO_BLISS["U+418d"].append("didactics")
BLISS_TO_UNICODE["pedagogy"] = ["U+418d"]
UNICODE_TO_BLISS["U+418d"].append("pedagogy")
BLISS_TO_UNICODE["education,didactics,pedagogy"] = ["U+418d"]
UNICODE_TO_BLISS["U+418d"].append("education,didactics,pedagogy")
BLISS_TO_UNICODE["balcony"] = ["U+418e"]
UNICODE_TO_BLISS["U+418e"] = ["balcony"]
BLISS_TO_UNICODE["porch"] = ["U+418e"]
UNICODE_TO_BLISS["U+418e"].append("porch")
BLISS_TO_UNICODE["veranda"] = ["U+418e"]
UNICODE_TO_BLISS["U+418e"].append("veranda")
BLISS_TO_UNICODE["balcony,porch,veranda"] = ["U+418e"]
UNICODE_TO_BLISS["U+418e"].append("balcony,porch,veranda")
BLISS_TO_UNICODE["mite"] = ["U+418f"]
UNICODE_TO_BLISS["U+418f"] = ["mite"]
BLISS_TO_UNICODE["tick"] = ["U+418f"]
UNICODE_TO_BLISS["U+418f"].append("tick")
BLISS_TO_UNICODE["mite,tick"] = ["U+418f"]
UNICODE_TO_BLISS["U+418f"].append("mite,tick")
BLISS_TO_UNICODE["slaughterhouse"] = ["U+4190"]
UNICODE_TO_BLISS["U+4190"] = ["slaughterhouse"]
BLISS_TO_UNICODE["abattoir"] = ["U+4190"]
UNICODE_TO_BLISS["U+4190"].append("abattoir")
BLISS_TO_UNICODE["slaughterhouse,abattoir"] = ["U+4190"]
UNICODE_TO_BLISS["U+4190"].append("slaughterhouse,abattoir")
BLISS_TO_UNICODE["slaughter"] = ["U+4191"]
UNICODE_TO_BLISS["U+4191"] = ["slaughter"]
BLISS_TO_UNICODE["fencing"] = ["U+4192"]
UNICODE_TO_BLISS["U+4192"] = ["fencing"]
BLISS_TO_UNICODE["to fight"] = ["U+4193"]
UNICODE_TO_BLISS["U+4193"] = ["to fight"]
BLISS_TO_UNICODE["oil power"] = ["U+4194"]
UNICODE_TO_BLISS["U+4194"] = ["oil power"]
BLISS_TO_UNICODE["oil energy"] = ["U+4194"]
UNICODE_TO_BLISS["U+4194"].append("oil energy")
BLISS_TO_UNICODE["oil power,oil energy"] = ["U+4194"]
UNICODE_TO_BLISS["U+4194"].append("oil power,oil energy")
BLISS_TO_UNICODE["water bucket"] = ["U+4195"]
UNICODE_TO_BLISS["U+4195"] = ["water bucket"]
BLISS_TO_UNICODE["chemist"] = ["U+4196"]
UNICODE_TO_BLISS["U+4196"] = ["chemist"]
BLISS_TO_UNICODE["chemistry"] = ["U+4197"]
UNICODE_TO_BLISS["U+4197"] = ["chemistry"]
BLISS_TO_UNICODE["troll"] = ["U+4198"]
UNICODE_TO_BLISS["U+4198"] = ["troll"]
BLISS_TO_UNICODE["thing ind."] = ["U+4199"]
UNICODE_TO_BLISS["U+4199"] = ["thing ind."]
BLISS_TO_UNICODE["pay channel"] = ["U+419a"]
UNICODE_TO_BLISS["U+419a"] = ["pay channel"]
BLISS_TO_UNICODE["channel"] = ["U+419b"]
UNICODE_TO_BLISS["U+419b"] = ["channel"]
BLISS_TO_UNICODE["ecstatic"] = ["U+419c"]
UNICODE_TO_BLISS["U+419c"] = ["ecstatic"]
BLISS_TO_UNICODE["ecstasy"] = ["U+419d"]
UNICODE_TO_BLISS["U+419d"] = ["ecstasy"]
BLISS_TO_UNICODE["stay"] = ["U+419e"]
UNICODE_TO_BLISS["U+419e"] = ["stay"]
BLISS_TO_UNICODE["remain"] = ["U+419e"]
UNICODE_TO_BLISS["U+419e"].append("remain")
BLISS_TO_UNICODE["stay,remain"] = ["U+419e"]
UNICODE_TO_BLISS["U+419e"].append("stay,remain")
BLISS_TO_UNICODE["celebration of life"] = ["U+419f"]
UNICODE_TO_BLISS["U+419f"] = ["celebration of life"]
BLISS_TO_UNICODE["life)"] = ["U+41a1"]
UNICODE_TO_BLISS["U+41a1"] = ["life)"]
BLISS_TO_UNICODE["atheism"] = ["U+41a2"]
UNICODE_TO_BLISS["U+41a2"] = ["atheism"]
BLISS_TO_UNICODE["pardon"].append("U+32c7")
UNICODE_TO_BLISS["U+32c7"].append("pardon")
BLISS_TO_UNICODE["forgive,pardon"] = ["U+32c7"]
UNICODE_TO_BLISS["U+32c7"].append("forgive,pardon")
BLISS_TO_UNICODE["what did you say"] = ["U+3b88"]
UNICODE_TO_BLISS["U+3b88"].append("what did you say")
BLISS_TO_UNICODE["pardon,what did you say"] = ["U+3b88"]
UNICODE_TO_BLISS["U+3b88"].append("pardon,what did you say")
BLISS_TO_UNICODE["limited"] = ["U+41a4"]
UNICODE_TO_BLISS["U+41a4"] = ["limited"]
BLISS_TO_UNICODE["restricted"] = ["U+41a4"]
UNICODE_TO_BLISS["U+41a4"].append("restricted")
BLISS_TO_UNICODE["confined"] = ["U+41a4"]
UNICODE_TO_BLISS["U+41a4"].append("confined")
BLISS_TO_UNICODE["limited,restricted,confined"] = ["U+41a4"]
UNICODE_TO_BLISS["U+41a4"].append("limited,restricted,confined")
BLISS_TO_UNICODE["resist"] = ["U+3bb9"]
UNICODE_TO_BLISS["U+3bb9"].append("resist")
BLISS_TO_UNICODE["protest,resist"] = ["U+3bb9"]
UNICODE_TO_BLISS["U+3bb9"].append("protest,resist")
BLISS_TO_UNICODE["resistance"] = ["U+3bb9"]
UNICODE_TO_BLISS["U+3bb9"].append("resistance")
BLISS_TO_UNICODE["protest,resistance"] = ["U+3bb9"]
UNICODE_TO_BLISS["U+3bb9"].append("protest,resistance")
BLISS_TO_UNICODE["whose"] = ["U+41a5"]
UNICODE_TO_BLISS["U+41a5"] = ["whose"]
BLISS_TO_UNICODE["pictograph of swan neck and head"] = ["U+41a6"]
UNICODE_TO_BLISS["U+41a6"] = ["pictograph of swan neck and head"]
BLISS_TO_UNICODE["stomach illness"] = ["U+41a7"]
UNICODE_TO_BLISS["U+41a7"] = ["stomach illness"]
BLISS_TO_UNICODE["teaspoon"] = ["U+41a8"]
UNICODE_TO_BLISS["U+41a8"] = ["teaspoon"]
BLISS_TO_UNICODE["instruction"] = ["U+41a9"]
UNICODE_TO_BLISS["U+41a9"] = ["instruction"]
BLISS_TO_UNICODE["teaching"] = ["U+41a9"]
UNICODE_TO_BLISS["U+41a9"].append("teaching")
BLISS_TO_UNICODE["instruction,teaching"] = ["U+41a9"]
UNICODE_TO_BLISS["U+41a9"].append("instruction,teaching")
BLISS_TO_UNICODE["sway"] = ["U+325c"]
UNICODE_TO_BLISS["U+325c"].append("sway")
BLISS_TO_UNICODE["rock"].append("U+325c")
UNICODE_TO_BLISS["U+325c"].append("rock")
BLISS_TO_UNICODE["swing,sway,rock"] = ["U+325c"]
UNICODE_TO_BLISS["U+325c"].append("swing,sway,rock")
BLISS_TO_UNICODE["rescue"] = ["U+41aa"]
UNICODE_TO_BLISS["U+41aa"] = ["rescue"]
BLISS_TO_UNICODE["sex organs"] = ["U+33ec"]
UNICODE_TO_BLISS["U+33ec"].append("sex organs")
BLISS_TO_UNICODE["genitals,sex organs"] = ["U+33ec"]
UNICODE_TO_BLISS["U+33ec"].append("genitals,sex organs")
BLISS_TO_UNICODE["tandem bicycle"] = ["U+41ab"]
UNICODE_TO_BLISS["U+41ab"] = ["tandem bicycle"]
BLISS_TO_UNICODE["raw"] = ["U+41ac"]
UNICODE_TO_BLISS["U+41ac"] = ["raw"]
BLISS_TO_UNICODE["uncooked"] = ["U+41ac"]
UNICODE_TO_BLISS["U+41ac"].append("uncooked")
BLISS_TO_UNICODE["raw,uncooked"] = ["U+41ac"]
UNICODE_TO_BLISS["U+41ac"].append("raw,uncooked")
BLISS_TO_UNICODE["farmhouse"] = ["U+41ad"]
UNICODE_TO_BLISS["U+41ad"] = ["farmhouse"]
BLISS_TO_UNICODE["chocolate drink"] = ["U+41ae"]
UNICODE_TO_BLISS["U+41ae"] = ["chocolate drink"]
BLISS_TO_UNICODE["bat mitzvah"] = ["U+41af"]
UNICODE_TO_BLISS["U+41af"] = ["bat mitzvah"]
BLISS_TO_UNICODE["cactus"] = ["U+41b0"]
UNICODE_TO_BLISS["U+41b0"] = ["cactus"]
BLISS_TO_UNICODE["desktop computer"] = ["U+41b1"]
UNICODE_TO_BLISS["U+41b1"] = ["desktop computer"]
BLISS_TO_UNICODE["table top"] = ["U+41b2"]
UNICODE_TO_BLISS["U+41b2"] = ["table top"]
BLISS_TO_UNICODE["orienteering"] = ["U+41b3"]
UNICODE_TO_BLISS["U+41b3"] = ["orienteering"]
BLISS_TO_UNICODE["to catch"] = ["U+41b4"]
UNICODE_TO_BLISS["U+41b4"] = ["to catch"]
BLISS_TO_UNICODE["signal strength meter"] = ["U+41b5"]
UNICODE_TO_BLISS["U+41b5"] = ["signal strength meter"]
BLISS_TO_UNICODE["barometer"] = ["U+41b6"]
UNICODE_TO_BLISS["U+41b6"] = ["barometer"]
BLISS_TO_UNICODE["manometer"] = ["U+41b6"]
UNICODE_TO_BLISS["U+41b6"].append("manometer")
BLISS_TO_UNICODE["barometer,manometer"] = ["U+41b6"]
UNICODE_TO_BLISS["U+41b6"].append("barometer,manometer")
BLISS_TO_UNICODE["never"] = ["U+41b7"]
UNICODE_TO_BLISS["U+41b7"] = ["never"]
BLISS_TO_UNICODE["anthropology"] = ["U+41b8"]
UNICODE_TO_BLISS["U+41b8"] = ["anthropology"]
BLISS_TO_UNICODE["remote control"] = ["U+41b9"]
UNICODE_TO_BLISS["U+41b9"] = ["remote control"]
BLISS_TO_UNICODE["cardboard"] = ["U+41ba"]
UNICODE_TO_BLISS["U+41ba"] = ["cardboard"]
BLISS_TO_UNICODE["paperboard"] = ["U+41ba"]
UNICODE_TO_BLISS["U+41ba"].append("paperboard")
BLISS_TO_UNICODE["cardboard,paperboard"] = ["U+41ba"]
UNICODE_TO_BLISS["U+41ba"].append("cardboard,paperboard")
BLISS_TO_UNICODE["piercing"] = ["U+41bb"]
UNICODE_TO_BLISS["U+41bb"] = ["piercing"]
BLISS_TO_UNICODE["male genitals"] = ["U+41bc"]
UNICODE_TO_BLISS["U+41bc"] = ["male genitals"]
BLISS_TO_UNICODE["pictograph of penis"] = ["U+41bd"]
UNICODE_TO_BLISS["U+41bd"] = ["pictograph of penis"]
BLISS_TO_UNICODE["anarthria"].append("U+39f7")
UNICODE_TO_BLISS["U+39f7"].append("anarthria")
BLISS_TO_UNICODE["no speech,anarthria"] = ["U+39f7"]
UNICODE_TO_BLISS["U+39f7"].append("no speech,anarthria")
BLISS_TO_UNICODE["skytrain"] = ["U+41be"]
UNICODE_TO_BLISS["U+41be"] = ["skytrain"]
BLISS_TO_UNICODE["monorail"] = ["U+41be"]
UNICODE_TO_BLISS["U+41be"].append("monorail")
BLISS_TO_UNICODE["skytrain,monorail"] = ["U+41be"]
UNICODE_TO_BLISS["U+41be"].append("skytrain,monorail")
BLISS_TO_UNICODE["bronze age"] = ["U+41bf"]
UNICODE_TO_BLISS["U+41bf"] = ["bronze age"]
BLISS_TO_UNICODE["past time"] = ["U+41c0"]
UNICODE_TO_BLISS["U+41c0"] = ["past time"]
BLISS_TO_UNICODE["bronze"] = ["U+41c1"]
UNICODE_TO_BLISS["U+41c1"] = ["bronze"]
BLISS_TO_UNICODE["serene"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("serene")
BLISS_TO_UNICODE["peaceful,serene,calm"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("peaceful,serene,calm")
BLISS_TO_UNICODE["advise"] = ["U+41c2"]
UNICODE_TO_BLISS["U+41c2"] = ["advise"]
BLISS_TO_UNICODE["counsel"] = ["U+41c2"]
UNICODE_TO_BLISS["U+41c2"].append("counsel")
BLISS_TO_UNICODE["recommend"] = ["U+41c2"]
UNICODE_TO_BLISS["U+41c2"].append("recommend")
BLISS_TO_UNICODE["advise,counsel,recommend"] = ["U+41c2"]
UNICODE_TO_BLISS["U+41c2"].append("advise,counsel,recommend")
BLISS_TO_UNICODE["advice"] = ["U+41c3"]
UNICODE_TO_BLISS["U+41c3"] = ["advice"]
BLISS_TO_UNICODE["kind"].append("U+3ee8")
UNICODE_TO_BLISS["U+3ee8"].append("kind")
BLISS_TO_UNICODE["sort"] = ["U+3ee8"]
UNICODE_TO_BLISS["U+3ee8"].append("sort")
BLISS_TO_UNICODE["type,kind,sort"] = ["U+3ee8"]
UNICODE_TO_BLISS["U+3ee8"].append("type,kind,sort")
BLISS_TO_UNICODE["supporters"] = ["U+41c4"]
UNICODE_TO_BLISS["U+41c4"] = ["supporters"]
BLISS_TO_UNICODE["cheering section"] = ["U+41c4"]
UNICODE_TO_BLISS["U+41c4"].append("cheering section")
BLISS_TO_UNICODE["supporters,cheering section"] = ["U+41c4"]
UNICODE_TO_BLISS["U+41c4"].append("supporters,cheering section")
BLISS_TO_UNICODE["warn"] = ["U+41c5"]
UNICODE_TO_BLISS["U+41c5"] = ["warn"]
BLISS_TO_UNICODE["warning"] = ["U+41c6"]
UNICODE_TO_BLISS["U+41c6"] = ["warning"]
BLISS_TO_UNICODE["commuter train"] = ["U+41c7"]
UNICODE_TO_BLISS["U+41c7"] = ["commuter train"]
BLISS_TO_UNICODE["bread crust"] = ["U+41c8"]
UNICODE_TO_BLISS["U+41c8"] = ["bread crust"]
BLISS_TO_UNICODE["dhoti"] = ["U+41c9"]
UNICODE_TO_BLISS["U+41c9"] = ["dhoti"]
BLISS_TO_UNICODE["lungi"] = ["U+41c9"]
UNICODE_TO_BLISS["U+41c9"].append("lungi")
BLISS_TO_UNICODE["dhoti,lungi"] = ["U+41c9"]
UNICODE_TO_BLISS["U+41c9"].append("dhoti,lungi")
BLISS_TO_UNICODE["herb flavouring"] = ["U+41ca"]
UNICODE_TO_BLISS["U+41ca"] = ["herb flavouring"]
BLISS_TO_UNICODE["drop anchor"] = ["U+41cb"]
UNICODE_TO_BLISS["U+41cb"] = ["drop anchor"]
BLISS_TO_UNICODE["anchor"] = ["U+41cc"]
UNICODE_TO_BLISS["U+41cc"] = ["anchor"]
BLISS_TO_UNICODE["one storey building"] = ["U+41cd"]
UNICODE_TO_BLISS["U+41cd"] = ["one storey building"]
BLISS_TO_UNICODE["bungalow"] = ["U+41cd"]
UNICODE_TO_BLISS["U+41cd"].append("bungalow")
BLISS_TO_UNICODE["one storey building,bungalow"] = ["U+41cd"]
UNICODE_TO_BLISS["U+41cd"].append("one storey building,bungalow")
BLISS_TO_UNICODE["Yom Kippur"] = ["U+41ce"]
UNICODE_TO_BLISS["U+41ce"] = ["Yom Kippur"]
BLISS_TO_UNICODE["pictograph of root"] = ["U+41cf"]
UNICODE_TO_BLISS["U+41cf"] = ["pictograph of root"]
BLISS_TO_UNICODE["social worker"] = ["U+41d0"]
UNICODE_TO_BLISS["U+41d0"] = ["social worker"]
BLISS_TO_UNICODE["honey"] = ["U+41d1"]
UNICODE_TO_BLISS["U+41d1"] = ["honey"]
BLISS_TO_UNICODE["reply"] = ["U+337a"]
UNICODE_TO_BLISS["U+337a"].append("reply")
BLISS_TO_UNICODE["answer,reply"] = ["U+337a"]
UNICODE_TO_BLISS["U+337a"].append("answer,reply")
BLISS_TO_UNICODE["Chronic Fatigue Syndrome"] = ["U+41d2"]
UNICODE_TO_BLISS["U+41d2"] = ["Chronic Fatigue Syndrome"]
BLISS_TO_UNICODE["briefcase"] = ["U+41d3"]
UNICODE_TO_BLISS["U+41d3"] = ["briefcase"]
BLISS_TO_UNICODE["twin sister"] = ["U+41d4"]
UNICODE_TO_BLISS["U+41d4"] = ["twin sister"]
BLISS_TO_UNICODE["president"] = ["U+41d5"]
UNICODE_TO_BLISS["U+41d5"] = ["president"]
BLISS_TO_UNICODE["chairman"] = ["U+41d6"]
UNICODE_TO_BLISS["U+41d6"] = ["chairman"]
BLISS_TO_UNICODE["go to sea"] = ["U+41d7"]
UNICODE_TO_BLISS["U+41d7"] = ["go to sea"]
BLISS_TO_UNICODE["boarding"] = ["U+41d8"]
UNICODE_TO_BLISS["U+41d8"] = ["boarding"]
BLISS_TO_UNICODE["embarkation"] = ["U+41d9"]
UNICODE_TO_BLISS["U+41d9"] = ["embarkation"]
BLISS_TO_UNICODE["buy"] = ["U+41da"]
UNICODE_TO_BLISS["U+41da"] = ["buy"]
BLISS_TO_UNICODE["purchase"] = ["U+41da"]
UNICODE_TO_BLISS["U+41da"].append("purchase")
BLISS_TO_UNICODE["buy,purchase"] = ["U+41da"]
UNICODE_TO_BLISS["U+41da"].append("buy,purchase")
BLISS_TO_UNICODE["farewell"] = ["U+378b"]
UNICODE_TO_BLISS["U+378b"].append("farewell")
BLISS_TO_UNICODE["goodbye,farewell"] = ["U+378b"]
UNICODE_TO_BLISS["U+378b"].append("goodbye,farewell")
BLISS_TO_UNICODE["deck"] = ["U+41db"]
UNICODE_TO_BLISS["U+41db"] = ["deck"]
BLISS_TO_UNICODE["hibernation"] = ["U+41dc"]
UNICODE_TO_BLISS["U+41dc"] = ["hibernation"]
BLISS_TO_UNICODE["siren of the woods"] = ["U+41dd"]
UNICODE_TO_BLISS["U+41dd"] = ["siren of the woods"]
BLISS_TO_UNICODE["staff"].append("U+3eac")
UNICODE_TO_BLISS["U+3eac"].append("staff")
BLISS_TO_UNICODE["crew,staff"] = ["U+3eac"]
UNICODE_TO_BLISS["U+3eac"].append("crew,staff")
BLISS_TO_UNICODE["better"] = ["U+41de"]
UNICODE_TO_BLISS["U+41de"] = ["better"]
BLISS_TO_UNICODE["missionary"] = ["U+41df"]
UNICODE_TO_BLISS["U+41df"] = ["missionary"]
BLISS_TO_UNICODE["French horn"] = ["U+41e0"]
UNICODE_TO_BLISS["U+41e0"] = ["French horn"]
BLISS_TO_UNICODE["bow and string"] = ["U+41e1"]
UNICODE_TO_BLISS["U+41e1"] = ["bow and string"]
BLISS_TO_UNICODE["viola"] = ["U+41e2"]
UNICODE_TO_BLISS["U+41e2"] = ["viola"]
BLISS_TO_UNICODE["sterilization"] = ["U+41e3"]
UNICODE_TO_BLISS["U+41e3"] = ["sterilization"]
BLISS_TO_UNICODE["weakness"] = ["U+41e4"]
UNICODE_TO_BLISS["U+41e4"] = ["weakness"]
BLISS_TO_UNICODE["unemployed"] = ["U+41e5"]
UNICODE_TO_BLISS["U+41e5"] = ["unemployed"]
BLISS_TO_UNICODE["caterpillar"] = ["U+41e6"]
UNICODE_TO_BLISS["U+41e6"] = ["caterpillar"]
BLISS_TO_UNICODE["sleepless"] = ["U+41e7"]
UNICODE_TO_BLISS["U+41e7"] = ["sleepless"]
BLISS_TO_UNICODE["India"] = ["U+41e8"]
UNICODE_TO_BLISS["U+41e8"] = ["India"]
BLISS_TO_UNICODE["bake"] = ["U+41e9"]
UNICODE_TO_BLISS["U+41e9"] = ["bake"]
BLISS_TO_UNICODE["cook"].append("U+41e9")
UNICODE_TO_BLISS["U+41e9"].append("cook")
BLISS_TO_UNICODE["roast"].append("U+41e9")
UNICODE_TO_BLISS["U+41e9"].append("roast")
BLISS_TO_UNICODE["bake,cook,roast"] = ["U+41e9"]
UNICODE_TO_BLISS["U+41e9"].append("bake,cook,roast")
BLISS_TO_UNICODE["navy"] = ["U+41ea"]
UNICODE_TO_BLISS["U+41ea"] = ["navy"]
BLISS_TO_UNICODE["gustation"] = ["U+32a1"]
UNICODE_TO_BLISS["U+32a1"].append("gustation")
BLISS_TO_UNICODE["sense of taste"] = ["U+32a1"]
UNICODE_TO_BLISS["U+32a1"].append("sense of taste")
BLISS_TO_UNICODE["taste,gustation,sense of taste"] = ["U+32a1"]
UNICODE_TO_BLISS["U+32a1"].append("taste,gustation,sense of taste")
BLISS_TO_UNICODE["Tammuz"] = ["U+41eb"]
UNICODE_TO_BLISS["U+41eb"] = ["Tammuz"]
BLISS_TO_UNICODE["kebab"] = ["U+41ec"]
UNICODE_TO_BLISS["U+41ec"] = ["kebab"]
BLISS_TO_UNICODE["NL)"] = ["U+41ec"]
UNICODE_TO_BLISS["U+41ec"].append("NL)")
BLISS_TO_UNICODE["diving equipment"] = ["U+41ed"]
UNICODE_TO_BLISS["U+41ed"] = ["diving equipment"]
BLISS_TO_UNICODE["diving gear"] = ["U+41ed"]
UNICODE_TO_BLISS["U+41ed"].append("diving gear")
BLISS_TO_UNICODE["diving equipment,diving gear"] = ["U+41ed"]
UNICODE_TO_BLISS["U+41ed"].append("diving equipment,diving gear")
BLISS_TO_UNICODE["body brace"] = ["U+41ee"]
UNICODE_TO_BLISS["U+41ee"] = ["body brace"]
BLISS_TO_UNICODE["corset"] = ["U+41ee"]
UNICODE_TO_BLISS["U+41ee"].append("corset")
BLISS_TO_UNICODE["body brace,corset"] = ["U+41ee"]
UNICODE_TO_BLISS["U+41ee"].append("body brace,corset")
BLISS_TO_UNICODE["signature"] = ["U+41ef"]
UNICODE_TO_BLISS["U+41ef"] = ["signature"]
BLISS_TO_UNICODE["school way"] = ["U+41f0"]
UNICODE_TO_BLISS["U+41f0"] = ["school way"]
BLISS_TO_UNICODE["loud"] = ["U+41f1"]
UNICODE_TO_BLISS["U+41f1"] = ["loud"]
BLISS_TO_UNICODE["noisy"] = ["U+41f1"]
UNICODE_TO_BLISS["U+41f1"].append("noisy")
BLISS_TO_UNICODE["loud,noisy"] = ["U+41f1"]
UNICODE_TO_BLISS["U+41f1"].append("loud,noisy")
BLISS_TO_UNICODE["noise"] = ["U+41f2"]
UNICODE_TO_BLISS["U+41f2"] = ["noise"]
BLISS_TO_UNICODE["naughty"] = ["U+41f3"]
UNICODE_TO_BLISS["U+41f3"] = ["naughty"]
BLISS_TO_UNICODE["not nice"] = ["U+41f3"]
UNICODE_TO_BLISS["U+41f3"].append("not nice")
BLISS_TO_UNICODE["naughty,not nice"] = ["U+41f3"]
UNICODE_TO_BLISS["U+41f3"].append("naughty,not nice")
BLISS_TO_UNICODE["hanger"].append("U+3939")
UNICODE_TO_BLISS["U+3939"].append("hanger")
BLISS_TO_UNICODE["hook,hanger"] = ["U+3939"]
UNICODE_TO_BLISS["U+3939"].append("hook,hanger")
BLISS_TO_UNICODE["Buddhism"] = ["U+41f4"]
UNICODE_TO_BLISS["U+41f4"] = ["Buddhism"]
BLISS_TO_UNICODE["dharma wheel"] = ["U+41f5"]
UNICODE_TO_BLISS["U+41f5"] = ["dharma wheel"]
BLISS_TO_UNICODE["computer peripheral"] = ["U+41f6"]
UNICODE_TO_BLISS["U+41f6"] = ["computer peripheral"]
BLISS_TO_UNICODE["historian"] = ["U+41f7"]
UNICODE_TO_BLISS["U+41f7"] = ["historian"]
BLISS_TO_UNICODE["boating"] = ["U+41f8"]
UNICODE_TO_BLISS["U+41f8"] = ["boating"]
BLISS_TO_UNICODE["spice box"] = ["U+41f9"]
UNICODE_TO_BLISS["U+41f9"] = ["spice box"]
BLISS_TO_UNICODE["shallowness"] = ["U+41fa"]
UNICODE_TO_BLISS["U+41fa"] = ["shallowness"]
BLISS_TO_UNICODE["two vertical lines"] = ["U+41fb"]
UNICODE_TO_BLISS["U+41fb"] = ["two vertical lines"]
BLISS_TO_UNICODE["gym"] = ["U+41fc"]
UNICODE_TO_BLISS["U+41fc"] = ["gym"]
BLISS_TO_UNICODE["gymnasium"] = ["U+41fc"]
UNICODE_TO_BLISS["U+41fc"].append("gymnasium")
BLISS_TO_UNICODE["gym,gymnasium"] = ["U+41fc"]
UNICODE_TO_BLISS["U+41fc"].append("gym,gymnasium")
BLISS_TO_UNICODE["gambler"] = ["U+41fd"]
UNICODE_TO_BLISS["U+41fd"] = ["gambler"]
BLISS_TO_UNICODE["embarkation"].append("U+41d8")
UNICODE_TO_BLISS["U+41d8"].append("embarkation")
BLISS_TO_UNICODE["boarding,embarkation"] = ["U+41d8"]
UNICODE_TO_BLISS["U+41d8"].append("boarding,embarkation")
BLISS_TO_UNICODE["solar energy"] = ["U+41fe"]
UNICODE_TO_BLISS["U+41fe"] = ["solar energy"]
BLISS_TO_UNICODE["solar power"] = ["U+41fe"]
UNICODE_TO_BLISS["U+41fe"].append("solar power")
BLISS_TO_UNICODE["solar energy,solar power"] = ["U+41fe"]
UNICODE_TO_BLISS["U+41fe"].append("solar energy,solar power")
BLISS_TO_UNICODE["palace"] = ["U+3c32"]
UNICODE_TO_BLISS["U+3c32"].append("palace")
BLISS_TO_UNICODE["castle,palace"] = ["U+3c32"]
UNICODE_TO_BLISS["U+3c32"].append("castle,palace")
BLISS_TO_UNICODE["rattle"] = ["U+41ff"]
UNICODE_TO_BLISS["U+41ff"] = ["rattle"]
BLISS_TO_UNICODE["my"] = ["U+4200"]
UNICODE_TO_BLISS["U+4200"] = ["my"]
BLISS_TO_UNICODE["mine"].append("U+4200")
UNICODE_TO_BLISS["U+4200"].append("mine")
BLISS_TO_UNICODE["my,mine"] = ["U+4200"]
UNICODE_TO_BLISS["U+4200"].append("my,mine")
BLISS_TO_UNICODE["two dots below"] = ["U+4201"]
UNICODE_TO_BLISS["U+4201"] = ["two dots below"]
BLISS_TO_UNICODE[" to represent seeds"] = ["U+4202"]
UNICODE_TO_BLISS["U+4202"] = [" to represent seeds"]
BLISS_TO_UNICODE["seem"] = ["U+4203"]
UNICODE_TO_BLISS["U+4203"] = ["seem"]
BLISS_TO_UNICODE["philosophy of religion"] = ["U+368f"]
UNICODE_TO_BLISS["U+368f"].append("philosophy of religion")
BLISS_TO_UNICODE["theology,philosophy of religion"] = ["U+368f"]
UNICODE_TO_BLISS["U+368f"].append("theology,philosophy of religion")
BLISS_TO_UNICODE["God-based religion"] = ["U+4204"]
UNICODE_TO_BLISS["U+4204"] = ["God-based religion"]
BLISS_TO_UNICODE["bass clarinet"] = ["U+4205"]
UNICODE_TO_BLISS["U+4205"] = ["bass clarinet"]
BLISS_TO_UNICODE["cheer"] = ["U+4206"]
UNICODE_TO_BLISS["U+4206"] = ["cheer"]
BLISS_TO_UNICODE["chess"] = ["U+4208"]
UNICODE_TO_BLISS["U+4208"] = ["chess"]
BLISS_TO_UNICODE["polar bear"] = ["U+4209"]
UNICODE_TO_BLISS["U+4209"] = ["polar bear"]
BLISS_TO_UNICODE["royal family"] = ["U+420a"]
UNICODE_TO_BLISS["U+420a"] = ["royal family"]
BLISS_TO_UNICODE["royal"] = ["U+420b"]
UNICODE_TO_BLISS["U+420b"] = ["royal"]
BLISS_TO_UNICODE["alarm"] = ["U+420c"]
UNICODE_TO_BLISS["U+420c"] = ["alarm"]
BLISS_TO_UNICODE["sequin"] = ["U+420d"]
UNICODE_TO_BLISS["U+420d"] = ["sequin"]
BLISS_TO_UNICODE["spangle"] = ["U+420d"]
UNICODE_TO_BLISS["U+420d"].append("spangle")
BLISS_TO_UNICODE["retire"] = ["U+420e"]
UNICODE_TO_BLISS["U+420e"] = ["retire"]
BLISS_TO_UNICODE["poison"] = ["U+420f"]
UNICODE_TO_BLISS["U+420f"] = ["poison"]
BLISS_TO_UNICODE["Dharma wheel"] = ["U+4210"]
UNICODE_TO_BLISS["U+4210"] = ["Dharma wheel"]
BLISS_TO_UNICODE["pictograph of spokes"] = ["U+4211"]
UNICODE_TO_BLISS["U+4211"] = ["pictograph of spokes"]
BLISS_TO_UNICODE["explain"] = ["U+4212"]
UNICODE_TO_BLISS["U+4212"] = ["explain"]
BLISS_TO_UNICODE["give a reason"] = ["U+4212"]
UNICODE_TO_BLISS["U+4212"].append("give a reason")
BLISS_TO_UNICODE["explain,give a reason"] = ["U+4212"]
UNICODE_TO_BLISS["U+4212"].append("explain,give a reason")
BLISS_TO_UNICODE["acne"] = ["U+4213"]
UNICODE_TO_BLISS["U+4213"] = ["acne"]
BLISS_TO_UNICODE["sweetener"] = ["U+3c77"]
UNICODE_TO_BLISS["U+3c77"].append("sweetener")
BLISS_TO_UNICODE["sugar,sweetener"] = ["U+3c77"]
UNICODE_TO_BLISS["U+3c77"].append("sugar,sweetener")
BLISS_TO_UNICODE["adding"] = ["U+4214"]
UNICODE_TO_BLISS["U+4214"] = ["adding"]
BLISS_TO_UNICODE["additive"] = ["U+4215"]
UNICODE_TO_BLISS["U+4215"] = ["additive"]
BLISS_TO_UNICODE["indicator +"] = ["U+4216"]
UNICODE_TO_BLISS["U+4216"] = ["indicator +"]
BLISS_TO_UNICODE["pictograph of a cluster of stalks"] = ["U+4217"]
UNICODE_TO_BLISS["U+4217"] = ["pictograph of a cluster of stalks"]
BLISS_TO_UNICODE["Frey"] = ["U+4218"]
UNICODE_TO_BLISS["U+4218"] = ["Frey"]
BLISS_TO_UNICODE["polenta"] = ["U+4219"]
UNICODE_TO_BLISS["U+4219"] = ["polenta"]
BLISS_TO_UNICODE["burial site"] = ["U+421a"]
UNICODE_TO_BLISS["U+421a"] = ["burial site"]
BLISS_TO_UNICODE["folder"] = ["U+421b"]
UNICODE_TO_BLISS["U+421b"] = ["folder"]
BLISS_TO_UNICODE["this month"] = ["U+421c"]
UNICODE_TO_BLISS["U+421c"] = ["this month"]
BLISS_TO_UNICODE["eating disorder"] = ["U+421d"]
UNICODE_TO_BLISS["U+421d"] = ["eating disorder"]
BLISS_TO_UNICODE["mental illness"] = ["U+421e"]
UNICODE_TO_BLISS["U+421e"] = ["mental illness"]
BLISS_TO_UNICODE["arrival"] = ["U+3243"]
UNICODE_TO_BLISS["U+3243"].append("arrival")
BLISS_TO_UNICODE["stop"].append("U+3243")
UNICODE_TO_BLISS["U+3243"].append("stop")
BLISS_TO_UNICODE["end,arrival,stop"] = ["U+3243"]
UNICODE_TO_BLISS["U+3243"].append("end,arrival,stop")
BLISS_TO_UNICODE["arrive"] = ["U+3a52"]
UNICODE_TO_BLISS["U+3a52"].append("arrive")
BLISS_TO_UNICODE["end"].append("U+3a52")
UNICODE_TO_BLISS["U+3a52"].append("end")
BLISS_TO_UNICODE["stop,arrive,end"] = ["U+3a52"]
UNICODE_TO_BLISS["U+3a52"].append("stop,arrive,end")
BLISS_TO_UNICODE["platform"].append("U+3a52")
UNICODE_TO_BLISS["U+3a52"].append("platform")
BLISS_TO_UNICODE["stop,platform"] = ["U+3a52"]
UNICODE_TO_BLISS["U+3a52"].append("stop,platform")
BLISS_TO_UNICODE["football supporters club"] = ["U+421f"]
UNICODE_TO_BLISS["U+421f"] = ["football supporters club"]
BLISS_TO_UNICODE["meditate"] = ["U+4220"]
UNICODE_TO_BLISS["U+4220"] = ["meditate"]
BLISS_TO_UNICODE["to reflect"] = ["U+4221"]
UNICODE_TO_BLISS["U+4221"] = ["to reflect"]
BLISS_TO_UNICODE["obey"] = ["U+4222"]
UNICODE_TO_BLISS["U+4222"] = ["obey"]
BLISS_TO_UNICODE["comply"] = ["U+4222"]
UNICODE_TO_BLISS["U+4222"].append("comply")
BLISS_TO_UNICODE["obey,comply"] = ["U+4222"]
UNICODE_TO_BLISS["U+4222"].append("obey,comply")
BLISS_TO_UNICODE["cake"].append("U+3c48")
UNICODE_TO_BLISS["U+3c48"].append("cake")
BLISS_TO_UNICODE["bar,cake"] = ["U+3c48"]
UNICODE_TO_BLISS["U+3c48"].append("bar,cake")
BLISS_TO_UNICODE["bar"].append("U+35a2")
UNICODE_TO_BLISS["U+35a2"].append("bar")
BLISS_TO_UNICODE["disco"] = ["U+4223"]
UNICODE_TO_BLISS["U+4223"] = ["disco"]
BLISS_TO_UNICODE["bag"].append("U+3501")
UNICODE_TO_BLISS["U+3501"].append("bag")
BLISS_TO_UNICODE["sack,bag"] = ["U+3501"]
UNICODE_TO_BLISS["U+3501"].append("sack,bag")
BLISS_TO_UNICODE["bleat"] = ["U+4225"]
UNICODE_TO_BLISS["U+4225"] = ["bleat"]
BLISS_TO_UNICODE["baa"] = ["U+4225"]
UNICODE_TO_BLISS["U+4225"].append("baa")
BLISS_TO_UNICODE["bleat,baa"] = ["U+4225"]
UNICODE_TO_BLISS["U+4225"].append("bleat,baa")
BLISS_TO_UNICODE["linguist"] = ["U+4226"]
UNICODE_TO_BLISS["U+4226"] = ["linguist"]
BLISS_TO_UNICODE["linguistics"] = ["U+4227"]
UNICODE_TO_BLISS["U+4227"] = ["linguistics"]
BLISS_TO_UNICODE["military reserve duty"] = ["U+4228"]
UNICODE_TO_BLISS["U+4228"] = ["military reserve duty"]
BLISS_TO_UNICODE["secret agent"] = ["U+4229"]
UNICODE_TO_BLISS["U+4229"] = ["secret agent"]
BLISS_TO_UNICODE["spy"] = ["U+4229"]
UNICODE_TO_BLISS["U+4229"].append("spy")
BLISS_TO_UNICODE["secret agent,spy"] = ["U+4229"]
UNICODE_TO_BLISS["U+4229"].append("secret agent,spy")
BLISS_TO_UNICODE["prophesy"] = ["U+422a"]
UNICODE_TO_BLISS["U+422a"] = ["prophesy"]
BLISS_TO_UNICODE["prophecy"] = ["U+422b"]
UNICODE_TO_BLISS["U+422b"] = ["prophecy"]
BLISS_TO_UNICODE["Christianity"].append("U+3438")
UNICODE_TO_BLISS["U+3438"].append("Christianity")
BLISS_TO_UNICODE["cross,Christianity"] = ["U+3438"]
UNICODE_TO_BLISS["U+3438"].append("cross,Christianity")
BLISS_TO_UNICODE["last year"] = ["U+422c"]
UNICODE_TO_BLISS["U+422c"] = ["last year"]
BLISS_TO_UNICODE["Christmas Eve"] = ["U+422d"]
UNICODE_TO_BLISS["U+422d"] = ["Christmas Eve"]
BLISS_TO_UNICODE["shaver"] = ["U+422e"]
UNICODE_TO_BLISS["U+422e"] = ["shaver"]
BLISS_TO_UNICODE["razor"] = ["U+422e"]
UNICODE_TO_BLISS["U+422e"].append("razor")
BLISS_TO_UNICODE["shaver,razor"] = ["U+422e"]
UNICODE_TO_BLISS["U+422e"].append("shaver,razor")
BLISS_TO_UNICODE["physicist"] = ["U+422f"]
UNICODE_TO_BLISS["U+422f"] = ["physicist"]
BLISS_TO_UNICODE["mezuzah"] = ["U+4230"]
UNICODE_TO_BLISS["U+4230"] = ["mezuzah"]
BLISS_TO_UNICODE["cousin"] = ["U+4231"]
UNICODE_TO_BLISS["U+4231"] = ["cousin"]
BLISS_TO_UNICODE["theologian"] = ["U+4232"]
UNICODE_TO_BLISS["U+4232"] = ["theologian"]
BLISS_TO_UNICODE["theologist"] = ["U+4232"]
UNICODE_TO_BLISS["U+4232"].append("theologist")
BLISS_TO_UNICODE["theologian,theologist"] = ["U+4232"]
UNICODE_TO_BLISS["U+4232"].append("theologian,theologist")
BLISS_TO_UNICODE["opposed to"] = ["U+3427"]
UNICODE_TO_BLISS["U+3427"].append("opposed to")
BLISS_TO_UNICODE["against,opposed to"] = ["U+3427"]
UNICODE_TO_BLISS["U+3427"].append("against,opposed to")
BLISS_TO_UNICODE["Gemini"] = ["U+4233"]
UNICODE_TO_BLISS["U+4233"] = ["Gemini"]
BLISS_TO_UNICODE["sea anemone"] = ["U+4234"]
UNICODE_TO_BLISS["U+4234"] = ["sea anemone"]
BLISS_TO_UNICODE["Arabic numeral 3 small"] = ["U+4235"]
UNICODE_TO_BLISS["U+4235"] = ["Arabic numeral 3 small"]
BLISS_TO_UNICODE["basin"].append("U+3cfd")
UNICODE_TO_BLISS["U+3cfd"].append("basin")
BLISS_TO_UNICODE["sink,basin"] = ["U+3cfd"]
UNICODE_TO_BLISS["U+3cfd"].append("sink,basin")
BLISS_TO_UNICODE["website"] = ["U+4236"]
UNICODE_TO_BLISS["U+4236"] = ["website"]
BLISS_TO_UNICODE["paraskiing"] = ["U+4237"]
UNICODE_TO_BLISS["U+4237"] = ["paraskiing"]
BLISS_TO_UNICODE["skiis"] = ["U+4238"]
UNICODE_TO_BLISS["U+4238"] = ["skiis"]
BLISS_TO_UNICODE["dismiss"] = ["U+3501"]
UNICODE_TO_BLISS["U+3501"].append("dismiss")
BLISS_TO_UNICODE["sack,dismiss"] = ["U+3501"]
UNICODE_TO_BLISS["U+3501"].append("sack,dismiss")
BLISS_TO_UNICODE["record"].append("U+3ff4")
UNICODE_TO_BLISS["U+3ff4"].append("record")
BLISS_TO_UNICODE["CD,record"] = ["U+3ff4"]
UNICODE_TO_BLISS["U+3ff4"].append("CD,record")
BLISS_TO_UNICODE["recording disk"] = ["U+4239"]
UNICODE_TO_BLISS["U+4239"] = ["recording disk"]
BLISS_TO_UNICODE["riding boots"] = ["U+423a"]
UNICODE_TO_BLISS["U+423a"] = ["riding boots"]
BLISS_TO_UNICODE["boots"] = ["U+423b"]
UNICODE_TO_BLISS["U+423b"] = ["boots"]
BLISS_TO_UNICODE["Persian"] = ["U+423c"]
UNICODE_TO_BLISS["U+423c"] = ["Persian"]
BLISS_TO_UNICODE["work from home"] = ["U+423d"]
UNICODE_TO_BLISS["U+423d"] = ["work from home"]
BLISS_TO_UNICODE["sense of balance"] = ["U+39fc"]
UNICODE_TO_BLISS["U+39fc"].append("sense of balance")
BLISS_TO_UNICODE["balance,sense of balance"] = ["U+39fc"]
UNICODE_TO_BLISS["U+39fc"].append("balance,sense of balance")
BLISS_TO_UNICODE["standing)"] = ["U+39fc"]
UNICODE_TO_BLISS["U+39fc"].append("standing)")
BLISS_TO_UNICODE["Arabic numeral 7 small"] = ["U+423e"]
UNICODE_TO_BLISS["U+423e"] = ["Arabic numeral 7 small"]
BLISS_TO_UNICODE["diaphragm"] = ["U+423f"]
UNICODE_TO_BLISS["U+423f"] = ["diaphragm"]
BLISS_TO_UNICODE["pessary"] = ["U+423f"]
UNICODE_TO_BLISS["U+423f"].append("pessary")
BLISS_TO_UNICODE["midriff"] = ["U+423f"]
UNICODE_TO_BLISS["U+423f"].append("midriff")
BLISS_TO_UNICODE["diaphragm,midriff"] = ["U+423f"]
UNICODE_TO_BLISS["U+423f"].append("diaphragm,midriff")
BLISS_TO_UNICODE["CKB says that this symbol is derived from small. The symbol also looks like the top part of the symbols for man and woman minus the specific gender parts. It refers to things rather than to people."] = ["U+4240"]
UNICODE_TO_BLISS["U+4240"] = ["CKB says that this symbol is derived from small. The symbol also looks like the top part of the symbols for man and woman minus the specific gender parts. It refers to things rather than to people."]
BLISS_TO_UNICODE["shame"] = ["U+4241"]
UNICODE_TO_BLISS["U+4241"] = ["shame"]
BLISS_TO_UNICODE["astrologer"] = ["U+4242"]
UNICODE_TO_BLISS["U+4242"] = ["astrologer"]
BLISS_TO_UNICODE["astrologist"] = ["U+4242"]
UNICODE_TO_BLISS["U+4242"].append("astrologist")
BLISS_TO_UNICODE["astrologer,astrologist"] = ["U+4242"]
UNICODE_TO_BLISS["U+4242"].append("astrologer,astrologist")
BLISS_TO_UNICODE["disappear"] = ["U+4243"]
UNICODE_TO_BLISS["U+4243"] = ["disappear"]
BLISS_TO_UNICODE["if"] = ["U+4244"]
UNICODE_TO_BLISS["U+4244"] = ["if"]
BLISS_TO_UNICODE["growl"] = ["U+4245"]
UNICODE_TO_BLISS["U+4245"] = ["growl"]
BLISS_TO_UNICODE["after school club"] = ["U+3c7e"]
UNICODE_TO_BLISS["U+3c7e"].append("after school club")
BLISS_TO_UNICODE["youth club"] = ["U+3c7e"]
UNICODE_TO_BLISS["U+3c7e"].append("youth club")
BLISS_TO_UNICODE["writer"] = ["U+4246"]
UNICODE_TO_BLISS["U+4246"] = ["writer"]
BLISS_TO_UNICODE["author"] = ["U+4246"]
UNICODE_TO_BLISS["U+4246"].append("author")
BLISS_TO_UNICODE["writer,author"] = ["U+4246"]
UNICODE_TO_BLISS["U+4246"].append("writer,author")
BLISS_TO_UNICODE["vegetable"].append("U+34a9")
UNICODE_TO_BLISS["U+34a9"].append("vegetable")
BLISS_TO_UNICODE["carrot,vegetable"] = ["U+34a9"]
UNICODE_TO_BLISS["U+34a9"].append("carrot,vegetable")
BLISS_TO_UNICODE["concert hall"] = ["U+4247"]
UNICODE_TO_BLISS["U+4247"] = ["concert hall"]
BLISS_TO_UNICODE["waterfall"] = ["U+4248"]
UNICODE_TO_BLISS["U+4248"] = ["waterfall"]
BLISS_TO_UNICODE["to fall"] = ["U+4249"]
UNICODE_TO_BLISS["U+4249"] = ["to fall"]
BLISS_TO_UNICODE["garlic"] = ["U+424a"]
UNICODE_TO_BLISS["U+424a"] = ["garlic"]
BLISS_TO_UNICODE["unicorn"] = ["U+424b"]
UNICODE_TO_BLISS["U+424b"] = ["unicorn"]
BLISS_TO_UNICODE["pictograph of a single horn"] = ["U+424c"]
UNICODE_TO_BLISS["U+424c"] = ["pictograph of a single horn"]
BLISS_TO_UNICODE["jealous"] = ["U+424d"]
UNICODE_TO_BLISS["U+424d"] = ["jealous"]
BLISS_TO_UNICODE["to resent"] = ["U+424e"]
UNICODE_TO_BLISS["U+424e"] = ["to resent"]
BLISS_TO_UNICODE["butter"] = ["U+424f"]
UNICODE_TO_BLISS["U+424f"] = ["butter"]
BLISS_TO_UNICODE["tombstone"] = ["U+4250"]
UNICODE_TO_BLISS["U+4250"] = ["tombstone"]
BLISS_TO_UNICODE["left turn"] = ["U+4251"]
UNICODE_TO_BLISS["U+4251"] = ["left turn"]
BLISS_TO_UNICODE["left"].append("U+4251")
UNICODE_TO_BLISS["U+4251"].append("left")
BLISS_TO_UNICODE["left turn,left"] = ["U+4251"]
UNICODE_TO_BLISS["U+4251"].append("left turn,left")
BLISS_TO_UNICODE["napkin"] = ["U+4252"]
UNICODE_TO_BLISS["U+4252"] = ["napkin"]
BLISS_TO_UNICODE["serviette"] = ["U+4252"]
UNICODE_TO_BLISS["U+4252"].append("serviette")
BLISS_TO_UNICODE["napkin,serviette"] = ["U+4252"]
UNICODE_TO_BLISS["U+4252"].append("napkin,serviette")
BLISS_TO_UNICODE["to eat"] = ["U+4253"]
UNICODE_TO_BLISS["U+4253"] = ["to eat"]
BLISS_TO_UNICODE["pile"].append("U+35af")
UNICODE_TO_BLISS["U+35af"].append("pile")
BLISS_TO_UNICODE["tussock"].append("U+35af")
UNICODE_TO_BLISS["U+35af"].append("tussock")
BLISS_TO_UNICODE["collection,pile,tussock"] = ["U+35af"]
UNICODE_TO_BLISS["U+35af"].append("collection,pile,tussock")
BLISS_TO_UNICODE["yes"] = ["U+4254"]
UNICODE_TO_BLISS["U+4254"] = ["yes"]
BLISS_TO_UNICODE["sunflower"] = ["U+4255"]
UNICODE_TO_BLISS["U+4255"] = ["sunflower"]
BLISS_TO_UNICODE["Aquarius"] = ["U+4256"]
UNICODE_TO_BLISS["U+4256"] = ["Aquarius"]
BLISS_TO_UNICODE["Freya"] = ["U+4257"]
UNICODE_TO_BLISS["U+4257"] = ["Freya"]
BLISS_TO_UNICODE["rock music"] = ["U+4258"]
UNICODE_TO_BLISS["U+4258"] = ["rock music"]
BLISS_TO_UNICODE["bar mitzvah"] = ["U+4259"]
UNICODE_TO_BLISS["U+4259"] = ["bar mitzvah"]
BLISS_TO_UNICODE["signal reception"] = ["U+425a"]
UNICODE_TO_BLISS["U+425a"] = ["signal reception"]
BLISS_TO_UNICODE["identity card"] = ["U+425b"]
UNICODE_TO_BLISS["U+425b"] = ["identity card"]
BLISS_TO_UNICODE["deaf"] = ["U+425c"]
UNICODE_TO_BLISS["U+425c"] = ["deaf"]
BLISS_TO_UNICODE["deceased"] = ["U+381f"]
UNICODE_TO_BLISS["U+381f"].append("deceased")
BLISS_TO_UNICODE["dead,deceased"] = ["U+381f"]
UNICODE_TO_BLISS["U+381f"].append("dead,deceased")
BLISS_TO_UNICODE["dining room"] = ["U+425d"]
UNICODE_TO_BLISS["U+425d"] = ["dining room"]
BLISS_TO_UNICODE["invoice"] = ["U+425e"]
UNICODE_TO_BLISS["U+425e"] = ["invoice"]
BLISS_TO_UNICODE["dear"] = ["U+425f"]
UNICODE_TO_BLISS["U+425f"] = ["dear"]
BLISS_TO_UNICODE["theatre"] = ["U+4260"]
UNICODE_TO_BLISS["U+4260"] = ["theatre"]
BLISS_TO_UNICODE["to hear"] = ["U+4261"]
UNICODE_TO_BLISS["U+4261"] = ["to hear"]
BLISS_TO_UNICODE["monitor"].append("U+39a7")
UNICODE_TO_BLISS["U+39a7"].append("monitor")
BLISS_TO_UNICODE["computer screen,monitor"] = ["U+39a7"]
UNICODE_TO_BLISS["U+39a7"].append("computer screen,monitor")
BLISS_TO_UNICODE["microwave"] = ["U+4262"]
UNICODE_TO_BLISS["U+4262"] = ["microwave"]
BLISS_TO_UNICODE["tracker"] = ["U+4263"]
UNICODE_TO_BLISS["U+4263"] = ["tracker"]
BLISS_TO_UNICODE["burn"] = ["U+4264"]
UNICODE_TO_BLISS["U+4264"] = ["burn"]
BLISS_TO_UNICODE["North America"] = ["U+4265"]
UNICODE_TO_BLISS["U+4265"] = ["North America"]
BLISS_TO_UNICODE["Sweden"] = ["U+4266"]
UNICODE_TO_BLISS["U+4266"] = ["Sweden"]
BLISS_TO_UNICODE["ice field"] = ["U+4267"]
UNICODE_TO_BLISS["U+4267"] = ["ice field"]
BLISS_TO_UNICODE["bolt"] = ["U+4268"]
UNICODE_TO_BLISS["U+4268"] = ["bolt"]
BLISS_TO_UNICODE["three intensity characters"] = ["U+4269"]
UNICODE_TO_BLISS["U+4269"] = ["three intensity characters"]
BLISS_TO_UNICODE["bury"] = ["U+426a"]
UNICODE_TO_BLISS["U+426a"] = ["bury"]
BLISS_TO_UNICODE["hide"] = ["U+426b"]
UNICODE_TO_BLISS["U+426b"] = ["hide"]
BLISS_TO_UNICODE["conceal"] = ["U+426b"]
UNICODE_TO_BLISS["U+426b"].append("conceal")
BLISS_TO_UNICODE["hide,conceal"] = ["U+426b"]
UNICODE_TO_BLISS["U+426b"].append("hide,conceal")
BLISS_TO_UNICODE["sleeping bag"] = ["U+426c"]
UNICODE_TO_BLISS["U+426c"] = ["sleeping bag"]
BLISS_TO_UNICODE["afternoon"] = ["U+426d"]
UNICODE_TO_BLISS["U+426d"] = ["afternoon"]
BLISS_TO_UNICODE["nerve"] = ["U+426e"]
UNICODE_TO_BLISS["U+426e"] = ["nerve"]
BLISS_TO_UNICODE["castanets"] = ["U+426f"]
UNICODE_TO_BLISS["U+426f"] = ["castanets"]
BLISS_TO_UNICODE["jobcentre"] = ["U+4270"]
UNICODE_TO_BLISS["U+4270"] = ["jobcentre"]
BLISS_TO_UNICODE["job centre"] = ["U+4270"]
UNICODE_TO_BLISS["U+4270"].append("job centre")
BLISS_TO_UNICODE["jobcentre,job-centre"] = ["U+4270"]
UNICODE_TO_BLISS["U+4270"].append("jobcentre,job-centre")
BLISS_TO_UNICODE["whipping knot"] = ["U+4271"]
UNICODE_TO_BLISS["U+4271"] = ["whipping knot"]
BLISS_TO_UNICODE["frightened"] = ["U+3b0b"]
UNICODE_TO_BLISS["U+3b0b"].append("frightened")
BLISS_TO_UNICODE["scared"].append("U+3b0b")
UNICODE_TO_BLISS["U+3b0b"].append("scared")
BLISS_TO_UNICODE["afraid,frightened,scared"] = ["U+3b0b"]
UNICODE_TO_BLISS["U+3b0b"].append("afraid,frightened,scared")
BLISS_TO_UNICODE["flying"] = ["U+4272"]
UNICODE_TO_BLISS["U+4272"] = ["flying"]
BLISS_TO_UNICODE["educationalist"] = ["U+4273"]
UNICODE_TO_BLISS["U+4273"] = ["educationalist"]
BLISS_TO_UNICODE["educationist"] = ["U+4273"]
UNICODE_TO_BLISS["U+4273"].append("educationist")
BLISS_TO_UNICODE["educationalist,educationist"] = ["U+4273"]
UNICODE_TO_BLISS["U+4273"].append("educationalist,educationist")
BLISS_TO_UNICODE["form"] = ["U+3797"]
UNICODE_TO_BLISS["U+3797"].append("form")
BLISS_TO_UNICODE["shape,form"] = ["U+3797"]
UNICODE_TO_BLISS["U+3797"].append("shape,form")
BLISS_TO_UNICODE["January"] = ["U+4274"]
UNICODE_TO_BLISS["U+4274"] = ["January"]
BLISS_TO_UNICODE["fore"] = ["U+32ad"]
UNICODE_TO_BLISS["U+32ad"].append("fore")
BLISS_TO_UNICODE["bow,fore"] = ["U+32ad"]
UNICODE_TO_BLISS["U+32ad"].append("bow,fore")
BLISS_TO_UNICODE["diaper"] = ["U+4275"]
UNICODE_TO_BLISS["U+4275"] = ["diaper"]
BLISS_TO_UNICODE["nappy"] = ["U+4275"]
UNICODE_TO_BLISS["U+4275"].append("nappy")
BLISS_TO_UNICODE["diaper,nappy"] = ["U+4275"]
UNICODE_TO_BLISS["U+4275"].append("diaper,nappy")
BLISS_TO_UNICODE["fort"] = ["U+4276"]
UNICODE_TO_BLISS["U+4276"] = ["fort"]
BLISS_TO_UNICODE["fortress"] = ["U+4276"]
UNICODE_TO_BLISS["U+4276"].append("fortress")
BLISS_TO_UNICODE["fort,fortress"] = ["U+4276"]
UNICODE_TO_BLISS["U+4276"].append("fort,fortress")
BLISS_TO_UNICODE["return"] = ["U+4277"]
UNICODE_TO_BLISS["U+4277"] = ["return"]
BLISS_TO_UNICODE["come back"] = ["U+4277"]
UNICODE_TO_BLISS["U+4277"].append("come back")
BLISS_TO_UNICODE["reverse"] = ["U+4277"]
UNICODE_TO_BLISS["U+4277"].append("reverse")
BLISS_TO_UNICODE["return,come back,reverse"] = ["U+4277"]
UNICODE_TO_BLISS["U+4277"].append("return,come back,reverse")
BLISS_TO_UNICODE["ski jumping"] = ["U+4278"]
UNICODE_TO_BLISS["U+4278"] = ["ski jumping"]
BLISS_TO_UNICODE["lower leg"] = ["U+4279"]
UNICODE_TO_BLISS["U+4279"] = ["lower leg"]
BLISS_TO_UNICODE["shank"] = ["U+4279"]
UNICODE_TO_BLISS["U+4279"].append("shank")
BLISS_TO_UNICODE["shin"] = ["U+4279"]
UNICODE_TO_BLISS["U+4279"].append("shin")
BLISS_TO_UNICODE["lower leg,shank,shin"] = ["U+4279"]
UNICODE_TO_BLISS["U+4279"].append("lower leg,shank,shin")
BLISS_TO_UNICODE["Romanian"] = ["U+427a"]
UNICODE_TO_BLISS["U+427a"] = ["Romanian"]
BLISS_TO_UNICODE["Romania"] = ["U+427b"]
UNICODE_TO_BLISS["U+427b"] = ["Romania"]
BLISS_TO_UNICODE["sexually mature"] = ["U+427c"]
UNICODE_TO_BLISS["U+427c"] = ["sexually mature"]
BLISS_TO_UNICODE["Good day"] = ["U+427d"]
UNICODE_TO_BLISS["U+427d"] = ["Good day"]
BLISS_TO_UNICODE["Tibet"] = ["U+427e"]
UNICODE_TO_BLISS["U+427e"] = ["Tibet"]
BLISS_TO_UNICODE["cartoon"] = ["U+427f"]
UNICODE_TO_BLISS["U+427f"] = ["cartoon"]
BLISS_TO_UNICODE["animated picture"] = ["U+427f"]
UNICODE_TO_BLISS["U+427f"].append("animated picture")
BLISS_TO_UNICODE["cartoon,animated picture"] = ["U+427f"]
UNICODE_TO_BLISS["U+427f"].append("cartoon,animated picture")
BLISS_TO_UNICODE["digital"] = ["U+4280"]
UNICODE_TO_BLISS["U+4280"] = ["digital"]
BLISS_TO_UNICODE["diet"] = ["U+4281"]
UNICODE_TO_BLISS["U+4281"] = ["diet"]
BLISS_TO_UNICODE["exported"] = ["U+4282"]
UNICODE_TO_BLISS["U+4282"] = ["exported"]
BLISS_TO_UNICODE["export"] = ["U+4283"]
UNICODE_TO_BLISS["U+4283"] = ["export"]
BLISS_TO_UNICODE["weekend"] = ["U+4284"]
UNICODE_TO_BLISS["U+4284"] = ["weekend"]
BLISS_TO_UNICODE["week"] = ["U+4285"]
UNICODE_TO_BLISS["U+4285"] = ["week"]
BLISS_TO_UNICODE["potato"] = ["U+4286"]
UNICODE_TO_BLISS["U+4286"] = ["potato"]
BLISS_TO_UNICODE["monkey"] = ["U+4287"]
UNICODE_TO_BLISS["U+4287"] = ["monkey"]
BLISS_TO_UNICODE["ape"] = ["U+4287"]
UNICODE_TO_BLISS["U+4287"].append("ape")
BLISS_TO_UNICODE["gorilla"] = ["U+4287"]
UNICODE_TO_BLISS["U+4287"].append("gorilla")
BLISS_TO_UNICODE["primate"] = ["U+4287"]
UNICODE_TO_BLISS["U+4287"].append("primate")
BLISS_TO_UNICODE["monkey,ape,gorilla,primate"] = ["U+4287"]
UNICODE_TO_BLISS["U+4287"].append("monkey,ape,gorilla,primate")
BLISS_TO_UNICODE["similar to"] = ["U+4288"]
UNICODE_TO_BLISS["U+4288"] = ["similar to"]
BLISS_TO_UNICODE["Megillah"] = ["U+4289"]
UNICODE_TO_BLISS["U+4289"] = ["Megillah"]
BLISS_TO_UNICODE["invent"] = ["U+428a"]
UNICODE_TO_BLISS["U+428a"] = ["invent"]
BLISS_TO_UNICODE["anticipation"] = ["U+333c"]
UNICODE_TO_BLISS["U+333c"].append("anticipation")
BLISS_TO_UNICODE["expectation,anticipation"] = ["U+333c"]
UNICODE_TO_BLISS["U+333c"].append("expectation,anticipation")
BLISS_TO_UNICODE["disgusting"] = ["U+428b"]
UNICODE_TO_BLISS["U+428b"] = ["disgusting"]
BLISS_TO_UNICODE["not tasty"] = ["U+428c"]
UNICODE_TO_BLISS["U+428c"] = ["not tasty"]
BLISS_TO_UNICODE["disgust"] = ["U+428d"]
UNICODE_TO_BLISS["U+428d"] = ["disgust"]
BLISS_TO_UNICODE["0"].append("U+355f")
UNICODE_TO_BLISS["U+355f"].append("0")
BLISS_TO_UNICODE["Arabic numeral 0"] = ["U+428e"]
UNICODE_TO_BLISS["U+428e"] = ["Arabic numeral 0"]
BLISS_TO_UNICODE["Holy Trinity"] = ["U+428f"]
UNICODE_TO_BLISS["U+428f"] = ["Holy Trinity"]
BLISS_TO_UNICODE["smartphone"] = ["U+4290"]
UNICODE_TO_BLISS["U+4290"] = ["smartphone"]
BLISS_TO_UNICODE["digital phone"] = ["U+4290"]
UNICODE_TO_BLISS["U+4290"].append("digital phone")
BLISS_TO_UNICODE["smartphone,digital phone"] = ["U+4290"]
UNICODE_TO_BLISS["U+4290"].append("smartphone,digital phone")
BLISS_TO_UNICODE["yeast"] = ["U+4292"]
UNICODE_TO_BLISS["U+4292"] = ["yeast"]
BLISS_TO_UNICODE["rubber boat"] = ["U+4293"]
UNICODE_TO_BLISS["U+4293"] = ["rubber boat"]
BLISS_TO_UNICODE["dinghy"] = ["U+4293"]
UNICODE_TO_BLISS["U+4293"].append("dinghy")
BLISS_TO_UNICODE["rubber boat,dinghy"] = ["U+4293"]
UNICODE_TO_BLISS["U+4293"].append("rubber boat,dinghy")
BLISS_TO_UNICODE["die"] = ["U+4294"]
UNICODE_TO_BLISS["U+4294"] = ["die"]
BLISS_TO_UNICODE["dice"] = ["U+4295"]
UNICODE_TO_BLISS["U+4295"] = ["dice"]
BLISS_TO_UNICODE["die"].append("U+4295")
UNICODE_TO_BLISS["U+4295"].append("die")
BLISS_TO_UNICODE["dice,die"] = ["U+4295"]
UNICODE_TO_BLISS["U+4295"].append("dice,die")
BLISS_TO_UNICODE["magnet"] = ["U+4296"]
UNICODE_TO_BLISS["U+4296"] = ["magnet"]
BLISS_TO_UNICODE["excellence"] = ["U+4297"]
UNICODE_TO_BLISS["U+4297"] = ["excellence"]
BLISS_TO_UNICODE["correctness"] = ["U+4298"]
UNICODE_TO_BLISS["U+4298"] = ["correctness"]
BLISS_TO_UNICODE["shave"] = ["U+4299"]
UNICODE_TO_BLISS["U+4299"] = ["shave"]
BLISS_TO_UNICODE["salt crystal"] = ["U+429a"]
UNICODE_TO_BLISS["U+429a"] = ["salt crystal"]
BLISS_TO_UNICODE["flavouring,seasoning"] = ["U+392b"]
UNICODE_TO_BLISS["U+392b"].append("flavouring,seasoning")
BLISS_TO_UNICODE["Old Testament"] = ["U+429b"]
UNICODE_TO_BLISS["U+429b"] = ["Old Testament"]
BLISS_TO_UNICODE["international"] = ["U+429c"]
UNICODE_TO_BLISS["U+429c"] = ["international"]
BLISS_TO_UNICODE["make a speech"] = ["U+429d"]
UNICODE_TO_BLISS["U+429d"] = ["make a speech"]
BLISS_TO_UNICODE["makeup"] = ["U+429e"]
UNICODE_TO_BLISS["U+429e"] = ["makeup"]
BLISS_TO_UNICODE["entire"] = ["U+39b2"]
UNICODE_TO_BLISS["U+39b2"].append("entire")
BLISS_TO_UNICODE["stallion,entire"] = ["U+39b2"]
UNICODE_TO_BLISS["U+39b2"].append("stallion,entire")
BLISS_TO_UNICODE["detest"] = ["U+429f"]
UNICODE_TO_BLISS["U+429f"] = ["detest"]
BLISS_TO_UNICODE["despise"] = ["U+429f"]
UNICODE_TO_BLISS["U+429f"].append("despise")
BLISS_TO_UNICODE["detest,despise"] = ["U+429f"]
UNICODE_TO_BLISS["U+429f"].append("detest,despise")
BLISS_TO_UNICODE["earthquake"] = ["U+42a0"]
UNICODE_TO_BLISS["U+42a0"] = ["earthquake"]
BLISS_TO_UNICODE["to shake"] = ["U+42a1"]
UNICODE_TO_BLISS["U+42a1"] = ["to shake"]
BLISS_TO_UNICODE["wait"] = ["U+42a2"]
UNICODE_TO_BLISS["U+42a2"] = ["wait"]
BLISS_TO_UNICODE["waiting"] = ["U+42a2"]
UNICODE_TO_BLISS["U+42a2"].append("waiting")
BLISS_TO_UNICODE["wait,waiting"] = ["U+42a2"]
UNICODE_TO_BLISS["U+42a2"].append("wait,waiting")
BLISS_TO_UNICODE["arc"] = ["U+32ad"]
UNICODE_TO_BLISS["U+32ad"].append("arc")
BLISS_TO_UNICODE["bow,arc"] = ["U+32ad"]
UNICODE_TO_BLISS["U+32ad"].append("bow,arc")
BLISS_TO_UNICODE["proposal"] = ["U+3ad7"]
UNICODE_TO_BLISS["U+3ad7"].append("proposal")
BLISS_TO_UNICODE["suggestion,proposal"] = ["U+3ad7"]
UNICODE_TO_BLISS["U+3ad7"].append("suggestion,proposal")
BLISS_TO_UNICODE["row"].append("U+3729")
UNICODE_TO_BLISS["U+3729"].append("row")
BLISS_TO_UNICODE["quarrel,row"] = ["U+3729"]
UNICODE_TO_BLISS["U+3729"].append("quarrel,row")
BLISS_TO_UNICODE["dance therapist"] = ["U+42a3"]
UNICODE_TO_BLISS["U+42a3"] = ["dance therapist"]
BLISS_TO_UNICODE["The Groke"] = ["U+42a4"]
UNICODE_TO_BLISS["U+42a4"] = ["The Groke"]
BLISS_TO_UNICODE["schach"] = ["U+42a5"]
UNICODE_TO_BLISS["U+42a5"] = ["schach"]
BLISS_TO_UNICODE["sport elf"] = ["U+42a7"]
UNICODE_TO_BLISS["U+42a7"] = ["sport elf"]
BLISS_TO_UNICODE["rocking horse"] = ["U+42a8"]
UNICODE_TO_BLISS["U+42a8"] = ["rocking horse"]
BLISS_TO_UNICODE["to rock"] = ["U+42a9"]
UNICODE_TO_BLISS["U+42a9"] = ["to rock"]
BLISS_TO_UNICODE["kayak"] = ["U+42aa"]
UNICODE_TO_BLISS["U+42aa"] = ["kayak"]
BLISS_TO_UNICODE["everybody"] = ["U+42ab"]
UNICODE_TO_BLISS["U+42ab"] = ["everybody"]
BLISS_TO_UNICODE["everyone"] = ["U+42ab"]
UNICODE_TO_BLISS["U+42ab"].append("everyone")
BLISS_TO_UNICODE["everybody,everyone"] = ["U+42ab"]
UNICODE_TO_BLISS["U+42ab"].append("everybody,everyone")
BLISS_TO_UNICODE["Australia"] = ["U+42ac"]
UNICODE_TO_BLISS["U+42ac"] = ["Australia"]
BLISS_TO_UNICODE["additive"].append("U+4214")
UNICODE_TO_BLISS["U+4214"].append("additive")
BLISS_TO_UNICODE["adding,additive"] = ["U+4214"]
UNICODE_TO_BLISS["U+4214"].append("adding,additive")
BLISS_TO_UNICODE["discus"] = ["U+42ad"]
UNICODE_TO_BLISS["U+42ad"] = ["discus"]
BLISS_TO_UNICODE["bottle opener"] = ["U+42ae"]
UNICODE_TO_BLISS["U+42ae"] = ["bottle opener"]
BLISS_TO_UNICODE["zigzag line"] = ["U+42af"]
UNICODE_TO_BLISS["U+42af"] = ["zigzag line"]
BLISS_TO_UNICODE["somersault"] = ["U+42b0"]
UNICODE_TO_BLISS["U+42b0"] = ["somersault"]
BLISS_TO_UNICODE["cremate"] = ["U+42b1"]
UNICODE_TO_BLISS["U+42b1"] = ["cremate"]
BLISS_TO_UNICODE["labyrinth"] = ["U+42b2"]
UNICODE_TO_BLISS["U+42b2"] = ["labyrinth"]
BLISS_TO_UNICODE["maze"] = ["U+42b2"]
UNICODE_TO_BLISS["U+42b2"].append("maze")
BLISS_TO_UNICODE["labyrinth,maze"] = ["U+42b2"]
UNICODE_TO_BLISS["U+42b2"].append("labyrinth,maze")
BLISS_TO_UNICODE["GPS"] = ["U+42b3"]
UNICODE_TO_BLISS["U+42b3"] = ["GPS"]
BLISS_TO_UNICODE["satnav"] = ["U+42b3"]
UNICODE_TO_BLISS["U+42b3"].append("satnav")
BLISS_TO_UNICODE["GPS,satnav"] = ["U+42b3"]
UNICODE_TO_BLISS["U+42b3"].append("GPS,satnav")
BLISS_TO_UNICODE["to fly"] = ["U+42b4"]
UNICODE_TO_BLISS["U+42b4"] = ["to fly"]
BLISS_TO_UNICODE["soul"] = ["U+42b5"]
UNICODE_TO_BLISS["U+42b5"] = ["soul"]
BLISS_TO_UNICODE["broth"] = ["U+354f"]
UNICODE_TO_BLISS["U+354f"].append("broth")
BLISS_TO_UNICODE["soup,broth"] = ["U+354f"]
UNICODE_TO_BLISS["U+354f"].append("soup,broth")
BLISS_TO_UNICODE["acid"] = ["U+39e9"]
UNICODE_TO_BLISS["U+39e9"].append("acid")
BLISS_TO_UNICODE["sour"].append("U+39e9")
UNICODE_TO_BLISS["U+39e9"].append("sour")
BLISS_TO_UNICODE["growing"].append("U+37cc")
UNICODE_TO_BLISS["U+37cc"].append("growing")
BLISS_TO_UNICODE["growth,growing"] = ["U+37cc"]
UNICODE_TO_BLISS["U+37cc"].append("growth,growing")
BLISS_TO_UNICODE["reflector"] = ["U+42b6"]
UNICODE_TO_BLISS["U+42b6"] = ["reflector"]
BLISS_TO_UNICODE["predict"] = ["U+42b7"]
UNICODE_TO_BLISS["U+42b7"] = ["predict"]
BLISS_TO_UNICODE["to prophesy"] = ["U+42b8"]
UNICODE_TO_BLISS["U+42b8"] = ["to prophesy"]
BLISS_TO_UNICODE["rathole"] = ["U+42b9"]
UNICODE_TO_BLISS["U+42b9"] = ["rathole"]
BLISS_TO_UNICODE["purr"] = ["U+42ba"]
UNICODE_TO_BLISS["U+42ba"] = ["purr"]
BLISS_TO_UNICODE["psychiatrist"] = ["U+42bb"]
UNICODE_TO_BLISS["U+42bb"] = ["psychiatrist"]
BLISS_TO_UNICODE["allergy"] = ["U+42bc"]
UNICODE_TO_BLISS["U+42bc"] = ["allergy"]
BLISS_TO_UNICODE["hypersensitivity"] = ["U+42bc"]
UNICODE_TO_BLISS["U+42bc"].append("hypersensitivity")
BLISS_TO_UNICODE["allergy,hypersensitivity"] = ["U+42bc"]
UNICODE_TO_BLISS["U+42bc"].append("allergy,hypersensitivity")
BLISS_TO_UNICODE["reaction"] = ["U+42bd"]
UNICODE_TO_BLISS["U+42bd"] = ["reaction"]
BLISS_TO_UNICODE["tile"] = ["U+42be"]
UNICODE_TO_BLISS["U+42be"] = ["tile"]
BLISS_TO_UNICODE["fertility counselling"] = ["U+42bf"]
UNICODE_TO_BLISS["U+42bf"] = ["fertility counselling"]
BLISS_TO_UNICODE["sacrament of marriage"] = ["U+42c0"]
UNICODE_TO_BLISS["U+42c0"] = ["sacrament of marriage"]
BLISS_TO_UNICODE["accessory"] = ["U+42c1"]
UNICODE_TO_BLISS["U+42c1"] = ["accessory"]
BLISS_TO_UNICODE["open one's mouth"] = ["U+42c2"]
UNICODE_TO_BLISS["U+42c2"] = ["open one's mouth"]
BLISS_TO_UNICODE["hold one's mouth open"] = ["U+42c2"]
UNICODE_TO_BLISS["U+42c2"].append("hold one's mouth open")
BLISS_TO_UNICODE["gape"].append("U+42c2")
UNICODE_TO_BLISS["U+42c2"].append("gape")
BLISS_TO_UNICODE["open one's mouth,hold one's mouth open,gape"] = ["U+42c2"]
UNICODE_TO_BLISS["U+42c2"].append("open one's mouth,hold one's mouth open,gape")
BLISS_TO_UNICODE["tablecloth"] = ["U+42c3"]
UNICODE_TO_BLISS["U+42c3"] = ["tablecloth"]
BLISS_TO_UNICODE["jellyfish"] = ["U+42c4"]
UNICODE_TO_BLISS["U+42c4"] = ["jellyfish"]
BLISS_TO_UNICODE["pictograph of jellyfish tentacles"] = ["U+42c5"]
UNICODE_TO_BLISS["U+42c5"] = ["pictograph of jellyfish tentacles"]
BLISS_TO_UNICODE["Christian charity"] = ["U+42c6"]
UNICODE_TO_BLISS["U+42c6"] = ["Christian charity"]
BLISS_TO_UNICODE["pictograph of neck"] = ["U+42c7"]
UNICODE_TO_BLISS["U+42c7"] = ["pictograph of neck"]
BLISS_TO_UNICODE["brick"].append("U+3388")
UNICODE_TO_BLISS["U+3388"].append("brick")
BLISS_TO_UNICODE["block,brick"] = ["U+3388"]
UNICODE_TO_BLISS["U+3388"].append("block,brick")
BLISS_TO_UNICODE["city block"] = ["U+3388"]
UNICODE_TO_BLISS["U+3388"].append("city block")
BLISS_TO_UNICODE["block,city block"] = ["U+3388"]
UNICODE_TO_BLISS["U+3388"].append("block,city block")
BLISS_TO_UNICODE["pillowcase"] = ["U+42c8"]
UNICODE_TO_BLISS["U+42c8"] = ["pillowcase"]
BLISS_TO_UNICODE["shake"] = ["U+42c9"]
UNICODE_TO_BLISS["U+42c9"] = ["shake"]
BLISS_TO_UNICODE["jiggle"] = ["U+42c9"]
UNICODE_TO_BLISS["U+42c9"].append("jiggle")
BLISS_TO_UNICODE["shake,jiggle"] = ["U+42c9"]
UNICODE_TO_BLISS["U+42c9"].append("shake,jiggle")
BLISS_TO_UNICODE["quarter of an hour"] = ["U+42ca"]
UNICODE_TO_BLISS["U+42ca"] = ["quarter of an hour"]
BLISS_TO_UNICODE["15"] = ["U+42cb"]
UNICODE_TO_BLISS["U+42cb"] = ["15"]
BLISS_TO_UNICODE["killer"] = ["U+42cc"]
UNICODE_TO_BLISS["U+42cc"] = ["killer"]
BLISS_TO_UNICODE["murderer"] = ["U+42cc"]
UNICODE_TO_BLISS["U+42cc"].append("murderer")
BLISS_TO_UNICODE["killer,murderer"] = ["U+42cc"]
UNICODE_TO_BLISS["U+42cc"].append("killer,murderer")
BLISS_TO_UNICODE["manslaughter"] = ["U+42cd"]
UNICODE_TO_BLISS["U+42cd"] = ["manslaughter"]
BLISS_TO_UNICODE["lunch"] = ["U+42ce"]
UNICODE_TO_BLISS["U+42ce"] = ["lunch"]
BLISS_TO_UNICODE["dinner"].append("U+42ce")
UNICODE_TO_BLISS["U+42ce"].append("dinner")
BLISS_TO_UNICODE["lunch,dinner"] = ["U+42ce"]
UNICODE_TO_BLISS["U+42ce"].append("lunch,dinner")
BLISS_TO_UNICODE["safari"] = ["U+42cf"]
UNICODE_TO_BLISS["U+42cf"] = ["safari"]
BLISS_TO_UNICODE["wildlife expedition"] = ["U+42cf"]
UNICODE_TO_BLISS["U+42cf"].append("wildlife expedition")
BLISS_TO_UNICODE["safari,wildlife expedition"] = ["U+42cf"]
UNICODE_TO_BLISS["U+42cf"].append("safari,wildlife expedition")
BLISS_TO_UNICODE["sea chart"] = ["U+42d0"]
UNICODE_TO_BLISS["U+42d0"] = ["sea chart"]
BLISS_TO_UNICODE["own"] = ["U+42d1"]
UNICODE_TO_BLISS["U+42d1"] = ["own"]
BLISS_TO_UNICODE["possess"].append("U+42d1")
UNICODE_TO_BLISS["U+42d1"].append("possess")
BLISS_TO_UNICODE["own,possess"] = ["U+42d1"]
UNICODE_TO_BLISS["U+42d1"].append("own,possess")
BLISS_TO_UNICODE["man made"] = ["U+42d2"]
UNICODE_TO_BLISS["U+42d2"] = ["man made"]
BLISS_TO_UNICODE["man-made"].append("U+42d2")
UNICODE_TO_BLISS["U+42d2"].append("man-made")
BLISS_TO_UNICODE["bookshop"] = ["U+42d3"]
UNICODE_TO_BLISS["U+42d3"] = ["bookshop"]
BLISS_TO_UNICODE["combination of sun and earth"] = ["U+42d4"]
UNICODE_TO_BLISS["U+42d4"] = ["combination of sun and earth"]
BLISS_TO_UNICODE["therapy centre"] = ["U+42d5"]
UNICODE_TO_BLISS["U+42d5"] = ["therapy centre"]
BLISS_TO_UNICODE["rehabilitation centre"] = ["U+42d5"]
UNICODE_TO_BLISS["U+42d5"].append("rehabilitation centre")
BLISS_TO_UNICODE["therapy centre,rehabilitation centre"] = ["U+42d5"]
UNICODE_TO_BLISS["U+42d5"].append("therapy centre,rehabilitation centre")
BLISS_TO_UNICODE["resource centre"] = ["U+42d6"]
UNICODE_TO_BLISS["U+42d6"] = ["resource centre"]
BLISS_TO_UNICODE["oere"] = ["U+42d7"]
UNICODE_TO_BLISS["U+42d7"] = ["oere"]
BLISS_TO_UNICODE["monster"] = ["U+42d8"]
UNICODE_TO_BLISS["U+42d8"] = ["monster"]
BLISS_TO_UNICODE["ajar"] = ["U+42d9"]
UNICODE_TO_BLISS["U+42d9"] = ["ajar"]
BLISS_TO_UNICODE["cough"] = ["U+42da"]
UNICODE_TO_BLISS["U+42da"] = ["cough"]
BLISS_TO_UNICODE["to blow"] = ["U+42db"]
UNICODE_TO_BLISS["U+42db"] = ["to blow"]
BLISS_TO_UNICODE["video recorder"] = ["U+42dc"]
UNICODE_TO_BLISS["U+42dc"] = ["video recorder"]
BLISS_TO_UNICODE["blacksmith"] = ["U+42dd"]
UNICODE_TO_BLISS["U+42dd"] = ["blacksmith"]
BLISS_TO_UNICODE["primary"] = ["U+377c"]
UNICODE_TO_BLISS["U+377c"].append("primary")
BLISS_TO_UNICODE["first,primary"] = ["U+377c"]
UNICODE_TO_BLISS["U+377c"].append("first,primary")
BLISS_TO_UNICODE["animal droppings"] = ["U+42de"]
UNICODE_TO_BLISS["U+42de"] = ["animal droppings"]
BLISS_TO_UNICODE["sport shop"] = ["U+42df"]
UNICODE_TO_BLISS["U+42df"] = ["sport shop"]
BLISS_TO_UNICODE["few"] = ["U+42e0"]
UNICODE_TO_BLISS["U+42e0"] = ["few"]
BLISS_TO_UNICODE["little"].append("U+42e0")
UNICODE_TO_BLISS["U+42e0"].append("little")
BLISS_TO_UNICODE["few,little"] = ["U+42e0"]
UNICODE_TO_BLISS["U+42e0"].append("few,little")
BLISS_TO_UNICODE["mermaid"] = ["U+42e1"]
UNICODE_TO_BLISS["U+42e1"] = ["mermaid"]
BLISS_TO_UNICODE["anus"] = ["U+42e2"]
UNICODE_TO_BLISS["U+42e2"] = ["anus"]
BLISS_TO_UNICODE["Nisan"] = ["U+42e3"]
UNICODE_TO_BLISS["U+42e3"] = ["Nisan"]
BLISS_TO_UNICODE["Nissan"] = ["U+42e3"]
UNICODE_TO_BLISS["U+42e3"].append("Nissan")
BLISS_TO_UNICODE["Nisan,Nissan"] = ["U+42e3"]
UNICODE_TO_BLISS["U+42e3"].append("Nisan,Nissan")
BLISS_TO_UNICODE["unleavened bread"] = ["U+42e4"]
UNICODE_TO_BLISS["U+42e4"] = ["unleavened bread"]
BLISS_TO_UNICODE["memo"] = ["U+42e5"]
UNICODE_TO_BLISS["U+42e5"] = ["memo"]
BLISS_TO_UNICODE["reminder note"] = ["U+42e5"]
UNICODE_TO_BLISS["U+42e5"].append("reminder note")
BLISS_TO_UNICODE["memo,reminder note"] = ["U+42e5"]
UNICODE_TO_BLISS["U+42e5"].append("memo,reminder note")
BLISS_TO_UNICODE["exhibition hall"] = ["U+42e6"]
UNICODE_TO_BLISS["U+42e6"] = ["exhibition hall"]
BLISS_TO_UNICODE["showplace"].append("U+42e6")
UNICODE_TO_BLISS["U+42e6"].append("showplace")
BLISS_TO_UNICODE["exhibition hall,showplace"] = ["U+42e6"]
UNICODE_TO_BLISS["U+42e6"].append("exhibition hall,showplace")
BLISS_TO_UNICODE["osteopath"] = ["U+42e7"]
UNICODE_TO_BLISS["U+42e7"] = ["osteopath"]
BLISS_TO_UNICODE["ceramics"] = ["U+42e8"]
UNICODE_TO_BLISS["U+42e8"] = ["ceramics"]
BLISS_TO_UNICODE["pottery"] = ["U+42e8"]
UNICODE_TO_BLISS["U+42e8"].append("pottery")
BLISS_TO_UNICODE["ceramics,pottery"] = ["U+42e8"]
UNICODE_TO_BLISS["U+42e8"].append("ceramics,pottery")
BLISS_TO_UNICODE["sailing"] = ["U+42e9"]
UNICODE_TO_BLISS["U+42e9"] = ["sailing"]
BLISS_TO_UNICODE["sheltered"] = ["U+3d6e"]
UNICODE_TO_BLISS["U+3d6e"].append("sheltered")
BLISS_TO_UNICODE["protected,sheltered"] = ["U+3d6e"]
UNICODE_TO_BLISS["U+3d6e"].append("protected,sheltered")
BLISS_TO_UNICODE["gigantic"] = ["U+42ea"]
UNICODE_TO_BLISS["U+42ea"] = ["gigantic"]
BLISS_TO_UNICODE["lullaby"] = ["U+42eb"]
UNICODE_TO_BLISS["U+42eb"] = ["lullaby"]
BLISS_TO_UNICODE["lick"] = ["U+42ec"]
UNICODE_TO_BLISS["U+42ec"] = ["lick"]
BLISS_TO_UNICODE["piccolo"] = ["U+42ed"]
UNICODE_TO_BLISS["U+42ed"] = ["piccolo"]
BLISS_TO_UNICODE["wind intrument"] = ["U+42ee"]
UNICODE_TO_BLISS["U+42ee"] = ["wind intrument"]
BLISS_TO_UNICODE["direct current"] = ["U+42ef"]
UNICODE_TO_BLISS["U+42ef"] = ["direct current"]
BLISS_TO_UNICODE["DC"] = ["U+42ef"]
UNICODE_TO_BLISS["U+42ef"].append("DC")
BLISS_TO_UNICODE["direct current,DC"] = ["U+42ef"]
UNICODE_TO_BLISS["U+42ef"].append("direct current,DC")
BLISS_TO_UNICODE["silk fabric"] = ["U+42f0"]
UNICODE_TO_BLISS["U+42f0"] = ["silk fabric"]
BLISS_TO_UNICODE["endangered"] = ["U+42f1"]
UNICODE_TO_BLISS["U+42f1"] = ["endangered"]
BLISS_TO_UNICODE["show"] = ["U+3e31"]
UNICODE_TO_BLISS["U+3e31"].append("show")
BLISS_TO_UNICODE["performance,show"] = ["U+3e31"]
UNICODE_TO_BLISS["U+3e31"].append("performance,show")
BLISS_TO_UNICODE["Kazakhstan"] = ["U+42f2"]
UNICODE_TO_BLISS["U+42f2"] = ["Kazakhstan"]
BLISS_TO_UNICODE["chocolate bar"] = ["U+42f3"]
UNICODE_TO_BLISS["U+42f3"] = ["chocolate bar"]
BLISS_TO_UNICODE["zigzag"] = ["U+42f4"]
UNICODE_TO_BLISS["U+42f4"] = ["zigzag"]
BLISS_TO_UNICODE["assault"].append("U+358a")
UNICODE_TO_BLISS["U+358a"].append("assault")
BLISS_TO_UNICODE["violence"].append("U+358a")
UNICODE_TO_BLISS["U+358a"].append("violence")
BLISS_TO_UNICODE["abuse,assault,violence"] = ["U+358a"]
UNICODE_TO_BLISS["U+358a"].append("abuse,assault,violence")
BLISS_TO_UNICODE["halva"] = ["U+42f5"]
UNICODE_TO_BLISS["U+42f5"] = ["halva"]
BLISS_TO_UNICODE["halvah"] = ["U+42f5"]
UNICODE_TO_BLISS["U+42f5"].append("halvah")
BLISS_TO_UNICODE["halwa"] = ["U+42f5"]
UNICODE_TO_BLISS["U+42f5"].append("halwa")
BLISS_TO_UNICODE["halva,halvah,halwa"] = ["U+42f5"]
UNICODE_TO_BLISS["U+42f5"].append("halva,halvah,halwa")
BLISS_TO_UNICODE["pair"] = ["U+42f6"]
UNICODE_TO_BLISS["U+42f6"] = ["pair"]
BLISS_TO_UNICODE["Independence Day"] = ["U+42f7"]
UNICODE_TO_BLISS["U+42f7"] = ["Independence Day"]
BLISS_TO_UNICODE["and also"] = ["U+42f8"]
UNICODE_TO_BLISS["U+42f8"] = ["and also"]
BLISS_TO_UNICODE["shop"] = ["U+373a"]
UNICODE_TO_BLISS["U+373a"].append("shop")
BLISS_TO_UNICODE["store,shop"] = ["U+373a"]
UNICODE_TO_BLISS["U+373a"].append("store,shop")
BLISS_TO_UNICODE["demonstrate"].append("U+3e31")
UNICODE_TO_BLISS["U+3e31"].append("demonstrate")
BLISS_TO_UNICODE["show,demonstrate"] = ["U+3e31"]
UNICODE_TO_BLISS["U+3e31"].append("show,demonstrate")
BLISS_TO_UNICODE["cornea"] = ["U+42f9"]
UNICODE_TO_BLISS["U+42f9"] = ["cornea"]
BLISS_TO_UNICODE["pointer to the right corner"] = ["U+42fa"]
UNICODE_TO_BLISS["U+42fa"] = ["pointer to the right corner"]
BLISS_TO_UNICODE["umbilical cord"] = ["U+42fb"]
UNICODE_TO_BLISS["U+42fb"] = ["umbilical cord"]
BLISS_TO_UNICODE["cards"] = ["U+42fc"]
UNICODE_TO_BLISS["U+42fc"] = ["cards"]
BLISS_TO_UNICODE["playing cards"] = ["U+42fc"]
UNICODE_TO_BLISS["U+42fc"].append("playing cards")
BLISS_TO_UNICODE["cards,playing cards"] = ["U+42fc"]
UNICODE_TO_BLISS["U+42fc"].append("cards,playing cards")
BLISS_TO_UNICODE["hostage"] = ["U+42fd"]
UNICODE_TO_BLISS["U+42fd"] = ["hostage"]
BLISS_TO_UNICODE["hide and seek"] = ["U+42fe"]
UNICODE_TO_BLISS["U+42fe"] = ["hide and seek"]
BLISS_TO_UNICODE["family planning clinic"] = ["U+42ff"]
UNICODE_TO_BLISS["U+42ff"] = ["family planning clinic"]
BLISS_TO_UNICODE["family planning"] = ["U+4300"]
UNICODE_TO_BLISS["U+4300"] = ["family planning"]
BLISS_TO_UNICODE["chiropractor"] = ["U+4301"]
UNICODE_TO_BLISS["U+4301"] = ["chiropractor"]
BLISS_TO_UNICODE["Viking ship"] = ["U+4302"]
UNICODE_TO_BLISS["U+4302"] = ["Viking ship"]
BLISS_TO_UNICODE["viking"] = ["U+4303"]
UNICODE_TO_BLISS["U+4303"] = ["viking"]
BLISS_TO_UNICODE["stupid"] = ["U+4304"]
UNICODE_TO_BLISS["U+4304"] = ["stupid"]
BLISS_TO_UNICODE["dumb"] = ["U+4304"]
UNICODE_TO_BLISS["U+4304"].append("dumb")
BLISS_TO_UNICODE["stupid,dumb"] = ["U+4304"]
UNICODE_TO_BLISS["U+4304"].append("stupid,dumb")
BLISS_TO_UNICODE["fire truck"] = ["U+4305"]
UNICODE_TO_BLISS["U+4305"] = ["fire truck"]
BLISS_TO_UNICODE["fire engine"] = ["U+4305"]
UNICODE_TO_BLISS["U+4305"].append("fire engine")
BLISS_TO_UNICODE["fire truck,fire engine"] = ["U+4305"]
UNICODE_TO_BLISS["U+4305"].append("fire truck,fire engine")
BLISS_TO_UNICODE["sitting"].append("U+36fa")
UNICODE_TO_BLISS["U+36fa"].append("sitting")
BLISS_TO_UNICODE["seat,sitting"] = ["U+36fa"]
UNICODE_TO_BLISS["U+36fa"].append("seat,sitting")
BLISS_TO_UNICODE["relation"].append("U+3403")
UNICODE_TO_BLISS["U+3403"].append("relation")
BLISS_TO_UNICODE["relative,relation"] = ["U+3403"]
UNICODE_TO_BLISS["U+3403"].append("relative,relation")
BLISS_TO_UNICODE["seal"] = ["U+4306"]
UNICODE_TO_BLISS["U+4306"] = ["seal"]
BLISS_TO_UNICODE["water creature with tail"] = ["U+4307"]
UNICODE_TO_BLISS["U+4307"] = ["water creature with tail"]
BLISS_TO_UNICODE["science centre"] = ["U+4308"]
UNICODE_TO_BLISS["U+4308"] = ["science centre"]
BLISS_TO_UNICODE["activity center"] = ["U+4309"]
UNICODE_TO_BLISS["U+4309"] = ["activity center"]
BLISS_TO_UNICODE["calendar"] = ["U+430a"]
UNICODE_TO_BLISS["U+430a"] = ["calendar"]
BLISS_TO_UNICODE["upper body"] = ["U+430b"]
UNICODE_TO_BLISS["U+430b"] = ["upper body"]
BLISS_TO_UNICODE["decoration"] = ["U+430c"]
UNICODE_TO_BLISS["U+430c"] = ["decoration"]
BLISS_TO_UNICODE["ornament"] = ["U+430c"]
UNICODE_TO_BLISS["U+430c"].append("ornament")
BLISS_TO_UNICODE["decoration,ornament"] = ["U+430c"]
UNICODE_TO_BLISS["U+430c"].append("decoration,ornament")
BLISS_TO_UNICODE["pump"] = ["U+430d"]
UNICODE_TO_BLISS["U+430d"] = ["pump"]
BLISS_TO_UNICODE["through"].append("U+3439")
UNICODE_TO_BLISS["U+3439"].append("through")
BLISS_TO_UNICODE["across,through"] = ["U+3439"]
UNICODE_TO_BLISS["U+3439"].append("across,through")
BLISS_TO_UNICODE["a vertical line with two horizontal lines"] = ["U+430e"]
UNICODE_TO_BLISS["U+430e"] = ["a vertical line with two horizontal lines"]
BLISS_TO_UNICODE["car track"] = ["U+430f"]
UNICODE_TO_BLISS["U+430f"] = ["car track"]
BLISS_TO_UNICODE["killing"] = ["U+4310"]
UNICODE_TO_BLISS["U+4310"] = ["killing"]
BLISS_TO_UNICODE["murder"] = ["U+4310"]
UNICODE_TO_BLISS["U+4310"].append("murder")
BLISS_TO_UNICODE["slaughter"].append("U+4310")
UNICODE_TO_BLISS["U+4310"].append("slaughter")
BLISS_TO_UNICODE["killing,murder,slaughter"] = ["U+4310"]
UNICODE_TO_BLISS["U+4310"].append("killing,murder,slaughter")
BLISS_TO_UNICODE["fried"] = ["U+4311"]
UNICODE_TO_BLISS["U+4311"] = ["fried"]
BLISS_TO_UNICODE["rugby"] = ["U+4312"]
UNICODE_TO_BLISS["U+4312"] = ["rugby"]
BLISS_TO_UNICODE["football"].append("U+4312")
UNICODE_TO_BLISS["U+4312"].append("football")
BLISS_TO_UNICODE["rugby,football"] = ["U+4312"]
UNICODE_TO_BLISS["U+4312"].append("rugby,football")
BLISS_TO_UNICODE["rugby ball"] = ["U+4313"]
UNICODE_TO_BLISS["U+4313"] = ["rugby ball"]
BLISS_TO_UNICODE["among"] = ["U+4314"]
UNICODE_TO_BLISS["U+4314"] = ["among"]
BLISS_TO_UNICODE["amongst"] = ["U+4314"]
UNICODE_TO_BLISS["U+4314"].append("amongst")
BLISS_TO_UNICODE["among,amongst"] = ["U+4314"]
UNICODE_TO_BLISS["U+4314"].append("among,amongst")
BLISS_TO_UNICODE["cancer"] = ["U+4315"]
UNICODE_TO_BLISS["U+4315"] = ["cancer"]
BLISS_TO_UNICODE["light meter"] = ["U+4316"]
UNICODE_TO_BLISS["U+4316"] = ["light meter"]
BLISS_TO_UNICODE["mare"] = ["U+4317"]
UNICODE_TO_BLISS["U+4317"] = ["mare"]
BLISS_TO_UNICODE["undershirt"] = ["U+4318"]
UNICODE_TO_BLISS["U+4318"] = ["undershirt"]
BLISS_TO_UNICODE["Good Friday"] = ["U+431a"]
UNICODE_TO_BLISS["U+431a"] = ["Good Friday"]
BLISS_TO_UNICODE["polytheism"] = ["U+431c"]
UNICODE_TO_BLISS["U+431c"] = ["polytheism"]
BLISS_TO_UNICODE["same sound"] = ["U+431d"]
UNICODE_TO_BLISS["U+431d"] = ["same sound"]
BLISS_TO_UNICODE["continuing"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("continuing")
BLISS_TO_UNICODE["ongoing"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("ongoing")
BLISS_TO_UNICODE["still,continuing,ongoing"] = ["U+3a2b"]
UNICODE_TO_BLISS["U+3a2b"].append("still,continuing,ongoing")
BLISS_TO_UNICODE["bear's head"] = ["U+431e"]
UNICODE_TO_BLISS["U+431e"] = ["bear's head"]
BLISS_TO_UNICODE["they"] = ["U+431f"]
UNICODE_TO_BLISS["U+431f"] = ["they"]
BLISS_TO_UNICODE["them"] = ["U+431f"]
UNICODE_TO_BLISS["U+431f"].append("them")
BLISS_TO_UNICODE["themselves"] = ["U+431f"]
UNICODE_TO_BLISS["U+431f"].append("themselves")
BLISS_TO_UNICODE["they,them,themselves"] = ["U+431f"]
UNICODE_TO_BLISS["U+431f"].append("they,them,themselves")
BLISS_TO_UNICODE["centre"].append("U+404c")
UNICODE_TO_BLISS["U+404c"].append("centre")
BLISS_TO_UNICODE["middle,centre"] = ["U+404c"]
UNICODE_TO_BLISS["U+404c"].append("middle,centre")
BLISS_TO_UNICODE["other"].append("U+34c0")
UNICODE_TO_BLISS["U+34c0"].append("other")
BLISS_TO_UNICODE["difference"] = ["U+34c0"]
UNICODE_TO_BLISS["U+34c0"].append("difference")
BLISS_TO_UNICODE["different,other,difference"] = ["U+34c0"]
UNICODE_TO_BLISS["U+34c0"].append("different,other,difference")
BLISS_TO_UNICODE["different,other"] = ["U+34c0"]
UNICODE_TO_BLISS["U+34c0"].append("different,other")
BLISS_TO_UNICODE["synagogue"] = ["U+4320"]
UNICODE_TO_BLISS["U+4320"] = ["synagogue"]
BLISS_TO_UNICODE["spend"] = ["U+371e"]
UNICODE_TO_BLISS["U+371e"].append("spend")
BLISS_TO_UNICODE["pay,spend"] = ["U+371e"]
UNICODE_TO_BLISS["U+371e"].append("pay,spend")
BLISS_TO_UNICODE["pan"].append("U+33b5")
UNICODE_TO_BLISS["U+33b5"].append("pan")
BLISS_TO_UNICODE["pot,pan"] = ["U+33b5"]
UNICODE_TO_BLISS["U+33b5"].append("pot,pan")
BLISS_TO_UNICODE["workplace"] = ["U+4321"]
UNICODE_TO_BLISS["U+4321"] = ["workplace"]
BLISS_TO_UNICODE["caesarean section"] = ["U+4322"]
UNICODE_TO_BLISS["U+4322"] = ["caesarean section"]
BLISS_TO_UNICODE["C section"] = ["U+4322"]
UNICODE_TO_BLISS["U+4322"].append("C section")
BLISS_TO_UNICODE["caesarean section,C-section"] = ["U+4322"]
UNICODE_TO_BLISS["U+4322"].append("caesarean section,C-section")
BLISS_TO_UNICODE["last night"] = ["U+4323"]
UNICODE_TO_BLISS["U+4323"] = ["last night"]
BLISS_TO_UNICODE["running"] = ["U+4324"]
UNICODE_TO_BLISS["U+4324"] = ["running"]
BLISS_TO_UNICODE["cloudberry"] = ["U+4325"]
UNICODE_TO_BLISS["U+4325"] = ["cloudberry"]
BLISS_TO_UNICODE["Heaven"] = ["U+4326"]
UNICODE_TO_BLISS["U+4326"] = ["Heaven"]
BLISS_TO_UNICODE["Kingdom of God"] = ["U+4326"]
UNICODE_TO_BLISS["U+4326"].append("Kingdom of God")
BLISS_TO_UNICODE["Heaven,Kingdom of God"] = ["U+4326"]
UNICODE_TO_BLISS["U+4326"].append("Heaven,Kingdom of God")
BLISS_TO_UNICODE["weave"] = ["U+4327"]
UNICODE_TO_BLISS["U+4327"] = ["weave"]
BLISS_TO_UNICODE["school uniform"] = ["U+4328"]
UNICODE_TO_BLISS["U+4328"] = ["school uniform"]
BLISS_TO_UNICODE["Ramadan"] = ["U+4329"]
UNICODE_TO_BLISS["U+4329"] = ["Ramadan"]
BLISS_TO_UNICODE["solve"] = ["U+432a"]
UNICODE_TO_BLISS["U+432a"] = ["solve"]
BLISS_TO_UNICODE["to answer"] = ["U+432b"]
UNICODE_TO_BLISS["U+432b"] = ["to answer"]
BLISS_TO_UNICODE["allowance"].append("U+35e5")
UNICODE_TO_BLISS["U+35e5"].append("allowance")
BLISS_TO_UNICODE["permission,allowance"] = ["U+35e5"]
UNICODE_TO_BLISS["U+35e5"].append("permission,allowance")
BLISS_TO_UNICODE["anemometer"] = ["U+432c"]
UNICODE_TO_BLISS["U+432c"] = ["anemometer"]
BLISS_TO_UNICODE["cash"] = ["U+328d"]
UNICODE_TO_BLISS["U+328d"].append("cash")
BLISS_TO_UNICODE["money,cash"] = ["U+328d"]
UNICODE_TO_BLISS["U+328d"].append("money,cash")
BLISS_TO_UNICODE["symbol suggests a modified rod of Mercury"] = ["U+432d"]
UNICODE_TO_BLISS["U+432d"] = ["symbol suggests a modified rod of Mercury"]
BLISS_TO_UNICODE[" the traditional symbol for trade and commerce"] = ["U+432e"]
UNICODE_TO_BLISS["U+432e"] = [" the traditional symbol for trade and commerce"]
BLISS_TO_UNICODE["riding school"] = ["U+432f"]
UNICODE_TO_BLISS["U+432f"] = ["riding school"]
BLISS_TO_UNICODE["manege"] = ["U+432f"]
UNICODE_TO_BLISS["U+432f"].append("manege")
BLISS_TO_UNICODE["riding school,manege"] = ["U+432f"]
UNICODE_TO_BLISS["U+432f"].append("riding school,manege")
BLISS_TO_UNICODE["similar looking"] = ["U+4330"]
UNICODE_TO_BLISS["U+4330"] = ["similar looking"]
BLISS_TO_UNICODE["looks similar"] = ["U+4330"]
UNICODE_TO_BLISS["U+4330"].append("looks similar")
BLISS_TO_UNICODE["similar looking,looks similar"] = ["U+4330"]
UNICODE_TO_BLISS["U+4330"].append("similar looking,looks similar")
BLISS_TO_UNICODE["Taurus"] = ["U+4331"]
UNICODE_TO_BLISS["U+4331"] = ["Taurus"]
BLISS_TO_UNICODE["bull"] = ["U+4332"]
UNICODE_TO_BLISS["U+4332"] = ["bull"]
BLISS_TO_UNICODE["tablet"].append("U+3d20")
UNICODE_TO_BLISS["U+3d20"].append("tablet")
BLISS_TO_UNICODE["pill,tablet"] = ["U+3d20"]
UNICODE_TO_BLISS["U+3d20"].append("pill,tablet")
BLISS_TO_UNICODE["go by car"] = ["U+4333"]
UNICODE_TO_BLISS["U+4333"] = ["go by car"]
BLISS_TO_UNICODE["copier"] = ["U+4334"]
UNICODE_TO_BLISS["U+4334"] = ["copier"]
BLISS_TO_UNICODE["photocopier"] = ["U+4334"]
UNICODE_TO_BLISS["U+4334"].append("photocopier")
BLISS_TO_UNICODE["copier,photocopier"] = ["U+4334"]
UNICODE_TO_BLISS["U+4334"].append("copier,photocopier")
BLISS_TO_UNICODE["alcoholic beverage"].append("U+362c")
UNICODE_TO_BLISS["U+362c"].append("alcoholic beverage")
BLISS_TO_UNICODE["liquor"] = ["U+362c"]
UNICODE_TO_BLISS["U+362c"].append("liquor")
BLISS_TO_UNICODE["alcoholic drink,alcoholic beverage,liquor"] = ["U+362c"]
UNICODE_TO_BLISS["U+362c"].append("alcoholic drink,alcoholic beverage,liquor")
BLISS_TO_UNICODE["transverse flute"] = ["U+3e7c"]
UNICODE_TO_BLISS["U+3e7c"].append("transverse flute")
BLISS_TO_UNICODE["flute,transverse flute"] = ["U+3e7c"]
UNICODE_TO_BLISS["U+3e7c"].append("flute,transverse flute")
BLISS_TO_UNICODE["mom"] = ["U+3401"]
UNICODE_TO_BLISS["U+3401"].append("mom")
BLISS_TO_UNICODE["mommy"] = ["U+3401"]
UNICODE_TO_BLISS["U+3401"].append("mommy")
BLISS_TO_UNICODE["mum"] = ["U+3401"]
UNICODE_TO_BLISS["U+3401"].append("mum")
BLISS_TO_UNICODE["mother,mom,mommy,mum"] = ["U+3401"]
UNICODE_TO_BLISS["U+3401"].append("mother,mom,mommy,mum")
BLISS_TO_UNICODE["filled food"] = ["U+4335"]
UNICODE_TO_BLISS["U+4335"] = ["filled food"]
BLISS_TO_UNICODE["stuffed food"] = ["U+4335"]
UNICODE_TO_BLISS["U+4335"].append("stuffed food")
BLISS_TO_UNICODE["filled food,stuffed food"] = ["U+4335"]
UNICODE_TO_BLISS["U+4335"].append("filled food,stuffed food")
BLISS_TO_UNICODE["terrorize"] = ["U+4336"]
UNICODE_TO_BLISS["U+4336"] = ["terrorize"]
BLISS_TO_UNICODE["nosy"] = ["U+4337"]
UNICODE_TO_BLISS["U+4337"] = ["nosy"]
BLISS_TO_UNICODE["doll"] = ["U+4338"]
UNICODE_TO_BLISS["U+4338"] = ["doll"]
BLISS_TO_UNICODE["rise"] = ["U+4339"]
UNICODE_TO_BLISS["U+4339"] = ["rise"]
BLISS_TO_UNICODE["ascend"] = ["U+4339"]
UNICODE_TO_BLISS["U+4339"].append("ascend")
BLISS_TO_UNICODE["go up"] = ["U+4339"]
UNICODE_TO_BLISS["U+4339"].append("go up")
BLISS_TO_UNICODE["rise,ascend,go up"] = ["U+4339"]
UNICODE_TO_BLISS["U+4339"].append("rise,ascend,go up")
BLISS_TO_UNICODE["alternating current"] = ["U+433a"]
UNICODE_TO_BLISS["U+433a"] = ["alternating current"]
BLISS_TO_UNICODE["AC"] = ["U+433a"]
UNICODE_TO_BLISS["U+433a"].append("AC")
BLISS_TO_UNICODE["alternating current,AC"] = ["U+433a"]
UNICODE_TO_BLISS["U+433a"].append("alternating current,AC")
BLISS_TO_UNICODE["pasture"] = ["U+433b"]
UNICODE_TO_BLISS["U+433b"] = ["pasture"]
BLISS_TO_UNICODE["enclosed field"] = ["U+433b"]
UNICODE_TO_BLISS["U+433b"].append("enclosed field")
BLISS_TO_UNICODE["pasture,enclosed field"] = ["U+433b"]
UNICODE_TO_BLISS["U+433b"].append("pasture,enclosed field")
BLISS_TO_UNICODE["put out to pasture"] = ["U+433b"]
UNICODE_TO_BLISS["U+433b"].append("put out to pasture")
BLISS_TO_UNICODE["pasture,put out to pasture"] = ["U+433b"]
UNICODE_TO_BLISS["U+433b"].append("pasture,put out to pasture")
BLISS_TO_UNICODE["organization"] = ["U+433c"]
UNICODE_TO_BLISS["U+433c"] = ["organization"]
BLISS_TO_UNICODE["organizing"] = ["U+433c"]
UNICODE_TO_BLISS["U+433c"].append("organizing")
BLISS_TO_UNICODE["organization,organizing"] = ["U+433c"]
UNICODE_TO_BLISS["U+433c"].append("organization,organizing")
BLISS_TO_UNICODE["too much"] = ["U+433d"]
UNICODE_TO_BLISS["U+433d"] = ["too much"]
BLISS_TO_UNICODE["too many"] = ["U+433d"]
UNICODE_TO_BLISS["U+433d"].append("too many")
BLISS_TO_UNICODE["too much,too many"] = ["U+433d"]
UNICODE_TO_BLISS["U+433d"].append("too much,too many")
BLISS_TO_UNICODE["lotto"] = ["U+433e"]
UNICODE_TO_BLISS["U+433e"] = ["lotto"]
BLISS_TO_UNICODE["bingo"] = ["U+433e"]
UNICODE_TO_BLISS["U+433e"].append("bingo")
BLISS_TO_UNICODE["lotto,bingo"] = ["U+433e"]
UNICODE_TO_BLISS["U+433e"].append("lotto,bingo")
BLISS_TO_UNICODE["raincoat"] = ["U+433f"]
UNICODE_TO_BLISS["U+433f"] = ["raincoat"]
BLISS_TO_UNICODE["broken"] = ["U+4340"]
UNICODE_TO_BLISS["U+4340"] = ["broken"]
BLISS_TO_UNICODE["bird of prey"] = ["U+4341"]
UNICODE_TO_BLISS["U+4341"] = ["bird of prey"]
BLISS_TO_UNICODE["raptor"] = ["U+4341"]
UNICODE_TO_BLISS["U+4341"].append("raptor")
BLISS_TO_UNICODE["bird of prey,raptor"] = ["U+4341"]
UNICODE_TO_BLISS["U+4341"].append("bird of prey,raptor")
BLISS_TO_UNICODE["pictograph of claws"] = ["U+4342"]
UNICODE_TO_BLISS["U+4342"] = ["pictograph of claws"]
BLISS_TO_UNICODE["tease"] = ["U+4343"]
UNICODE_TO_BLISS["U+4343"] = ["tease"]
BLISS_TO_UNICODE["to act"] = ["U+4344"]
UNICODE_TO_BLISS["U+4344"] = ["to act"]
BLISS_TO_UNICODE["roar"] = ["U+4345"]
UNICODE_TO_BLISS["U+4345"] = ["roar"]
BLISS_TO_UNICODE["bug"] = ["U+3466"]
UNICODE_TO_BLISS["U+3466"].append("bug")
BLISS_TO_UNICODE["insect,bug"] = ["U+3466"]
UNICODE_TO_BLISS["U+3466"].append("insect,bug")
BLISS_TO_UNICODE["toothpaste"] = ["U+4346"]
UNICODE_TO_BLISS["U+4346"] = ["toothpaste"]
BLISS_TO_UNICODE["folk music"] = ["U+4347"]
UNICODE_TO_BLISS["U+4347"] = ["folk music"]
BLISS_TO_UNICODE["quietly"] = ["U+3f0d"]
UNICODE_TO_BLISS["U+3f0d"].append("quietly")
BLISS_TO_UNICODE["quiet,quietly"] = ["U+3f0d"]
UNICODE_TO_BLISS["U+3f0d"].append("quiet,quietly")
BLISS_TO_UNICODE["fertile"] = ["U+4348"]
UNICODE_TO_BLISS["U+4348"] = ["fertile"]
BLISS_TO_UNICODE["control oneself"] = ["U+4349"]
UNICODE_TO_BLISS["U+4349"] = ["control oneself"]
BLISS_TO_UNICODE["liquor shop"] = ["U+434a"]
UNICODE_TO_BLISS["U+434a"] = ["liquor shop"]
BLISS_TO_UNICODE["Balder"] = ["U+434b"]
UNICODE_TO_BLISS["U+434b"] = ["Balder"]
BLISS_TO_UNICODE["doll pram"] = ["U+434c"]
UNICODE_TO_BLISS["U+434c"] = ["doll pram"]
BLISS_TO_UNICODE["doll carriage"] = ["U+434c"]
UNICODE_TO_BLISS["U+434c"].append("doll carriage")
BLISS_TO_UNICODE["doll pram,doll carriage"] = ["U+434c"]
UNICODE_TO_BLISS["U+434c"].append("doll pram,doll carriage")
BLISS_TO_UNICODE["trapeze"] = ["U+434f"]
UNICODE_TO_BLISS["U+434f"] = ["trapeze"]
BLISS_TO_UNICODE["acrobatics"] = ["U+4350"]
UNICODE_TO_BLISS["U+4350"] = ["acrobatics"]
BLISS_TO_UNICODE["Moominpappa"] = ["U+4351"]
UNICODE_TO_BLISS["U+4351"] = ["Moominpappa"]
BLISS_TO_UNICODE["baby carriage"] = ["U+4352"]
UNICODE_TO_BLISS["U+4352"] = ["baby carriage"]
BLISS_TO_UNICODE["buggy"] = ["U+4352"]
UNICODE_TO_BLISS["U+4352"].append("buggy")
BLISS_TO_UNICODE["pram"] = ["U+4352"]
UNICODE_TO_BLISS["U+4352"].append("pram")
BLISS_TO_UNICODE["pushchair"] = ["U+4352"]
UNICODE_TO_BLISS["U+4352"].append("pushchair")
BLISS_TO_UNICODE["stroller"] = ["U+4352"]
UNICODE_TO_BLISS["U+4352"].append("stroller")
BLISS_TO_UNICODE["baby carriage,buggy,pram,pushchair,stroller"] = ["U+4352"]
UNICODE_TO_BLISS["U+4352"].append("baby carriage,buggy,pram,pushchair,stroller")
BLISS_TO_UNICODE["God the father"] = ["U+4353"]
UNICODE_TO_BLISS["U+4353"] = ["God the father"]
BLISS_TO_UNICODE["hiccup"] = ["U+4354"]
UNICODE_TO_BLISS["U+4354"] = ["hiccup"]
BLISS_TO_UNICODE["multi storey building"] = ["U+4355"]
UNICODE_TO_BLISS["U+4355"] = ["multi storey building"]
BLISS_TO_UNICODE["walkway"] = ["U+4356"]
UNICODE_TO_BLISS["U+4356"] = ["walkway"]
BLISS_TO_UNICODE["footpath"] = ["U+4356"]
UNICODE_TO_BLISS["U+4356"].append("footpath")
BLISS_TO_UNICODE["walkway,footpath"] = ["U+4356"]
UNICODE_TO_BLISS["U+4356"].append("walkway,footpath")
BLISS_TO_UNICODE["blackbird"] = ["U+4358"]
UNICODE_TO_BLISS["U+4358"] = ["blackbird"]
BLISS_TO_UNICODE["crow"] = ["U+4358"]
UNICODE_TO_BLISS["U+4358"].append("crow")
BLISS_TO_UNICODE["raven"] = ["U+4358"]
UNICODE_TO_BLISS["U+4358"].append("raven")
BLISS_TO_UNICODE["blackbird,crow,raven"] = ["U+4358"]
UNICODE_TO_BLISS["U+4358"].append("blackbird,crow,raven")
BLISS_TO_UNICODE["black)"] = ["U+435a"]
UNICODE_TO_BLISS["U+435a"] = ["black)"]
BLISS_TO_UNICODE["USA"] = ["U+435b"]
UNICODE_TO_BLISS["U+435b"] = ["USA"]
BLISS_TO_UNICODE["rapids"] = ["U+435c"]
UNICODE_TO_BLISS["U+435c"] = ["rapids"]
BLISS_TO_UNICODE["general"] = ["U+435d"]
UNICODE_TO_BLISS["U+435d"] = ["general"]
BLISS_TO_UNICODE["examine"] = ["U+435e"]
UNICODE_TO_BLISS["U+435e"] = ["examine"]
BLISS_TO_UNICODE["girlfriend"] = ["U+435f"]
UNICODE_TO_BLISS["U+435f"] = ["girlfriend"]
BLISS_TO_UNICODE["court"] = ["U+4360"]
UNICODE_TO_BLISS["U+4360"] = ["court"]
BLISS_TO_UNICODE["field"].append("U+4360")
UNICODE_TO_BLISS["U+4360"].append("field")
BLISS_TO_UNICODE["court,field"] = ["U+4360"]
UNICODE_TO_BLISS["U+4360"].append("court,field")
BLISS_TO_UNICODE["beach tennis"] = ["U+4361"]
UNICODE_TO_BLISS["U+4361"] = ["beach tennis"]
BLISS_TO_UNICODE["assessment room"] = ["U+4362"]
UNICODE_TO_BLISS["U+4362"] = ["assessment room"]
BLISS_TO_UNICODE["significant"] = ["U+3cb2"]
UNICODE_TO_BLISS["U+3cb2"].append("significant")
BLISS_TO_UNICODE["important,significant"] = ["U+3cb2"]
UNICODE_TO_BLISS["U+3cb2"].append("important,significant")
BLISS_TO_UNICODE["sneeze"] = ["U+4363"]
UNICODE_TO_BLISS["U+4363"] = ["sneeze"]
BLISS_TO_UNICODE["herring"] = ["U+4364"]
UNICODE_TO_BLISS["U+4364"] = ["herring"]
BLISS_TO_UNICODE["sardine"] = ["U+4364"]
UNICODE_TO_BLISS["U+4364"].append("sardine")
BLISS_TO_UNICODE["herring,sardine"] = ["U+4364"]
UNICODE_TO_BLISS["U+4364"].append("herring,sardine")
BLISS_TO_UNICODE["water play"] = ["U+4365"]
UNICODE_TO_BLISS["U+4365"] = ["water play"]
BLISS_TO_UNICODE["ovary"] = ["U+4366"]
UNICODE_TO_BLISS["U+4366"] = ["ovary"]
BLISS_TO_UNICODE["tuna fish"] = ["U+4367"]
UNICODE_TO_BLISS["U+4367"] = ["tuna fish"]
BLISS_TO_UNICODE["dollar"] = ["U+4368"]
UNICODE_TO_BLISS["U+4368"] = ["dollar"]
BLISS_TO_UNICODE["international symbol for dollar"] = ["U+4369"]
UNICODE_TO_BLISS["U+4369"] = ["international symbol for dollar"]
BLISS_TO_UNICODE["those"] = ["U+436a"]
UNICODE_TO_BLISS["U+436a"] = ["those"]
BLISS_TO_UNICODE["wild strawberry"] = ["U+436b"]
UNICODE_TO_BLISS["U+436b"] = ["wild strawberry"]
BLISS_TO_UNICODE["scout"] = ["U+436c"]
UNICODE_TO_BLISS["U+436c"] = ["scout"]
BLISS_TO_UNICODE["save as"] = ["U+436d"]
UNICODE_TO_BLISS["U+436d"] = ["save as"]
BLISS_TO_UNICODE["washing"].append("U+3681")
UNICODE_TO_BLISS["U+3681"].append("washing")
BLISS_TO_UNICODE["bath,washing"] = ["U+3681"]
UNICODE_TO_BLISS["U+3681"].append("bath,washing")
BLISS_TO_UNICODE["Sivan"] = ["U+436e"]
UNICODE_TO_BLISS["U+436e"] = ["Sivan"]
BLISS_TO_UNICODE["portable"] = ["U+436f"]
UNICODE_TO_BLISS["U+436f"] = ["portable"]
BLISS_TO_UNICODE["grasshopper"] = ["U+4370"]
UNICODE_TO_BLISS["U+4370"] = ["grasshopper"]
BLISS_TO_UNICODE["Arabic numeral 0 small"] = ["U+4371"]
UNICODE_TO_BLISS["U+4371"] = ["Arabic numeral 0 small"]
BLISS_TO_UNICODE["lawyer"] = ["U+4372"]
UNICODE_TO_BLISS["U+4372"] = ["lawyer"]
BLISS_TO_UNICODE["cable car"] = ["U+4373"]
UNICODE_TO_BLISS["U+4373"] = ["cable car"]
BLISS_TO_UNICODE["todefend"] = ["U+4374"]
UNICODE_TO_BLISS["U+4374"] = ["todefend"]
BLISS_TO_UNICODE["public"] = ["U+4375"]
UNICODE_TO_BLISS["U+4375"] = ["public"]
BLISS_TO_UNICODE["motion"].append("U+3cd7")
UNICODE_TO_BLISS["U+3cd7"].append("motion")
BLISS_TO_UNICODE["movement,motion"] = ["U+3cd7"]
UNICODE_TO_BLISS["U+3cd7"].append("movement,motion")
BLISS_TO_UNICODE["this week"] = ["U+4376"]
UNICODE_TO_BLISS["U+4376"] = ["this week"]
BLISS_TO_UNICODE["donkey"] = ["U+4377"]
UNICODE_TO_BLISS["U+4377"] = ["donkey"]
BLISS_TO_UNICODE["mule"] = ["U+4377"]
UNICODE_TO_BLISS["U+4377"].append("mule")
BLISS_TO_UNICODE["donkey,mule"] = ["U+4377"]
UNICODE_TO_BLISS["U+4377"].append("donkey,mule")
BLISS_TO_UNICODE["publisher"] = ["U+4378"]
UNICODE_TO_BLISS["U+4378"] = ["publisher"]
BLISS_TO_UNICODE["search"] = ["U+4379"]
UNICODE_TO_BLISS["U+4379"] = ["search"]
BLISS_TO_UNICODE["to watch"] = ["U+437a"]
UNICODE_TO_BLISS["U+437a"] = ["to watch"]
BLISS_TO_UNICODE["lasagne"] = ["U+437b"]
UNICODE_TO_BLISS["U+437b"] = ["lasagne"]
BLISS_TO_UNICODE["lasagna"] = ["U+437b"]
UNICODE_TO_BLISS["U+437b"].append("lasagna")
BLISS_TO_UNICODE["lasagne,lasagna"] = ["U+437b"]
UNICODE_TO_BLISS["U+437b"].append("lasagne,lasagna")
BLISS_TO_UNICODE["airport"] = ["U+437c"]
UNICODE_TO_BLISS["U+437c"] = ["airport"]
BLISS_TO_UNICODE["voluntary work"] = ["U+437d"]
UNICODE_TO_BLISS["U+437d"] = ["voluntary work"]
BLISS_TO_UNICODE["unpaid work"] = ["U+437d"]
UNICODE_TO_BLISS["U+437d"].append("unpaid work")
BLISS_TO_UNICODE["voluntary work,unpaid work"] = ["U+437d"]
UNICODE_TO_BLISS["U+437d"].append("voluntary work,unpaid work")
BLISS_TO_UNICODE["cowardly"] = ["U+437e"]
UNICODE_TO_BLISS["U+437e"] = ["cowardly"]
BLISS_TO_UNICODE["clapping"] = ["U+39e4"]
UNICODE_TO_BLISS["U+39e4"].append("clapping")
BLISS_TO_UNICODE["applause,clapping"] = ["U+39e4"]
UNICODE_TO_BLISS["U+39e4"].append("applause,clapping")
BLISS_TO_UNICODE["water meter"] = ["U+437f"]
UNICODE_TO_BLISS["U+437f"] = ["water meter"]
BLISS_TO_UNICODE["extinguishing"].append("U+4151")
UNICODE_TO_BLISS["U+4151"].append("extinguishing")
BLISS_TO_UNICODE["extinction,extinguishing"] = ["U+4151"]
UNICODE_TO_BLISS["U+4151"].append("extinction,extinguishing")
BLISS_TO_UNICODE["armed"] = ["U+4380"]
UNICODE_TO_BLISS["U+4380"] = ["armed"]
BLISS_TO_UNICODE["weapon"] = ["U+4381"]
UNICODE_TO_BLISS["U+4381"] = ["weapon"]
BLISS_TO_UNICODE["Europe"] = ["U+4382"]
UNICODE_TO_BLISS["U+4382"] = ["Europe"]
BLISS_TO_UNICODE["lollipop"] = ["U+4383"]
UNICODE_TO_BLISS["U+4383"] = ["lollipop"]
BLISS_TO_UNICODE["sucker"] = ["U+4383"]
UNICODE_TO_BLISS["U+4383"].append("sucker")
BLISS_TO_UNICODE["lollipop,sucker"] = ["U+4383"]
UNICODE_TO_BLISS["U+4383"].append("lollipop,sucker")
BLISS_TO_UNICODE["splash"] = ["U+4384"]
UNICODE_TO_BLISS["U+4384"] = ["splash"]
BLISS_TO_UNICODE["coral reef"] = ["U+4385"]
UNICODE_TO_BLISS["U+4385"] = ["coral reef"]
BLISS_TO_UNICODE["maple syrup flavouring"] = ["U+4386"]
UNICODE_TO_BLISS["U+4386"] = ["maple syrup flavouring"]
BLISS_TO_UNICODE["sap flavouring"] = ["U+4387"]
UNICODE_TO_BLISS["U+4387"] = ["sap flavouring"]
BLISS_TO_UNICODE["nothing"] = ["U+4388"]
UNICODE_TO_BLISS["U+4388"] = ["nothing"]
BLISS_TO_UNICODE["none"] = ["U+4388"]
UNICODE_TO_BLISS["U+4388"].append("none")
BLISS_TO_UNICODE["nothing,none"] = ["U+4388"]
UNICODE_TO_BLISS["U+4388"].append("nothing,none")
BLISS_TO_UNICODE["isosceles triangle"] = ["U+4389"]
UNICODE_TO_BLISS["U+4389"] = ["isosceles triangle"]
BLISS_TO_UNICODE["driving license"] = ["U+438a"]
UNICODE_TO_BLISS["U+438a"] = ["driving license"]
BLISS_TO_UNICODE["den"] = ["U+438b"]
UNICODE_TO_BLISS["U+438b"] = ["den"]
BLISS_TO_UNICODE["lair"] = ["U+438b"]
UNICODE_TO_BLISS["U+438b"].append("lair")
BLISS_TO_UNICODE["den,lair"] = ["U+438b"]
UNICODE_TO_BLISS["U+438b"].append("den,lair")
BLISS_TO_UNICODE["shark"] = ["U+438c"]
UNICODE_TO_BLISS["U+438c"] = ["shark"]
BLISS_TO_UNICODE["ritual"] = ["U+438d"]
UNICODE_TO_BLISS["U+438d"] = ["ritual"]
BLISS_TO_UNICODE["hamburger"] = ["U+438e"]
UNICODE_TO_BLISS["U+438e"] = ["hamburger"]
BLISS_TO_UNICODE["share"] = ["U+438f"]
UNICODE_TO_BLISS["U+438f"] = ["share"]
BLISS_TO_UNICODE["birdhouse"] = ["U+4390"]
UNICODE_TO_BLISS["U+4390"] = ["birdhouse"]
BLISS_TO_UNICODE["house for bird"] = ["U+4390"]
UNICODE_TO_BLISS["U+4390"].append("house for bird")
BLISS_TO_UNICODE["birdhouse,house for bird"] = ["U+4390"]
UNICODE_TO_BLISS["U+4390"].append("birdhouse,house for bird")
BLISS_TO_UNICODE["botanist"] = ["U+4391"]
UNICODE_TO_BLISS["U+4391"] = ["botanist"]
BLISS_TO_UNICODE["botany"] = ["U+4392"]
UNICODE_TO_BLISS["U+4392"] = ["botany"]
BLISS_TO_UNICODE["triathlon"] = ["U+4393"]
UNICODE_TO_BLISS["U+4393"] = ["triathlon"]
BLISS_TO_UNICODE["rye"] = ["U+4394"]
UNICODE_TO_BLISS["U+4394"] = ["rye"]
BLISS_TO_UNICODE["Tyr"] = ["U+4395"]
UNICODE_TO_BLISS["U+4395"] = ["Tyr"]
BLISS_TO_UNICODE["punk rock"] = ["U+4396"]
UNICODE_TO_BLISS["U+4396"] = ["punk rock"]
BLISS_TO_UNICODE["sexual play"] = ["U+4397"]
UNICODE_TO_BLISS["U+4397"] = ["sexual play"]
BLISS_TO_UNICODE["counsel"].append("U+41c3")
UNICODE_TO_BLISS["U+41c3"].append("counsel")
BLISS_TO_UNICODE["recommendation"] = ["U+41c3"]
UNICODE_TO_BLISS["U+41c3"].append("recommendation")
BLISS_TO_UNICODE["advice,counsel,recommendation"] = ["U+41c3"]
UNICODE_TO_BLISS["U+41c3"].append("advice,counsel,recommendation")
BLISS_TO_UNICODE["orchard"] = ["U+4398"]
UNICODE_TO_BLISS["U+4398"] = ["orchard"]
BLISS_TO_UNICODE["mislead"] = ["U+4399"]
UNICODE_TO_BLISS["U+4399"] = ["mislead"]
BLISS_TO_UNICODE["stepparent"] = ["U+439a"]
UNICODE_TO_BLISS["U+439a"] = ["stepparent"]
BLISS_TO_UNICODE["step parent"] = ["U+439a"]
UNICODE_TO_BLISS["U+439a"].append("step parent")
BLISS_TO_UNICODE["stepparent,step-parent"] = ["U+439a"]
UNICODE_TO_BLISS["U+439a"].append("stepparent,step-parent")
BLISS_TO_UNICODE["fun"].append("U+3618")
UNICODE_TO_BLISS["U+3618"].append("fun")
BLISS_TO_UNICODE["joy"].append("U+3618")
UNICODE_TO_BLISS["U+3618"].append("joy")
BLISS_TO_UNICODE["pleasure"].append("U+3618")
UNICODE_TO_BLISS["U+3618"].append("pleasure")
BLISS_TO_UNICODE["happiness,fun,joy,pleasure"] = ["U+3618"]
UNICODE_TO_BLISS["U+3618"].append("happiness,fun,joy,pleasure")
BLISS_TO_UNICODE["Christmas pudding"] = ["U+439b"]
UNICODE_TO_BLISS["U+439b"] = ["Christmas pudding"]
BLISS_TO_UNICODE["New Year's Day"] = ["U+439c"]
UNICODE_TO_BLISS["U+439c"] = ["New Year's Day"]
BLISS_TO_UNICODE["dough"] = ["U+439d"]
UNICODE_TO_BLISS["U+439d"] = ["dough"]
BLISS_TO_UNICODE["flour"] = ["U+439e"]
UNICODE_TO_BLISS["U+439e"] = ["flour"]
BLISS_TO_UNICODE["equal"].append("U+34bf")
UNICODE_TO_BLISS["U+34bf"].append("equal")
BLISS_TO_UNICODE["equality"] = ["U+34bf"]
UNICODE_TO_BLISS["U+34bf"].append("equality")
BLISS_TO_UNICODE["same,equal,equality"] = ["U+34bf"]
UNICODE_TO_BLISS["U+34bf"].append("same,equal,equality")
BLISS_TO_UNICODE["international mathematical symbol"] = ["U+439f"]
UNICODE_TO_BLISS["U+439f"] = ["international mathematical symbol"]
BLISS_TO_UNICODE["same"].append("U+3ad2")
UNICODE_TO_BLISS["U+3ad2"].append("same")
BLISS_TO_UNICODE["equal,same"] = ["U+3ad2"]
UNICODE_TO_BLISS["U+3ad2"].append("equal,same")
BLISS_TO_UNICODE["muskrat"] = ["U+43a0"]
UNICODE_TO_BLISS["U+43a0"] = ["muskrat"]
BLISS_TO_UNICODE["combination of water animal and rodent"] = ["U+43a1"]
UNICODE_TO_BLISS["U+43a1"] = ["combination of water animal and rodent"]
BLISS_TO_UNICODE["late"] = ["U+43a2"]
UNICODE_TO_BLISS["U+43a2"] = ["late"]
BLISS_TO_UNICODE["sexual urge"].append("U+3cff")
UNICODE_TO_BLISS["U+3cff"].append("sexual urge")
BLISS_TO_UNICODE["libido"].append("U+3cff")
UNICODE_TO_BLISS["U+3cff"].append("libido")
BLISS_TO_UNICODE["sex drive,sexual urge,libido"] = ["U+3cff"]
UNICODE_TO_BLISS["U+3cff"].append("sex drive,sexual urge,libido")
BLISS_TO_UNICODE["detach"] = ["U+43a3"]
UNICODE_TO_BLISS["U+43a3"] = ["detach"]
BLISS_TO_UNICODE["take apart"] = ["U+43a3"]
UNICODE_TO_BLISS["U+43a3"].append("take apart")
BLISS_TO_UNICODE["detach,take apart"] = ["U+43a3"]
UNICODE_TO_BLISS["U+43a3"].append("detach,take apart")
BLISS_TO_UNICODE["raise one's hand"] = ["U+43a4"]
UNICODE_TO_BLISS["U+43a4"] = ["raise one's hand"]
BLISS_TO_UNICODE["put up one's hand"] = ["U+43a4"]
UNICODE_TO_BLISS["U+43a4"].append("put up one's hand")
BLISS_TO_UNICODE["raise one's hand,put up one's hand"] = ["U+43a4"]
UNICODE_TO_BLISS["U+43a4"].append("raise one's hand,put up one's hand")
BLISS_TO_UNICODE["show of hands"] = ["U+43a5"]
UNICODE_TO_BLISS["U+43a5"] = ["show of hands"]
BLISS_TO_UNICODE["unknown"].append("U+3c05")
UNICODE_TO_BLISS["U+3c05"].append("unknown")
BLISS_TO_UNICODE["mystery,unknown"] = ["U+3c05"]
UNICODE_TO_BLISS["U+3c05"].append("mystery,unknown")
BLISS_TO_UNICODE["chairlift"] = ["U+43a6"]
UNICODE_TO_BLISS["U+43a6"] = ["chairlift"]
BLISS_TO_UNICODE["pregnant"] = ["U+43a7"]
UNICODE_TO_BLISS["U+43a7"] = ["pregnant"]
BLISS_TO_UNICODE["astarboard"] = ["U+43a8"]
UNICODE_TO_BLISS["U+43a8"] = ["astarboard"]
BLISS_TO_UNICODE["greengrocer"] = ["U+43a9"]
UNICODE_TO_BLISS["U+43a9"] = ["greengrocer"]
BLISS_TO_UNICODE["grave field"] = ["U+43aa"]
UNICODE_TO_BLISS["U+43aa"] = ["grave field"]
BLISS_TO_UNICODE["rabbit"] = ["U+43ab"]
UNICODE_TO_BLISS["U+43ab"] = ["rabbit"]
BLISS_TO_UNICODE["hare"] = ["U+43ab"]
UNICODE_TO_BLISS["U+43ab"].append("hare")
BLISS_TO_UNICODE["rabbit,hare"] = ["U+43ab"]
UNICODE_TO_BLISS["U+43ab"].append("rabbit,hare")
BLISS_TO_UNICODE["hard"].append("U+3576")
UNICODE_TO_BLISS["U+3576"].append("hard")
BLISS_TO_UNICODE["difficult,hard"] = ["U+3576"]
UNICODE_TO_BLISS["U+3576"].append("difficult,hard")
BLISS_TO_UNICODE["difficulty"] = ["U+43ac"]
UNICODE_TO_BLISS["U+43ac"] = ["difficulty"]
BLISS_TO_UNICODE["thought"] = ["U+32ce"]
UNICODE_TO_BLISS["U+32ce"].append("thought")
BLISS_TO_UNICODE["idea,thought"] = ["U+32ce"]
UNICODE_TO_BLISS["U+32ce"].append("idea,thought")
BLISS_TO_UNICODE["lubricant"] = ["U+3207"]
UNICODE_TO_BLISS["U+3207"].append("lubricant")
BLISS_TO_UNICODE["oil,lubricant"] = ["U+3207"]
UNICODE_TO_BLISS["U+3207"].append("oil,lubricant")
BLISS_TO_UNICODE["care manager"] = ["U+43ad"]
UNICODE_TO_BLISS["U+43ad"] = ["care manager"]
BLISS_TO_UNICODE["care plan manager"] = ["U+43ad"]
UNICODE_TO_BLISS["U+43ad"].append("care plan manager")
BLISS_TO_UNICODE["care manager,care plan manager"] = ["U+43ad"]
UNICODE_TO_BLISS["U+43ad"].append("care manager,care plan manager")
BLISS_TO_UNICODE["schoolmate"] = ["U+43ae"]
UNICODE_TO_BLISS["U+43ae"] = ["schoolmate"]
BLISS_TO_UNICODE["harp"] = ["U+43af"]
UNICODE_TO_BLISS["U+43af"] = ["harp"]
BLISS_TO_UNICODE["prepare food"] = ["U+43b0"]
UNICODE_TO_BLISS["U+43b0"] = ["prepare food"]
BLISS_TO_UNICODE["cook"].append("U+43b0")
UNICODE_TO_BLISS["U+43b0"].append("cook")
BLISS_TO_UNICODE["prepare food,cook"] = ["U+43b0"]
UNICODE_TO_BLISS["U+43b0"].append("prepare food,cook")
BLISS_TO_UNICODE["print"] = ["U+43b1"]
UNICODE_TO_BLISS["U+43b1"] = ["print"]
BLISS_TO_UNICODE["value"].append("U+3461")
UNICODE_TO_BLISS["U+3461"].append("value")
BLISS_TO_UNICODE["evaluation,value"] = ["U+3461"]
UNICODE_TO_BLISS["U+3461"].append("evaluation,value")
BLISS_TO_UNICODE["symbol represents a cone balancing unsteadily on its point"] = ["U+43b2"]
UNICODE_TO_BLISS["U+43b2"] = ["symbol represents a cone balancing unsteadily on its point"]
BLISS_TO_UNICODE[" reminding us that our evaluations are variable and unreliable"] = ["U+43b3"]
UNICODE_TO_BLISS["U+43b3"] = [" reminding us that our evaluations are variable and unreliable"]
BLISS_TO_UNICODE["Ukraine"] = ["U+43b4"]
UNICODE_TO_BLISS["U+43b4"] = ["Ukraine"]
BLISS_TO_UNICODE["nice"] = ["U+43b5"]
UNICODE_TO_BLISS["U+43b5"] = ["nice"]
BLISS_TO_UNICODE["pleasant"] = ["U+43b5"]
UNICODE_TO_BLISS["U+43b5"].append("pleasant")
BLISS_TO_UNICODE["nice,pleasant"] = ["U+43b5"]
UNICODE_TO_BLISS["U+43b5"].append("nice,pleasant")
BLISS_TO_UNICODE["prophet"] = ["U+43b7"]
UNICODE_TO_BLISS["U+43b7"] = ["prophet"]
BLISS_TO_UNICODE["corkscrew"] = ["U+43b8"]
UNICODE_TO_BLISS["U+43b8"] = ["corkscrew"]
BLISS_TO_UNICODE["herb sauce"] = ["U+43b9"]
UNICODE_TO_BLISS["U+43b9"] = ["herb sauce"]
BLISS_TO_UNICODE["copper"] = ["U+43ba"]
UNICODE_TO_BLISS["U+43ba"] = ["copper"]
BLISS_TO_UNICODE["shoal"] = ["U+43bb"]
UNICODE_TO_BLISS["U+43bb"] = ["shoal"]
BLISS_TO_UNICODE["school"].append("U+43bb")
UNICODE_TO_BLISS["U+43bb"].append("school")
BLISS_TO_UNICODE["shoal,school"] = ["U+43bb"]
UNICODE_TO_BLISS["U+43bb"].append("shoal,school")
BLISS_TO_UNICODE["divorce"] = ["U+43bc"]
UNICODE_TO_BLISS["U+43bc"] = ["divorce"]
BLISS_TO_UNICODE["hidden treasure"] = ["U+43bd"]
UNICODE_TO_BLISS["U+43bd"] = ["hidden treasure"]
BLISS_TO_UNICODE["treasure trove"] = ["U+43bd"]
UNICODE_TO_BLISS["U+43bd"].append("treasure trove")
BLISS_TO_UNICODE["hidden treasure,treasure trove"] = ["U+43bd"]
UNICODE_TO_BLISS["U+43bd"].append("hidden treasure,treasure trove")
BLISS_TO_UNICODE["jewel"] = ["U+43be"]
UNICODE_TO_BLISS["U+43be"] = ["jewel"]
BLISS_TO_UNICODE["build"] = ["U+43bf"]
UNICODE_TO_BLISS["U+43bf"] = ["build"]
BLISS_TO_UNICODE["construct"] = ["U+43bf"]
UNICODE_TO_BLISS["U+43bf"].append("construct")
BLISS_TO_UNICODE["build,construct"] = ["U+43bf"]
UNICODE_TO_BLISS["U+43bf"].append("build,construct")
BLISS_TO_UNICODE["paint"] = ["U+43c0"]
UNICODE_TO_BLISS["U+43c0"] = ["paint"]
BLISS_TO_UNICODE["dye"] = ["U+43c0"]
UNICODE_TO_BLISS["U+43c0"].append("dye")
BLISS_TO_UNICODE["paint,dye"] = ["U+43c0"]
UNICODE_TO_BLISS["U+43c0"].append("paint,dye")
BLISS_TO_UNICODE["statement"] = ["U+43c1"]
UNICODE_TO_BLISS["U+43c1"] = ["statement"]
BLISS_TO_UNICODE["Belgium"] = ["U+43c2"]
UNICODE_TO_BLISS["U+43c2"] = ["Belgium"]
BLISS_TO_UNICODE["compartment"] = ["U+43c3"]
UNICODE_TO_BLISS["U+43c3"] = ["compartment"]
BLISS_TO_UNICODE["voyeurism"] = ["U+43c4"]
UNICODE_TO_BLISS["U+43c4"] = ["voyeurism"]
BLISS_TO_UNICODE["PEP mask"] = ["U+43c5"]
UNICODE_TO_BLISS["U+43c5"] = ["PEP mask"]
BLISS_TO_UNICODE["breathing aid"] = ["U+43c6"]
UNICODE_TO_BLISS["U+43c6"] = ["breathing aid"]
BLISS_TO_UNICODE["dentist"] = ["U+43c7"]
UNICODE_TO_BLISS["U+43c7"] = ["dentist"]
BLISS_TO_UNICODE["believe"] = ["U+43c9"]
UNICODE_TO_BLISS["U+43c9"] = ["believe"]
BLISS_TO_UNICODE["wind power"] = ["U+43ca"]
UNICODE_TO_BLISS["U+43ca"] = ["wind power"]
BLISS_TO_UNICODE["wind energy"] = ["U+43ca"]
UNICODE_TO_BLISS["U+43ca"].append("wind energy")
BLISS_TO_UNICODE["wind farm"] = ["U+43ca"]
UNICODE_TO_BLISS["U+43ca"].append("wind farm")
BLISS_TO_UNICODE["wind power,wind energy,wind farm"] = ["U+43ca"]
UNICODE_TO_BLISS["U+43ca"].append("wind power,wind energy,wind farm")
BLISS_TO_UNICODE["dancing"].append("U+342d")
UNICODE_TO_BLISS["U+342d"].append("dancing")
BLISS_TO_UNICODE["business)"] = ["U+342d"]
UNICODE_TO_BLISS["U+342d"].append("business)")
BLISS_TO_UNICODE["salmon"] = ["U+43cb"]
UNICODE_TO_BLISS["U+43cb"] = ["salmon"]
BLISS_TO_UNICODE["sanctity of life"] = ["U+43cc"]
UNICODE_TO_BLISS["U+43cc"] = ["sanctity of life"]
BLISS_TO_UNICODE["Christmas tree"] = ["U+43cd"]
UNICODE_TO_BLISS["U+43cd"] = ["Christmas tree"]
BLISS_TO_UNICODE["charm"] = ["U+43ce"]
UNICODE_TO_BLISS["U+43ce"] = ["charm"]
BLISS_TO_UNICODE["refrigerator"] = ["U+43cf"]
UNICODE_TO_BLISS["U+43cf"] = ["refrigerator"]
BLISS_TO_UNICODE["fridge"] = ["U+43cf"]
UNICODE_TO_BLISS["U+43cf"].append("fridge")
BLISS_TO_UNICODE["refrigerator,fridge"] = ["U+43cf"]
UNICODE_TO_BLISS["U+43cf"].append("refrigerator,fridge")
BLISS_TO_UNICODE["Egypt"] = ["U+43d0"]
UNICODE_TO_BLISS["U+43d0"] = ["Egypt"]
BLISS_TO_UNICODE["train station"] = ["U+43d1"]
UNICODE_TO_BLISS["U+43d1"] = ["train station"]
BLISS_TO_UNICODE["Pisces"] = ["U+43d2"]
UNICODE_TO_BLISS["U+43d2"] = ["Pisces"]
BLISS_TO_UNICODE["organism"] = ["U+43d3"]
UNICODE_TO_BLISS["U+43d3"] = ["organism"]
BLISS_TO_UNICODE["sector"].append("U+3da4")
UNICODE_TO_BLISS["U+3da4"].append("sector")
BLISS_TO_UNICODE["circle sector"].append("U+3da4")
UNICODE_TO_BLISS["U+3da4"].append("circle sector")
BLISS_TO_UNICODE["pictograph of pizza divided into pieces"] = ["U+43d4"]
UNICODE_TO_BLISS["U+43d4"] = ["pictograph of pizza divided into pieces"]
BLISS_TO_UNICODE[" a circle divided into circle ectors"] = ["U+43d5"]
UNICODE_TO_BLISS["U+43d5"] = [" a circle divided into circle ectors"]
BLISS_TO_UNICODE["pilot boat"] = ["U+43d6"]
UNICODE_TO_BLISS["U+43d6"] = ["pilot boat"]
BLISS_TO_UNICODE["outdoor"] = ["U+43d7"]
UNICODE_TO_BLISS["U+43d7"] = ["outdoor"]
BLISS_TO_UNICODE["outdoors"] = ["U+43d7"]
UNICODE_TO_BLISS["U+43d7"].append("outdoors")
BLISS_TO_UNICODE["outdoor,outdoors"] = ["U+43d7"]
UNICODE_TO_BLISS["U+43d7"].append("outdoor,outdoors")
BLISS_TO_UNICODE["find"] = ["U+43d8"]
UNICODE_TO_BLISS["U+43d8"] = ["find"]
BLISS_TO_UNICODE["giant"] = ["U+43d9"]
UNICODE_TO_BLISS["U+43d9"] = ["giant"]
BLISS_TO_UNICODE["bandit"] = ["U+43da"]
UNICODE_TO_BLISS["U+43da"] = ["bandit"]
BLISS_TO_UNICODE["armed robber"] = ["U+43da"]
UNICODE_TO_BLISS["U+43da"].append("armed robber")
BLISS_TO_UNICODE["bandit,armed robber"] = ["U+43da"]
UNICODE_TO_BLISS["U+43da"].append("bandit,armed robber")
BLISS_TO_UNICODE["getting"] = ["U+43db"]
UNICODE_TO_BLISS["U+43db"] = ["getting"]
BLISS_TO_UNICODE["8"].append("U+3568")
UNICODE_TO_BLISS["U+3568"].append("8")
BLISS_TO_UNICODE["Arabic numeral 8"] = ["U+43dc"]
UNICODE_TO_BLISS["U+43dc"] = ["Arabic numeral 8"]
BLISS_TO_UNICODE["batter"] = ["U+43dd"]
UNICODE_TO_BLISS["U+43dd"] = ["batter"]
BLISS_TO_UNICODE["smell bad"] = ["U+43de"]
UNICODE_TO_BLISS["U+43de"] = ["smell bad"]
BLISS_TO_UNICODE["stink"] = ["U+43de"]
UNICODE_TO_BLISS["U+43de"].append("stink")
BLISS_TO_UNICODE["smell bad,stink"] = ["U+43de"]
UNICODE_TO_BLISS["U+43de"].append("smell bad,stink")
BLISS_TO_UNICODE["to smell"] = ["U+43df"]
UNICODE_TO_BLISS["U+43df"] = ["to smell"]
BLISS_TO_UNICODE["silk"] = ["U+43e0"]
UNICODE_TO_BLISS["U+43e0"] = ["silk"]
BLISS_TO_UNICODE["TV programme"] = ["U+43e1"]
UNICODE_TO_BLISS["U+43e1"] = ["TV programme"]
BLISS_TO_UNICODE["TV show"] = ["U+43e1"]
UNICODE_TO_BLISS["U+43e1"].append("TV show")
BLISS_TO_UNICODE["radio programme"] = ["U+43e1"]
UNICODE_TO_BLISS["U+43e1"].append("radio programme")
BLISS_TO_UNICODE["TV programme,TV show,radio programme"] = ["U+43e1"]
UNICODE_TO_BLISS["U+43e1"].append("TV programme,TV show,radio programme")
BLISS_TO_UNICODE["infectious"] = ["U+43e2"]
UNICODE_TO_BLISS["U+43e2"] = ["infectious"]
BLISS_TO_UNICODE["contagious"] = ["U+43e2"]
UNICODE_TO_BLISS["U+43e2"].append("contagious")
BLISS_TO_UNICODE["infectious,contagious"] = ["U+43e2"]
UNICODE_TO_BLISS["U+43e2"].append("infectious,contagious")
BLISS_TO_UNICODE["Triceratops"] = ["U+43e4"]
UNICODE_TO_BLISS["U+43e4"] = ["Triceratops"]
BLISS_TO_UNICODE["take away,remove"] = ["U+407d"]
UNICODE_TO_BLISS["U+407d"].append("take away,remove")
BLISS_TO_UNICODE["snorkeling"] = ["U+43e5"]
UNICODE_TO_BLISS["U+43e5"] = ["snorkeling"]
BLISS_TO_UNICODE["scuba diving"] = ["U+43e5"]
UNICODE_TO_BLISS["U+43e5"].append("scuba diving")
BLISS_TO_UNICODE["deep sea diving"] = ["U+43e5"]
UNICODE_TO_BLISS["U+43e5"].append("deep sea diving")
BLISS_TO_UNICODE["snorkeling,scuba diving,deep sea diving"] = ["U+43e5"]
UNICODE_TO_BLISS["U+43e5"].append("snorkeling,scuba diving,deep sea diving")
BLISS_TO_UNICODE["gospel"] = ["U+43e6"]
UNICODE_TO_BLISS["U+43e6"] = ["gospel"]
BLISS_TO_UNICODE["lower arm bone"] = ["U+43e7"]
UNICODE_TO_BLISS["U+43e7"] = ["lower arm bone"]
BLISS_TO_UNICODE["lower arm"] = ["U+43e8"]
UNICODE_TO_BLISS["U+43e8"] = ["lower arm"]
BLISS_TO_UNICODE["burned"] = ["U+43e9"]
UNICODE_TO_BLISS["U+43e9"] = ["burned"]
BLISS_TO_UNICODE["burnt"] = ["U+43e9"]
UNICODE_TO_BLISS["U+43e9"].append("burnt")
BLISS_TO_UNICODE["burned,burnt"] = ["U+43e9"]
UNICODE_TO_BLISS["U+43e9"].append("burned,burnt")
BLISS_TO_UNICODE["sparkling wine"] = ["U+43ea"]
UNICODE_TO_BLISS["U+43ea"] = ["sparkling wine"]
BLISS_TO_UNICODE["restaurant"] = ["U+43eb"]
UNICODE_TO_BLISS["U+43eb"] = ["restaurant"]
BLISS_TO_UNICODE["cafeteria"] = ["U+43eb"]
UNICODE_TO_BLISS["U+43eb"].append("cafeteria")
BLISS_TO_UNICODE["restaurant,cafeteria"] = ["U+43eb"]
UNICODE_TO_BLISS["U+43eb"].append("restaurant,cafeteria")
BLISS_TO_UNICODE["to search"] = ["U+43ec"]
UNICODE_TO_BLISS["U+43ec"] = ["to search"]
BLISS_TO_UNICODE["foreign"] = ["U+43ed"]
UNICODE_TO_BLISS["U+43ed"] = ["foreign"]
BLISS_TO_UNICODE["hard cheese"] = ["U+43ee"]
UNICODE_TO_BLISS["U+43ee"] = ["hard cheese"]
BLISS_TO_UNICODE["misericordia"] = ["U+43ef"]
UNICODE_TO_BLISS["U+43ef"] = ["misericordia"]
BLISS_TO_UNICODE["headmouse"] = ["U+43f0"]
UNICODE_TO_BLISS["U+43f0"] = ["headmouse"]
BLISS_TO_UNICODE["expensive"] = ["U+43f1"]
UNICODE_TO_BLISS["U+43f1"] = ["expensive"]
BLISS_TO_UNICODE["apostle"] = ["U+43f2"]
UNICODE_TO_BLISS["U+43f2"] = ["apostle"]
BLISS_TO_UNICODE["create"] = ["U+43f3"]
UNICODE_TO_BLISS["U+43f3"] = ["create"]
BLISS_TO_UNICODE["Passover"] = ["U+43f4"]
UNICODE_TO_BLISS["U+43f4"] = ["Passover"]
BLISS_TO_UNICODE["encounter"].append("U+38a2")
UNICODE_TO_BLISS["U+38a2"].append("encounter")
BLISS_TO_UNICODE["meeting,encounter"] = ["U+38a2"]
UNICODE_TO_BLISS["U+38a2"].append("meeting,encounter")
BLISS_TO_UNICODE["pictograph of a bubble"] = ["U+43f5"]
UNICODE_TO_BLISS["U+43f5"] = ["pictograph of a bubble"]
BLISS_TO_UNICODE["choke"] = ["U+43f6"]
UNICODE_TO_BLISS["U+43f6"] = ["choke"]
BLISS_TO_UNICODE["gag"] = ["U+43f6"]
UNICODE_TO_BLISS["U+43f6"].append("gag")
BLISS_TO_UNICODE["choke,gag"] = ["U+43f6"]
UNICODE_TO_BLISS["U+43f6"].append("choke,gag")
BLISS_TO_UNICODE["to swallow"] = ["U+43f7"]
UNICODE_TO_BLISS["U+43f7"] = ["to swallow"]
BLISS_TO_UNICODE["pierce"] = ["U+43f8"]
UNICODE_TO_BLISS["U+43f8"] = ["pierce"]
BLISS_TO_UNICODE["politician"] = ["U+43f9"]
UNICODE_TO_BLISS["U+43f9"] = ["politician"]
BLISS_TO_UNICODE["politics"] = ["U+43fa"]
UNICODE_TO_BLISS["U+43fa"] = ["politics"]
BLISS_TO_UNICODE["genocide"] = ["U+43fb"]
UNICODE_TO_BLISS["U+43fb"] = ["genocide"]
BLISS_TO_UNICODE["holocaust"] = ["U+43fb"]
UNICODE_TO_BLISS["U+43fb"].append("holocaust")
BLISS_TO_UNICODE["genocide,holocaust"] = ["U+43fb"]
UNICODE_TO_BLISS["U+43fb"].append("genocide,holocaust")
BLISS_TO_UNICODE["a people"] = ["U+43fc"]
UNICODE_TO_BLISS["U+43fc"] = ["a people"]
BLISS_TO_UNICODE["horseshoe"] = ["U+43fd"]
UNICODE_TO_BLISS["U+43fd"] = ["horseshoe"]
BLISS_TO_UNICODE["remembrance day"] = ["U+43fe"]
UNICODE_TO_BLISS["U+43fe"] = ["remembrance day"]
BLISS_TO_UNICODE["to remember"] = ["U+43ff"]
UNICODE_TO_BLISS["U+43ff"] = ["to remember"]
BLISS_TO_UNICODE["sexuality"] = ["U+4400"]
UNICODE_TO_BLISS["U+4400"] = ["sexuality"]
BLISS_TO_UNICODE["radio"] = ["U+4401"]
UNICODE_TO_BLISS["U+4401"] = ["radio"]
BLISS_TO_UNICODE["century"] = ["U+4402"]
UNICODE_TO_BLISS["U+4402"] = ["century"]
BLISS_TO_UNICODE["100"] = ["U+4403"]
UNICODE_TO_BLISS["U+4403"] = ["100"]
BLISS_TO_UNICODE["breastbone"] = ["U+4404"]
UNICODE_TO_BLISS["U+4404"] = ["breastbone"]
BLISS_TO_UNICODE["sternum"] = ["U+4404"]
UNICODE_TO_BLISS["U+4404"].append("sternum")
BLISS_TO_UNICODE["breastbone,sternum"] = ["U+4404"]
UNICODE_TO_BLISS["U+4404"].append("breastbone,sternum")
BLISS_TO_UNICODE["urethra"] = ["U+4405"]
UNICODE_TO_BLISS["U+4405"] = ["urethra"]
BLISS_TO_UNICODE["sociologist"] = ["U+4406"]
UNICODE_TO_BLISS["U+4406"] = ["sociologist"]
BLISS_TO_UNICODE["medical insurance"] = ["U+4407"]
UNICODE_TO_BLISS["U+4407"] = ["medical insurance"]
BLISS_TO_UNICODE["ewe"] = ["U+4408"]
UNICODE_TO_BLISS["U+4408"] = ["ewe"]
BLISS_TO_UNICODE["itch"] = ["U+4409"]
UNICODE_TO_BLISS["U+4409"] = ["itch"]
BLISS_TO_UNICODE["uncomfortable"] = ["U+440a"]
UNICODE_TO_BLISS["U+440a"] = ["uncomfortable"]
BLISS_TO_UNICODE["leopard"] = ["U+440b"]
UNICODE_TO_BLISS["U+440b"] = ["leopard"]
BLISS_TO_UNICODE["yesterday"] = ["U+440c"]
UNICODE_TO_BLISS["U+440c"] = ["yesterday"]
BLISS_TO_UNICODE["combination of health and muscle"] = ["U+440d"]
UNICODE_TO_BLISS["U+440d"] = ["combination of health and muscle"]
BLISS_TO_UNICODE["lacrosse"] = ["U+440e"]
UNICODE_TO_BLISS["U+440e"] = ["lacrosse"]
BLISS_TO_UNICODE["iron age"] = ["U+4410"]
UNICODE_TO_BLISS["U+4410"] = ["iron age"]
BLISS_TO_UNICODE["sexual pleasure"] = ["U+4411"]
UNICODE_TO_BLISS["U+4411"] = ["sexual pleasure"]
BLISS_TO_UNICODE["cut"] = ["U+4412"]
UNICODE_TO_BLISS["U+4412"] = ["cut"]
BLISS_TO_UNICODE["wound"] = ["U+4413"]
UNICODE_TO_BLISS["U+4413"] = ["wound"]
BLISS_TO_UNICODE["cut"].append("U+4413")
UNICODE_TO_BLISS["U+4413"].append("cut")
BLISS_TO_UNICODE["sore"].append("U+4413")
UNICODE_TO_BLISS["U+4413"].append("sore")
BLISS_TO_UNICODE["wound,cut,sore"] = ["U+4413"]
UNICODE_TO_BLISS["U+4413"].append("wound,cut,sore")
BLISS_TO_UNICODE["cup"] = ["U+33b7"]
UNICODE_TO_BLISS["U+33b7"].append("cup")
BLISS_TO_UNICODE["mug,cup"] = ["U+33b7"]
UNICODE_TO_BLISS["U+33b7"].append("mug,cup")
BLISS_TO_UNICODE["landscape designer"] = ["U+4414"]
UNICODE_TO_BLISS["U+4414"] = ["landscape designer"]
BLISS_TO_UNICODE["stand in"] = ["U+4415"]
UNICODE_TO_BLISS["U+4415"] = ["stand in"]
BLISS_TO_UNICODE["substitute"].append("U+4415")
UNICODE_TO_BLISS["U+4415"].append("substitute")
BLISS_TO_UNICODE["alternate"] = ["U+4415"]
UNICODE_TO_BLISS["U+4415"].append("alternate")
BLISS_TO_UNICODE["stand-in,substitute,alternate"] = ["U+4415"]
UNICODE_TO_BLISS["U+4415"].append("stand-in,substitute,alternate")
BLISS_TO_UNICODE["North Pole"] = ["U+4416"]
UNICODE_TO_BLISS["U+4416"] = ["North Pole"]
BLISS_TO_UNICODE["easter"] = ["U+4417"]
UNICODE_TO_BLISS["U+4417"] = ["easter"]
BLISS_TO_UNICODE["to rise"] = ["U+4418"]
UNICODE_TO_BLISS["U+4418"] = ["to rise"]
BLISS_TO_UNICODE["bib"] = ["U+4419"]
UNICODE_TO_BLISS["U+4419"] = ["bib"]
BLISS_TO_UNICODE["littleness"] = ["U+441a"]
UNICODE_TO_BLISS["U+441a"] = ["littleness"]
BLISS_TO_UNICODE["smallness"] = ["U+441a"]
UNICODE_TO_BLISS["U+441a"].append("smallness")
BLISS_TO_UNICODE["littleness,smallness"] = ["U+441a"]
UNICODE_TO_BLISS["U+441a"].append("littleness,smallness")
BLISS_TO_UNICODE["knock"] = ["U+441c"]
UNICODE_TO_BLISS["U+441c"] = ["knock"]
BLISS_TO_UNICODE["tap"] = ["U+441c"]
UNICODE_TO_BLISS["U+441c"].append("tap")
BLISS_TO_UNICODE["knock,tap"] = ["U+441c"]
UNICODE_TO_BLISS["U+441c"].append("knock,tap")
BLISS_TO_UNICODE["sports glove"] = ["U+441d"]
UNICODE_TO_BLISS["U+441d"] = ["sports glove"]
BLISS_TO_UNICODE["glove"].append("U+441d")
UNICODE_TO_BLISS["U+441d"].append("glove")
BLISS_TO_UNICODE["mitt"].append("U+441d")
UNICODE_TO_BLISS["U+441d"].append("mitt")
BLISS_TO_UNICODE["sports glove,glove,mitt"] = ["U+441d"]
UNICODE_TO_BLISS["U+441d"].append("sports glove,glove,mitt")
BLISS_TO_UNICODE["drilling rig"] = ["U+441e"]
UNICODE_TO_BLISS["U+441e"] = ["drilling rig"]
BLISS_TO_UNICODE["walrus"] = ["U+441f"]
UNICODE_TO_BLISS["U+441f"] = ["walrus"]
BLISS_TO_UNICODE["cheerleader"] = ["U+4420"]
UNICODE_TO_BLISS["U+4420"] = ["cheerleader"]
BLISS_TO_UNICODE["back"].append("U+324e")
UNICODE_TO_BLISS["U+324e"].append("back")
BLISS_TO_UNICODE["backward,back"] = ["U+324e"]
UNICODE_TO_BLISS["U+324e"].append("backward,back")
BLISS_TO_UNICODE["falafel"] = ["U+4421"]
UNICODE_TO_BLISS["U+4421"] = ["falafel"]
BLISS_TO_UNICODE["candle"] = ["U+4422"]
UNICODE_TO_BLISS["U+4422"] = ["candle"]
BLISS_TO_UNICODE["jewellery"] = ["U+3f87"]
UNICODE_TO_BLISS["U+3f87"].append("jewellery")
BLISS_TO_UNICODE["jewelry,jewellery"] = ["U+3f87"]
UNICODE_TO_BLISS["U+3f87"].append("jewelry,jewellery")
BLISS_TO_UNICODE["pet"] = ["U+4423"]
UNICODE_TO_BLISS["U+4423"] = ["pet"]
BLISS_TO_UNICODE["hide"].append("U+3f30")
UNICODE_TO_BLISS["U+3f30"].append("hide")
BLISS_TO_UNICODE["pelt"] = ["U+3f30"]
UNICODE_TO_BLISS["U+3f30"].append("pelt")
BLISS_TO_UNICODE["animal skin,hide,pelt"] = ["U+3f30"]
UNICODE_TO_BLISS["U+3f30"].append("animal skin,hide,pelt")
BLISS_TO_UNICODE["to arrive"] = ["U+4424"]
UNICODE_TO_BLISS["U+4424"] = ["to arrive"]
BLISS_TO_UNICODE["bench"] = ["U+4425"]
UNICODE_TO_BLISS["U+4425"] = ["bench"]
BLISS_TO_UNICODE["pew"] = ["U+4425"]
UNICODE_TO_BLISS["U+4425"].append("pew")
BLISS_TO_UNICODE["bench,pew"] = ["U+4425"]
UNICODE_TO_BLISS["U+4425"].append("bench,pew")
BLISS_TO_UNICODE["cut and paste"] = ["U+4426"]
UNICODE_TO_BLISS["U+4426"] = ["cut and paste"]
BLISS_TO_UNICODE[" pointing forward"] = ["U+4427"]
UNICODE_TO_BLISS["U+4427"] = [" pointing forward"]
BLISS_TO_UNICODE["bandy stick"] = ["U+3954"]
UNICODE_TO_BLISS["U+3954"].append("bandy stick")
BLISS_TO_UNICODE["sport stick and ball,bandy stick"] = ["U+3954"]
UNICODE_TO_BLISS["U+3954"].append("sport stick and ball,bandy stick")
BLISS_TO_UNICODE["patient"] = ["U+4428"]
UNICODE_TO_BLISS["U+4428"] = ["patient"]
BLISS_TO_UNICODE["enduring"] = ["U+4428"]
UNICODE_TO_BLISS["U+4428"].append("enduring")
BLISS_TO_UNICODE["patient,enduring"] = ["U+4428"]
UNICODE_TO_BLISS["U+4428"].append("patient,enduring")
BLISS_TO_UNICODE["patience"] = ["U+4429"]
UNICODE_TO_BLISS["U+4429"] = ["patience"]
BLISS_TO_UNICODE["R"] = ["U+442a"]
UNICODE_TO_BLISS["U+442a"] = ["R"]
BLISS_TO_UNICODE["O"] = ["U+442b"]
UNICODE_TO_BLISS["U+442b"] = ["O"]
BLISS_TO_UNICODE["U"] = ["U+442c"]
UNICODE_TO_BLISS["U+442c"] = ["U"]
BLISS_TO_UNICODE["drama"] = ["U+442d"]
UNICODE_TO_BLISS["U+442d"] = ["drama"]
BLISS_TO_UNICODE["pollution"] = ["U+442e"]
UNICODE_TO_BLISS["U+442e"] = ["pollution"]
BLISS_TO_UNICODE["seat belt"] = ["U+442f"]
UNICODE_TO_BLISS["U+442f"] = ["seat belt"]
BLISS_TO_UNICODE["water skiing"] = ["U+4430"]
UNICODE_TO_BLISS["U+4430"] = ["water skiing"]
BLISS_TO_UNICODE["water ski"] = ["U+4431"]
UNICODE_TO_BLISS["U+4431"] = ["water ski"]
BLISS_TO_UNICODE["lecture"] = ["U+36b9"]
UNICODE_TO_BLISS["U+36b9"].append("lecture")
BLISS_TO_UNICODE["class"].append("U+36b9")
UNICODE_TO_BLISS["U+36b9"].append("class")
BLISS_TO_UNICODE["lesson,lecture,class"] = ["U+36b9"]
UNICODE_TO_BLISS["U+36b9"].append("lesson,lecture,class")
BLISS_TO_UNICODE["to learn"] = ["U+4432"]
UNICODE_TO_BLISS["U+4432"] = ["to learn"]
BLISS_TO_UNICODE["jockey"] = ["U+4433"]
UNICODE_TO_BLISS["U+4433"] = ["jockey"]
BLISS_TO_UNICODE["horse rider"] = ["U+4434"]
UNICODE_TO_BLISS["U+4434"] = ["horse rider"]
BLISS_TO_UNICODE["infected"] = ["U+4435"]
UNICODE_TO_BLISS["U+4435"] = ["infected"]
BLISS_TO_UNICODE["translate"] = ["U+4437"]
UNICODE_TO_BLISS["U+4437"] = ["translate"]
BLISS_TO_UNICODE["Midgard's serpent"] = ["U+4438"]
UNICODE_TO_BLISS["U+4438"] = ["Midgard's serpent"]
BLISS_TO_UNICODE["Cheshvan"] = ["U+4439"]
UNICODE_TO_BLISS["U+4439"] = ["Cheshvan"]
BLISS_TO_UNICODE["garden centre"] = ["U+443a"]
UNICODE_TO_BLISS["U+443a"] = ["garden centre"]
BLISS_TO_UNICODE["cure"] = ["U+443b"]
UNICODE_TO_BLISS["U+443b"] = ["cure"]
BLISS_TO_UNICODE["good"].append("U+391e")
UNICODE_TO_BLISS["U+391e"].append("good")
BLISS_TO_UNICODE["appetizing"] = ["U+391e"]
UNICODE_TO_BLISS["U+391e"].append("appetizing")
BLISS_TO_UNICODE["tasty,good,appetizing"] = ["U+391e"]
UNICODE_TO_BLISS["U+391e"].append("tasty,good,appetizing")
BLISS_TO_UNICODE["curl"] = ["U+3307"]
UNICODE_TO_BLISS["U+3307"].append("curl")
BLISS_TO_UNICODE["spiral,curl"] = ["U+3307"]
UNICODE_TO_BLISS["U+3307"].append("spiral,curl")
BLISS_TO_UNICODE["percent"] = ["U+443c"]
UNICODE_TO_BLISS["U+443c"] = ["percent"]
BLISS_TO_UNICODE["percentage"] = ["U+443c"]
UNICODE_TO_BLISS["U+443c"].append("percentage")
BLISS_TO_UNICODE["%"] = ["U+443c"]
UNICODE_TO_BLISS["U+443c"].append("%")
BLISS_TO_UNICODE["percent,percentage,%"] = ["U+443c"]
UNICODE_TO_BLISS["U+443c"].append("percent,percentage,%")
BLISS_TO_UNICODE["May"] = ["U+443d"]
UNICODE_TO_BLISS["U+443d"] = ["May"]
BLISS_TO_UNICODE["tax"] = ["U+443e"]
UNICODE_TO_BLISS["U+443e"] = ["tax"]
BLISS_TO_UNICODE["regional)"] = ["U+443e"]
UNICODE_TO_BLISS["U+443e"].append("regional)")
BLISS_TO_UNICODE["favourite"] = ["U+443f"]
UNICODE_TO_BLISS["U+443f"] = ["favourite"]
BLISS_TO_UNICODE["tablespoon"] = ["U+4440"]
UNICODE_TO_BLISS["U+4440"] = ["tablespoon"]
BLISS_TO_UNICODE["charming"] = ["U+4441"]
UNICODE_TO_BLISS["U+4441"] = ["charming"]
BLISS_TO_UNICODE["desert"] = ["U+4442"]
UNICODE_TO_BLISS["U+4442"] = ["desert"]
BLISS_TO_UNICODE["day and night"] = ["U+4443"]
UNICODE_TO_BLISS["U+4443"] = ["day and night"]
BLISS_TO_UNICODE["24"] = ["U+4444"]
UNICODE_TO_BLISS["U+4444"] = ["24"]
BLISS_TO_UNICODE["womb"] = ["U+334f"]
UNICODE_TO_BLISS["U+334f"].append("womb")
BLISS_TO_UNICODE["uterus,womb"] = ["U+334f"]
UNICODE_TO_BLISS["U+334f"].append("uterus,womb")
BLISS_TO_UNICODE["give birth"] = ["U+4445"]
UNICODE_TO_BLISS["U+4445"] = ["give birth"]
BLISS_TO_UNICODE["reindeer"] = ["U+4446"]
UNICODE_TO_BLISS["U+4446"] = ["reindeer"]
BLISS_TO_UNICODE["caribou"] = ["U+4446"]
UNICODE_TO_BLISS["U+4446"].append("caribou")
BLISS_TO_UNICODE["reindeer,caribou"] = ["U+4446"]
UNICODE_TO_BLISS["U+4446"].append("reindeer,caribou")
BLISS_TO_UNICODE["Hattifatteners"] = ["U+4447"]
UNICODE_TO_BLISS["U+4447"] = ["Hattifatteners"]
BLISS_TO_UNICODE["amplifier"] = ["U+4448"]
UNICODE_TO_BLISS["U+4448"] = ["amplifier"]
BLISS_TO_UNICODE["midnight sun"] = ["U+4449"]
UNICODE_TO_BLISS["U+4449"] = ["midnight sun"]
BLISS_TO_UNICODE["snowmobile"] = ["U+444a"]
UNICODE_TO_BLISS["U+444a"] = ["snowmobile"]
BLISS_TO_UNICODE["rudder"] = ["U+444b"]
UNICODE_TO_BLISS["U+444b"] = ["rudder"]
BLISS_TO_UNICODE["ingredient"] = ["U+444c"]
UNICODE_TO_BLISS["U+444c"] = ["ingredient"]
BLISS_TO_UNICODE["dessert"] = ["U+444d"]
UNICODE_TO_BLISS["U+444d"] = ["dessert"]
BLISS_TO_UNICODE["rhyme"] = ["U+444e"]
UNICODE_TO_BLISS["U+444e"] = ["rhyme"]
BLISS_TO_UNICODE["accuse"] = ["U+444f"]
UNICODE_TO_BLISS["U+444f"] = ["accuse"]
BLISS_TO_UNICODE["charge"].append("U+444f")
UNICODE_TO_BLISS["U+444f"].append("charge")
BLISS_TO_UNICODE["prosecute"] = ["U+444f"]
UNICODE_TO_BLISS["U+444f"].append("prosecute")
BLISS_TO_UNICODE["surgeon"] = ["U+4450"]
UNICODE_TO_BLISS["U+4450"] = ["surgeon"]
BLISS_TO_UNICODE["challah"] = ["U+4451"]
UNICODE_TO_BLISS["U+4451"] = ["challah"]
BLISS_TO_UNICODE["bun"].append("U+335b")
UNICODE_TO_BLISS["U+335b"].append("bun")
BLISS_TO_UNICODE["roll,bun"] = ["U+335b"]
UNICODE_TO_BLISS["U+335b"].append("roll,bun")
BLISS_TO_UNICODE["roll"].append("U+3db5")
UNICODE_TO_BLISS["U+3db5"].append("roll")
BLISS_TO_UNICODE["scone"] = ["U+3db5"]
UNICODE_TO_BLISS["U+3db5"].append("scone")
BLISS_TO_UNICODE["brioche"] = ["U+3db5"]
UNICODE_TO_BLISS["U+3db5"].append("brioche")
BLISS_TO_UNICODE["wind surfing"] = ["U+4452"]
UNICODE_TO_BLISS["U+4452"] = ["wind surfing"]
BLISS_TO_UNICODE["handicraft shop"] = ["U+4453"]
UNICODE_TO_BLISS["U+4453"] = ["handicraft shop"]
BLISS_TO_UNICODE["Turkey"] = ["U+4454"]
UNICODE_TO_BLISS["U+4454"] = ["Turkey"]
BLISS_TO_UNICODE["Tu Bishvat"] = ["U+4455"]
UNICODE_TO_BLISS["U+4455"] = ["Tu Bishvat"]
BLISS_TO_UNICODE["gas cylinder"] = ["U+4457"]
UNICODE_TO_BLISS["U+4457"] = ["gas cylinder"]
BLISS_TO_UNICODE["Norway"] = ["U+4458"]
UNICODE_TO_BLISS["U+4458"] = ["Norway"]
BLISS_TO_UNICODE["sitski"] = ["U+4459"]
UNICODE_TO_BLISS["U+4459"] = ["sitski"]
BLISS_TO_UNICODE["sit ski"] = ["U+4459"]
UNICODE_TO_BLISS["U+4459"].append("sit ski")
BLISS_TO_UNICODE["sitski,sit ski"] = ["U+4459"]
UNICODE_TO_BLISS["U+4459"].append("sitski,sit ski")
BLISS_TO_UNICODE["gift"].append("U+37ef")
UNICODE_TO_BLISS["U+37ef"].append("gift")
BLISS_TO_UNICODE["giving,gift"] = ["U+37ef"]
UNICODE_TO_BLISS["U+37ef"].append("giving,gift")
BLISS_TO_UNICODE["intrauterine device"] = ["U+445a"]
UNICODE_TO_BLISS["U+445a"] = ["intrauterine device"]
BLISS_TO_UNICODE["IUD"] = ["U+445a"]
UNICODE_TO_BLISS["U+445a"].append("IUD")
BLISS_TO_UNICODE["intrauterine device,IUD"] = ["U+445a"]
UNICODE_TO_BLISS["U+445a"].append("intrauterine device,IUD")
BLISS_TO_UNICODE["oar"].append("U+3757")
UNICODE_TO_BLISS["U+3757"].append("oar")
BLISS_TO_UNICODE["paddle,oar"] = ["U+3757"]
UNICODE_TO_BLISS["U+3757"].append("paddle,oar")
BLISS_TO_UNICODE["access"] = ["U+445b"]
UNICODE_TO_BLISS["U+445b"] = ["access"]
BLISS_TO_UNICODE["hockey helmet"] = ["U+445c"]
UNICODE_TO_BLISS["U+445c"] = ["hockey helmet"]
BLISS_TO_UNICODE["work out"] = ["U+37c0"]
UNICODE_TO_BLISS["U+37c0"].append("work out")
BLISS_TO_UNICODE["exercise,work out"] = ["U+37c0"]
UNICODE_TO_BLISS["U+37c0"].append("exercise,work out")
BLISS_TO_UNICODE["body"].append("U+3d48")
UNICODE_TO_BLISS["U+3d48"].append("body")
BLISS_TO_UNICODE["hull,body"] = ["U+3d48"]
UNICODE_TO_BLISS["U+3d48"].append("hull,body")
BLISS_TO_UNICODE["last week"] = ["U+445d"]
UNICODE_TO_BLISS["U+445d"] = ["last week"]
BLISS_TO_UNICODE["others"] = ["U+445e"]
UNICODE_TO_BLISS["U+445e"] = ["others"]
BLISS_TO_UNICODE["climb"] = ["U+445f"]
UNICODE_TO_BLISS["U+445f"] = ["climb"]
BLISS_TO_UNICODE["nocturnal emission"] = ["U+4460"]
UNICODE_TO_BLISS["U+4460"] = ["nocturnal emission"]
BLISS_TO_UNICODE["wet dream"] = ["U+4460"]
UNICODE_TO_BLISS["U+4460"].append("wet dream")
BLISS_TO_UNICODE["nocturnal emission,wet dream"] = ["U+4460"]
UNICODE_TO_BLISS["U+4460"].append("nocturnal emission,wet dream")
BLISS_TO_UNICODE["ejaculation"] = ["U+4461"]
UNICODE_TO_BLISS["U+4461"] = ["ejaculation"]
BLISS_TO_UNICODE["Valhalla"] = ["U+4462"]
UNICODE_TO_BLISS["U+4462"] = ["Valhalla"]
BLISS_TO_UNICODE["manna"] = ["U+4463"]
UNICODE_TO_BLISS["U+4463"] = ["manna"]
BLISS_TO_UNICODE["trachea"] = ["U+4464"]
UNICODE_TO_BLISS["U+4464"] = ["trachea"]
BLISS_TO_UNICODE["wind pipe"] = ["U+4464"]
UNICODE_TO_BLISS["U+4464"].append("wind pipe")
BLISS_TO_UNICODE["trachea,wind pipe"] = ["U+4464"]
UNICODE_TO_BLISS["U+4464"].append("trachea,wind pipe")
BLISS_TO_UNICODE["private"] = ["U+4465"]
UNICODE_TO_BLISS["U+4465"] = ["private"]
BLISS_TO_UNICODE["to close"] = ["U+4466"]
UNICODE_TO_BLISS["U+4466"] = ["to close"]
BLISS_TO_UNICODE["composer"] = ["U+4467"]
UNICODE_TO_BLISS["U+4467"] = ["composer"]
BLISS_TO_UNICODE["ellipse"] = ["U+40ca"]
UNICODE_TO_BLISS["U+40ca"].append("ellipse")
BLISS_TO_UNICODE["oval,ellipse"] = ["U+40ca"]
UNICODE_TO_BLISS["U+40ca"].append("oval,ellipse")
BLISS_TO_UNICODE["lime"] = ["U+4468"]
UNICODE_TO_BLISS["U+4468"] = ["lime"]
BLISS_TO_UNICODE["blissymbolics resource centre"] = ["U+4469"]
UNICODE_TO_BLISS["U+4469"] = ["blissymbolics resource centre"]
BLISS_TO_UNICODE["thirsty"] = ["U+446a"]
UNICODE_TO_BLISS["U+446a"] = ["thirsty"]
BLISS_TO_UNICODE["orthopaedist"] = ["U+446b"]
UNICODE_TO_BLISS["U+446b"] = ["orthopaedist"]
BLISS_TO_UNICODE["asteroid"] = ["U+446c"]
UNICODE_TO_BLISS["U+446c"] = ["asteroid"]
BLISS_TO_UNICODE["handcraft"] = ["U+446d"]
UNICODE_TO_BLISS["U+446d"] = ["handcraft"]
BLISS_TO_UNICODE["craft"].append("U+446d")
UNICODE_TO_BLISS["U+446d"].append("craft")
BLISS_TO_UNICODE["handcraft,craft"] = ["U+446d"]
UNICODE_TO_BLISS["U+446d"].append("handcraft,craft")
BLISS_TO_UNICODE["harvest"] = ["U+446e"]
UNICODE_TO_BLISS["U+446e"] = ["harvest"]
BLISS_TO_UNICODE["Estonia"] = ["U+446f"]
UNICODE_TO_BLISS["U+446f"] = ["Estonia"]
BLISS_TO_UNICODE["hymnal"] = ["U+4470"]
UNICODE_TO_BLISS["U+4470"] = ["hymnal"]
BLISS_TO_UNICODE["hymn book"] = ["U+4470"]
UNICODE_TO_BLISS["U+4470"].append("hymn book")
BLISS_TO_UNICODE["hymnal,hymn book"] = ["U+4470"]
UNICODE_TO_BLISS["U+4470"].append("hymnal,hymn book")
BLISS_TO_UNICODE["staff"].append("U+3fd2")
UNICODE_TO_BLISS["U+3fd2"].append("staff")
BLISS_TO_UNICODE["stave,staff"] = ["U+3fd2"]
UNICODE_TO_BLISS["U+3fd2"].append("stave,staff")
BLISS_TO_UNICODE["speech recognition"] = ["U+4471"]
UNICODE_TO_BLISS["U+4471"] = ["speech recognition"]
BLISS_TO_UNICODE["two curved arrows mingling"] = ["U+4472"]
UNICODE_TO_BLISS["U+4472"] = ["two curved arrows mingling"]
BLISS_TO_UNICODE["hangar"] = ["U+4473"]
UNICODE_TO_BLISS["U+4473"] = ["hangar"]
BLISS_TO_UNICODE["democracy"] = ["U+4474"]
UNICODE_TO_BLISS["U+4474"] = ["democracy"]
BLISS_TO_UNICODE["to permit"] = ["U+4475"]
UNICODE_TO_BLISS["U+4475"] = ["to permit"]
BLISS_TO_UNICODE["boxing"] = ["U+4476"]
UNICODE_TO_BLISS["U+4476"] = ["boxing"]
BLISS_TO_UNICODE["philosophy"] = ["U+4478"]
UNICODE_TO_BLISS["U+4478"] = ["philosophy"]
BLISS_TO_UNICODE["curtain"] = ["U+4479"]
UNICODE_TO_BLISS["U+4479"] = ["curtain"]
BLISS_TO_UNICODE["drape"] = ["U+4479"]
UNICODE_TO_BLISS["U+4479"].append("drape")
BLISS_TO_UNICODE["linen"] = ["U+447a"]
UNICODE_TO_BLISS["U+447a"] = ["linen"]
BLISS_TO_UNICODE["flax fabric"] = ["U+447a"]
UNICODE_TO_BLISS["U+447a"].append("flax fabric")
BLISS_TO_UNICODE["linen,flax fabric"] = ["U+447a"]
UNICODE_TO_BLISS["U+447a"].append("linen,flax fabric")
BLISS_TO_UNICODE["closeness"].append("U+403f")
UNICODE_TO_BLISS["U+403f"].append("closeness")
BLISS_TO_UNICODE["proximity"] = ["U+403f"]
UNICODE_TO_BLISS["U+403f"].append("proximity")
BLISS_TO_UNICODE["nearness,closeness,proximity"] = ["U+403f"]
UNICODE_TO_BLISS["U+403f"].append("nearness,closeness,proximity")
BLISS_TO_UNICODE["Buddha"] = ["U+447b"]
UNICODE_TO_BLISS["U+447b"] = ["Buddha"]
BLISS_TO_UNICODE["spell"] = ["U+447d"]
UNICODE_TO_BLISS["U+447d"] = ["spell"]
BLISS_TO_UNICODE["prime minister"] = ["U+447e"]
UNICODE_TO_BLISS["U+447e"] = ["prime minister"]
BLISS_TO_UNICODE["courtroom"] = ["U+4360"]
UNICODE_TO_BLISS["U+4360"].append("courtroom")
BLISS_TO_UNICODE["court,courtroom"] = ["U+4360"]
UNICODE_TO_BLISS["U+4360"].append("court,courtroom")
BLISS_TO_UNICODE["cider"] = ["U+447f"]
UNICODE_TO_BLISS["U+447f"] = ["cider"]
BLISS_TO_UNICODE["musical group"] = ["U+4480"]
UNICODE_TO_BLISS["U+4480"] = ["musical group"]
BLISS_TO_UNICODE["be patient"] = ["U+4481"]
UNICODE_TO_BLISS["U+4481"] = ["be patient"]
BLISS_TO_UNICODE["China"] = ["U+4482"]
UNICODE_TO_BLISS["U+4482"] = ["China"]
BLISS_TO_UNICODE["barley"] = ["U+4483"]
UNICODE_TO_BLISS["U+4483"] = ["barley"]
BLISS_TO_UNICODE["straw"] = ["U+4484"]
UNICODE_TO_BLISS["U+4484"] = ["straw"]
BLISS_TO_UNICODE["amuse"] = ["U+4485"]
UNICODE_TO_BLISS["U+4485"] = ["amuse"]
BLISS_TO_UNICODE["entertain"] = ["U+4485"]
UNICODE_TO_BLISS["U+4485"].append("entertain")
BLISS_TO_UNICODE["please"].append("U+4485")
UNICODE_TO_BLISS["U+4485"].append("please")
BLISS_TO_UNICODE["amuse,entertain,please"] = ["U+4485"]
UNICODE_TO_BLISS["U+4485"].append("amuse,entertain,please")
BLISS_TO_UNICODE["bleed"] = ["U+4486"]
UNICODE_TO_BLISS["U+4486"] = ["bleed"]
BLISS_TO_UNICODE["eyebrow pencil"] = ["U+4488"]
UNICODE_TO_BLISS["U+4488"] = ["eyebrow pencil"]
BLISS_TO_UNICODE["mortal"] = ["U+4489"]
UNICODE_TO_BLISS["U+4489"] = ["mortal"]
BLISS_TO_UNICODE["workbook"] = ["U+448a"]
UNICODE_TO_BLISS["U+448a"] = ["workbook"]
BLISS_TO_UNICODE["embarrassed"] = ["U+448b"]
UNICODE_TO_BLISS["U+448b"] = ["embarrassed"]
BLISS_TO_UNICODE["embarrassment"] = ["U+448c"]
UNICODE_TO_BLISS["U+448c"] = ["embarrassment"]
BLISS_TO_UNICODE["puppet"] = ["U+448d"]
UNICODE_TO_BLISS["U+448d"] = ["puppet"]
BLISS_TO_UNICODE["therapeutic riding"] = ["U+448e"]
UNICODE_TO_BLISS["U+448e"] = ["therapeutic riding"]
BLISS_TO_UNICODE["oesophagus"] = ["U+448f"]
UNICODE_TO_BLISS["U+448f"] = ["oesophagus"]
BLISS_TO_UNICODE["gullet"] = ["U+448f"]
UNICODE_TO_BLISS["U+448f"].append("gullet")
BLISS_TO_UNICODE["oesophagus,gullet"] = ["U+448f"]
UNICODE_TO_BLISS["U+448f"].append("oesophagus,gullet")
BLISS_TO_UNICODE["unending"] = ["U+4490"]
UNICODE_TO_BLISS["U+4490"] = ["unending"]
BLISS_TO_UNICODE["prune"] = ["U+4491"]
UNICODE_TO_BLISS["U+4491"] = ["prune"]
BLISS_TO_UNICODE["shampoo"] = ["U+4492"]
UNICODE_TO_BLISS["U+4492"] = ["shampoo"]
BLISS_TO_UNICODE["amplitude"] = ["U+4493"]
UNICODE_TO_BLISS["U+4493"] = ["amplitude"]
BLISS_TO_UNICODE["anthropologist"] = ["U+4494"]
UNICODE_TO_BLISS["U+4494"] = ["anthropologist"]
BLISS_TO_UNICODE["swim centre"] = ["U+4495"]
UNICODE_TO_BLISS["U+4495"] = ["swim centre"]
BLISS_TO_UNICODE["bisexual"] = ["U+4496"]
UNICODE_TO_BLISS["U+4496"] = ["bisexual"]
BLISS_TO_UNICODE["bisexuality"] = ["U+4497"]
UNICODE_TO_BLISS["U+4497"] = ["bisexuality"]
BLISS_TO_UNICODE["comfortable"] = ["U+4498"]
UNICODE_TO_BLISS["U+4498"] = ["comfortable"]
BLISS_TO_UNICODE["restful"] = ["U+4498"]
UNICODE_TO_BLISS["U+4498"].append("restful")
BLISS_TO_UNICODE["comfortable,restful"] = ["U+4498"]
UNICODE_TO_BLISS["U+4498"].append("comfortable,restful")
BLISS_TO_UNICODE["rough sea"] = ["U+4499"]
UNICODE_TO_BLISS["U+4499"] = ["rough sea"]
BLISS_TO_UNICODE["have"] = ["U+449a"]
UNICODE_TO_BLISS["U+449a"] = ["have"]
BLISS_TO_UNICODE["sidecar"] = ["U+449b"]
UNICODE_TO_BLISS["U+449b"] = ["sidecar"]
BLISS_TO_UNICODE["side car"] = ["U+449c"]
UNICODE_TO_BLISS["U+449c"] = ["side car"]
BLISS_TO_UNICODE["billiards"] = ["U+449d"]
UNICODE_TO_BLISS["U+449d"] = ["billiards"]
BLISS_TO_UNICODE["unless"] = ["U+449e"]
UNICODE_TO_BLISS["U+449e"] = ["unless"]
BLISS_TO_UNICODE["great experience"] = ["U+449f"]
UNICODE_TO_BLISS["U+449f"] = ["great experience"]
BLISS_TO_UNICODE["Arabic numeral 8 small"] = ["U+44a0"]
UNICODE_TO_BLISS["U+44a0"] = ["Arabic numeral 8 small"]
BLISS_TO_UNICODE["prisoner"] = ["U+44a1"]
UNICODE_TO_BLISS["U+44a1"] = ["prisoner"]
BLISS_TO_UNICODE["occupational therapist"] = ["U+44a2"]
UNICODE_TO_BLISS["U+44a2"] = ["occupational therapist"]
BLISS_TO_UNICODE["request"] = ["U+44a3"]
UNICODE_TO_BLISS["U+44a3"] = ["request"]
BLISS_TO_UNICODE["switch on"] = ["U+44a4"]
UNICODE_TO_BLISS["U+44a4"] = ["switch on"]
BLISS_TO_UNICODE["turn on"] = ["U+44a4"]
UNICODE_TO_BLISS["U+44a4"].append("turn on")
BLISS_TO_UNICODE["switch on,turn on"] = ["U+44a4"]
UNICODE_TO_BLISS["U+44a4"].append("switch on,turn on")
BLISS_TO_UNICODE["Saturday"] = ["U+44a5"]
UNICODE_TO_BLISS["U+44a5"] = ["Saturday"]
BLISS_TO_UNICODE["birdfeeder"] = ["U+44a6"]
UNICODE_TO_BLISS["U+44a6"] = ["birdfeeder"]
BLISS_TO_UNICODE["bird table"] = ["U+44a6"]
UNICODE_TO_BLISS["U+44a6"].append("bird table")
BLISS_TO_UNICODE["birdfeeder,bird table"] = ["U+44a6"]
UNICODE_TO_BLISS["U+44a6"].append("birdfeeder,bird table")
BLISS_TO_UNICODE["to serve"] = ["U+44a7"]
UNICODE_TO_BLISS["U+44a7"] = ["to serve"]
BLISS_TO_UNICODE["class"].append("U+32d6")
UNICODE_TO_BLISS["U+32d6"].append("class")
BLISS_TO_UNICODE["knowledge,class"] = ["U+32d6"]
UNICODE_TO_BLISS["U+32d6"].append("knowledge,class")
BLISS_TO_UNICODE["combination of mind and enclosure"] = ["U+44a8"]
UNICODE_TO_BLISS["U+44a8"] = ["combination of mind and enclosure"]
BLISS_TO_UNICODE["to puncture"] = ["U+44a9"]
UNICODE_TO_BLISS["U+44a9"] = ["to puncture"]
BLISS_TO_UNICODE["medication for breathing"] = ["U+44aa"]
UNICODE_TO_BLISS["U+44aa"] = ["medication for breathing"]
BLISS_TO_UNICODE["reaching aid"] = ["U+44ab"]
UNICODE_TO_BLISS["U+44ab"] = ["reaching aid"]
BLISS_TO_UNICODE["grabber"] = ["U+44ab"]
UNICODE_TO_BLISS["U+44ab"].append("grabber")
BLISS_TO_UNICODE["reaching aid,grabber"] = ["U+44ab"]
UNICODE_TO_BLISS["U+44ab"].append("reaching aid,grabber")
BLISS_TO_UNICODE["to bring"] = ["U+44ac"]
UNICODE_TO_BLISS["U+44ac"] = ["to bring"]
BLISS_TO_UNICODE["hearing aid"] = ["U+44ad"]
UNICODE_TO_BLISS["U+44ad"] = ["hearing aid"]
BLISS_TO_UNICODE["below"].append("U+3492")
UNICODE_TO_BLISS["U+3492"].append("below")
BLISS_TO_UNICODE["inferior"].append("U+3492")
UNICODE_TO_BLISS["U+3492"].append("inferior")
BLISS_TO_UNICODE["under,below,inferior"] = ["U+3492"]
UNICODE_TO_BLISS["U+3492"].append("under,below,inferior")
BLISS_TO_UNICODE["spermicide"] = ["U+44ae"]
UNICODE_TO_BLISS["U+44ae"] = ["spermicide"]
BLISS_TO_UNICODE["sperm destruction"] = ["U+44af"]
UNICODE_TO_BLISS["U+44af"] = ["sperm destruction"]
BLISS_TO_UNICODE["Finnish"] = ["U+44b0"]
UNICODE_TO_BLISS["U+44b0"] = ["Finnish"]
BLISS_TO_UNICODE["dental floss"] = ["U+44b2"]
UNICODE_TO_BLISS["U+44b2"] = ["dental floss"]
BLISS_TO_UNICODE["striped"] = ["U+44b3"]
UNICODE_TO_BLISS["U+44b3"] = ["striped"]
BLISS_TO_UNICODE["ashtray"] = ["U+44b4"]
UNICODE_TO_BLISS["U+44b4"] = ["ashtray"]
BLISS_TO_UNICODE["body part"] = ["U+44b5"]
UNICODE_TO_BLISS["U+44b5"] = ["body part"]
BLISS_TO_UNICODE["shot put"] = ["U+44b6"]
UNICODE_TO_BLISS["U+44b6"] = ["shot put"]
BLISS_TO_UNICODE["binoculars"] = ["U+44b7"]
UNICODE_TO_BLISS["U+44b7"] = ["binoculars"]
BLISS_TO_UNICODE["field glass"] = ["U+44b7"]
UNICODE_TO_BLISS["U+44b7"].append("field glass")
BLISS_TO_UNICODE["binoculars,field glass"] = ["U+44b7"]
UNICODE_TO_BLISS["U+44b7"].append("binoculars,field glass")
BLISS_TO_UNICODE["yearning"].append("U+38c3")
UNICODE_TO_BLISS["U+38c3"].append("yearning")
BLISS_TO_UNICODE["longing,yearning"] = ["U+38c3"]
UNICODE_TO_BLISS["U+38c3"].append("longing,yearning")
BLISS_TO_UNICODE["water polo"] = ["U+44b8"]
UNICODE_TO_BLISS["U+44b8"] = ["water polo"]
BLISS_TO_UNICODE["Pluto"] = ["U+44b9"]
UNICODE_TO_BLISS["U+44b9"] = ["Pluto"]
BLISS_TO_UNICODE["dwarf planet ice"] = ["U+44ba"]
UNICODE_TO_BLISS["U+44ba"] = ["dwarf planet ice"]
BLISS_TO_UNICODE["hammock"] = ["U+44bb"]
UNICODE_TO_BLISS["U+44bb"] = ["hammock"]
BLISS_TO_UNICODE["July"] = ["U+44bc"]
UNICODE_TO_BLISS["U+44bc"] = ["July"]
BLISS_TO_UNICODE["respect"] = ["U+44bd"]
UNICODE_TO_BLISS["U+44bd"] = ["respect"]
BLISS_TO_UNICODE["admiration"] = ["U+44bd"]
UNICODE_TO_BLISS["U+44bd"].append("admiration")
BLISS_TO_UNICODE["respect,admiration"] = ["U+44bd"]
UNICODE_TO_BLISS["U+44bd"].append("respect,admiration")
BLISS_TO_UNICODE["cauliflower"] = ["U+44be"]
UNICODE_TO_BLISS["U+44be"] = ["cauliflower"]
BLISS_TO_UNICODE["monarchy"] = ["U+44bf"]
UNICODE_TO_BLISS["U+44bf"] = ["monarchy"]
BLISS_TO_UNICODE["four o'clock eating break"] = ["U+44c0"]
UNICODE_TO_BLISS["U+44c0"] = ["four o'clock eating break"]
BLISS_TO_UNICODE["empathy"] = ["U+44c1"]
UNICODE_TO_BLISS["U+44c1"] = ["empathy"]
BLISS_TO_UNICODE["joke"] = ["U+44c2"]
UNICODE_TO_BLISS["U+44c2"] = ["joke"]
BLISS_TO_UNICODE["swallow"] = ["U+44c3"]
UNICODE_TO_BLISS["U+44c3"] = ["swallow"]
BLISS_TO_UNICODE["laughter"].append("U+3b85")
UNICODE_TO_BLISS["U+3b85"].append("laughter")
BLISS_TO_UNICODE["laugh,laughter"] = ["U+3b85"]
UNICODE_TO_BLISS["U+3b85"].append("laugh,laughter")
BLISS_TO_UNICODE["memory game"] = ["U+44c4"]
UNICODE_TO_BLISS["U+44c4"] = ["memory game"]
BLISS_TO_UNICODE["Kim's game"] = ["U+44c4"]
UNICODE_TO_BLISS["U+44c4"].append("Kim's game")
BLISS_TO_UNICODE["memory game,Kim's game"] = ["U+44c4"]
UNICODE_TO_BLISS["U+44c4"].append("memory game,Kim's game")
BLISS_TO_UNICODE["moadan"] = ["U+4018"]
UNICODE_TO_BLISS["U+4018"].append("moadan")
BLISS_TO_UNICODE["recreation room,moadan"] = ["U+4018"]
UNICODE_TO_BLISS["U+4018"].append("recreation room,moadan")
BLISS_TO_UNICODE["teamwork"] = ["U+44c5"]
UNICODE_TO_BLISS["U+44c5"] = ["teamwork"]
BLISS_TO_UNICODE["volunteer"] = ["U+44c6"]
UNICODE_TO_BLISS["U+44c6"] = ["volunteer"]
BLISS_TO_UNICODE["next week"] = ["U+44c7"]
UNICODE_TO_BLISS["U+44c7"] = ["next week"]
BLISS_TO_UNICODE["holy event"] = ["U+44c8"]
UNICODE_TO_BLISS["U+44c8"] = ["holy event"]
BLISS_TO_UNICODE["table sports"] = ["U+44c9"]
UNICODE_TO_BLISS["U+44c9"] = ["table sports"]
BLISS_TO_UNICODE["handwriting"] = ["U+44ca"]
UNICODE_TO_BLISS["U+44ca"] = ["handwriting"]
BLISS_TO_UNICODE["penmanship"] = ["U+44ca"]
UNICODE_TO_BLISS["U+44ca"].append("penmanship")
BLISS_TO_UNICODE["handwriting,penmanship"] = ["U+44ca"]
UNICODE_TO_BLISS["U+44ca"].append("handwriting,penmanship")
BLISS_TO_UNICODE["Haggadah"] = ["U+44cb"]
UNICODE_TO_BLISS["U+44cb"] = ["Haggadah"]
BLISS_TO_UNICODE["father in law"] = ["U+44cc"]
UNICODE_TO_BLISS["U+44cc"] = ["father in law"]
BLISS_TO_UNICODE["father-in-law"] = ["U+44cc"]
UNICODE_TO_BLISS["U+44cc"].append("father-in-law")
BLISS_TO_UNICODE["dot is repeated"] = ["U+44cd"]
UNICODE_TO_BLISS["U+44cd"] = ["dot is repeated"]
BLISS_TO_UNICODE["Moominmamma"] = ["U+44ce"]
UNICODE_TO_BLISS["U+44ce"] = ["Moominmamma"]
BLISS_TO_UNICODE["downward curving arrow"] = ["U+44cf"]
UNICODE_TO_BLISS["U+44cf"] = ["downward curving arrow"]
BLISS_TO_UNICODE["sunburn"] = ["U+44d0"]
UNICODE_TO_BLISS["U+44d0"] = ["sunburn"]
BLISS_TO_UNICODE["slice of bread"] = ["U+44d1"]
UNICODE_TO_BLISS["U+44d1"] = ["slice of bread"]
BLISS_TO_UNICODE["bread slice"] = ["U+44d1"]
UNICODE_TO_BLISS["U+44d1"].append("bread slice")
BLISS_TO_UNICODE["slice of bread,bread slice"] = ["U+44d1"]
UNICODE_TO_BLISS["U+44d1"].append("slice of bread,bread slice")
BLISS_TO_UNICODE["the pictograph of a protruding biceps"] = ["U+44d2"]
UNICODE_TO_BLISS["U+44d2"] = ["the pictograph of a protruding biceps"]
BLISS_TO_UNICODE["domestic"] = ["U+44d3"]
UNICODE_TO_BLISS["U+44d3"] = ["domestic"]
BLISS_TO_UNICODE["clinic"] = ["U+44d4"]
UNICODE_TO_BLISS["U+44d4"] = ["clinic"]
BLISS_TO_UNICODE["hospital"] = ["U+44d5"]
UNICODE_TO_BLISS["U+44d5"] = ["hospital"]
BLISS_TO_UNICODE["clinic"].append("U+44d5")
UNICODE_TO_BLISS["U+44d5"].append("clinic")
BLISS_TO_UNICODE["hospital,clinic"] = ["U+44d5"]
UNICODE_TO_BLISS["U+44d5"].append("hospital,clinic")
BLISS_TO_UNICODE["brush teeth"] = ["U+44d6"]
UNICODE_TO_BLISS["U+44d6"] = ["brush teeth"]
BLISS_TO_UNICODE["toothbrush"] = ["U+44d7"]
UNICODE_TO_BLISS["U+44d7"] = ["toothbrush"]
BLISS_TO_UNICODE["Friday"] = ["U+44d8"]
UNICODE_TO_BLISS["U+44d8"] = ["Friday"]
BLISS_TO_UNICODE["lake"] = ["U+44d9"]
UNICODE_TO_BLISS["U+44d9"] = ["lake"]
BLISS_TO_UNICODE["pond"] = ["U+44d9"]
UNICODE_TO_BLISS["U+44d9"].append("pond")
BLISS_TO_UNICODE["lake,pond"] = ["U+44d9"]
UNICODE_TO_BLISS["U+44d9"].append("lake,pond")
BLISS_TO_UNICODE["bobsleigh"] = ["U+44da"]
UNICODE_TO_BLISS["U+44da"] = ["bobsleigh"]
BLISS_TO_UNICODE["match"] = ["U+44db"]
UNICODE_TO_BLISS["U+44db"] = ["match"]
BLISS_TO_UNICODE["thread"] = ["U+44dd"]
UNICODE_TO_BLISS["U+44dd"] = ["thread"]
BLISS_TO_UNICODE["string"].append("U+44dd")
UNICODE_TO_BLISS["U+44dd"].append("string")
BLISS_TO_UNICODE["cord"].append("U+44dd")
UNICODE_TO_BLISS["U+44dd"].append("cord")
BLISS_TO_UNICODE["thread,string,cord"] = ["U+44dd"]
UNICODE_TO_BLISS["U+44dd"].append("thread,string,cord")
BLISS_TO_UNICODE["enter"] = ["U+44de"]
UNICODE_TO_BLISS["U+44de"] = ["enter"]
BLISS_TO_UNICODE["absorb"] = ["U+44de"]
UNICODE_TO_BLISS["U+44de"].append("absorb")
BLISS_TO_UNICODE["insert"] = ["U+44de"]
UNICODE_TO_BLISS["U+44de"].append("insert")
BLISS_TO_UNICODE["penetrate"] = ["U+44de"]
UNICODE_TO_BLISS["U+44de"].append("penetrate")
BLISS_TO_UNICODE["enter,absorb,insert,penetrate"] = ["U+44de"]
UNICODE_TO_BLISS["U+44de"].append("enter,absorb,insert,penetrate")
BLISS_TO_UNICODE["journalist"] = ["U+44df"]
UNICODE_TO_BLISS["U+44df"] = ["journalist"]
BLISS_TO_UNICODE["chick"] = ["U+44e0"]
UNICODE_TO_BLISS["U+44e0"] = ["chick"]
BLISS_TO_UNICODE["care centre"] = ["U+44e1"]
UNICODE_TO_BLISS["U+44e1"] = ["care centre"]
BLISS_TO_UNICODE["accessible"] = ["U+44e2"]
UNICODE_TO_BLISS["U+44e2"] = ["accessible"]
BLISS_TO_UNICODE["paddock"] = ["U+44e3"]
UNICODE_TO_BLISS["U+44e3"] = ["paddock"]
BLISS_TO_UNICODE["corpse"] = ["U+44e4"]
UNICODE_TO_BLISS["U+44e4"] = ["corpse"]
BLISS_TO_UNICODE["cadaver"] = ["U+44e4"]
UNICODE_TO_BLISS["U+44e4"].append("cadaver")
BLISS_TO_UNICODE["corpse,cadaver"] = ["U+44e4"]
UNICODE_TO_BLISS["U+44e4"].append("corpse,cadaver")
BLISS_TO_UNICODE["religion teacher"] = ["U+44e5"]
UNICODE_TO_BLISS["U+44e5"] = ["religion teacher"]
BLISS_TO_UNICODE["hurricane"] = ["U+44e6"]
UNICODE_TO_BLISS["U+44e6"] = ["hurricane"]
BLISS_TO_UNICODE["spreadable cheese"] = ["U+44e7"]
UNICODE_TO_BLISS["U+44e7"] = ["spreadable cheese"]
BLISS_TO_UNICODE["three arrowheads"] = ["U+44e8"]
UNICODE_TO_BLISS["U+44e8"] = ["three arrowheads"]
BLISS_TO_UNICODE["spines"] = ["U+3b7d"]
UNICODE_TO_BLISS["U+3b7d"].append("spines")
BLISS_TO_UNICODE["quills,spines"] = ["U+3b7d"]
UNICODE_TO_BLISS["U+3b7d"].append("quills,spines")
BLISS_TO_UNICODE["December"] = ["U+44e9"]
UNICODE_TO_BLISS["U+44e9"] = ["December"]
BLISS_TO_UNICODE["South America"] = ["U+44ea"]
UNICODE_TO_BLISS["U+44ea"] = ["South America"]
BLISS_TO_UNICODE["Japan"] = ["U+44eb"]
UNICODE_TO_BLISS["U+44eb"] = ["Japan"]
BLISS_TO_UNICODE["sunrise"] = ["U+44ec"]
UNICODE_TO_BLISS["U+44ec"] = ["sunrise"]
BLISS_TO_UNICODE["tomb"] = ["U+44ed"]
UNICODE_TO_BLISS["U+44ed"] = ["tomb"]
BLISS_TO_UNICODE["blood vessel"] = ["U+44ee"]
UNICODE_TO_BLISS["U+44ee"] = ["blood vessel"]
BLISS_TO_UNICODE["hitch"] = ["U+44ef"]
UNICODE_TO_BLISS["U+44ef"] = ["hitch"]
BLISS_TO_UNICODE["tie up"] = ["U+44ef"]
UNICODE_TO_BLISS["U+44ef"].append("tie up")
BLISS_TO_UNICODE["fix up"] = ["U+44ef"]
UNICODE_TO_BLISS["U+44ef"].append("fix up")
BLISS_TO_UNICODE["hitch,tie up,fix up"] = ["U+44ef"]
UNICODE_TO_BLISS["U+44ef"].append("hitch,tie up,fix up")
BLISS_TO_UNICODE["adolescent"].append("U+34b5")
UNICODE_TO_BLISS["U+34b5"].append("adolescent")
BLISS_TO_UNICODE["youth"] = ["U+34b5"]
UNICODE_TO_BLISS["U+34b5"].append("youth")
BLISS_TO_UNICODE["teenager,adolescent,youth"] = ["U+34b5"]
UNICODE_TO_BLISS["U+34b5"].append("teenager,adolescent,youth")
BLISS_TO_UNICODE["condense"] = ["U+44f0"]
UNICODE_TO_BLISS["U+44f0"] = ["condense"]
BLISS_TO_UNICODE["make cheese"] = ["U+44f1"]
UNICODE_TO_BLISS["U+44f1"] = ["make cheese"]
BLISS_TO_UNICODE["November"] = ["U+44f2"]
UNICODE_TO_BLISS["U+44f2"] = ["November"]
BLISS_TO_UNICODE["11"] = ["U+44f3"]
UNICODE_TO_BLISS["U+44f3"] = ["11"]
BLISS_TO_UNICODE["coach"] = ["U+347f"]
UNICODE_TO_BLISS["U+347f"].append("coach")
BLISS_TO_UNICODE["bus,coach"] = ["U+347f"]
UNICODE_TO_BLISS["U+347f"].append("bus,coach")
BLISS_TO_UNICODE["except"] = ["U+34c7"]
UNICODE_TO_BLISS["U+34c7"].append("except")
BLISS_TO_UNICODE["but,except"] = ["U+34c7"]
UNICODE_TO_BLISS["U+34c7"].append("but,except")
BLISS_TO_UNICODE["CKB likens the but that halts a free flow of speech to a vertical line that stops a horizontal flowing line"] = ["U+44f4"]
UNICODE_TO_BLISS["U+44f4"] = ["CKB likens the but that halts a free flow of speech to a vertical line that stops a horizontal flowing line"]
BLISS_TO_UNICODE["dangerous"] = ["U+44f5"]
UNICODE_TO_BLISS["U+44f5"] = ["dangerous"]
BLISS_TO_UNICODE["minutes"] = ["U+44f6"]
UNICODE_TO_BLISS["U+44f6"] = ["minutes"]
BLISS_TO_UNICODE["skating"] = ["U+44f7"]
UNICODE_TO_BLISS["U+44f7"] = ["skating"]
BLISS_TO_UNICODE["Tevet"] = ["U+44f8"]
UNICODE_TO_BLISS["U+44f8"] = ["Tevet"]
BLISS_TO_UNICODE["whisper"] = ["U+44f9"]
UNICODE_TO_BLISS["U+44f9"] = ["whisper"]
BLISS_TO_UNICODE["domino"] = ["U+44fa"]
UNICODE_TO_BLISS["U+44fa"] = ["domino"]
BLISS_TO_UNICODE["pictograph of curly tail"] = ["U+44fb"]
UNICODE_TO_BLISS["U+44fb"] = ["pictograph of curly tail"]
BLISS_TO_UNICODE["tabletop"] = ["U+44fc"]
UNICODE_TO_BLISS["U+44fc"] = ["tabletop"]
BLISS_TO_UNICODE["pointer to the top"] = ["U+44fd"]
UNICODE_TO_BLISS["U+44fd"] = ["pointer to the top"]
BLISS_TO_UNICODE["Children's Day"] = ["U+44fe"]
UNICODE_TO_BLISS["U+44fe"] = ["Children's Day"]
BLISS_TO_UNICODE["April"] = ["U+44ff"]
UNICODE_TO_BLISS["U+44ff"] = ["April"]
BLISS_TO_UNICODE["baker"] = ["U+4500"]
UNICODE_TO_BLISS["U+4500"] = ["baker"]
BLISS_TO_UNICODE["student"] = ["U+4501"]
UNICODE_TO_BLISS["U+4501"] = ["student"]
BLISS_TO_UNICODE["pupil"] = ["U+4501"]
UNICODE_TO_BLISS["U+4501"].append("pupil")
BLISS_TO_UNICODE["student,pupil"] = ["U+4501"]
UNICODE_TO_BLISS["U+4501"].append("student,pupil")
BLISS_TO_UNICODE["bagpipe"] = ["U+4502"]
UNICODE_TO_BLISS["U+4502"] = ["bagpipe"]
BLISS_TO_UNICODE["ladybird"] = ["U+4503"]
UNICODE_TO_BLISS["U+4503"] = ["ladybird"]
BLISS_TO_UNICODE["grape juice"] = ["U+4504"]
UNICODE_TO_BLISS["U+4504"] = ["grape juice"]
BLISS_TO_UNICODE["polar night"] = ["U+4505"]
UNICODE_TO_BLISS["U+4505"] = ["polar night"]
BLISS_TO_UNICODE["hate"] = ["U+4506"]
UNICODE_TO_BLISS["U+4506"] = ["hate"]
BLISS_TO_UNICODE["hatred"] = ["U+4506"]
UNICODE_TO_BLISS["U+4506"].append("hatred")
BLISS_TO_UNICODE["hate,hatred"] = ["U+4506"]
UNICODE_TO_BLISS["U+4506"].append("hate,hatred")
BLISS_TO_UNICODE["discount sale"] = ["U+4507"]
UNICODE_TO_BLISS["U+4507"] = ["discount sale"]
BLISS_TO_UNICODE["reference dot"] = ["U+4508"]
UNICODE_TO_BLISS["U+4508"] = ["reference dot"]
BLISS_TO_UNICODE["playground"] = ["U+4509"]
UNICODE_TO_BLISS["U+4509"] = ["playground"]
BLISS_TO_UNICODE["dreidel top"] = ["U+450a"]
UNICODE_TO_BLISS["U+450a"] = ["dreidel top"]
BLISS_TO_UNICODE["each"] = ["U+450b"]
UNICODE_TO_BLISS["U+450b"] = ["each"]
BLISS_TO_UNICODE["every"].append("U+450b")
UNICODE_TO_BLISS["U+450b"].append("every")
BLISS_TO_UNICODE["each,every"] = ["U+450b"]
UNICODE_TO_BLISS["U+450b"].append("each,every")
BLISS_TO_UNICODE["Little My"] = ["U+450c"]
UNICODE_TO_BLISS["U+450c"] = ["Little My"]
BLISS_TO_UNICODE["enjoy"] = ["U+450d"]
UNICODE_TO_BLISS["U+450d"] = ["enjoy"]
BLISS_TO_UNICODE["equestrian sports"] = ["U+450e"]
UNICODE_TO_BLISS["U+450e"] = ["equestrian sports"]
BLISS_TO_UNICODE["butcher shop"] = ["U+450f"]
UNICODE_TO_BLISS["U+450f"] = ["butcher shop"]
BLISS_TO_UNICODE["French fries"] = ["U+4510"]
UNICODE_TO_BLISS["U+4510"] = ["French fries"]
BLISS_TO_UNICODE["chips"] = ["U+4510"]
UNICODE_TO_BLISS["U+4510"].append("chips")
BLISS_TO_UNICODE["French fries,chips"] = ["U+4510"]
UNICODE_TO_BLISS["U+4510"].append("French fries,chips")
BLISS_TO_UNICODE["ethanol"] = ["U+39b9"]
UNICODE_TO_BLISS["U+39b9"].append("ethanol")
BLISS_TO_UNICODE["alcohol,ethanol"] = ["U+39b9"]
UNICODE_TO_BLISS["U+39b9"].append("alcohol,ethanol")
BLISS_TO_UNICODE["length)"] = ["U+3ae6"]
UNICODE_TO_BLISS["U+3ae6"].append("length)")
BLISS_TO_UNICODE["quatersized vertical line"] = ["U+4511"]
UNICODE_TO_BLISS["U+4511"] = ["quatersized vertical line"]
BLISS_TO_UNICODE["quatersized circle"] = ["U+4512"]
UNICODE_TO_BLISS["U+4512"] = ["quatersized circle"]
BLISS_TO_UNICODE["drinking straw"] = ["U+4484"]
UNICODE_TO_BLISS["U+4484"].append("drinking straw")
BLISS_TO_UNICODE["straw,drinking straw"] = ["U+4484"]
UNICODE_TO_BLISS["U+4484"].append("straw,drinking straw")
BLISS_TO_UNICODE["go by airplane"] = ["U+4514"]
UNICODE_TO_BLISS["U+4514"] = ["go by airplane"]
BLISS_TO_UNICODE["curved line"].append("U+32ef")
UNICODE_TO_BLISS["U+32ef"].append("curved line")
BLISS_TO_UNICODE["curve,curved line"] = ["U+32ef"]
UNICODE_TO_BLISS["U+32ef"].append("curve,curved line")
BLISS_TO_UNICODE["to wait"] = ["U+4515"]
UNICODE_TO_BLISS["U+4515"] = ["to wait"]
BLISS_TO_UNICODE["slaughterer"] = ["U+4516"]
UNICODE_TO_BLISS["U+4516"] = ["slaughterer"]
BLISS_TO_UNICODE["June"] = ["U+4517"]
UNICODE_TO_BLISS["U+4517"] = ["June"]
BLISS_TO_UNICODE["Messiah"] = ["U+4518"]
UNICODE_TO_BLISS["U+4518"] = ["Messiah"]
BLISS_TO_UNICODE["excellent"] = ["U+4519"]
UNICODE_TO_BLISS["U+4519"] = ["excellent"]
BLISS_TO_UNICODE["kangaroo"] = ["U+451a"]
UNICODE_TO_BLISS["U+451a"] = ["kangaroo"]
BLISS_TO_UNICODE["marsupial"].append("U+451a")
UNICODE_TO_BLISS["U+451a"].append("marsupial")
BLISS_TO_UNICODE["pouched mammal"] = ["U+451a"]
UNICODE_TO_BLISS["U+451a"].append("pouched mammal")
BLISS_TO_UNICODE["kangaroo,marsupial"] = ["U+451a"]
UNICODE_TO_BLISS["U+451a"].append("kangaroo,marsupial")
BLISS_TO_UNICODE["advocacy"] = ["U+451b"]
UNICODE_TO_BLISS["U+451b"] = ["advocacy"]
BLISS_TO_UNICODE["representation"] = ["U+451b"]
UNICODE_TO_BLISS["U+451b"].append("representation")
BLISS_TO_UNICODE["advocacy,representation"] = ["U+451b"]
UNICODE_TO_BLISS["U+451b"].append("advocacy,representation")
BLISS_TO_UNICODE["Muhammad"] = ["U+451c"]
UNICODE_TO_BLISS["U+451c"] = ["Muhammad"]
BLISS_TO_UNICODE["Mohammed"] = ["U+451c"]
UNICODE_TO_BLISS["U+451c"].append("Mohammed")
BLISS_TO_UNICODE["Muhammed"] = ["U+451c"]
UNICODE_TO_BLISS["U+451c"].append("Muhammed")
BLISS_TO_UNICODE["Muhammad,Mohammed,Muhammed"] = ["U+451c"]
UNICODE_TO_BLISS["U+451c"].append("Muhammad,Mohammed,Muhammed")
BLISS_TO_UNICODE["tissue"] = ["U+451d"]
UNICODE_TO_BLISS["U+451d"] = ["tissue"]
BLISS_TO_UNICODE["Brahma"] = ["U+451e"]
UNICODE_TO_BLISS["U+451e"] = ["Brahma"]
BLISS_TO_UNICODE["flight instrument"] = ["U+451f"]
UNICODE_TO_BLISS["U+451f"] = ["flight instrument"]
BLISS_TO_UNICODE["woodpecker"] = ["U+4520"]
UNICODE_TO_BLISS["U+4520"] = ["woodpecker"]
BLISS_TO_UNICODE["slalom"] = ["U+4521"]
UNICODE_TO_BLISS["U+4521"] = ["slalom"]
BLISS_TO_UNICODE["to turn"] = ["U+4522"]
UNICODE_TO_BLISS["U+4522"] = ["to turn"]
BLISS_TO_UNICODE["pictograph of head and horn"] = ["U+4523"]
UNICODE_TO_BLISS["U+4523"] = ["pictograph of head and horn"]
BLISS_TO_UNICODE["ancestor"] = ["U+4524"]
UNICODE_TO_BLISS["U+4524"] = ["ancestor"]
BLISS_TO_UNICODE["martial arts"] = ["U+4525"]
UNICODE_TO_BLISS["U+4525"] = ["martial arts"]
BLISS_TO_UNICODE["four dots"] = ["U+4526"]
UNICODE_TO_BLISS["U+4526"] = ["four dots"]
BLISS_TO_UNICODE["altar cloth"] = ["U+4527"]
UNICODE_TO_BLISS["U+4527"] = ["altar cloth"]
BLISS_TO_UNICODE["altar"] = ["U+4528"]
UNICODE_TO_BLISS["U+4528"] = ["altar"]
BLISS_TO_UNICODE["backwards"] = ["U+4529"]
UNICODE_TO_BLISS["U+4529"] = ["backwards"]
BLISS_TO_UNICODE["short vertical line"] = ["U+452a"]
UNICODE_TO_BLISS["U+452a"] = ["short vertical line"]
BLISS_TO_UNICODE["crown prince"] = ["U+452b"]
UNICODE_TO_BLISS["U+452b"] = ["crown prince"]
BLISS_TO_UNICODE["prince"] = ["U+452c"]
UNICODE_TO_BLISS["U+452c"] = ["prince"]
BLISS_TO_UNICODE["drupe"] = ["U+32b7"]
UNICODE_TO_BLISS["U+32b7"].append("drupe")
BLISS_TO_UNICODE["plum,drupe"] = ["U+32b7"]
UNICODE_TO_BLISS["U+32b7"].append("plum,drupe")
BLISS_TO_UNICODE["digest"] = ["U+452d"]
UNICODE_TO_BLISS["U+452d"] = ["digest"]
BLISS_TO_UNICODE["digestion"] = ["U+452e"]
UNICODE_TO_BLISS["U+452e"] = ["digestion"]
BLISS_TO_UNICODE["uterine contraction"] = ["U+452f"]
UNICODE_TO_BLISS["U+452f"] = ["uterine contraction"]
BLISS_TO_UNICODE["writing"] = ["U+4530"]
UNICODE_TO_BLISS["U+4530"] = ["writing"]
BLISS_TO_UNICODE["flower meadow"] = ["U+4531"]
UNICODE_TO_BLISS["U+4531"] = ["flower meadow"]
BLISS_TO_UNICODE["croquet"] = ["U+4532"]
UNICODE_TO_BLISS["U+4532"] = ["croquet"]
BLISS_TO_UNICODE["Spain"] = ["U+4533"]
UNICODE_TO_BLISS["U+4533"] = ["Spain"]
BLISS_TO_UNICODE["castanet"] = ["U+4534"]
UNICODE_TO_BLISS["U+4534"] = ["castanet"]
BLISS_TO_UNICODE["Judaism"] = ["U+4535"]
UNICODE_TO_BLISS["U+4535"] = ["Judaism"]
BLISS_TO_UNICODE["tourist"] = ["U+4536"]
UNICODE_TO_BLISS["U+4536"] = ["tourist"]
BLISS_TO_UNICODE["ten o'clock eating break"] = ["U+4537"]
UNICODE_TO_BLISS["U+4537"] = ["ten o'clock eating break"]
BLISS_TO_UNICODE["Noah"] = ["U+4538"]
UNICODE_TO_BLISS["U+4538"] = ["Noah"]
BLISS_TO_UNICODE["constipation"] = ["U+4539"]
UNICODE_TO_BLISS["U+4539"] = ["constipation"]
BLISS_TO_UNICODE["waffle"] = ["U+453a"]
UNICODE_TO_BLISS["U+453a"] = ["waffle"]
BLISS_TO_UNICODE["unidentified object"] = ["U+453b"]
UNICODE_TO_BLISS["U+453b"] = ["unidentified object"]
BLISS_TO_UNICODE["endocrine system"] = ["U+453c"]
UNICODE_TO_BLISS["U+453c"] = ["endocrine system"]
BLISS_TO_UNICODE["hotel"] = ["U+453d"]
UNICODE_TO_BLISS["U+453d"] = ["hotel"]
BLISS_TO_UNICODE["motel"] = ["U+453d"]
UNICODE_TO_BLISS["U+453d"].append("motel")
BLISS_TO_UNICODE["hotel,motel"] = ["U+453d"]
UNICODE_TO_BLISS["U+453d"].append("hotel,motel")
BLISS_TO_UNICODE["eternal"] = ["U+453e"]
UNICODE_TO_BLISS["U+453e"] = ["eternal"]
BLISS_TO_UNICODE["acrobat"] = ["U+453f"]
UNICODE_TO_BLISS["U+453f"] = ["acrobat"]
BLISS_TO_UNICODE["cheap"] = ["U+4540"]
UNICODE_TO_BLISS["U+4540"] = ["cheap"]
BLISS_TO_UNICODE["inexpensive"] = ["U+4540"]
UNICODE_TO_BLISS["U+4540"].append("inexpensive")
BLISS_TO_UNICODE["cheap,inexpensive"] = ["U+4540"]
UNICODE_TO_BLISS["U+4540"].append("cheap,inexpensive")
BLISS_TO_UNICODE["Antarctic"] = ["U+4541"]
UNICODE_TO_BLISS["U+4541"] = ["Antarctic"]
BLISS_TO_UNICODE["researcher"] = ["U+376e"]
UNICODE_TO_BLISS["U+376e"].append("researcher")
BLISS_TO_UNICODE["scientist,researcher"] = ["U+376e"]
UNICODE_TO_BLISS["U+376e"].append("scientist,researcher")
BLISS_TO_UNICODE["lovable"] = ["U+4542"]
UNICODE_TO_BLISS["U+4542"] = ["lovable"]
BLISS_TO_UNICODE["insulation"].append("U+3ec3")
UNICODE_TO_BLISS["U+3ec3"].append("insulation")
BLISS_TO_UNICODE["impermeable material,insulation"] = ["U+3ec3"]
UNICODE_TO_BLISS["U+3ec3"].append("impermeable material,insulation")
BLISS_TO_UNICODE["mercury"] = ["U+4543"]
UNICODE_TO_BLISS["U+4543"] = ["mercury"]
BLISS_TO_UNICODE["thermometer"] = ["U+4544"]
UNICODE_TO_BLISS["U+4544"] = ["thermometer"]
BLISS_TO_UNICODE["their"] = ["U+4545"]
UNICODE_TO_BLISS["U+4545"] = ["their"]
BLISS_TO_UNICODE["theirs"] = ["U+4545"]
UNICODE_TO_BLISS["U+4545"].append("theirs")
BLISS_TO_UNICODE["their,theirs"] = ["U+4545"]
UNICODE_TO_BLISS["U+4545"].append("their,theirs")
BLISS_TO_UNICODE["table game"] = ["U+4546"]
UNICODE_TO_BLISS["U+4546"] = ["table game"]
BLISS_TO_UNICODE["paediatrician"] = ["U+4547"]
UNICODE_TO_BLISS["U+4547"] = ["paediatrician"]
BLISS_TO_UNICODE["kill"] = ["U+4548"]
UNICODE_TO_BLISS["U+4548"] = ["kill"]
BLISS_TO_UNICODE["murder"].append("U+4548")
UNICODE_TO_BLISS["U+4548"].append("murder")
BLISS_TO_UNICODE["kill,murder"] = ["U+4548"]
UNICODE_TO_BLISS["U+4548"].append("kill,murder")
BLISS_TO_UNICODE["to die"] = ["U+4549"]
UNICODE_TO_BLISS["U+4549"] = ["to die"]
BLISS_TO_UNICODE["Spiderman"] = ["U+454a"]
UNICODE_TO_BLISS["U+454a"] = ["Spiderman"]
BLISS_TO_UNICODE["western"] = ["U+454b"]
UNICODE_TO_BLISS["U+454b"] = ["western"]
BLISS_TO_UNICODE["sanitary napkin"] = ["U+454c"]
UNICODE_TO_BLISS["U+454c"] = ["sanitary napkin"]
BLISS_TO_UNICODE["sanitary towel"] = ["U+454c"]
UNICODE_TO_BLISS["U+454c"].append("sanitary towel")
BLISS_TO_UNICODE["tampon"] = ["U+454c"]
UNICODE_TO_BLISS["U+454c"].append("tampon")
BLISS_TO_UNICODE["sanitary napkin,sanitary towel,tampon"] = ["U+454c"]
UNICODE_TO_BLISS["U+454c"].append("sanitary napkin,sanitary towel,tampon")
BLISS_TO_UNICODE["closet"] = ["U+3379"]
UNICODE_TO_BLISS["U+3379"].append("closet")
BLISS_TO_UNICODE["wardrobe"] = ["U+3379"]
UNICODE_TO_BLISS["U+3379"].append("wardrobe")
BLISS_TO_UNICODE["cupboard,closet,wardrobe"] = ["U+3379"]
UNICODE_TO_BLISS["U+3379"].append("cupboard,closet,wardrobe")
BLISS_TO_UNICODE["tie whipping knot"] = ["U+454d"]
UNICODE_TO_BLISS["U+454d"] = ["tie whipping knot"]
BLISS_TO_UNICODE["national day"] = ["U+454e"]
UNICODE_TO_BLISS["U+454e"] = ["national day"]
BLISS_TO_UNICODE["lying"].append("U+3c2d")
UNICODE_TO_BLISS["U+3c2d"].append("lying")
BLISS_TO_UNICODE["reclining,lying"] = ["U+3c2d"]
UNICODE_TO_BLISS["U+3c2d"].append("reclining,lying")
BLISS_TO_UNICODE["rag"] = ["U+454f"]
UNICODE_TO_BLISS["U+454f"] = ["rag"]
BLISS_TO_UNICODE["handkerchief"] = ["U+4550"]
UNICODE_TO_BLISS["U+4550"] = ["handkerchief"]
BLISS_TO_UNICODE["ram"] = ["U+4551"]
UNICODE_TO_BLISS["U+4551"] = ["ram"]
BLISS_TO_UNICODE["rap"] = ["U+4552"]
UNICODE_TO_BLISS["U+4552"] = ["rap"]
BLISS_TO_UNICODE["spade"] = ["U+34bc"]
UNICODE_TO_BLISS["U+34bc"].append("spade")
BLISS_TO_UNICODE["shovel,spade"] = ["U+34bc"]
UNICODE_TO_BLISS["U+34bc"].append("shovel,spade")
BLISS_TO_UNICODE["triangular shape"] = ["U+4553"]
UNICODE_TO_BLISS["U+4553"] = ["triangular shape"]
BLISS_TO_UNICODE["food processor"] = ["U+4554"]
UNICODE_TO_BLISS["U+4554"] = ["food processor"]
BLISS_TO_UNICODE["kitchen machine"] = ["U+4554"]
UNICODE_TO_BLISS["U+4554"].append("kitchen machine")
BLISS_TO_UNICODE["food processor,kitchen machine"] = ["U+4554"]
UNICODE_TO_BLISS["U+4554"].append("food processor,kitchen machine")
BLISS_TO_UNICODE["Good evening"] = ["U+4555"]
UNICODE_TO_BLISS["U+4555"] = ["Good evening"]
BLISS_TO_UNICODE["milkman"] = ["U+4556"]
UNICODE_TO_BLISS["U+4556"] = ["milkman"]
BLISS_TO_UNICODE["evangelise"] = ["U+4557"]
UNICODE_TO_BLISS["U+4557"] = ["evangelise"]
BLISS_TO_UNICODE["Brontosaurus"] = ["U+4558"]
UNICODE_TO_BLISS["U+4558"] = ["Brontosaurus"]
BLISS_TO_UNICODE["coin"] = ["U+4559"]
UNICODE_TO_BLISS["U+4559"] = ["coin"]
BLISS_TO_UNICODE["unforgivable"] = ["U+455a"]
UNICODE_TO_BLISS["U+455a"] = ["unforgivable"]
BLISS_TO_UNICODE["inexcusable"] = ["U+455a"]
UNICODE_TO_BLISS["U+455a"].append("inexcusable")
BLISS_TO_UNICODE["unforgivable,inexcusable"] = ["U+455a"]
UNICODE_TO_BLISS["U+455a"].append("unforgivable,inexcusable")
BLISS_TO_UNICODE["glow"] = ["U+455b"]
UNICODE_TO_BLISS["U+455b"] = ["glow"]
BLISS_TO_UNICODE["pictograph with stem and leaves"] = ["U+455c"]
UNICODE_TO_BLISS["U+455c"] = ["pictograph with stem and leaves"]
BLISS_TO_UNICODE["pictograph of cluster of currants"] = ["U+455d"]
UNICODE_TO_BLISS["U+455d"] = ["pictograph of cluster of currants"]
BLISS_TO_UNICODE["raisins"] = ["U+455e"]
UNICODE_TO_BLISS["U+455e"] = ["raisins"]
BLISS_TO_UNICODE["currants"].append("U+455e")
UNICODE_TO_BLISS["U+455e"].append("currants")
BLISS_TO_UNICODE["raisins,currants"] = ["U+455e"]
UNICODE_TO_BLISS["U+455e"].append("raisins,currants")
BLISS_TO_UNICODE["inspire"] = ["U+455f"]
UNICODE_TO_BLISS["U+455f"] = ["inspire"]
BLISS_TO_UNICODE["queen"] = ["U+4560"]
UNICODE_TO_BLISS["U+4560"] = ["queen"]
BLISS_TO_UNICODE["aid store room"] = ["U+4561"]
UNICODE_TO_BLISS["U+4561"] = ["aid store room"]
BLISS_TO_UNICODE["store room"] = ["U+4562"]
UNICODE_TO_BLISS["U+4562"] = ["store room"]
BLISS_TO_UNICODE["head louse"] = ["U+4563"]
UNICODE_TO_BLISS["U+4563"] = ["head louse"]
BLISS_TO_UNICODE["bus stop"] = ["U+4564"]
UNICODE_TO_BLISS["U+4564"] = ["bus stop"]
BLISS_TO_UNICODE["bus bay"].append("U+4564")
UNICODE_TO_BLISS["U+4564"].append("bus bay")
BLISS_TO_UNICODE["bus stop,bus bay"] = ["U+4564"]
UNICODE_TO_BLISS["U+4564"].append("bus stop,bus bay")
BLISS_TO_UNICODE["shower chair"] = ["U+4565"]
UNICODE_TO_BLISS["U+4565"] = ["shower chair"]
BLISS_TO_UNICODE["sunglasses"] = ["U+4566"]
UNICODE_TO_BLISS["U+4566"] = ["sunglasses"]
BLISS_TO_UNICODE["fluid"].append("U+3206")
UNICODE_TO_BLISS["U+3206"].append("fluid")
BLISS_TO_UNICODE["liquid"].append("U+3206")
UNICODE_TO_BLISS["U+3206"].append("liquid")
BLISS_TO_UNICODE["water,fluid,liquid"] = ["U+3206"]
UNICODE_TO_BLISS["U+3206"].append("water,fluid,liquid")
BLISS_TO_UNICODE["symbol looks like a wave"] = ["U+4567"]
UNICODE_TO_BLISS["U+4567"] = ["symbol looks like a wave"]
BLISS_TO_UNICODE[" suggesting water or liquid"] = ["U+4568"]
UNICODE_TO_BLISS["U+4568"] = [" suggesting water or liquid"]
BLISS_TO_UNICODE["spokesperson"] = ["U+3c9d"]
UNICODE_TO_BLISS["U+3c9d"].append("spokesperson")
BLISS_TO_UNICODE["rowing"] = ["U+4569"]
UNICODE_TO_BLISS["U+4569"] = ["rowing"]
BLISS_TO_UNICODE["egoism"] = ["U+32e3"]
UNICODE_TO_BLISS["U+32e3"].append("egoism")
BLISS_TO_UNICODE["selfishness,egoism"] = ["U+32e3"]
UNICODE_TO_BLISS["U+32e3"].append("selfishness,egoism")
BLISS_TO_UNICODE["erupt"] = ["U+456a"]
UNICODE_TO_BLISS["U+456a"] = ["erupt"]
BLISS_TO_UNICODE["eruption"] = ["U+456b"]
UNICODE_TO_BLISS["U+456b"] = ["eruption"]
BLISS_TO_UNICODE["Jupiter"] = ["U+456c"]
UNICODE_TO_BLISS["U+456c"] = ["Jupiter"]
BLISS_TO_UNICODE["game box"] = ["U+456d"]
UNICODE_TO_BLISS["U+456d"] = ["game box"]
BLISS_TO_UNICODE["approach"] = ["U+456e"]
UNICODE_TO_BLISS["U+456e"] = ["approach"]
BLISS_TO_UNICODE["come"] = ["U+456f"]
UNICODE_TO_BLISS["U+456f"] = ["come"]
BLISS_TO_UNICODE["approach"].append("U+456f")
UNICODE_TO_BLISS["U+456f"].append("approach")
BLISS_TO_UNICODE["come,approach"] = ["U+456f"]
UNICODE_TO_BLISS["U+456f"].append("come,approach")
BLISS_TO_UNICODE["weak"] = ["U+4570"]
UNICODE_TO_BLISS["U+4570"] = ["weak"]
BLISS_TO_UNICODE["improve"] = ["U+4571"]
UNICODE_TO_BLISS["U+4571"] = ["improve"]
BLISS_TO_UNICODE["riding instructor"] = ["U+4572"]
UNICODE_TO_BLISS["U+4572"] = ["riding instructor"]
BLISS_TO_UNICODE["pole"] = ["U+35a2"]
UNICODE_TO_BLISS["U+35a2"].append("pole")
BLISS_TO_UNICODE["linear thing,pole"] = ["U+35a2"]
UNICODE_TO_BLISS["U+35a2"].append("linear thing,pole")
BLISS_TO_UNICODE["betting"] = ["U+4573"]
UNICODE_TO_BLISS["U+4573"] = ["betting"]
BLISS_TO_UNICODE["tallith"] = ["U+4574"]
UNICODE_TO_BLISS["U+4574"] = ["tallith"]
BLISS_TO_UNICODE["to pray"] = ["U+4575"]
UNICODE_TO_BLISS["U+4575"] = ["to pray"]
BLISS_TO_UNICODE["beef"] = ["U+4576"]
UNICODE_TO_BLISS["U+4576"] = ["beef"]
BLISS_TO_UNICODE["Sandman"] = ["U+4577"]
UNICODE_TO_BLISS["U+4577"] = ["Sandman"]
BLISS_TO_UNICODE["fairy tale"] = ["U+4578"]
UNICODE_TO_BLISS["U+4578"] = ["fairy tale"]
BLISS_TO_UNICODE["beet"] = ["U+4579"]
UNICODE_TO_BLISS["U+4579"] = ["beet"]
BLISS_TO_UNICODE["rabbitlike"] = ["U+457a"]
UNICODE_TO_BLISS["U+457a"] = ["rabbitlike"]
BLISS_TO_UNICODE["bladder"] = ["U+457b"]
UNICODE_TO_BLISS["U+457b"] = ["bladder"]
BLISS_TO_UNICODE["rhythm instrument"] = ["U+457c"]
UNICODE_TO_BLISS["U+457c"] = ["rhythm instrument"]
BLISS_TO_UNICODE["glider"] = ["U+457d"]
UNICODE_TO_BLISS["U+457d"] = ["glider"]
BLISS_TO_UNICODE["decorated cake"] = ["U+457e"]
UNICODE_TO_BLISS["U+457e"] = ["decorated cake"]
BLISS_TO_UNICODE["list"] = ["U+457f"]
UNICODE_TO_BLISS["U+457f"] = ["list"]
BLISS_TO_UNICODE["inventory"] = ["U+457f"]
UNICODE_TO_BLISS["U+457f"].append("inventory")
BLISS_TO_UNICODE["list,inventory"] = ["U+457f"]
UNICODE_TO_BLISS["U+457f"].append("list,inventory")
BLISS_TO_UNICODE["shoulder blade"] = ["U+4580"]
UNICODE_TO_BLISS["U+4580"] = ["shoulder blade"]
BLISS_TO_UNICODE["scapula"] = ["U+4580"]
UNICODE_TO_BLISS["U+4580"].append("scapula")
BLISS_TO_UNICODE["shoulder blade,scapula"] = ["U+4580"]
UNICODE_TO_BLISS["U+4580"].append("shoulder blade,scapula")
BLISS_TO_UNICODE["several"] = ["U+4581"]
UNICODE_TO_BLISS["U+4581"] = ["several"]
BLISS_TO_UNICODE["moose"] = ["U+4582"]
UNICODE_TO_BLISS["U+4582"] = ["moose"]
BLISS_TO_UNICODE["elk"] = ["U+4582"]
UNICODE_TO_BLISS["U+4582"].append("elk")
BLISS_TO_UNICODE["moose,elk"] = ["U+4582"]
UNICODE_TO_BLISS["U+4582"].append("moose,elk")
BLISS_TO_UNICODE["L"] = ["U+4583"]
UNICODE_TO_BLISS["U+4583"] = ["L"]
BLISS_TO_UNICODE["cycle"] = ["U+4584"]
UNICODE_TO_BLISS["U+4584"] = ["cycle"]
BLISS_TO_UNICODE["ride a bike"] = ["U+4584"]
UNICODE_TO_BLISS["U+4584"].append("ride a bike")
BLISS_TO_UNICODE["cycle,ride a bike"] = ["U+4584"]
UNICODE_TO_BLISS["U+4584"].append("cycle,ride a bike")
BLISS_TO_UNICODE["snowman"] = ["U+4585"]
UNICODE_TO_BLISS["U+4585"] = ["snowman"]
BLISS_TO_UNICODE["Estonian"] = ["U+4586"]
UNICODE_TO_BLISS["U+4586"] = ["Estonian"]
BLISS_TO_UNICODE["laptop"] = ["U+4587"]
UNICODE_TO_BLISS["U+4587"] = ["laptop"]
BLISS_TO_UNICODE["dent"].append("U+3a3b")
UNICODE_TO_BLISS["U+3a3b"].append("dent")
BLISS_TO_UNICODE["bruise,dent"] = ["U+3a3b"]
UNICODE_TO_BLISS["U+3a3b"].append("bruise,dent")
BLISS_TO_UNICODE["Christian faith"] = ["U+4588"]
UNICODE_TO_BLISS["U+4588"] = ["Christian faith"]
BLISS_TO_UNICODE["elf"] = ["U+4589"]
UNICODE_TO_BLISS["U+4589"] = ["elf"]
BLISS_TO_UNICODE["turquoise"] = ["U+458a"]
UNICODE_TO_BLISS["U+458a"] = ["turquoise"]
BLISS_TO_UNICODE["bandy"] = ["U+458b"]
UNICODE_TO_BLISS["U+458b"] = ["bandy"]
BLISS_TO_UNICODE["vulture"] = ["U+458c"]
UNICODE_TO_BLISS["U+458c"] = ["vulture"]
BLISS_TO_UNICODE["paratrooper"] = ["U+458d"]
UNICODE_TO_BLISS["U+458d"] = ["paratrooper"]
BLISS_TO_UNICODE["above/superior"] = ["U+458e"]
UNICODE_TO_BLISS["U+458e"] = ["above/superior"]
BLISS_TO_UNICODE["celibacy"] = ["U+458f"]
UNICODE_TO_BLISS["U+458f"] = ["celibacy"]
BLISS_TO_UNICODE["chastity"] = ["U+458f"]
UNICODE_TO_BLISS["U+458f"].append("chastity")
BLISS_TO_UNICODE["abstinence"] = ["U+458f"]
UNICODE_TO_BLISS["U+458f"].append("abstinence")
BLISS_TO_UNICODE["celibacy,chastity,abstinence"] = ["U+458f"]
UNICODE_TO_BLISS["U+458f"].append("celibacy,chastity,abstinence")
BLISS_TO_UNICODE["to decide"] = ["U+4590"]
UNICODE_TO_BLISS["U+4590"] = ["to decide"]
BLISS_TO_UNICODE["celibacy,chastity"] = ["U+458f"]
UNICODE_TO_BLISS["U+458f"].append("celibacy,chastity")
BLISS_TO_UNICODE["specific"] = ["U+4591"]
UNICODE_TO_BLISS["U+4591"] = ["specific"]
BLISS_TO_UNICODE["mosquito"] = ["U+4592"]
UNICODE_TO_BLISS["U+4592"] = ["mosquito"]
BLISS_TO_UNICODE["aroma therapist"] = ["U+4593"]
UNICODE_TO_BLISS["U+4593"] = ["aroma therapist"]
BLISS_TO_UNICODE["escape"] = ["U+4594"]
UNICODE_TO_BLISS["U+4594"] = ["escape"]
BLISS_TO_UNICODE["icy"] = ["U+4595"]
UNICODE_TO_BLISS["U+4595"] = ["icy"]
BLISS_TO_UNICODE["frozen"].append("U+4595")
UNICODE_TO_BLISS["U+4595"].append("frozen")
BLISS_TO_UNICODE["icy,frozen"] = ["U+4595"]
UNICODE_TO_BLISS["U+4595"].append("icy,frozen")
BLISS_TO_UNICODE["backspace"] = ["U+4596"]
UNICODE_TO_BLISS["U+4596"] = ["backspace"]
BLISS_TO_UNICODE["espionage"] = ["U+4597"]
UNICODE_TO_BLISS["U+4597"] = ["espionage"]
BLISS_TO_UNICODE["spying"] = ["U+4597"]
UNICODE_TO_BLISS["U+4597"].append("spying")
BLISS_TO_UNICODE["espionage,spying"] = ["U+4597"]
UNICODE_TO_BLISS["U+4597"].append("espionage,spying")
BLISS_TO_UNICODE["menopause"] = ["U+4598"]
UNICODE_TO_BLISS["U+4598"] = ["menopause"]
BLISS_TO_UNICODE["Holy City"] = ["U+4599"]
UNICODE_TO_BLISS["U+4599"] = ["Holy City"]
BLISS_TO_UNICODE["chapter"] = ["U+459a"]
UNICODE_TO_BLISS["U+459a"] = ["chapter"]
BLISS_TO_UNICODE["curry"] = ["U+459b"]
UNICODE_TO_BLISS["U+459b"] = ["curry"]
BLISS_TO_UNICODE["speed skating"] = ["U+459c"]
UNICODE_TO_BLISS["U+459c"] = ["speed skating"]
BLISS_TO_UNICODE["rolling pin"] = ["U+459d"]
UNICODE_TO_BLISS["U+459d"] = ["rolling pin"]
BLISS_TO_UNICODE["fuselage"] = ["U+459e"]
UNICODE_TO_BLISS["U+459e"] = ["fuselage"]
BLISS_TO_UNICODE["electorate"] = ["U+459f"]
UNICODE_TO_BLISS["U+459f"] = ["electorate"]
BLISS_TO_UNICODE["shopping mall"] = ["U+45a0"]
UNICODE_TO_BLISS["U+45a0"] = ["shopping mall"]
BLISS_TO_UNICODE["Chumash"] = ["U+45a1"]
UNICODE_TO_BLISS["U+45a1"] = ["Chumash"]
BLISS_TO_UNICODE["Pentateuch"] = ["U+45a1"]
UNICODE_TO_BLISS["U+45a1"].append("Pentateuch")
BLISS_TO_UNICODE["Chumash,Pentateuch"] = ["U+45a1"]
UNICODE_TO_BLISS["U+45a1"].append("Chumash,Pentateuch")
BLISS_TO_UNICODE["why"] = ["U+45a2"]
UNICODE_TO_BLISS["U+45a2"] = ["why"]
BLISS_TO_UNICODE["wildflower"] = ["U+45a3"]
UNICODE_TO_BLISS["U+45a3"] = ["wildflower"]
BLISS_TO_UNICODE["heal"] = ["U+45a4"]
UNICODE_TO_BLISS["U+45a4"] = ["heal"]
BLISS_TO_UNICODE["to become"] = ["U+45a5"]
UNICODE_TO_BLISS["U+45a5"] = ["to become"]
BLISS_TO_UNICODE["dollhouse"] = ["U+45a6"]
UNICODE_TO_BLISS["U+45a6"] = ["dollhouse"]
BLISS_TO_UNICODE["doll house"] = ["U+45a6"]
UNICODE_TO_BLISS["U+45a6"].append("doll house")
BLISS_TO_UNICODE["dollhouse,doll house"] = ["U+45a6"]
UNICODE_TO_BLISS["U+45a6"].append("dollhouse,doll house")
BLISS_TO_UNICODE["rich"] = ["U+45a7"]
UNICODE_TO_BLISS["U+45a7"] = ["rich"]
BLISS_TO_UNICODE["wealthy"] = ["U+45a7"]
UNICODE_TO_BLISS["U+45a7"].append("wealthy")
BLISS_TO_UNICODE["rich,wealthy"] = ["U+45a7"]
UNICODE_TO_BLISS["U+45a7"].append("rich,wealthy")
BLISS_TO_UNICODE["card game"] = ["U+45a8"]
UNICODE_TO_BLISS["U+45a8"] = ["card game"]
BLISS_TO_UNICODE["tin,can"] = ["U+3a10"]
UNICODE_TO_BLISS["U+3a10"].append("tin,can")
BLISS_TO_UNICODE["toad"] = ["U+3e64"]
UNICODE_TO_BLISS["U+3e64"].append("toad")
BLISS_TO_UNICODE["frog,toad"] = ["U+3e64"]
UNICODE_TO_BLISS["U+3e64"].append("frog,toad")
BLISS_TO_UNICODE["amphibian"] = ["U+45aa"]
UNICODE_TO_BLISS["U+45aa"] = ["amphibian"]
BLISS_TO_UNICODE["soccer"] = ["U+3cbd"]
UNICODE_TO_BLISS["U+3cbd"].append("soccer")
BLISS_TO_UNICODE["football,soccer"] = ["U+3cbd"]
UNICODE_TO_BLISS["U+3cbd"].append("football,soccer")
BLISS_TO_UNICODE["longer"] = ["U+45ab"]
UNICODE_TO_BLISS["U+45ab"] = ["longer"]
BLISS_TO_UNICODE["navel"] = ["U+45ac"]
UNICODE_TO_BLISS["U+45ac"] = ["navel"]
BLISS_TO_UNICODE["closeness"].append("U+39fb")
UNICODE_TO_BLISS["U+39fb"].append("closeness")
BLISS_TO_UNICODE["intimacy,closeness"] = ["U+39fb"]
UNICODE_TO_BLISS["U+39fb"].append("intimacy,closeness")
BLISS_TO_UNICODE["rob"] = ["U+45ad"]
UNICODE_TO_BLISS["U+45ad"] = ["rob"]
BLISS_TO_UNICODE["to steal"] = ["U+45ae"]
UNICODE_TO_BLISS["U+45ae"] = ["to steal"]
BLISS_TO_UNICODE["long time"] = ["U+45af"]
UNICODE_TO_BLISS["U+45af"] = ["long time"]
BLISS_TO_UNICODE["sing"] = ["U+45b0"]
UNICODE_TO_BLISS["U+45b0"] = ["sing"]
BLISS_TO_UNICODE["Rosh Hashana"] = ["U+45b1"]
UNICODE_TO_BLISS["U+45b1"] = ["Rosh Hashana"]
BLISS_TO_UNICODE["navigational sign"] = ["U+45b2"]
UNICODE_TO_BLISS["U+45b2"] = ["navigational sign"]
BLISS_TO_UNICODE["tablet computer"] = ["U+45b3"]
UNICODE_TO_BLISS["U+45b3"] = ["tablet computer"]
BLISS_TO_UNICODE["tablet"].append("U+45b3")
UNICODE_TO_BLISS["U+45b3"].append("tablet")
BLISS_TO_UNICODE["tablet PC"] = ["U+45b3"]
UNICODE_TO_BLISS["U+45b3"].append("tablet PC")
BLISS_TO_UNICODE["tablet computer,tablet,tablet PC"] = ["U+45b3"]
UNICODE_TO_BLISS["U+45b3"].append("tablet computer,tablet,tablet PC")
BLISS_TO_UNICODE["layer"] = ["U+45b4"]
UNICODE_TO_BLISS["U+45b4"] = ["layer"]
BLISS_TO_UNICODE["level"].append("U+45b4")
UNICODE_TO_BLISS["U+45b4"].append("level")
BLISS_TO_UNICODE["layer,level"] = ["U+45b4"]
UNICODE_TO_BLISS["U+45b4"].append("layer,level")
BLISS_TO_UNICODE["cloudy"] = ["U+45b5"]
UNICODE_TO_BLISS["U+45b5"] = ["cloudy"]
BLISS_TO_UNICODE["dried"] = ["U+45b6"]
UNICODE_TO_BLISS["U+45b6"] = ["dried"]
BLISS_TO_UNICODE["anal intercourse"] = ["U+45b7"]
UNICODE_TO_BLISS["U+45b7"] = ["anal intercourse"]
BLISS_TO_UNICODE["agnosticism"] = ["U+45b8"]
UNICODE_TO_BLISS["U+45b8"] = ["agnosticism"]
BLISS_TO_UNICODE["airport terminal"] = ["U+45b9"]
UNICODE_TO_BLISS["U+45b9"] = ["airport terminal"]
BLISS_TO_UNICODE["baseball"] = ["U+45ba"]
UNICODE_TO_BLISS["U+45ba"] = ["baseball"]
BLISS_TO_UNICODE["proud"] = ["U+45bb"]
UNICODE_TO_BLISS["U+45bb"] = ["proud"]
BLISS_TO_UNICODE["cinnamon"] = ["U+45bc"]
UNICODE_TO_BLISS["U+45bc"] = ["cinnamon"]
BLISS_TO_UNICODE["bark"] = ["U+45bd"]
UNICODE_TO_BLISS["U+45bd"] = ["bark"]
BLISS_TO_UNICODE["weight lifting"] = ["U+45be"]
UNICODE_TO_BLISS["U+45be"] = ["weight lifting"]
BLISS_TO_UNICODE["compare"] = ["U+45bf"]
UNICODE_TO_BLISS["U+45bf"] = ["compare"]
BLISS_TO_UNICODE["Aries"] = ["U+45c0"]
UNICODE_TO_BLISS["U+45c0"] = ["Aries"]
BLISS_TO_UNICODE["runes"] = ["U+45c1"]
UNICODE_TO_BLISS["U+45c1"] = ["runes"]
BLISS_TO_UNICODE["today"] = ["U+45c2"]
UNICODE_TO_BLISS["U+45c2"] = ["today"]
BLISS_TO_UNICODE["October"] = ["U+45c3"]
UNICODE_TO_BLISS["U+45c3"] = ["October"]
BLISS_TO_UNICODE["Eve"] = ["U+45c4"]
UNICODE_TO_BLISS["U+45c4"] = ["Eve"]
BLISS_TO_UNICODE["employee"] = ["U+45c5"]
UNICODE_TO_BLISS["U+45c5"] = ["employee"]
BLISS_TO_UNICODE["drown"] = ["U+45c6"]
UNICODE_TO_BLISS["U+45c6"] = ["drown"]
BLISS_TO_UNICODE["judo"] = ["U+45c7"]
UNICODE_TO_BLISS["U+45c7"] = ["judo"]
BLISS_TO_UNICODE["German"] = ["U+45c8"]
UNICODE_TO_BLISS["U+45c8"] = ["German"]
BLISS_TO_UNICODE["Germany"] = ["U+45c9"]
UNICODE_TO_BLISS["U+45c9"] = ["Germany"]
BLISS_TO_UNICODE["sandstorm"] = ["U+45ca"]
UNICODE_TO_BLISS["U+45ca"] = ["sandstorm"]
BLISS_TO_UNICODE["ferry"] = ["U+45cb"]
UNICODE_TO_BLISS["U+45cb"] = ["ferry"]
BLISS_TO_UNICODE["chocolate spread"] = ["U+45cc"]
UNICODE_TO_BLISS["U+45cc"] = ["chocolate spread"]
BLISS_TO_UNICODE["stroke"] = ["U+45cd"]
UNICODE_TO_BLISS["U+45cd"] = ["stroke"]
BLISS_TO_UNICODE["bicycle path"] = ["U+45ce"]
UNICODE_TO_BLISS["U+45ce"] = ["bicycle path"]
BLISS_TO_UNICODE["Advent"] = ["U+45cf"]
UNICODE_TO_BLISS["U+45cf"] = ["Advent"]
BLISS_TO_UNICODE["classroom"] = ["U+45d0"]
UNICODE_TO_BLISS["U+45d0"] = ["classroom"]
BLISS_TO_UNICODE["Ceres"] = ["U+45d1"]
UNICODE_TO_BLISS["U+45d1"] = ["Ceres"]
BLISS_TO_UNICODE["disability benefit"] = ["U+45d2"]
UNICODE_TO_BLISS["U+45d2"] = ["disability benefit"]
BLISS_TO_UNICODE["lay the table"] = ["U+45d3"]
UNICODE_TO_BLISS["U+45d3"] = ["lay the table"]
BLISS_TO_UNICODE["console"] = ["U+3221"]
UNICODE_TO_BLISS["U+3221"].append("console")
BLISS_TO_UNICODE["comfort,console"] = ["U+3221"]
UNICODE_TO_BLISS["U+3221"].append("comfort,console")
BLISS_TO_UNICODE["midnight"] = ["U+45d4"]
UNICODE_TO_BLISS["U+45d4"] = ["midnight"]
BLISS_TO_UNICODE["courthouse"] = ["U+4360"]
UNICODE_TO_BLISS["U+4360"].append("courthouse")
BLISS_TO_UNICODE["court,courthouse"] = ["U+4360"]
UNICODE_TO_BLISS["U+4360"].append("court,courthouse")
BLISS_TO_UNICODE["chalice"] = ["U+45d5"]
UNICODE_TO_BLISS["U+45d5"] = ["chalice"]
BLISS_TO_UNICODE["computer case"] = ["U+45d6"]
UNICODE_TO_BLISS["U+45d6"] = ["computer case"]
BLISS_TO_UNICODE["bike lamp"] = ["U+45d7"]
UNICODE_TO_BLISS["U+45d7"] = ["bike lamp"]
BLISS_TO_UNICODE["bike"] = ["U+45d8"]
UNICODE_TO_BLISS["U+45d8"] = ["bike"]
BLISS_TO_UNICODE["married"] = ["U+45d9"]
UNICODE_TO_BLISS["U+45d9"] = ["married"]
BLISS_TO_UNICODE["intensity)"] = ["U+45db"]
UNICODE_TO_BLISS["U+45db"] = ["intensity)"]
BLISS_TO_UNICODE["zebra"] = ["U+45dc"]
UNICODE_TO_BLISS["U+45dc"] = ["zebra"]
BLISS_TO_UNICODE["psychology room"] = ["U+45dd"]
UNICODE_TO_BLISS["U+45dd"] = ["psychology room"]
BLISS_TO_UNICODE["of"].append("U+3437")
UNICODE_TO_BLISS["U+3437"].append("of")
BLISS_TO_UNICODE["belongs to,of"] = ["U+3437"]
UNICODE_TO_BLISS["U+3437"].append("belongs to,of")
BLISS_TO_UNICODE["oral sex"] = ["U+45de"]
UNICODE_TO_BLISS["U+45de"] = ["oral sex"]
BLISS_TO_UNICODE["light year"] = ["U+45df"]
UNICODE_TO_BLISS["U+45df"] = ["light year"]
BLISS_TO_UNICODE["hawk"] = ["U+45e0"]
UNICODE_TO_BLISS["U+45e0"] = ["hawk"]
BLISS_TO_UNICODE["eagle"] = ["U+45e0"]
UNICODE_TO_BLISS["U+45e0"].append("eagle")
BLISS_TO_UNICODE["hawk,eagle"] = ["U+45e0"]
UNICODE_TO_BLISS["U+45e0"].append("hawk,eagle")
BLISS_TO_UNICODE["theory"].append("U+3aee")
UNICODE_TO_BLISS["U+3aee"].append("theory")
BLISS_TO_UNICODE["hypothesis,theory"] = ["U+3aee"]
UNICODE_TO_BLISS["U+3aee"].append("hypothesis,theory")
BLISS_TO_UNICODE["flyer"] = ["U+45e1"]
UNICODE_TO_BLISS["U+45e1"] = ["flyer"]
BLISS_TO_UNICODE["notary"] = ["U+45e2"]
UNICODE_TO_BLISS["U+45e2"] = ["notary"]
BLISS_TO_UNICODE["sceptical"] = ["U+45e3"]
UNICODE_TO_BLISS["U+45e3"] = ["sceptical"]
BLISS_TO_UNICODE["skeptical"] = ["U+45e3"]
UNICODE_TO_BLISS["U+45e3"].append("skeptical")
BLISS_TO_UNICODE["questioning"] = ["U+45e3"]
UNICODE_TO_BLISS["U+45e3"].append("questioning")
BLISS_TO_UNICODE["sceptical,skeptical,questioning"] = ["U+45e3"]
UNICODE_TO_BLISS["U+45e3"].append("sceptical,skeptical,questioning")
BLISS_TO_UNICODE["fallopian tube"] = ["U+45e4"]
UNICODE_TO_BLISS["U+45e4"] = ["fallopian tube"]
BLISS_TO_UNICODE["male and female"] = ["U+45e5"]
UNICODE_TO_BLISS["U+45e5"] = ["male and female"]
BLISS_TO_UNICODE["history teacher"] = ["U+45e6"]
UNICODE_TO_BLISS["U+45e6"] = ["history teacher"]
BLISS_TO_UNICODE["pelican"] = ["U+45e7"]
UNICODE_TO_BLISS["U+45e7"] = ["pelican"]
BLISS_TO_UNICODE["ice layer"] = ["U+45e8"]
UNICODE_TO_BLISS["U+45e8"] = ["ice layer"]
BLISS_TO_UNICODE["plastic"] = ["U+45e9"]
UNICODE_TO_BLISS["U+45e9"] = ["plastic"]
BLISS_TO_UNICODE["mustard sauce"] = ["U+45ea"]
UNICODE_TO_BLISS["U+45ea"] = ["mustard sauce"]
BLISS_TO_UNICODE["mustard"] = ["U+45eb"]
UNICODE_TO_BLISS["U+45eb"] = ["mustard"]
BLISS_TO_UNICODE["oats"] = ["U+45ec"]
UNICODE_TO_BLISS["U+45ec"] = ["oats"]
BLISS_TO_UNICODE["Santa Claus"] = ["U+45ed"]
UNICODE_TO_BLISS["U+45ed"] = ["Santa Claus"]
BLISS_TO_UNICODE["Father Christmas"] = ["U+45ed"]
UNICODE_TO_BLISS["U+45ed"].append("Father Christmas")
BLISS_TO_UNICODE["Santa Claus,Father Christmas"] = ["U+45ed"]
UNICODE_TO_BLISS["U+45ed"].append("Santa Claus,Father Christmas")
BLISS_TO_UNICODE["Shiva"] = ["U+45ee"]
UNICODE_TO_BLISS["U+45ee"] = ["Shiva"]
BLISS_TO_UNICODE["ant"] = ["U+45ef"]
UNICODE_TO_BLISS["U+45ef"] = ["ant"]
BLISS_TO_UNICODE["deep fryer"] = ["U+45f0"]
UNICODE_TO_BLISS["U+45f0"] = ["deep fryer"]
BLISS_TO_UNICODE["tambourine"] = ["U+45f1"]
UNICODE_TO_BLISS["U+45f1"] = ["tambourine"]
BLISS_TO_UNICODE["go through"] = ["U+44de"]
UNICODE_TO_BLISS["U+44de"].append("go through")
BLISS_TO_UNICODE["penetrate,go through"] = ["U+44de"]
UNICODE_TO_BLISS["U+44de"].append("penetrate,go through")
BLISS_TO_UNICODE["equestrian"] = ["U+4434"]
UNICODE_TO_BLISS["U+4434"].append("equestrian")
BLISS_TO_UNICODE["horse rider,equestrian"] = ["U+4434"]
UNICODE_TO_BLISS["U+4434"].append("horse rider,equestrian")
BLISS_TO_UNICODE["kibbutz"] = ["U+45f2"]
UNICODE_TO_BLISS["U+45f2"] = ["kibbutz"]
BLISS_TO_UNICODE["multiply"] = ["U+45f3"]
UNICODE_TO_BLISS["U+45f3"] = ["multiply"]
BLISS_TO_UNICODE["librarian"] = ["U+45f4"]
UNICODE_TO_BLISS["U+45f4"] = ["librarian"]
BLISS_TO_UNICODE["bluebird"] = ["U+45f5"]
UNICODE_TO_BLISS["U+45f5"] = ["bluebird"]
BLISS_TO_UNICODE["tendon"] = ["U+45f6"]
UNICODE_TO_BLISS["U+45f6"] = ["tendon"]
BLISS_TO_UNICODE["hungry"] = ["U+45f7"]
UNICODE_TO_BLISS["U+45f7"] = ["hungry"]
BLISS_TO_UNICODE["masturbation"] = ["U+45f8"]
UNICODE_TO_BLISS["U+45f8"] = ["masturbation"]
BLISS_TO_UNICODE["to touch"] = ["U+45f9"]
UNICODE_TO_BLISS["U+45f9"] = ["to touch"]
BLISS_TO_UNICODE["perch"] = ["U+45fa"]
UNICODE_TO_BLISS["U+45fa"] = ["perch"]
BLISS_TO_UNICODE["cheat"] = ["U+45fb"]
UNICODE_TO_BLISS["U+45fb"] = ["cheat"]
BLISS_TO_UNICODE["witch"] = ["U+45fc"]
UNICODE_TO_BLISS["U+45fc"] = ["witch"]
BLISS_TO_UNICODE["nectarine"] = ["U+32f8"]
UNICODE_TO_BLISS["U+32f8"].append("nectarine")
BLISS_TO_UNICODE["peach,nectarine"] = ["U+32f8"]
UNICODE_TO_BLISS["U+32f8"].append("peach,nectarine")
BLISS_TO_UNICODE["Pegasus"] = ["U+45fd"]
UNICODE_TO_BLISS["U+45fd"] = ["Pegasus"]
BLISS_TO_UNICODE["wool"] = ["U+45fe"]
UNICODE_TO_BLISS["U+45fe"] = ["wool"]
BLISS_TO_UNICODE["control tower"] = ["U+45ff"]
UNICODE_TO_BLISS["U+45ff"] = ["control tower"]
BLISS_TO_UNICODE["neither"] = ["U+4600"]
UNICODE_TO_BLISS["U+4600"] = ["neither"]
BLISS_TO_UNICODE["Resurrection of Christ"] = ["U+4601"]
UNICODE_TO_BLISS["U+4601"] = ["Resurrection of Christ"]
BLISS_TO_UNICODE["resurrection"] = ["U+4602"]
UNICODE_TO_BLISS["U+4602"] = ["resurrection"]
BLISS_TO_UNICODE["buffalo"] = ["U+4603"]
UNICODE_TO_BLISS["U+4603"] = ["buffalo"]
BLISS_TO_UNICODE["bison"].append("U+4603")
UNICODE_TO_BLISS["U+4603"].append("bison")
BLISS_TO_UNICODE["buffalo,bison"] = ["U+4603"]
UNICODE_TO_BLISS["U+4603"].append("buffalo,bison")
BLISS_TO_UNICODE["hump"] = ["U+4604"]
UNICODE_TO_BLISS["U+4604"] = ["hump"]
BLISS_TO_UNICODE["picnic"] = ["U+4605"]
UNICODE_TO_BLISS["U+4605"] = ["picnic"]
BLISS_TO_UNICODE["stepson"] = ["U+4606"]
UNICODE_TO_BLISS["U+4606"] = ["stepson"]
BLISS_TO_UNICODE["voluntary"] = ["U+4607"]
UNICODE_TO_BLISS["U+4607"] = ["voluntary"]
BLISS_TO_UNICODE["volunteering"] = ["U+4608"]
UNICODE_TO_BLISS["U+4608"] = ["volunteering"]
BLISS_TO_UNICODE["amen"] = ["U+4609"]
UNICODE_TO_BLISS["U+4609"] = ["amen"]
BLISS_TO_UNICODE["shiva"] = ["U+460a"]
UNICODE_TO_BLISS["U+460a"] = ["shiva"]
BLISS_TO_UNICODE["to mourn"] = ["U+460b"]
UNICODE_TO_BLISS["U+460b"] = ["to mourn"]
BLISS_TO_UNICODE["hiss"] = ["U+460c"]
UNICODE_TO_BLISS["U+460c"] = ["hiss"]
BLISS_TO_UNICODE["when"] = ["U+460d"]
UNICODE_TO_BLISS["U+460d"] = ["when"]
BLISS_TO_UNICODE["what time"] = ["U+460d"]
UNICODE_TO_BLISS["U+460d"].append("what time")
BLISS_TO_UNICODE["when,what time"] = ["U+460d"]
UNICODE_TO_BLISS["U+460d"].append("when,what time")
BLISS_TO_UNICODE["tuning fork"] = ["U+460e"]
UNICODE_TO_BLISS["U+460e"] = ["tuning fork"]
BLISS_TO_UNICODE["Holy Spirit"] = ["U+460f"]
UNICODE_TO_BLISS["U+460f"] = ["Holy Spirit"]
BLISS_TO_UNICODE["oil tanker"] = ["U+4610"]
UNICODE_TO_BLISS["U+4610"] = ["oil tanker"]
BLISS_TO_UNICODE["male gender"] = ["U+35df"]
UNICODE_TO_BLISS["U+35df"].append("male gender")
BLISS_TO_UNICODE["activity,male gender"] = ["U+35df"]
UNICODE_TO_BLISS["U+35df"].append("activity,male gender")
BLISS_TO_UNICODE["polo"] = ["U+4611"]
UNICODE_TO_BLISS["U+4611"] = ["polo"]
BLISS_TO_UNICODE["brussels sprout"] = ["U+4612"]
UNICODE_TO_BLISS["U+4612"] = ["brussels sprout"]
BLISS_TO_UNICODE["pod"] = ["U+4613"]
UNICODE_TO_BLISS["U+4613"] = ["pod"]
BLISS_TO_UNICODE["multi sport event"] = ["U+4614"]
UNICODE_TO_BLISS["U+4614"] = ["multi sport event"]
BLISS_TO_UNICODE["multi-sport event"] = ["U+4614"]
UNICODE_TO_BLISS["U+4614"].append("multi-sport event")
BLISS_TO_UNICODE["turkey"] = ["U+4615"]
UNICODE_TO_BLISS["U+4615"] = ["turkey"]
BLISS_TO_UNICODE["ravioli"] = ["U+4616"]
UNICODE_TO_BLISS["U+4616"] = ["ravioli"]
BLISS_TO_UNICODE["direction"].append("U+41a9")
UNICODE_TO_BLISS["U+41a9"].append("direction")
BLISS_TO_UNICODE["to use"] = ["U+4617"]
UNICODE_TO_BLISS["U+4617"] = ["to use"]
BLISS_TO_UNICODE["tasteless"] = ["U+4618"]
UNICODE_TO_BLISS["U+4618"] = ["tasteless"]
BLISS_TO_UNICODE["careful"] = ["U+4619"]
UNICODE_TO_BLISS["U+4619"] = ["careful"]
BLISS_TO_UNICODE["dribble"] = ["U+461a"]
UNICODE_TO_BLISS["U+461a"] = ["dribble"]
BLISS_TO_UNICODE["robber"] = ["U+461b"]
UNICODE_TO_BLISS["U+461b"] = ["robber"]
BLISS_TO_UNICODE["to rob"] = ["U+461c"]
UNICODE_TO_BLISS["U+461c"] = ["to rob"]
BLISS_TO_UNICODE["cast"] = ["U+461d"]
UNICODE_TO_BLISS["U+461d"] = ["cast"]
BLISS_TO_UNICODE["oil gauge"] = ["U+461e"]
UNICODE_TO_BLISS["U+461e"] = ["oil gauge"]
BLISS_TO_UNICODE["sexual aid"] = ["U+461f"]
UNICODE_TO_BLISS["U+461f"] = ["sexual aid"]
BLISS_TO_UNICODE["participant"] = ["U+4620"]
UNICODE_TO_BLISS["U+4620"] = ["participant"]
BLISS_TO_UNICODE["macaroni"] = ["U+4621"]
UNICODE_TO_BLISS["U+4621"] = ["macaroni"]
BLISS_TO_UNICODE["driver"] = ["U+4622"]
UNICODE_TO_BLISS["U+4622"] = ["driver"]
BLISS_TO_UNICODE["chauffeur"] = ["U+4622"]
UNICODE_TO_BLISS["U+4622"].append("chauffeur")
BLISS_TO_UNICODE["driver,chauffeur"] = ["U+4622"]
UNICODE_TO_BLISS["U+4622"].append("driver,chauffeur")
BLISS_TO_UNICODE["footprint"] = ["U+4623"]
UNICODE_TO_BLISS["U+4623"] = ["footprint"]
BLISS_TO_UNICODE["magical"] = ["U+4624"]
UNICODE_TO_BLISS["U+4624"] = ["magical"]
BLISS_TO_UNICODE["sinner"] = ["U+4625"]
UNICODE_TO_BLISS["U+4625"] = ["sinner"]
BLISS_TO_UNICODE["sin"] = ["U+4626"]
UNICODE_TO_BLISS["U+4626"] = ["sin"]
BLISS_TO_UNICODE["to rub"] = ["U+4627"]
UNICODE_TO_BLISS["U+4627"] = ["to rub"]
BLISS_TO_UNICODE["blow"] = ["U+4628"]
UNICODE_TO_BLISS["U+4628"] = ["blow"]
BLISS_TO_UNICODE["blot"] = ["U+4629"]
UNICODE_TO_BLISS["U+4629"] = ["blot"]
BLISS_TO_UNICODE["to sacrifice"] = ["U+462a"]
UNICODE_TO_BLISS["U+462a"] = ["to sacrifice"]
BLISS_TO_UNICODE["rose"] = ["U+462b"]
UNICODE_TO_BLISS["U+462b"] = ["rose"]
BLISS_TO_UNICODE["star of David"] = ["U+462c"]
UNICODE_TO_BLISS["U+462c"] = ["star of David"]
BLISS_TO_UNICODE["symbol for Judaism"] = ["U+462d"]
UNICODE_TO_BLISS["U+462d"] = ["symbol for Judaism"]
BLISS_TO_UNICODE["cottage cheese"] = ["U+462e"]
UNICODE_TO_BLISS["U+462e"] = ["cottage cheese"]
BLISS_TO_UNICODE["make and tend a fire"] = ["U+462f"]
UNICODE_TO_BLISS["U+462f"] = ["make and tend a fire"]
BLISS_TO_UNICODE["inflation"] = ["U+4630"]
UNICODE_TO_BLISS["U+4630"] = ["inflation"]
BLISS_TO_UNICODE["furniture"] = ["U+4631"]
UNICODE_TO_BLISS["U+4631"] = ["furniture"]
BLISS_TO_UNICODE["towel"] = ["U+4632"]
UNICODE_TO_BLISS["U+4632"] = ["towel"]
BLISS_TO_UNICODE["bracelet"] = ["U+4633"]
UNICODE_TO_BLISS["U+4633"] = ["bracelet"]
BLISS_TO_UNICODE["trolleybus"] = ["U+4634"]
UNICODE_TO_BLISS["U+4634"] = ["trolleybus"]
BLISS_TO_UNICODE["perspiration"] = ["U+40c9"]
UNICODE_TO_BLISS["U+40c9"].append("perspiration")
BLISS_TO_UNICODE["sweat,perspiration"] = ["U+40c9"]
UNICODE_TO_BLISS["U+40c9"].append("sweat,perspiration")
BLISS_TO_UNICODE["Danish"] = ["U+4635"]
UNICODE_TO_BLISS["U+4635"] = ["Danish"]
BLISS_TO_UNICODE["New Year"] = ["U+4636"]
UNICODE_TO_BLISS["U+4636"] = ["New Year"]
BLISS_TO_UNICODE["head lamp"] = ["U+4637"]
UNICODE_TO_BLISS["U+4637"] = ["head lamp"]
BLISS_TO_UNICODE["poem"] = ["U+4638"]
UNICODE_TO_BLISS["U+4638"] = ["poem"]
BLISS_TO_UNICODE["communicate"] = ["U+4639"]
UNICODE_TO_BLISS["U+4639"] = ["communicate"]
BLISS_TO_UNICODE["right angle"].append("U+3539")
UNICODE_TO_BLISS["U+3539"].append("right angle")
BLISS_TO_UNICODE["terrified"] = ["U+463a"]
UNICODE_TO_BLISS["U+463a"] = ["terrified"]
BLISS_TO_UNICODE["shrimp"] = ["U+463c"]
UNICODE_TO_BLISS["U+463c"] = ["shrimp"]
BLISS_TO_UNICODE["stand"] = ["U+463d"]
UNICODE_TO_BLISS["U+463d"] = ["stand"]
BLISS_TO_UNICODE["ox"] = ["U+463e"]
UNICODE_TO_BLISS["U+463e"] = ["ox"]
BLISS_TO_UNICODE["chive"] = ["U+463f"]
UNICODE_TO_BLISS["U+463f"] = ["chive"]
BLISS_TO_UNICODE["syringe"] = ["U+4640"]
UNICODE_TO_BLISS["U+4640"] = ["syringe"]
BLISS_TO_UNICODE["fishing"] = ["U+4641"]
UNICODE_TO_BLISS["U+4641"] = ["fishing"]
BLISS_TO_UNICODE["sacrament of confirmation"] = ["U+4642"]
UNICODE_TO_BLISS["U+4642"] = ["sacrament of confirmation"]
BLISS_TO_UNICODE["promote"] = ["U+4643"]
UNICODE_TO_BLISS["U+4643"] = ["promote"]
BLISS_TO_UNICODE["tiptoe"] = ["U+4644"]
UNICODE_TO_BLISS["U+4644"] = ["tiptoe"]
BLISS_TO_UNICODE["hot tray"] = ["U+4645"]
UNICODE_TO_BLISS["U+4645"] = ["hot tray"]
BLISS_TO_UNICODE["beginning of year"] = ["U+4646"]
UNICODE_TO_BLISS["U+4646"] = ["beginning of year"]
BLISS_TO_UNICODE["bishop"] = ["U+4647"]
UNICODE_TO_BLISS["U+4647"] = ["bishop"]
BLISS_TO_UNICODE["biochemistry"] = ["U+4648"]
UNICODE_TO_BLISS["U+4648"] = ["biochemistry"]
BLISS_TO_UNICODE["signature stamp"] = ["U+4649"]
UNICODE_TO_BLISS["U+4649"] = ["signature stamp"]
BLISS_TO_UNICODE["classmate"] = ["U+464a"]
UNICODE_TO_BLISS["U+464a"] = ["classmate"]
BLISS_TO_UNICODE["Earth axis"] = ["U+464b"]
UNICODE_TO_BLISS["U+464b"] = ["Earth axis"]
BLISS_TO_UNICODE["lipstick"] = ["U+464c"]
UNICODE_TO_BLISS["U+464c"] = ["lipstick"]
BLISS_TO_UNICODE["guard duty"] = ["U+464d"]
UNICODE_TO_BLISS["U+464d"] = ["guard duty"]
BLISS_TO_UNICODE["mother in law"] = ["U+464e"]
UNICODE_TO_BLISS["U+464e"] = ["mother in law"]
BLISS_TO_UNICODE["mother-in-law"] = ["U+464e"]
UNICODE_TO_BLISS["U+464e"].append("mother-in-law")
BLISS_TO_UNICODE["disk"].append("U+37de")
UNICODE_TO_BLISS["U+37de"].append("disk")
BLISS_TO_UNICODE["disc,disk"] = ["U+37de"]
UNICODE_TO_BLISS["U+37de"].append("disc,disk")
BLISS_TO_UNICODE["pictograph of cigarette"] = ["U+464f"]
UNICODE_TO_BLISS["U+464f"] = ["pictograph of cigarette"]
BLISS_TO_UNICODE["pictograph of smoking pipe"] = ["U+4650"]
UNICODE_TO_BLISS["U+4650"] = ["pictograph of smoking pipe"]
BLISS_TO_UNICODE["follow"] = ["U+4651"]
UNICODE_TO_BLISS["U+4651"] = ["follow"]
BLISS_TO_UNICODE["pasta wheel"] = ["U+4652"]
UNICODE_TO_BLISS["U+4652"] = ["pasta wheel"]
BLISS_TO_UNICODE["programme"] = ["U+3b1b"]
UNICODE_TO_BLISS["U+3b1b"].append("programme")
BLISS_TO_UNICODE["program,programme"] = ["U+3b1b"]
UNICODE_TO_BLISS["U+3b1b"].append("program,programme")
BLISS_TO_UNICODE["presentation"] = ["U+3b1b"]
UNICODE_TO_BLISS["U+3b1b"].append("presentation")
BLISS_TO_UNICODE["program,programme,presentation"] = ["U+3b1b"]
UNICODE_TO_BLISS["U+3b1b"].append("program,programme,presentation")
BLISS_TO_UNICODE["dairy"] = ["U+4653"]
UNICODE_TO_BLISS["U+4653"] = ["dairy"]
BLISS_TO_UNICODE["painter"] = ["U+4654"]
UNICODE_TO_BLISS["U+4654"] = ["painter"]
BLISS_TO_UNICODE["fax"] = ["U+4655"]
UNICODE_TO_BLISS["U+4655"] = ["fax"]
BLISS_TO_UNICODE["chameleon"] = ["U+4656"]
UNICODE_TO_BLISS["U+4656"] = ["chameleon"]
BLISS_TO_UNICODE["to change"] = ["U+4657"]
UNICODE_TO_BLISS["U+4657"] = ["to change"]
BLISS_TO_UNICODE["shellfish salad"] = ["U+4658"]
UNICODE_TO_BLISS["U+4658"] = ["shellfish salad"]
BLISS_TO_UNICODE["psychologist"] = ["U+4659"]
UNICODE_TO_BLISS["U+4659"] = ["psychologist"]
BLISS_TO_UNICODE["awful"] = ["U+465a"]
UNICODE_TO_BLISS["U+465a"] = ["awful"]
BLISS_TO_UNICODE["saxophone"] = ["U+465b"]
UNICODE_TO_BLISS["U+465b"] = ["saxophone"]
BLISS_TO_UNICODE["tea"] = ["U+465c"]
UNICODE_TO_BLISS["U+465c"] = ["tea"]
BLISS_TO_UNICODE["imported"] = ["U+465d"]
UNICODE_TO_BLISS["U+465d"] = ["imported"]
BLISS_TO_UNICODE["crust"].append("U+358f")
UNICODE_TO_BLISS["U+358f"].append("crust")
BLISS_TO_UNICODE["shell,crust"] = ["U+358f"]
UNICODE_TO_BLISS["U+358f"].append("shell,crust")
BLISS_TO_UNICODE["squeeze"].append("U+3240")
UNICODE_TO_BLISS["U+3240"].append("squeeze")
BLISS_TO_UNICODE["crush,squeeze"] = ["U+3240"]
UNICODE_TO_BLISS["U+3240"].append("crush,squeeze")
BLISS_TO_UNICODE["christian"] = ["U+465f"]
UNICODE_TO_BLISS["U+465f"] = ["christian"]
BLISS_TO_UNICODE["summer day camp"] = ["U+4660"]
UNICODE_TO_BLISS["U+4660"] = ["summer day camp"]
BLISS_TO_UNICODE["behaviour"] = ["U+4661"]
UNICODE_TO_BLISS["U+4661"] = ["behaviour"]
BLISS_TO_UNICODE["tragedy"] = ["U+4662"]
UNICODE_TO_BLISS["U+4662"] = ["tragedy"]
BLISS_TO_UNICODE["milkshake"] = ["U+4663"]
UNICODE_TO_BLISS["U+4663"] = ["milkshake"]
BLISS_TO_UNICODE["bus lane"] = ["U+4664"]
UNICODE_TO_BLISS["U+4664"] = ["bus lane"]
BLISS_TO_UNICODE["pictograph of two tablets of the laws"] = ["U+4665"]
UNICODE_TO_BLISS["U+4665"] = ["pictograph of two tablets of the laws"]
BLISS_TO_UNICODE["bread with seeds"] = ["U+4666"]
UNICODE_TO_BLISS["U+4666"] = ["bread with seeds"]
BLISS_TO_UNICODE["flap"] = ["U+333f"]
UNICODE_TO_BLISS["U+333f"].append("flap")
BLISS_TO_UNICODE["leaf,flap"] = ["U+333f"]
UNICODE_TO_BLISS["U+333f"].append("leaf,flap")
BLISS_TO_UNICODE["Good night"] = ["U+4667"]
UNICODE_TO_BLISS["U+4667"] = ["Good night"]
BLISS_TO_UNICODE["winter house"] = ["U+4668"]
UNICODE_TO_BLISS["U+4668"] = ["winter house"]
BLISS_TO_UNICODE["plant louse"] = ["U+4669"]
UNICODE_TO_BLISS["U+4669"] = ["plant louse"]
BLISS_TO_UNICODE["plant-louse"] = ["U+4669"]
UNICODE_TO_BLISS["U+4669"].append("plant-louse")
BLISS_TO_UNICODE["flax"] = ["U+466a"]
UNICODE_TO_BLISS["U+466a"] = ["flax"]
BLISS_TO_UNICODE["short time home"] = ["U+466b"]
UNICODE_TO_BLISS["U+466b"] = ["short time home"]
BLISS_TO_UNICODE["textile craft"] = ["U+466c"]
UNICODE_TO_BLISS["U+466c"] = ["textile craft"]
BLISS_TO_UNICODE["embarrassing"] = ["U+466d"]
UNICODE_TO_BLISS["U+466d"] = ["embarrassing"]
BLISS_TO_UNICODE["religious service"] = ["U+466e"]
UNICODE_TO_BLISS["U+466e"] = ["religious service"]
BLISS_TO_UNICODE["solar system"] = ["U+466f"]
UNICODE_TO_BLISS["U+466f"] = ["solar system"]
BLISS_TO_UNICODE["stone material"] = ["U+4670"]
UNICODE_TO_BLISS["U+4670"] = ["stone material"]
BLISS_TO_UNICODE["goat"] = ["U+4671"]
UNICODE_TO_BLISS["U+4671"] = ["goat"]
BLISS_TO_UNICODE["sandwich"] = ["U+4672"]
UNICODE_TO_BLISS["U+4672"] = ["sandwich"]
BLISS_TO_UNICODE["horseshoe nail"] = ["U+4673"]
UNICODE_TO_BLISS["U+4673"] = ["horseshoe nail"]
BLISS_TO_UNICODE["repair room"] = ["U+4674"]
UNICODE_TO_BLISS["U+4674"] = ["repair room"]
BLISS_TO_UNICODE["March"] = ["U+4675"]
UNICODE_TO_BLISS["U+4675"] = ["March"]
BLISS_TO_UNICODE["pray"] = ["U+4676"]
UNICODE_TO_BLISS["U+4676"] = ["pray"]
BLISS_TO_UNICODE["power plant"] = ["U+4677"]
UNICODE_TO_BLISS["U+4677"] = ["power plant"]
BLISS_TO_UNICODE["power station"] = ["U+4677"]
UNICODE_TO_BLISS["U+4677"].append("power station")
BLISS_TO_UNICODE["power plant,power station"] = ["U+4677"]
UNICODE_TO_BLISS["U+4677"].append("power plant,power station")
BLISS_TO_UNICODE["hunter"] = ["U+4678"]
UNICODE_TO_BLISS["U+4678"] = ["hunter"]
BLISS_TO_UNICODE["adventurous"] = ["U+4679"]
UNICODE_TO_BLISS["U+4679"] = ["adventurous"]
BLISS_TO_UNICODE["mathematician"] = ["U+467a"]
UNICODE_TO_BLISS["U+467a"] = ["mathematician"]
BLISS_TO_UNICODE["athletics"] = ["U+467b"]
UNICODE_TO_BLISS["U+467b"] = ["athletics"]
BLISS_TO_UNICODE["Vishnu"] = ["U+467c"]
UNICODE_TO_BLISS["U+467c"] = ["Vishnu"]
BLISS_TO_UNICODE["hill"] = ["U+467d"]
UNICODE_TO_BLISS["U+467d"] = ["hill"]
BLISS_TO_UNICODE["cookie"] = ["U+467e"]
UNICODE_TO_BLISS["U+467e"] = ["cookie"]
BLISS_TO_UNICODE["biscuit"] = ["U+467e"]
UNICODE_TO_BLISS["U+467e"].append("biscuit")
BLISS_TO_UNICODE["cookie,biscuit"] = ["U+467e"]
UNICODE_TO_BLISS["U+467e"].append("cookie,biscuit")
BLISS_TO_UNICODE["dysarthria"].append("U+3d5a")
UNICODE_TO_BLISS["U+3d5a"].append("dysarthria")
BLISS_TO_UNICODE["speech impairment,dysarthria"] = ["U+3d5a"]
UNICODE_TO_BLISS["U+3d5a"].append("speech impairment,dysarthria")
BLISS_TO_UNICODE["Iyar"] = ["U+467f"]
UNICODE_TO_BLISS["U+467f"] = ["Iyar"]
BLISS_TO_UNICODE["sea lion"] = ["U+4680"]
UNICODE_TO_BLISS["U+4680"] = ["sea lion"]
BLISS_TO_UNICODE["to shout"] = ["U+4681"]
UNICODE_TO_BLISS["U+4681"] = ["to shout"]
BLISS_TO_UNICODE["snowboarding"] = ["U+4682"]
UNICODE_TO_BLISS["U+4682"] = ["snowboarding"]
BLISS_TO_UNICODE["feed"] = ["U+4683"]
UNICODE_TO_BLISS["U+4683"] = ["feed"]
BLISS_TO_UNICODE["lunch box"] = ["U+4684"]
UNICODE_TO_BLISS["U+4684"] = ["lunch box"]
BLISS_TO_UNICODE["speedometer"] = ["U+4685"]
UNICODE_TO_BLISS["U+4685"] = ["speedometer"]
BLISS_TO_UNICODE["pensioner"] = ["U+4686"]
UNICODE_TO_BLISS["U+4686"] = ["pensioner"]
BLISS_TO_UNICODE["exploded"] = ["U+4687"]
UNICODE_TO_BLISS["U+4687"] = ["exploded"]
BLISS_TO_UNICODE["clothing shop"] = ["U+4688"]
UNICODE_TO_BLISS["U+4688"] = ["clothing shop"]
BLISS_TO_UNICODE["surfboard"] = ["U+4689"]
UNICODE_TO_BLISS["U+4689"] = ["surfboard"]
BLISS_TO_UNICODE["king"] = ["U+468a"]
UNICODE_TO_BLISS["U+468a"] = ["king"]
BLISS_TO_UNICODE["architect"] = ["U+468b"]
UNICODE_TO_BLISS["U+468b"] = ["architect"]
BLISS_TO_UNICODE["summer day"] = ["U+468d"]
UNICODE_TO_BLISS["U+468d"] = ["summer day"]
BLISS_TO_UNICODE["sister in law"] = ["U+468e"]
UNICODE_TO_BLISS["U+468e"] = ["sister in law"]
BLISS_TO_UNICODE["sister-in-law"] = ["U+468e"]
UNICODE_TO_BLISS["U+468e"].append("sister-in-law")
BLISS_TO_UNICODE["winter day"] = ["U+468f"]
UNICODE_TO_BLISS["U+468f"] = ["winter day"]
BLISS_TO_UNICODE["D"] = ["U+4690"]
UNICODE_TO_BLISS["U+4690"] = ["D"]
BLISS_TO_UNICODE["E"] = ["U+4691"]
UNICODE_TO_BLISS["U+4691"] = ["E"]
BLISS_TO_UNICODE["banjo"] = ["U+4692"]
UNICODE_TO_BLISS["U+4692"] = ["banjo"]
BLISS_TO_UNICODE["react"] = ["U+4693"]
UNICODE_TO_BLISS["U+4693"] = ["react"]
BLISS_TO_UNICODE["daughter in law"] = ["U+4694"]
UNICODE_TO_BLISS["U+4694"] = ["daughter in law"]
BLISS_TO_UNICODE["daughter-in-law"] = ["U+4694"]
UNICODE_TO_BLISS["U+4694"].append("daughter-in-law")
BLISS_TO_UNICODE["constitution"] = ["U+4695"]
UNICODE_TO_BLISS["U+4695"] = ["constitution"]
BLISS_TO_UNICODE["make believe man"] = ["U+4696"]
UNICODE_TO_BLISS["U+4696"] = ["make believe man"]
BLISS_TO_UNICODE["make-believe man"].append("U+4696")
UNICODE_TO_BLISS["U+4696"].append("make-believe man")
BLISS_TO_UNICODE["shepherd"] = ["U+4697"]
UNICODE_TO_BLISS["U+4697"] = ["shepherd"]
BLISS_TO_UNICODE["hit"] = ["U+4698"]
UNICODE_TO_BLISS["U+4698"] = ["hit"]
BLISS_TO_UNICODE["whistle"] = ["U+4699"]
UNICODE_TO_BLISS["U+4699"] = ["whistle"]
BLISS_TO_UNICODE["longest"] = ["U+469a"]
UNICODE_TO_BLISS["U+469a"] = ["longest"]
BLISS_TO_UNICODE["foster parent"] = ["U+469b"]
UNICODE_TO_BLISS["U+469b"] = ["foster parent"]
BLISS_TO_UNICODE["ice skating rink"] = ["U+469c"]
UNICODE_TO_BLISS["U+469c"] = ["ice skating rink"]
BLISS_TO_UNICODE["snowstorm"] = ["U+469d"]
UNICODE_TO_BLISS["U+469d"] = ["snowstorm"]
BLISS_TO_UNICODE["vulva"] = ["U+469e"]
UNICODE_TO_BLISS["U+469e"] = ["vulva"]
BLISS_TO_UNICODE["farrier"] = ["U+469f"]
UNICODE_TO_BLISS["U+469f"] = ["farrier"]
BLISS_TO_UNICODE["equilateral triangle"] = ["U+46a0"]
UNICODE_TO_BLISS["U+46a0"] = ["equilateral triangle"]
BLISS_TO_UNICODE["corruption"] = ["U+46a1"]
UNICODE_TO_BLISS["U+46a1"] = ["corruption"]
BLISS_TO_UNICODE["religious fanatic"] = ["U+46a2"]
UNICODE_TO_BLISS["U+46a2"] = ["religious fanatic"]
BLISS_TO_UNICODE["pictograph of Union Jack flag pattern"] = ["U+46a3"]
UNICODE_TO_BLISS["U+46a3"] = ["pictograph of Union Jack flag pattern"]
BLISS_TO_UNICODE["sole"] = ["U+46a4"]
UNICODE_TO_BLISS["U+46a4"] = ["sole"]
BLISS_TO_UNICODE["fire extinguisher"] = ["U+46a5"]
UNICODE_TO_BLISS["U+46a5"] = ["fire extinguisher"]
BLISS_TO_UNICODE["counter forces"] = ["U+324f"]
UNICODE_TO_BLISS["U+324f"].append("counter forces")
BLISS_TO_UNICODE["opposing forces,counter-forces"] = ["U+324f"]
UNICODE_TO_BLISS["U+324f"].append("opposing forces,counter-forces")
BLISS_TO_UNICODE["ampullae"] = ["U+46a6"]
UNICODE_TO_BLISS["U+46a6"] = ["ampullae"]
BLISS_TO_UNICODE["prescription"] = ["U+46a7"]
UNICODE_TO_BLISS["U+46a7"] = ["prescription"]
BLISS_TO_UNICODE["interrogate"] = ["U+46a8"]
UNICODE_TO_BLISS["U+46a8"] = ["interrogate"]
BLISS_TO_UNICODE["Superman"] = ["U+46a9"]
UNICODE_TO_BLISS["U+46a9"] = ["Superman"]
BLISS_TO_UNICODE["S"] = ["U+46aa"]
UNICODE_TO_BLISS["U+46aa"] = ["S"]
BLISS_TO_UNICODE["home worker"] = ["U+46ab"]
UNICODE_TO_BLISS["U+46ab"] = ["home worker"]
BLISS_TO_UNICODE["camping mat"] = ["U+46ac"]
UNICODE_TO_BLISS["U+46ac"] = ["camping mat"]
BLISS_TO_UNICODE["sleeping mat"] = ["U+46ac"]
UNICODE_TO_BLISS["U+46ac"].append("sleeping mat")
BLISS_TO_UNICODE["camping mat,sleeping mat"] = ["U+46ac"]
UNICODE_TO_BLISS["U+46ac"].append("camping mat,sleeping mat")
BLISS_TO_UNICODE["strategy"] = ["U+46ae"]
UNICODE_TO_BLISS["U+46ae"] = ["strategy"]
BLISS_TO_UNICODE["who,whom"] = ["U+360e"]
UNICODE_TO_BLISS["U+360e"].append("who,whom")
BLISS_TO_UNICODE["Toffle"] = ["U+46af"]
UNICODE_TO_BLISS["U+46af"] = ["Toffle"]
BLISS_TO_UNICODE["demand"] = ["U+46b0"]
UNICODE_TO_BLISS["U+46b0"] = ["demand"]
BLISS_TO_UNICODE["tomorrow night"] = ["U+46b1"]
UNICODE_TO_BLISS["U+46b1"] = ["tomorrow night"]
BLISS_TO_UNICODE["price rise"] = ["U+46b2"]
UNICODE_TO_BLISS["U+46b2"] = ["price rise"]
BLISS_TO_UNICODE["Italy"] = ["U+46b3"]
UNICODE_TO_BLISS["U+46b3"] = ["Italy"]
BLISS_TO_UNICODE["rib"] = ["U+46b4"]
UNICODE_TO_BLISS["U+46b4"] = ["rib"]
BLISS_TO_UNICODE["biochemist"] = ["U+46b5"]
UNICODE_TO_BLISS["U+46b5"] = ["biochemist"]
BLISS_TO_UNICODE["movie disc"].append("U+4124")
UNICODE_TO_BLISS["U+4124"].append("movie disc")
BLISS_TO_UNICODE["DVD,movie disc"] = ["U+4124"]
UNICODE_TO_BLISS["U+4124"].append("DVD,movie disc")
BLISS_TO_UNICODE["birch"] = ["U+46b6"]
UNICODE_TO_BLISS["U+46b6"] = ["birch"]
BLISS_TO_UNICODE["contact sports"] = ["U+46b7"]
UNICODE_TO_BLISS["U+46b7"] = ["contact sports"]
BLISS_TO_UNICODE["lower"] = ["U+46b8"]
UNICODE_TO_BLISS["U+46b8"] = ["lower"]
BLISS_TO_UNICODE["horse racing"] = ["U+46b9"]
UNICODE_TO_BLISS["U+46b9"] = ["horse racing"]
BLISS_TO_UNICODE["homeward"] = ["U+46ba"]
UNICODE_TO_BLISS["U+46ba"] = ["homeward"]
BLISS_TO_UNICODE["margarine"] = ["U+46bb"]
UNICODE_TO_BLISS["U+46bb"] = ["margarine"]
BLISS_TO_UNICODE["self raising flour"] = ["U+46bc"]
UNICODE_TO_BLISS["U+46bc"] = ["self raising flour"]
BLISS_TO_UNICODE["self-raising flour"] = ["U+46bc"]
UNICODE_TO_BLISS["U+46bc"].append("self-raising flour")
BLISS_TO_UNICODE["rocking chair"] = ["U+46bd"]
UNICODE_TO_BLISS["U+46bd"] = ["rocking chair"]
BLISS_TO_UNICODE["action in favour of"] = ["U+46be"]
UNICODE_TO_BLISS["U+46be"] = ["action in favour of"]
BLISS_TO_UNICODE["nipple"] = ["U+46bf"]
UNICODE_TO_BLISS["U+46bf"] = ["nipple"]
BLISS_TO_UNICODE["piglet"] = ["U+46c0"]
UNICODE_TO_BLISS["U+46c0"] = ["piglet"]
BLISS_TO_UNICODE["sitting mat"] = ["U+46c1"]
UNICODE_TO_BLISS["U+46c1"] = ["sitting mat"]
BLISS_TO_UNICODE["vacuum cleaner"] = ["U+46c2"]
UNICODE_TO_BLISS["U+46c2"] = ["vacuum cleaner"]
BLISS_TO_UNICODE["porridge"] = ["U+46c3"]
UNICODE_TO_BLISS["U+46c3"] = ["porridge"]
BLISS_TO_UNICODE["zombie"] = ["U+46c4"]
UNICODE_TO_BLISS["U+46c4"] = ["zombie"]
BLISS_TO_UNICODE["altimeter"] = ["U+46c5"]
UNICODE_TO_BLISS["U+46c5"] = ["altimeter"]
BLISS_TO_UNICODE["tefillin"] = ["U+46c6"]
UNICODE_TO_BLISS["U+46c6"] = ["tefillin"]
BLISS_TO_UNICODE["circumcision ceremony"] = ["U+46c7"]
UNICODE_TO_BLISS["U+46c7"] = ["circumcision ceremony"]
BLISS_TO_UNICODE["hair spray"] = ["U+46c8"]
UNICODE_TO_BLISS["U+46c8"] = ["hair spray"]
BLISS_TO_UNICODE["external hard drive"] = ["U+46c9"]
UNICODE_TO_BLISS["U+46c9"] = ["external hard drive"]
BLISS_TO_UNICODE["camping stove"] = ["U+46ca"]
UNICODE_TO_BLISS["U+46ca"] = ["camping stove"]
BLISS_TO_UNICODE["canal"] = ["U+46cb"]
UNICODE_TO_BLISS["U+46cb"] = ["canal"]
BLISS_TO_UNICODE["waterway"] = ["U+46cc"]
UNICODE_TO_BLISS["U+46cc"] = ["waterway"]
BLISS_TO_UNICODE["Belarus"] = ["U+46cd"]
UNICODE_TO_BLISS["U+46cd"] = ["Belarus"]
BLISS_TO_UNICODE["wave length"] = ["U+46ce"]
UNICODE_TO_BLISS["U+46ce"] = ["wave length"]
BLISS_TO_UNICODE["lenght"] = ["U+46cf"]
UNICODE_TO_BLISS["U+46cf"] = ["lenght"]
BLISS_TO_UNICODE["hydropower"] = ["U+46d0"]
UNICODE_TO_BLISS["U+46d0"] = ["hydropower"]
BLISS_TO_UNICODE["hydro energy"] = ["U+46d0"]
UNICODE_TO_BLISS["U+46d0"].append("hydro energy")
BLISS_TO_UNICODE["hydropower,hydro energy"] = ["U+46d0"]
UNICODE_TO_BLISS["U+46d0"].append("hydropower,hydro energy")
BLISS_TO_UNICODE["tack room"] = ["U+46d1"]
UNICODE_TO_BLISS["U+46d1"] = ["tack room"]
BLISS_TO_UNICODE["sled sport"] = ["U+46d2"]
UNICODE_TO_BLISS["U+46d2"] = ["sled sport"]
BLISS_TO_UNICODE["crane"] = ["U+46d3"]
UNICODE_TO_BLISS["U+46d3"] = ["crane"]
BLISS_TO_UNICODE["penguin"] = ["U+46d4"]
UNICODE_TO_BLISS["U+46d4"] = ["penguin"]
BLISS_TO_UNICODE["forefather"] = ["U+46d5"]
UNICODE_TO_BLISS["U+46d5"] = ["forefather"]
BLISS_TO_UNICODE["apricot"] = ["U+46d6"]
UNICODE_TO_BLISS["U+46d6"] = ["apricot"]
BLISS_TO_UNICODE["summer house"] = ["U+46d7"]
UNICODE_TO_BLISS["U+46d7"] = ["summer house"]
BLISS_TO_UNICODE["summerhouse"] = ["U+46d7"]
UNICODE_TO_BLISS["U+46d7"].append("summerhouse")
BLISS_TO_UNICODE["summer house,summerhouse"] = ["U+46d7"]
UNICODE_TO_BLISS["U+46d7"].append("summer house,summerhouse")
BLISS_TO_UNICODE["sometimes"] = ["U+46d8"]
UNICODE_TO_BLISS["U+46d8"] = ["sometimes"]
BLISS_TO_UNICODE["Father's Day"] = ["U+46d9"]
UNICODE_TO_BLISS["U+46d9"] = ["Father's Day"]
BLISS_TO_UNICODE["Earth"] = ["U+46da"]
UNICODE_TO_BLISS["U+46da"] = ["Earth"]
BLISS_TO_UNICODE["Tellus"] = ["U+46da"]
UNICODE_TO_BLISS["U+46da"].append("Tellus")
BLISS_TO_UNICODE["Earth,Tellus"] = ["U+46da"]
UNICODE_TO_BLISS["U+46da"].append("Earth,Tellus")
BLISS_TO_UNICODE["rainbow"] = ["U+46db"]
UNICODE_TO_BLISS["U+46db"] = ["rainbow"]
BLISS_TO_UNICODE["rainy"] = ["U+46dc"]
UNICODE_TO_BLISS["U+46dc"] = ["rainy"]
BLISS_TO_UNICODE["seeds"] = ["U+46dd"]
UNICODE_TO_BLISS["U+46dd"] = ["seeds"]
BLISS_TO_UNICODE["ice coated"] = ["U+46de"]
UNICODE_TO_BLISS["U+46de"] = ["ice coated"]
BLISS_TO_UNICODE["ice covered"] = ["U+46de"]
UNICODE_TO_BLISS["U+46de"].append("ice covered")
BLISS_TO_UNICODE["ice coated,ice covered"] = ["U+46de"]
UNICODE_TO_BLISS["U+46de"].append("ice coated,ice covered")
BLISS_TO_UNICODE["fertilized"] = ["U+46df"]
UNICODE_TO_BLISS["U+46df"] = ["fertilized"]
BLISS_TO_UNICODE["weigh"] = ["U+46e0"]
UNICODE_TO_BLISS["U+46e0"] = ["weigh"]
BLISS_TO_UNICODE["wheelchair tricycle"] = ["U+46e1"]
UNICODE_TO_BLISS["U+46e1"] = ["wheelchair tricycle"]
BLISS_TO_UNICODE["military plane"] = ["U+46e2"]
UNICODE_TO_BLISS["U+46e2"] = ["military plane"]
BLISS_TO_UNICODE["once"] = ["U+46e3"]
UNICODE_TO_BLISS["U+46e3"] = ["once"]
BLISS_TO_UNICODE["Libra"] = ["U+46e4"]
UNICODE_TO_BLISS["U+46e4"] = ["Libra"]
BLISS_TO_UNICODE["philosopher"] = ["U+46e5"]
UNICODE_TO_BLISS["U+46e5"] = ["philosopher"]
BLISS_TO_UNICODE["discordant"] = ["U+46e6"]
UNICODE_TO_BLISS["U+46e6"] = ["discordant"]
BLISS_TO_UNICODE["protection of the environment"] = ["U+46e7"]
UNICODE_TO_BLISS["U+46e7"] = ["protection of the environment"]
BLISS_TO_UNICODE["include"] = ["U+46e8"]
UNICODE_TO_BLISS["U+46e8"] = ["include"]
BLISS_TO_UNICODE["half an hour"] = ["U+46e9"]
UNICODE_TO_BLISS["U+46e9"] = ["half an hour"]
BLISS_TO_UNICODE["30"] = ["U+46ea"]
UNICODE_TO_BLISS["U+46ea"] = ["30"]
BLISS_TO_UNICODE["confirmation"] = ["U+46eb"]
UNICODE_TO_BLISS["U+46eb"] = ["confirmation"]
BLISS_TO_UNICODE["ladle"] = ["U+46ec"]
UNICODE_TO_BLISS["U+46ec"] = ["ladle"]
BLISS_TO_UNICODE["along with"] = ["U+46ed"]
UNICODE_TO_BLISS["U+46ed"] = ["along with"]
BLISS_TO_UNICODE["cardiovascular system"] = ["U+46ee"]
UNICODE_TO_BLISS["U+46ee"] = ["cardiovascular system"]
BLISS_TO_UNICODE["pleat"] = ["U+33d9"]
UNICODE_TO_BLISS["U+33d9"].append("pleat")
BLISS_TO_UNICODE["fold,pleat"] = ["U+33d9"]
UNICODE_TO_BLISS["U+33d9"].append("fold,pleat")
BLISS_TO_UNICODE["wrestling"] = ["U+46ef"]
UNICODE_TO_BLISS["U+46ef"] = ["wrestling"]
BLISS_TO_UNICODE["sacrament of holy orders"] = ["U+46f0"]
UNICODE_TO_BLISS["U+46f0"] = ["sacrament of holy orders"]
BLISS_TO_UNICODE["meatball"] = ["U+46f1"]
UNICODE_TO_BLISS["U+46f1"] = ["meatball"]
BLISS_TO_UNICODE["core activity"] = ["U+46f2"]
UNICODE_TO_BLISS["U+46f2"] = ["core activity"]
BLISS_TO_UNICODE["scales"] = ["U+46f3"]
UNICODE_TO_BLISS["U+46f3"] = ["scales"]
BLISS_TO_UNICODE["to weigh"] = ["U+46f4"]
UNICODE_TO_BLISS["U+46f4"] = ["to weigh"]
BLISS_TO_UNICODE["respirator"] = ["U+46f5"]
UNICODE_TO_BLISS["U+46f5"] = ["respirator"]
BLISS_TO_UNICODE["redo"] = ["U+46f6"]
UNICODE_TO_BLISS["U+46f6"] = ["redo"]
BLISS_TO_UNICODE["to add"] = ["U+46f7"]
UNICODE_TO_BLISS["U+46f7"] = ["to add"]
BLISS_TO_UNICODE["use"].append("U+3a22")
UNICODE_TO_BLISS["U+3a22"].append("use")
BLISS_TO_UNICODE["usage,use"] = ["U+3a22"]
UNICODE_TO_BLISS["U+3a22"].append("usage,use")
BLISS_TO_UNICODE["fee"] = ["U+46f8"]
UNICODE_TO_BLISS["U+46f8"] = ["fee"]
BLISS_TO_UNICODE["otolaryngologist"] = ["U+46f9"]
UNICODE_TO_BLISS["U+46f9"] = ["otolaryngologist"]
BLISS_TO_UNICODE["rhythm method"] = ["U+46fa"]
UNICODE_TO_BLISS["U+46fa"] = ["rhythm method"]
BLISS_TO_UNICODE["musician"] = ["U+46fb"]
UNICODE_TO_BLISS["U+46fb"] = ["musician"]
BLISS_TO_UNICODE["mechanical engineer"] = ["U+46fc"]
UNICODE_TO_BLISS["U+46fc"] = ["mechanical engineer"]
BLISS_TO_UNICODE["rape"] = ["U+46fd"]
UNICODE_TO_BLISS["U+46fd"] = ["rape"]
BLISS_TO_UNICODE["sit"] = ["U+46fe"]
UNICODE_TO_BLISS["U+46fe"] = ["sit"]
BLISS_TO_UNICODE["Arabic numeral 6 small"] = ["U+46ff"]
UNICODE_TO_BLISS["U+46ff"] = ["Arabic numeral 6 small"]
BLISS_TO_UNICODE["goldsmith"] = ["U+4700"]
UNICODE_TO_BLISS["U+4700"] = ["goldsmith"]
BLISS_TO_UNICODE["long jump"] = ["U+4701"]
UNICODE_TO_BLISS["U+4701"] = ["long jump"]
BLISS_TO_UNICODE["hurdles"] = ["U+4702"]
UNICODE_TO_BLISS["U+4702"] = ["hurdles"]
BLISS_TO_UNICODE["daycare"] = ["U+4703"]
UNICODE_TO_BLISS["U+4703"] = ["daycare"]
BLISS_TO_UNICODE["son in law"] = ["U+4704"]
UNICODE_TO_BLISS["U+4704"] = ["son in law"]
BLISS_TO_UNICODE["son-in-law"] = ["U+4704"]
UNICODE_TO_BLISS["U+4704"].append("son-in-law")
BLISS_TO_UNICODE["necklace"] = ["U+4705"]
UNICODE_TO_BLISS["U+4705"] = ["necklace"]
BLISS_TO_UNICODE["inlet"] = ["U+4706"]
UNICODE_TO_BLISS["U+4706"] = ["inlet"]
BLISS_TO_UNICODE["swimming pool"] = ["U+4707"]
UNICODE_TO_BLISS["U+4707"] = ["swimming pool"]
BLISS_TO_UNICODE["eastward"] = ["U+4708"]
UNICODE_TO_BLISS["U+4708"] = ["eastward"]
BLISS_TO_UNICODE["to crash"] = ["U+4709"]
UNICODE_TO_BLISS["U+4709"] = ["to crash"]
BLISS_TO_UNICODE["Adar"] = ["U+470a"]
UNICODE_TO_BLISS["U+470a"] = ["Adar"]
BLISS_TO_UNICODE["Adam"] = ["U+470b"]
UNICODE_TO_BLISS["U+470b"] = ["Adam"]
BLISS_TO_UNICODE["fingerprint"] = ["U+470c"]
UNICODE_TO_BLISS["U+470c"] = ["fingerprint"]
BLISS_TO_UNICODE["flea"] = ["U+470d"]
UNICODE_TO_BLISS["U+470d"] = ["flea"]
BLISS_TO_UNICODE["piggery"] = ["U+470e"]
UNICODE_TO_BLISS["U+470e"] = ["piggery"]
BLISS_TO_UNICODE["tram"] = ["U+470f"]
UNICODE_TO_BLISS["U+470f"] = ["tram"]
BLISS_TO_UNICODE["long vehicle"] = ["U+4710"]
UNICODE_TO_BLISS["U+4710"] = ["long vehicle"]
BLISS_TO_UNICODE["trap"] = ["U+4711"]
UNICODE_TO_BLISS["U+4711"] = ["trap"]
BLISS_TO_UNICODE["schoolbag"] = ["U+4712"]
UNICODE_TO_BLISS["U+4712"] = ["schoolbag"]
BLISS_TO_UNICODE["parasailing"] = ["U+4714"]
UNICODE_TO_BLISS["U+4714"] = ["parasailing"]
BLISS_TO_UNICODE["maple-leaf"] = ["U+34ce"]
UNICODE_TO_BLISS["U+34ce"].append("maple-leaf")
BLISS_TO_UNICODE["scrambled eggs"] = ["U+4715"]
UNICODE_TO_BLISS["U+4715"] = ["scrambled eggs"]
BLISS_TO_UNICODE["utensil"] = ["U+4716"]
UNICODE_TO_BLISS["U+4716"] = ["utensil"]
BLISS_TO_UNICODE["Lag B'Omer"] = ["U+4717"]
UNICODE_TO_BLISS["U+4717"] = ["Lag B'Omer"]
BLISS_TO_UNICODE["Neptune"] = ["U+4718"]
UNICODE_TO_BLISS["U+4718"] = ["Neptune"]
BLISS_TO_UNICODE["international symbol for Israeli shekel"] = ["U+4719"]
UNICODE_TO_BLISS["U+4719"] = ["international symbol for Israeli shekel"]
BLISS_TO_UNICODE["glass craft"] = ["U+471a"]
UNICODE_TO_BLISS["U+471a"] = ["glass craft"]
BLISS_TO_UNICODE["tanker"] = ["U+471b"]
UNICODE_TO_BLISS["U+471b"] = ["tanker"]
BLISS_TO_UNICODE["zoologist"] = ["U+471c"]
UNICODE_TO_BLISS["U+471c"] = ["zoologist"]
BLISS_TO_UNICODE["zoology"] = ["U+471d"]
UNICODE_TO_BLISS["U+471d"] = ["zoology"]
BLISS_TO_UNICODE["sew"] = ["U+471e"]
UNICODE_TO_BLISS["U+471e"] = ["sew"]
BLISS_TO_UNICODE["to sew"] = ["U+471f"]
UNICODE_TO_BLISS["U+471f"] = ["to sew"]
BLISS_TO_UNICODE["galley"] = ["U+4720"]
UNICODE_TO_BLISS["U+4720"] = ["galley"]
BLISS_TO_UNICODE["act in favour of"] = ["U+4721"]
UNICODE_TO_BLISS["U+4721"] = ["act in favour of"]
BLISS_TO_UNICODE["boil"] = ["U+4722"]
UNICODE_TO_BLISS["U+4722"] = ["boil"]
BLISS_TO_UNICODE["goblin"] = ["U+4723"]
UNICODE_TO_BLISS["U+4723"] = ["goblin"]
BLISS_TO_UNICODE["baby animal"] = ["U+4724"]
UNICODE_TO_BLISS["U+4724"] = ["baby animal"]
BLISS_TO_UNICODE["apartment block"] = ["U+4726"]
UNICODE_TO_BLISS["U+4726"] = ["apartment block"]
BLISS_TO_UNICODE["sculpture"] = ["U+4727"]
UNICODE_TO_BLISS["U+4727"] = ["sculpture"]
BLISS_TO_UNICODE["Holy Infant"] = ["U+4728"]
UNICODE_TO_BLISS["U+4728"] = ["Holy Infant"]
BLISS_TO_UNICODE["electric pan"] = ["U+4729"]
UNICODE_TO_BLISS["U+4729"] = ["electric pan"]
BLISS_TO_UNICODE["westward"] = ["U+472a"]
UNICODE_TO_BLISS["U+472a"] = ["westward"]
BLISS_TO_UNICODE["bagel"] = ["U+472b"]
UNICODE_TO_BLISS["U+472b"] = ["bagel"]
BLISS_TO_UNICODE["pharmacist"] = ["U+472c"]
UNICODE_TO_BLISS["U+472c"] = ["pharmacist"]
BLISS_TO_UNICODE["Abraham"] = ["U+472d"]
UNICODE_TO_BLISS["U+472d"] = ["Abraham"]
BLISS_TO_UNICODE["tubal ligation"] = ["U+472e"]
UNICODE_TO_BLISS["U+472e"] = ["tubal ligation"]
BLISS_TO_UNICODE["seaweed"] = ["U+472f"]
UNICODE_TO_BLISS["U+472f"] = ["seaweed"]
BLISS_TO_UNICODE["synchronized swimming"] = ["U+4730"]
UNICODE_TO_BLISS["U+4730"] = ["synchronized swimming"]
BLISS_TO_UNICODE["sled dog"] = ["U+4731"]
UNICODE_TO_BLISS["U+4731"] = ["sled dog"]
BLISS_TO_UNICODE["buzzer"] = ["U+4732"]
UNICODE_TO_BLISS["U+4732"] = ["buzzer"]
BLISS_TO_UNICODE["spending spree"] = ["U+4733"]
UNICODE_TO_BLISS["U+4733"] = ["spending spree"]
BLISS_TO_UNICODE["to buy"] = ["U+4734"]
UNICODE_TO_BLISS["U+4734"] = ["to buy"]
BLISS_TO_UNICODE["sewing machine"] = ["U+4735"]
UNICODE_TO_BLISS["U+4735"] = ["sewing machine"]
BLISS_TO_UNICODE["kitchen tongs"] = ["U+4736"]
UNICODE_TO_BLISS["U+4736"] = ["kitchen tongs"]
BLISS_TO_UNICODE["tongs"] = ["U+4737"]
UNICODE_TO_BLISS["U+4737"] = ["tongs"]
BLISS_TO_UNICODE["sheltered workshop"] = ["U+4738"]
UNICODE_TO_BLISS["U+4738"] = ["sheltered workshop"]
BLISS_TO_UNICODE["closed"] = ["U+4739"]
UNICODE_TO_BLISS["U+4739"] = ["closed"]
BLISS_TO_UNICODE["frustrated"] = ["U+473a"]
UNICODE_TO_BLISS["U+473a"] = ["frustrated"]
BLISS_TO_UNICODE["dish rack"] = ["U+473b"]
UNICODE_TO_BLISS["U+473b"] = ["dish rack"]
BLISS_TO_UNICODE["lifeboat"] = ["U+473c"]
UNICODE_TO_BLISS["U+473c"] = ["lifeboat"]
BLISS_TO_UNICODE["to aid"] = ["U+473d"]
UNICODE_TO_BLISS["U+473d"] = ["to aid"]
BLISS_TO_UNICODE["pictograph of two traversing bars"] = ["U+473e"]
UNICODE_TO_BLISS["U+473e"] = ["pictograph of two traversing bars"]
BLISS_TO_UNICODE["puberty"] = ["U+473f"]
UNICODE_TO_BLISS["U+473f"] = ["puberty"]
BLISS_TO_UNICODE["farmer"] = ["U+4740"]
UNICODE_TO_BLISS["U+4740"] = ["farmer"]
BLISS_TO_UNICODE["cowshed"] = ["U+4741"]
UNICODE_TO_BLISS["U+4741"] = ["cowshed"]
BLISS_TO_UNICODE["buddhist"] = ["U+4742"]
UNICODE_TO_BLISS["U+4742"] = ["buddhist"]
BLISS_TO_UNICODE["member"] = ["U+4743"]
UNICODE_TO_BLISS["U+4743"] = ["member"]
BLISS_TO_UNICODE["belong to"] = ["U+4744"]
UNICODE_TO_BLISS["U+4744"] = ["belong to"]
BLISS_TO_UNICODE["low water"] = ["U+4745"]
UNICODE_TO_BLISS["U+4745"] = ["low water"]
BLISS_TO_UNICODE["hamentasch"] = ["U+4746"]
UNICODE_TO_BLISS["U+4746"] = ["hamentasch"]
BLISS_TO_UNICODE["whale"] = ["U+4747"]
UNICODE_TO_BLISS["U+4747"] = ["whale"]
BLISS_TO_UNICODE["collar"] = ["U+4748"]
UNICODE_TO_BLISS["U+4748"] = ["collar"]
BLISS_TO_UNICODE["splint"] = ["U+4749"]
UNICODE_TO_BLISS["U+4749"] = ["splint"]
BLISS_TO_UNICODE["pictograph of head and neck and two humps"] = ["U+474a"]
UNICODE_TO_BLISS["U+474a"] = ["pictograph of head and neck and two humps"]
BLISS_TO_UNICODE["stolen goods"] = ["U+474b"]
UNICODE_TO_BLISS["U+474b"] = ["stolen goods"]
BLISS_TO_UNICODE["biologist"] = ["U+474c"]
UNICODE_TO_BLISS["U+474c"] = ["biologist"]
BLISS_TO_UNICODE["drunk"] = ["U+474d"]
UNICODE_TO_BLISS["U+474d"] = ["drunk"]
BLISS_TO_UNICODE["weak person"] = ["U+474e"]
UNICODE_TO_BLISS["U+474e"] = ["weak person"]
BLISS_TO_UNICODE["myth"] = ["U+474f"]
UNICODE_TO_BLISS["U+474f"] = ["myth"]
BLISS_TO_UNICODE["know"] = ["U+4750"]
UNICODE_TO_BLISS["U+4750"] = ["know"]
BLISS_TO_UNICODE["doughnut"] = ["U+4751"]
UNICODE_TO_BLISS["U+4751"] = ["doughnut"]
BLISS_TO_UNICODE["pictograph symbol suggests the outline of a chemical retort"] = ["U+4752"]
UNICODE_TO_BLISS["U+4752"] = ["pictograph symbol suggests the outline of a chemical retort"]
BLISS_TO_UNICODE["symbol is derived from the mathematical symbol for smaller than. This symbol in halfsize is the basis for against"] = ["U+4753"]
UNICODE_TO_BLISS["U+4753"] = ["symbol is derived from the mathematical symbol for smaller than. This symbol in halfsize is the basis for against"]
BLISS_TO_UNICODE[" by"] = ["U+4754"]
UNICODE_TO_BLISS["U+4754"] = [" by"]
BLISS_TO_UNICODE[" and there."] = ["U+4755"]
UNICODE_TO_BLISS["U+4755"] = [" and there."]
BLISS_TO_UNICODE["virginity"] = ["U+4756"]
UNICODE_TO_BLISS["U+4756"] = ["virginity"]
BLISS_TO_UNICODE["because"] = ["U+4757"]
UNICODE_TO_BLISS["U+4757"] = ["because"]
BLISS_TO_UNICODE["a weight"] = ["U+4758"]
UNICODE_TO_BLISS["U+4758"] = ["a weight"]
BLISS_TO_UNICODE["hovercraft"] = ["U+4759"]
UNICODE_TO_BLISS["U+4759"] = ["hovercraft"]
BLISS_TO_UNICODE["food ball"] = ["U+475a"]
UNICODE_TO_BLISS["U+475a"] = ["food ball"]
BLISS_TO_UNICODE["bugle"] = ["U+475b"]
UNICODE_TO_BLISS["U+475b"] = ["bugle"]
BLISS_TO_UNICODE["wilderness"] = ["U+475c"]
UNICODE_TO_BLISS["U+475c"] = ["wilderness"]
BLISS_TO_UNICODE["open/wild"] = ["U+475d"]
UNICODE_TO_BLISS["U+475d"] = ["open/wild"]
BLISS_TO_UNICODE["polisher"] = ["U+475e"]
UNICODE_TO_BLISS["U+475e"] = ["polisher"]
BLISS_TO_UNICODE["to polish"] = ["U+475f"]
UNICODE_TO_BLISS["U+475f"] = ["to polish"]
BLISS_TO_UNICODE["Valentine's Day"] = ["U+4761"]
UNICODE_TO_BLISS["U+4761"] = ["Valentine's Day"]
BLISS_TO_UNICODE["figure skating"] = ["U+4762"]
UNICODE_TO_BLISS["U+4762"] = ["figure skating"]
BLISS_TO_UNICODE["salad dressing"] = ["U+4763"]
UNICODE_TO_BLISS["U+4763"] = ["salad dressing"]
BLISS_TO_UNICODE["whether"] = ["U+4765"]
UNICODE_TO_BLISS["U+4765"] = ["whether"]
BLISS_TO_UNICODE["baby clinic"] = ["U+4766"]
UNICODE_TO_BLISS["U+4766"] = ["baby clinic"]
BLISS_TO_UNICODE["domestic animal"] = ["U+4767"]
UNICODE_TO_BLISS["U+4767"] = ["domestic animal"]
BLISS_TO_UNICODE["boom"] = ["U+4768"]
UNICODE_TO_BLISS["U+4768"] = ["boom"]
BLISS_TO_UNICODE["Universe"] = ["U+4769"]
UNICODE_TO_BLISS["U+4769"] = ["Universe"]
BLISS_TO_UNICODE["The Nordic countries"] = ["U+476a"]
UNICODE_TO_BLISS["U+476a"] = ["The Nordic countries"]
BLISS_TO_UNICODE["to shine"] = ["U+476b"]
UNICODE_TO_BLISS["U+476b"] = ["to shine"]
BLISS_TO_UNICODE["flatfish"] = ["U+476c"]
UNICODE_TO_BLISS["U+476c"] = ["flatfish"]
BLISS_TO_UNICODE["gynecologist"] = ["U+476d"]
UNICODE_TO_BLISS["U+476d"] = ["gynecologist"]
BLISS_TO_UNICODE["all-terrain bike"] = ["U+3577"]
UNICODE_TO_BLISS["U+3577"].append("all-terrain bike")
BLISS_TO_UNICODE["ca-ca"] = ["U+3656"]
UNICODE_TO_BLISS["U+3656"].append("ca-ca")
BLISS_TO_UNICODE["chick-pea"] = ["U+333a"]
UNICODE_TO_BLISS["U+333a"].append("chick-pea")
BLISS_TO_UNICODE["blow-organ"] = ["U+3771"]
UNICODE_TO_BLISS["U+3771"].append("blow-organ")
BLISS_TO_UNICODE["e-mail address"] = ["U+357c"]
UNICODE_TO_BLISS["U+357c"].append("e-mail address")
BLISS_TO_UNICODE["email address"].append("U+357c")
UNICODE_TO_BLISS["U+357c"].append("email address")
BLISS_TO_UNICODE["tumble-drier"] = ["U+357d"]
UNICODE_TO_BLISS["U+357d"].append("tumble-drier")
BLISS_TO_UNICODE["tumble-dryer"] = ["U+357d"]
UNICODE_TO_BLISS["U+357d"].append("tumble-dryer")
BLISS_TO_UNICODE["teeter-totter"] = ["U+352d"]
UNICODE_TO_BLISS["U+352d"].append("teeter-totter")
BLISS_TO_UNICODE["go-karting"] = ["U+37fe"]
UNICODE_TO_BLISS["U+37fe"].append("go-karting")
BLISS_TO_UNICODE["make-believe"] = ["U+3580"]
UNICODE_TO_BLISS["U+3580"].append("make-believe")
BLISS_TO_UNICODE["pretend"].append("U+3580")
UNICODE_TO_BLISS["U+3580"].append("pretend")
BLISS_TO_UNICODE["imaginary"].append("U+3580")
UNICODE_TO_BLISS["U+3580"].append("imaginary")
BLISS_TO_UNICODE["text-to-speech"] = ["U+38c0"]
UNICODE_TO_BLISS["U+38c0"].append("text-to-speech")
BLISS_TO_UNICODE["walk-in closet"] = ["U+3902"]
UNICODE_TO_BLISS["U+3902"].append("walk-in closet")
BLISS_TO_UNICODE["man-made item"] = ["U+3581"]
UNICODE_TO_BLISS["U+3581"].append("man-made item")
BLISS_TO_UNICODE["artefact"].append("U+3581")
UNICODE_TO_BLISS["U+3581"].append("artefact")
BLISS_TO_UNICODE["artifact"].append("U+3581")
UNICODE_TO_BLISS["U+3581"].append("artifact")
BLISS_TO_UNICODE["product"].append("U+3581")
UNICODE_TO_BLISS["U+3581"].append("product")
BLISS_TO_UNICODE["half-slip"] = ["U+3993"]
UNICODE_TO_BLISS["U+3993"].append("half-slip")
BLISS_TO_UNICODE["groom-to-be"] = ["U+39d7"]
UNICODE_TO_BLISS["U+39d7"].append("groom-to-be")
BLISS_TO_UNICODE["take-off"] = ["U+3a1b"]
UNICODE_TO_BLISS["U+3a1b"].append("take-off")
BLISS_TO_UNICODE["airplane take-off"] = ["U+3a1b"]
UNICODE_TO_BLISS["U+3a1b"].append("airplane take-off")
BLISS_TO_UNICODE["good-looking"] = ["U+3a1f"]
UNICODE_TO_BLISS["U+3a1f"].append("good-looking")
BLISS_TO_UNICODE["burned-out"] = ["U+3585"]
UNICODE_TO_BLISS["U+3585"].append("burned-out")
BLISS_TO_UNICODE["burnt-out"] = ["U+3585"]
UNICODE_TO_BLISS["U+3585"].append("burnt-out")
BLISS_TO_UNICODE["ping-pong"] = ["U+3af0"]
UNICODE_TO_BLISS["U+3af0"].append("ping-pong")
BLISS_TO_UNICODE["one-half"] = ["U+3b53"]
UNICODE_TO_BLISS["U+3b53"].append("one-half")
BLISS_TO_UNICODE["single-foot"] = ["U+3c0b"]
UNICODE_TO_BLISS["U+3c0b"].append("single-foot")
BLISS_TO_UNICODE["cease-fire"] = ["U+3595"]
UNICODE_TO_BLISS["U+3595"].append("cease-fire")
BLISS_TO_UNICODE["armistice"].append("U+3595")
UNICODE_TO_BLISS["U+3595"].append("armistice")
BLISS_TO_UNICODE["email"].append("U+37c6")
UNICODE_TO_BLISS["U+37c6"].append("email")
BLISS_TO_UNICODE["mind-altering drug"] = ["U+397c"]
UNICODE_TO_BLISS["U+397c"].append("mind-altering drug")
BLISS_TO_UNICODE["self-centred"] = ["U+3e1f"]
UNICODE_TO_BLISS["U+3e1f"].append("self-centred")
BLISS_TO_UNICODE["self-centered"] = ["U+3e1f"]
UNICODE_TO_BLISS["U+3e1f"].append("self-centered")
BLISS_TO_UNICODE["scooter-board"] = ["U+3eef"]
UNICODE_TO_BLISS["U+3eef"].append("scooter-board")
BLISS_TO_UNICODE["merry-go-round"] = ["U+359b"]
UNICODE_TO_BLISS["U+359b"].append("merry-go-round")
BLISS_TO_UNICODE["carousel"].append("U+359b")
UNICODE_TO_BLISS["U+359b"].append("carousel")
BLISS_TO_UNICODE["worn-out"] = ["U+359c"]
UNICODE_TO_BLISS["U+359c"].append("worn-out")
BLISS_TO_UNICODE["raddled"].append("U+359c")
UNICODE_TO_BLISS["U+359c"].append("raddled")
BLISS_TO_UNICODE["T-shirt"] = ["U+359e"]
UNICODE_TO_BLISS["U+359e"].append("T-shirt")
BLISS_TO_UNICODE["tee shirt"].append("U+359e")
UNICODE_TO_BLISS["U+359e"].append("tee shirt")
BLISS_TO_UNICODE["jersey"].append("U+359e")
UNICODE_TO_BLISS["U+359e"].append("jersey")
BLISS_TO_UNICODE["world-wide"] = ["U+3fe2"]
UNICODE_TO_BLISS["U+3fe2"].append("world-wide")
BLISS_TO_UNICODE["go-kart"] = ["U+35a2"]
UNICODE_TO_BLISS["U+35a2"].append("go-kart")
BLISS_TO_UNICODE["kart"].append("U+35a2")
UNICODE_TO_BLISS["U+35a2"].append("kart")
BLISS_TO_UNICODE["bride-to-be"] = ["U+4066"]
UNICODE_TO_BLISS["U+4066"].append("bride-to-be")
BLISS_TO_UNICODE["horse-drawn sleigh"] = ["U+3c6f"]
UNICODE_TO_BLISS["U+3c6f"].append("horse-drawn sleigh")
BLISS_TO_UNICODE["USB-memory"] = ["U+40d2"]
UNICODE_TO_BLISS["U+40d2"].append("USB-memory")
BLISS_TO_UNICODE["imaginary person"].append("U+3950")
UNICODE_TO_BLISS["U+3950"].append("imaginary person")
BLISS_TO_UNICODE["water nymph"].append("U+3950")
UNICODE_TO_BLISS["U+3950"].append("water nymph")
BLISS_TO_UNICODE["job-centre"] = ["U+4270"]
UNICODE_TO_BLISS["U+4270"].append("job-centre")
BLISS_TO_UNICODE["C-section"] = ["U+4322"]
UNICODE_TO_BLISS["U+4322"].append("C-section")
BLISS_TO_UNICODE["step-parent"].append("U+439a")
UNICODE_TO_BLISS["U+439a"].append("step-parent")
BLISS_TO_UNICODE["stand-in"] = ["U+35ba"]
UNICODE_TO_BLISS["U+35ba"].append("stand-in")
BLISS_TO_UNICODE["substitute"].append("U+35ba")
UNICODE_TO_BLISS["U+35ba"].append("substitute")
BLISS_TO_UNICODE["alternate"].append("U+35ba")
UNICODE_TO_BLISS["U+35ba"].append("alternate")
BLISS_TO_UNICODE["counter-forces"] = ["U+324f"]
UNICODE_TO_BLISS["U+324f"].append("counter-forces")
"""
GRAMMAR_CATEGORIES:

    Used for holding data representing grammar categories in languages,
    e.g. tense, number, gender, etc.
"""

TENSES = ["present", "past", "future"]
NUMBERS = ["singular", "plural", "dual", "trial", "paucal"]
GENDERS = ["masculine", "masculine gender", "feminine", "feminine gender", "neuter", "neuter gender",
           "animate", "inanimate"]
PERSONS = ["1st", "2nd", "3rd"]
CASES = ["nominative", "accusative", "dative", "ablative", "genitive", "vocative", "locative", "instrumental"]
ASPECTS = {"perfective": ["momentane"], "imperfective": {"continuous": ["progressive", "stative"],
                                                         "habitual": [], "delimitative": [],
                                                         "imperfect": []},
           "generic": [], "episodic": [],
           "inceptive": [], "inchoative": [], "cessative": [],
           "retrospective": ["pluperfect", "future perfect"], "prospective": [], "present perfect": []}
MOODS = ['indicative', 'subjunctive', 'conditional', 'optative', 'imperative', 'jussive', 'potential',
         'hypothetical', 'inferential', 'desiderative', 'dubitative', 'presumptive', 'permissive',
         'admirative', 'hortative', 'eventive', 'precative', 'volitive', 'necessitive', 'interrogative']


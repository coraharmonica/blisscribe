# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import helpers
import forms
import models
import blisscribe_py.blisscribe
import blisscribe_py.excerpts

# Create your tests here.
"""
DefaultTranslator = helpers.FormTranslator(lang="English",
                                           phrase="hello",  #blisscribe_py.excerpts.alice_in_wonderland[:3000],
                                           title="hello",
                                           font_fam=blisscribe_py.blisscribe.BlissTranslator.ROMAN_FONT,
                                           font_size=10,
                                           sub_all=False,
                                           fast_translate=False,
                                           page_nums=False,
                                           nouns=False,
                                           verbs=False,
                                           adjs=False,
                                           other=False)
DefaultTranslator.savePdf()
"""

data = {'phrase': 'hello',
        'title': 'Hi there',
        'lang': 'English',
        'font_fam': blisscribe_py.blisscribe.BlissTranslator.ROMAN_FONT,
        'font_size': 10,
        'sub_all': False,
        'fast_translate': False,
        'page_nums': False,
        'nouns': False,
        'verbs': False,
        'adjs': False,
        'other': False}
f = forms.TranslationForm(data)
f.is_valid()
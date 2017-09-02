# -*- coding: utf-8 -*-
# bliss_webapp/forms.py
from __future__ import unicode_literals
from django import forms
import models
import chosen


class TranslationForm(forms.ModelForm):
    class Meta:
        model = models.TranslationModel
        fields = ['phrase', 'title', 'lang',
                  'font_fam', 'font_size',
                  'nouns', 'verbs', 'adjs', 'other_pos',
                  'fast_translate', 'sub_all', 'page_nums']

    phrase = forms.CharField(
        label="Text to translate: ",
        required=True,
        max_length=10000,
        widget=forms.Textarea(attrs={'rows': '10', 'cols': '100'})
    )
    title = forms.CharField(
        label="Title:  ",
        max_length=50,
        required=False,
        widget=forms.TextInput()
    )
    lang = forms.ChoiceField(
        label="Language:  ",
        required=True,
        widget=forms.Select,
        choices=chosen.SUPPORTED_LANGS
    )

    font_fam = forms.ChoiceField(
        label="Font family:  ",
        required=False,
        choices=chosen.FONT_FAMS,
        widget=forms.Select
    )
    font_size = forms.ChoiceField(
        label="Font size:  ",
        required=False,
        choices=chosen.FONT_SIZES,
        widget=forms.Select
    )

    nouns = forms.BooleanField(
        label="Translate nouns:  ",
        required=False,
        widget=forms.CheckboxInput
    )
    verbs = forms.BooleanField(
        label="Translate verbs:  ",
        required=False,
        widget=forms.CheckboxInput
    )
    adjs = forms.BooleanField(
        label="Translate adjectives/adverbs:  ",
        required=False,
        widget=forms.CheckboxInput
    )
    other_pos = forms.BooleanField(
        label="Translate all other parts of speech:  ",
        required=False,
        widget=forms.CheckboxInput
    )

    fast_translate = forms.BooleanField(
        label="Translate all words to Blissymbols (vs only common words):  ",
        required=False,
        widget=forms.CheckboxInput
    )
    sub_all = forms.BooleanField(
        label="Subtitle all Blissymbols (vs only new Blissymbols):  ",
        required=False,
        widget=forms.CheckboxInput
    )
    page_nums = forms.BooleanField(
        label="Include page numbers:  ",
        required=False,
        widget=forms.CheckboxInput
    )

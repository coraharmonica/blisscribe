# -*- coding: utf-8 -*-
# bliss_webapp/forms.py
from __future__ import unicode_literals
from django import forms
import models
import chosen
import blisscribe_py


class TranslationForm(forms.ModelForm):
    class Meta:
        model = models.TranslationModel
        fields = ['phrase', 'title', 'lang',
                  'font_fam', 'font_size',
                  'nouns', 'verbs', 'adjs', 'other',
                  'fast_translate', 'sub_all', 'page_nums']

    phrase = forms.CharField(
        label="Text to translate: ",
        initial="write text here",
        required=False,
        max_length=10000,
        widget=forms.Textarea(attrs={'rows': '10', 'cols': '100'})
    )
    title = forms.CharField(
        label="Title:  ",
        initial="my title",
        max_length=50,
        required=False,
        widget=forms.TextInput()
    )
    lang = forms.ChoiceField(
        label="Language:  ",
        initial=chosen.SUPPORTED_LANGS[0][0],
        required=False,
        widget=forms.Select,
        choices=chosen.SUPPORTED_LANGS
    )

    font_fam = forms.ChoiceField(
        label="Font family:  ",
        initial=chosen.FONT_FAMS[2],
        required=False,
        choices=chosen.FONT_FAMS,
        widget=forms.Select
    )
    font_size = forms.ChoiceField(
        label="Font size:  ",
        initial="10",
        required=False,
        choices=chosen.FONT_SIZES,
        widget=forms.Select
    )

    nouns = forms.BooleanField(
        label="Translate nouns:  ",
        initial=True,
        required=False,
        widget=forms.CheckboxInput
    )
    verbs = forms.BooleanField(
        label="Translate verbs:  ",
        initial=True,
        required=False,
        widget=forms.CheckboxInput
    )
    adjs = forms.BooleanField(
        label="Translate adjectives/adverbs:  ",
        initial=True,
        required=False,
        widget=forms.CheckboxInput
    )
    other = forms.BooleanField(
        label="Translate all other parts of speech:  ",
        initial=False,
        required=False,
        widget=forms.CheckboxInput
    )

    fast_translate = forms.BooleanField(
        label="Translate all words to Blissymbols (vs only common words):  ",
        initial=False,
        required=False,
        widget=forms.CheckboxInput
    )
    sub_all = forms.BooleanField(
        label="Subtitle all Blissymbols (vs only new Blissymbols):  ",
        initial=True,
        required=False,
        widget=forms.CheckboxInput
    )
    page_nums = forms.BooleanField(
        label="Include page numbers:  ",
        initial=False,
        required=False,
        widget=forms.CheckboxInput
    )
    def clean_field(self, field):
        assert field in self.fields
        if not self[field].html_name in self.data:
            return self.fields[field].initial
        return self.cleaned_data[field]
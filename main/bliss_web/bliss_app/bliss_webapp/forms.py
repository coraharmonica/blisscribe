# -*- coding: utf-8 -*-
# bliss_webapp/forms.py
from __future__ import unicode_literals
from django import forms
import models
import chosen


class TranslationForm(forms.ModelForm):
    class Meta:
        model = models.TranslationModel
        fields = ['phrase', 'title', 'title_page',
                  'lang', 'font_fam', 'font_size',
                  'nouns', 'verbs', 'adjs', 'other',
                  'fast_translate', 'sub_all', 'page_nums']

    phrase = forms.CharField(
        label="text_image to translate: ",
        initial="write up to 10000 characters of text_image here...",
        required=False,
        max_length=10000,
        widget=forms.Textarea(attrs={'rows': '10', 'cols': '100'})
    )
    title = forms.CharField(
        label="title:  ",
        initial="my title",
        max_length=50,
        required=False,
        widget=forms.TextInput()
    )
    title_page = forms.BooleanField(
        label="create title page:  ",
        initial=False,
        required=False,
        widget=forms.CheckboxInput
    )
    lang = forms.ChoiceField(
        label="input language:  ",
        initial="English",
        required=False,
        widget=forms.Select,
        choices=chosen.SUPPORTED_LANGS
    )
    font_fam = forms.ChoiceField(
        label="font family:  ",
        initial="Arial",
        required=False,
        choices=chosen.FONT_FAMS,
        widget=forms.Select
    )
    font_size = forms.ChoiceField(
        label="font size:  ",
        initial="30",
        required=False,
        choices=chosen.FONT_SIZES,
        widget=forms.Select
    )
    nouns = forms.BooleanField(
        label="translate nouns:  ",
        initial=True,
        required=False,
        widget=forms.CheckboxInput
    )
    verbs = forms.BooleanField(
        label="translate verbs:  ",
        initial=True,
        required=False,
        widget=forms.CheckboxInput
    )
    adjs = forms.BooleanField(
        label="translate adjectives/adverbs:  ",
        initial=True,
        required=False,
        widget=forms.CheckboxInput
    )
    other = forms.BooleanField(
        label="translate all other parts of speech:  ",
        initial=True,
        required=False,
        widget=forms.CheckboxInput
    )
    fast_translate = forms.BooleanField(
        label="translate uncommon words to Blissymbols:  ",
        initial=True,
        required=False,
        widget=forms.CheckboxInput
    )
    sub_all = forms.BooleanField(
        label="subtitle all Blissymbols:  ",
        initial=True,
        required=False,
        widget=forms.CheckboxInput
    )
    page_nums = forms.BooleanField(
        label="include page numbers:  ",
        initial=False,
        required=False,
        widget=forms.CheckboxInput
    )
    def clean_field(self, field):
        assert field in self.fields
        return self.cleaned_data[field]

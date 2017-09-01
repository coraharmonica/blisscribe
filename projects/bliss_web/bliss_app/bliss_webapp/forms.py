# -*- coding: utf-8 -*-
# bliss_webapp/forms.py
from __future__ import unicode_literals
from django import forms
from main import blisscribe
from . import models


class TranslationForm(forms.ModelForm):
    translator = blisscribe.BlissTranslator()

    class Meta:
        model = models.TranslationModel

    parts_of_speech = forms.MultipleChoiceField(
        required=True,
        widget=forms.SelectMultiple,
        choices=list(translator.PARTS_OF_SPEECH))

    input_phrase = forms.CharField(widget=forms.TextInput())

    language = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices=translator.SUPPORTED_LANGS)


# -*- coding: utf-8 -*-
# bliss_webapp/models.py
from __future__ import unicode_literals
from django.db import models
import chosen


class TranslationModel(models.Model):

    phrase = models.TextField()
    title = models.CharField(max_length=50)
    lang = models.CharField(
        max_length=30,
        choices=chosen.SUPPORTED_LANGS,
        default=True)

    font_fam = models.CharField(
        max_length=30,
        choices=chosen.FONT_FAMS,
        default=chosen.SANS_FONT)
    font_size = models.IntegerField(
        choices=chosen.FONT_SIZES,
        default=12)

    nouns = models.BooleanField(default=True)
    verbs = models.BooleanField(default=False)
    adjs = models.BooleanField(default=False)
    other_pos = models.BooleanField(default=False)

    fast_translate = models.BooleanField(default=True)
    sub_all = models.BooleanField(default=False)
    page_nums = models.BooleanField(default=False)

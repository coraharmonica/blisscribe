# -*- coding: utf-8 -*-
# bliss_webapp/models.py
from __future__ import unicode_literals
from django.db import models
import chosen


class TranslationModel(models.Model):
    class Meta:
        db_tablespace = 'tables'

    phrase = models.TextField()
    title = models.CharField(max_length=50)
    title_page = models.BooleanField(default=False)

    lang = models.CharField(
        max_length=30,
        choices=chosen.SUPPORTED_LANGS,
        default=True)
    font_fam = models.CharField(
        max_length=50,
        choices=chosen.FONT_FAMS,
        default=chosen.FONT_FAMS[1])
    font_size = models.CharField(
        max_length=2,
        choices=chosen.FONT_SIZES,
        default=chosen.FONT_SIZES[2])

    nouns = models.BooleanField(default=False)
    verbs = models.BooleanField(default=False)
    adjs = models.BooleanField(default=False)
    other = models.BooleanField(default=False)

    fast_translate = models.BooleanField(default=False)
    sub_all = models.BooleanField(default=False)
    page_nums = models.BooleanField(default=False)

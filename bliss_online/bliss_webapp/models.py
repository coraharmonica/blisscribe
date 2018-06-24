from django.db import models
from .chosen import FONT_SIZES
from .chosen import SUPPORTED_LANGS
from .chosen import FONT_FAMS


class TranslationModel(models.Model):
    class Meta:
        db_tablespace = 'tables'
    phrase = models.TextField()
    title = models.CharField(max_length=50)
    title_page = models.BooleanField(default=False)

    lang = models.CharField(
        max_length=30,
        choices=SUPPORTED_LANGS,
        default=True)
    font_fam = models.CharField(
        max_length=50,
        choices=FONT_FAMS)
    font_size = models.CharField(
        max_length=2,
        choices=FONT_SIZES)

    nouns = models.BooleanField(default=False)
    verbs = models.BooleanField(default=False)
    adjs = models.BooleanField(default=False)
    other = models.BooleanField(default=False)

    fast_translate = models.BooleanField(default=False)
    sub_all = models.BooleanField(default=False)
    page_nums = models.BooleanField(default=False)


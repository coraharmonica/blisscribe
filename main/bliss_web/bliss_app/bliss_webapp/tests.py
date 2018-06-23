# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import blisscribe_py.lexicon_parser


LEX_PARSER = blisscribe_py.lexicon_parser.LexiconParser()
LEX_PARSER.read_ili_mapping()
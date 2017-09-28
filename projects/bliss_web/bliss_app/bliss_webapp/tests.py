# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import blisscribe_py.parse_lexica


LEX_PARSER = blisscribe_py.parse_lexica.LexiconParser()
LEX_PARSER.readILIMapping()
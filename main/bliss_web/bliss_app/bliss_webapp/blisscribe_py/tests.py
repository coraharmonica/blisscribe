# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import blisscribe_py.blisscribe

LEX_PARSER = blisscribe_py.blisscribe.LexiconParser()
LEX_PARSER.readILIMapping()
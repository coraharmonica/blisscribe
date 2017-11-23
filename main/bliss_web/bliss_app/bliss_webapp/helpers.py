# -*- coding: utf-8 -*-
# bliss_webapp/helpers.py
from django.http import HttpResponse
from django.forms import Form
from django.utils.encoding import smart_str
#import os
from blisscribe_py import blisscribe


class FormTranslator:
    FILE_PATH = blisscribe.BlissTranslator.FILE_PATH + '/bliss pdfs'
    
    def __init__(self, phrase, title, title_page,
                 lang, font_fam, font_size,
                 nouns, verbs, adjs, other,
                 sub_all, page_nums, fast_translate):
        self.phrase = smart_str(phrase)
        self.title = smart_str(title)
        self.title_page = bool(title_page)
        self.lang = smart_str(lang)
        self.font_fam = smart_str(font_fam)
        self.font_size = int(font_size)
        self.translator = blisscribe.BlissTranslator(language=self.lang,
                                                     font_path=self.font_fam,
                                                     font_size=self.font_size)
        self.nouns = bool(nouns)
        self.verbs = bool(verbs)
        self.adjs = bool(adjs)
        self.other = bool(other)
        self.sub_all = bool(sub_all)
        self.page_nums = bool(page_nums)
        self.fast_translate = bool(fast_translate)
        self.configTranslator()

    def configTranslator(self):
        self.translator.setFont(self.font_fam, self.font_size)
        self.translator.chooseTranslatables(self.nouns, self.verbs, self.adjs, self.other)
        self.translator.setFastTranslate(self.fast_translate)
        self.translator.setSubAll(self.sub_all)
        self.translator.setPageNums(self.page_nums)

    def translate(self):
        self.translator.translate(self.phrase, self.title, title_page=self.title_page)
        
    def savePdf(self):
        self.translator.translate(self.phrase, self.title, title_page=self.title_page)

    def getTitle(self):
        return self.title

    def deleteTranslation(self, filename):
        self.translator.deletePdf(filename)

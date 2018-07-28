from django.utils.encoding import smart_str

from .translation import blisscribe


class FormTranslator:
    FILE_PATH = blisscribe.PATH + '/out'
    
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
        self.translator.set_translatables(self.nouns, self.verbs, self.adjs, self.other)
        self.translator.set_fast_translate(self.fast_translate)
        self.translator.set_sub_all(self.sub_all)
        self.translator.set_page_nums(self.page_nums)

    def translate(self):
        self.translator.translate(self.phrase, self.title, title_page=self.title_page)

    def deleteTranslation(self, filename):
        self.translator.delete_pdf(filename)

# -*- coding: utf-8 -*-
# bliss_webapp/views.py
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils.encoding import smart_str
from django.views.generic import *
from django.views.generic.edit import *
from wsgiref.util import FileWrapper
from forms import TranslationForm
import os
from fpdf import FPDF
import helpers


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        # equivalent to template_name = "index.html"
        return render(request, 'index.html', context=None)


class InfoPageView(TemplateView):
    template_name = 'info.html'


class TranslatePageView(FormView):
    form_class = TranslationForm
    success_url = "/translated/"

    def get(self, request, **kwargs):
        return getTranslationText(request)

    def post(self, request, *args, **kwargs):
        return getTranslationText(request)


class TranslatedPageView(FormView):
    template_name = 'translated.html'
    form_class = TranslationForm
    success_url = "/translated/"

    def get(self, request, **kwargs):
        return render(request, 'translated.html')

    def post(self, request, *args, **kwargs):
        return downloadPdf(request)


def downloadPdf(request):
    path = smart_str(helpers.FormTranslator.FILE_PATH + "/")  # + '/translation.pdf')
    form = TranslationForm(data=request.POST)

    if form.is_valid():
        lang = smart_str(form.clean_field('lang'))
        phrase = smart_str(form.clean_field('phrase'))
        title = smart_str(form.clean_field('title'))
        font_fam = smart_str(form.clean_field('font_fam'))
        font_size = int(smart_str(form.clean_field('font_size')))
        nouns = bool(form.clean_field('nouns'))
        verbs = bool(form.clean_field('verbs'))
        adjs = bool(form.clean_field('adjs'))
        other = bool(form.clean_field('other'))
        sub_all = bool(form.clean_field('sub_all'))
        page_nums = bool(form.clean_field('page_nums'))
        fast_translate = bool(form.clean_field('fast_translate'))
        translator = helpers.FormTranslator(lang=lang,
                                            phrase=phrase,
                                            title=title,
                                            font_fam=font_fam,
                                            font_size=font_size,
                                            nouns=nouns,
                                            verbs=verbs,
                                            adjs=adjs,
                                            other=other,
                                            sub_all=sub_all,
                                            page_nums=page_nums,
                                            fast_translate=fast_translate)
        translator.savePdf()
        f = open(path + "translation.pdf", str("r+"))  # FPDF.open(pdf)
        response = HttpResponse(FileWrapper(f), content_type='application/pdf')
        f.close()
        title = translator.getTitle()
        title = title.decode('utf-8')
        # response['Content-Length'] = os.path.getsize(fn)
        response['Content-Disposition'] = 'attachment; filename='+title.encode('ascii', errors='replace')+'.pdf'
        response['X-Sendfile'] = smart_str(path)
        return response
    else:
        print(form.errors)
        return render(request, 'translate.html', {'form': TranslationForm()})


def getTranslationText(request):
    # POST b/c we need to PROCESS input to translate
    if request.method == 'POST':
        # populate form w/ user input
        return render(request, 'translated.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TranslationForm()

    return render(request, 'translate.html', {'form': form})

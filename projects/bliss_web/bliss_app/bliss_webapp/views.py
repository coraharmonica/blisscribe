# -*- coding: utf-8 -*-
# bliss_webapp/views.py
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import TranslationForm


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        # equivalent to template_name = "index.html"
        return render(request, 'index.html', context=None)


class InfoPageView(TemplateView):
    template_name = 'info.html'


class TranslatePageView(FormView):
    template_name = "translate.html"
    form_class = TranslationForm
    success_url = "translated.html"


class TranslatedPageView(TemplateView):
    template_name = 'translated.html'

    def get(self, request, **kwargs):
        return getTranslationText(request)


def getTranslationText(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TranslationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/translated/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TranslationForm()

    return render(request, 'translate.html', {'form': form})
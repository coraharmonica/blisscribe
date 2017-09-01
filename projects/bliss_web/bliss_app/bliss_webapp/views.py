# -*- coding: utf-8 -*-
# bliss_webapp/views.py
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        # equivalent to template_name = "index.html"
        return render(request, 'index.html', context=None)


class AboutPageView(TemplateView):
    template_name = 'about.html'


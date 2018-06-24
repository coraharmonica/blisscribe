from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils.encoding import smart_str
from django.views.generic import *
from django.views.generic.edit import *
from wsgiref.util import FileWrapper
from .forms import TranslationForm
from . import helpers


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
    path = smart_str(helpers.FormTranslator.FILE_PATH + "/")
    form = TranslationForm(data=request.POST)

    if form.is_valid():
        phrase = smart_str(form.clean_field('phrase'))
        title = smart_str(form.clean_field('title'))
        title_page = bool(form.clean_field('title_page'))
        lang = smart_str(form.clean_field('lang'))
        font_fam = smart_str(form.clean_field('font_fam'))
        font_size = int(smart_str(form.clean_field('font_size')))
        nouns = bool(form.clean_field('nouns'))
        verbs = bool(form.clean_field('verbs'))
        adjs = bool(form.clean_field('adjs'))
        other = bool(form.clean_field('other'))
        sub_all = bool(form.clean_field('sub_all'))
        page_nums = bool(form.clean_field('page_nums'))
        fast_translate = bool(form.clean_field('fast_translate'))
        translator = helpers.FormTranslator(phrase=phrase,
                                            title=title,
                                            title_page=title_page,
                                            lang=lang,
                                            font_fam=font_fam,
                                            font_size=font_size,
                                            nouns=nouns,
                                            verbs=verbs,
                                            adjs=adjs,
                                            other=other,
                                            sub_all=sub_all,
                                            page_nums=page_nums,
                                            fast_translate=fast_translate)
        translator.translate()
        title = title.decode('utf-8')
        filename = title + ".pdf"
        f = open(path + filename, str("r+"))
        response = HttpResponse(FileWrapper(f), content_type='application/pdf')
        f.close()
        translator.deleteTranslation(filename=filename)
        response['Content-Disposition'] = 'attachment; filename='+filename
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

    # if a GET (or any translate_other method) we'll create a blank form
    else:
        form = TranslationForm()

    return render(request, 'translate.html', {'form': form})

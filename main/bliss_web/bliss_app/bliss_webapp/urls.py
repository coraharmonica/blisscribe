from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^info/$', views.InfoPageView.as_view()),
    url(r'^translate/$', views.TranslatePageView.as_view()),
    url(r'^translated/$', views.TranslatedPageView.as_view()),
    url(r'^translation.pdf/$', views.downloadPdf),
]
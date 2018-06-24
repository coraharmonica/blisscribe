from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('info/', views.InfoPageView.as_view()),
    path('translate/', views.TranslatePageView.as_view()),
    path('translated/', views.TranslatedPageView.as_view()),
    path('translation.pdf/', views.downloadPdf),
]

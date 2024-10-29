from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('home/',views.home, name='home'),
    path('welcome/',views.login_view, name='welcome'),
    path('questionario/',views.questionario, name='questionario'),
    path('simplecontinuouspresent/',views.simplecontinuouspresent, name='simplecontinuouspresent'),
    path('resultsimplecontinuouspresent/',views.resultsimplecontinuouspresent, name='resultsimplecontinuouspresent'),
    path('simplepresent/',views.simplepresent, name='simplepresent'),
    path('resultsimplepresent/',views.resultsimplepresent, name='resultsimplepresent'),
    path('gabarito/',views.resultado_questionario, name='resultado_questionario'),
]

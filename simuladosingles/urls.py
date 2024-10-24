from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('home/',views.home, name='home'),
    path('welcome/',views.login_view, name='welcome'),
    path('questionario/',views.questionario, name='questionario'),
    path('gabarito/',views.resultado_questionario, name='resultado_questionario'),
]

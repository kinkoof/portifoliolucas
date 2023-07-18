from django.urls import path

from . import views

urlpatterns = [
    path("cadastro/", views.Cadastro, name='cadastro'),
    path("login/", views.Login, name='login'),
    path("sair/", views.Sair, name='sair'),

]
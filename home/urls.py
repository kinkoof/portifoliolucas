from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name='inicial'),
    path("contato/", views.contato, name='contato'),

]
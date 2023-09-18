from django.urls import path

from . import views


urlpatterns = [
    path("", views.listaTodo, name='todo'),
    path("tarefa/<int:id>", views.viewTarefa, name='tarefa'),
    path("novatarefa/", views.novaTarefa, name='nova tarefa'),
    path("edit/<int:id>", views.editTarefa, name='editar'),
    path("excluir/<int:id>", views.excluirTarefa, name='excluir'),

]
from django.urls import path

from . import views



urlpatterns = [
    path("", views.listaProjetos, name='projetos'),
    path("projeto/<int:id>", views.ViewProjeto, name="projetos-view"),
    path("novoprojeto/", views.NovoProjeto, name="novo-projeto"),
    path("projeto/edit/<int:id>", views.EditProjeto, name="edit-projeto"),
    path("projeto/excluir/<int:id>", views.ExcluirProjeto, name="excluir-projeto"),
]

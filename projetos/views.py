from django.shortcuts import render, get_object_or_404, redirect
from .models import Projeto
from .forms import ProjetoForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


def listaProjetos(request):
    projetos_lista = Projeto.objects.all().order_by('-created_at')

    paginator = Paginator(projetos_lista, 2)
    page = request.GET.get('page')
    projetos = paginator.get_page(page)

    return render(request, 'projetos/lista.html', {'projetos': projetos, 'nome_pagina': 'PROJETOS'})

def ViewProjeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    return render(request, "Projetos/projeto.html ", {'projeto': projeto, 'nome_pagina': 'PROJETOS'})

def NovoProjeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)

        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.save()
            return redirect('/projetos')

    else:
        form = ProjetoForm()
        return render(request, "projetos/novoprojeto.html", {'form': form, 'nome_pagina': 'PROJETOS'})

def EditProjeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    form = ProjetoForm(instance=projeto)

    if request.method == "POST":
        form = ProjetoForm(request.POST, instance=projeto)

        if (form.is_valid()):
            projeto.save()
            return redirect('/projetos')
        else:
            return render(request, "projetos/editprojeto.html", {'form': form, 'projeto': projeto, 'nome_pagina': 'PROJETOS'})

    else:
        return render(request, "projetos/editprojeto.html", {'form': form, 'projeto': projeto, 'nome_pagina': 'PROJETOS'})

def ExcluirProjeto(request, id):

    projeto = get_object_or_404(Projeto, pk=id)
    projeto.delete()
    return redirect('/projetos')



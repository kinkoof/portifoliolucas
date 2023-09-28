from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm


def listaTodo(request):
    # serve para chamar todas as tarefas salvas na variavel
    tarefas = Todo.objects.all().order_by('-created_at')
    return render(request, "todo/listatodo.html", {'tarefas': tarefas, 'nome_pagina': 'TO DO'})


def novaTarefa(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.save()
            return redirect('/todo')
    else:
        form = TodoForm()

    return render(request, "todo/novatarefa.html", {'form': form, 'nome_pagina': 'TAREFAS'})


def viewTarefa(request, id):
    tarefa = get_object_or_404(Todo, pk=id)
    return render(request, 'todo/tarefa.html', {'tarefa': tarefa})


def editTarefa(request, id):
    tarefa = get_object_or_404(Todo, pk=id)
    form = TodoForm(instance=tarefa)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=tarefa)

        if (form.is_valid()):
            tarefa.save()
            return redirect('/todo')
    else:
        return render(request, "todo/edittarefa.html", {'form': form, 'tarefa': tarefa, 'nome_pagina': 'TAREFAS'})

def excluirTarefa(request, id):
    tarefa = get_object_or_404(Todo, pk=id)
    tarefa.delete()
    return redirect('/todo')

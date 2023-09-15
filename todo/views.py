from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm


def listaTodo(request):
    tarefas = Todo.objects.all().order_by('-created_at') #serve para chamar todas as tarefas salvas na variavel
    return render(request, "todo/listatodo.html", {'tarefas' : tarefas, 'nome_pagina': 'TO DO'})


def novaTarefa(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.done = 'doing'
            projeto.save()
            return redirect('/todo')

    else:
        form = TodoForm()
        return render (request, "todo/novatarefa.html", { 'form' : form, 'nome_pagina' : 'TAREFAS'})

def viewTarefa(request, id):
    tarefa = get_object_or_404(Todo, pk=id)
    return render(request, 'todo/tarefa.html', {'tarefa': tarefa})
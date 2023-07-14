from django.shortcuts import render

def listaTodo(request):
    return render(request, "todo/lista.html", {'nome_pagina': 'TO DO'})
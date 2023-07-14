from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home/inicial.html', {'nome_pagina': 'BEM-VINDO'})

def contato(request):
    return render(request, 'home/contato.html', {'nome_pagina': 'CONTATO'})





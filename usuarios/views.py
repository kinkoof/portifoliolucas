from django.http import HttpResponse
from django.shortcuts import render

def Cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        return HttpResponse(nome)
        

def Login(request):
    return render(request, 'usuarios/login')
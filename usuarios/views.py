from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

#parte do cadastro
def Cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html', {'nome_pagina': 'CADASTRO'})
    else:
        nome = request.POST.get('nome')
        email =  request.POST.get('email')       
        senha =  request.POST.get('senha')  

        user = User.objects.filter(username = nome).first()

        if user:
            return HttpResponse("ja existe um usuario com esse nome")

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        return HttpResponse("usuario cadastrado com sucesso")

def Login(request):
    
    if request.method == "GET":
        return render(request, 'usuarios/login.html', {'nome_pagina': 'LOGIN'})
    
    else:
        nome = request.POST.get('nome') 
        senha = request.POST.get('senha') 

        user = authenticate(username = nome, password = senha)

        if user:
            login(request, user)

            return HttpResponse("autenticado")

        else:
            return HttpResponse('usuario ou senha invalidos')
              

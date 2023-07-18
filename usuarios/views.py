from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
            return HttpResponseRedirect('/usuarios/cadastro')


        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        return HttpResponseRedirect('/usuarios/login')

def Login(request):
    
    if request.method == "GET":
        return render(request, 'usuarios/login.html', {'nome_pagina': 'LOGIN'})
    
    else:
        nome = request.POST.get('nome') 
        senha = request.POST.get('senha') 

        user = authenticate(username = nome, password = senha)

        if user:
            login(request, user)

            return HttpResponseRedirect('/todo')

        else:
            return messages.success('usuario ou senha invalidos')
              

def Sair(request):
    logout(request)

    
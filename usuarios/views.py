from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# parte do cadastro


def Cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html', {'nome_pagina': 'CADASTRO'})
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=nome).first()
        email1 = User.objects.filter(email=email).first()


        if user:
            messages.error(request, 'Já existe um usuário com esse nome.')
        elif email1:
            messages.error(request, 'Email já cadastrado.')

        else:
            user = User.objects.create_user(
                username=nome, email=email, password=senha)
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return HttpResponseRedirect('/usuarios/login')

        return HttpResponseRedirect('/usuarios/cadastro')


def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, email=email, password=senha)

        if user is not None:
            login(request, user)
            return redirect('/todo')
        else:
            messages.error(request, 'Email ou senha inválidos. Por favor, tente novamente.')

    return render(request, 'usuarios/login.html', {'nome_pagina': 'LOGIN'})


def Sair(request):
    logout(request)

    return HttpResponseRedirect('/usuarios/login')

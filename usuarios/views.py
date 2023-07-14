from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

#parte do cadastro
def Cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(email=email).first()

        if user:
            return HttpResponse("email ja cadastrado")
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        return HttpResponse("Usuario cadastrado com sucesso")
        

def Login(request):
    return render(request, 'usuarios/login')
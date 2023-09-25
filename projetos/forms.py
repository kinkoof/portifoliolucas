from django import forms

from .models import Projeto

class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields = ('titulo', 'descriçao')
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Digite o título aqui'}),
            'descriçao': forms.Textarea(attrs={'placeholder': 'Descreva o projeto'}),

        }
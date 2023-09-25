from django import forms

from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:

        model = Todo
        fields = ('titulo', 'descriçao', 'status')
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Digite o título aqui'}),
            'descriçao': forms.Textarea(attrs={'placeholder': 'Descreva a sujestão'}),

        }
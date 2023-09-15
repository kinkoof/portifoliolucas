from django.db import models

# Create your models here.

STATUS = (
    ('fazendo', 'Fazendo'),
    ('feito', 'Feito'),
    ('fazer', 'Fazer')
    )

class Projeto(models.Model):

    titulo = models.CharField(max_length=255)
    descriçao = models.TextField(verbose_name='descrição')
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.titulo


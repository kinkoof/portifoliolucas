from django.db import models

# Create your models here.


class Projeto(models.Model):

    titulo = models.CharField(max_length=255)
    descriçao = models.TextField(verbose_name='descrição')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.titulo


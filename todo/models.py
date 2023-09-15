from django.db import models

# Create your models here.

STATUS = (
    ('backlog', 'Backlog'),
    ('to do', 'To do'),
    ('doing', 'Doing'),
    ('done', 'Done')
    )

class Todo(models.Model):

    titulo = models.CharField(max_length=255)
    descriçao = models.TextField(verbose_name='descrição')
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):   #serve para mostrar o titulo da tarefa quando for chamado
        return self.titulo
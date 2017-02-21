from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Turmas(models.Model):
    disciplina = models.CharField(max_length=200)
    semestre = models.CharField(max_length=2)
    curso = models.CharField(max_length=200)
    dia_aula = models.CharField(max_length=5)
    hora_inicio = models.CharField(max_length=10)
    hora_fim = models.CharField(max_length=10)
    codigo = models.CharField(max_length=10)
    lixo = models.CharField(max_length=4)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.

class Aula(models.Model):
    titulo = models.CharField('Aula', max_length=100)
    data_lancamento = models.DateField('Data Lançamento')
    disponivel = models.BooleanField('Disponivel?', default=True)

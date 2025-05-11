from django.db import models

# Create your models here.

class Item(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    unid_medida = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome


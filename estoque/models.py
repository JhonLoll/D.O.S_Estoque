from django.db import models

# Create your models here.

class Item(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    unid_medida = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    quantidade = models.IntegerField()
    endereco = models.CharField(max_length=50)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=False)

    def __str__(self):
        return self.endereco


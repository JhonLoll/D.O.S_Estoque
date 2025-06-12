from django.db import models

# Create your models here.

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=50)
    sku = models.CharField(max_length=16)

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    quantidade = models.IntegerField()
    endereco = models.CharField(max_length=50)
    dt_ultima_entrada = models.DateTimeField(auto_now_add=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=False)

    def __str__(self):
        return self.endereco


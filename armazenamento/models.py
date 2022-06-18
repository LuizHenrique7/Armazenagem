from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    dataCriacao = models.DateTimeField(default=timezone.now)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField()


class PedidoItem(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=100, decimal_places=2)
    desconto = models.DecimalField(max_digits=10, decimal_places=2)


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    imagemURL = models.CharField(max_length=200)
    quantidade_estoque = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome

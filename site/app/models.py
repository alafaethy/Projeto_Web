from django.db import models
from datetime import datetime

# Create your models here.

# class Produtos(models.Model):
#     nome = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.nome

# class Vendedor(models.Model):
#     nome = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.nome

# class Vendas(models.Model):
#     nome_produto = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING)
#     vendedor = models.ForeignKey(Vendedor,on_delete=models.DO_NOTHING)
#     total = models.FloatField()
#     datatime = models.DateTimeField(default=datetime.now())

#     def __str__(self):
#         return self.nome_produto.nome
    



class Ticket(models.Model):
    ticket = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    cota = models.CharField(max_length=50)

    price = models.FloatField()
    var_mercado_preco = models.FloatField()
    var_preco_porcento = models.CharField(max_length=100)

    ultimo_rendimento = models.FloatField()
    proximo_rendimento = models.FloatField() # <<<- sera calculado antes de enviar para o banco



    div_yield_mes = models.CharField(max_length=100)
    div_yield_ano = models.CharField(max_length=100)

    datatime = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.ticket

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
    company = models.CharField(max_length=200)
    cota = models.CharField(max_length=50 , null=True)

    price = models.FloatField()
    preco_mercado = models.FloatField(null= True)
    mercado_percente = models.CharField(max_length=100,null=True)

    rendimento = models.FloatField(null=True)
    px_rendimento = models.FloatField(null=True) # <<<- sera calculado antes de enviar para o banco



    yld_mes = models.CharField(max_length=100,null=True)
    yld_ano = models.CharField(max_length=100,null=True)

    datatime = models.DateTimeField(default=datetime.now())
    def __str__(self) -> str:
        return self.ticket

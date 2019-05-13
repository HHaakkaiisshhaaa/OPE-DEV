from django.db import models

# Create your models here.


class Produto(models.Model):
    nome_produto = models.CharField(max_length = 30)
    descricao_produto = models.CharField(max_length = 50)
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade_produto = models.IntegerField()

    def __str__(self):
        nome_produto = self.nome_produto
        descricao_produto =self.descricao_produto 
        preco_compra= str(self.preco_compra )
        quantidade_produto= str(self.quantidade_produto )
        return 'Nome  {} Descrição  {} Preço {} Quantidade {}'.format(nome_produto,descricao_produto,preco_compra,quantidade_produto)
    

from django.db import models


class Produto(models.Model):

    nome = models.CharField("nome", max_length=15, help_text="nome do produto")
    preco = models.DecimalField ("Preço", max_digits=8, decimal_places=0, help_text='informe o preço')
    fornecedor = models.CharField("Fornecedor", max_length=99, help_text="nome do fornecedor")
    quantidade = models.DecimalField("Quantidade", max_digits=8, decimal_places=0, help_text="Quantidade em estoque do produto")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.nome}"

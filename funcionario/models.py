from django.db import models
from home.models import Pessoa


class Funcionario(Pessoa):
    funcao = models.CharField('função', max_length=58, help_text='Função')
    data_admissao = models.DateField('Admissão', help_text='Data de admissão')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return super().name

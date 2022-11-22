from django.db import models
from home.models import Pessoa


class Cliente(Pessoa):
    endereço = models.CharField('endereço', max_length=100, help_text='endereço completo')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return super().nome

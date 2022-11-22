from django.db import models

class Atendimento(models.Model):
    SITUACAO_OPCOES ={
        ('A', 'Agendado'),
        ('R', 'Realizado'),
        ('C', 'Cancelado')
    }


    horario = models.DateTimeField('Horario', help_text='Data e hora do atendimento')
    cliente = models.ForeignKey('cliente.Cliente', verbose_name='Cliente', help_text='Nome do cliente',
                            on_delete=models.CASCADE)
    funcionario = models.ForeignKey('funcionario.Funcionario', verbose_name='Funcionario',
                                help_text='Nome do funcionario', on_delete=models.CASCADE)
    situacao = models.CharField('Situação', max_length=15,help_text='Situações do atendimento', choices=SITUACAO_OPCOES,default='A')
    servico = models.ForeignKey('servico.Servico', verbose_name='Servico', help_text='Nome do serviço', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'

    def __str__(self):
        return f'Cliente: {self.cliente} Funcionario: {self.funcionario} - Servico: {self.servico}'

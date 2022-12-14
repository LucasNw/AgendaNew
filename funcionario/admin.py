from django.contrib import admin
from django.utils.html import format_html
from funcionario.models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    fields = ('nome', 'endereco', 'fone', 'email', 'funcao', 'data_admissao', 'foto', 'fotografia')
    list_display = ('nome', 'fone', 'email', 'funcao')
    readonly_fields = ['fotografia']

    def fotografia(self, obj):
       if obj.foto:
           return format_html('<img width="75px" src="{}" />', obj.foto.url)
       pass

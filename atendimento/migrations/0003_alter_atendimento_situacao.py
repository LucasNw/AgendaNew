# Generated by Django 4.1.2 on 2022-11-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0002_alter_atendimento_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='situacao',
            field=models.CharField(choices=[('A', 'Agendado'), ('C', 'Cancelado'), ('R', 'Realizado')], default='A', help_text='Situações do atendimento', max_length=15, verbose_name='Situação'),
        ),
    ]

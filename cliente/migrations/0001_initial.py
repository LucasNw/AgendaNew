# Generated by Django 4.1.2 on 2022-11-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='nome completo', max_length=58, verbose_name='nome')),
                ('fone', models.CharField(help_text='número de telefone', max_length=15, verbose_name='Telefone')),
                ('email', models.EmailField(help_text='endereço de email', max_length=168, unique=True, verbose_name='E-mail')),
                ('endereco', models.CharField(help_text='endereço completo', max_length=100, verbose_name='endereço')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]

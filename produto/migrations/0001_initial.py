# Generated by Django 4.1.2 on 2022-11-01 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='nome do produto', max_length=15, verbose_name='nome')),
                ('preco', models.DecimalField(decimal_places=0, help_text='informe o preço', max_digits=8, verbose_name='Preço')),
                ('fornecedor', models.CharField(help_text='nome do fornecedor', max_length=99, verbose_name='Fornecedor')),
                ('quantidade', models.DecimalField(decimal_places=0, help_text='Quantidade em estoque do produto', max_digits=8, verbose_name='Quantidade')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
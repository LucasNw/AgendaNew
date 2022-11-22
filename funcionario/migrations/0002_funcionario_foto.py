# Generated by Django 4.1.2 on 2022-11-08 20:01

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='pessoas', variations={'thumbmail': {'crop': True, 'height': 100, 'width': 100}}, verbose_name='foto'),
        ),
    ]

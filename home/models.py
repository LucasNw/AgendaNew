from django.db import models
from stdimage import StdImageField

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=58, help_text='nome completo')
    fone = models.CharField('Telefone', max_length=15, help_text='número de telefone')
    email = models.EmailField('E-mail', max_length=168, help_text='endereço de email', unique=True)
    foto = StdImageField('foto', upload_to='pessoas', variations={'thumbmail':{'width': 100, 'height': 100, 'crop': True}}, delete_orphans=True , null= True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
from django.db import models
from django.urls import reverse

class Inscricao(models.Model):
    nome = models.CharField('Nome', blank=False, max_length=100)
    email = models.EmailField('E-mail', blank=False, unique=True)
    grupo = models.BooleanField(verbose_name='Deseja entrar em nosso grupo?', blank=True, null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
    
    def get_absolute_url(self):
        return reverse('index')

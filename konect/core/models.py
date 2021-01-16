from django.db import models
from django.urls import reverse

class Area(models.Model):
    titulo = models.CharField('Título', blank=False, max_length=100)
    slug = models.SlugField('Atalho', unique=True)
    icone = models.ImageField(
        upload_to='core/areas',
        verbose_name='Icone da área',
        blank=False
    )

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'
    
    def get_absolute_url(self):
        return reverse('area_view', args=[self.slug])

class Oportunidade(models.Model): 
    titulo = models.CharField('Título', blank=False, max_length=100)
    slug = models.SlugField('Atalho', unique=True)
    icone = models.ImageField(
        upload_to='core/oportunidades',
        verbose_name='Icone a oportunidade',
        blank=False
    )
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Oportunidade'
        verbose_name_plural = 'Oportunidades'
    
    def get_absolute_url(self):
        return reverse('oportunidade_view', args=[self.slug])
    

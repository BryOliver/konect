from django.db import models
from django.urls import reverse

class Categoria(models.Model): 
    titulo = models.CharField('Título', blank=False, max_length=100)
    slug = models.SlugField('Atalho', unique=True)
    icone = models.ImageField(
        upload_to='core/categorias',
        verbose_name='Icone da categoria',
        blank=False
    )

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Area(models.Model):
    titulo = models.CharField('Título', blank=False, max_length=100)
    slug = models.SlugField('Atalho', unique=True)
    icone = models.ImageField(
        upload_to='core/areas',
        verbose_name='Icone da área',
        blank=False
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'
    
    def get_absolute_url(self):
        return reverse('area_view', args=[self.slug])

class Empresa(models.Model):
    titulo = models.CharField('Título', blank=False, max_length=100)
    icone = models.ImageField(
        upload_to='core/empresas',
        verbose_name='Icone a oportunidade',
        blank=False
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

class Oportunidade(models.Model): 
    titulo = models.CharField('Título', blank=False, max_length=100)
    slug = models.SlugField('Atalho', unique=True)
    icone = models.ImageField(
        upload_to='core/oportunidades',
        verbose_name='Icone a oportunidade',
        blank=False
    )
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Oportunidade'
        verbose_name_plural = 'Oportunidades'
    
    def get_absolute_url(self):
        return reverse('oportunidade_view', args=[self.slug])
    

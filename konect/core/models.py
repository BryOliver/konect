from django.db import models
from django.urls import reverse

class Categoria(models.Model): 
    titulo = models.CharField('Título', blank=False, max_length=100)
    slug = models.SlugField('Atalho', unique=True)
    icone = models.ImageField(
        upload_to='core/categorias',
        verbose_name='Icone da categoria',
        blank=True
    )

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def get_absolute_url(self):
        return reverse('categoria_view', args=[self.slug])

class Area(models.Model):
    titulo = models.CharField('Título', blank=False, max_length=100)
    slug = models.SlugField('Atalho', unique=True)
    icone = models.ImageField(
        upload_to='core/areas',
        verbose_name='Icone da área',
        blank=False
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.TextField('Descrição', max_length=500, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'
    
    def get_absolute_url(self):
        return reverse('area_view', args=[self.slug])

class Pergunta(models.Model):
    pergunta = models.TextField('Pergunta', max_length=500)
    resposta = models.TextField('Resposta', max_length=500)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return "Pergunta " + str(self.id) + " - " + str(self.area)
    
    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

class Empresa(models.Model):
    titulo = models.CharField('Título', blank=False, max_length=100)
    icone = models.ImageField(
        upload_to='core/empresas',
        verbose_name='Icone a oportunidade',
        blank=False
    )
    area_de_atuacao = models.CharField('Área de atuação', blank=True, max_length=100)
    link_doacao = models.TextField('Link para doações', max_length=500, blank=True)
    link_instagram = models.TextField('Link para o instagram', max_length=500, blank=True)

    def __str__(self):
        return self.titulo

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
    descricao = models.TextField('Descrição', max_length=500, blank=True)
    atuacao = models.CharField('Atuação', blank=True, max_length=100)
    data = models.CharField('Inscrições até', blank=True, max_length=100)
    beneficios = models.TextField('Benefícios', max_length=500, blank=True)
    vagas = models.TextField('Vagas', max_length=500, blank=True)
    link_inscricao = models.TextField('link de inscrição', max_length=500, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Oportunidade'
        verbose_name_plural = 'Oportunidades'
    
    def get_absolute_url(self):
        return reverse('oportunidade_view', args=[self.slug])
    
class Banner(models.Model):
    titulo = models.CharField('Título', max_length=100)
    frase = models.TextField('Frase', max_length=100)
    pergunta = models.CharField('Segundo título', max_length=100)
    descricao = models.TextField('Segunda frase', max_length=100)

    def __str__(self):
        return "Versão " + str(self.id)
    
    class Meta: 
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

class QuemSomos(models.Model):
    titulo = models.CharField('Título', max_length=100)
    subtitulo = models.CharField('Subtítulo', max_length=100)
    texto = models.TextField('Texto', max_length=500)

    def __str__(self):
        return "Versão " + str(self.id)
    
    class Meta: 
        verbose_name = 'Quem somos'
        verbose_name_plural = 'Quem somos'
    
class Cadastro(models.Model):
    titulo = models.CharField('Título', max_length=100)
    subtitulo = models.CharField('Subtítulo', max_length=100)
    texto = models.TextField('Texto', max_length=500)

    def __str__(self):
        return "Versão " + str(self.id)
    
    class Meta: 
        verbose_name = 'Cadastro'
        verbose_name_plural = 'Cadastro'
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Inscricao

class InscricaoCreate(CreateView):
    model = Inscricao
    fields = ['nome', 'email']
    template_name = 'inscricao.html'
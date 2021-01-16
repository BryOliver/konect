from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    areas = Area.objects.all()

    context = {
        'areas' : areas,
    }

    return render(request, 'index.html', context)

def area_view(request, slug):
    area = get_object_or_404(Area, slug=slug)
    oportunidades = Oportunidade.objects.filter(area=area)

    context = {
        'area' : area,
        'oportunidades' : oportunidades,
    }

    return render(request, 'oportunidade-list.html', context)

def oportunidade_view(request, slug):
    oportunidade = get_object_or_404(Oportunidade, slug=slug)

    context = {
        'oportunidade' : oportunidade,
    }

    return render(request, 'oportunidade-view.html', context)
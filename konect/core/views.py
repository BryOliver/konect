from django.shortcuts import render, get_object_or_404
from .models import *
from inscrito.models import *
from django.views.generic.edit import CreateView

class Index(CreateView):
    model = Inscricao
    fields = ['nome', 'email']
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['areas'] = Area.objects.all()
        return context

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

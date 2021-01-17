from django.urls import path, include
from .views import Index, area_view, oportunidade_view, categoria_view

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('categoria/<slug:slug>', categoria_view, name='categoria_view'),
    path('area/<slug:slug>', area_view, name='area_view'),
    path('oportunidade/<slug:slug>', oportunidade_view, name='oportunidade_view'),
]
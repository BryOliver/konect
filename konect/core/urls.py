from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('area/<slug:slug>', views.area_view, name='area_view'),
    path('oportunidade/<slug:slug>', views.oportunidade_view, name='oportunidade_view'),
]
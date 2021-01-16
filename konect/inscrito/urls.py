from django.urls import path
from .views import InscricaoCreate

urlpatterns = [
    path('', InscricaoCreate.as_view(), name='inscricao-create'),
]
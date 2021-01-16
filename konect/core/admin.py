from django.contrib import admin
from .models import *

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('titulo', )}

@admin.register(Oportunidade)
class OportunidadeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('titulo', )}



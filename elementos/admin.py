from django.contrib import admin
from .models import Carta, Nota

@admin.register(Carta)
class CartasAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'cuerpo', 'fecha']

@admin.register(Nota)
class NotasAdmin(admin.ModelAdmin):
    list_display = ['cuerpo']
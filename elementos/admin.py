from django.contrib import admin
from .models import Carta, Nota, Foto

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion_corta', 'creada', 'subida_por']
    list_filter = ['subida_por', 'creada']
    
    def descripcion_corta(self, obj):
        return obj.descripcion[:50] if obj.descripcion else "Sin descripción"
    descripcion_corta.short_description = "Descripción"
    
    def save_model(self, request, obj, form, change):
        if not change:  # Si es nueva foto desde admin
            obj.subida_por = 'admin'
        super().save_model(request, obj, form, change)
        
@admin.register(Carta)
class CartasAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'cuerpo', 'fecha']

@admin.register(Nota)
class NotasAdmin(admin.ModelAdmin):
    list_display = ['cuerpo']
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Carta, Nota, Foto
from decouple import config
import random
import os


PASSWORD_NOTA = config('PASSWORD_NOTA')
def inicio(request):
    error = None

    if request.method == "POST":
        if request.POST.get("password") == PASSWORD_NOTA:
            cuerpo = request.POST.get("cuerpo")

            if cuerpo:
                Nota.objects.create(
                    cuerpo=cuerpo,
                    autor="Abi ❤️"
                )
                return redirect("elementos:inicio")
        else:
            error = "Contraseña incorrecta"

    total_cartas = Carta.objects.count()
    notas = Nota.objects.all().order_by('-creada')

    return render(request, 'inicio.html', {
        'total_cartas': total_cartas,
        'notas': notas,
        'error': error
    })


def lista_cartas(request):
    cartas = Carta.objects.all().order_by('-fecha')
    return render(request, 'lista_cartas.html', {
        'cartas': cartas
    })


def detalle_carta(request, id):
    carta = get_object_or_404(Carta, id=id)
    return render(request, 'detalle_carta.html', {
        'carta': carta
    })


PASSWORD = config('PASSWORD')

def subir_foto(request):
    error = None

    if request.method == "POST":
        if request.POST.get("password") == PASSWORD:
            imagen = request.FILES.get("imagen")
            descripcion = request.POST.get("descripcion")

            if imagen:
                
                Foto.objects.create(
                    imagen=imagen, 
                    descripcion=descripcion,
                    subida_por='ella'
                )
                return redirect("elementos:collage")
        else:
            error = "Contraseña incorrecta"

    return render(request, "subir_foto.html", {"error": error})

def collage(request):
    fotos = list(Foto.objects.all())
    random.shuffle(fotos)

    return render(request, "collage.html", {"fotos": fotos})    
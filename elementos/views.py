from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Carta, Nota, Foto
import random

def inicio(request):
    total_cartas = Carta.objects.count()
    notas = Nota.objects.all().order_by('-creada')

    return render(request, 'inicio.html', {
        'total_cartas': total_cartas,
        'notas': notas
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


PASSWORD = "16112026"

def subir_foto(request):
    error = None

    if request.method == "POST":
        if request.POST.get("password") == PASSWORD:
            imagen = request.FILES.get("imagen")
            descripcion = request.POST.get("descripcion")

            if imagen:
                Foto.objects.create(imagen=imagen, descripcion=descripcion)
                return redirect("elementos:collage")
        else:
            error = "Contraseña incorrecta"

    return render(request, "subir_foto.html", {"error": error})

def collage(request):
    fotos = list(Foto.objects.all())
    random.shuffle(fotos)

    return render(request, "collage.html", {"fotos": fotos})
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Carta, Nota


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

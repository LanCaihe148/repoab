from django.urls import path
from . import views

app_name = 'elementos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cartas/', views.lista_cartas, name='lista_cartas'),
    path('cartas/<int:id>/', views.detalle_carta, name='detalle_carta'),
]

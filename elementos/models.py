from django.db import models
from django.utils import timezone

class Carta(models.Model):
    titulo = models.CharField(max_length=30)
    cuerpo = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.titulo


class Nota(models.Model):
    cuerpo = models.TextField()
    creada = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cuerpo[:30]
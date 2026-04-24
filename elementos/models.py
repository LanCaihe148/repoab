from django.db import models
from django.utils import timezone

class Carta(models.Model):
    titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    fecha = models.DateField()
    correo_enviado = models.BooleanField(default=False)
    def __str__(self):
        return self.titulo


class Nota(models.Model):
    cuerpo = models.TextField()
    creada = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=20, default="Efra ❤️")
    def __str__(self):
        return self.cuerpo[:30]


from cloudinary.models import CloudinaryField

class Foto(models.Model):
    imagen = CloudinaryField('imagen')
    descripcion = models.TextField(blank=True, null=True)
    creada = models.DateTimeField(auto_now_add=True)
    
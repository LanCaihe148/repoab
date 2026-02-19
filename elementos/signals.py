from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Carta, Nota
import socket
import os
# ⏱️ timeout global para SMTP (CRÍTICO)
socket.setdefaulttimeout(5)

DESTINATARIO = "sandovalpitsakise@gmail.com"  # ← Correo destino

@receiver(post_save, sender=Carta)
def notificar_nueva_carta(sender, instance, created, **kwargs):
    if not created:
        return

    try:
        send_mail(
            subject='💌 Nueva carta para Abi',
            message=f'Tienes una nueva carta:\n\n{instance.titulo}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[DESTINATARIO],  # ← Cambiado
            fail_silently=False,            # Para ver errores durante pruebas
        )
    except Exception as e:
        print("⚠️ Error enviando correo carta:", e)
        os.system("python manage.py shell from sendgrid_django import SendgridBackend")


@receiver(post_save, sender=Nota)
def notificar_nueva_nota(sender, instance, created, **kwargs):
    if not created:
        return

    try:
        send_mail(
            subject='📝 Nueva nota',
            message=instance.cuerpo[:200],
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[DESTINATARIO],  # ← Cambiado
            fail_silently=False,            # Para ver errores durante pruebas
        )
    except Exception as e:
        print("⚠️ Error enviando correo nota:", e)

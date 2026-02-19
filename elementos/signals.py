from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Carta, Nota
import socket

# ⏱️ timeout global para SMTP (CRÍTICO)
socket.setdefaulttimeout(5)


@receiver(post_save, sender=Carta)
def notificar_nueva_carta(sender, instance, created, **kwargs):
    if not created:
        return

    try:
        send_mail(
            subject='💌 Nueva carta para Abi',
            message=f'Tienes una nueva carta:\n\n{instance.titulo}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=True,
        )
    except Exception as e:
        print("⚠️ Error enviando correo carta:", e)


@receiver(post_save, sender=Nota)
def notificar_nueva_nota(sender, instance, created, **kwargs):
    if not created:
        return

    try:
        send_mail(
            subject='📝 Nueva nota',
            message=instance.cuerpo[:200],
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=True,
        )
    except Exception as e:
        print("⚠️ Error enviando correo nota:", e)

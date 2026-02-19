from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from django.core.mail import send_mail
from .models import Carta, Nota


# ===============================
# CARTAS
# ===============================
@receiver(post_save, sender=Carta)
def notificar_nueva_carta(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: enviar_correo_carta(instance))


def enviar_correo_carta(instance):
    try:
        send_mail(
            subject='💌 Nueva carta para Abi',
            message=f'Tienes una nueva carta:\n\n{instance.contenido}',
            from_email=None,  # usa DEFAULT_FROM_EMAIL
            recipient_list=['sandovalpitsakise@gmail.com'],
            fail_silently=True,
        )
    except Exception:
        pass


# ===============================
# NOTAS
# ===============================
@receiver(post_save, sender=Nota)
def notificar_nueva_nota(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: enviar_correo_nota(instance))


def enviar_correo_nota(instance):
    try:
        send_mail(
            subject='📝 Nueva nota para Abi',
            message=f'Tienes una nueva nota:\n\n{instance.contenido}',
            from_email=None,
            recipient_list=['sandovalpitsakise@gmail.com'],
            fail_silently=True,
        )
    except Exception:
        pass

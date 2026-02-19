from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Carta, Nota


@receiver(post_save, sender=Carta)
def notificar_nueva_carta(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='💌 Nueva carta para Abi',
            message=f'Se publicó una nueva carta:\n\n{instance.titulo}',
            from_email=None,
            recipient_list=['sandovalpitsakise@gmail.com'],
            fail_silently=True,
        )


@receiver(post_save, sender=Nota)
def notificar_nueva_nota(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='📝 Nueva nota',
            message='Se publicó una nueva nota para Abi 💖',
            from_email=None,
            recipient_list=['sandovalpitsakise@gmail.com'],
            fail_silently=False,
        )

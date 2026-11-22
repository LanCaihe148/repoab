from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Carta, Nota, Foto

DESTINATARIO = "sandovalpitsakise@gmail.com"  # ← Correo al que llegan los avisos
SITIO = "https://repoab.vercel.app"


def _enviar(asunto, mensaje):
    """Manda el correo. Si falla, lo deja en los logs pero NO tumba la página."""
    try:
        send_mail(
            subject=asunto,
            message=mensaje,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[DESTINATARIO],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print("⚠️ Error enviando correo:", e)
        return False


@receiver(post_save, sender=Carta)
def notificar_nueva_carta(sender, instance, created, **kwargs):
    if not created:
        return

    enviado = _enviar(
        "💌 Nueva carta para Abi",
        f"Tienes una nueva carta:\n\n{instance.titulo}\n\n"
        f"Léela aquí: {SITIO}/cartas/{instance.id}/",
    )
    if enviado:
        # .update() no vuelve a disparar esta señal
        Carta.objects.filter(pk=instance.pk).update(correo_enviado=True)


@receiver(post_save, sender=Nota)
def notificar_nueva_nota(sender, instance, created, **kwargs):
    if not created:
        return

    _enviar(
        "📝 Nueva nota",
        f"{instance.cuerpo[:200]}\n\n— {instance.autor}\n\n{SITIO}/",
    )


@receiver(post_save, sender=Foto)
def notificar_nueva_foto(sender, instance, created, **kwargs):
    # Solo avisamos cuando la sube ella desde la página;
    # las fotos que subes tú desde el admin no mandan correo.
    if not created or instance.subida_por != 'ella':
        return

    _enviar(
        "📸 Nuevo recuerdo en el collage",
        f"Se subió una foto nueva:\n\n{instance.descripcion or '(sin descripción)'}\n\n"
        f"Verla: {SITIO}/collage/",
    )

from django.apps import AppConfig


class ElementosConfig(AppConfig):
    name = 'elementos'

    def ready(self):
        import elementos.signals
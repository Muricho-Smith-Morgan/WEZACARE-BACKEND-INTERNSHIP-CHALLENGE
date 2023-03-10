from django.apps import AppConfig


class WezaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weza'

    def ready(self):
        import weza.signals
        
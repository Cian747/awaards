from django.apps import AppConfig


class GreazeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'greaze'

    def ready(self):
        import greaze.signals
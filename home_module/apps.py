from django.apps import AppConfig


class HomeModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home_module'

    def ready(self):
        import home_module.signals
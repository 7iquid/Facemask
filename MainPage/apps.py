from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'MainPage'

    def ready(self):
        from backgroundTask import updater
        updater.start()
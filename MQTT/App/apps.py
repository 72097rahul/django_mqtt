from django.apps import AppConfig



class AppConfig(AppConfig):
    name = 'App'

    def ready(self):
        from .mqtt import client
        client.loop_start()

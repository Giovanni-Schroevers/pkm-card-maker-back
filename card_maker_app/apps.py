from django.apps import AppConfig


class CardMakerAppConfig(AppConfig):
    name = 'card_maker_app'

    def ready(self):
        import card_maker_app.signals

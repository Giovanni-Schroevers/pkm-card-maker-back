from django.db import models

from card_maker_app.models.named_model import NamedModel


class Set(NamedModel):
    number = models.IntegerField()

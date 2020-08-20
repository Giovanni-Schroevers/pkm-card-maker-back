from django.db import models

from card_maker_app.models import Type
from card_maker_app.models.named_model import NamedModel


class Supertype(NamedModel):
    types = models.ManyToManyField(Type)

from django.db import models

from card_maker_app.models import Type, Subtype
from card_maker_app.models.named_model import NamedModel


class Supertype(NamedModel):
    types = models.ManyToManyField(Type, related_name='supertypes')
    subtypes = models.ManyToManyField(Subtype, related_name='supertypes')

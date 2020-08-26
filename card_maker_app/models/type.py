from django.db import models

from card_maker_app.models import Subtype, Rarity
from card_maker_app.models.named_model import NamedModel


class Type(NamedModel):
    subtype_required = models.BooleanField()
    has_white_text = models.BooleanField()
    has_sub_name = models.BooleanField()
    has_special_style = models.BooleanField()
    is_energy = models.BooleanField()
    subtypes = models.ManyToManyField(Subtype, related_name='types')
    rarities = models.ManyToManyField(Rarity, related_name='types')

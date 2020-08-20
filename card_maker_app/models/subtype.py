from django.db import models

from card_maker_app.models import Rarity, Variation
from card_maker_app.models.named_model import NamedModel


class Subtype(NamedModel):
    has_prevolve = models.BooleanField()
    has_pokedex_entry = models.BooleanField()
    has_description = models.BooleanField()
    has_white_top_text = models.BooleanField()
    has_v_style = models.BooleanField()
    has_v_symbol = models.BooleanField()
    has_name_outline = models.BooleanField()
    has_vmax_symbol = models.BooleanField()
    rarities = models.ManyToManyField(Rarity)
    variations = models.ManyToManyField(Variation)

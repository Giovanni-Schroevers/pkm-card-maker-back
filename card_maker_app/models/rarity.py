from django.db import models

from card_maker_app.models.named_model import NamedModel


class Rarity(NamedModel):
    has_name_outline = models.BooleanField()
    has_black_top_text = models.BooleanField()
    has_v_style = models.BooleanField()

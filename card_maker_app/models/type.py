from django.db import models

from card_maker_app.models import Subtype
from card_maker_app.models.named_model import NamedModel


class Type(NamedModel):
    sub_type_required = models.BooleanField()
    has_white_text = models.BooleanField()
    has_sub_name = models.BooleanField()
    has_special_style = models.BooleanField()
    is_energy = models.BooleanField()
    subtypes = models.ManyToManyField(Subtype)

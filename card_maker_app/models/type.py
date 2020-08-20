from django.db import models

from card_maker_app.models import Subtype
from card_maker_app.models.named_model import NamedModel


class Type(NamedModel):
    sub_type_required = models.BooleanField()
    has_white_text = models.BooleanField(default=False)
    has_sub_name = models.BooleanField(default=False)
    has_special_style = models.BooleanField(default=False)
    subtypes = models.ManyToManyField(Subtype)

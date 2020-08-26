from django.db import models

from card_maker_app.models import BaseSet
from card_maker_app.models.named_model import NamedModel


class Set(NamedModel):
    number = models.IntegerField()
    base_set = models.ForeignKey(BaseSet, on_delete=models.CASCADE, related_name='sets', null=True, blank=True)

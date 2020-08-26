from django.db import models

from card_maker_app.models import Type
from card_maker_app.models.move import Move


class MoveEnergyCost(models.Model):
    move = models.ForeignKey(Move, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    amount = models.IntegerField()

    class Meta:
        db_table = Move._meta.app_label + "_move_energy_cost"

    def __str__(self):
        return self.move

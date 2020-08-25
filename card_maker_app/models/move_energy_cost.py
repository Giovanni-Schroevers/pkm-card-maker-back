from django.db import models

from card_maker_app.models import Move, Type


class MoveEnergyCost(models.Model):
    move = models.ForeignKey(Move, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    amount = models.IntegerField()

    class Meta:
        db_table = Move._meta.app_label + "move_energy_cost"

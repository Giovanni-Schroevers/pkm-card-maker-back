from django.db import models

from card_maker_app.models import Type


class Move(models.Model):
    name = models.CharField(max_length=255)
    damage = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    types = models.ManyToManyField(Type, through='MoveEnergyCost', related_name='move_energy_cost')

    def __str__(self):
        return self.name

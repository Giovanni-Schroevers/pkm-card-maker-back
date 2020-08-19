from django.db import models

from card_maker_app.models import SuperType


class Card(models.Model):
    name = models.CharField(max_length=255)
    sub_name = models.CharField(max_length=255, null=True, blank=True)
    hit_points = models.IntegerField()
    card_number = models.CharField(max_length=255)
    total_cards = models.CharField(max_length=255)
    illustrator = models.CharField(max_length=255)
    weakness_amount = models.IntegerField()
    resistance_amount = models.IntegerField()
    retreat_cost = models.IntegerField()
    pokedex_entry = models.CharField(max_length=255)
    description = models.TextField()
    prevolve_name = models.CharField(max_length=255, null=True, blank=True)
    background_image = models.FileField(upload_to='card')
    super_type = models.ForeignKey(SuperType, on_delete=models.PROTECT)


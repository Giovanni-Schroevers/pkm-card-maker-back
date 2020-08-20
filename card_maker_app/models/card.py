from django.db import models

from card_maker_app.models import Supertype, Type, Subtype, Rarity, Rotation, RarityIcon


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
    background_image = models.FileField(upload_to='card/', null=True, blank=True)
    card_image = models.FileField(upload_to='card/', null=True, blank=True)
    top_image = models.FileField(upload_to='card/', null=True, blank=True)
    type_image = models.FileField(upload_to='card/', null=True, blank=True)
    prevolve_image = models.FileField(upload_to='card/', null=True, blank=True)
    super_type = models.ForeignKey(Supertype, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    subtype = models.ForeignKey(Subtype, on_delete=models.PROTECT, null=True, blank=True)
    rarity = models.ForeignKey(Rarity, on_delete=models.PROTECT, null=True, blank=True)
    rotation = models.ForeignKey(Rotation, on_delete=models.PROTECT)
    rarity_icon = models.ForeignKey(RarityIcon, on_delete=models.PROTECT)


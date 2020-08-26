from django.db import models

from card_maker_app.models import Supertype, Type, Subtype, Rarity, Rotation, RarityIcon, Set, BaseSet, Move, \
                                  Variation, User


class Card(models.Model):
    name = models.CharField(max_length=255)
    sub_name = models.CharField(max_length=255, null=True, blank=True)
    hit_points = models.IntegerField(null=True, blank=True)
    card_number = models.CharField(max_length=255)
    total_cards = models.CharField(max_length=255)
    illustrator = models.CharField(max_length=255)
    weakness_amount = models.IntegerField(null=True, blank=True)
    weakness_type = models.ForeignKey(
        Type, on_delete=models.PROTECT, related_name='card_weakness', null=True, blank=True
    )
    resistance_amount = models.IntegerField(null=True, blank=True)
    resistance_type = models.ForeignKey(
        Type, on_delete=models.PROTECT, null=True, blank=True, related_name='card_resistance'
    )
    retreat_cost = models.IntegerField(null=True, blank=True)
    pokedex_entry = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    prevolve_name = models.CharField(max_length=255, null=True, blank=True)
    background_image = models.FileField(upload_to='card/', null=True, blank=True)
    card_image = models.FileField(upload_to='card/', null=True, blank=True)
    top_image = models.FileField(upload_to='card/', null=True, blank=True)
    type_image = models.FileField(upload_to='card/', null=True, blank=True)
    prevolve_image = models.FileField(upload_to='card/', null=True, blank=True)
    supertype = models.ForeignKey(Supertype, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='card_type')
    subtype = models.ForeignKey(Subtype, on_delete=models.PROTECT, null=True, blank=True)
    rarity = models.ForeignKey(Rarity, on_delete=models.PROTECT, null=True, blank=True)
    variation = models.ForeignKey(Variation, on_delete=models.PROTECT, null=True, blank=True)
    rotation = models.ForeignKey(Rotation, on_delete=models.PROTECT)
    rarity_icon = models.ForeignKey(RarityIcon, on_delete=models.PROTECT)
    set = models.ForeignKey(Set, on_delete=models.PROTECT, null=True, blank=True)
    base_set = models.ForeignKey(BaseSet, on_delete=models.PROTECT)
    move_1 = models.ForeignKey(Move, on_delete=models.SET_NULL, null=True, blank=True, related_name='card_move1')
    move_2 = models.ForeignKey(Move, on_delete=models.SET_NULL, null=True, blank=True, related_name='card_move2')
    move_3 = models.ForeignKey(Move, on_delete=models.SET_NULL, null=True, blank=True, related_name='card_move3')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

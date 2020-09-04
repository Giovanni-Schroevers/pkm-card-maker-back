from django.core.validators import FileExtensionValidator
from django.db import models

from card_maker_app.models import Supertype, Type, Subtype, Rarity, Rotation, RarityIcon, Set, BaseSet, Move, \
    Variation, User, Ability


class Card(models.Model):
    name = models.CharField(max_length=255)
    sub_name = models.CharField(max_length=255, null=True, blank=True)
    hit_points = models.IntegerField(null=True, blank=True)
    card_number = models.CharField(max_length=255, null=True, blank=True)
    total_cards = models.CharField(max_length=255, null=True, blank=True)
    illustrator = models.CharField(max_length=255, null=True, blank=True)
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
    background_image = models.FileField(
        upload_to='card/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]
    )
    card_image = models.ImageField(upload_to='card/', null=True, blank=True)
    top_image = models.ImageField(upload_to='card/', null=True, blank=True)
    type_image = models.ImageField(upload_to='card/', null=True, blank=True)
    prevolve_image = models.ImageField(upload_to='card/', null=True, blank=True)
    custom_set_image = models.ImageField(upload_to='card/', null=True, blank=True)
    supertype = models.ForeignKey(Supertype, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='card_type', null=True, blank=True)
    subtype = models.ForeignKey(Subtype, on_delete=models.PROTECT, null=True, blank=True)
    rarity = models.ForeignKey(Rarity, on_delete=models.PROTECT, null=True, blank=True)
    variation = models.ForeignKey(Variation, on_delete=models.PROTECT, null=True, blank=True)
    rotation = models.ForeignKey(Rotation, on_delete=models.PROTECT, null=True, blank=True)
    rarity_icon = models.ForeignKey(RarityIcon, on_delete=models.PROTECT, null=True, blank=True)
    set = models.ForeignKey(Set, on_delete=models.PROTECT, null=True, blank=True)
    base_set = models.ForeignKey(BaseSet, on_delete=models.PROTECT)
    ability = models.ForeignKey(Ability, on_delete=models.SET_NULL, null=True, blank=True)
    move_1 = models.ForeignKey(Move, on_delete=models.SET_NULL, null=True, blank=True, related_name='card_move1')
    move_2 = models.ForeignKey(Move, on_delete=models.SET_NULL, null=True, blank=True, related_name='card_move2')
    move_3 = models.ForeignKey(Move, on_delete=models.SET_NULL, null=True, blank=True, related_name='card_move3')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_card_image = models.ImageField(upload_to='card/')

    def __str__(self):
        return self.name
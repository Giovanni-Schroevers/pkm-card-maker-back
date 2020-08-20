from django.db import models

from card_maker_app.models import Card


class Ability(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

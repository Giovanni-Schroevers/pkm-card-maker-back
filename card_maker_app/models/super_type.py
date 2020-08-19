from django.db import models

from card_maker_app.models import Type


class SuperType(models.Model):
    short_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    types = models.ManyToManyField(Type)


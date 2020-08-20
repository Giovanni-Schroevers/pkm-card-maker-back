from django.db import models


class NamedModel(models.Model):
    short_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

from django.db import models


class NamedModel(models.Model):
    short_name = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

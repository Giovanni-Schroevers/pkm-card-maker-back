from django.db import models


class Type(models.Model):
    short_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sub_type_required = models.BooleanField()
    has_white_text = models.BooleanField(default=False)
    has_sub_name = models.BooleanField(default=False)
    has_special_style = models.BooleanField(default=False)

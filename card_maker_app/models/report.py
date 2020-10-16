from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel

from card_maker_app.models import User


class Report(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    categories = (
        ('sexual', 'sexual content'),
        ('harmful or hateful', 'harmful or hateful content'),
        ('violent', 'violent content'),
        ('spam', 'spam')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, choices=categories)
    description = models.TextField(null=True, blank=True)
    parent_object_id = models.IntegerField()
    parent_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT
    )
    parent = GenericForeignKey(
        'parent_content_type',
        'parent_object_id',
    )
    created_at = models.DateTimeField(auto_now_add=True)

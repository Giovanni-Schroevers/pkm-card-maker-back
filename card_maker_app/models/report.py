from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel

from card_maker_app.models import User, Category


class Report(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
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

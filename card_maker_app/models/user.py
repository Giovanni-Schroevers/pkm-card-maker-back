from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill


class User(AbstractUser):
    def directory_path(instance, filename):
        if not instance.id:
            return filename
        return f'{instance.id}/{filename}'

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    over13 = models.BooleanField(null=True, blank=True)
    photo = ProcessedImageField(
        null=True,
        blank=True,
        upload_to=directory_path,
        processors=[ResizeToFill(200, 200)],
        format='PNG',
        default='default.png'
    )
    last_name = None

    def __str__(self):
        return self.username

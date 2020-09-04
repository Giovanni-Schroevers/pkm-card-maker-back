from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='profile/')

    def __str__(self):
        return self.username

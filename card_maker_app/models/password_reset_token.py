from django.db import models
from django.utils.timezone import now

from . import User


class PasswordResetToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, related_name="password_reset_token", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = User._meta.app_label + "_password_reset_token"

    def __str__(self):
        return self.token

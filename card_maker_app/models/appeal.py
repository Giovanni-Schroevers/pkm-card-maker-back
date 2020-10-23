from django.db import models

from card_maker_app.models import UserBan, User


class Appeal(models.Model):
    statuses = (
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected')
    )

    ban = models.OneToOneField(UserBan, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.CharField(choices=statuses, default='pending', max_length=255)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.ban.user.username + ":" + self.status

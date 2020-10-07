from django.db import models

from card_maker_app.models import User


class UserFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_following')
    follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_followers')

    class Meta:
        db_table = User._meta.app_label + "_user_follow"
        unique_together = ('user', 'follow')

    def __str__(self):
        return self.user.username + ":" + self.follow.username


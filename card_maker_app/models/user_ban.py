from django.db import models

from card_maker_app.models import User, Category


class UserBan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='banned')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_admin')
    reason = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = User._meta.app_label + "_user_ban"

    def __str__(self):
        return self.user.username + ":" + self.reason.name

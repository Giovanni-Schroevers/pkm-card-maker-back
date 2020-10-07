from django.db import models

from card_maker_app.models import Card, User


class CardLike(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = User._meta.app_label + "_card_like"
        unique_together = ('card', 'user')

    def __str__(self):
        return self.card.name + ":" + self.user.username

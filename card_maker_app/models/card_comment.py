from django.db import models

from card_maker_app.models import Card, User


class CardComment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    likes = models.ManyToManyField(User, through='CommentLike', related_name='comment_like')

    class Meta:
        db_table = User._meta.app_label + "_card_comment"

    def __str__(self):
        return self.card.name + ":" + self.user.username

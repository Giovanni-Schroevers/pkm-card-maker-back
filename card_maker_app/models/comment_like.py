from django.db import models

from card_maker_app.models import CardComment, User


class CommentLike(models.Model):
    comment = models.ForeignKey(CardComment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = User._meta.app_label + "_comment_like"
        unique_together = ('comment', 'user')

    def __str__(self):
        return self.comment.card.name + ':' + self.comment.user.username + ":" + self.user.username

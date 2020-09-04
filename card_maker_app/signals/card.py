from django.db.models.signals import post_delete
from django.dispatch import receiver
from card_maker_app.models import Card


@receiver(post_delete, sender=Card)
def card_post_delete(sender, **kwargs):
    if kwargs['instance'].move_1:
        kwargs['instance'].move_1.delete()
    if kwargs['instance'].move_2:
        kwargs['instance'].move_2.delete()
    if kwargs['instance'].move_3:
        kwargs['instance'].move_3.delete()
    if kwargs['instance'].ability:
        kwargs['instance'].ability.delete()

import os
import shutil

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from card_maker import settings
from card_maker_app.models import Card, User


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


@receiver(post_save, sender=Card)
@receiver(post_save, sender=User)
def update_image_path(sender, instance, created, **kwargs):
    if created:
        for image in ['background_image', 'card_image', 'top_image', 'type_image', 'prevolve_image', 'prevolve_image',
                      'custom_set_image', 'full_card_image', 'photo']:
            if image in [item.name for item in instance._meta.get_fields()]:
                image_file = getattr(instance, image)
                if image_file:
                    old_name = image_file.name
                    if not old_name:
                        pass

                    print(old_name)
                    new_name = os.path.basename(old_name)
                    new_path = os.path.join(settings.MEDIA_ROOT, sender.directory_path(instance, new_name))
                    if not os.path.exists(os.path.dirname(new_path)):
                        os.makedirs(os.path.dirname(new_path))
                    if old_name == 'default.png':
                        shutil.copy(image_file.path, new_path)
                    else:
                        os.rename(image_file.path, new_path)
                    image_file.name = sender.directory_path(instance, new_name)
        instance.save()

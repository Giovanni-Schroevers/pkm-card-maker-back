# Generated by Django 3.1.1 on 2020-09-23 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_maker_app', '0007_user_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='hit_points',
            new_name='hitpoints',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='move_1',
            new_name='move1',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='move_2',
            new_name='move2',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='move_3',
            new_name='move3',
        ),
    ]

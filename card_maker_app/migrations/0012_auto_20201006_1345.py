# Generated by Django 3.1.1 on 2020-10-06 11:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('card_maker_app', '0011_auto_20201001_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardlike',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentlike',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

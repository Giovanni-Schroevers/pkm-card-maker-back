# Generated by Django 3.1.2 on 2020-10-28 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card_maker_app', '0023_appeal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='ban',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='card_maker_app.userban'),
        ),
    ]

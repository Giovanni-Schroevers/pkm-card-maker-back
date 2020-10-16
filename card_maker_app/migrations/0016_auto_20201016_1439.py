# Generated by Django 3.1.2 on 2020-10-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_maker_app', '0015_report_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='category',
            field=models.CharField(choices=[('sexual', 'sexual content'), ('harmful or hateful', 'harmful or hateful content'), ('violent', 'violent content'), ('spam', 'spam')], max_length=255),
        ),
    ]

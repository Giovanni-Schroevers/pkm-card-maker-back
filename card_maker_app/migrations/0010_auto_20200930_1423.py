# Generated by Django 3.1.1 on 2020-09-30 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card_maker_app', '0009_card_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_maker_app.card')),
            ],
            options={
                'db_table': 'card_maker_app_card_comment',
            },
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_maker_app.cardcomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'card_maker_app_comment_like',
                'unique_together': {('comment', 'user')},
            },
        ),
        migrations.CreateModel(
            name='CardLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_maker_app.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'card_maker_app_card_like',
                'unique_together': {('card', 'user')},
            },
        ),
        migrations.AddField(
            model_name='cardcomment',
            name='likes',
            field=models.ManyToManyField(related_name='comment_like', through='card_maker_app.CommentLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cardcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='card',
            name='comments',
            field=models.ManyToManyField(related_name='card_comments', through='card_maker_app.CardComment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='card',
            name='likes',
            field=models.ManyToManyField(related_name='card_likes', through='card_maker_app.CardLike', to=settings.AUTH_USER_MODEL),
        ),
    ]

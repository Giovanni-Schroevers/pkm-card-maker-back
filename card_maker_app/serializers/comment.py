from rest_framework import serializers

from card_maker_app.models import CardComment
from card_maker_app.serializers import UserOverviewSerializer


class CardCommentSerializer(serializers.ModelSerializer):
    user = UserOverviewSerializer()
    likes = serializers.IntegerField(source='likes.count')
    liked_by = UserOverviewSerializer(many=True, source='likes')

    class Meta:
        model = CardComment
        fields = (
            'user',
            'comment',
            'likes',
            'liked_by',
            'created_at',
            'updated_at'
        )


class CreateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardComment
        fields = (
            'card',
            'user',
            'comment',
        )

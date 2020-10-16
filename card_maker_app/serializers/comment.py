from rest_framework import serializers

from card_maker_app.models import CardComment
from card_maker_app.serializers import UserOverviewSerializer


class CardCommentOverviewSerializer(serializers.ModelSerializer):
    user = UserOverviewSerializer()

    class Meta:
        model = CardComment
        fields = (
            'id',
            'user',
            'comment',
        )


class CardCommentSerializer(serializers.ModelSerializer):
    user = UserOverviewSerializer()
    likes = serializers.IntegerField(source='likes.count')
    liked_by = UserOverviewSerializer(many=True, source='likes')
    quote = CardCommentOverviewSerializer()

    class Meta:
        model = CardComment
        fields = (
            'id',
            'user',
            'comment',
            'likes',
            'liked_by',
            'created_at',
            'updated_at',
            'quote',
        )


class CreateCommentSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        if 'quote' in attrs:
            if attrs['quote'].card != attrs['card']:
                raise serializers.ValidationError('Can not quote a comment from another card')

        return attrs

    class Meta:
        model = CardComment
        fields = (
            'card',
            'user',
            'comment',
            'quote',
        )

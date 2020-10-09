from rest_framework import serializers

from card_maker_app.models import CardLike
from card_maker_app.serializers import UserOverviewSerializer, CardOverviewSerializer


class CardLikeSerializer(serializers.ModelSerializer):
    user = UserOverviewSerializer()
    card = CardOverviewSerializer()

    class Meta:
        model = CardLike
        fields = (
            'user',
            'card',
            'created_at',
        )

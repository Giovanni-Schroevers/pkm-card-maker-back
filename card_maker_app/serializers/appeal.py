from rest_framework import serializers

from card_maker_app.models import Appeal
from card_maker_app.serializers import UserBanSerializer


class AppealCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appeal
        fields = (
            'ban',
            'text',
        )


class AppealSerializer(serializers.ModelSerializer):
    ban = UserBanSerializer(read_only=True)

    class Meta:
        model = Appeal
        fields = (
            'id',
            'ban',
            'text',
            'status',
        )

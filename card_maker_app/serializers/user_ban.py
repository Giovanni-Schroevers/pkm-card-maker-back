from rest_framework import serializers

from card_maker_app.models import UserBan


class UserBanSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserBan
        fields = (
            'id',
            'user',
            'admin',
            'reason',
            'created_at',
        )

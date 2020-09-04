from rest_framework import serializers

from card_maker_app.models import RarityIcon


class RarityIconSerializer(serializers.ModelSerializer):

    class Meta:
        model = RarityIcon
        fields = (
            'id',
            'short_name',
            'name',
        )

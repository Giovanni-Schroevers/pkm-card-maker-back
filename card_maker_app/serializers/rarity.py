from rest_framework import serializers

from card_maker_app.models import Rarity


class RaritySerializer(serializers.ModelSerializer):

    class Meta:
        model = Rarity
        fields = (
            'id',
            'short_name',
            'name',
            'has_name_outline',
            'has_black_top_text',
            'has_v_style',
        )

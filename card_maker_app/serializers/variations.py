from rest_framework import serializers

from card_maker_app.models import Variation


class VariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variation
        fields = (
            'id',
            'short_name',
            'name',
        )

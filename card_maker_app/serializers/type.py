from rest_framework import serializers

from card_maker_app.models import Type
from card_maker_app.serializers.move_energy_cost import ReadOnlyMoveEnergyCostSerializer


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = (
            'id',
            'short_name',
            'name',
            'subtype_required',
            'has_white_text',
            'has_sub_name',
            'has_special_style',
            'is_energy',
            'rarities'
        )


class EnergyCostTypeSerializer(serializers.ModelSerializer):
    amount = ReadOnlyMoveEnergyCostSerializer(many=True)

    class Meta:
        model = Type
        fields = (
            'id',
            'amount',
        )

from rest_framework import serializers

from card_maker_app.models import Move
from card_maker_app.serializers import MoveEnergyCostSerializer, ReadOnlyMoveEnergyCostSerializer


class MoveSerializer(serializers.ModelSerializer):
    energy_cost = MoveEnergyCostSerializer(many=True)

    class Meta:
        model = Move
        fields = (
            'id',
            'name',
            'damage',
            'text',
            'energy_cost',
        )


class ReadOnlyMoveSerializer(serializers.ModelSerializer):
    energy_cost = ReadOnlyMoveEnergyCostSerializer(many=True, read_only=True)

    class Meta:
        model = Move
        fields = (
            'name',
            'damage',
            'text',
            'energy_cost',
        )


class MoveCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Move
        fields = (
            'id',
            'name',
            'damage',
            'text',
        )
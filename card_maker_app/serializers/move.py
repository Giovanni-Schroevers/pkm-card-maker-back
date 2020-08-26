from rest_framework import serializers

from card_maker_app.models import Move
from card_maker_app.serializers import MoveEnergyCostSerializer


class MoveSerializer(serializers.ModelSerializer):
    move_energy_cost = MoveEnergyCostSerializer()

    class Meta:
        model = Move
        fields = (
            'id',
            'name',
            'damage',
            'text',
            'move_energy_cost',
        )

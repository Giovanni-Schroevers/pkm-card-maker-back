from rest_framework import serializers

from card_maker_app.models import MoveEnergyCost


class ReadOnlyMoveEnergyCostSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoveEnergyCost
        fields = ('type', 'amount',)


class MoveEnergyCostCreateSerializer(serializers.ModelSerializer):

    def validate_type(self, energy_type):
        if not energy_type.is_energy:
            raise serializers.ValidationError(f'You can not use the type {energy_type.name} for a move cost')

        return energy_type

    class Meta:
        model = MoveEnergyCost
        fields = (
            'id',
            'move',
            'type',
            'amount',
        )

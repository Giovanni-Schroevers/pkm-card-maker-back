from rest_framework import serializers

from card_maker_app.models import MoveEnergyCost


class MoveEnergyCostSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoveEnergyCost
        fields = (
            'id',
            'type',
            'amount',
        )


class ReadOnlyMoveEnergyCostSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField(source='move_energy_cost.amount', read_only=True)

    class Meta:
        model = MoveEnergyCost
        fields = ('id', 'amount')


class MoveEnergyCostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoveEnergyCost
        fields = (
            'id',
            'move',
            'type',
            'amount',
        )

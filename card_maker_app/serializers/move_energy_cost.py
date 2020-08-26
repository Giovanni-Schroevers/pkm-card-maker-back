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

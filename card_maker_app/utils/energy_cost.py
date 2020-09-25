from rest_framework import status
from rest_framework.response import Response

from card_maker_app.models import Type
from card_maker_app.serializers import MoveEnergyCostCreateSerializer


def save_energy_cost(energy_cost, move):
    move_energy_cost = {
        'move': move.pk,
        'type': energy_cost['type'],
        'amount': energy_cost['amount']
    }

    move_energy_cost_serializer = MoveEnergyCostCreateSerializer(data=move_energy_cost)
    move_energy_cost_serializer.is_valid(raise_exception=True)
    move_energy_cost_serializer.save()

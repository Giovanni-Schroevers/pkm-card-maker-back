from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from card_maker_app.models import Supertype, Subtype, Type, BaseSet, Set, Rarity, Variation, Rotation, RarityIcon, Card
from card_maker_app.permissions.admin import IsAdminOrGetRequest
from card_maker_app.serializers import SubtypeSerializer, SupertypeSerializer, TypeSerializer, BaseSetSerializer, \
    SetSerializer, RaritySerializer, VariationSerializer, RotationSerializer, RarityIconSerializer, CardSerializer, \
    CardCreateSerializer, MoveCreateSerializer, MoveEnergyCostCreateSerializer, AbilitySerializer


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_card_options(request):

    supertypes = SupertypeSerializer(Supertype.objects.all(), many=True).data
    types = TypeSerializer(Type.objects.all(), many=True).data
    subtypes = SubtypeSerializer(Subtype.objects.all(), many=True).data
    rarities = RaritySerializer(Rarity.objects.all(), many=True).data
    variations = VariationSerializer(Variation.objects.all(), many=True).data
    base_sets = BaseSetSerializer(BaseSet.objects.all(), many=True).data
    sets = SetSerializer(Set.objects.all(), many=True).data
    rotations = RotationSerializer(Rotation.objects.all(), many=True).data
    rarity_icons = RarityIconSerializer(RarityIcon.objects.all(), many=True).data

    return Response({
        'supertypes': supertypes,
        'types': types,
        'subtypes': subtypes,
        'rarities': rarities,
        'variations': variations,
        'base_sets': base_sets,
        'sets': sets,
        'rotations': rotations,
        'rarity_icons': rarity_icons
    })


@permission_classes((IsAdminOrGetRequest,))
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        data['user'] = request.user.pk

        serializer = CardCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        card = serializer.validated_data

        if card['type'] not in card['supertype'].types.all():
            return Response(
                {'detail': f'The type {card["type"].name} is not allowed for {card["supertype"].name}'},
                status.HTTP_400_BAD_REQUEST
            )

        if card['supertype'].short_name == 'Pokemon':
            if not card['subtype']:
                Response({'detail': f'Subtype {card["subtype"]} could not be found'}, status.HTTP_404_NOT_FOUND)
            if card['subtype'] not in card['supertype'].subtypes.all():
                return Response(
                    {'detail': f'The subtype {card["subtype"].name} is not allowed for {card["supertype"].name}'},
                    status.HTTP_400_BAD_REQUEST
                )

            has_move = False

            for move in ['move_1', 'move_2', 'move_3']:
                if move in card and card[move]:
                    try:
                        with transaction.atomic():
                            move_serializer = MoveCreateSerializer(data=card[move])
                            move_serializer.is_valid(raise_exception=True)
                            saved_move = move_serializer.save()

                            print(card[move])

                            for energy_cost in card[move]['energy_cost']:
                                if not energy_cost['type'].is_energy:
                                    raise ValueError
                                move_energy_cost = {
                                    'move': saved_move.pk,
                                    'type': energy_cost['type'].pk,
                                    'amount': energy_cost['amount']
                                }

                                move_energy_cost_serializer = MoveEnergyCostCreateSerializer(data=move_energy_cost)
                                move_energy_cost_serializer.is_valid(raise_exception=True)
                                move_energy_cost_serializer.save()
                    except ValueError:
                        return Response(
                            {'detail': f'You can not use the type {energy_cost["type"].name} for a move cost'},
                            status.HTTP_400_BAD_REQUEST
                        )
                    has_move = True
                    card[move] = saved_move

            if card['ability']:
                ability_serializer = AbilitySerializer(data=card['ability'])
                ability_serializer.is_valid(raise_exception=True)
                ability = ability_serializer.save()
                card['ability'] = ability
            elif not has_move:
                return Response(
                    {'detail': 'A card requires at least one attack or ability'},
                    status.HTTP_400_BAD_REQUEST
                )

        else:
            card['ability'] = None
            card['move_1'] = None
            card['move_2'] = None
            card['move_3'] = None

        if card['supertype'].short_name == 'Trainer':
            if card['subtype'] and card['subtype'] not in card['type'].subtypes.all():
                return Response(
                    {'detail': f'The subtype {card["subtype"].name} is not allowed for {card["type"].name}'},
                    status.HTTP_400_BAD_REQUEST
                )

        if card['supertype'].short_name == 'Energy':
            card['subtype'] = None

        card = serializer.save()

        return Response(CardSerializer(card).data, status.HTTP_201_CREATED)

from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from card_maker_app.models import Supertype, Subtype, Type, BaseSet, Set, Rarity, Variation, Rotation, RarityIcon, Card
from card_maker_app.permissions.admin import IsAdminOrGetRequest
from card_maker_app.serializers import SubtypeSerializer, SupertypeSerializer, TypeSerializer, BaseSetSerializer, \
    SetSerializer, RaritySerializer, VariationSerializer, RotationSerializer, RarityIconSerializer, CardSerializer, \
    CardCreateSerializer, MoveCreateSerializer, MoveEnergyCostCreateSerializer


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

        card = serializer.data

        supertype = Supertype.objects.get(pk=card['supertype'])
        card_type = Type.objects.get(pk=card['type'])

        if card_type not in supertype.types.all():
            return Response(
                {'detail': f'The type {card_type.name} is not allowed for {supertype.name}'},
                status.HTTP_400_BAD_REQUEST
            )

        if supertype.short_name == 'Pokemon':
            try:
                subtype = Subtype.objects.get(pk=card['subtype'])
            except Subtype.DoesNotExist:
                return Response({'detail': f'Subtype {card["subtype"]} could not be found'}, status.HTTP_404_NOT_FOUND)
            if subtype not in supertype.subtypes.all():
                return Response(
                    {'detail': f'The subtype {subtype.name} is not allowed for {supertype.name}'},
                    status.HTTP_400_BAD_REQUEST
                )

            has_move = False

            for move in ['move_1', 'move_2', 'move_3']:
                if card[move]:
                    try:
                        with transaction.atomic():
                            move_serializer = MoveCreateSerializer(data=card[move])
                            move_serializer.is_valid(raise_exception=True)
                            move_serializer.save()

                            for energy_cost in card[move]['energy_cost']:
                                cost_type = Type.objects.get(energy_cost['type'])
                                if not cost_type.is_energy:
                                    raise ValueError
                                move_energy_cost = {
                                    'move': move_serializer.data.pk,
                                    'type': cost_type.pk,
                                    'amount': energy_cost['amount']
                                }

                                move_energy_cost_serializer = MoveEnergyCostCreateSerializer(data=move_energy_cost)
                                move_energy_cost_serializer.is_valid(raise_exception=True)
                                move_energy_cost_serializer.save()
                    except ValueError:
                        return Response({'detail': f'You can not use the type {cost_type.name} for a move cost'})
                    has_move = True

            if card['ability']:
                pass
            elif not has_move:
                return Response(
                    {'detail': 'A card requires at least one attack or ability'},
                    status.HTTP_400_BAD_REQUEST
                )

        return Response(CardSerializer(Card.objects.get(pk=card.pk)).data)

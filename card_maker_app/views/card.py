import json

from django.forms import model_to_dict
from django.http import QueryDict
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, action
from rest_framework.response import Response

from card_maker_app.models import Supertype, Subtype, Type, BaseSet, Set, Rarity, Variation, Rotation, RarityIcon, \
    Card, Move
from card_maker_app.permissions import IsAuthenticatedListCreate
from card_maker_app.permissions.card import IsAdminOrOwnerOrPublic
from card_maker_app.serializers import SubtypeSerializer, SupertypeSerializer, TypeSerializer, BaseSetSerializer, \
    SetSerializer, RaritySerializer, VariationSerializer, RotationSerializer, RarityIconSerializer, CardSerializer, \
    CardCreateSerializer, MoveCreateSerializer, AbilitySerializer, TrainerCardSerializer, SpecialEnergyCardSerializer, \
    BaseEnergyCardSerializer, CardOverviewSerializer
from card_maker_app.utils.camel_to_underscore import convert_JSON
from card_maker_app.utils.energy_cost import save_energy_cost


@permission_classes((IsAdminOrOwnerOrPublic, IsAuthenticatedListCreate))
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        cards = Card.objects.filter(user=user)
        return Response(CardOverviewSerializer(cards, many=True, context={'request': request}).data)

    def create(self, request, *args, **kwargs):
        data = request.data
        if type(data) is QueryDict:
            data = data.dict()
        data['user'] = request.user.pk

        serializer = CardCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        card = serializer.validated_data
        saved_card = None

        if card['supertype'].short_name == 'Pokemon':
            for move in ['move1', 'move2', 'move3']:
                if move in card:
                    data = convert_JSON(json.loads(card[move]))
                    move_serializer = MoveCreateSerializer(data=data)
                    move_serializer.is_valid(raise_exception=True)
                    saved_move = move_serializer.save()

                    for energy_cost in data['energy_cost']:
                        save_energy_cost(energy_cost, saved_move)
                    card[move] = saved_move

            if 'ability' in card:
                data = convert_JSON(json.loads(card['ability']))
                ability_serializer = AbilitySerializer(data=data)
                ability_serializer.is_valid(raise_exception=True)
                ability = ability_serializer.save()
                card['ability'] = ability

            saved_card = serializer.save()

        elif card['supertype'].short_name == 'Trainer':
            serializer = TrainerCardSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            saved_card = serializer.save()

        elif card['supertype'].short_name == 'Energy':
            if 'type' in card:
                serializer = SpecialEnergyCardSerializer(data=data)
            else:
                serializer = BaseEnergyCardSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            saved_card = serializer.save()

        return Response(CardSerializer(saved_card, context={'request': request}).data, status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        old_card = self.get_object()

        if old_card.published:
            return Response({'detail': 'A published card can not be updated'}, status.HTTP_403_FORBIDDEN)

        data = request.data
        if type(data) is QueryDict:
            data = data.dict()
        data['user'] = request.user.pk

        serializer = CardCreateSerializer(old_card, data=data)
        serializer.is_valid(raise_exception=True)

        card = serializer.validated_data
        saved_card = None

        if card['supertype'].short_name == 'Pokemon':
            for move in ['move1', 'move2', 'move3']:
                if move in card:
                    data = convert_JSON(json.loads(card[move]))
                    move_serializer = MoveCreateSerializer(data=data)
                    move_serializer.is_valid(raise_exception=True)
                    saved_move = move_serializer.save()

                    try:
                        Move.objects.get(pk=model_to_dict(old_card)[move]).delete()
                    except Move.DoesNotExist:
                        pass

                    for energy_cost in data['energy_cost']:
                        save_energy_cost(energy_cost, saved_move)
                    card[move] = saved_move

            if card['ability']:
                data = convert_JSON(json.loads(card['ability']))
                ability_serializer = AbilitySerializer(data=data)
                ability_serializer.is_valid(raise_exception=True)
                ability = ability_serializer.save()
                try:
                    old_card.ability.delete()
                except AttributeError:
                    # Old ability does not exist
                    pass
                card['ability'] = ability

            saved_card = serializer.save()

        elif card['supertype'].short_name == 'Trainer':
            serializer = TrainerCardSerializer(old_card, data=data)
            serializer.is_valid(raise_exception=True)
            saved_card = serializer.save()

        elif card['supertype'].short_name == 'Energy':
            if 'type' in card:
                serializer = SpecialEnergyCardSerializer(old_card, data=data)
            else:
                serializer = BaseEnergyCardSerializer(old_card, data=data)
            serializer.is_valid(raise_exception=True)
            saved_card = serializer.save()

        return Response(CardSerializer(saved_card, context={'request': request}).data, status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def options(self, request):
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

    @action(detail=False, methods=['get'])
    def published(self, request):
        cards = Card.objects.filter(public=True)
        return Response(CardOverviewSerializer(cards, many=True, context={'request': request}).data)

    @action(detail=True, methods=['get'])
    def publish(self, request, pk):
        card = self.get_object()

        if not card.public:
            card.public = True
            card.save()

        return Response("", status.HTTP_204_NO_CONTENT)

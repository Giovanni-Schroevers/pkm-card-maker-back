from collections import OrderedDict

from rest_framework import serializers

from card_maker_app.models import Card
from card_maker_app.serializers import MoveSerializer, AbilitySerializer, UserOverviewSerializer, \
    ReadOnlyMoveSerializer


def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')


class CardSerializer(serializers.ModelSerializer):
    move_1 = ReadOnlyMoveSerializer()
    move_2 = ReadOnlyMoveSerializer()
    move_3 = ReadOnlyMoveSerializer()
    user = UserOverviewSerializer()
    ability = AbilitySerializer()

    class Meta:
        model = Card
        fields = '__all__'

    def to_representation(self, instance):
        result = super(CardSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])


class CardCreateSerializer(serializers.ModelSerializer):
    move_1 = MoveSerializer(required=False, allow_null=True)
    move_2 = MoveSerializer(required=False, allow_null=True)
    move_3 = MoveSerializer(required=False, allow_null=True)
    ability = AbilitySerializer(required=False, allow_null=True)

    def validate(self, card):
        if 'type' in card:
            if card['type'] not in card['supertype'].types.all():
                raise serializers.ValidationError(
                    f'The type {card["type"].name} is not allowed for {card["supertype"].name}'
                )
        elif card['supertype'].short_name != 'Energy':
            raise serializers.ValidationError(f'Type is required for a {card["supertype"].name}')

        if 'background_image' not in card and 'card_image' not in card and 'top_image' not in card:
            raise serializers.ValidationError('A card requires at least a background, card or top image')

        if 'subtype' in card:
            if card['subtype'] not in card['supertype'].subtypes.all():
                raise serializers.ValidationError(
                    f'The subtype {card["subtype"].name} is not allowed for {card["supertype"].name}'
                )
        elif card['supertype'].short_name == 'Pokemon':
            raise serializers.ValidationError('Subtype is required for a pokemon')

        if card['supertype'].short_name == 'Pokemon':
            has_item = False
            for item in ['move_1', 'move_2', 'move_3', 'ability']:
                if item in card:
                    has_item = True
            if not has_item:
                raise serializers.ValidationError('A pokemon requires at least one attack or ability')
        return card

    class Meta:
        model = Card
        fields = '__all__'


class TrainerCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = (
            'name',
            'sub_name',
            'base_set',
            'supertype',
            'type',
            'subtype',
            'rotation',
            'rarity',
            'set',
            'description',
            'illustrator',
            'card_number',
            'total_cards',
            'rarity_icon',
            'background_image',
            'card_image',
            'custom_set_image',
            'top_image',
            'user',
            'full_card_image',
        )


class BaseEnergyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'name',
            'supertype',
            'base_set',
            'background_image',
            'card_image',
            'custom_set_image',
            'top_image',
            'type_image',
            'user',
            'full_card_image',
        )


class SpecialEnergyCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = (
            'name',
            'base_set',
            'supertype',
            'type',
            'rotation',
            'rarity',
            'set',
            'description',
            'card_number',
            'total_cards',
            'rarity_icon',
            'background_image',
            'card_image',
            'custom_set_image',
            'top_image',
            'type_image',
            'user',
            'full_card_image',
        )


class CardOverviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = (
            'id',
            'name',
            'full_card_image',
        )

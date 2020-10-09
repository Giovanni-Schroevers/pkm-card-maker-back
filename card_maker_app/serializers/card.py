from collections import OrderedDict

from rest_framework import serializers

from card_maker_app.models import Card
from card_maker_app.serializers import AbilitySerializer, UserOverviewSerializer, \
    ReadOnlyMoveSerializer, CardCommentSerializer


def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')


class CardSerializer(serializers.ModelSerializer):
    move1 = ReadOnlyMoveSerializer()
    move2 = ReadOnlyMoveSerializer()
    move3 = ReadOnlyMoveSerializer()
    user = UserOverviewSerializer()
    ability = AbilitySerializer()
    likes = serializers.IntegerField(source='likes.count')
    liked_by = UserOverviewSerializer(many=True, source='likes')
    comments = CardCommentSerializer(source='card_comments', many=True)

    class Meta:
        model = Card
        exclude = ['public']

    def to_representation(self, instance):
        result = super(CardSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])


class CardCreateSerializer(serializers.ModelSerializer):
    move1 = serializers.CharField(required=False, allow_null=True)
    move2 = serializers.CharField(required=False, allow_null=True)
    move3 = serializers.CharField(required=False, allow_null=True)
    ability = serializers.CharField(required=False, allow_null=True)

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
            for item in ['move1', 'move2', 'move3', 'ability']:
                if item in card:
                    has_item = True
            if not has_item:
                raise serializers.ValidationError('A pokemon requires at least one attack or ability')
        return card

    class Meta:
        model = Card
        exclude = ['public']


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
    likes = serializers.IntegerField(source='likes.count')
    comments = serializers.IntegerField(source='comments.count')
    user = UserOverviewSerializer()

    class Meta:
        model = Card
        fields = (
            'id',
            'name',
            'full_card_image',
            'likes',
            'comments',
            'public',
            'user',
        )

from rest_framework import serializers

from card_maker_app.models import Card
from card_maker_app.serializers import UserSerializer, MoveSerializer


class CardSerializer(serializers.ModelSerializer):
    move_1 = MoveSerializer()
    move_2 = MoveSerializer()
    move_3 = MoveSerializer()
    user = UserSerializer()

    class Meta:
        model = Card
        fields = (
            'id',
            'sub_name',
            'hit_points',
            'card_number',
            'total_cards',
            'illustrator',
            'weakness_amount',
            'weakness_type',
            'weakness_type',
            'resistance_amount',
            'resistance_type',
            'retreat_cost',
            'pokedex_entry',
            'description',
            'prevolve_name',
            'background_image',
            'card_image',
            'top_image',
            'type_image',
            'prevolve_image',
            'supertype',
            'type',
            'subtype',
            'rarity',
            'variation',
            'rotation',
            'rarity_icon',
            'set',
            'base_set',
            'move_1',
            'move_2',
            'move_3',
            'user'
        )

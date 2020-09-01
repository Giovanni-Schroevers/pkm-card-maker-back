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
    ability = AbilitySerializer()

    class Meta:
        model = Card
        fields = '__all__'

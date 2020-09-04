from rest_framework import serializers

from card_maker_app.models import Ability


class AbilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Ability
        fields = (
            'name',
            'text',
        )

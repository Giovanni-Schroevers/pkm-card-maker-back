from rest_framework import serializers

from card_maker_app.models import Set


class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = (
            'id',
            'short_name',
            'name',
            'number',
        )

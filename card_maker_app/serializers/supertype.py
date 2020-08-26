from rest_framework import serializers

from card_maker_app.models import Supertype


class SupertypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supertype
        fields = (
            'id',
            'short_name',
            'name',
        )

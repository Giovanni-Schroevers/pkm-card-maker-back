from rest_framework import serializers

from card_maker_app.models import BaseSet


class BaseSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseSet
        fields = (
            'id',
            'short_name',
            'name',
            'sets'
        )

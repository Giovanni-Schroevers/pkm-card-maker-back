from rest_framework import serializers

from card_maker_app.models import Rotation


class RotationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rotation
        fields = (
            'id',
            'short_name',
            'name',
        )

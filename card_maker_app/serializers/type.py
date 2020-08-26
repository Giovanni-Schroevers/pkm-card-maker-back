from rest_framework import serializers

from card_maker_app.models import Type


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = (
            'id',
            'short_name',
            'name',
            'subtype_required',
            'has_white_text',
            'has_sub_name',
            'has_special_style',
            'is_energy',
            'rarities'
        )

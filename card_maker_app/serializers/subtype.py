from rest_framework import serializers

from card_maker_app.models import Subtype


class SubtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtype
        fields = (
            'id',
            'short_name',
            'name',
            'has_prevolve',
            'has_pokedex_entry',
            'has_description',
            'has_white_top_text',
            'has_v_style',
            'has_v_symbol',
            'has_name_outline',
            'has_vmax_symbol',
            'rarities',
            'variations',
            'types',
            'supertypes',
        )

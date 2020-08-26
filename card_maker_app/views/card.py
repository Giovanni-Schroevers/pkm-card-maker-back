from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from card_maker_app.models import Supertype, Subtype, Type, BaseSet, Set, Rarity, Variation, Rotation, RarityIcon
from card_maker_app.serializers import SubtypeSerializer, SupertypeSerializer, TypeSerializer, BaseSetSerializer, \
    SetSerializer, RaritySerializer, VariationSerializer, RotationSerializer, RarityIconSerializer


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_card_options(request):

    supertypes = SupertypeSerializer(Supertype.objects.all(), many=True).data
    types = TypeSerializer(Type.objects.all(), many=True).data
    subtypes = SubtypeSerializer(Subtype.objects.all(), many=True).data
    rarities = RaritySerializer(Rarity.objects.all(), many=True).data
    variations = VariationSerializer(Variation.objects.all(), many=True).data
    base_sets = BaseSetSerializer(BaseSet.objects.all(), many=True).data
    sets = SetSerializer(Set.objects.all(), many=True).data
    rotations = RotationSerializer(Rotation.objects.all(), many=True).data
    rarity_icons = RarityIconSerializer(RarityIcon.objects.all(), many=True).data

    return Response({
        'supertypes': supertypes,
        'types': types,
        'subtypes': subtypes,
        'rarities': rarities,
        'variations': variations,
        'base_sets': base_sets,
        'sets': sets,
        'rotations': rotations,
        'rarity_icons': rarity_icons
    })

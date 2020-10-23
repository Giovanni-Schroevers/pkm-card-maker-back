from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

from card_maker_app.models import Appeal
from card_maker_app.serializers import AppealSerializer


@permission_classes((IsAdminUser,))
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

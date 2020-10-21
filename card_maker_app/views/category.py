from rest_framework import viewsets
from rest_framework.decorators import permission_classes

from card_maker_app.models import Category
from card_maker_app.permissions.category import IsAuthenticatedCategory
from card_maker_app.serializers import CategorySerializer


@permission_classes((IsAuthenticatedCategory,))
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

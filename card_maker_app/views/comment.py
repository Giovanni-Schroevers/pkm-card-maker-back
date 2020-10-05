from rest_framework import viewsets
from rest_framework.decorators import action

from card_maker_app.models import CardComment
from card_maker_app.serializers import CardCommentSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = CardComment.objects.all()
    serializer_class = CardCommentSerializer()

    @action(detail=True, methods=['get'])
    def like(self, request, pk):



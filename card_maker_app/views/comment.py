from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response

from card_maker_app.models import CardComment
from card_maker_app.permissions import IsAuthenticatedComment
from card_maker_app.serializers import CardCommentSerializer
from card_maker_app.utils.report import create_report


@permission_classes((IsAuthenticatedComment,))
class CardCommentViewSet(viewsets.ModelViewSet):
    queryset = CardComment.objects.all()
    serializer_class = CardCommentSerializer

    @action(detail=True, methods=['get'])
    def like(self, request, pk):
        comment = self.get_object()
        user = request.user

        if comment in user.card_likes.all():
            user.comment_like.remove(comment)
        else:
            user.comment_like.add(comment)

        return Response("", status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def report(self, request, pk):
        user = request.user
        parent = self.get_object()
        data = request.data
        data['user'] = user.pk

        return create_report(parent, data)

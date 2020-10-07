from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response

from card_maker_app.models import CardComment
from card_maker_app.permissions import IsAuthenticatedComment
from card_maker_app.serializers import CardCommentSerializer


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

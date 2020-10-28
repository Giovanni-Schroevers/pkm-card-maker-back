from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from card_maker_app.models import Appeal
from card_maker_app.serializers import AppealSerializer


@permission_classes((IsAdminUser,))
class AppealViewSet(viewsets.ModelViewSet):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

    @action(detail=True, methods=['get'])
    def approve(self, request, pk):
        appeal = self.get_object()

        appeal.status = 'approved'
        appeal.ban.delete()
        appeal.ban = None
        appeal.admin = request.user
        appeal.save()

        return Response('', status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def decline(self, request, pk):
        appeal = self.get_object()

        appeal.status = 'rejected'
        appeal.admin = request.user
        appeal.save()

        return Response('', status.HTTP_204_NO_CONTENT)

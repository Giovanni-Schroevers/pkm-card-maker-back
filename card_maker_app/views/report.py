from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from card_maker_app.models import Report
from card_maker_app.permissions import ReportIsAdmin
from card_maker_app.serializers import ReportSerializer


@permission_classes((ReportIsAdmin, IsAuthenticated))
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    @action(detail=False, methods=['get'])
    def categories(self, request):
        return Response(Report.categories)

    @action(detail=False, methods=['get'])
    def archived(self, request):
        reports = Report.objects.deleted_only()

        return Response(ReportSerializer(reports, many=True).data)

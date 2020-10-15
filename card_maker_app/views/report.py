from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from card_maker_app.models import Report
from card_maker_app.serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    @action(detail=False, methods=['get'])
    def categories(self, request):
        return Response(Report.categories)

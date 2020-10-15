from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.response import Response

from card_maker_app.serializers import ReportCreateSerializer


def create_report(item, data):
    serializer = ReportCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save(
        parent_content_type=ContentType.objects.get_for_model(item),
        parent_object_id=item.pk
    )
    return Response(serializer.data, status.HTTP_201_CREATED)

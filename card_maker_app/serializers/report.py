from rest_framework import serializers

from card_maker_app.models import Report
from card_maker_app.serializers import UserOverviewSerializer, CategorySerializer


class ReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            'id',
            'user',
            'description',
            'created_at',
            'category',
        )


class ReportSerializer(serializers.ModelSerializer):
    user = UserOverviewSerializer(read_only=True)
    model = serializers.CharField(source='parent_content_type.model')
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Report
        fields = (
            'id',
            'user',
            'description',
            'created_at',
            'category',
            'model'
        )

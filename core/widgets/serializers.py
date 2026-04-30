# core/widgets/serializers.py

from rest_framework import serializers
from core.widgets.models import UIWidget


class WidgetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UIWidget
        fields = [
            "id",
            "type",
            "position",
            "title",
            "config",
            "order",
        ]


class WidgetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UIWidget
        fields = "__all__"


class WidgetCreateSerializer(serializers.Serializer):
    type = serializers.CharField()
    position = serializers.CharField()
    title = serializers.CharField(required=False, allow_blank=True)
    config = serializers.JSONField(required=False)
    starts_at = serializers.DateTimeField(required=False)
    ends_at = serializers.DateTimeField(required=False)
    target_roles = serializers.JSONField(required=False)
    target_permissions = serializers.JSONField(required=False)
    order = serializers.IntegerField(required=False)
    is_active = serializers.BooleanField(required=False)


class WidgetUpdateSerializer(WidgetCreateSerializer):
    pass

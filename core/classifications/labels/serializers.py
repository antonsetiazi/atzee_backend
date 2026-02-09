# core/classifications/labels/serializers.py

from rest_framework import serializers
from core.classifications.labels.models import Label


class LabelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ["id", "code", "name", "scope"]


class LabelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"


class LabelCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False, allow_blank=True)
    scope = serializers.CharField(max_length=50)


class LabelUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False, allow_blank=True)
    scope = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)

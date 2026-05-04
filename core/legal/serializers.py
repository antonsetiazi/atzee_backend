# core/legal/serializers.py

from rest_framework import serializers
from core.legal.models import PolicyDocument


class PolicyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyDocument
        fields = [
            "id",
            "code",
            "title",
            "policy_type",
            "version",
        ]


class PolicyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyDocument
        fields = [
            "id",
            "code",
            "title",
            "policy_type",
            "content",
            "version",
            "created_at",
            "updated_at",
        ]


class PolicyCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=255)
    policy_type = serializers.CharField(max_length=50)
    content = serializers.CharField()


class PolicyUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)


class PolicyAcceptSerializer(serializers.Serializer):
    policy_id = serializers.IntegerField()
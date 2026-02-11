# core/classifications/tags/serializers.py

from rest_framework import serializers
from core.classifications.tags.models import Tag


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "code", "name"]


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "code",
            "name",
            "description",
            "is_active",
            "created_at",
            "updated_at",
        ]


class TagCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50, required=False)
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Tag
        fields = ["code", "name", "description"]

    def validate(self, attrs):
        if "code" not in attrs:
            # otomatis generate kode dari name, misal lowercase + replace spasi
            name = attrs.get("name", "")
            attrs["code"] = name.lower().replace(" ", "_")
        return attrs


class TagUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)

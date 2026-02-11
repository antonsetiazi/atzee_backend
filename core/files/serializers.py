# core/files/serializers.py

from rest_framework import serializers
from core.files.models import File


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            "id",
            "original_name",
            "mime_type",
            "size",
            "is_public",
            "created_at",
        ]


class FileDetailSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = "__all__"

    def get_file_url(self, obj: File) -> str:
        request = self.context.get("request")
        if obj.is_public and request:
            return request.build_absolute_uri(obj.file.url)
        return ""


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    related_entity = serializers.CharField(max_length=100)
    related_id = serializers.CharField()
    is_public = serializers.BooleanField(required=False, default=False)

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
        if request:
            if obj.is_public:
                # Gunakan storage service untuk resolve public URL
                from core.files.storage import FileStorageService
                return request.build_absolute_uri(
                    FileStorageService.get_url(path=obj.file.name)
                )
            else:
                # Private file → pakai endpoint download
                return request.build_absolute_uri(f"/api/files/{obj.id}/download/")
        return ""


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    related_entity = serializers.CharField(max_length=100)
    related_id = serializers.CharField()
    is_public = serializers.BooleanField(required=False, default=False)

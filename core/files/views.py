# core/files/views.py

from django.http import FileResponse
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action

from core.tenants.services import TenantService
from core.files import selectors, services
from core.files.serializers import (
    FileListSerializer,
    FileDetailSerializer,
    FileUploadSerializer,
)


class FileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "download":
            return [AllowAny()]
        return [IsAuthenticated()]

    def list(self, request):
        """
        List files by related entity.
        Query params:
        - related_entity
        - related_id
        """
        tenant = TenantService.get_current_tenant(request)

        related_entity = request.query_params.get("related_entity")
        related_id = request.query_params.get("related_id")

        if not related_entity or not related_id:
            raise ValidationError(
                "related_entity and related_id are required."
            )

        qs = selectors.get_files_by_relation(
            tenant=tenant,
            related_entity=related_entity,
            related_id=related_id,
        )

        return Response(
            FileListSerializer(qs, many=True).data
        )

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        obj = selectors.get_file_by_id(
            tenant=tenant,
            file_id=pk,
        )

        if not obj:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            FileDetailSerializer(
                obj,
                context={"request": request}
            ).data
        )

    def create(self, request):
        """
        Upload file.
        """
        tenant = TenantService.get_current_tenant(request)

        serializer = FileUploadSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        obj = services.upload_file(
            tenant=tenant,
            uploaded_by=request.user,
            **serializer.validated_data,
        )

        services.bind_file_to_entity(
            file=obj,
            entity_type=serializer.validated_data.get("related_entity"),
            entity_id=serializer.validated_data.get("related_id"),
            user=request.user,
        )

        return Response(
            FileDetailSerializer(
                obj,
                context={"request": request}
            ).data,
            status=status.HTTP_201_CREATED,
        )

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_file(
            tenant=tenant,
            file_id=pk,
            deleted_by=request.user,
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

    @action(detail=True, methods=["get"], url_path="download")
    def download(self, request, pk=None):
        """
        Download endpoint (public + private aware).
        """

        # 🔥 Jangan ambil tenant dari request
        obj = selectors.get_file_by_id_no_tenant(file_id=pk)

        if not obj:
            return Response(status=404)

        # 🔐 Jika file private → wajib authenticated
        if not obj.is_public and not request.user.is_authenticated:
            return Response(status=403)

        response = FileResponse(
            obj.file.open("rb"),
            as_attachment=False,
        )

        response["Content-Type"] = obj.mime_type
        return response


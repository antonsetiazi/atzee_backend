# core/classifications/labels/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.classifications.labels import selectors, services
from core.classifications.labels.serializers import (
    LabelListSerializer,
    LabelDetailSerializer,
    LabelCreateSerializer,
    LabelUpdateSerializer,
)


class LabelViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        scope = request.query_params.get("scope")
        qs = selectors.get_labels(tenant=tenant, scope=scope)
        return Response(LabelListSerializer(qs, many=True).data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        obj = selectors.get_label_by_id(tenant=tenant, label_id=pk)
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(LabelDetailSerializer(obj).data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = LabelCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = services.create_label(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data,
        )
        return Response(LabelDetailSerializer(obj).data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        serializer = LabelUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        obj = services.update_label(
            tenant=tenant,
            label_id=pk,
            updated_by=request.user,
            **serializer.validated_data,
        )
        return Response(LabelDetailSerializer(obj).data)

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        services.delete_label(
            tenant=tenant,
            label_id=pk,
            deleted_by=request.user,
        )
        return Response(status=status.HTTP_204_NO_CONTENT)

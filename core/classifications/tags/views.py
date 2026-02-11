# core/classifications/tags/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.classifications.tags import selectors, services
from core.classifications.tags.serializers import (
    TagListSerializer,
    TagDetailSerializer,
    TagCreateSerializer,
    TagUpdateSerializer,
)


class TagViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        qs = selectors.get_tags(tenant=tenant)
        
        search = request.query_params.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        return Response(TagListSerializer(qs, many=True).data)


    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        obj = selectors.get_tag_by_id(tenant=tenant, tag_id=pk)
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(TagDetailSerializer(obj).data)


    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = TagCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = services.create_tag(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data,
        )

        return Response(TagDetailSerializer(obj).data, status=status.HTTP_201_CREATED)
    

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        serializer = TagUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        obj = services.update_tag(
            tenant=tenant,
            tag_id=pk,
            updated_by=request.user,
            **serializer.validated_data,
        )

        return Response(TagDetailSerializer(obj).data)


    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        services.delete_tag(
            tenant=tenant,
            tag_id=pk,
            deleted_by=request.user,
        )
        return Response(status=status.HTTP_204_NO_CONTENT)

# core/classifications/categories/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.classifications.categories import selectors, services
from core.classifications.categories.serializers import (
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategoryCreateSerializer,
    CategoryUpdateSerializer,
)


class CategoryViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)

        scope = request.query_params.get("scope")
        parent_id = request.query_params.get("parent")

        qs = selectors.get_categories(
            tenant=tenant,
            scope=scope,
            parent_id=parent_id,
        )

        return Response(CategoryListSerializer(qs, many=True).data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        obj = selectors.get_category_by_id(
            tenant=tenant,
            category_id=pk,
        )

        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(CategoryDetailSerializer(obj).data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)

        serializer = CategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = services.create_category(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            CategoryDetailSerializer(obj).data,
            status=status.HTTP_201_CREATED,
        )

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = CategoryUpdateSerializer(
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        obj = services.update_category(
            tenant=tenant,
            category_id=pk,
            updated_by=request.user,
            **serializer.validated_data,
        )

        return Response(CategoryDetailSerializer(obj).data)

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_category(
            tenant=tenant,
            category_id=pk,
            deleted_by=request.user,
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

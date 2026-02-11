# core/classifications/attributes/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.classifications.attributes import selectors, services
from core.classifications.attributes.serializers import (
    AttributeListSerializer,
    AttributeDetailSerializer,
    AttributeCreateSerializer,
    AttributeUpdateSerializer,
    AttributeOptionSerializer,
    AttributeOptionCreateSerializer,
    AttributeOptionUpdateSerializer
)


class AttributeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        scope = request.query_params.get("scope")

        qs = selectors.get_attributes(
            tenant=tenant,
            scope=scope,
        )

        return Response(AttributeListSerializer(qs, many=True).data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        obj = selectors.get_attribute_by_id(
            tenant=tenant,
            attribute_id=pk,
        )

        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(AttributeDetailSerializer(obj).data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)

        serializer = AttributeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = services.create_attribute(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            AttributeDetailSerializer(obj).data,
            status=status.HTTP_201_CREATED,
        )

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = AttributeUpdateSerializer(
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        obj = services.update_attribute(
            tenant=tenant,
            attribute_id=pk,
            updated_by=request.user,
            **serializer.validated_data,
        )

        return Response(AttributeDetailSerializer(obj).data)

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_attribute(
            tenant=tenant,
            attribute_id=pk,
            deleted_by=request.user,
        )

        return Response(status=status.HTTP_204_NO_CONTENT)


class AttributeOptionViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request, attribute_id=None):
        tenant = TenantService.get_current_tenant(request)

        attribute = selectors.get_attribute_by_id(
            tenant=tenant,
            attribute_id=attribute_id,
        )
        if not attribute:
            return Response(status=status.HTTP_404_NOT_FOUND)

        qs = selectors.get_attribute_options(
            tenant=tenant,
            attribute=attribute,
        )

        return Response(AttributeOptionSerializer(qs, many=True).data)


    def retrieve(self, request, attribute_id=None, pk=None):
        tenant = TenantService.get_current_tenant(request)
        print("attribute_id: ", attribute_id)
        attribute = selectors.get_attribute_by_id(
            tenant=tenant,
            attribute_id=attribute_id,
        )
        if not attribute:
            return Response(status=status.HTTP_404_NOT_FOUND)

        obj = selectors.get_attribute_option_by_id(
            tenant=tenant,
            attribute=attribute,
            option_id=pk,
        )
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(AttributeOptionSerializer(obj).data)


    def create(self, request, attribute_id=None):
        tenant = TenantService.get_current_tenant(request)

        attribute = selectors.get_attribute_by_id(
            tenant=tenant,
            attribute_id=attribute_id,
        )
        if not attribute:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AttributeOptionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = services.create_attribute_option(
            tenant=tenant,
            attribute=attribute,
            created_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            AttributeOptionSerializer(obj).data,
            status=status.HTTP_201_CREATED,
        )

    def partial_update(self, request, attribute_id=None, pk=None):
        tenant = TenantService.get_current_tenant(request)

        attribute = selectors.get_attribute_by_id(
            tenant=tenant,
            attribute_id=attribute_id,
        )
        if not attribute:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AttributeOptionUpdateSerializer(
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        obj = services.update_attribute_option(
            tenant=tenant,
            attribute=attribute,
            option_id=pk,
            updated_by=request.user,
            **serializer.validated_data,
        )

        return Response(AttributeOptionSerializer(obj).data)

    def destroy(self, request, attribute_id=None, pk=None):
        tenant = TenantService.get_current_tenant(request)

        attribute = selectors.get_attribute_by_id(
            tenant=tenant,
            attribute_id=attribute_id,
        )
        if not attribute:
            return Response(status=status.HTTP_404_NOT_FOUND)

        services.delete_attribute_option(
            tenant=tenant,
            attribute=attribute,
            option_id=pk,
            deleted_by=request.user,
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

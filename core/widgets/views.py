# core/widgets/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from core.widgets import selectors, services
from core.widgets.serializers import (
    WidgetListSerializer,
    WidgetDetailSerializer,
    WidgetCreateSerializer,
    WidgetUpdateSerializer
)


class WidgetViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        position = request.query_params.get("position")

        widgets = selectors.get_active_widgets_for_user(
            tenant=tenant,
            user=request.user,
            position=position,
        )

        serializer = WidgetListSerializer(widgets, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        # print('retrieve')
        tenant = TenantService.get_current_tenant(request)
        widget = selectors.get_widget_by_id(tenant=tenant, widget_id=pk)

        if not widget:
            return Response(
                {"detail": "Widget not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = WidgetDetailSerializer(widget)
        return Response(serializer.data)
    

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = WidgetCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        widget = services.create_widget(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )

        return Response(
            WidgetDetailSerializer(widget).data,
            status=status.HTTP_201_CREATED
        )


    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        serializer = WidgetUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        widget = services.update_widget(
            tenant=tenant,
            widget_id=pk,
            updated_by=request.user,
            **serializer.validated_data
        )

        return Response(
            WidgetDetailSerializer(widget).data
        )


    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        serializer = WidgetUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        widget = services.update_widget(
            tenant=tenant,
            widget_id=pk,
            updated_by=request.user,
            **serializer.validated_data
        )

        return Response(
            WidgetDetailSerializer(widget).data
        )
    

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_widget(
            tenant=tenant,
            widget_id=pk,
            deleted_by=request.user
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

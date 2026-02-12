# core/schedule/views/recurring_views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from core.schedule.recurring import selectors, services, serializers


class RecurringRuleViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        rules = selectors.get_recurring_rule_queryset(tenant=tenant)
        serializer = serializers(rules, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        rule = selectors.get_recurring_rule_by_id(tenant=tenant, rule_id=pk)
        if not rule:
            return Response({"detail": "Recurring rule not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers(rule)
        return Response(serializer.data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = serializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        rule = services.create_recurring_rule(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )
        output = serializers(rule)
        return Response(output.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        rule = selectors.get_recurring_rule_by_id(tenant=tenant, rule_id=pk)
        if not rule:
            return Response({"detail": "Recurring rule not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        rule = services.update_recurring_rule(
            tenant=tenant,
            rule_id=rule.id,
            updated_by=request.user,
            **serializer.validated_data
        )
        output = serializers(rule)
        return Response(output.data)

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        services.delete_recurring_rule(tenant=tenant, rule_id=pk, deleted_by=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

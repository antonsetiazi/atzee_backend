# core/legal/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.legal import selectors, services
from core.legal.serializers import (
    PolicyListSerializer,
    PolicyDetailSerializer,
    PolicyCreateSerializer,
    PolicyUpdateSerializer,
    PolicyAcceptSerializer,
)


class PolicyViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)

        policy_type = request.query_params.get("type")

        qs = selectors.get_policies(
            tenant=tenant,
            policy_type=policy_type,
        )

        return Response(PolicyListSerializer(qs, many=True).data)

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        obj = selectors.get_policy_by_id(
            tenant=tenant,
            policy_id=pk,
        )

        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(PolicyDetailSerializer(obj).data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)

        serializer = PolicyCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = services.create_policy(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data,
        )

        return Response(
            PolicyDetailSerializer(obj).data,
            status=status.HTTP_201_CREATED,
        )

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        serializer = PolicyUpdateSerializer(
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        obj = services.update_policy(
            tenant=tenant,
            policy_id=pk,
            updated_by=request.user,
            **serializer.validated_data,
        )

        return Response(PolicyDetailSerializer(obj).data)

    @action(detail=False, methods=["post"])
    def accept(self, request):
        tenant = TenantService.get_current_tenant(request)

        serializer = PolicyAcceptSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = services.accept_policy(
            tenant=tenant,
            user=request.user,
            policy_id=serializer.validated_data["policy_id"],
            ip_address=request.META.get("REMOTE_ADDR"),
        )

        return Response(
            {"status": "accepted"},
            status=status.HTTP_200_OK,
        )
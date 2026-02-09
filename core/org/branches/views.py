# core/org/branches/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.org.branches import selectors, services
from core.org.branches.serializers import (
    BranchListSerializer,
    BranchDetailSerializer,
    BranchCreateSerializer,
    BranchUpdateSerializer,
)


class BranchViewSet(viewsets.ViewSet):
    """
    Organization Branch management (CORE).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        branches = selectors.get_branches(tenant=tenant)
        return Response(
            BranchListSerializer(branches, many=True).data
        )

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        branch = selectors.get_branch_by_id(
            tenant=tenant,
            branch_id=pk
        )

        if not branch:
            return Response(
                {"detail": "Branch not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            BranchDetailSerializer(branch).data
        )

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = BranchCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        branch = services.create_branch(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )

        return Response(
            BranchDetailSerializer(branch).data,
            status=status.HTTP_201_CREATED
        )

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        serializer = BranchUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        branch = services.update_branch(
            tenant=tenant,
            branch_id=pk,
            updated_by=request.user,
            **serializer.validated_data
        )

        return Response(
            BranchDetailSerializer(branch).data
        )

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_branch(
            tenant=tenant,
            branch_id=pk,
            deleted_by=request.user
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

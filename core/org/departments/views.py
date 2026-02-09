# core/org/departments/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tenants.services import TenantService
from core.org.departments import selectors, services
from core.org.departments.serializers import (
    DepartmentListSerializer,
    DepartmentDetailSerializer,
    DepartmentCreateSerializer,
    DepartmentUpdateSerializer,
)


class DepartmentViewSet(viewsets.ViewSet):
    """
    Organization Department management (CORE).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        departments = selectors.get_departments(tenant=tenant)
        return Response(
            DepartmentListSerializer(departments, many=True).data
        )

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        dept = selectors.get_department_by_id(
            tenant=tenant,
            department_id=pk
        )

        if not dept:
            return Response(
                {"detail": "Department not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            DepartmentDetailSerializer(dept).data
        )

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = DepartmentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dept = services.create_department(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )

        return Response(
            DepartmentDetailSerializer(dept).data,
            status=status.HTTP_201_CREATED
        )

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        serializer = DepartmentUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        dept = services.update_department(
            tenant=tenant,
            department_id=pk,
            updated_by=request.user,
            **serializer.validated_data
        )

        return Response(
            DepartmentDetailSerializer(dept).data
        )

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_department(
            tenant=tenant,
            department_id=pk,
            deleted_by=request.user
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

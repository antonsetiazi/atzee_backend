# hr/employees/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from hr.employees import selectors, services
from hr.employees.serializers import (
    EmployeeListSerializer,
    EmployeeDetailSerializer,
    EmployeeCreateSerializer,
    EmployeeUpdateSerializer
)


class EmployeeViewSet(viewsets.ViewSet):
    """
    Employee API endpoints (tenant scoped).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        employees = selectors.get_employees(tenant=tenant)
        serializer = EmployeeListSerializer(employees, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        employee = selectors.get_employee_by_id(tenant=tenant, employee_id=pk)

        if not employee:
            return Response(
                {"detail": "Employee not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = EmployeeDetailSerializer(employee)
        return Response(serializer.data)
    

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = EmployeeCreateSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)

        employee = services.create_employee(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )
        
        output = EmployeeDetailSerializer(employee)

        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )
    

    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        employee = selectors.get_employee_by_id(tenant=tenant, employee_id=pk)

        if not employee:
            return Response(
                {"detail": "Employee not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = EmployeeUpdateSerializer(data=request.data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)

        employee = services.update_employee(
            tenant=tenant,
            employee_id=employee.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = EmployeeDetailSerializer(employee)
        return Response(output.data)
    

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        employee = selectors.get_employee_by_id(tenant=tenant, employee_id=pk)

        if not employee:
            return Response(
                {"detail": "Employee not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = EmployeeUpdateSerializer(data=request.data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)

        employee = services.update_employee(
            tenant=tenant,
            employee_id=employee.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = EmployeeDetailSerializer(employee)
        return Response(output.data)
    

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_employee(
            tenant=tenant,
            employee_id=pk,
            deleted_by=request.user
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

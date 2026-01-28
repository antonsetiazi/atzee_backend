from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from hr.employees import selectors
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
        employees = selectors.get_employees(
            tenant=request.tenant
        )
        serializer = EmployeeListSerializer(
            employees, many=True
        )
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        employee = selectors.get_employee_by_id(
            tenant=request.tenant,
            employee_id=pk
        )

        if not employee:
            return Response(
                {"detail": "Employee not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = EmployeeDetailSerializer(employee)
        return Response(serializer.data)
    

    def create(self, request):
        serializer = EmployeeCreateSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        employee = serializer.save()
        output = EmployeeDetailSerializer(employee)

        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )
    

    def update(self, request, pk=None):
        employee = selectors.get_employee_by_id(
            tenant=request.tenant,
            employee_id=pk
        )

        if not employee:
            return Response(
                {"detail": "Employee not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = EmployeeUpdateSerializer(
            instance=employee,
            data=request.data,
            partial=True,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        employee = serializer.save()
        output = EmployeeDetailSerializer(employee)

        return Response(output.data)
    

    def destroy(self, request, pk=None):
        from hr.employees.services import delete_employee

        delete_employee(
            tenant=request.tenant,
            employee_id=pk,
            deleted_by=request.user
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

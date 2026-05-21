# hrms/api/employee/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# from hrms.models import Employee
from hrms.selectors import (
    get_active_employees,
)
from hrms.services import (
    onboard_employee,
)

from .serializers import EmployeeSerializer


class EmployeeListApi(APIView):

    def get(self, request):
        employees = get_active_employees(
            tenant=request.user.tenant,
        )

        serializer = EmployeeSerializer(
            employees,
            many=True,
        )

        return Response(serializer.data)


class EmployeeOnboardApi(APIView):

    def post(self, request):

        employee = onboard_employee(
            tenant=request.user.tenant,
            employee_id=request.data.get("employee_id"),
            full_name=request.data.get("full_name"),
            email=request.data.get("email"),
            created_by=request.user,
        )

        serializer = EmployeeSerializer(employee)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

# hrms/api/payroll/views.py

from rest_framework.response import Response
from rest_framework.views import APIView

from hrms.models import (
    Employee,
    Payroll,
)
from hrms.selectors import (
    get_processed_payrolls,
)
from hrms.services.payroll import (
    approve_payroll,
    generate_payroll,
)

from .serializers import PayrollSerializer


class PayrollListApi(APIView):

    def get(self, request):

        payrolls = get_processed_payrolls(
            tenant=request.user.tenant,
        )

        serializer = PayrollSerializer(
            payrolls,
            many=True,
        )

        return Response(serializer.data)


class GeneratePayrollApi(APIView):

    def post(self, request):

        employee = Employee.objects.get(pk=request.data.get("employee_id"))

        payroll = generate_payroll(
            tenant=request.user.tenant,
            employee=employee,
            payroll_period=request.data.get("payroll_period"),
            created_by=request.user,
        )

        serializer = PayrollSerializer(payroll)

        return Response(serializer.data)


class ApprovePayrollApi(APIView):

    def post(self, request, pk):

        payroll = Payroll.objects.get(pk=pk)

        payroll = approve_payroll(
            payroll=payroll,
            approved_by=request.user,
        )

        serializer = PayrollSerializer(payroll)

        return Response(serializer.data)

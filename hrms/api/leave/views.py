# hrms/api/leave/views.py

from rest_framework.response import Response
from rest_framework.views import APIView

from hrms.models import (
    Employee,
    LeaveRequest,
)
from hrms.selectors import (
    get_pending_leave_requests,
)
from hrms.services import (
    apply_leave,
    approve_leave,
)

from .serializers import (
    LeaveRequestSerializer,
)


class PendingLeaveApi(APIView):

    def get(self, request):

        leaves = get_pending_leave_requests(
            tenant=request.user.tenant,
        )

        serializer = LeaveRequestSerializer(
            leaves,
            many=True,
        )

        return Response(serializer.data)


class ApplyLeaveApi(APIView):

    def post(self, request):

        employee = Employee.objects.get(pk=request.data.get("employee_id"))

        leave = apply_leave(
            tenant=request.user.tenant,
            employee=employee,
            leave_type=request.data.get("leave_type"),
            start_date=request.data.get("start_date"),
            end_date=request.data.get("end_date"),
            reason=request.data.get("reason"),
            created_by=request.user,
        )

        serializer = LeaveRequestSerializer(leave)

        return Response(serializer.data)


class ApproveLeaveApi(APIView):

    def post(self, request, pk):

        leave_request = LeaveRequest.objects.get(pk=pk)

        employee = Employee.objects.get(user=request.user)

        leave_request = approve_leave(
            leave_request=leave_request,
            approved_by=employee,
        )

        serializer = LeaveRequestSerializer(leave_request)

        return Response(serializer.data)

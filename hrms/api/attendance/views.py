# hrms/api/attendance/views.py

from datetime import date

from rest_framework.response import Response
from rest_framework.views import APIView

from hrms.models import Employee
from hrms.selectors import (
    get_today_attendance,
)
from hrms.services import (
    check_in,
    check_out,
)

from .serializers import (
    AttendanceSerializer,
)


class TodayAttendanceApi(APIView):

    def get(self, request):

        attendance = get_today_attendance(
            tenant=request.user.tenant,
            attendance_date=date.today(),
        )

        serializer = AttendanceSerializer(
            attendance,
            many=True,
        )

        return Response(serializer.data)


class CheckInApi(APIView):

    def post(self, request):

        employee = Employee.objects.get(pk=request.data.get("employee_id"))

        attendance = check_in(
            tenant=request.user.tenant,
            employee=employee,
            attendance_date=date.today(),
            created_by=request.user,
        )

        serializer = AttendanceSerializer(attendance)

        return Response(serializer.data)


class CheckOutApi(APIView):

    def post(self, request):

        employee = Employee.objects.get(pk=request.data.get("employee_id"))

        attendance = employee.attendances.filter(
            attendance_date=date.today()
        ).first()

        attendance = check_out(
            attendance=attendance,
            updated_by=request.user,
        )

        serializer = AttendanceSerializer(attendance)

        return Response(serializer.data)

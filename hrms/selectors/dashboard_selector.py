# hrms/selectors/dashboard_selector.py

from hrms.enums import (
    EmployeeStatus,
    LeaveStatus,
)
from hrms.models import (
    Attendance,
    Employee,
    LeaveRequest,
)


def get_hrms_dashboard_summary(
    tenant,
):
    return {
        "total_employees": Employee.objects.filter(
            tenant=tenant,
            employment_status=EmployeeStatus.ACTIVE,
            is_deleted=False,
        ).count(),
        "pending_leave_requests": LeaveRequest.objects.filter(
            tenant=tenant,
            status=LeaveStatus.PENDING,
            is_deleted=False,
        ).count(),
        "today_attendance_count": Attendance.objects.filter(
            tenant=tenant,
            is_deleted=False,
        ).count(),
    }

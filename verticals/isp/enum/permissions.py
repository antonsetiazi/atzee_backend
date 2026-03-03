# verticals/isp/enum/permissions.py

from enum import Enum

class IspPermission(str, Enum):

    # ORGANIZATION_VIEW = "isp.organization.view"
    # ORGANIZATION_MANAGE = "isp.organization.manage"

    # MY_PROFILE_VIEW = "isp.my.profile.view"
    # MY_ATTENDANCE_VIEW = "isp.my.attendance.view"
    # MY_LEAVE_REQUEST = "isp.my.leave.request"
    # MY_PAYROLL_VIEW = "isp.my.payroll.view"
    # MY_PERFORMANCE_VIEW = "isp.my.performance.view"


    def __str__(self):
        return self.value
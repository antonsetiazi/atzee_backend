# verticals/bengkel/enum/permissions.py

from enum import Enum

class BengkelPermission(str, Enum):

    # ORGANIZATION_VIEW = "bengkel.organization.view"
    # ORGANIZATION_MANAGE = "bengkel.organization.manage"

    # MY_PROFILE_VIEW = "bengkel.my.profile.view"
    # MY_ATTENDANCE_VIEW = "bengkel.my.attendance.view"
    # MY_LEAVE_REQUEST = "bengkel.my.leave.request"
    # MY_PAYROLL_VIEW = "bengkel.my.payroll.view"
    # MY_PERFORMANCE_VIEW = "bengkel.my.performance.view"


    def __str__(self):
        return self.value
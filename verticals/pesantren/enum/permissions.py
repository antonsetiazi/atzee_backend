# verticals/pesantren/enum/permissions.py

from enum import Enum

class PesantrenPermission(str, Enum):

    # ORGANIZATION_VIEW = "pesantren.organization.view"
    # ORGANIZATION_MANAGE = "pesantren.organization.manage"

    # MY_PROFILE_VIEW = "pesantren.my.profile.view"
    # MY_ATTENDANCE_VIEW = "pesantren.my.attendance.view"
    # MY_LEAVE_REQUEST = "pesantren.my.leave.request"
    # MY_PAYROLL_VIEW = "pesantren.my.payroll.view"
    # MY_PERFORMANCE_VIEW = "pesantren.my.performance.view"


    def __str__(self):
        return self.value
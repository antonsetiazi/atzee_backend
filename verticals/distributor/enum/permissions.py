# verticals/distributor/enum/permissions.py

from enum import Enum

class DistributorPermission(str, Enum):

    # ORGANIZATION_VIEW = "distributor.organization.view"
    # ORGANIZATION_MANAGE = "distributor.organization.manage"

    # MY_PROFILE_VIEW = "distributor.my.profile.view"
    # MY_ATTENDANCE_VIEW = "distributor.my.attendance.view"
    # MY_LEAVE_REQUEST = "distributor.my.leave.request"
    # MY_PAYROLL_VIEW = "distributor.my.payroll.view"
    # MY_PERFORMANCE_VIEW = "distributor.my.performance.view"


    def __str__(self):
        return self.value
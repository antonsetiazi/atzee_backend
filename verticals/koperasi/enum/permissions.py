# verticals/koperasi/enum/permissions.py

from enum import Enum

class KoperasiPermission(str, Enum):

    # ORGANIZATION_VIEW = "koperasi.organization.view"
    # ORGANIZATION_MANAGE = "koperasi.organization.manage"

    # MY_PROFILE_VIEW = "koperasi.my.profile.view"
    # MY_ATTENDANCE_VIEW = "koperasi.my.attendance.view"
    # MY_LEAVE_REQUEST = "koperasi.my.leave.request"
    # MY_PAYROLL_VIEW = "koperasi.my.payroll.view"
    # MY_PERFORMANCE_VIEW = "koperasi.my.performance.view"


    def __str__(self):
        return self.value
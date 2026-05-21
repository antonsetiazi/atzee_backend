# verticals/hr/enum/permissions.py

from enum import Enum


class HrPermission(str, Enum):

    GUEST_HOME_VIEW = "hr.guest.home.view"

    ADMIN_DASHBOARD_VIEW = "hr.admin.dashboard.view"

    def __str__(self):
        return self.value

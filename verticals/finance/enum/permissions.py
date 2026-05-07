# verticals/finance/enum/permissions.py

from enum import Enum

class FinancePermission(str, Enum):

    GUEST_HOME_VIEW = "finance.guest.home.view"

    ADMIN_DASHBOARD_VIEW = "finance.admin.dashboard.view"


    def __str__(self):
        return self.value
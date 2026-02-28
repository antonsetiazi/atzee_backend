# verticals/ustadzku/enum/permissions.py

from enum import Enum

class UstadzkuPermission(str, Enum):

    ADMIN_DASHBOARD_VIEW = "ustadzku.admin.dashboard.view"
    PARTNER_DASHBOARD_VIEW = "ustadzku.partner.dashboard.view"
    USER_DASHBOARD_VIEW = "ustadzku.user.dashboard.view"


    def __str__(self):
        return self.value
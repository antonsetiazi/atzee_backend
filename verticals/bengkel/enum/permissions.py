# verticals/bengkel/enum/permissions.py

from enum import Enum

class BengkelPermission(str, Enum):

    OWNER_DASHBOARD_VIEW = "bengkel.owner.dashboard.view"
    SERVICE_ADVISOR_DASHBOARD_VIEW = "bengkel.service.advisor.dashboard.view"
    MECHANIC_DASHBOARD_VIEW = "bengkel.mechanic.dashboard.view"
    CASHIER_DASHBOARD_VIEW = "bengkel.cashier.dashboard.view"



    def __str__(self):
        return self.value
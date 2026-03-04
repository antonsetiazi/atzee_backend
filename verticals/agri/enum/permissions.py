# verticals/agri/enum/permissions.py

from enum import Enum

class AgriPermission(str, Enum):

    OWNER_DASHBOARD_VIEW = "agri.owner.dashboard.view"
    MANAGER_DASHBOARD_VIEW = "agri.manager.dashboard.view"
    SUPERVISOR_DASHBOARD_VIEW = "agri.supervisor.dashboard.view"
    WORKER_DASHBOARD_VIEW = "agri.worker.dashboard.view"
    FINANCE_DASHBOARD_VIEW = "agri.finance.dashboard.view"



    def __str__(self):
        return self.value
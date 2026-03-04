# verticals/distributor/enum/permissions.py

from enum import Enum

class DistributorPermission(str, Enum):

    EXECUTIVE_DASHBOARD_VIEW = "distributor.executive.dashboard.view"
    SALES_MANAGER_DASHBOARD_VIEW = "distributor.sales.manager.dashboard.view"
    WAREHOUSE_MANAGER_DASHBOARD_VIEW = "distributor.warehouse.manager.dashboard.view"
    FINANCE_MANAGER_DASHBOARD_VIEW = "distributor.finance.manager.dashboard.view"
    SALES_REP_DASHBOARD_VIEW = "distributor.sales.rep.dashboard.view"
    ADMIN_SALES_DASHBOARD_VIEW = "distributor.admin.sales.dashboard.view"
    WAREHOUSE_STAFF_DASHBOARD_VIEW = "distributor.warehouse.staff.dashboard.view"
    FINANCE_STAFF_DASHBOARD_VIEW = "distributor.finance.staff.dashboard.view"


    def __str__(self):
        return self.value
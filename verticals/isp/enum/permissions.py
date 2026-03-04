# verticals/isp/enum/permissions.py

from enum import Enum

class IspPermission(str, Enum):

    OWNER_DASHBOARD_VIEW = "isp.owner.dashboard.view"
    GM_DASHBOARD_VIEW = "isp.gm.dashboard.view"
    NETWORK_DASHBOARD_VIEW = "isp.network.dashboard.view"
    BILLING_DASHBOARD_VIEW = "isp.billing.dashboard.view"
    NOC_DASHBOARD_VIEW = "isp.noc.dashboard.view"
    CS_DASHBOARD_VIEW = "isp.cs.dashboard.view"
    FIELD_DASHBOARD_VIEW = "isp.field.dashboard.view"
    SALES_DASHBOARD_VIEW = "isp.sales.dashboard.view"
    FINANCE_DASHBOARD_VIEW = "isp.finance.dashboard.view"
    CUSTOMER_PORTAL_VIEW = "isp.customer.portal.dashboard.view"


    def __str__(self):
        return self.value
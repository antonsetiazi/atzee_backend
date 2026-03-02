# verticals/pos/enum/permissions.py

from enum import Enum

class PosPermission(str, Enum):

    # DASHBOARD
    DASHBOARD_VIEW = "pos.dashboard.view"
    CASHIER_DASHBOARD_VIEW = "pos.cashier.dashboard.view"
    SUPERVISOR_DASHBOARD_VIEW = "pos.supervisor.dashboard.view"
    MANAGER_DASHBOARD_VIEW = "pos.manager.dashboard.view"
    AREA_DASHBOARD_VIEW = "pos.area.dashboard.view"


    OUTLET_SETTINGS_VIEW = "pos.outlet.settings.view"
    OUTLET_PERFORMANCE_VIEW = "pos.outlet.performance.view"

    REPORT_VIEW = "pos.report.view"

    SHIFT_MANAGE = "pos.shift.manage"
    SHIFT_OPEN = "pos.shift.open"
    SHIFT_CLOSE = "pos.shift.close"
    
    TRANSACTION_VIEW = "pos.transaction.view"
    TRANSACTION_CREATE = "pos.transaction.create"
    TRANSACTION_REFUND = "pos.trasaction.refund"

    TRANSACTION_CASHIER_VIEW = "pos.transaction.cashier.view"
    TRANSACTION_CASHIER_CREATE = "pos.transaction.cashier.create"


    def __str__(self):
        return self.value
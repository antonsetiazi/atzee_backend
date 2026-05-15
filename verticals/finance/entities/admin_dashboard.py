# verticals/finance/entities/admin_dashboard.py

from accounting.selectors.cashflow_selectors import (
    get_monthly_cash_flow,
)
from accounting.selectors.receivable_selectors import (
    get_recent_receivable_invoices,
)
from core.activity.selectors.recent_activity_selector import (
    get_recent_activities,
)
from core.entities.contracts import BaseEntity
from verticals.finance.dashboard.builders.hero import build_hero
from verticals.finance.dashboard.builders.metrics import build_metrics
from verticals.finance.dashboard.builders.modules import build_modules
from verticals.finance.dashboard.builders.quick_actions import (
    build_quick_actions,
)
from verticals.finance.enum.permissions import FinancePermission


class AdminDashboardEntity(BaseEntity):
    """
    finance.admin.dashboard entity
    """

    key = "admin.dashboard"
    domain = "finance"
    permission = FinancePermission.ADMIN_DASHBOARD_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        try:
            return {
                "dashboard": {
                    "hero": build_hero(user),
                    "metrics": build_metrics(),
                    "quickActions": build_quick_actions(),
                    "modules": build_modules(),
                    "activities": get_recent_activities(tenant=tenant),
                    "invoices": get_recent_receivable_invoices(tenant=tenant),
                    "cashFlow": get_monthly_cash_flow(tenant=tenant),
                }
            }

        except Exception as e:
            print(e)

            return {"dashboard": {}}

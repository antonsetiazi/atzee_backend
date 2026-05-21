# verticals/hr/entities/admin_dashboard.py

from accounting.selectors.receivable_selectors import (
    get_recent_receivable_invoices,
)
from core.activity.selectors.recent_activity_selector import (
    get_recent_activities,
)
from core.entities.contracts import BaseEntity
from verticals.hr.dashboard.builders.hero import build_hero
from verticals.hr.dashboard.builders.metrics import build_metrics
from verticals.hr.dashboard.builders.modules import build_modules
from verticals.hr.dashboard.builders.quick_actions import (
    build_quick_actions,
)
from verticals.hr.enum.permissions import HrPermission


class AdminDashboardEntity(BaseEntity):
    """
    hr.admin.dashboard entity
    """

    key = "admin.dashboard"
    domain = "hr"
    permission = HrPermission.ADMIN_DASHBOARD_VIEW

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
                }
            }

        except Exception as e:
            print(e)

            return {"dashboard": {}}

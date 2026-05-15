# verticals/finance/ui/pages/dahsboard/admin_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.block import (
    DashboardBlock,
)
from core.ui.schema.page import Page
from verticals.finance.enum.permissions import FinancePermission

UI_PAGES = [
    Page(
        key="finance.admin.dashboard",
        entity="dashboard",
        domain="finance",
        path="/dashboard",
        title="Admin Dashboard",
        permissions=[FinancePermission.ADMIN_DASHBOARD_VIEW],
        meta={
            "showBottomNav": True,
            "showHeader": False,
            "fullscreen": False,
            "headerMode": "overlay",
        },
        description="Finance Control Room & Accounting Overview Platform Atzee Finance",
        data_source="/entities/finance/admin.dashboard/query/",
        blocks=[
            DashboardBlock(
                variant="finance",
                data_key="dashboard",
            )
        ],
    )
]


register_ui_module_pages("finance", UI_PAGES)

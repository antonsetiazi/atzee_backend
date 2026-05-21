# verticals/hr/ui/pages/dahsboard/admin_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.block import (
    DashboardBlock,
)
from core.ui.schema.page import Page
from verticals.hr.enum.permissions import HrPermission

UI_PAGES = [
    Page(
        key="hr.admin.dashboard",
        entity="dashboard",
        domain="hr",
        path="/dashboard",
        title="Admin Dashboard",
        permissions=[HrPermission.ADMIN_DASHBOARD_VIEW],
        meta={
            "showBottomNav": True,
            "showHeader": False,
            "fullscreen": False,
            "headerMode": "overlay",
        },
        description="",
        data_source="/entities/hr/admin.dashboard/query/",
        blocks=[
            DashboardBlock(
                variant="hr",
                data_key="dashboard",
            )
        ],
    )
]


register_ui_module_pages("hr", UI_PAGES)

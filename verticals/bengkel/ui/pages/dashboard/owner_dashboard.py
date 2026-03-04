# verticals/bengkel/ui/pages/dashboard/owner_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.bengkel.enum.permissions import BengkelPermission


UI_PAGES = [
    Page(
        key="bengkel.owner.dashboard",
        entity="dashboard",
        domain="bengkel",
        path="/dashboard",
        title="Owner Dashboard",
        permissions=[BengkelPermission.OWNER_DASHBOARD_VIEW], 
        description="Workshop Business Overview",
        data_source="/entities/bengkel/owner.dashboard/query/",
        blocks=[

            # QUICK ACCESS
            ShortcutBlock(
                title="Quick Access",
                items=[
                    ShortcutItem(key="create_wo", label="Create Work Order", icon="file-plus", to="/work-order/create"),
                    ShortcutItem(key="approval", label="Pending Approval", icon="check-circle", to="/work-order/approval"),
                    ShortcutItem(key="invoice", label="Invoices", icon="receipt", to="/finance/invoice"),
                    ShortcutItem(key="report", label="Revenue Report", icon="bar-chart", to="/reports/revenue"),
                ],
            ),

            # KPI SECTION
            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="today_revenue", title="Revenue Today", data_key="today_revenue"),
                    StatBlock(key="active_work_orders", title="Active Work Orders", data_key="active_work_orders"),
                    StatBlock(key="pending_approval", title="Pending Approval", data_key="pending_approval"),
                    StatBlock(key="low_stock", title="Low Stock Items", data_key="low_stock"),
                ]
            ),

            # MECHANIC PERFORMANCE
            ListViewBlock(
                title="Mechanic Performance",
                data_key="mechanic_performance",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="mechanic_name"),
                    subtitle=ListFieldSchema(key="jobs_completed"),
                    description=ListFieldSchema(key="efficiency_rate", suffix="%"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[BengkelPermission.OWNER_DASHBOARD_VIEW], 
            ),
        ],
    ),
]

register_ui_module_pages("bengkel", UI_PAGES)
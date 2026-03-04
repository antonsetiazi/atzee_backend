# verticals/bengkel/ui/pages/dashboard/service_advisor_dashboard.py

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
        key="bengkel.service_advisor.dashboard",
        entity="dashboard",
        domain="bengkel",
        path="/dashboard",
        title="Service Advisor Dashboard",
        permissions=[BengkelPermission.SERVICE_ADVISOR_DASHBOARD_VIEW], 
        description="Front Desk & Work Order Monitoring",
        data_source="/entities/bengkel/service_advisor.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Action",
                items=[
                    ShortcutItem(key="create_wo", label="Create Work Order", icon="file-plus", to="/work-order/create"),
                    ShortcutItem(key="approval", label="Approval Estimasi", icon="check", to="/work-order/approval"),
                    ShortcutItem(key="booking", label="New Booking", icon="calendar-plus", to="/appointment/create"),
                ],
            ),

            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="today_wo", title="Work Order Today", data_key="today_work_orders"),
                    StatBlock(key="pending_approval", title="Pending Approval", data_key="pending_approval"),
                    StatBlock(key="waiting_confirmation", title="Waiting Confirmation", data_key="waiting_confirmation"),
                ]
            ),

            ListViewBlock(
                title="Recent Work Orders",
                data_key="recent_work_orders",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="work_order_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="vehicle"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[BengkelPermission.SERVICE_ADVISOR_DASHBOARD_VIEW], 
            ),
        ],
    ),
]

register_ui_module_pages("bengkel", UI_PAGES)
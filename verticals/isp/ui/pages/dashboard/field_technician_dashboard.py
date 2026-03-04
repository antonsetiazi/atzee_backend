# verticals/isp/ui/pages/dashboard/field_technician_dashboard.py

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

from verticals.isp.enum.permissions import IspPermission


UI_PAGES = [
    Page(
        key="isp.field.dashboard",
        entity="dashboard",
        domain="isp",
        path="/dashboard",
        title="Field Technician Dashboard",
        permissions=[IspPermission.FIELD_DASHBOARD_VIEW], 
        description="Field Operations & Installation Tasks",
        data_source="/entities/isp/field.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="My Tasks",
                items=[
                    ShortcutItem(key="work_orders", label="My Work Orders", icon="clipboard", to="/operations/my-work-orders"),
                    ShortcutItem(key="install_tasks", label="Installation Tasks", icon="tool", to="/operations/installations"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="pending_tasks", title="Pending Tasks", data_key="pending_tasks"),
                    StatBlock(key="completed_today", title="Completed Today", data_key="completed_today"),
                ],
            ),

            ListViewBlock(
                title="Assigned Work Orders",
                data_key="assigned_work_orders",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="work_order_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="address"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[IspPermission.FIELD_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("isp", UI_PAGES)
# verticals/bengkel/ui/pages/dashboard/mechanic_dashboard.py

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
        key="bengkel.mechanic.dashboard",
        entity="dashboard",
        domain="bengkel",
        path="/dashboard",
        title="Mechanic Dashboard",
        permissions=[BengkelPermission.MECHANIC_DASHBOARD_VIEW],  
        description="Assigned Jobs & Checklist",
        data_source="/entities/bengkel/mechanic.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Action",
                items=[
                    ShortcutItem(key="my_jobs", label="My Jobs", icon="tool", to="/mechanic/jobs"),
                    ShortcutItem(key="checklist", label="Checklist", icon="check-square", to="/mechanic/checklist"),
                    ShortcutItem(key="parts_request", label="Parts Request", icon="package", to="/mechanic/parts-request"),
                ],
            ),

            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="assigned_jobs", title="Assigned Jobs", data_key="assigned_jobs"),
                    StatBlock(key="in_progress", title="In Progress", data_key="in_progress"),
                    StatBlock(key="completed_today", title="Completed Today", data_key="completed_today"),
                ]
            ),

            ListViewBlock(
                title="My Active Work Orders",
                data_key="my_active_work_orders",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="work_order_number"),
                    subtitle=ListFieldSchema(key="vehicle"),
                    description=ListFieldSchema(key="service_type"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[BengkelPermission.MECHANIC_DASHBOARD_VIEW],  
            ),
        ],
    ),
]

register_ui_module_pages("bengkel", UI_PAGES)
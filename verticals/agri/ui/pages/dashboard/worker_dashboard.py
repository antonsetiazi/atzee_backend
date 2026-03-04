# verticals/agri/ui/pages/dashboard/worker_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ShortcutBlock,
    ShortcutItem,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.agri.enum.permissions import AgriPermission


UI_PAGES = [
    Page(
        key="agri.worker.dashboard",
        entity="dashboard",
        domain="agri",
        path="/dashboard",
        title="My Work Dashboard",
        permissions=[AgriPermission.WORKER_DASHBOARD_VIEW],
        description="Daily Task Panel",
        data_source="/entities/agri/worker.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="My Actions",
                items=[
                    ShortcutItem(key="log_work", label="Input Work Log", icon="edit"),
                    ShortcutItem(key="submit_activity", label="Submit Activity", icon="send"),
                ],
            ),
 
            ListViewBlock(
                title="My Tasks Today",
                data_key="my_tasks",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="activity_type"),
                    subtitle=ListFieldSchema(key="plot_name"),
                    description=ListFieldSchema(key="schedule_time"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[AgriPermission.WORKER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("agri", UI_PAGES)
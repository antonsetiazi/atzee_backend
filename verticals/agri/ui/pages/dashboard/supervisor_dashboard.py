# verticals/agri/ui/pages/dashboard/supervisor_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.agri.enum.permissions import AgriPermission


UI_PAGES = [
    Page(
        key="agri.supervisor.dashboard",
        entity="dashboard", 
        domain="agri",
        path="/dashboard",
        title="Field Supervisor Dashboard",
        permissions=[AgriPermission.SUPERVISOR_DASHBOARD_VIEW],
        description="Field Monitoring Panel",
        data_source="/entities/agri/supervisor.dashboard/query/",
        blocks=[

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="today_tasks", title="Today's Tasks", data_key="today_tasks"),
                    StatBlock(key="open_issues", title="Open Incidents", data_key="open_incidents"),
                ]
            ),

            ListViewBlock(
                title="Today's Field Activities",
                data_key="today_activities",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="activity_type"),
                    subtitle=ListFieldSchema(key="plot_name"),
                    description=ListFieldSchema(key="worker_name"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[AgriPermission.SUPERVISOR_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("agri", UI_PAGES)
# verticals/research/ui/pages/dashboard/researcher_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.research.enum.permissions import ResearchPermission 


UI_PAGES = [
    Page(
        key="research.researcher.dashboard",
        entity="dashboard",
        domain="research",
        path="/dashboard",
        title="Researcher Dashboard",
        permissions=[ResearchPermission.RESEARCHER_DASHBOARD_VIEW], 
        data_source="/entities/research/researcher.dashboard/query/",
        blocks=[
            ContainerBlock(
                blocks=[
                    StatBlock(key="assigned_tasks", title="Assigned Tasks", data_key="assigned_tasks"),
                    StatBlock(key="experiment_logs", title="Experiment Logs This Week", data_key="logs_week"),
                ]
            ),

            ListViewBlock(
                title="My Active Projects",
                data_key="assigned_projects",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="project_title"),
                    description=ListFieldSchema(key="role"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[ResearchPermission.RESEARCHER_DASHBOARD_VIEW],
            ),
        ],
    )
]

register_ui_module_pages("research", UI_PAGES)
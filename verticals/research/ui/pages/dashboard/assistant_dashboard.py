# verticals/research/ui/pages/dashboard/assistant_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.research.enum.permissions import ResearchPermission 


UI_PAGES = [
    Page(
        key="research.assistant.dashboard",
        entity="dashboard",
        domain="research",
        path="/dashboard",
        title="Research Assistant Dashboard",
        permissions=[ResearchPermission.ASSISTANT_DASHBOARD_VIEW], 
        data_source="/entities/research/assistant.dashboard/query/",
        blocks=[
            ListViewBlock(
                title="Supporting Projects",
                data_key="support_projects",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="project_title"),
                    subtitle=ListFieldSchema(key="principal_investigator"),
                ),
                permissions=[ResearchPermission.ASSISTANT_DASHBOARD_VIEW], 
            ),
        ],
    )
]

register_ui_module_pages("research", UI_PAGES)
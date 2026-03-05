# verticals/research/ui/pages/dashboard/reviewer_dashboard.py

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

from verticals.research.enum.permissions import ResearchPermission 


UI_PAGES = [
    Page(
        key="research.reviewer.dashboard",
        entity="dashboard",
        domain="research",
        path="/dashboard",
        title="Reviewer Dashboard",
        permissions=[ResearchPermission.REVIEWER_DASHBOARD_VIEW], 
        data_source="/entities/research/reviewer.dashboard/query/",
        blocks=[

            ContainerBlock(
                blocks=[
                    StatBlock(key="assigned", title="Assigned Reviews", data_key="assigned_reviews"),
                    StatBlock(key="due_soon", title="Due Soon", data_key="due_soon"),
                ]
            ),

            ListViewBlock(
                title="My Assigned Proposals",
                data_key="assigned_proposals",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="proposal_title"),
                    subtitle=ListFieldSchema(key="submitted_by"),
                    description=ListFieldSchema(key="deadline"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[ResearchPermission.REVIEWER_DASHBOARD_VIEW],
            ),
        ],
    )
]

register_ui_module_pages("research", UI_PAGES)
# verticals/research/ui/pages/dashboard/committee_dashboard.py

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
        key="research.committee.dashboard",
        entity="dashboard",
        domain="research",
        path="/dashboard",
        title="Committee Dashboard",
        permissions=[ResearchPermission.COMMITTEE_DASHBOARD_VIEW], 
        data_source="/entities/research/committee.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Review Center",
                items=[
                    ShortcutItem(key="proposals", label="Pending Proposals", icon="file-check", to="/research/pipeline/proposals"),
                    ShortcutItem(key="ethics", label="Ethics Review", icon="shield", to="/research/governance/ethics"),
                ],
            ),

            ContainerBlock(
                blocks=[
                    StatBlock(key="pending_review", title="Proposals Pending Review", data_key="pending_review"),
                    StatBlock(key="approved_this_month", title="Approved This Month", data_key="approved_this_month"),
                ]
            ),

            ListViewBlock(
                title="Recently Submitted Proposals",
                data_key="recent_proposals",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="proposal_title"),
                    subtitle=ListFieldSchema(key="applicant"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[ResearchPermission.COMMITTEE_DASHBOARD_VIEW], 
            ),
        ],
    )
]

register_ui_module_pages("research", UI_PAGES)
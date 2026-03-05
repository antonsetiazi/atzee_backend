# verticals/research/ui/pages/dashboard/pi_dashboard.py

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
        key="research.pi.dashboard",
        entity="dashboard",
        domain="research",
        path="/dashboard",
        title="Principal Investigator Dashboard",
        permissions=[ResearchPermission.PI_DASHBOARD_VIEW],
        data_source="/entities/research/pi.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Action",
                items=[
                    ShortcutItem(key="new_proposal", label="Submit Proposal", icon="plus-circle", to="/research/pipeline/proposals/create"),
                    ShortcutItem(key="my_projects", label="My Projects", icon="flask", to="/research/projects/my"),
                ],
            ),

            ContainerBlock(
                blocks=[
                    StatBlock(key="active_projects", title="My Active Projects", data_key="active_projects"),
                    StatBlock(key="budget_remaining", title="Remaining Budget", data_key="remaining_budget"),
                ]
            ),

            ListViewBlock(
                title="Upcoming Milestones",
                data_key="upcoming_milestones",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="milestone_name"),
                    subtitle=ListFieldSchema(key="project"),
                    description=ListFieldSchema(key="due_date"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[ResearchPermission.PI_DASHBOARD_VIEW],
            ), 
        ],
    )
]

register_ui_module_pages("research", UI_PAGES)
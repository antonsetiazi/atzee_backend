# verticals/research/ui/pages/dashboard/admin_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
)

from verticals.research.enum.permissions import ResearchPermission 


UI_PAGES = [
    Page(
        key="research.admin.dashboard",
        entity="dashboard",
        domain="research",
        path="/dashboard",
        title="Research Admin Dashboard",
        permissions=[ResearchPermission.ADMIN_DASHBOARD_VIEW], 
        data_source="/entities/research/admin.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Operational Tools",
                items=[
                    ShortcutItem(key="manage_program", label="Manage Programs", icon="settings", to="/research/governance/programs"),
                    ShortcutItem(key="archive", label="Archive", icon="archive", to="/research/archive"),
                ],
            ),

            ContainerBlock(
                blocks=[
                    StatBlock(key="total_users", title="Research Users", data_key="users"),
                    StatBlock(key="total_projects", title="Total Projects", data_key="projects"),
                ]
            ),
        ],
    )
]

register_ui_module_pages("research", UI_PAGES)
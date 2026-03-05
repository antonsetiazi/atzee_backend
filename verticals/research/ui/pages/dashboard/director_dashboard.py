# verticals/research/ui/pages/dashboard/research_director_dashboard.py

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
        key="research.director.dashboard",
        entity="dashboard",
        domain="research",
        path="/dashboard",
        title="Research Director Dashboard",
        permissions=[ResearchPermission.DIRECTOR_DASHBOARD_VIEW], 
        description="Global Research Overview & Governance Control",
        data_source="/entities/research/director.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Access",
                items=[
                    ShortcutItem(key="programs", label="Research Programs", icon="layers", to="/research/governance/programs"),
                    ShortcutItem(key="proposals", label="All Proposals", icon="file-text", to="/research/pipeline/proposals"),
                    ShortcutItem(key="projects", label="Active Projects", icon="flask", to="/research/projects"),
                    ShortcutItem(key="reports", label="Reports", icon="bar-chart-2", to="/research/reports"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="active_projects", title="Active Projects", data_key="active_projects"),
                    StatBlock(key="pending_approvals", title="Pending Approvals", data_key="pending_approvals"),
                    StatBlock(key="total_budget", title="Total Budget Utilization", data_key="budget_utilization", suffix="%"),
                    StatBlock(key="publications", title="Total Publications", data_key="publications_count"),
                ],
            ),

            ListViewBlock(
                title="Projects Near Deadline",
                data_key="deadline_projects",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="project_title"),
                    subtitle=ListFieldSchema(key="principal_investigator"),
                    description=ListFieldSchema(key="deadline"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[ResearchPermission.DIRECTOR_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("research", UI_PAGES)
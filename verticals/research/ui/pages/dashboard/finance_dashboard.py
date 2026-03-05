# verticals/research/ui/pages/dashboard/finance_dashboard.py

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
        key="research.finance.dashboard",
        entity="dashboard",
        domain="research",
        path="/dashboard",
        title="Finance Dashboard", 
        permissions=[ResearchPermission.FINANCE_DASHBOARD_VIEW],
        data_source="/entities/research/finance.dashboard/query/",
        blocks=[

            ContainerBlock(
                blocks=[
                    StatBlock(key="total_allocated", title="Total Budget Allocated", data_key="allocated"),
                    StatBlock(key="total_spent", title="Total Spent", data_key="spent"),
                ]
            ),

            ListViewBlock(
                title="Projects Over Budget",
                data_key="over_budget_projects",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="project_title"),
                    subtitle=ListFieldSchema(key="principal_investigator"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[ResearchPermission.FINANCE_DASHBOARD_VIEW],
            ),
        ],
    )
]

register_ui_module_pages("research", UI_PAGES)
# verticals/agri/ui/pages/dashboard/manager_dashboard.py

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

from verticals.agri.enum.permissions import AgriPermission


UI_PAGES = [
    Page(
        key="agri.manager.dashboard",
        entity="dashboard",
        domain="agri",
        path="/dashboard",
        title="Farm Manager Dashboard",
        permissions=[AgriPermission.MANAGER_DASHBOARD_VIEW],
        description="Operational Agriculture Control",
        data_source="/entities/agri/manager.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Operations",
                items=[
                    ShortcutItem(key="new_cycle", label="Start Cycle", icon="play"),
                    ShortcutItem(key="assign_worker", label="Assign Worker", icon="users"),
                    ShortcutItem(key="add_activity", label="Add Activity", icon="clipboard"),
                    ShortcutItem(key="inventory", label="Inventory", icon="package"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="active_plots", title="Active Plots", data_key="active_plots"),
                    StatBlock(key="today_activities", title="Today's Activities", data_key="today_activities"),
                    StatBlock(key="pending_tasks", title="Pending Tasks", data_key="pending_tasks"),
                    StatBlock(key="monthly_cost", title="Monthly Cost", data_key="monthly_cost"),
                ]
            ),

            ListViewBlock(
                title="Active Planting Cycles",
                data_key="active_cycles", 
                tile=ListTileSchema(
                    title=ListFieldSchema(key="plot_name"),
                    subtitle=ListFieldSchema(key="crop_name"),
                    description=ListFieldSchema(key="stage"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[AgriPermission.MANAGER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("agri", UI_PAGES)
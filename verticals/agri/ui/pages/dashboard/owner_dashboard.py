# verticals/agri/ui/pages/dashboard/owner_dashboard.py

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
        key="agri.owner.dashboard",
        entity="dashboard",
        domain="agri",
        path="/dashboard",
        title="Owner Dashboard",
        permissions=[AgriPermission.OWNER_DASHBOARD_VIEW],
        description="Strategic Agriculture Overview",
        data_source="/entities/agri/owner.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Strategic Overview",
                items=[
                    ShortcutItem(key="farms", label="Farms", icon="map", to="/farms"),
                    ShortcutItem(key="cycles", label="Planting Cycles", icon="refresh-cw", to="/cycles"),
                    ShortcutItem(key="finance", label="Finance", icon="dollar-sign", to="/finance"),
                    ShortcutItem(key="reports", label="Reports", icon="bar-chart-3", to="/reports"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="total_land", title="Total Land Area", data_key="total_land", suffix=" ha"),
                    StatBlock(key="active_cycles", title="Active Cycles", data_key="active_cycles"),
                    StatBlock(key="total_cost", title="Total Cost", data_key="total_cost"),
                    StatBlock(key="roi", title="ROI", data_key="roi", suffix="%"),
                ]
            ),

            ListViewBlock(
                title="Recent Harvest Results",
                data_key="recent_harvests",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="farm_name"),
                    subtitle=ListFieldSchema(key="crop_name"),
                    description=ListFieldSchema(key="harvest_date"),
                    trailing=ListFieldSchema(key="total_yield", suffix=" kg"),
                ),
                permissions=[AgriPermission.OWNER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("agri", UI_PAGES)
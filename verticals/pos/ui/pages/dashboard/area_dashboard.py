# verticals/pos/ui/pages/dashboard/area_dashboard.py

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

from verticals.pos.enum.permissions import PosPermission


UI_PAGES = [
    Page(
        key="pos.area.dashboard",
        entity="dashboard",
        domain="pos",
        path="/dashboard",
        title="Area Manager Dashboard",
        permissions=[PosPermission.AREA_DASHBOARD_VIEW],
        description="Multi Outlet Monitoring & Performance Overview",
        data_source="/entities/pos/area.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Monitoring",
                items=[
                    ShortcutItem(key="global_dashboard", label="Global Dashboard", icon="globe", to="/pos/area/dashboard"),
                    ShortcutItem(key="outlet_perf", label="Outlet Performance", icon="bar-chart-2", to="/pos/area/performance"),
                    ShortcutItem(key="inventory_compare", label="Inventory Comparison", icon="layers", to="/pos/area/inventory"),
                    ShortcutItem(key="transaction_search", label="Transaction Search", icon="search", to="/pos/transactions"),
                ],
            ),

            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="total_revenue", title="Total Revenue Today", data_key="total_revenue"),
                    StatBlock(key="active_outlets", title="Active Outlets", data_key="active_outlets"),
                    StatBlock(key="total_transactions", title="Total Transactions", data_key="transactions"),
                    StatBlock(key="refund_rate", title="Refund Rate", data_key="refund_rate"),
                ]
            ),

            ListViewBlock(
                title="Outlet Performance Snapshot",
                data_key="outlet_performance",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="outlet_name"),
                    subtitle=ListFieldSchema(key="revenue"),
                    description=ListFieldSchema(key="transactions"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[PosPermission.AREA_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("pos", UI_PAGES)
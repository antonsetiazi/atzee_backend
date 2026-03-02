# verticals/pos/ui/pages/dashboard/manager_dashboard.py

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
        key="pos.manager.dashboard",
        entity="dashboard",
        domain="pos",
        path="/dashboard",
        title="Store Manager Dashboard",
        permissions=[PosPermission.MANAGER_DASHBOARD_VIEW],
        description="Outlet Performance & Financial Overview",
        data_source="/entities/pos/manager.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Management",
                items=[
                    ShortcutItem(key="pos", label="POS", icon="shopping-cart", to="/pos/sale/new"),
                    ShortcutItem(key="reports", label="Reports", icon="bar-chart", to="/pos/reports"),
                    ShortcutItem(key="inventory", label="Inventory Snapshot", icon="archive", to="/pos/inventory"),
                    ShortcutItem(key="staff", label="Staff", icon="users", to="/pos/staff"),
                    ShortcutItem(key="settings", label="Outlet Settings", icon="settings", to="/pos/settings"),
                ],
            ),

            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="daily_revenue", title="Daily Revenue", data_key="daily_revenue"),
                    StatBlock(key="monthly_revenue", title="Monthly Revenue", data_key="monthly_revenue"),
                    StatBlock(key="total_transactions", title="Transactions Today", data_key="transactions_today"),
                    StatBlock(key="refund_total", title="Refund Total", data_key="refund_total"),
                ]
            ),

            ListViewBlock(
                title="Top Selling Products",
                data_key="top_products",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="product_name"),
                    subtitle=ListFieldSchema(key="qty_sold"),
                    description=ListFieldSchema(key="revenue"),
                ),
                permissions=[PosPermission.MANAGER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("pos", UI_PAGES)
# verticals/marketplace/ui/pages/dashboard/admin_dashboard.py

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

from verticals.marketplace.enum.permissions import MarketplacePermission


UI_PAGES = [
    Page(
        key="marketplace.admin.dashboard",
        entity="dashboard",
        domain="marketplace",
        path="/admin/dashboard",
        title="Marketplace Admin Dashboard",
        description="Marketplace monitoring & control panel",
        permissions=[MarketplacePermission.ADMIN_DASHBOARD_VIEW],
        data_source="/entities/marketplace/admin.dashboard/query/",
        blocks=[

            # QUICK ACTION
            ShortcutBlock(
                title="Admin Actions",
                items=[
                    ShortcutItem(key="manage_users", label="Users", icon="users", to="/admin/users"),
                    ShortcutItem(key="stores", label="Stores", icon="store", to="/admin/stores"),
                    ShortcutItem(key="products", label="Products", icon="box", to="/admin/products"),
                    ShortcutItem(key="orders", label="Orders", icon="shopping-bag", to="/admin/orders"),
                ],
            ),

            # PLATFORM KPI
            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="total_revenue", title="Total Revenue", data_key="total_revenue"),
                    StatBlock(key="total_orders", title="Total Orders", data_key="total_orders"),
                    StatBlock(key="active_sellers", title="Active Sellers", data_key="active_sellers"),
                    StatBlock(key="active_buyers", title="Active Buyers", data_key="active_buyers"),
                ],
            ),

            # RECENT ORDERS
            ListViewBlock(
                title="Latest Marketplace Orders",
                data_key="recent_orders",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="order_number"),
                    subtitle=ListFieldSchema(key="buyer_name"),
                    description=ListFieldSchema(key="total_amount", format="currency"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[MarketplacePermission.ADMIN_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("marketplace", UI_PAGES)
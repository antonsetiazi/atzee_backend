# verticals/marketplace/ui/pages/dashboard/buyer_dashboard.py

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
        key="marketplace.buyer.dashboard",
        entity="dashboard",
        domain="marketplace",
        path="/dashboard",
        title="Marketplace Home",
        description="Browse products and track your orders",
        permissions=[MarketplacePermission.BUYER_DASHBOARD_VIEW],
        data_source="/entities/marketplace/buyer.dashboard/query/",
        blocks=[

            # QUICK ACTION
            ShortcutBlock(
                title="Quick Access",
                items=[
                    ShortcutItem(key="browse_products", label="Browse Products", icon="search", to="/marketplace/products"),
                    ShortcutItem(key="categories", label="Categories", icon="grid", to="/marketplace/categories"),
                    ShortcutItem(key="flash_sale", label="Flash Sale", icon="zap", to="/marketplace/flash-sale"),
                    ShortcutItem(key="cart", label="My Cart", icon="shopping-cart", to="/marketplace/cart"),
                ],
            ),

            # PERSONAL STATS
            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="active_orders", title="Active Orders", data_key="active_orders"),
                    StatBlock(key="wishlist_items", title="Wishlist Items", data_key="wishlist_items"),
                    StatBlock(key="coupons", title="Available Coupons", data_key="available_coupons"),
                    StatBlock(key="reward_points", title="Reward Points", data_key="reward_points"),
                ],
            ),

            # RECENT ORDERS
            ListViewBlock(
                title="Recent Orders",
                data_key="recent_orders",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="order_number"),
                    subtitle=ListFieldSchema(key="total_amount", format="currency"),
                    description=ListFieldSchema(key="store_name"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[MarketplacePermission.BUYER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("marketplace", UI_PAGES)
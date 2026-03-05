# verticals/marketplace/ui/pages/dashboard/seller_dashboard.py

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
        key="marketplace.seller.dashboard",
        entity="dashboard",
        domain="marketplace",
        path="/seller/dashboard",
        title="Seller Dashboard",
        description="Manage your store and track performance",
        permissions=[MarketplacePermission.SELLER_DASHBOARD_VIEW],
        data_source="/entities/marketplace/seller.dashboard/query/",
        blocks=[

            # QUICK ACTION
            ShortcutBlock(
                title="Quick Action",
                items=[
                    ShortcutItem(key="add_product", label="Add Product", icon="plus-circle", to="/seller/products/create"),
                    ShortcutItem(key="product_list", label="My Products", icon="box", to="/seller/products"),
                    ShortcutItem(key="orders", label="Orders", icon="shopping-bag", to="/seller/orders"),
                    ShortcutItem(key="marketing", label="Marketing", icon="megaphone", to="/seller/marketing"),
                ],
            ),

            # KPI
            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="today_sales", title="Sales Today", data_key="today_sales"),
                    StatBlock(key="pending_orders", title="Pending Orders", data_key="pending_orders"),
                    StatBlock(key="total_products", title="Total Products", data_key="total_products"),
                    StatBlock(key="store_rating", title="Store Rating", data_key="store_rating", suffix="★"),
                ],
            ),

            # RECENT ORDERS
            ListViewBlock(
                title="Recent Orders",
                data_key="recent_orders",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="order_number"),
                    subtitle=ListFieldSchema(key="buyer_name"),
                    description=ListFieldSchema(key="total_amount", format="currency"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[MarketplacePermission.SELLER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("marketplace", UI_PAGES)
# marketplace/ui/pages/order_list.py

from core.ui.registry import register_ui_module_pages
from marketplace.ui.pages._base_order_list import build_order_list_page

from marketplace.enum.permissions import MarketplacePermission

UI_PAGES = build_order_list_page(
    key="orders.list",
    domain="marketplace",
    title_page="Orders",
    subtitle_page="Monitor all customer orders and transactions",
    path="/admin/orders",
    data_source="/entities/marketplace/orders.list/query/",
    permissions=[MarketplacePermission.ADMIN_ORDERS_VIEW],
    detail_path="/admin/orders/{id}",
    search_mode="server",
)

register_ui_module_pages("marketplace", UI_PAGES)
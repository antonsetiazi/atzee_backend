# business/payment_gateway/ui/pages/payment_gateway_list.py

from core.ui.registry import register_ui_module_pages
from business.payment_gateway.ui.pages._base_payment_gateway_list import (
    build_payment_gateway_list_page,
)

from business.enum.permissions import BusinessPermission

UI_PAGES = build_payment_gateway_list_page(
    key="payment_gateway.list",
    domain="business",
    title_page="Payment Transactions",
    subtitle_page="Monitor all external payment gateway transactions",
    path="/admin/payment-transactions",
    data_source="/entities/business/payment_gateway.list/query/",
    permissions=[BusinessPermission.ADMIN_PAYMENT_GATEWAY_VIEW],
    detail_path="/admin/payment-transactions/{id}",
    search_mode="server",
)

register_ui_module_pages("business", UI_PAGES)
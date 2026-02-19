# business/customers/ui/pages/customer_list.py

from core.ui.registry import register_ui_module_pages
from business.customers.ui.pages._base_customer_list import (
    build_customer_list_page,
)

UI_PAGES = build_customer_list_page(
    key="customers.list",
    domain="business",
    path="/business/customers",
    data_source="/entities/business/customers.list/query/",
    permissions=["business.customers.view"],
    create_path="/business/customers/create",
    edit_path="/business/customers/{id}/edit",
    delete_endpoint="/business/customers/{id}/",
    search_mode="client"
)

register_ui_module_pages("business", UI_PAGES)
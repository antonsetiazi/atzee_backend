# business/customers/ui/pages/customer_list.py

from business.customers.ui.pages._base_customer_list import (
    build_customer_list_page,
)

UI_PAGES = build_customer_list_page(
    key="apotek.customers.list",
    domain="business",
    path="/apotek/customers",
    data_source="/entities/business/customers.list/query/",
    permissions=["business.customers.view"],
    create_path="/apotek/customers/create",
    edit_path="/apotek/customers/{id}/edit",
    delete_endpoint="/business/customers/{id}/",
    search_mode="client"
)

# business/products/ui/pages/product_list.py

from business.products.ui.pages._base_product_list import (
    build_product_list_page,
)

UI_PAGES = build_product_list_page(
    key="products.list",
    domain="business",
    path="/business/products",
    data_source="/entities/business/products.list/query/",
    permissions=["business.products.view"],
    create_path="/business/products/create",
    edit_path="/business/products/{id}/edit",
    delete_endpoint="/business/products/{id}/",
    search_mode="client"
)

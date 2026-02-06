# business/products/ui/pages/product_create.py

from business.products.ui.pages._base_product_form import (
    build_product_form_page,
)

UI_PAGES = build_product_form_page(
    key="products.create",
    domain="business",
    path="/business/products/create",
    submit_to="/business/products/",
    method="POST",
    permissions=["business.products.add"],
    title="Create Product",
    redirect_page="/business/products",
)

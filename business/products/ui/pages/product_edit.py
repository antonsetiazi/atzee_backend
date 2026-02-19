# business/products/ui/pages/product_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from business.products.ui.pages._base_product_form import (
    build_product_form_page,
)

UI_PAGES = build_product_form_page(
    key="products.edit",
    domain="business",
    path="/business/products/:id/edit",
    submit_to="/business/products/{id}/",
    method="PATCH",
    permissions=["business.products.update"],
    title="Edit Product",
    redirect_page="/business/products",
    extra_fields=[
        Field(
            key="id",
            label="Product ID",
            type="hidden",
        ),
    ],
)

register_ui_module_pages("business", UI_PAGES)
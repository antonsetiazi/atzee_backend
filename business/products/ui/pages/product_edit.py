# business/products/ui/pages/product_edit.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="products.edit",
    entity="products",
    title="Product",
    permissions=["business.products.update"],
    blocks=[
        FormBlock(
            submit_to="/business/products/{id}/",
            method="PATCH",
            title="Edit Product",
            description="Perbarui data produk",
            fields=[
                Field(key="id", label="Product ID", type="hidden"),
                Field(key="code", label="Product Code", type="text"),
                Field(key="name", label="Product Name", type="text", required=True),
                Field(
                    key="product_type",
                    label="Product Type",
                    type="select",
                    required=True,
                    options=[
                        {"label": "Good", "value": "good"},
                        {"label": "Service", "value": "service"},
                    ],
                ),
                Field(
                    key="description",
                    label="Description",
                    type="textarea",
                ),
            ],
            actions=[
                Action(type="submit", label="Save"),
                Action(
                    type="redirect",
                    label="Cancel",
                    to="/products"
                ),
            ],
        )
    ],
)

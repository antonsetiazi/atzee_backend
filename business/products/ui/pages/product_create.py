# business/products/ui/pages/product_create.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="products.create",
    entity="products",
    domain="business",
    path="/business/products/create",
    title="Product",
    permissions=["business.products.add"],
    blocks=[
        FormBlock(
            submit_to="/business/products/",
            method="POST",
            title="Create Product",
            description="Lengkapi data produk dengan benar",
            redirect_to={
                "page": "products.list",
            },
            fields=[
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
                    to="/business/products"
                ),
            ],
        )
    ],
)

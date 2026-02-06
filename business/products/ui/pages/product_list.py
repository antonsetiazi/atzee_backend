# business/products/ui/pages/product_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="products.list",
    entity="products",
    domain="business",
    path="/business/products",
    title="Products",
    permissions=["business.products.view"],
    blocks=[
        TableBlock(
            data_source="/entities/business/products.list/query/",
            search_mode="client",
            columns=[
                TableColumn(key="code", label="Code"),
                TableColumn(key="name", label="Name"),
                TableColumn(key="product_type", label="Type"),
                TableColumn(key="is_active", label="Active"),
            ],
            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    icon="edit",
                    to="/business/products/{id}/edit",
                    permission="business.products.update",
                ),
                Action(
                    type="delete",
                    label="Delete",
                    icon="delete",
                    permission="business.products.delete",
                    confirm={
                        "title": "Delete Product",
                        "message": "Are you sure you want to delete this product?",
                        "level": "danger",
                    },
                    endpoint="/business/products/{id}/",
                ),
            ],
            top_actions=[
                Action(
                    type="navigate",
                    label="Create Product",
                    to="/business/products/create",
                    permission="business.products.add",
                )
            ],
        )
    ],
)

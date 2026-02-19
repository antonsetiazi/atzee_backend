# business/sales/pages/sales_direct_item_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="sales.direct.item.edit",
    entity="sales.direct.item",
    domain="business",
    path="/business/sales/direct/item/:id/edit",
    title="Direct Sales Detail",
    permissions=["business.sales.update"],
    blocks=[
        FormBlock(
            mode="create",
            submit_to="/business/transactions/{parent_id}/items/{id}/",
            method="PATCH",
            title="Edit Item",
            description="Perbarui data item",
            redirect_to={
                "page": "sales.direct.detail",
                "param": "id",        # ambil dari response.id
            },
            fields=[
                Field(
                    key="product_id",
                    label="Product",
                    type="select",
                    required=True,
                    data_source={
                        "type": "entity",
                        "domain": "business",
                        "entity": "products.list",
                        "query": {
                            "filters": {"is_active": True},
                            "fields": ["id", "code", "name"],
                        },
                        "map": {
                            "value": "id",
                            "label": "{code} - {name}",
                        },
                    },
                ),
                Field(
                    key="quantity",
                    label="Quantity",
                    type="text",
                    required=True,
                ),
                Field(
                    key="unit_price",
                    label="Unit Price",
                    type="text",
                    required=True,
                ),
                Field(
                    key="notes",
                    label="Notes",
                    type="textarea",
                ),
            ],
            actions=[
                Action(type="submit", label="Save"),
                Action(
                    type="redirect",
                    label="Cancel",
                    to="/business/sales.direct/{id}",
                ),
            ],
        )
    ],
)

register_ui_module_pages("business", UI_PAGES)
# business/inventory/ui/pages/inventory_lot_create.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="inventory.lot.create",
    entity="inventory.lot",
    domain="business",
    path="/business/inventory-lot/create",
    title="Create Inventory Lot",
    permissions=["business.inventory.create"],
    blocks=[
        FormBlock(
            mode="create",
            submit_to="/api/inventory/lots/",
            fields=[
                Field(
                    key="product",
                    label="Product",
                    type="select",
                    required=True,
                    data_source="product"
                ),
                Field(
                    key="lot_number",
                    label="Lot / Batch Number",
                    type="text",
                    required=True
                ),
                Field(
                    key="expiry_date",
                    label="Expiry Date",
                    type="date",
                    required=True
                ),
                Field(
                    key="quantity",
                    label="Initial Quantity",
                    type="number",
                    required=True
                ),
            ],
            actions=[
                Action(type="submit", label="Save"),
                Action(type="navigate", label="Cancel", to="inventory.lot.list")
            ]
        )
    ]
)

register_ui_module_pages("business", UI_PAGES)
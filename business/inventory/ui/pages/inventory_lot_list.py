# business/inventory/ui/pages/inventory_lot_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="inventory.lot.list",
    entity="inventory.lot",
    domain="business",
    path="/business/inventory-lot",
    title="Inventory Lots",
    permissions=["business.inventory.view"],
    blocks=[
        TableBlock(
            title="Inventory Lots",
            data_source="inventory.lot",
            columns=[
                TableColumn(
                    key="lot_number",
                    label="Lot / Batch",
                ),
                TableColumn(
                    key="product_name",
                    label="Product",
                ),
                TableColumn(
                    key="expiry_date",
                    label="Expiry Date",
                ),
                TableColumn(
                    key="quantity",
                    label="Available Qty",
                ),
                TableColumn(
                    key="status",
                    label="Status",
                ),
            ],
            top_actions=[
                Action(
                    type="navigate",
                    label="Add Lot",
                    to="inventory.lot.create",
                    permission="business.inventory.create"
                )
            ],
            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    to="inventory.lot.edit",
                    permission="business.inventory.edit"
                )
            ]
        )
    ]
)

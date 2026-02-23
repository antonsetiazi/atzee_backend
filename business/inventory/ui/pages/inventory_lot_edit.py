# business/inventory/ui/pages/inventory_lot_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="inventory.lot.edit",
    entity="inventory.lot",
    domain="business",
    path="/business/inventory/lot/:id/edit",
    title="Edit Inventory Lot",
    permissions=["business.inventory.edit"],
    blocks=[
        FormBlock(
            mode="edit",
            submit_to="/api/inventory/lots/{id}/",
            method="PUT",
            fields=[
                Field(
                    key="expiry_date",
                    label="Expiry Date",
                    type="date",
                    required=True
                ),
            ],
            actions=[
                Action(type="submit", label="Update"),
                Action(type="navigate", label="Cancel", to="inventory.lot.list")
            ]
        )
    ]
)

register_ui_module_pages("business", UI_PAGES)
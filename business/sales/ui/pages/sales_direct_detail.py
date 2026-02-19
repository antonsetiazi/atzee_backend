# business/sales/ui/pages/sales_direct_detail.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    FormBlock, 
    TableBlock, 
    TableColumn,
    WorkflowBlock,
    WorkflowStatus
)
from core.ui.schema.field import Field
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="sales.direct.detail",
    entity="sales.direct",
    domain="business",
    path="/business/sales/direct/detail/:id",
    title="Direct Sales Detail",
    permissions=["business.sales.view"],
    description="Informasi Rincian Penjualan Langsung",
    blocks=[

        # ==================================================
        # WORKFLOW BLOCK (STATUS + ACTIONS)
        # ==================================================
        WorkflowBlock(
            status=WorkflowStatus(
                key="draft",
                label="Draft",
                color="gray",
            ),
            actions=[
                Action(
                    key="confirm",
                    type="submit",
                    label="Confirm",
                    permission="business.sales.confirm",
                    confirm={
                        "title": "Confirm Sales",
                        "message": "Are you sure you want to confirm this sales?",
                        "level": "warning",
                    },
                ),
                Action(
                    key="cancel",
                    type="submit",
                    label="Cancel",
                    permission="business.sales.cancel",
                    confirm={
                        "title": "Cancel Sales",
                        "message": "This action cannot be undone. Continue?",
                        "level": "danger",
                    },
                ),
            ],
        ),

        # ==================================================
        # Transaction Summary (READ ONLY)
        # ==================================================
        FormBlock(
            mode="view",
            submit_to="/business/transactions/{id}/",
            title="Transaction Information",
            description="Informasi utama transaksi penjualan langsung",
            fields=[
                Field(
                    key="reference",
                    label="Reference",
                    type="text",
                ),
                Field(
                    key="transaction_date",
                    label="Transaction Date",
                    type="date",
                ),
                Field(
                    key="status",
                    label="Status",
                    type="badge",
                ),
                Field(
                    key="notes",
                    label="Notes",
                    type="textarea",
                ),
            ],
            actions=[
                Action(
                    type="redirect",
                    label="Back to List",
                    to="/business/sales/direct",
                ),
            ],
        ),

        # ==================================================
        # Items Table
        # ==================================================
        TableBlock(
            title="Items",
            search_mode="client",
            description="Daftar produk dalam transaksi",
            data_source="/entities/business/sales.direct.items/query/",
            columns=[
                TableColumn(key="product_name", label="Product"),
                TableColumn(key="quantity", label="Qty"),
                TableColumn(key="unit_price", label="Unit Price"),
                TableColumn(key="total_price", label="Total"),
                TableColumn(key="notes", label="Notes"),
            ],
            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    icon="edit",
                    to="/business/sales.direct.item/{id}/edit?parent_id={parent_id}",
                    permission="business.sales.update"
                ),
                Action(
                    type="delete",
                    label="Delete",
                    icon="delete",
                    permission="business.sales.delete",
                    confirm={
                        "title": "Delete Item",
                        "message": "Are you sure you want to delete this item?",
                        "level": "danger",
                    },
                    endpoint="/business/transactions/{parent_id}/items/{id}/"
                ),
            ],
            top_actions=[
                Action(
                    type="navigate",
                    label="Add Item",
                    to="/business/sales.direct.item/create?parent_id={id}",
                    permission="business.sales.edit",
                )
            ],
        ),
    ],
)

register_ui_module_pages("business", UI_PAGES)
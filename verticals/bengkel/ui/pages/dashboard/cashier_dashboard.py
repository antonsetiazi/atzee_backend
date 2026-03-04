# verticals/bengkel/ui/pages/dashboard/cashier_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.bengkel.enum.permissions import BengkelPermission


UI_PAGES = [
    Page(
        key="bengkel.cashier.dashboard",
        entity="dashboard",
        domain="bengkel",
        path="/dashboard",
        title="Cashier Dashboard",
        permissions=[BengkelPermission.CASHIER_DASHBOARD_VIEW], 
        description="Invoice & Payment Control",
        data_source="/entities/bengkel/cashier.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Action",
                items=[
                    ShortcutItem(key="generate_invoice", label="Generate Invoice", icon="file-text", to="/finance/invoice/create"),
                    ShortcutItem(key="payment", label="Receive Payment", icon="credit-card", to="/finance/payment"),
                    ShortcutItem(key="closing", label="Daily Closing", icon="lock", to="/finance/closing"),
                ],
            ),

            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="today_invoice", title="Invoice Today", data_key="today_invoice"),
                    StatBlock(key="today_payment", title="Payment Received", data_key="today_payment"),
                    StatBlock(key="outstanding", title="Outstanding", data_key="outstanding"),
                ]
            ),

            ListViewBlock(
                title="Completed Work Orders (Ready to Bill)",
                data_key="completed_work_orders",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="work_order_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="total_amount"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[BengkelPermission.CASHIER_DASHBOARD_VIEW], 
            ),
        ],
    ),
]

register_ui_module_pages("bengkel", UI_PAGES)
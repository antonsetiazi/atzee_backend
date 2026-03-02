# verticals/pos/ui/pages/dashboard/cashier_dashboard.py

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

from verticals.pos.enum.permissions import PosPermission


UI_PAGES = [
    Page(
        key="pos.cashier.dashboard",
        entity="dashboard",
        domain="pos",
        path="/dashboard",
        title="Cashier Dashboard",
        permissions=[PosPermission.CASHIER_DASHBOARD_VIEW],
        description="Transaction & Shift Control Panel",
        data_source="/entities/pos/cashier.dashboard/query/",
        blocks=[

            # QUICK ACTION
            ShortcutBlock(
                title="Quick Action",
                items=[
                    ShortcutItem(key="new_sale", label="New Sale", icon="shopping-cart", to="/sales/cashier/create"),
                    ShortcutItem(key="held", label="Held Transactions", icon="pause-circle", to="/pos/sale/held"),
                    ShortcutItem(key="refund", label="Return / Refund", icon="rotate-ccw", to="/pos/refund"),
                    ShortcutItem(key="shift", label="My Shift", icon="clock", to="/pos/shift"),
                ],
            ),

            # KPI
            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="today_sales", title="Sales Today", data_key="today_sales"),
                    StatBlock(key="today_transactions", title="Transactions", data_key="today_transactions"),
                    StatBlock(key="total_items_sold", title="Items Sold", data_key="items_sold"),
                    StatBlock(key="my_shift_balance", title="Shift Balance", data_key="shift_balance"),
                ]
            ),

            # RECENT PERSONAL TRANSACTIONS
            ListViewBlock(
                title="My Recent Transactions",
                data_key="recent_transactions",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="receipt_number"),
                    subtitle=ListFieldSchema(key="total_amount"),
                    description=ListFieldSchema(key="payment_method"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[PosPermission.CASHIER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("pos", UI_PAGES)
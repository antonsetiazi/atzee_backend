# verticals/pos/ui/pages/sales/cashier_sales.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import TransactionBlock
from verticals.pos.enum.permissions import PosPermission


UI_PAGES = [
    Page(
        key="transactions.sales.cashier.create",
        entity="transactions",
        domain="pos",
        path="/sales/cashier/create",
        title="Sales POS",
        data_source="/entities/pos/cashier.sales/query/",
        permissions=[PosPermission.TRANSACTION_CASHIER_CREATE],
        blocks=[
            TransactionBlock(
                title="Cashier",
                submit_to="/business/transactions/",
                redirect_to={
                    "page": "transactions.detail",
                    "param": "id"
                },
                affects=[
                    "products.stock",
                    "customers.balance"
                ],
                refresh_cache=[
                    "transactions.list",
                    "dashboard.stats"
                ],
                config={
                    "transaction_type": "sales",
                    "subtype": "direct"
                }
            ),
        ]
    )
]

register_ui_module_pages("pos", UI_PAGES)
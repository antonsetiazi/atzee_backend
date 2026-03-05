# verticals/cbs/ui/pages/dashboard/teller_dashboard.py

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

from verticals.cbs.enum.permissions import CbsPermission


UI_PAGES = [
    Page(
        key="cbs.teller.dashboard",
        entity="dashboard",
        domain="cbs",
        path="/dashboard",
        title="Teller Dashboard",
        permissions=[CbsPermission.TELLER_DASHBOARD_VIEW],
        description="Transaction Control Panel",
        data_source="/entities/cbs/teller.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Transaction",
                items=[
                    ShortcutItem(key="deposit", label="Cash Deposit", icon="plus-circle", to="/transactions/deposit"),
                    ShortcutItem(key="withdrawal", label="Cash Withdrawal", icon="minus-circle", to="/transactions/withdrawal"),
                    ShortcutItem(key="transfer", label="Internal Transfer", icon="repeat", to="/transactions/transfer"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="today_transactions", title="Transactions Today", data_key="today_transactions"),
                    StatBlock(key="cash_balance", title="Cash Balance", data_key="cash_balance"),
                ]
            ),

            ListViewBlock(
                title="Recent Transactions",
                data_key="recent_transactions",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="reference_number"),
                    subtitle=ListFieldSchema(key="account_number"),
                    description=ListFieldSchema(key="amount"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[CbsPermission.TELLER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("cbs", UI_PAGES)
# accounting/ui/pages/ledger_account.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn

from accounting.enum.permissions import AccountingPermission


UI_PAGES = Page(
    key="accounting.ledger.account",
    entity="ledger",
    domain="accounting",

    path="/admin/finance/ledger",

    title="General Ledger",
    subtitle="Mutasi per akun",

    permissions=[
        AccountingPermission.ADMIN_ACCOUNT_VIEW
    ],

    data_source="/entities/accounting/accounting.ledger.account/query/",

    blocks=[
        TableBlock(
            title="Ledger Entries",
            data_key="items",

            columns=[
                TableColumn(key="date", label="Date"),
                TableColumn(key="reference", label="Reference"),
                TableColumn(key="description", label="Description"),
                TableColumn(key="account_code", label="Code"),
                TableColumn(key="account_name", label="Account"),
                TableColumn(key="debit", label="Debit", align="right"),
                TableColumn(key="credit", label="Credit", align="right"),
                TableColumn(key="balance", label="Balance", align="right"),
            ],
        )
    ],
)

register_ui_module_pages("accounting", UI_PAGES)
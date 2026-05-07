# accounting/ui/pages/journal_list.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn, ActionBlock
from core.ui.schema.action import Action

from accounting.enum.permissions import AccountingPermission


UI_PAGES = Page(
    key="accounting.journals.list",
    entity="journals",
    domain="accounting",

    path="/admin/finance/journals",

    title="Journal",
    subtitle="Riwayat transaksi keuangan",

    permissions=[
        AccountingPermission.JOURNAL_VIEW
    ],

    data_source="/entities/accounting/accounting.journals.list/query/",

    blocks=[
        TableBlock(
            title="Daftar Journal",
            data_key="items",

            columns=[
                TableColumn(key="date", label="Date"),
                TableColumn(key="reference", label="Reference"),
                TableColumn(key="description", label="Description"),
                TableColumn(key="total_debit", label="Debit", align="right"),
                TableColumn(key="total_credit", label="Credit", align="right"),
            ],

            actions=[
                Action(
                    type="navigate",
                    label="Detail",
                    icon="next",
                    to="/admin/finance/journals/{id}",
                    permission=AccountingPermission.JOURNAL_VIEW,
                )
            ],
        ),

        ActionBlock(
            actions=[
                Action(
                    type="navigate",
                    label="Tambah Journal",
                    icon="plus",
                    to="/admin/finance/journal",
                    permission=AccountingPermission.JOURNAL_CREATE,
                )
            ]
        ),
    ],
)

register_ui_module_pages("accounting", UI_PAGES)
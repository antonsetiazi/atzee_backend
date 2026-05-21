# accounting/ui/pages/journal_list.py

from accounting.enum.permissions import AccountingPermission
from core.ui.registry import register_ui_module_pages
from core.ui.schema.action import Action
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.page import Page

UI_PAGES = Page(
    key="accounting.journals.list",
    entity="journals",
    domain="accounting",
    path="/admin/finance/journals",
    title="Journal",
    subtitle="Riwayat transaksi keuangan",
    permissions=[AccountingPermission.JOURNAL_VIEW],
    data_source="/entities/accounting/accounting.journals.list/query/",
    actions=[
        Action(
            type="navigate",
            label="Add Journal",
            icon="plus",
            to="/admin/finance/journal",
            permission=AccountingPermission.JOURNAL_CREATE,
        )
    ],
    blocks=[
        TableBlock(
            title="Daftar Journal",
            data_key="items",
            on_row_click="/admin/finance/journals/{id}",
            columns=[
                TableColumn(
                    key="reference", label="Reference", weight="semibold"
                ),
                TableColumn(
                    key="date",
                    label="Date",
                    format="date",
                    size="xs",
                    text_style="muted",
                ),
                TableColumn(key="description", label="Description"),
                TableColumn(
                    key="total_debit",
                    label="Debit",
                    align="right",
                    format="currency",
                    weight="semibold",
                ),
                TableColumn(
                    key="total_credit",
                    label="Credit",
                    align="right",
                    format="currency",
                    weight="semibold",
                ),
            ],
        ),
    ],
)

register_ui_module_pages("accounting", UI_PAGES)

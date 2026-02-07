# accounting/ledger/ui/pages/_base_ledger_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn


def build_ledger_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    permissions: list[str],
):
    columns = [
        TableColumn(key="entry_date", label="Date"),
        TableColumn(key="account_code", label="Account Code"),
        TableColumn(key="account_name", label="Account Name"),
        TableColumn(key="debit", label="Debit", align="right"),
        TableColumn(key="credit", label="Credit", align="right"),
        TableColumn(key="journal_number", label="Journal"),
    ]

    return Page(
        key=key,
        entity="ledger_entry",
        domain=domain,
        path=path,
        title="Ledger",
        permissions=permissions,
        blocks=[
            TableBlock(
                data_source=data_source,
                search_mode="server",
                columns=columns,
                detail_as_state=False,
            )
        ]
    )

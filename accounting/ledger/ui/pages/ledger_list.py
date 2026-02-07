from accounting.ledger.ui.pages._base_ledger_list import (
    build_ledger_list_page,
)

UI_PAGES = build_ledger_list_page(
    key="ledger.list",
    domain="accounting",
    path="/accounting/ledger",
    data_source="/entities/accounting/ledger.list/query/",
    permissions=["accounting.ledger.view"],
)

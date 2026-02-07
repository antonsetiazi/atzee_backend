# accounting/journals/ui/pages/general_journal_list.py

from accounting.journals.ui.pages._base_general_journal_list import (
    build_general_journal_list_page,
)

UI_PAGES = build_general_journal_list_page(
    key="accounting.journals.general.list",
    domain="accounting",
    path="/accounting/journals/general",
    data_source="/entities/accounting/journals.general.list/query/",
    permissions=["accounting.journals.view"],
    create_path="/accounting/journals/general/create",
)

# accounting/journals/ui/pages/journal_list.py

from accounting.journals.ui.pages._base_journal_list import (
    build_journal_list_page,
)


UI_PAGES = build_journal_list_page(
    key="journals.list",
    domain="accounting",
    path="/accounting/journals",
    create_path="/accounting/journals/general/create",
    data_source="/entities/accounting/journals.list/query/",
    permissions=["accounting.journals.view"],
    detail_path="/accounting/journals/{id}",
)

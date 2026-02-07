# accounting/journals/ui/pages/general_journal_create.py

from accounting.journals.ui.pages._base_general_journal_form import (
    build_general_journal_form_page,
)

UI_PAGES = build_general_journal_form_page(
    key="accounting.journals.general.create",
    domain="accounting",
    path="/accounting/journals/general/create",
    submit_to="/accounting/journals/general/",
    method="POST",
    permissions=["accounting.journals.add"],
    title="Create General Journal",
    redirect_page="/accounting/journals/general",
)
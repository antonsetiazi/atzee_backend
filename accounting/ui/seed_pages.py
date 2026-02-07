# accounting/ui/seed_pages.py

from accounting.chart_of_accounts.ui.pages import UI_PAGES as COA_PAGES
from accounting.ledger.ui.pages import UI_PAGES as LEDGER_PAGES
from accounting.fiscal_period.ui.pages import UI_PAGES as FISCAL_PERIOD_PAGES
from accounting.journals.ui.pages import UI_PAGES as JOURNAL_PAGES

UI_PAGES = [
    *COA_PAGES,
    *LEDGER_PAGES,
    *FISCAL_PERIOD_PAGES,
    *JOURNAL_PAGES
]
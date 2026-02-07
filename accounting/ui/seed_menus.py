# accounting/ui/seed_menus.py

from accounting.chart_of_accounts.ui.menus import UI_MENUS as COA_MENUS
from accounting.financial_reports.ui.menus import UI_MENUS as REPORTS_MENUS
from accounting.fiscal_period.ui.menus import UI_MENUS as FISCAL_PERIOD_MENUS
from accounting.journals.ui.menus import UI_MENUS as JOURNALS_MENUS
from accounting.taxes.ui.menus import UI_MENUS as TAXES_MENUS
from accounting.ledger.ui.menus import UI_MENUS as LEDGER_MENUS

UI_MENUS = (
    COA_MENUS + 
    REPORTS_MENUS +
    FISCAL_PERIOD_MENUS + 
    JOURNALS_MENUS +
    TAXES_MENUS +
    LEDGER_MENUS
)

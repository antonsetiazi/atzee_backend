# accounting/ledger/ui/pages/__init__.py

from .fiscal_period_list import UI_PAGES as FISCAL_PERIOD_LIST_PAGE
from .fiscal_period_create import UI_PAGES as FISCAL_PERIOD_CREATE_PAGE
from .fiscal_period_edit import UI_PAGES as FISCAL_PERIOD_EDIT_PAGE


UI_PAGES = [
    FISCAL_PERIOD_LIST_PAGE,
    FISCAL_PERIOD_CREATE_PAGE,
    FISCAL_PERIOD_EDIT_PAGE
]
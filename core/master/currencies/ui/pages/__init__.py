# core/master/currencies/ui/pages/__init__.py

from .currency_list import UI_PAGES as CURRENCY_LIST_PAGE 
from .currency_create import UI_PAGES as CURRENCY_CREATE_PAGE
from .currency_edit import UI_PAGES as CURRENCY_EDIT_PAGE

UI_PAGES = [
    CURRENCY_LIST_PAGE,
    CURRENCY_CREATE_PAGE,
    CURRENCY_EDIT_PAGE,
]

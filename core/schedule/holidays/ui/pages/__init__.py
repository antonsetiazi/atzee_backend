# core/schedule/holidays/ui/pages/__init__.py

from .holiday_list import UI_PAGES as HOLIDAY_LIST_PAGE
from .holiday_create import UI_PAGES as HOLIDAY_CREATE_PAGE
from .holiday_edit import UI_PAGES as HOLIDAY_EDIT_PAGE

UI_PAGES = [
    HOLIDAY_LIST_PAGE,
    HOLIDAY_CREATE_PAGE,
    HOLIDAY_EDIT_PAGE,
]

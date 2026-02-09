# core/geo/timezones/ui/pages/__init__.py

from .timezone_list import UI_PAGES as TIMEZONE_LIST_PAGE
from .timezone_create import UI_PAGES as TIMEZONE_CREATE_PAGE
from .timezone_edit import UI_PAGES as TIMEZONE_EDIT_PAGE

UI_PAGES = [
    TIMEZONE_LIST_PAGE,
    TIMEZONE_CREATE_PAGE,
    TIMEZONE_EDIT_PAGE,
]

# core/schedule/shifts/ui/pages/__init__.py

from .shift_list import UI_PAGES as SHIFT_LIST_PAGE 
from .shift_create import UI_PAGES as SHIFT_CREATE_PAGE
from .shift_edit import UI_PAGES as SHIFT_EDIT_PAGE

UI_PAGES = [
    SHIFT_LIST_PAGE,
    SHIFT_CREATE_PAGE,
    SHIFT_EDIT_PAGE,
]

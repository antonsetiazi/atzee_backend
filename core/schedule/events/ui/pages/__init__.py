# core/schedule/events/ui/pages/__init__.py

from .event_list import UI_PAGES as EVENT_LIST_PAGE 
from .event_create import UI_PAGES as EVENT_CREATE_PAGE
from .event_edit import UI_PAGES as EVENT_EDIT_PAGE

UI_PAGES = [
    EVENT_LIST_PAGE,
    EVENT_CREATE_PAGE,
    EVENT_EDIT_PAGE,
]

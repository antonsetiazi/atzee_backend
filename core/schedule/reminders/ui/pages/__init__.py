# core/schedule/reminders/ui/pages/__init__.py

from .reminder_list import UI_PAGES as REMINDER_LIST_PAGE
from .reminder_create import UI_PAGES as REMINDER_CREATE_PAGE
from .reminder_edit import UI_PAGES as REMINDER_EDIT_PAGE

UI_PAGES = [
    REMINDER_LIST_PAGE, 
    REMINDER_CREATE_PAGE,
    REMINDER_EDIT_PAGE,
]

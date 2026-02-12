# core/schedule/ui/seed_pages.py

from core.schedule.events.ui.pages import UI_PAGES as EVENT_PAGES
from core.schedule.holidays.ui.pages import UI_PAGES as HOLIDAY_PAGES 
from core.schedule.shifts.ui.pages import UI_PAGES as SHIFT_PAGES

UI_PAGES = [
    *EVENT_PAGES,
    *HOLIDAY_PAGES,
    *SHIFT_PAGES
]

# core/schedule/ui/seed_pages.py

from core.schedule.events.ui.pages import UI_PAGES as EVENT_PAGES
from core.schedule.holidays.ui.pages import UI_PAGES as HOLIDAY_PAGES 
# from core.schedule.timezones.ui.pages import UI_PAGES as TIMEZONE_PAGES

UI_PAGES = [
    *EVENT_PAGES,
    *HOLIDAY_PAGES,
    # *TIMEZONE_PAGES
]

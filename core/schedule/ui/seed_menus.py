# core/schedule/ui/seed_menus.py

from core.schedule.ui.menus import UI_MENUS as SCHEDULE_MENUS
from core.schedule.events.ui.menus import UI_MENUS as EVENT_MENUS
from core.schedule.holidays.ui.menus import UI_MENUS as HOLIDAY_MENUS
from core.schedule.shifts.ui.menus import UI_MENUS as SHIFT_MENUS


UI_MENUS = (
    SCHEDULE_MENUS +
    EVENT_MENUS +
    HOLIDAY_MENUS +
    SHIFT_MENUS
)

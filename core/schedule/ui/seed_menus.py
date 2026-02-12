# core/schedule/ui/seed_menus.py

from core.schedule.ui.menus import UI_MENUS as SCHEDULE_MENUS
from core.schedule.events.ui.menus import UI_MENUS as EVENT_MENUS
# from core.schedule.regions.ui.menus import UI_MENUS as REGION_MENUS
# from core.schedule.timezones.ui.menus import UI_MENUS as TIMEZONE_MENUS


UI_MENUS = (
    SCHEDULE_MENUS +
    EVENT_MENUS
    # REGION_MENUS +
    # TIMEZONE_MENUS
)

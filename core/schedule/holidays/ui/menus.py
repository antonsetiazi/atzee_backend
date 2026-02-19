# core/schedule/holidays/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="holidays.list",
        parent="core.schedule",
        label="Holidays",
        icon="calendar-off",
        app="core",
        resource="schedule.holidays",
        action="view",
        route="/core/holidays",
        order=30,
    ),
]

register_ui_module_menus("core", UI_MENUS)

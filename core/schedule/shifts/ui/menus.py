# core/schedule/shifts/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="shifts.list",
        parent="core.schedule",
        label="Shifts",
        icon="clock",
        app="core",
        resource="schedule.shifts",
        action="view",
        route="/core/shifts",
        order=30,
    ),
]

register_ui_module_menus("core", UI_MENUS)

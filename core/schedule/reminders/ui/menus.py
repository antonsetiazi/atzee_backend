# core/schedule/reminders/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="reminders.list",
        parent="core.schedule",
        label="Reminders",
        icon="notification",
        app="core",
        resource="schedule.reminders",
        action="view",
        route="/core/reminders",
        order=30,
    ),
]

register_ui_module_menus("core", UI_MENUS)

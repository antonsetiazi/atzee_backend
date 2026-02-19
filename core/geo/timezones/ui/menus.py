# core/geo/timezones/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="timezones.list",
        parent="core.geo",
        label="Timezones",
        icon="clock",
        app="core",
        resource="timezones",
        action="view",
        route="/settings/geo/timezones",
        order=30,
    ),
]

register_ui_module_menus("core", UI_MENUS)

# core/master/locations/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="locations.list",
        parent="core.master",
        label="Locations",
        icon="ruler",
        app="core",
        resource="locations",
        action="view",
        route="/core/master/locations",
        order=20,
    ),
]

register_ui_module_menus("core", UI_MENUS)
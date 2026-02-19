# core/geo/countries/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="countries.list",
        parent="core.geo",
        label="Countries",
        icon="globe",
        app="core",
        resource="countries",
        action="view",
        route="/settings/geo/countries",
        order=10,
    ),
]

register_ui_module_menus("core", UI_MENUS)
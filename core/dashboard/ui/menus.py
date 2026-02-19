# core/geo/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="core.dashboard",
        label="Dashboard",
        app="core",
        resource="core",
        action="view",
        route="/dashboard",
        order=1,
    ),
]

register_ui_module_menus("core", UI_MENUS)
# core/org/departments/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="departments.list",
        parent="core.org",
        label="Department",
        icon="ruler",
        app="core",
        resource="departments",
        action="view",
        route="/core/org/departments",
        order=20,
    ),
]

register_ui_module_menus("core", UI_MENUS)
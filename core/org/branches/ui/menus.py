# core/org/branches/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="branches.list",
        parent="core.org",
        label="Branch",
        icon="building",
        app="core",
        resource="branches",
        action="view",
        route="/settings/org/branches",
        order=30,
    ),
]

register_ui_module_menus("core", UI_MENUS)
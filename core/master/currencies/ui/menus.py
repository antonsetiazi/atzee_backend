# core/master/currencies/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="currencies.list",
        parent="core.master",
        label="Currencies",
        icon="dollar",
        app="core",
        resource="currencies",
        action="view",
        route="/settings/master/currencies",
        order=30,
    ),
]

register_ui_module_menus("core", UI_MENUS)
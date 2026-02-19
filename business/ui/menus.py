# business/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="business",
        label="Business",
        app="business",
        resource="business",
        action="view",
        route="/business",
        order=10,
    ),
]

register_ui_module_menus("business", UI_MENUS)
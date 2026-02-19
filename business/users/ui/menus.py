# business/users/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="users.list",
        parent="business",
        label="Users",
        icon="users",
        app="business",
        resource="users",
        action="view",
        route="/business/users",
        order=20,
    ),
]

register_ui_module_menus("business", UI_MENUS)
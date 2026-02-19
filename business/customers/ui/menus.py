# business/customers/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="customers.list",
        parent="business",
        label="Customers",
        icon="user-check",
        app="business",
        resource="customers",
        action="view",
        route="/business/customers",
        order=10,
    ),
]

register_ui_module_menus("business", UI_MENUS)
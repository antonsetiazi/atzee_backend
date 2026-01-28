# business/customers/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="customers.list",
        label="Customers",
        icon="user-check",
        app="business",
        resource="customers",
        action="view",
        route="/customers",
        order=10,
    ),
]

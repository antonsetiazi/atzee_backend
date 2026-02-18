# business/users/ui/menus.py

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

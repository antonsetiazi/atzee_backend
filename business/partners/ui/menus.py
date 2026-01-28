# business/partners/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="partners.list",
        label="Partners",
        icon="users",
        app="business",
        resource="partners",
        action="view",
        route="/partners",
        order=30,
    ),
]


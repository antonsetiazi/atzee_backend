# business/partners/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="partners.list",
        parent="business",
        label="Partners",
        icon="users",
        app="business",
        resource="partners",
        action="view",
        route="/business/partners",
        order=30,
    ),
]


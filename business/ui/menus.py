# business/ui/menus.py

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

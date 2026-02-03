# hr/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="hr",
        label="HR",
        app="hr",
        resource="hr",
        action="view",
        route="/hr",
        order=10,
    ),
]

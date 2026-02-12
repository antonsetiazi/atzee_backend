# core/schedule/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="core.schedule",
        label="Schedule",
        app="core",
        resource="core",
        action="view",
        route="/core/schedule",
        order=10,
    ),
]

# core/org/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="core.org",
        label="Organization",
        app="core",
        resource="core",
        action="view",
        route="/core",
        order=10,
    ),
]

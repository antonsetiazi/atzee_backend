# core/geo/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="core.dashboard",
        label="Dashboardssss",
        app="core",
        resource="core",
        action="view",
        route="/dashboard",
        order=1,
    ),
]

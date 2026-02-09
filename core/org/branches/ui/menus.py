# core/org/branches/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="branches.list",
        parent="core.org",
        label="Branch",
        icon="building",
        app="core",
        resource="branches",
        action="view",
        route="/settings/org/branches",
        order=30,
    ),
]

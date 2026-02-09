# core/master/currencies/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="currencies.list",
        parent="core.master",
        label="Currencies",
        icon="dollar",
        app="core",
        resource="currencies",
        action="view",
        route="/settings/master/currencies",
        order=30,
    ),
]

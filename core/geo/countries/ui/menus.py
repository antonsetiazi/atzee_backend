# core/geo/countries/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="countries.list",
        parent="core.geo",
        label="Countries",
        icon="globe",
        app="core",
        resource="countries",
        action="view",
        route="/settings/geo/countries",
        order=10,
    ),
]

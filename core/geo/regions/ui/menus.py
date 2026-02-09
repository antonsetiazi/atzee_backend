# core/geo/regions/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="regions.list",
        parent="core.geo",
        label="Regions",
        icon="map",
        app="core",
        resource="regions",
        action="view",
        route="/settings/geo/regions",
        order=20,
    ),
]

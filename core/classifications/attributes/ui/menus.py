# core/classifications/attributes/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="attributes.list",
        parent="core.classifications",
        label="Attributes",
        icon="sliders",
        app="core",
        resource="attributes",
        action="view",
        route="/settings/classifications/attributes",
        order=40,
    ),
]

# core/classifications/labels/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="labels.list",
        parent="core.classifications",
        label="Labels",
        icon="label",
        app="core",
        resource="labels",
        action="view",
        route="/settings/classifications/labels",
        order=40,
    ),
]

# hr/assets/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="assets.list",
        parent="hr",
        label="Assets",
        icon="archive",
        app="hr",
        resource="assets",
        action="view",
        route="/hr/assets",
        order=40,
    ),
]

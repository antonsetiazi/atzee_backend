# hr/assets/ui/menus.py

from core.ui.registry import register_ui_module_menus
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

register_ui_module_menus("hr", UI_MENUS)

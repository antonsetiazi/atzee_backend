# core/master/uom/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="uom.list",
        parent="core.master",
        label="Unit of Measure",
        icon="ruler",
        app="core",
        resource="uom",
        action="view",
        route="/core/master/uom",
        order=20,
    ),
]

register_ui_module_menus("core", UI_MENUS)
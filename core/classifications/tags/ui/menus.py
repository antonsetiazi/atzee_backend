# core/classifications/tags/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="tags.list",
        parent="core.classifications",
        label="Tags",
        icon="tag",
        app="core",
        resource="tags",
        action="view",
        route="/settings/classifications/tags",
        order=40,
    ),
]

register_ui_module_menus("core", UI_MENUS)

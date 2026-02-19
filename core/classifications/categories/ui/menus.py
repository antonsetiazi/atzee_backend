# core/classifications/categories/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="categories.list",
        parent="core.classifications",
        label="Categories",
        icon="tag",
        app="core",
        resource="categories",
        action="view",
        route="/settings/classifications/categories",
        order=30,
    ),
]

register_ui_module_menus("core", UI_MENUS)
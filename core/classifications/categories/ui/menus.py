# core/classifications/categories/ui/menus.py

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

# business/products/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="products.list",
        parent="business",
        label="Products",
        icon="package",
        app="business",
        resource="products",
        action="view",
        route="/business/products",
        order=20,
    ),
]

register_ui_module_menus("business", UI_MENUS)
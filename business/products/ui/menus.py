# business/products/ui/seed_menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="products.list",
        label="Products",
        icon="package",
        app="business",
        resource="products",
        action="view",
        route="/products",
        order=20,
    ),
]

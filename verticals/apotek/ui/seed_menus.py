# verticals/apotek/ui/seed_menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="apotek.root",
        label="Apotek",
        app="apotek",
        resource="apotek",
        action="view",
        route="/apotek",
        order=10,
    ),
    Menu(
        key="apotek.customers.list",
        parent="apotek.root",
        label="Customers",
        icon="user-check",
        app="apotek",
        resource="customers",
        action="view",
        route="/apotek/customers",
        order=20,
    ),
    Menu(
        key="apotek.products.list",
        parent="apotek.root",
        label="Products",
        icon="package",
        app="apotek",
        resource="products",
        action="view",
        route="/apotek/products",
        order=30,
    ),
]

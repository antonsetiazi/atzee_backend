# business/sales/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="sales",
        label="Sales",
        icon="shopping-cart",
        app="business",
        resource="business",
        action="view",
        route="/business",
        order=20,
    ),
    Menu(
        key="sales.direct.list",
        parent="sales",
        label="Direct Sales",
        icon="zap",
        app="business",
        resource="transactions",
        action="create",
        route="/business/sales/direct",
        order=10,
    ),
    Menu(
        key="sales.order.list",
        parent="sales",
        label="Sales Orders",
        icon="file-text",
        app="business",
        resource="transactions",
        action="create",
        route="/sales/orders",
        order=20,
    ),
    Menu(
        key="sales.manufacture.list",
        parent="sales",
        label="Manufacturing Sales",
        icon="factory",
        app="business",
        resource="transactions",
        action="create",
        route="/sales/manufacture",
        order=30,
    ),
]

register_ui_module_menus("business", UI_MENUS)

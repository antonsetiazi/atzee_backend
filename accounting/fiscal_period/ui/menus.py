# accounting/fiscal_period/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="fiscal_period.list",
        parent="accounting",
        label="Fiscal Periods",
        icon="calendar",
        app="accounting",
        resource="fiscal_period",
        action="view",
        route="/accounting/fiscal-periods",
        order=40,
    ),
]

register_ui_module_menus("accounting", UI_MENUS)
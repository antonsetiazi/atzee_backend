# hr/payroll/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="payroll.list",
        parent="hr",
        label="Payroll",
        icon="credit-card",
        app="hr",
        resource="payroll",
        action="view",
        route="/hr/payroll",
        order=30,
    ),
]

register_ui_module_menus("hr", UI_MENUS)

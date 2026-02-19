# accounting/chart_of_accounts/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="chart_of_accounts.list",
        parent="accounting",
        label="Chart of Accounts",
        icon="book",
        app="accounting",
        resource="chart_of_accounts",
        action="view",
        route="/accounting/chart-of-accounts",
        order=10,
    ),
]

register_ui_module_menus("accounting", UI_MENUS)
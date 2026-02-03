# accounting/fiscal_period/ui/menus.py

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

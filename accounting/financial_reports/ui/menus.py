# accounting/financial_reports/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="financial_reports.list",
        parent="accounting",
        label="Financial Reports",
        icon="bar-chart-2",
        app="accounting",
        resource="financial_reports",
        action="view",
        route="/accounting/reports",
        order=60,
    ),
]

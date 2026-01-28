# accounting/taxes/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="taxes.list",
        label="Taxes",
        icon="percent",
        app="accounting",
        resource="taxes",
        action="view",
        route="/accounting/taxes",
        order=50,
    ),
]

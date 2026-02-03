# accounting/ledger/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="ledger.list",
        parent="accounting",
        label="Ledger",
        icon="grid",
        app="accounting",
        resource="ledger",
        action="view",
        route="/accounting/ledger",
        order=30,
    ),
]

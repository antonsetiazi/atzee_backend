# accounting/ledger/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="ledger.list",
        parent="accounting",
        label="Ledger",
        icon="book-open",
        app="accounting",
        resource="ledger",
        action="view",
        route="/accounting/ledger",
        order=10,
    ),
]

register_ui_module_menus("accounting", UI_MENUS)

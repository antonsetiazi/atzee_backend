# accounting/taxes/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="taxes.list",
        parent="accounting",
        label="Taxes",
        icon="percent",
        app="accounting",
        resource="taxes",
        action="view",
        route="/accounting/taxes",
        order=50,
    ),
]

register_ui_module_menus("accounting", UI_MENUS)
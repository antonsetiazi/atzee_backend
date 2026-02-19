# accounting/journals/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="journals.list",
        parent="accounting",
        label="Journals",
        icon="file-text",
        app="accounting",
        resource="journals",
        action="view",
        route="/accounting/journals",
        order=20,
    ),
]

register_ui_module_menus("accounting", UI_MENUS)
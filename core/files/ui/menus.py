# core/files/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="files.list",
        parent="system",
        label="Files",
        icon="paperclip",
        app="core",
        resource="files",
        action="view",
        route="/core/files",
        order=90,
    ),
]

register_ui_module_menus("core", UI_MENUS)
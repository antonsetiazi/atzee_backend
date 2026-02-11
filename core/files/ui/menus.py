# core/files/ui/menus.py

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

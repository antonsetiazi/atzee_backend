# accounting/journals/ui/menus.py

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

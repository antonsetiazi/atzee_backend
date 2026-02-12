# core/schedule/recurrings/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="recurrings.list",
        parent="core.schedule",
        label="Recurrings",
        icon="repeat",
        app="core",
        resource="schedule.recurrings",
        action="view",
        route="/core/recurrings",
        order=40,
    ),
]

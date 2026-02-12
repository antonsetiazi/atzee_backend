# core/schedule/events/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="events.list",
        parent="core.schedule",
        label="Events",
        icon="calendar",
        app="core",
        resource="schedule.events",
        action="view",
        route="/core/events",
        order=20,
    ),
]

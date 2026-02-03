# hr/attendance/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="attendance.list",
        parent="hr",
        label="Attendance",
        icon="clock",
        app="hr",
        resource="attendance",
        action="view",
        route="/hr/attendance",
        order=20,
    ),
]

# hr/employees/ui/menus.py

from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="employees.list",
        parent="hr",
        label="Employees",
        icon="user",
        app="hr",
        resource="employees",
        action="view",
        route="/hr/employees",
        order=10,
    ),
]

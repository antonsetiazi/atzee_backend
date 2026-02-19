# hr/employees/ui/menus.py

from core.ui.registry import register_ui_module_menus
from core.ui.schema.menu import Menu

UI_MENUS = [
    Menu(
        key="hr",
        label="HR",
        app="hr",
        resource="hr",
        action="view",
        route="/hr",
        order=10,
    ),

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

register_ui_module_menus("hr", UI_MENUS)
# hr/ui/seed_menus.py

from hr.ui.menus import UI_MENUS as HR_MENUS
from hr.employees.ui.menus import UI_MENUS as EMPLOYEES_MENUS
from hr.attendance.ui.menus import UI_MENUS as ATTENDANCE_MENUS
from hr.payroll.ui.menus import UI_MENUS as PAYROLL_MENUS
from hr.assets.ui.menus import UI_MENUS as ASSETS_MENUS

UI_MENUS = (
    HR_MENUS +
    EMPLOYEES_MENUS +
    ATTENDANCE_MENUS +
    PAYROLL_MENUS +
    ASSETS_MENUS
)

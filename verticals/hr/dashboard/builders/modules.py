# verticals/hr/dashboard/builders/modules.py

from verticals.hr.dashboard.constants import modules


def build_modules():
    return [
        modules.dashboard,
        modules.employees,
        modules.attendance,
        modules.leave,
        modules.payroll,
    ]

# verticals/hrms/ui/pages/dashboard/employee_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock, StatBlock,
    ShortcutBlock, ShortcutItem,
    ListViewBlock, ListFieldSchema, ListTileSchema,
)

from verticals.hrms.enum.permissions import HrmsPermission


UI_PAGES = [
    Page(
        key="hrms.employee.dashboard",
        entity="dashboard",
        domain="hrms",
        path="/portal/dashboard",
        title="My HR Dashboard",
        permissions=[HrmsPermission.EMPLOYEE_DASHBOARD_VIEW], 
        description="Employee Self-Service Portal",
        data_source="/entities/hrms/employee.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="My HR",
                items=[
                    ShortcutItem(key="profile", label="My Profile", icon="user", to="/portal/profile"),
                    ShortcutItem(key="apply_leave", label="Apply Leave", icon="calendar", to="/portal/leave/apply"),
                    ShortcutItem(key="attendance", label="My Attendance", icon="clock", to="/portal/attendance"),
                    ShortcutItem(key="payroll_slip", label="My Payroll Slip", icon="file-text", to="/portal/payroll"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="leave_balance", title="Leave Balance", data_key="leave_balance"),
                    StatBlock(key="attendance_this_month", title="Attendance This Month", data_key="attendance_this_month"),
                ]
            ),

            ListViewBlock(
                title="My Recent Requests",
                data_key="my_recent_requests",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="request_type"),
                    subtitle=ListFieldSchema(key="date"),
                    description=ListFieldSchema(key="details"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[HrmsPermission.EMPLOYEE_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("hrms", UI_PAGES)
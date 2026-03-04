# verticals/hrms/ui/pages/dashboard/officer_dashboard.py

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
        key="hrms.officer.dashboard",
        entity="dashboard",
        domain="hrms",
        path="/dashboard",
        title="HR Officer Dashboard",
        permissions=[HrmsPermission.OFFICER_DASHBOARD_VIEW],
        description="Daily HR Operations",
        data_source="/entities/hrms/officer.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Operational Tasks",
                items=[
                    ShortcutItem(key="employees", label="Employees", icon="users", to="/hrms/employees"),
                    ShortcutItem(key="attendance", label="Attendance Records", icon="clock", to="/hrms/attendance"),
                    ShortcutItem(key="leave", label="Leave Requests", icon="calendar", to="/hrms/leave"),
                    ShortcutItem(key="payroll_process", label="Payroll Processing", icon="credit-card", to="/hrms/payroll/process"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="today_attendance", title="Today's Attendance", data_key="today_attendance"),
                    StatBlock(key="leave_requests", title="Pending Leave", data_key="leave_requests"),
                    StatBlock(key="overtime_requests", title="Overtime Requests", data_key="overtime_requests"),
                ]
            ),

            ListViewBlock(
                title="Recent Leave Requests",
                data_key="recent_leave_requests",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="employee_name"),
                    subtitle=ListFieldSchema(key="leave_type"),
                    description=ListFieldSchema(key="date_range"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[HrmsPermission.OFFICER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("hrms", UI_PAGES)
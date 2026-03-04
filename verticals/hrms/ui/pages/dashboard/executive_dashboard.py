# verticals/hrms/ui/pages/dashboard/executive_dashboard.py

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
        key="hrms.executive.dashboard",
        entity="dashboard",
        domain="hrms",
        path="/dashboard/executive",
        title="Executive HR Dashboard",
        permissions=[HrmsPermission.EXECUTIVE_DASHBOARD_VIEW],
        description="Workforce & Payroll Insight",
        data_source="/entities/hrms/executive.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Executive Overview",
                items=[
                    ShortcutItem(key="workforce", label="Workforce Overview", icon="users", to="/hrms/reports/workforce"),
                    ShortcutItem(key="payroll_summary", label="Payroll Summary", icon="credit-card", to="/hrms/reports/payroll"),
                    ShortcutItem(key="attendance_stats", label="Attendance Statistics", icon="clock", to="/hrms/reports/attendance"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="total_employees", title="Total Employees", data_key="total_employees"),
                    StatBlock(key="total_payroll", title="Total Payroll", data_key="total_payroll"),
                    StatBlock(key="avg_attendance_rate", title="Attendance Rate", data_key="attendance_rate", suffix="%"),
                ]
            ),

            ListViewBlock(
                title="Performance Summary",
                data_key="performance_summary",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="department"),
                    subtitle=ListFieldSchema(key="avg_score"),
                    description=ListFieldSchema(key="review_period"),
                ),
                permissions=[HrmsPermission.EXECUTIVE_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("hrms", UI_PAGES)
# verticals/hrms/ui/pages/dashboard/line_manager_dashboard.py

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
        key="hrms.manager.dashboard",
        entity="dashboard",
        domain="hrms",
        path="/dashboard/line-manager",
        title="Team Dashboard",
        permissions=[HrmsPermission.LINE_MANAGER_DASHBOARD_VIEW], 
        description="Team Overview & Approvals",
        data_source="/entities/hrms/manager.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Team Management",
                items=[
                    ShortcutItem(key="team_members", label="Team Members", icon="users", to="/hrms/team"),
                    ShortcutItem(key="leave_approval", label="Leave Approval", icon="check-circle", to="/hrms/approvals/leave"),
                    ShortcutItem(key="overtime_approval", label="Overtime Approval", icon="clock", to="/hrms/approvals/overtime"),
                    ShortcutItem(key="performance_review", label="Performance Review", icon="target", to="/hrms/performance/review"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="team_size", title="Team Size", data_key="team_size"),
                    StatBlock(key="pending_approval", title="Pending Approvals", data_key="pending_approval"),
                    StatBlock(key="team_attendance_rate", title="Attendance Rate", data_key="team_attendance_rate", suffix="%"),
                ]
            ),

            ListViewBlock(
                title="Pending Team Approvals",
                data_key="team_pending_approvals",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="employee_name"),
                    subtitle=ListFieldSchema(key="request_type"),
                    description=ListFieldSchema(key="date_range"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[HrmsPermission.LINE_MANAGER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("hrms", UI_PAGES)
# verticals/hrms/ui/pages/dashboard/admin_dashboard.py

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
        key="hrms.admin.dashboard",
        entity="dashboard",
        domain="hrms",
        path="/dashboard/hr-admin",
        title="HR Administrator Dashboard",
        permissions=[HrmsPermission.ADMIN_DASHBOARD_VIEW], 
        description="Full HR System Control Panel",
        data_source="/entities/hrms/admin.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="HR Configuration",
                items=[
                    ShortcutItem(key="org_structure", label="Organization Structure", icon="git-branch", to="/hrms/organization"),
                    ShortcutItem(key="employees", label="Employees", icon="users", to="/hrms/employees"),
                    ShortcutItem(key="payroll_setup", label="Payroll Setup", icon="settings", to="/hrms/payroll/components"),
                    ShortcutItem(key="performance", label="Performance Setup", icon="target", to="/hrms/performance/templates"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="total_employees", title="Total Employees", data_key="total_employees"),
                    StatBlock(key="active_contracts", title="Active Contracts", data_key="active_contracts"),
                    StatBlock(key="pending_leave", title="Pending Leave Requests", data_key="pending_leave"),
                    StatBlock(key="pending_payroll", title="Pending Payroll Period", data_key="pending_payroll"),
                ]
            ),

            ListViewBlock(
                title="Recent HR Activities",
                data_key="recent_hr_activity",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="activity_type"),
                    subtitle=ListFieldSchema(key="employee_name"),
                    description=ListFieldSchema(key="date"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[HrmsPermission.ADMIN_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("hrms", UI_PAGES)
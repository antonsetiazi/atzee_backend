# verticals/hrms/ui/pages/dashboard/finance_dashboard.py

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
        key="hrms.finance.dashboard",
        entity="dashboard",
        domain="hrms",
        path="/dashboard",
        title="Payroll Dashboard",
        permissions=[HrmsPermission.FINANCE_DASHBOARD_VIEW],
        description="Payroll & Journal Processing",
        data_source="/entities/hrms/finance.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Payroll Management",
                items=[
                    ShortcutItem(key="payroll_period", label="Payroll Period", icon="calendar", to="/hrms/payroll/period"),
                    ShortcutItem(key="generate_payroll", label="Generate Payroll", icon="play-circle", to="/hrms/payroll/generate"),
                    ShortcutItem(key="journal_posting", label="Journal Posting", icon="book", to="/hrms/payroll/journal"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="total_payroll", title="Total Payroll This Period", data_key="total_payroll"),
                    StatBlock(key="pending_approval", title="Pending Payroll Approval", data_key="pending_approval"),
                ]
            ),

            ListViewBlock(
                title="Recent Payroll Runs",
                data_key="recent_payroll_runs",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="period"),
                    subtitle=ListFieldSchema(key="total_amount"),
                    description=ListFieldSchema(key="generated_date"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[HrmsPermission.FINANCE_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("hrms", UI_PAGES)
# verticals/cbs/ui/pages/dashboard/branch_manager_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.cbs.enum.permissions import CbsPermission


UI_PAGES = [
    Page(
        key="cbs.branch_manager.dashboard",
        entity="dashboard",
        domain="cbs",
        path="/dashboard",
        title="Branch Manager Dashboard",
        permissions=[CbsPermission.BRANCH_MANAGER_DASHBOARD_VIEW],
        description="Branch Performance Overview",
        data_source="/entities/cbs/branch_manager.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Branch Control",
                items=[
                    ShortcutItem(key="customers", label="Branch Customers", icon="users", to="/customers"),
                    ShortcutItem(key="accounts", label="Open Account", icon="plus-circle", to="/accounts/create"),
                    ShortcutItem(key="loans", label="Loan Applications", icon="file-text", to="/loans/applications"),
                    ShortcutItem(key="closing", label="Daily Closing", icon="clock", to="/closing/daily"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="branch_deposits", title="Total Deposits", data_key="branch_deposits"),
                    StatBlock(key="branch_loans", title="Total Loans", data_key="branch_loans"),
                    StatBlock(key="cash_position", title="Cash Position", data_key="cash_position"),
                ]
            ),

            ListViewBlock(
                title="Pending Approvals",
                data_key="pending_approvals",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="reference_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="amount"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[CbsPermission.BRANCH_MANAGER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("cbs", UI_PAGES)
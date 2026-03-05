# verticals/cbs/ui/pages/dashboard/credit_officer_dashboard.py

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
        key="cbs.credit_officer.dashboard",
        entity="dashboard",
        domain="cbs",
        path="/dashboard",
        title="Credit Officer Dashboard",
        permissions=[CbsPermission.CREDIT_OFFICER_DASHBOARD_VIEW],
        description="Loan & Risk Control Panel",
        data_source="/entities/cbs/credit_officer.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Loan Actions",
                items=[
                    ShortcutItem(key="new_application", label="New Loan", icon="plus", to="/loans/create"),
                    ShortcutItem(key="pipeline", label="Loan Pipeline", icon="git-branch", to="/loans/pipeline"),
                    ShortcutItem(key="collateral", label="Collateral", icon="shield", to="/loans/collateral"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="pending_loans", title="Pending Loans", data_key="pending_loans"),
                    StatBlock(key="approved_loans", title="Approved Loans", data_key="approved_loans"),
                    StatBlock(key="npl_count", title="NPL Accounts", data_key="npl_count"),
                ]
            ),

            ListViewBlock(
                title="Loan Applications",
                data_key="loan_applications",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="application_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="requested_amount"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[CbsPermission.CREDIT_OFFICER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("cbs", UI_PAGES)
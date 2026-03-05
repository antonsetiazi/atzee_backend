# verticals/cbs/ui/pages/dashboard/director_dashboard.py

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
        key="cbs.director.dashboard",
        entity="dashboard",
        domain="cbs",
        path="/dashboard",
        title="Director Dashboard",
        permissions=[CbsPermission.DIRECTOR_DASHBOARD_VIEW],
        description="Executive Banking Overview",
        data_source="/entities/cbs/director.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Strategic Menu",
                items=[
                    ShortcutItem(key="financials", label="Financial Statement", icon="bar-chart", to="/reports/financial"),
                    ShortcutItem(key="liquidity", label="Liquidity Overview", icon="activity", to="/treasury/liquidity"),
                    ShortcutItem(key="loan_portfolio", label="Loan Portfolio", icon="credit-card", to="/loans/portfolio"),
                    ShortcutItem(key="risk", label="Risk Exposure", icon="alert-triangle", to="/compliance/risk"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="total_assets", title="Total Assets", data_key="total_assets"),
                    StatBlock(key="total_deposits", title="Total Deposits", data_key="total_deposits"),
                    StatBlock(key="total_loans", title="Total Loans", data_key="total_loans"),
                    StatBlock(key="npl_ratio", title="NPL Ratio", data_key="npl_ratio", suffix="%"),
                ]
            ),

            ListViewBlock(
                title="High Risk Accounts",
                data_key="high_risk_accounts",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="account_number"),
                    subtitle=ListFieldSchema(key="customer_name"),
                    description=ListFieldSchema(key="risk_score"),
                    status=ListFieldSchema(key="risk_level"),
                ),
                permissions=[CbsPermission.DIRECTOR_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("cbs", UI_PAGES)
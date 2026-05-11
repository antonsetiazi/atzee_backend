# verticals/finance/ui/pages/dahsboard/admin_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.block import (
    BannerBlock,
    HeaderBlock,
    ShortcutBlock,
    ShortcutItem,
)
from core.ui.schema.page import Page
from verticals.finance.enum.permissions import FinancePermission

UI_PAGES = [
    Page(
        key="finance.admin.dashboard",
        entity="dashboard",
        domain="finance",
        path="/dashboard",
        title="Admin Dashboard",
        permissions=[FinancePermission.ADMIN_DASHBOARD_VIEW],
        meta={
            "showBottomNav": True,
            "showHeader": False,
            "fullscreen": False,
            "headerMode": "overlay",
        },
        description="Finance Control Room & Accounting Overview Platform Atzee Finance",
        data_source="/entities/finance/admin.dashboard/query/",
        blocks=[
            # ===============================
            # 🔥 HEADER DASHBOARD
            # ===============================
            HeaderBlock(
                title="FINANCE CONTROL CENTER",
                subtitle="Accounting & Cashflow Monitoring",
                variant="dashboard",
                show_greeting=True,
                show_avatar=True,
                show_search=True,
            ),
            # =====================================================
            # GLOBAL ALERT / ANOMALY SYSTEM
            # =====================================================
            BannerBlock(
                title="Financial Alerts",
                data_key="alerts",
                size="lg",
            ),
            ShortcutBlock(
                title="Quick Navigation",
                bordered=False,
                items=[
                    ShortcutItem(
                        key="users",
                        label="User Management",
                        icon="users",
                        to="/admin/users",
                    ),
                    ShortcutItem(
                        key="accounts",
                        label="Chart of Account",
                        icon="coa",
                        to="/admin/finance/accounts",
                    ),
                    ShortcutItem(
                        key="journal",
                        label="Journal",
                        icon="booking",
                        to="/admin/finance/journals",
                    ),
                    ShortcutItem(
                        key="ledger",
                        label="Ledger",
                        icon="ledger",
                        to="/admin/finance/ledger",
                    ),
                ],
                scrollable=False,
            ),
            ShortcutBlock(
                title="Quick Navigation",
                bordered=False,
                items=[
                    ShortcutItem(
                        key="trial-balance",
                        label="Trial Balance",
                        icon="report",
                        to="/admin/finance/reports/trial-balance",
                    ),
                    ShortcutItem(
                        key="profit-loss",
                        label="Profit & Loss",
                        icon="report",
                        to="/admin/finance/reports/profit-loss",
                    ),
                    ShortcutItem(
                        key="balance-sheet",
                        label="Balance Sheet",
                        icon="report",
                        to="/admin/finance/reports/balance-sheet",
                    ),
                    ShortcutItem(
                        key="cash-flow",
                        label="Cash Flow",
                        icon="report",
                        to="/admin/finance/reports/cash-flow",
                    ),
                ],
                scrollable=False,
            ),
            ShortcutBlock(
                title="Receivable",
                bordered=False,
                items=[
                    ShortcutItem(
                        key="ar-dashboard",
                        label="AR Dashboard",
                        icon="dashboard",
                        to="/finance/receivables/dashboard",
                    ),
                    ShortcutItem(
                        key="ar-invoice",
                        label="AR Invoice",
                        icon="invoice",
                        to="/finance/receivables/invoices",
                    ),
                    ShortcutItem(
                        key="ar-payment",
                        label="AR Payment",
                        icon="payment",
                        to="/finance/receivables/payments",
                    ),
                ],
                scrollable=False,
            ),
            ShortcutBlock(
                title="Payable",
                bordered=False,
                items=[
                    ShortcutItem(
                        key="ap-dashboard",
                        label="AP Dashboard",
                        icon="dashboard",
                        to="/finance/payables/dashboard",
                    ),
                    ShortcutItem(
                        key="ap-invoice",
                        label="AP Invoice",
                        icon="invoice",
                        to="/finance/payables/invoices",
                    ),
                    ShortcutItem(
                        key="ap-payment",
                        label="AP Payment",
                        icon="payment",
                        to="/finance/payables/payments",
                    ),
                ],
                scrollable=False,
            ),
            ShortcutBlock(
                title="Fixed Assets",
                bordered=False,
                items=[
                    ShortcutItem(
                        key="fa-dashboard",
                        label="Fixed Asset Dashboard",
                        icon="dashboard",
                        to="/finance/fixed-assets/dashboard",
                    ),
                    ShortcutItem(
                        key="fa-list",
                        label="Daftar Asset",
                        icon="asset",
                        to="/finance/fixed-assets/",
                    ),
                    ShortcutItem(
                        key="fa-categories",
                        label="FA Categories",
                        icon="categories",
                        to="/finance/fixed-assets/categories",
                    ),
                ],
                scrollable=False,
            ),
            ShortcutBlock(
                title="Fixed Assets",
                bordered=False,
                items=[
                    ShortcutItem(
                        key="fa-depreciation",
                        label="FA Depreciation",
                        icon="depreciation",
                        to="/finance/fixed-assets/depreciation",
                    ),
                    ShortcutItem(
                        key="fa-disposals",
                        label="FA Disposals",
                        icon="disposals",
                        to="/finance/fixed-assets/disposals",
                    ),
                ],
                scrollable=False,
            ),
            ShortcutBlock(
                title="Quick Navigation",
                bordered=False,
                items=[
                    ShortcutItem(
                        key="payments",
                        label="Payments",
                        icon="credit-card",
                        to="/admin/payment-transactions",
                    ),
                    ShortcutItem(
                        key="wallet",
                        label="Wallet",
                        icon="credit-card",
                        to="/admin/wallet-transactions",
                    ),
                    ShortcutItem(
                        key="withdrawals",
                        label="Withdrawals",
                        icon="credit-card",
                        to="/admin/withdrawals",
                    ),
                    ShortcutItem(
                        key="reviews",
                        label="Reviews",
                        icon="notification",
                        to="/admin/reviews",
                    ),
                ],
                scrollable=False,
            ),
            ShortcutBlock(
                title="Quick Navigation",
                bordered=False,
                items=[
                    ShortcutItem(
                        key="banners",
                        label="Banner",
                        icon="tool",
                        to="/admin/widgets/banners",
                    ),
                    ShortcutItem(
                        key="banks",
                        label="Master Banks",
                        icon="book",
                        to="/admin/master/banks",
                    ),
                    ShortcutItem(
                        key="branding",
                        label="Branding",
                        icon="profile",
                        to="/admin/settings/branding",
                    ),
                    ShortcutItem(
                        key="policies",
                        label="Policies",
                        icon="policy",
                        to="/admin/legal/policies",
                    ),
                ],
                scrollable=False,
            ),
        ],
    ),
]


register_ui_module_pages("finance", UI_PAGES)

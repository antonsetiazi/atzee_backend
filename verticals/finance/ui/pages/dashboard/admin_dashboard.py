# verticals/finance/ui/pages/dahsboard/admin_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
    BannerBlock,
    HeaderBlock,
)

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


            # =====================================================
            # KPI ROW 2 (FINANCIAL MONITORING)
            # =====================================================
            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(
                        key="platform_revenue",
                        title="Revenue Platform (Bulan Ini)",
                        data_key="platform_revenue",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="pending_payment",
                        title="Pending Payment",
                        data_key="pending_payment",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="pending_payout",
                        title="Pending Payout",
                        data_key="pending_payout",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="escrow_balance",
                        title="Escrow Balance",
                        data_key="escrow_balance",
                        size="sm",
                        value=None,
                    ),
                ]
            ),

            ShortcutBlock(
                title="Quick Navigation",
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

            # =====================================================
            # KPI ROW 1 (REAL-TIME CORE HEALTH)
            # =====================================================
            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(
                        key="today_bookings",
                        title="Booking Hari Ini",
                        data_key="today_bookings",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="active_bookings",
                        title="Booking Aktif",
                        data_key="active_bookings",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="completed_today",
                        title="Selesai Hari Ini",
                        data_key="completed_today",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="cancelled_today",
                        title="Batal Hari Ini",
                        data_key="cancelled_today",
                        size="sm",
                        value=None,
                    ),
                ]
            ), 

            ShortcutBlock(
                title="Quick Navigation",
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

            # =====================================================
            # KPI ROW 3 (PARTNER HEALTH)
            # =====================================================
            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(
                        key="active_partners",
                        title="Ustadz Aktif Hari Ini",
                        data_key="active_partners",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="pending_verification",
                        title="Pending Verification",
                        data_key="pending_verification",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="flagged_reviews",
                        title="Flagged Reviews",
                        data_key="flagged_reviews",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="open_disputes",
                        title="Open Disputes",
                        data_key="open_disputes",
                        size="sm",
                        value=None,
                    ),
                ]
            ),
        ],
    ),
]


register_ui_module_pages("finance", UI_PAGES)
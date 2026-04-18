# verticals/ustadzku/ui/pages/dahsboard/admin_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
    BannerBlock,
    ListFieldSchema,
    ListViewBlock,
    ListTileSchema,
)

from business.enum.permissions import BusinessPermission
from verticals.ustadzku.enum.permissions import UstadzkuPermission


UI_PAGES = [
    Page(
        key="ustadzku.admin.dashboard",
        entity="dashboard",
        domain="ustadzku",
        path="/dashboard",
        title="Admin Dashboard",
        permissions=[UstadzkuPermission.ADMIN_DASHBOARD_VIEW], 
        description="Control Room & Monitoring Global Platform Ustadzku",
        data_source="/entities/ustadzku/admin.dashboard/query/",
        blocks=[

            # =====================================================
            # GLOBAL ALERT / ANOMALY SYSTEM
            # =====================================================
            BannerBlock(
                title="System Alerts & Anomalies",
                data_key="alerts",
                size="lg",
            ),

            # =====================================================
            # QUICK ACTION (SUPERVISOR SHORTCUT)
            # =====================================================
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
                        key="partners",
                        label="Ustadz Management",
                        icon="shield",
                        to="/admin/partners",
                    ),
                    ShortcutItem(
                        key="bookings",
                        label="Bookings",
                        icon="booking",
                        to="/admin/bookings",
                    ),
                    ShortcutItem(
                        key="orders",
                        label="Orders",
                        icon="archive",
                        to="/admin/orders",
                    ),
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
                    ShortcutItem(
                        key="widgets",
                        label="Widgets",
                        icon="tool",
                        to="/admin/widgets",
                    ),
                    ShortcutItem(
                        key="banks",
                        label="Master Banks",
                        icon="book",
                        to="/admin/master/banks",
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


register_ui_module_pages("ustadzku", UI_PAGES)
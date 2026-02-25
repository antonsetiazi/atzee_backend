# verticals/ustadzku/dashboards/ui/pages/user_dashboard.py

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

UI_PAGES = [
    Page(
        key="ustadzku.user.dashboard",
        entity="dashboard",
        domain="ustadzku",
        path="/dashboard",
        title="Dashboard",
        permissions=["ustadzku.user.dashboard.view"],
        description="Ringkasan aktivitas dan booking Anda",
        data_source="/entities/ustadzku/user.dashboard/query/",
        blocks=[

            # ===============================
            # Banner / Notifikasi Penting
            # ===============================
            BannerBlock(
                title="Informasi Penting",
                data_key="banners",
                size="lg",
            ),

            # ===============================
            # Shortcut: Cari Ustadz
            # ===============================
            ShortcutBlock(
                title="Aksi Cepat",
                items=[
                    ShortcutItem(
                        key="search_ustadz",
                        label="Cari Ustadz",
                        icon="search",
                        to="/business/partners/search",
                    ),
                    ShortcutItem(
                        key="my_bookings",
                        label="Riwayat Booking",
                        icon="calendar",
                        to="/business/my-bookings",
                    ),
                    ShortcutItem(
                        key="transactions",
                        label="Transaksi",
                        icon="credit-card",
                        to="/ustadzku/transactions",
                    ),
                    ShortcutItem(
                        key="wallet",
                        label="Wallet",
                        icon="wallet",
                        to="/core/wallet",
                    ),
                ],
                scrollable=False,
            ),

            # ===============================
            # STAT SUMMARY
            # ===============================
            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(
                        key="upcoming_booking",
                        title="Booking Mendatang",
                        data_key="upcoming_booking",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="active_booking",
                        title="Booking Aktif",
                        data_key="active_booking",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="completed_booking",
                        title="Selesai",
                        data_key="completed_booking",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="total_booking",
                        title="Total Booking",
                        data_key="total_booking",
                        size="sm",
                        value=None,
                    ),
                ]
            ),

            # ======================================
            # UPCOMING LIST
            # ======================================
            ListViewBlock(
                title="Booking Mendatang",
                data_key="upcoming_bookings",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="booking_number"),
                    subtitle=ListFieldSchema(key="partner_name"),
                    description=ListFieldSchema(key="start_time", format="date"),
                    status=ListFieldSchema(key="status"),
                ),
                layout="standard",
                permissions=["business.bookings.view"],
            ),

            # ===============================
            # RIWAYAT TERAKHIR
            # ===============================
            ListViewBlock(
                title="Riwayat Terakhir",
                data_key="recent_bookings",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="booking_number"),
                    subtitle=ListFieldSchema(key="partner_name"),
                    description=ListFieldSchema(key="start_time", format="date"),
                    status=ListFieldSchema(key="status"),
                ),
                layout="standard",
                permissions=["business.bookings.view"],
            )
        ],
    ),
]

register_ui_module_pages("ustadzku", UI_PAGES)
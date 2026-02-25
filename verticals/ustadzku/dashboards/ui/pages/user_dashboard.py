# verticals/ustadzku/dashboards/ui/pages/user_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
    BannerBlock,
    TableBlock,
    TableColumn,
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
        blocks=[

            # ===============================
            # Banner / Notifikasi Penting
            # ===============================
            BannerBlock(
                title="Informasi Penting",
                data_source="/entities/core/widgets.banner.dashboard/query/",
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
            # STAT RINGKAS
            # ===============================
            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(
                        key="upcoming_booking",
                        title="Booking Mendatang",
                        value="--",
                        size="sm",
                        meta={
                            "data_source": "/entities/business/user.bookings.upcoming.count/query/"
                        }
                    ),
                    StatBlock(
                        key="active_booking",
                        title="Booking Aktif",
                        value="--",
                        size="sm",
                        meta={
                            "data_source": "/entities/business/user.bookings.active.count/query/"
                        }
                    ),
                    StatBlock(
                        key="total_history",
                        title="Total Booking",
                        value="--",
                        size="sm",
                        meta={
                            "data_source": "/entities/business/user.bookings.total.count/query/"
                        }
                    ),
                ]
            ),

            # ===============================
            # UPCOMING BOOKING TABLE
            # ===============================
            TableBlock(
                title="Booking Mendatang",
                data_source="/entities/business/user.bookings.upcoming/query/",
                search_mode="server",
                columns=[
                    TableColumn(key="booking_code", label="Kode"),
                    TableColumn(key="ustadz_name", label="Ustadz"),
                    TableColumn(key="schedule_date", label="Tanggal", format="date"),
                    TableColumn(key="status", label="Status"),
                ],
                detail_as_state=True,
            ),

            # ===============================
            # RIWAYAT TERAKHIR
            # ===============================
            TableBlock(
                title="Riwayat Terakhir",
                data_source="/entities/business/user.bookings.recent/query/",
                search_mode="server",
                columns=[
                    TableColumn(key="booking_code", label="Kode"),
                    TableColumn(key="ustadz_name", label="Ustadz"),
                    TableColumn(key="schedule_date", label="Tanggal", format="date"),
                    TableColumn(key="status", label="Status"),
                ],
                query={"limit": 5},
                detail_as_state=True,
            ),
        ],
    ),
]

register_ui_module_pages("ustadzku", UI_PAGES)
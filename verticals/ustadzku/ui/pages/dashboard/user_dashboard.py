# verticals/ustadzku/ui/pages/dashboard/user_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    HeaderBlock,
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
    BannerBlock,
    ListFieldSchema,
    ListViewBlock,
    CategorySliderBlock,
    ListingSectionBlock,
)

from business.enum.permissions import BusinessPermission
from verticals.ustadzku.enum.permissions import UstadzkuPermission

UI_PAGES = [
    Page(
        key="ustadzku.user.dashboard",
        entity="dashboard",
        domain="ustadzku",
        path="/dashboard",
        title="Dashboard",
        permissions=[UstadzkuPermission.USER_DASHBOARD_VIEW],
        meta={
            "showBottomNav": True,
            "showHeader": False,
            "fullscreen": False,
            "headerMode": "overlay",            
        },
        description="Ringkasan aktivitas dan booking Anda",
        data_source="/entities/ustadzku/user.dashboard/query/",
        blocks=[

            # ===============================
            # 🔥 HEADER DASHBOARD
            # ===============================
            HeaderBlock(
                title="HOME",
                subtitle="Platform Booking Ustadz",
                variant="dashboard",
                show_greeting=True,
                show_avatar=True,
                show_search=True,
            ),

            # ===============================
            # Banner / Notifikasi Penting
            # ===============================
            BannerBlock(
                title="Informasi Penting",
                data_key="banners",
                size="lg",
                padding="md",
                margin_bottom="lg",
            ),

            CategorySliderBlock(
                title="Kategori Layanan",
                scope="partners.service_category",
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
                        to="/services",
                    ),
                    ShortcutItem(
                        key="my_bookings",
                        label="Riwayat Booking",
                        icon="calendar",
                        to="/bookings",
                    ),
                    ShortcutItem(
                        key="transactions",
                        label="Order",
                        icon="credit-card",
                        to="/orders",
                    ),
                    ShortcutItem(
                        key="wallet",
                        label="Wallet",
                        icon="wallet",
                        to="/wallet",
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
                        title="Booking Selesai",
                        data_key="completed_booking",
                        size="sm",
                        value=None,
                    ),
                ]
            ),         

            ListingSectionBlock(
                title="Ustadz Terdekat",
                section_type="nearby_services",
                limit=4,
            ),

            ListingSectionBlock(
                title="Paling Populer",
                section_type="popular_services",
                limit=4,
            ),

            ListingSectionBlock(
                title="Terbaru",
                section_type="new_services",
                limit=4,
            ),

            ListingSectionBlock(
                title="Rekomendasi",
                section_type="recommended_services",
                limit=4,
            ),

            ListingSectionBlock(
                title="Top Rated",
                section_type="top_rated_services",
                limit=4,
            ),

            ListingSectionBlock(
                title="Paling Terjangkau",
                section_type="cheap_services",
                limit=4,
            ),
        ],
    ),
]

register_ui_module_pages("ustadzku", UI_PAGES)
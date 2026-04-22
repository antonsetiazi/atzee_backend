# verticals/ustadzku/ui/pages/dashboard/partner_dashboard.py

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
    HeaderBlock,
)

from business.enum.permissions import BusinessPermission
from verticals.ustadzku.enum.permissions import UstadzkuPermission

UI_PAGES = [
    Page(
        key="ustadzku.partner.dashboard",
        entity="dashboard",
        domain="ustadzku",
        path="/dashboard",
        title="Dashboard Mitra",
        permissions=[UstadzkuPermission.PARTNER_DASHBOARD_VIEW],
        meta={
            "showBottomNav": True,
            "showHeader": False,
            "fullscreen": False,
            "headerMode": "overlay",            
        },
        description="Ringkasan aktivitas, booking masuk, dan performa Anda sebagai Mitra",
        data_source="/entities/ustadzku/partner.dashboard/query/",
        blocks=[

            HeaderBlock(
                title="PARTNER USTADZKU",
                subtitle="Dashboard Management Partner",
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
            ),

            # ===============================
            # Shortcut: Aksi Cepat Mitra
            # ===============================
            ShortcutBlock(
                title="Aksi Cepat",
                items=[
                    ShortcutItem(
                        key="partner_profile",
                        label="Profil Partner",
                        icon="user",
                        to="/partner/profile",
                    ),
                    ShortcutItem(
                        key="partner_products",
                        label="Produk Layanan",
                        icon="box",
                        to="/partner/products",
                    ),
                    ShortcutItem(
                        key="incoming_bookings",
                        label="Booking Masuk",
                        icon="inbox",
                        to="/business/partner/bookings/schedule",
                    ),
                    ShortcutItem(
                        key="my_schedule",
                        label="Jadwal & Kalender",
                        icon="calendar",
                        to="/partner/schedule",
                    ),
                ],
                scrollable=False,
            ),

            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(
                        key="total_earnings",
                        title="Total Pendapatan (Bulan Ini)",
                        data_key="total_earnings",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="average_rating",
                        title="Rating Rata-Rata",
                        data_key="average_rating",
                        size="sm",
                        value=None,
                    ),
                ]
            ),

            ShortcutBlock(
                title="Aksi Cepat",
                items=[
                    ShortcutItem(
                        key="active_services",
                        label="Layanan Aktif",
                        icon="map-pin",
                        to="/verticals/ustadzku/tracking/active",
                    ),
                    ShortcutItem(
                        key="earnings",
                        label="Pendapatan",
                        icon="dollar-sign",
                        to="/business/payments/overview",
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
                        key="today_bookings",
                        title="Booking Hari Ini",
                        data_key="today_bookings",
                        size="sm",
                        value=None,
                    ),
                    StatBlock(
                        key="upcoming_bookings",
                        title="Booking Mendatang",
                        data_key="upcoming_bookings_count",
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
                ]
            ),           
        ],
    ),
]

register_ui_module_pages("ustadzku", UI_PAGES)
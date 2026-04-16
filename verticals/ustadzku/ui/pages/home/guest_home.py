# verticals/ustadzku/ui/pages/home/guest_home.py

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
        key="ustadzku.guest.home",
        entity="home",
        domain="ustadzku",
        path="/",
        title="Home",
        permissions=[UstadzkuPermission.GUEST_HOME_VIEW],
        meta={
            "showBottomNav": True,
            "showHeader": False,
            "fullscreen": False,
            "headerMode": "overlay",            
        },
        description="Selamat datang di aplikasi USTADZKU",
        data_source="/entities/ustadzku/guest.home/query/",
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
                        to="/business/guest/bookings/schedule",
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
        ],
    ),
]

register_ui_module_pages("ustadzku", UI_PAGES)
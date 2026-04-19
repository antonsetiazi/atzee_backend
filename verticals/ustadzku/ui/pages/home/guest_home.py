# verticals/ustadzku/ui/pages/home/guest_home.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    HeaderBlock,
    ShortcutBlock,
    ShortcutItem,
    BannerBlock,
    ListFieldSchema,
    ListViewBlock,
    CategorySliderBlock,
    ListingSectionBlock
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
            # 🔥 HEADER DASHBOARD
            # ===============================
            HeaderBlock(
                title="HOME",
                subtitle="Platform Booking Ustadz",
                variant="dashboard",
                show_greeting=False,
                show_avatar=False,
                show_search=False,
            ),

            # ===============================
            # Banner / Notifikasi Penting
            # ===============================
            BannerBlock(
                title="Informasi Penting",
                data_key="banners",
                size="lg",
            ),

            CategorySliderBlock(
                title="Kategori Layanan",
                scope="partners.service_category",
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
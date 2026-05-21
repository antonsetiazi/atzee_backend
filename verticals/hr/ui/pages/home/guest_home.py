# verticals/hr/ui/pages/home/guest_home.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.block import (
    BannerBlock,
    HeaderBlock,
)
from core.ui.schema.page import Page
from verticals.hr.enum.permissions import HrPermission

UI_PAGES = [
    Page(
        key="hr.guest.home",
        entity="home",
        domain="hr",
        path="/",
        title="Home",
        permissions=[HrPermission.GUEST_HOME_VIEW],
        meta={
            "showBottomNav": True,
            "showHeader": False,
            "fullscreen": False,
            "headerMode": "overlay",
        },
        description="Selamat datang di aplikasi HR",
        data_source="/entities/hr/guest.home/query/",
        blocks=[
            # ===============================
            # 🔥 HEADER DASHBOARD
            # ===============================
            HeaderBlock(
                title="HR",
                subtitle="Human Resource Monitoring",
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
        ],
    ),
]

register_ui_module_pages("hr", UI_PAGES)

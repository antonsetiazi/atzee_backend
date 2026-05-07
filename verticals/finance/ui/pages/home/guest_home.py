# verticals/finance/ui/pages/home/guest_home.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    HeaderBlock,
    BannerBlock,
)

from verticals.finance.enum.permissions import FinancePermission

UI_PAGES = [
    Page(
        key="finance.guest.home",
        entity="home",
        domain="finance",
        path="/",
        title="Home",
        permissions=[FinancePermission.GUEST_HOME_VIEW],
        meta={
            "showBottomNav": True,
            "showHeader": False,
            "fullscreen": False,
            "headerMode": "overlay",            
        },
        description="Selamat datang di aplikasi FINANCE",
        data_source="/entities/finance/guest.home/query/",
        blocks=[

            # ===============================
            # 🔥 HEADER DASHBOARD
            # ===============================
            HeaderBlock(
                title="FINANCE",
                subtitle="Accounting & Cashflow Monitoring",
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

register_ui_module_pages("finance", UI_PAGES)
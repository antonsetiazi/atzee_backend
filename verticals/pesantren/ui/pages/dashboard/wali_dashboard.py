# verticals/pesantren/ui/pages/dashboard/wali_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ShortcutBlock,
    ShortcutItem,
    StatBlock,
    ContainerBlock,
)

from verticals.pesantren.enum.permissions import PesantrenPermission


UI_PAGES = [
    Page(
        key="pesantren.wali.dashboard",
        entity="dashboard",
        domain="pesantren",
        path="/dashboard",
        title="Dashboard Anak",
        permissions=[PesantrenPermission.WALI_DASHBOARD_VIEW], 
        description="Monitoring Perkembangan Anak",
        data_source="/entities/pesantren/wali.dashboard/query/",
        blocks=[

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="hafalan", title="Progres Hafalan", data_key="hafalan_progress", suffix="%"),
                    StatBlock(key="absensi", title="Kehadiran", data_key="attendance_percentage", suffix="%"),
                ],
            ),

            ShortcutBlock(
                title="Monitoring",
                items=[
                    ShortcutItem(key="nilai", label="Nilai", icon="book", to="/nilai"),
                    ShortcutItem(key="tagihan", label="Tagihan", icon="wallet", to="/tagihan"),
                    ShortcutItem(key="izin", label="Ajukan Izin", icon="log-out", to="/izin"),
                ],
            ),
        ],
    ),
]

register_ui_module_pages("pesantren", UI_PAGES)
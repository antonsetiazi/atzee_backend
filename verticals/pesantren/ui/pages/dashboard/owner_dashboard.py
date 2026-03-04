# verticals/pesantren/ui/pages/dashboard/owner_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
    ChartBlock,
    ListViewBlock,
    ListFieldSchema,
    ListTileSchema,
)

from verticals.pesantren.enum.permissions import PesantrenPermission
 

UI_PAGES = [
    Page(
        key="pesantren.owner.dashboard",
        entity="dashboard",
        domain="pesantren",
        path="/dashboard",
        title="Owner Dashboard",
        permissions=[PesantrenPermission.OWNER_DASHBOARD_VIEW], 
        description="Global Overview Pesantren",
        data_source="/entities/pesantren/owner.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Access",
                items=[
                    ShortcutItem(key="santri", label="Data Santri", icon="users", to="/santri"),
                    ShortcutItem(key="keuangan", label="Keuangan", icon="wallet", to="/keuangan"),
                    ShortcutItem(key="tahfidz", label="Tahfidz", icon="book-open", to="/tahfidz"),
                    ShortcutItem(key="asset", label="Asset & Wakaf", icon="home", to="/asset"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="total_santri", title="Total Santri", data_key="total_santri"),
                    StatBlock(key="active_santri", title="Santri Aktif", data_key="active_santri"),
                    StatBlock(key="monthly_income", title="Income Bulan Ini", data_key="monthly_income"),
                    StatBlock(key="hafidz_progress", title="Progres Tahfidz", data_key="hafidz_progress", suffix="%"),
                ],
            ),

            ChartBlock(
                key="financial_chart",
                title="Grafik Keuangan",
                data_key="financial_chart",
            ),

            ListViewBlock(
                title="Laporan Kehadiran Terbaru",
                data_key="recent_attendance",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="santri_name"),
                    subtitle=ListFieldSchema(key="date"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[PesantrenPermission.OWNER_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("pesantren", UI_PAGES)
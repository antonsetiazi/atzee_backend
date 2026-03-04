# verticals/pesantren/ui/pages/dashboard/musyrif_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
    ListViewBlock,
    ListTileSchema,
    ListFieldSchema,
)

from verticals.pesantren.enum.permissions import PesantrenPermission


UI_PAGES = [
    Page(
        key="pesantren.musyrif.dashboard",
        entity="dashboard",
        domain="pesantren",
        path="/dashboard",
        title="Dashboard Asrama",
        permissions=[PesantrenPermission.MUSYRIF_DASHBOARD_VIEW], 
        description="Monitoring Asrama & Disiplin",
        data_source="/entities/pesantren/musyrif.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Asrama",
                items=[
                    ShortcutItem(key="absensi", label="Absensi Asrama", icon="check-square", to="/asrama/absensi"),
                    ShortcutItem(key="pelanggaran", label="Pelanggaran", icon="alert-triangle", to="/disiplin"),
                    ShortcutItem(key="izin", label="Izin Keluar", icon="log-out", to="/perizinan"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="santri_asrama", title="Santri Asrama", data_key="santri_count"),
                    StatBlock(key="pelanggaran_bulan", title="Pelanggaran Bulan Ini", data_key="violation_count"),
                ],
            ),

            ListViewBlock(
                title="Izin Keluar Pending",
                data_key="pending_permission",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="santri_name"),
                    subtitle=ListFieldSchema(key="reason"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[PesantrenPermission.MUSYRIF_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("pesantren", UI_PAGES)
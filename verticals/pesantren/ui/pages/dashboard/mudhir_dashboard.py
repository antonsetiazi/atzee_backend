# verticals/pesantren/ui/pages/dashboard/mudhir_dashboard.py

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
        key="pesantren.mudhir.dashboard",
        entity="dashboard",
        domain="pesantren",
        path="/dashboard",
        title="Mudhir Dashboard",
        permissions=[PesantrenPermission.MUDHIR_DASHBOARD_VIEW],
        description="Operasional & Monitoring", 
        data_source="/entities/pesantren/mudhir.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Operasional",
                items=[
                    ShortcutItem(key="santri", label="Data Santri", icon="users", to="/santri"),
                    ShortcutItem(key="akademik", label="Akademik", icon="book", to="/akademik"),
                    ShortcutItem(key="tahfidz", label="Tahfidz", icon="book-open", to="/tahfidz"),
                    ShortcutItem(key="disiplin", label="Disiplin", icon="shield", to="/disiplin"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="santri_total", title="Total Santri", data_key="total_santri"),
                    StatBlock(key="kelas_active", title="Kelas Aktif", data_key="active_classes"),
                    StatBlock(key="tahfidz_active", title="Halaqah Aktif", data_key="active_halaqah"),
                ],
            ),

            ListViewBlock(
                title="Pengajuan Menunggu Approval",
                data_key="pending_approvals",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="title"),
                    subtitle=ListFieldSchema(key="created_at"),
                    status=ListFieldSchema(key="status"),
                ),
                permissions=[PesantrenPermission.MUDHIR_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("pesantren", UI_PAGES)
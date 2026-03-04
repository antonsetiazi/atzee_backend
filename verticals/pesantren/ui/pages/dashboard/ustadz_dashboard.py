# verticals/pesantren/ui/pages/dashboard/ustadz_dashboard.py

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
        key="pesantren.ustadz.dashboard",
        entity="dashboard",
        domain="pesantren",
        path="/dashboard",
        title="Dashboard Mengajar",
        permissions=[PesantrenPermission.USTADZ_DASHBOARD_VIEW],
        description="Kontrol Pengajaran",
        data_source="/entities/pesantren/ustadz.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Aktivitas Mengajar",
                items=[
                    ShortcutItem(key="jadwal", label="Jadwal Mengajar", icon="calendar", to="/akademik/jadwal"),
                    ShortcutItem(key="absensi", label="Input Absensi", icon="check-square", to="/akademik/absensi"),
                    ShortcutItem(key="nilai", label="Input Nilai", icon="edit", to="/akademik/nilai"),
                ],
            ),

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="kelas_diampu", title="Kelas Diampu", data_key="classes_count"),
                    StatBlock(key="total_santri", title="Total Santri", data_key="students_count"),
                ],
            ),

            ListViewBlock(
                title="Jadwal Hari Ini",
                data_key="today_schedule",
                tile=ListTileSchema(
                    title=ListFieldSchema(key="subject"),
                    subtitle=ListFieldSchema(key="class_name"),
                    description=ListFieldSchema(key="time"),
                ),
                permissions=[PesantrenPermission.USTADZ_DASHBOARD_VIEW],
            ),
        ],
    ),
]

register_ui_module_pages("pesantren", UI_PAGES)
# verticals/pesantren/ui/pages/dashboard/santri_dashboard.py

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
        key="pesantren.santri.dashboard",
        entity="dashboard",
        domain="pesantren",
        path="/dashboard",
        title="Dashboard Santri",
        permissions=[PesantrenPermission.SANTRI_DASHBOARD_VIEW], 
        description="Self Service Portal",
        data_source="/entities/pesantren/santri.dashboard/query/",
        blocks=[

            ContainerBlock(
                direction="row",
                blocks=[
                    StatBlock(key="hafalan", title="Progres Hafalan", data_key="hafalan_progress", suffix="%"),
                    StatBlock(key="tabungan", title="Saldo Tabungan", data_key="saving_balance"),
                ],
            ),

            ShortcutBlock(
                title="Menu",
                items=[
                    ShortcutItem(key="jadwal", label="Jadwal", icon="calendar", to="/jadwal"),
                    ShortcutItem(key="nilai", label="Nilai", icon="book", to="/nilai"),
                    ShortcutItem(key="izin", label="Ajukan Izin", icon="log-out", to="/izin"),
                ],
            ),
        ],
    ),
]

register_ui_module_pages("pesantren", UI_PAGES)
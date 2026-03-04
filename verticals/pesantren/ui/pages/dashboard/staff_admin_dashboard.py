# verticals/pesantren/ui/pages/dashboard/staff_admin_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ShortcutBlock,
    ShortcutItem,
)

from verticals.pesantren.enum.permissions import PesantrenPermission


UI_PAGES = [
    Page(
        key="pesantren.staff_admin.dashboard",
        entity="dashboard",
        domain="pesantren",
        path="/dashboard",
        title="Dashboard Administrasi",
        permissions=[PesantrenPermission.STAFF_ADMIN_DASHBOARD_VIEW],
        description="Operasional Administrasi", 
        data_source="/entities/pesantren/staff_admin.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Administrasi",
                items=[
                    ShortcutItem(key="santri", label="Data Santri", icon="users", to="/santri"),
                    ShortcutItem(key="pendaftaran", label="Pendaftaran Baru", icon="user-plus", to="/santri/register"),
                    ShortcutItem(key="keuangan", label="Keuangan Santri", icon="wallet", to="/keuangan"),
                ],
            ),
        ],
    ),
]

register_ui_module_pages("pesantren", UI_PAGES)
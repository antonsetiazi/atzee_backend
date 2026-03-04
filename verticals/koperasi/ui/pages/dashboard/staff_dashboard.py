# verticals/koperasi/ui/pages/dashboard/staff_dashboard.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    StatBlock,
    ShortcutBlock,
    ShortcutItem,
)

from verticals.koperasi.enum.permissions import KoperasiPermission


UI_PAGES = [
    Page(
        key="koperasi.staff.dashboard",
        entity="dashboard",
        domain="koperasi",
        path="/dashboard",
        title="Staff Dashboard",
        permissions=[KoperasiPermission.STAFF_DASHBOARD_VIEW], 
        description="Daily Operational Input",
        data_source="/entities/koperasi/staff.dashboard/query/",
        blocks=[

            ShortcutBlock(
                title="Quick Input",
                items=[
                    ShortcutItem(key="add_member", label="Tambah Member", icon="user-plus", to="/members/create"),
                    ShortcutItem(key="input_savings", label="Input Simpanan", icon="plus", to="/savings/input"),
                    ShortcutItem(key="loan_request", label="Input Pengajuan", icon="file-text", to="/loans/request"),
                ],
            ),

            ContainerBlock(
                direction="row",
                gap=16,
                blocks=[
                    StatBlock(key="members_today", title="New Members Today", data_key="members_today"),
                    StatBlock(key="transactions_today", title="Transactions Today", data_key="transactions_today"),
                ]
            ),
        ],
    ),
]

register_ui_module_pages("koperasi", UI_PAGES)
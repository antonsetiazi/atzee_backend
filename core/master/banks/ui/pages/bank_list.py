# core/master/banks/ui/pages/bank_list.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn, ActionBlock
from core.ui.schema.action import Action

from core.enum.permissions import CorePermission


UI_PAGES = Page(
    key="core.master.banks.list",
    entity="banks",
    domain="core",

    path="/admin/master/banks",

    title="Master Bank",
    subtitle="Kelola daftar bank yang tersedia dalam sistem",

    permissions=[
        CorePermission.ADMIN_BANK_VIEW
    ],

    data_source="/entities/core/master.banks.list/query/",

    blocks=[
        TableBlock(
            title="Daftar Bank",
            data_key="items",
            search_mode="server",

            columns=[
                TableColumn(
                    key="code",
                    label="Kode",
                ),
                TableColumn(
                    key="name",
                    label="Nama Bank",
                ),
                TableColumn(
                    key="short_name",
                    label="Nama Singkat",
                ),
                TableColumn(
                    key="sort_order",
                    label="Urutan",
                    align="center",
                ),
                TableColumn(
                    key="is_active",
                    label="Status",
                    align="center",
                ),
                TableColumn(
                    key="created_at",
                    label="Dibuat",
                    format="datetime",
                ),
            ],

            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    icon="pencil",
                    to="/admin/master/banks/{id}",
                    permission=CorePermission.ADMIN_BANK_EDIT,
                )
            ],
        ),

        ActionBlock(
            title="",
            justify="center",
            align="center",

            actions=[
                Action(
                    type="navigate",
                    label="Tambah Bank",
                    icon="plus",
                    to="/admin/master/banks/create",
                    permission=CorePermission.ADMIN_BANK_CREATE,
                )
            ],
        ),
    ],
)

register_ui_module_pages("core", UI_PAGES)
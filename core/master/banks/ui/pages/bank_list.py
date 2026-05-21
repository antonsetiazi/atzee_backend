# core/master/banks/ui/pages/bank_list.py

from core.enum.permissions import CorePermission
from core.ui.registry import register_ui_module_pages
from core.ui.schema.action import Action
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.page import Page

UI_PAGES = Page(
    key="core.master.banks.list",
    entity="banks",
    domain="core",
    path="/admin/master/banks",
    title="Master Bank",
    subtitle="Kelola daftar bank yang tersedia dalam sistem",
    permissions=[CorePermission.ADMIN_BANK_VIEW],
    data_source="/entities/core/master.banks.list/query/",
    actions=[
        Action(
            type="navigate",
            label="Tambah Bank",
            icon="plus",
            to="/admin/master/banks/create",
            permission=CorePermission.ADMIN_BANK_CREATE,
        )
    ],
    blocks=[
        TableBlock(
            title="Daftar Bank",
            data_key="items",
            on_row_click="/admin/master/banks/{id}",
            search_mode="server",
            columns=[
                TableColumn(key="code", label="Kode", weight="semibold"),
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
                    boolean_style="active_inactive",
                    size="xs",
                    weight="semibold",
                ),
                TableColumn(
                    key="created_at",
                    label="Created At",
                    format="datetime",
                    size="xs",
                    text_style="muted",
                ),
            ],
        ),
    ],
)

register_ui_module_pages("core", UI_PAGES)

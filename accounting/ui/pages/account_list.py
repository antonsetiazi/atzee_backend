# accounting/ui/pages/account_list.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn, ActionBlock
from core.ui.schema.action import Action

from accounting.enum.permissions import AccountingPermission


UI_PAGES = Page(
    key="accounting.accounts.list",
    entity="accounts",
    domain="accounting",

    path="/admin/finance/accounts",

    title="Chart of Accounts",
    subtitle="Kelola daftar akun keuangan",

    permissions=[
        AccountingPermission.ADMIN_ACCOUNT_VIEW
    ],

    data_source="/entities/accounting/accounting.accounts.list/query/",

    blocks=[
        TableBlock(
            title="Daftar Akun",
            data_key="items",
            search_mode="server",

            columns=[
                TableColumn(key="code", label="Code"),
                TableColumn(key="name", label="Name"),
                TableColumn(key="account_type", label="Type"),
                TableColumn(key="parent_name", label="Parent"),
                TableColumn(key="is_group", label="Group", align="center"),
                TableColumn(key="is_active", label="Active", align="center"),
            ],

            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    icon="pencil",
                    to="/admin/finance/accounts/{id}",
                    permission=AccountingPermission.ADMIN_ACCOUNT_EDIT,
                ),
                Action(
                    type="delete",
                    label="Delete",
                    icon="trash",
                    permission=AccountingPermission.ADMIN_ACCOUNT_DELETE,
                    endpoint="/entities/accounting.accounts.delete/execute/",
                    confirm={
                        "title": "Hapus Account",
                        "message": "Yakin ingin menghapus akun ini?",
                        "level": "danger",
                    },
                    refresh_cache=[
                        "accounting.accounts.list"
                    ],
                ),
            ],
        ),

        ActionBlock(
            actions=[
                Action(
                    type="navigate",
                    label="Tambah Account",
                    icon="plus",
                    to="/admin/finance/accounts/create",
                    permission=AccountingPermission.ADMIN_ACCOUNT_CREATE,
                )
            ],
        ),
    ],
)

register_ui_module_pages("accounting", UI_PAGES)
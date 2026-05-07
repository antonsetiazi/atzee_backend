# accounting/ui/pages/account_edit.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

from accounting.enum.permissions import AccountingPermission


UI_PAGES = Page(
    key="accounting.accounts.edit",
    entity="accounts",
    domain="accounting",

    title="Edit Account",
    path="/admin/finance/accounts/{id}",

    permissions=[
        AccountingPermission.ADMIN_ACCOUNT_EDIT
    ],

    data_source="/entities/accounting/accounting.accounts.detail/query/",

    blocks=[
        FormBlock(
            title="Edit Account",
            mode="edit",

            submit_to="/entities/accounting/accounting.accounts.update/execute/",
            method="POST",

            redirect_to={"page": "/admin/finance/accounts"},

            refresh_cache=[
                "accounting.accounts.list",
                "accounting.accounts.edit",
            ],

            fields=[
                Field(key="id", label="id", type="hidden"),
                Field(key="code", label="Code", type="text"),
                Field(key="name", label="Name", type="text"),

                Field(
                    key="is_active",
                    label="Active",
                    type="boolean",
                ),
            ],

            actions=[
                Action(type="submit", label="Update", icon="save"),
                Action(type="redirect", label="Batal", to="/admin/finance/accounts"),
            ],
        )
    ],
)

register_ui_module_pages("accounting", UI_PAGES)
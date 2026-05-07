# accounting/ui/pages/account_create.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

from accounting.enum.permissions import AccountingPermission


UI_PAGES = Page(
    key="accounting.accounts.create",
    entity="accounts",
    domain="accounting",

    title="Tambah Account",
    path="/admin/finance/accounts/create",

    permissions=[
        AccountingPermission.ADMIN_ACCOUNT_CREATE
    ],

    blocks=[
        FormBlock(
            title="Form Account",
            mode="create",

            submit_to="/entities/accounting/accounting.accounts.create/execute/",
            method="POST",

            redirect_to={"page": "/admin/finance/accounts"},

            refresh_cache=[
                "accounting.accounts.list",
                "accounting.accounts.edit",
            ],

            fields=[
                Field(key="code", label="Code", type="text", required=True),
                Field(key="name", label="Name", type="text", required=True),

                Field(
                    key="account_type",
                    label="Account Type",
                    type="select",
                    required=True,
                    options=[
                        {"label": "Asset", "value": "asset"},
                        {"label": "Liability", "value": "liability"},
                        {"label": "Equity", "value": "equity"},
                        {"label": "Revenue", "value": "revenue"},
                        {"label": "Expense", "value": "expense"},
                    ],
                ),

                Field(
                    key="normal_balance",
                    label="Normal Balance",
                    type="select",
                    required=True,
                    options=[
                        {"label": "Debit", "value": "debit"},
                        {"label": "Credit", "value": "credit"},
                    ],
                ),

                Field(
                    key="parent_id",
                    label="Parent Account",
                    type="select",
                    data_source="/entities/accounting/accounting.accounts.select.list/query/",
                    required=False,
                ),

                Field(
                    key="is_group",
                    label="Group Account",
                    type="boolean",
                    default=True
                ),
            ],

            actions=[
                Action(type="submit", label="Simpan", icon="save"),
                Action(type="redirect", label="Batal", to="/admin/finance/accounts"),
            ],
        )
    ],
)

register_ui_module_pages("accounting", UI_PAGES)
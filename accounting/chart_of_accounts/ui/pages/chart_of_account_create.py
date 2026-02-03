# accounting/chart_of_accounts/ui/pages/chart_of_account_create.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="chart_of_accounts.create",
    domain="accounting",
    entity="chart_of_accounts",
    title="Chart of Account",
    permissions=["accounting.chart_of_accounts.add"],
    blocks=[
        FormBlock(
            submit_to="/accounting/chart-of-accounts/",
            method="POST",
            title="Add Account",
            description="Buat akun baru untuk struktur pembukuan",
            fields=[
                Field(key="code", label="Account Code", type="text", required=True),
                Field(key="name", label="Account Name", type="text", required=True),
                Field(
                    key="account_type",
                    label="Account Type",
                    type="select",
                    required=True,
                    options=[
                        {"label": "Asset", "value": "asset"},
                        {"label": "Liability", "value": "liability"},
                        {"label": "Equity", "value": "equity"},
                        {"label": "Income", "value": "income"},
                        {"label": "Expense", "value": "expense"},
                    ],
                ),
                Field(
                    key="parent_id",
                    label="Parent Account",
                    type="select",
                    data_source={
                        "type": "entity",
                        "domain": "accounting",
                        "entity": "chart_of_accounts.list",
                        "query": {
                            "filters": {
                                "is_postable": False
                            },
                            "fields": ["id", "code", "name"]
                        },
                        "map": {
                            "value": "id",
                            "label": "{code} - {name}"
                        }
                    },
                    required=False,
                ),
                Field(
                    key="is_active",
                    label="Active",
                    type="boolean",
                    default=True,
                ),
                Field(
                    key="description",
                    label="Description",
                    type="textarea",
                ),
            ],
            actions=[
                Action(type="submit", label="Save"),
                Action(
                    type="redirect",
                    label="Cancel",
                    to="/accounting/chart-of-accounts",
                ),
            ],
        )
    ],
)

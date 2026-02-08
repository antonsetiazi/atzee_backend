# accounting/chart_of_accounts/ui/pages/_base_chart_of_account_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_chart_of_account_form_page(
    *,
    key: str,
    domain: str,
    path: str,
    submit_to: str,
    method: str,
    permissions: list[str],
    title: str,
    redirect_page: str,
    extra_fields: list[Field] | None = None,
):
    fields = [
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
            data_source="/entities/accounting/chart_of_accounts.parent.list/query/",
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
    ]

    if extra_fields:
        # extra_fields boleh:
        # - id (edit)
        # - vertical-specific fields
        fields = fields + extra_fields
    
    return Page(
        key=key,
        entity="chart_of_accounts",
        domain=domain,
        path=path,
        title="Chart of Account",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Lengkapi data chart_of_account dengan benar",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(type="redirect", label="Cancel", to=path.rsplit("/", 2)[0],)
                ],
            )
        ],
    )

# core/master/currencies/ui/pages/_base_currency_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_currency_form_page(
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
        Field(
            key="code",
            label="Currency Code",
            type="text",
            required=True,
        ),
        Field(
            key="name",
            label="Currency Name",
            type="text",
            required=True,
        ),
        Field(
            key="symbol",
            label="Symbol",
            type="text",
            required=False,
            default="",
        ),
        Field(
            key="decimal_places",
            label="Decimal Places",
            type="number",
            required=False,
            default=2,
        ),
        Field(
            key="is_active",
            label="Active",
            type="boolean",
            required=False,
            default=True,
        ),
    ]

    if extra_fields:
        fields = fields + extra_fields

    return Page(
        key=key,
        entity="currencies",
        domain=domain,
        path=path,
        title="Currency",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(
                        type="redirect",
                        label="Cancel",
                        to=redirect_page,
                    ),
                ],
                refresh_cache=["currencies.list"],
            )
        ],
    )

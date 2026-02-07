# accounting/fiscal_period/ui/pages/_base_fiscal_period_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_fiscal_period_form_page(
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
        Field(key="name", label="Fiscal Period Name", type="text", required=True),
        Field(key="start_date", label="Start Date", type="date", required=True),
        Field(key="end_date", label="End Date", type="date", required=True),
    ]

    if extra_fields:
        fields = fields + extra_fields

    return Page(
        key=key,
        entity="fiscal_period",
        domain=domain,
        path=path,
        title="Fiscal Periods",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Lengkapi data fiscal period dengan benar",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(
                        type="redirect",
                        label="Cancel",
                        to=path.rsplit("/", 2)[0],
                    ),
                ],
            )
        ],
    )

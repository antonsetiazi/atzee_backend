# core/geo/regions/ui/pages/_base_region_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_region_form_page(
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
            key="country_id",
            label="Country",
            type="select",
            required=True,
            data_source="/entities/core/countries.select.list/query/",
        ),
        Field(
            key="code",
            label="Region Code",
            type="text",
            required=True,
        ),
        Field(
            key="name",
            label="Region Name",
            type="text",
            required=True,
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
        entity="regions",
        domain=domain,
        path=path,
        title="Region",
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
            )
        ],
    )

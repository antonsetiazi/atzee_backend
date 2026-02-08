# core/master/locations/ui/pages/_base_location_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_location_form_page(
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
            label="Code",
            type="text",
            required=True,
        ),
        Field(
            key="name",
            label="Name",
            type="text",
            required=True,
        ),
        Field(
            key="parent_id",
            label="Parent Location",
            type="select",
            data_source="/entities/core/locations.select.list/query/",
            required=False,
        ),
        Field(
            key="description",
            label="Description",
            type="textarea",
        ),
        Field(
            key="is_active",
            label="Active",
            type="boolean",
            default=True,
        ),
    ]

    if extra_fields:
        fields = fields + extra_fields

    return Page(
        key=key,
        entity="location",
        domain=domain,
        path=path,
        title="Location",
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

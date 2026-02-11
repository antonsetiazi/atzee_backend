# core/classifications/attributes/ui/pages/attributes/_base_attribute_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_attribute_form_page(
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
    extra_blocks: list | None = None,
):
    fields = [
        Field(
            key="scope",
            label="Scope",
            type="text",
            required=True,
        ),
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
            key="type",
            label="Type",
            type="select",
            required=True,
            options=[
                {"value": "text", "label": "Text"},
                {"value": "number", "label": "Number"},
                {"value": "boolean", "label": "Boolean"},
                {"value": "date", "label": "Date"},
                {"value": "select", "label": "Select"},
                {"value": "multi_select", "label": "Multi Select"},
            ],
        ),
    ]

    if extra_fields:
        fields = fields + extra_fields

    blocks = [
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
    ]

    if extra_blocks:
        blocks.extend(extra_blocks)


    return Page(
        key=key,
        entity="attributes",
        domain=domain,
        path=path,
        title="Attribute",
        permissions=permissions,
        blocks=blocks,
    )

# core/classifications/attributes/ui/pages/attribute_options/_base_attribute_option_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_attribute_option_form_page(
    *,
    key: str,
    domain: str,
    path: str,
    submit_to: str,
    method: str,
    permissions: list[str],
    title: str,
    redirect_page: str,
    attribute_id: str,
    extra_fields: list[Field] | None = None,
):
    fields = [
        Field(key="attribute_id", label="Attribute", type="hidden", default=attribute_id),
        Field(key="code", label="Code", type="text", required=True),
        Field(key="name", label="Name", type="text", required=True),
    ]

    if extra_fields:
        fields = fields + extra_fields

    return Page(
        key=key,
        entity="attributes",
        domain=domain,
        path=path,
        title=title,
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
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
                refresh_cache=["attribute.options.list"],
            )
        ],
    )

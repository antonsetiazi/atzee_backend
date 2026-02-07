# core/master/uom/ui/pages/_base_uom_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_uom_form_page(
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
        Field(key="code", label="Code", type="text", required=True),
        Field(key="name", label="Name", type="text", required=True),
        Field(
            key="category_id",
            label="Category",
            type="select",
            data_source={
                "type": "entity",
                "domain": "core",
                "entity": "uom.categories.list",
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
        Field(key="symbol", label="Symbol", type="text"),
        Field(key="precision", label="Precision", type="number"),
        Field(key="is_base", label="Base Unit", type="boolean"),
    ]

    if extra_fields:
        fields = fields + extra_fields

    return Page(
        key=key,
        entity="uom",
        domain=domain,
        path=path,
        title="Unit of Measure",
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

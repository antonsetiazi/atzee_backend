# core/classifications/categories/ui/pages/_base_category_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_category_form_page(
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
            key="parent_id",
            label="Parent Category",
            type="select",
            data_source="/entities/core/categories.select.list/query/",
            required=False,
        ),
    ]

    if extra_fields:
        fields = fields + extra_fields

    return Page(
        key=key,
        entity="categories",
        domain=domain,
        path=path,
        title="Category",
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

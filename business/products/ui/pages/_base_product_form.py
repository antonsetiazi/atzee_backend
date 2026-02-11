# business/products/ui/pages/_base_product_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock, FileBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_product_form_page(
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
    fields=[
        Field(key="code", label="Product Code", type="text"),
        Field(key="name", label="Product Name", type="text", required=True),
        Field(
            key="product_type",
            label="Product Type",
            type="select",
            required=True,
            options=[
                {"label": "Good", "value": "good"},
                {"label": "Service", "value": "service"},
            ],
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
        entity="products",
        domain=domain,
        path=path,
        title="Product",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Lengkapi data product dengan benar",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(type="redirect", label="Cancel", to=path.rsplit("/", 2)[0],)
                ],
            ),

            FileBlock(
                title="Product Files",
                entity_type="products",
                entity_id_from="id",
                multiple=True,
                accept="image/*,.pdf",
                permissions=["business.products.update"],
            ),
        ],
    )

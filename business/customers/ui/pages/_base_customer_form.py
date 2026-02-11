# business/customers/ui/pages/_base_customer_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock, FileBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_customer_form_page(
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
        Field(key="code", label="Customer Code", type="text"),
        Field(key="name", label="Customer Name", type="text", required=True),
        Field(key="email", label="Email", type="email"),
        Field(key="phone", label="Phone", type="text"),
        Field(key="address", label="Address", type="textarea"),
        Field(key="notes", label="Notes", type="textarea"),
    ]

    if extra_fields:
        # extra_fields boleh:
        # - id (edit)
        # - vertical-specific fields
        fields = fields + extra_fields
    
    return Page(
        key=key,
        entity="customers",
        domain=domain,
        path=path,
        title="Customer",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Lengkapi data customer dengan benar",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(type="redirect", label="Cancel", to=path.rsplit("/", 2)[0],)
                ],
            ),

            # 🔽 FILE ATTACHMENTS
            FileBlock(
                title="Customer Files",
                entity_type="customer",
                entity_id_from="id",
                multiple=True,
                accept="image/*,.pdf",
                permissions=["business.customers.update"],
            ),
        ],
    )

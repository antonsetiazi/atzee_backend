# business/partners/ui/pages/_base_partner_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock, FileBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action
from business.enum.permissions import BusinessPermission


def build_partner_form_page(
    *,
    key: str,
    domain: str,
    path: str,
    mode: str = "create",
    submit_to: str,
    method: str,
    permissions: list[str],
    title: str,
    redirect_page: str,
    extra_fields: list[Field] | None = None,
):
    fields = [
        Field(key="code", label="Partner Code", type="text"),
        Field(key="name", label="Partner Name", type="text", required=True),
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
        entity="partners",
        domain=domain,
        path=path,
        title="Partner",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                mode=mode,
                description="Lengkapi data partner dengan benar",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(type="redirect", label="Cancel", to=path.rsplit("/", 2)[0],)
                ],
                refresh_cache=["partners.list"],
            ),

            FileBlock(
                title="Partner Files",
                entity_type="partners",
                entity_id_from="id",
                multiple=True,
                accept="image/*,.pdf",
                permissions=[BusinessPermission.PARTNERS_UPDATE],
            ),
        ],
    )

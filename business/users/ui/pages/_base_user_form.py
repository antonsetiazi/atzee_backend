# business/users/ui/pages/_base_user_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock, FileBlock, MapBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_user_form_page(
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
        Field(key="name", label="Name", type="text", required=True),
        Field(key="email", label="Email", type="email"),
        Field(key="phone", label="Phone", type="text"),
        Field(key="organization_name", label="Organization Name", type="text"),
        Field(key="organization_type", label="Organization Type", type="text"),
        Field(key="address", label="Address", type="textarea"),
        Field(key="notes", label="Notes", type="textarea"),
    ]

    if extra_fields:
        fields = fields + extra_fields

    return Page(
        key=key,
        entity="users",
        domain=domain,
        path=path,
        title="User",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Lengkapi data user dengan benar",
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
                refresh_cache=["users.list"],
            ),

            FileBlock(
                title="User Files",
                entity_type="user",
                entity_id_from="id",
                multiple=True,
                accept="image/*,.pdf",
                permissions=["business.users.update"],
            ),

            MapBlock(
                title="User Location",
                entity_type="users",
                entity_id_from="id",
                mode="select",
                multiple=False,
                permissions=["business.users.update"],
            ),
        ],
    )

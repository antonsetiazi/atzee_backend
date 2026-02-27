# core/account/ui/pages/address/_base_address_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock, MapBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_address_form_page(
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
    fields=[
        Field(key="label", label="Label", type="text", required=True),
        Field(key="recipient_name", label="Recipient Name", type="text", required=True),
        Field(key="phone", label="Phone", type="text"),
        Field(key="address_line", label="Address", type="textarea", required=True),
        Field(key="city", label="City", type="text", required=True),
        Field(key="province", label="Province", type="text"),
        Field(key="postal_code", label="Postal Code", type="text"),
        Field(key="country", label="Country", type="text", required=True),
        Field(key="is_default", label="Set as Default", type="boolean", default=False),
    ]

    if extra_fields:
        # extra_fields boleh:
        # - id (edit)
        # - vertical-specific fields
        fields = fields + extra_fields
    
    return Page(
        key=key,
        entity="account.address",
        domain=domain,
        path=path,
        title="Address",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                mode=mode,
                title=title,
                description="Lengkapi data alamat dengan benar",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(type="redirect", label="Cancel", to=path.rsplit("/", 2)[0],)
                ],
                refresh_cache=["core.account.address"],
            ),

            MapBlock(
                title="Address Location",
                entity_type="account_address",     # 🔥 harus sama dengan related_entity
                entity_id_from="id",
                mode="select",               # bisa pilih lokasi
                multiple=False,              # 1 customer = 1 primary location
                permissions=["core.account.profile.update"],
            ),
        ],
    )

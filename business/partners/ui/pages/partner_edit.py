# business/partners/ui/pages/partner_edit.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="partners.edit",
    entity="partners",
    domain="business",
    title="Partner",
    permissions=["business.partners.update"],
    blocks=[
        FormBlock(
            submit_to="/business/partners/{id}/",  # gunakan placeholder id
            method="PATCH",
            title="Edit Partner",
            description="Lengkapi data partner dengan benar",
            redirect_to={
                "page": "partners.list",
            },
            fields=[
                Field(key="id", label="Partner ID", type="hidden"),
                Field(key="code", label="Partner Code", type="text"),
                Field(key="name", label="Partner Name", type="text", required=True),
                Field(key="email", label="Email", type="email"),
                Field(key="phone", label="Phone", type="text"),
                Field(key="address", label="Address", type="textarea"),
                Field(key="notes", label="Notes", type="textarea"),
            ],
            actions=[
                Action(type="submit", label="Save"),
                Action(type="redirect", label="Cancel", to="/business/partners"),
            ],
        )
    ],
)

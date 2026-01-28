# business/partners/ui/pages/partner_create.py
from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="partners.create",
    entity="partners",
    title="Partner",
    permissions=["business.partners.add"],
    blocks=[
        FormBlock(
            submit_to="/business/partners/",
            method="POST",
            title="Create Partner",
            description="Lengkapi data partner dengan benar",
            fields=[
                Field(key="code", label="Partner Code", type="text"),
                Field(key="name", label="Partner Name", type="text", required=True),
                Field(key="email", label="Email", type="email"),
                Field(key="phone", label="Phone", type="text"),
                Field(key="address", label="Address", type="textarea"),
                Field(key="notes", label="Notes", type="textarea"),
            ],
            actions=[
                Action(type="submit", label="Save"),
                Action(type="redirect", label="Cancel", to="/partners")
            ]
        )
    ],
)

# business/users/ui/pages/user_my_profile.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock, FileBlock, MapBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="users.my_profile",
    entity="users.profile",
    domain="business",
    path="/business/profile",
    title="My Profile",
    permissions=["business.users.self.update"],
    blocks=[
        FormBlock(
            submit_to="/entities/business/users.profile.update/query/",
            method="POST",
            title="My Profile",
            description="Update your personal information",
            redirect_to={"page": "/business/profile"},
            fields=[
                Field(key="name", label="Name", type="text", required=True),
                Field(key="email", label="Email", type="email"),
                Field(key="phone", label="Phone", type="text"),
                Field(key="organization_name", label="Organization Name", type="text"),
                Field(key="organization_type", label="Organization Type", type="text"),
                Field(key="address", label="Address", type="textarea"),
                Field(key="notes", label="Notes", type="textarea"),
            ],
            actions=[
                Action(type="submit", label="Save Changes"),
            ],
        ),

        FileBlock(
            title="My Files",
            entity_type="user",
            entity_id_from="self",  # 🔥 khusus self
            multiple=True,
            accept="image/*,.pdf",
            permissions=["business.users.self.update"],
        ),

        MapBlock(
            title="My Location",
            entity_type="users",
            entity_id_from="self",
            mode="select",
            multiple=False,
            permissions=["business.users.self.update"],
        ),
    ],
)

register_ui_module_pages("business", UI_PAGES)
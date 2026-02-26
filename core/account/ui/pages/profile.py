# core/account/ui/pages/profile.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    FormBlock,
    ActionBlock,
    FileBlock,
)
from core.ui.schema.field import Field
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="core.account.profile",
    entity="account.profile",
    domain="core",
    path="/account/profile",
    title="My Profile",
    description="Manage your personal information and account preferences",
    permissions=["core.account.profile.view"],
    blocks=[
        # 🔹 Profile Form
        ContainerBlock(
            direction="row",
            gap=24,
            blocks=[
                FormBlock(
                    mode="edit",
                    submit_to="/entities/core/account.profile.update/query/",
                    method="POST",
                    title="Basic Information",
                    description="These details will be visible across the platform.",
                    fields=[
                        Field(
                            key="username",
                            label="Username",
                            type="text",
                            disabled=True,  # tidak boleh diubah
                        ),
                        Field(
                            key="email",
                            label="Email",
                            type="email",
                            required=True,
                            disabled=True
                        ),
                        Field(
                            key="full_name",
                            label="Full Name",
                            type="text",
                            required=True,
                        ),
                        Field(
                            key="phone",
                            label="Phone",
                            type="text",
                        ),
                    ],
                    actions=[
                        Action(type="submit", label="Save Changes"),
                    ],
                    affects="session_user"
                ),

                # 🔹 Avatar Upload
                FileBlock(
                    title="Profile Picture",
                    entity_type="user_avatar",
                    entity_id_from="self",
                    multiple=False,
                    accept="image/*",
                    permissions=["core.account.profile.update"],
                    affects="session_user"
                ),
            ],
        ),
        ContainerBlock(
            direction="row",
            justify="start",
            blocks=[
                ActionBlock(
                    title="",
                    actions=[
                        Action(
                            type="navigate",
                            label="Change Password",
                            icon="password",
                            to="/account/password",
                            permission="core.account.password.update",
                        )
                    ],
                    justify="center",
                )
            ],
        ),
    ],
)

register_ui_module_pages("core", UI_PAGES)

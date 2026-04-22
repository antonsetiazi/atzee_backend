# core/account/ui/pages/password.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    FormBlock,
)
from core.ui.schema.field import Field
from core.ui.schema.action import Action

 
UI_PAGES = Page(
    key="core.account.password",
    entity="account.password",
    domain="core",
    path="/account/password",
    title="Change Password",
    description="Update your account password safely",
    permissions=["core.account.password.update"],
    blocks=[
        ContainerBlock(
            direction="column",
            gap=24,
            blocks=[
                FormBlock(
                    mode="create",
                    submit_to="/auth/change-password/",
                    method="POST",
                    title="Change Password",
                    description="Enter your current password and new password to update.",
                    redirect_to={
                        "page": "/"
                    },
                    fields=[
                        Field(
                            key="current_password",
                            label="Current Password",
                            type="password",
                            required=True,
                        ),
                        Field(
                            key="new_password",
                            label="New Password",
                            type="password",
                            required=True,
                        ),
                        Field(
                            key="confirm_password",
                            label="Confirm New Password",
                            type="password",
                            required=True,
                        ),
                    ],
                    actions=[
                        Action(type="submit", label="Update Password"),
                    ],
                ),
            ],
        ),
    ],
)

register_ui_module_pages("core", UI_PAGES)
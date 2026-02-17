# core/account/ui/pages/settings.py

from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    FormBlock,
)
from core.ui.schema.field import Field
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="core.account.settings",
    entity="account.settings",
    domain="core",
    path="/account/settings",
    title="Account Settings",
    description="Manage your application preferences and behavior.",
    permissions=["core.account.settings.view"],
    blocks=[
        ContainerBlock(
            direction="column",
            gap=24,
            blocks=[

                # 🔹 General Preferences
                FormBlock(
                    mode="edit",
                    submit_to="/entities/core/account.settings.update/execute/",
                    method="POST",
                    title="General Settings",
                    description="Personalize your platform experience.",
                    fields=[
                        Field(
                            key="language",
                            label="Language",
                            type="select",
                            options=[
                                {"label": "English", "value": "en"},
                                {"label": "Bahasa Indonesia", "value": "id"},
                            ],
                            required=True,
                        ),
                        Field(
                            key="timezone",
                            label="Timezone",
                            type="select",
                            data_source="/entities/core/timezones.select.list/query/",
                            required=True,
                        ),
                        Field(
                            key="theme",
                            label="Theme",
                            type="select",
                            options=[
                                {"label": "Light", "value": "light"},
                                {"label": "Dark", "value": "dark"},
                                {"label": "System", "value": "system"},
                            ],
                        ),
                        Field(
                            key="email_notifications",
                            label="Enable Email Notifications",
                            type="boolean",
                        ),
                    ],
                    actions=[
                        Action(type="submit", label="Save Settings"),
                    ],
                ),
            ],
        ),
    ],
)

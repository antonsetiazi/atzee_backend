# core/tenants/ui/pages/tenant_branding_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

from core.enum.permissions import CorePermission

UI_PAGES = Page(
    key="tenants.branding.edit",
    entity="tenants",
    domain="core",
    title="Edit Tenant Branding",
    path="/admin/settings/branding",
    permissions=[CorePermission.ADMIN_TENANT_BRANDING_VIEW],
    data_source="/entities/core/tenant.branding/query/",

    blocks=[
        FormBlock(
            title="Brand Identity",
            description="Manage logo, app name and theme branding",
            mode="edit",

            submit_to="/entities/core/tenant.branding.update/execute/",
            method="POST",

            redirect_to={
                "page": "/admin/settings/branding"
            },

            refresh_cache=[
                "tenant.branding.query",
                "tenant.current"
            ],

            fields=[

                Field(
                    key="appName",
                    label="Application Name",
                    type="text",
                    required=True,
                ),

                Field(
                    key="logoUrl",
                    label="Logo URL",
                    type="text",
                ),

                Field(
                    key="faviconUrl",
                    label="Favicon URL",
                    type="text",
                ),

                Field(
                    key="theme.mode",
                    label="Theme Mode",
                    type="select",
                    options=[
                        {"label": "Light", "value": "light"},
                        {"label": "Dark", "value": "dark"},
                    ]
                ),

                Field(
                    key="theme.primary",
                    label="Primary Color",
                    type="color",
                ),

                Field(
                    key="theme.secondary",
                    label="Secondary Color",
                    type="color",
                ),

                Field(
                    key="theme.accent",
                    label="Accent Color",
                    type="color",
                ),

                Field(
                    key="theme.background",
                    label="Background",
                    type="color",
                ),

                Field(
                    key="theme.surface",
                    label="Surface",
                    type="color",
                ),

                Field(
                    key="theme.textPrimary",
                    label="Text Primary",
                    type="color",
                ),

                Field(
                    key="theme.textSecondary",
                    label="Text Secondary",
                    type="color",
                ),

                Field(
                    key="theme.radius",
                    label="Radius",
                    type="text",
                ),

                Field(
                    key="theme.shadow",
                    label="Shadow",
                    type="textarea",
                ),

                Field(
                    key="theme.font.family",
                    label="Font Family",
                    type="text",
                ),

                Field(
                    key="theme.font.size",
                    label="Font Size",
                    type="text",
                ),
            ],

            actions=[
                Action(
                    type="submit",
                    label="Save Branding",
                    icon="save",
                ),
            ],
        )
    ],
)

register_ui_module_pages("core", UI_PAGES)
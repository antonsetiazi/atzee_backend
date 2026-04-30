# core/widgets/ui/pages/banners/banner_create.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

from core.enum.permissions import CorePermission

UI_PAGES = Page(
    key="widgets.banners.create",
    entity="widgets",
    domain="core",
    title="New Banner",
    path="/admin/widgets/banners/create",
    permissions=[CorePermission.ADMIN_WIDGETS_CREATE],
    blocks=[
        FormBlock(
            mode="create",
            submit_to="/entities/core/widgets.create/execute/",
            method="POST",
            redirect_to={
                "page": "/admin/widgets/banners"
            },
            refresh_cache=[
                "widgets.banners.list",
            ],
            fields=[
                Field(key="type", type="hidden", label="Widget Type", required=True, default="banner"),
                Field(
                    key="position",
                    label="Position",
                    type="select",
                    required=True,
                    options=[
                        {"value": "dashboard.main", "label": "Dashboard Main"},
                        {"value": "dashboard.sidebar", "label": "Dashboard Sidebar"},
                        {"value": "app.main", "label": "App Main"},
                        {"value": "app.sidebar", "label": "App Sidebar"},
                    ],
                ),
                Field(
                    key="title",
                    label="Title",
                    type="text",
                    required=False,
                ),
                Field(
                    key="config.image_url",
                    label="Image URL",
                    type="text",
                    required=True,
                ),
                Field(
                    key="config.link_url",
                    label="Link URL",
                    type="text",
                    required=False,
                ),
                Field(
                    key="config.open_in_new_tab",
                    label="Open In New Tab",
                    type="boolean",
                    default=True,
                ),
                Field(
                    key="starts_at",
                    label="Starts At",
                    type="datetime",
                    required=False,
                ),
                Field(
                    key="ends_at",
                    label="Ends At",
                    type="datetime",
                    required=False,
                ),
                Field(
                    key="target_roles",
                    label="Target Roles",
                    type="json",
                    required=False,
                    default=[]
                ),
                Field(
                    key="target_permissions",
                    label="Target Permissions",
                    type="json",
                    required=False,
                    default=[]
                ),
                Field(
                    key="order",
                    label="Order",
                    type="number",
                    required=False,
                    default=50,
                ),
                Field(
                    key="is_active",
                    label="Active",
                    type="boolean",
                    required=False,
                    default=True,
                ),
            ],

            actions=[
                Action(
                    type="submit",
                    label="Simpan",
                    icon="save",
                ),
            ],
        )
    ],
)

register_ui_module_pages("core", UI_PAGES)
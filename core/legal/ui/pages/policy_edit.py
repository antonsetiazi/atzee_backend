# core/legal/ui/pages/policy_edit.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

from core.enum.permissions import CorePermission


UI_PAGES = Page(
    key="core.legal.policies.edit",
    entity="policies",
    domain="core",

    title="Edit Policy",
    path="/admin/legal/policies/{id}",

    permissions=[
        CorePermission.ADMIN_POLICY_EDIT
    ],

    data_source="/entities/core/legal.policies.detail/query/",

    blocks=[
        FormBlock(
            title="Edit Policy",
            mode="edit",

            submit_to="/entities/core/legal.policies.update/execute/",
            method="POST",

            redirect_to={"page": "/admin/legal/policies"},

            refresh_cache=[
                "core.legal.policies.list",
                "core.legal.policies.edit",
            ],

            fields=[
                Field(key="id", label="id", type="hidden"),
                Field(key="code", label="Code", type="text"),
                Field(key="title", label="Title", type="text"),
                Field(
                    key="content",
                    label="Content",
                    type="textarea",
                ),
                Field(
                    key="is_active",
                    label="Active",
                    type="boolean",
                ),
            ],

            actions=[
                Action(type="submit", label="Update", icon="save"),
                Action(type="redirect", label="Batal", to="/admin/legal/policies"),
            ],
        )
    ],
)

register_ui_module_pages("core", UI_PAGES)
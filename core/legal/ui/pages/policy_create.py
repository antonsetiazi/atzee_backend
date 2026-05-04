# core/legal/ui/pages/policy_create.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

from core.enum.permissions import CorePermission


UI_PAGES = Page(
    key="core.legal.policies.create",
    entity="policies",
    domain="core",

    title="Tambah Policy",
    path="/admin/legal/policies/create",

    permissions=[
        CorePermission.ADMIN_POLICY_CREATE
    ],

    blocks=[
        FormBlock(
            title="Form Policy",
            mode="create",

            submit_to="/entities/core/legal.policies.create/execute/",
            method="POST",

            redirect_to={"page": "/admin/legal/policies"},

            refresh_cache=[
                "core.legal.policies.list",
                "core.legal.policies.edit",
            ],

            fields=[
                Field(key="code", label="Code", type="text", required=True),
                Field(key="title", label="Title", type="text", required=True),
                Field(
                    key="policy_type",
                    label="Type",
                    type="select",
                    required=True,
                    options=[
                        {"label": "Terms of Service", "value": "tos"},
                        {"label": "Privacy Policy", "value": "privacy"},
                        {"label": "Terms & Conditions", "value": "terms"},
                    ],
                ),
                Field(
                    key="content",
                    label="Content",
                    type="textarea",
                    required=True,
                ),
            ],

            actions=[
                Action(type="submit", label="Simpan", icon="save"),
                Action(type="redirect", label="Batal", to="/admin/legal/policies"),
            ],
        )
    ],
)

register_ui_module_pages("core", UI_PAGES)
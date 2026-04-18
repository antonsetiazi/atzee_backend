# core/master/banks/ui/pages/bank_edit.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

from core.enum.permissions import CorePermission


UI_PAGES = Page(
    key="core.master.banks.edit",
    entity="banks",
    domain="core",

    title="Edit Bank",
    path="/admin/master/banks/{id}",

    permissions=[
        CorePermission.ADMIN_BANK_EDIT
    ],

    data_source="/entities/core/master.banks.detail/query/",

    blocks=[
        FormBlock(
            title="Edit Bank",
            description="Perbarui data bank",
            mode="edit",

            submit_to="/entities/core/master.banks.update/execute/",
            method="POST",

            redirect_to={
                "page": "/admin/master/banks"
            },

            refresh_cache=[
                "core.master.banks.list",
                "core.master.banks.edit"
            ],

            fields=[
                Field(
                    key="id",
                    label="id",
                    type="hidden",
                ),
                Field(
                    key="code",
                    label="Kode Bank",
                    type="text",
                    required=True,
                ),
                Field(
                    key="name",
                    label="Nama Bank",
                    type="text",
                    required=True,
                ),
                Field(
                    key="short_name",
                    label="Nama Singkat",
                    type="text",
                ),
                Field(
                    key="sort_order",
                    label="Urutan",
                    type="number",
                ),
                Field(
                    key="is_active",
                    label="Aktif",
                    type="boolean",
                ),
            ],

            actions=[
                Action(
                    type="submit",
                    label="Update",
                    icon="save",
                ),
                Action(
                    type="redirect",
                    label="Batal",
                    to="/admin/master/banks",
                ),
            ],
        )
    ],
)

register_ui_module_pages("core", UI_PAGES)
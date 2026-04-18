# core/master/banks/ui/pages/bank_create.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

from core.enum.permissions import CorePermission


UI_PAGES = Page(
    key="core.master.banks.create",
    entity="banks",
    domain="core",

    title="Tambah Bank",
    path="/admin/master/banks/create",

    permissions=[
        CorePermission.ADMIN_BANK_CREATE
    ],

    blocks=[
        FormBlock(
            title="Form Bank",
            description="Tambahkan bank baru ke dalam master data sistem",
            mode="create",

            submit_to="/entities/core/master.banks.create/execute/",
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
            ],

            actions=[
                Action(
                    type="submit",
                    label="Simpan",
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
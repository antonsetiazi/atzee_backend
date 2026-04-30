# core/widgets/ui/pages/banners/banner_list.py

from core.ui.registry import register_ui_module_pages

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn, ActionBlock
from core.ui.schema.action import Action

from core.enum.permissions import CorePermission

UI_PAGES = Page(
    key="widgets.banners.list",
    entity="widgets",
    domain="core",
    path="/admin/widgets/banners",
    title="Banner",
    subtitle="Manage dashboard banners",
    permissions=[CorePermission.ADMIN_WIDGETS_VIEW],
    data_source="/entities/core/widgets.list/query/?type=banner",
    blocks=[
        TableBlock(
            title="Daftar Banner",
            data_key="items",
            search_mode="client",
            columns=[
                TableColumn(key="title", label="Title"),
                TableColumn(key="position", label="Position"),
                TableColumn(key="target_roles", label="Roles"),
                TableColumn(
                    key="order",
                    label="Order",
                    align="center",
                ),
                TableColumn(
                    key="is_active",
                    label="Status",
                    align="center",
                ),
                TableColumn(
                    key="created_at",
                    label="Dibuat",
                    format="datetime",
                ),
            ],

            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    icon="pencil",
                    to="/admin/widgets/banners/{id}",
                    permission=CorePermission.ADMIN_WIDGETS_EDIT,
                )
            ],
        ),

        ActionBlock(
            title="",
            justify="center",
            align="center",

            actions=[
                Action(
                    type="navigate",
                    label="New Banner",
                    icon="plus",
                    to="/admin/widgets/banners/create",
                    permission=CorePermission.ADMIN_WIDGETS_CREATE,
                )
            ],
        ),
    ],
)

register_ui_module_pages("core", UI_PAGES)
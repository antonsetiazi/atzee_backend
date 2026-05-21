# core/widgets/ui/pages/banners/banner_list.py

from core.enum.permissions import CorePermission
from core.ui.registry import register_ui_module_pages
from core.ui.schema.action import Action
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.page import Page

UI_PAGES = Page(
    key="widgets.banners.list",
    entity="widgets",
    domain="core",
    path="/admin/widgets/banners",
    title="Banner",
    subtitle="Manage dashboard banners",
    permissions=[CorePermission.ADMIN_WIDGETS_VIEW],
    data_source="/entities/core/widgets.list/query/?type=banner",
    actions=[
        Action(
            type="navigate",
            label="New Banner",
            icon="plus",
            to="/admin/widgets/banners/create",
            permission=CorePermission.ADMIN_WIDGETS_CREATE,
        )
    ],
    blocks=[
        TableBlock(
            title="Daftar Banner",
            data_key="items",
            on_row_click="/admin/widgets/banners/{id}",
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
                    boolean_style="active_inactive",
                    size="xs",
                    weight="semibold",
                ),
                TableColumn(
                    key="created_at",
                    label="Created At",
                    format="datetime",
                    size="xs",
                    text_style="muted",
                ),
            ],
            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    icon="pencil",
                    to="/admin/widgets/banners/{id}",
                    permission=CorePermission.ADMIN_WIDGETS_EDIT,
                ),
                Action(
                    type="delete",
                    label="Delete",
                    icon="trash",
                    permission=CorePermission.ADMIN_WIDGETS_DELETE,
                    endpoint="/entities/core/widgets.delete/execute/",
                    confirm={
                        "title": "Hapus Banner",
                        "message": "Yakin ingin menghapus banner ini?",
                        "level": "danger",
                    },
                    refresh_cache=["widgets.banners.list"],
                    success_title="Berhasil",
                    success_message="Banner berhasil dihapus",
                ),
            ],
        ),
    ],
)

register_ui_module_pages("core", UI_PAGES)

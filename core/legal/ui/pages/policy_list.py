# core/legal/ui/pages/policy_list.py

from core.enum.permissions import CorePermission
from core.ui.registry import register_ui_module_pages
from core.ui.schema.action import Action
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.page import Page

UI_PAGES = Page(
    key="core.legal.policies.list",
    entity="policies",
    domain="core",
    path="/admin/legal/policies",
    title="Policy Management",
    subtitle="Kelola Terms, Privacy Policy, dan lainnya",
    permissions=[CorePermission.ADMIN_POLICY_VIEW],
    data_source="/entities/core/legal.policies.list/query/",
    actions=[
        Action(
            type="navigate",
            label="Add Policy",
            icon="plus",
            to="/admin/legal/policies/create",
            permission=CorePermission.ADMIN_POLICY_CREATE,
        )
    ],
    blocks=[
        TableBlock(
            title="Daftar Policy",
            data_key="items",
            on_row_click="/admin/legal/policies/{id}",
            search_mode="server",
            columns=[
                TableColumn(key="code", label="Code", weight="semibold"),
                TableColumn(key="title", label="Title"),
                TableColumn(key="policy_type", label="Type"),
                TableColumn(key="version", label="Version", align="center"),
                TableColumn(
                    key="is_active",
                    label="Active",
                    align="center",
                    boolean_style="active_inactive",
                    size="xs",
                    weight="semibold",
                ),
                TableColumn(
                    key="created_at",
                    label="Created",
                    format="datetime",
                    size="xs",
                    text_style="muted",
                ),
            ],
            actions=[
                Action(
                    type="delete",
                    label="Delete",
                    icon="trash",
                    permission=CorePermission.ADMIN_POLICY_DELETE,
                    endpoint="/entities/core/legal.policies.delete/execute/",
                    confirm={
                        "title": "Hapus Policy",
                        "message": "Yakin ingin menghapus policy ini?",
                        "level": "danger",
                    },
                    refresh_cache=["core.legal.policies.list"],
                    success_title="Berhasil",
                    success_message="Policy berhasil dihapus",
                ),
            ],
        ),
    ],
)

register_ui_module_pages("core", UI_PAGES)

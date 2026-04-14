# core/users/ui/pages/user_list.py

from core.ui.registry import register_ui_module_pages
from core.users.ui.pages._base_user_list import build_user_list_page

from core.enum.permissions import CorePermission

UI_PAGES = build_user_list_page(
    key="users.list",
    domain="core",
    title_page="Users",
    subtitle_page="Manage and monitor all platform users",
    path="/admin/users",
    data_source="/entities/core/users.list/query/",
    permissions=[CorePermission.ADMIN_USERS_VIEW],
    detail_path="/admin/users/{id}",
    search_mode="server",
)

register_ui_module_pages("core", UI_PAGES)
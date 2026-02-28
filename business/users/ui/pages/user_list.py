# business/users/ui/pages/user_list.py

from core.ui.registry import register_ui_module_pages
from business.users.ui.pages._base_user_list import (
    build_user_list_page,
)

from business.enum.permissions import BusinessPermission

UI_PAGES = build_user_list_page(
    key="users.list",
    domain="business",
    path="/business/users",
    data_source="/entities/business/users.list/query/",
    permissions=[BusinessPermission.USERS_VIEW],
    create_path="/business/users/create",
    edit_path="/business/users/{id}/edit",
    delete_endpoint="/business/users/{id}/",
    search_mode="client",
)

register_ui_module_pages("business", UI_PAGES)
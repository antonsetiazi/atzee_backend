# business/users/ui/pages/user_create.py

from core.ui.registry import register_ui_module_pages
from business.users.ui.pages._base_user_form import (
    build_user_form_page,
)

UI_PAGES = build_user_form_page(
    key="users.create",
    domain="business",
    path="/business/users/create",
    submit_to="/business/users/",
    method="POST",
    permissions=["business.users.add"],
    title="Create User",
    redirect_page="/business/users",
)

register_ui_module_pages("business", UI_PAGES)
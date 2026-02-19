# business/users/ui/pages/user_edit.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.field import Field
from business.users.ui.pages._base_user_form import (
    build_user_form_page,
)

UI_PAGES = build_user_form_page(
    key="users.edit",
    domain="business",
    path="/business/users/:id/edit",
    submit_to="/business/users/{id}/",
    method="PATCH",
    permissions=["business.users.update"],
    title="Edit User",
    redirect_page="/business/users",
    extra_fields=[
        Field(
            key="id",
            label="User ID",
            type="hidden",
        ),
    ],
)

register_ui_module_pages("business", UI_PAGES)
# core/users/ui/pages/_base_user_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_user_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    title_page: str,
    subtitle_page: str,
    data_source: str,
    permissions: list[str],
    detail_path: str,
    search_mode: str,
):
    columns = [
        # 🔗 identity
        TableColumn(key="id", label="ID"),

        # 👤 basic info
        TableColumn(key="full_name", label="Full Name"),
        TableColumn(key="username", label="Username"),

        # 📞 contact
        TableColumn(key="phone", label="Phone"),
        TableColumn(key="email", label="Email"),

        # ✅ verification
        TableColumn(
            key="is_verified",
            label="Verified",
            align="center",
        ),
        TableColumn(
            key="is_phone_verified",
            label="Phone Verified",
            align="center",
        ),

        # 🔐 status
        TableColumn(
            key="is_active",
            label="Active",
            align="center",
        ),

        # ⏱️ join date
        TableColumn(
            key="date_joined",
            label="Joined",
            format="datetime",
        ),
    ]

    return Page(
        key=key,
        entity="users",
        domain=domain,
        path=path,
        title=title_page,
        subtitle=subtitle_page,
        permissions=permissions,
        data_source=data_source,
        blocks=[
            TableBlock(
                title="User List",
                data_key="items",
                search_mode=search_mode,
                columns=columns,
                detail_as_state=False,
                actions=[
                    Action(
                        type="navigate",
                        label="View",
                        icon="eye",
                        to=detail_path,
                        permission="core.users.view",
                    ),
                ],
                top_actions=[],
            )
        ],
    )
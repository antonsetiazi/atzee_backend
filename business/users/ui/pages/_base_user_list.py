# business/users/ui/pages/_base_user_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_user_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    permissions: list[str],
    create_path: str,
    edit_path: str,
    delete_endpoint: str,
    search_mode: str,
):
    columns = [
        TableColumn(key="name", label="Name", priority=1),
        TableColumn(key="email", label="Email", priority=2),
        TableColumn(key="phone", label="Phone"),
        TableColumn(key="organization_name", label="Organization"),
    ]

    return Page(
        key=key,
        entity="users",
        domain=domain,
        path=path,
        title="Users",
        permissions=permissions,
        data_source=data_source,
        blocks=[
            TableBlock(
                data_key="items",
                search_mode=search_mode,
                columns=columns,
                detail_as_state=False,
                actions=[
                    Action(
                        type="navigate",
                        label="Edit",
                        icon="edit",
                        to=edit_path,
                        permission="business.users.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="business.users.delete",
                        confirm={
                            "title": "Delete User",
                            "message": "Are you sure you want to delete this user?",
                            "level": "danger",
                        },
                        endpoint=delete_endpoint,
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create User",
                        to=create_path,
                        permission="business.users.add",
                    )
                ],
            )
        ],
    )

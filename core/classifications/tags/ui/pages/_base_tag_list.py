# core/classifications/tags/ui/pages/_base_tag_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_tag_list_page(
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
        TableColumn(key="code", label="Code"),
        TableColumn(key="name", label="Name"),
    ]

    return Page(
        key=key,
        entity="tags",
        domain=domain,
        path=path,
        title="Tags",
        permissions=permissions,
        blocks=[
            TableBlock(
                data_source=data_source,
                search_mode=search_mode,
                columns=columns,
                detail_as_state=False,
                actions=[
                    Action(
                        type="navigate",
                        label="Edit",
                        icon="edit",
                        to=edit_path,
                        permission="core.tags.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="core.tags.delete",
                        endpoint=delete_endpoint,
                        confirm={
                            "title": "Delete Tag",
                            "message": "Are you sure you want to delete this tag?",
                            "level": "danger",
                        },
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Tag",
                        to=create_path,
                        permission="core.tags.add",
                    )
                ],
            )
        ],
    )

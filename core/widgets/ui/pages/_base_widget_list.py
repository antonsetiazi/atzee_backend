# core/widgets/ui/pages/_base_widget_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_widget_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    title_page: str,
    data_source: str,
    permissions: list[str],
    create_label: str,
    create_path: str,
    edit_path: str,
    delete_endpoint: str,
    search_mode: str = "client",
    default_query: dict | None = None,
):

    columns = [
        TableColumn(key="type", label="Type"),
        TableColumn(key="position", label="Position"),
        TableColumn(key="title", label="Title"),
        TableColumn(key="order", label="Order"),
        TableColumn(key="is_active", label="Active"),
    ]

    return Page(
        key=key,
        entity="widgets",
        domain=domain,
        path=path,
        title=title_page,
        permissions=permissions,
        blocks=[
            TableBlock(
                data_source=data_source,
                search_mode=search_mode,
                columns=columns,
                detail_as_state=False,
                query=default_query or {},
                actions=[
                    Action(
                        type="navigate",
                        label="Edit",
                        icon="edit",
                        to=edit_path,
                        permission="core.widgets.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="core.widgets.delete",
                        endpoint=delete_endpoint,
                        confirm={
                            "title": "Delete Widget",
                            "message": "Are you sure you want to delete this widget?",
                            "level": "danger",
                        },
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label=create_label,
                        to=create_path,
                        permission="core.widgets.add",
                    )
                ],
            )
        ],
    )

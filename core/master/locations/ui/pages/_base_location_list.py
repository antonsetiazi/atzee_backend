# core/master/locations/ui/pages/_base_location_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_location_list_page(
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
    extra_columns: list[TableColumn] | None = None,
):
    columns = [
        TableColumn(key="code", label="Code"),
        TableColumn(key="name", label="Name"),
        TableColumn(key="parent_name", label="Parent"),
        TableColumn(key="is_active", label="Active"),
    ]

    if extra_columns:
        columns.extend(extra_columns)

    return Page(
        key=key,
        entity="location",
        domain=domain,
        path=path,
        title="Locations",
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
                        permission="core.location.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="core.location.delete",
                        endpoint=delete_endpoint,
                        confirm={
                            "title": "Delete Location",
                            "message": "Are you sure you want to delete this location?",
                            "level": "danger",
                        },
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Location",
                        to=create_path,
                        permission="core.location.add",
                    )
                ],
            )
        ],
    )

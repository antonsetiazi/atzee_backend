# core/org/departments/ui/pages/_base_department_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_department_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    permissions: list[str],
    create_path: str,
    edit_path: str,
    search_mode: str,
    delete_endpoint: str,
    extra_columns: list[TableColumn] | None = None,
):
    columns = [
        TableColumn(key="code", label="Code"),
        TableColumn(key="name", label="Name"),
        TableColumn(key="parent", label="Parent"),
    ]

    if extra_columns:
        columns.extend(extra_columns)

    return Page(
        key=key,
        entity="departments",
        domain=domain,
        path=path,
        title="Departments",
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
                        permission="core.department.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="core.department.delete",
                        endpoint=delete_endpoint,
                        confirm={
                            "title": "Delete Department",
                            "message": "Are you sure you want to delete this department?",
                            "level": "danger",
                        },
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Department",
                        to=create_path,
                        permission="core.department.add",
                    )
                ],
            )
        ],
    )

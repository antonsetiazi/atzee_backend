# core/master/uom/ui/pages/_base_uom_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_uom_list_page(
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
        TableColumn(key="category", label="Category"),
        TableColumn(key="is_base", label="Base"),
        TableColumn(key="precision", label="Precision"),
    ]

    if extra_columns:
        columns.extend(extra_columns)

    return Page(
        key=key,
        entity="uom",
        domain=domain,
        path=path,
        title="Units of Measure",
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
                        permission="core.uom.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="core.uom.delete",
                        endpoint=delete_endpoint,
                        confirm={
                            "title": "Delete UOM",
                            "message": "Are you sure you want to delete this unit?",
                            "level": "danger",
                        },
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create UOM",
                        to=create_path,
                        permission="core.uom.add",
                    )
                ],
            )
        ],
    )

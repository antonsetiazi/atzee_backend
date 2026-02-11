# core/classifications/attributes/ui/pages/attributes/_base_attribute_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_attribute_list_page(
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
        TableColumn(key="scope", label="Scope"),
        TableColumn(key="code", label="Code"),
        TableColumn(key="name", label="Name"),
        TableColumn(key="type", label="Type"),
    ]

    return Page(
        key=key,
        entity="attributes",
        domain=domain,
        path=path,
        title="Attributes",
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
                        permission="core.attributes.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="core.attributes.delete",
                        endpoint=delete_endpoint,
                        confirm={
                            "title": "Delete Attribute",
                            "message": "Are you sure you want to delete this attribute?",
                            "level": "danger",
                        },
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Attribute",
                        to=create_path,
                        permission="core.attributes.add",
                    )
                ],
            )
        ],
    )

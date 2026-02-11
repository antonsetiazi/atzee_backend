# core/classifications/attributes/ui/pages/attribute_options/_base_attribute_option_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_attribute_option_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    permissions: list[str],
    create_path: str,
    edit_path: str,
    delete_endpoint: str,
):
    columns = [
        TableColumn(key="code", label="Code"),
        TableColumn(key="name", label="Name"),
    ]

    return Page(
        key=key,
        entity="attribute.options",
        domain=domain,
        path=path,
        title="Attribute Options",
        permissions=permissions,
        blocks=[
            TableBlock(
                data_source=data_source,
                columns=columns,
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
                            "title": "Delete Option",
                            "message": "Are you sure you want to delete this option?",
                            "level": "danger",
                        },
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Add Option",
                        to=create_path,
                        permission="core.attributes.add",
                    )
                ],
            )
        ],
    )

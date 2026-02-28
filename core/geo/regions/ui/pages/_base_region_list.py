# core/geo/regions/ui/pages/_base_region_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_region_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    permissions: list[str],
    create_path: str,
    edit_path: str,
    delete_endpoint: str,
    search_mode: str = "client",
):
    columns = [
        TableColumn(key="code", label="Code"),
        TableColumn(key="name", label="Region"),
        TableColumn(key="country", label="Country"),
    ]

    return Page(
        key=key,
        entity="regions",
        domain=domain,
        path=path,
        title="Regions",
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
                        permission="core.regions.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="core.regions.delete",
                        endpoint=delete_endpoint,
                        confirm={
                            "title": "Delete Region",
                            "message": "Are you sure you want to delete this region?",
                            "level": "danger",
                        },
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Region",
                        to=create_path,
                        permission="core.regions.add",
                    )
                ],
            )
        ],
    )

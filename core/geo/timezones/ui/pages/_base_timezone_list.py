# core/geo/timezones/ui/pages/_base_timezone_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_timezone_list_page(
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
        TableColumn(key="name", label="Timezone"),
        TableColumn(key="utc_offset", label="UTC Offset"),
    ]

    return Page(
        key=key,
        entity="timezones",
        domain=domain,
        path=path,
        title="Timezones",
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
                        permission="core.timezones.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="core.timezones.delete",
                        endpoint=delete_endpoint,
                        confirm={
                            "title": "Delete Timezone",
                            "message": "Are you sure you want to delete this timezone?",
                            "level": "danger",
                        },
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Timezone",
                        to=create_path,
                        permission="core.timezones.add",
                    )
                ],
            )
        ],
    )

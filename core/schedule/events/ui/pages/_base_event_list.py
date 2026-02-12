# core/schedule/events/ui/pages/_base_event_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_event_list_page(
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
        TableColumn(key="title", label="Title"),
        TableColumn(key="start_datetime", label="Start"),
        TableColumn(key="end_datetime", label="End"),
        TableColumn(key="all_day", label="All Day"),
        TableColumn(key="created_by", label="Created By"),
    ]

    if extra_columns:
        columns.extend(extra_columns)

    return Page(
        key=key,
        entity="events",
        domain=domain,
        path=path,
        title="Events",
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
                        permission=f"{domain}.schedule.events.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission=f"{domain}.schedule.events.delete",
                        confirm={
                            "title": "Delete Event",
                            "message": "Are you sure you want to delete this event?",
                            "level": "danger",
                        },
                        endpoint=delete_endpoint,
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Event",
                        to=create_path,
                        permission=f"{domain}.schedule.events.add",
                    )
                ],
            )
        ],
    )

# core/schedule/reminders/ui/pages/_base_reminder_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_reminder_list_page(
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
        TableColumn(key="event_title", label="Event"),
        TableColumn(key="reminder_time", label="Reminder Time"),
        TableColumn(key="reminder_type", label="Type"),
        TableColumn(key="repeat_interval", label="Repeat Interval"),
    ]

    return Page(
        key=key,
        entity="reminders",
        domain=domain,
        path=path,
        title="Reminders",
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
                        permission=f"{domain}.schedule.reminders.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission=f"{domain}.schedule.reminders.delete",
                        confirm={
                            "title": "Delete Reminder",
                            "message": "Are you sure you want to delete this reminder?",
                            "level": "danger",
                        },
                        endpoint=delete_endpoint,
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Reminder",
                        to=create_path,
                        permission=f"{domain}.schedule.reminders.add",
                    )
                ],
            )
        ],
    )

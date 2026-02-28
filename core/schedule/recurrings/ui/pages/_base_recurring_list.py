# core/schedule/recurrings/ui/pages/_base_recurring_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_recurring_list_page(
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
        TableColumn(key="frequency", label="Frequency"),
        TableColumn(key="interval", label="Interval"),
        TableColumn(key="end_date", label="End Date"),
    ]

    return Page(
        key=key,
        entity="recurrings",
        domain=domain,
        path=path,
        title="Recurrings",
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
                        permission=f"{domain}.schedule.recurrings.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission=f"{domain}.schedule.recurrings.delete",
                        confirm={
                            "title": "Delete Recurring",
                            "message": "Are you sure you want to delete this recurring rule?",
                            "level": "danger",
                        },
                        endpoint=delete_endpoint,
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Recurring",
                        to=create_path,
                        permission=f"{domain}.schedule.recurrings.add",
                    )
                ],
            )
        ],
    )

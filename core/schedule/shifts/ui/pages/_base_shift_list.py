# core/schedule/shifts/ui/pages/_base_shift_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_shift_list_page(
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
        TableColumn(key="name", label="Shift Name"),
        TableColumn(key="start_datetime", label="Start"),
        TableColumn(key="end_datetime", label="End"),
    ]

    return Page(
        key=key,
        entity="shifts",
        domain=domain,
        path=path,
        title="Shifts",
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
                        permission=f"{domain}.schedule.shifts.update",
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission=f"{domain}.schedule.shifts.delete",
                        confirm={
                            "title": "Delete Shift",
                            "message": "Are you sure you want to delete this shift?",
                            "level": "danger",
                        },
                        endpoint=delete_endpoint,
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Shift",
                        to=create_path,
                        permission=f"{domain}.schedule.shifts.add",
                    )
                ],
            )
        ],
    )

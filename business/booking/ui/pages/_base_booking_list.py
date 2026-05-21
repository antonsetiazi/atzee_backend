# business/booking/ui/pages/_base_booking_list.py

from business.enum.permissions import BusinessPermission
from core.ui.schema.action import Action
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.page import Page


def build_booking_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    title_page: str,
    subtitle_page: str,
    data_source: str,
    permissions: list[str],
    detail_path: str,
    search_mode: str,
):
    columns = [
        # 🔗 identity
        TableColumn(key="id", label="Booking ID"),
        # 🔥 resource
        TableColumn(key="resource_type", label="Type"),
        TableColumn(key="resource_id", label="Resource"),
        # ⏱️ time
        TableColumn(
            key="start_time",
            label="Start",
            format="datetime",
        ),
        TableColumn(
            key="end_time",
            label="End",
            format="datetime",
        ),
        # ⏳ duration
        TableColumn(
            key="total_duration",
            label="Duration (min)",
            align="right",
            weight="semibold",
        ),
        # 🔄 status
        TableColumn(
            key="status",
            label="Status",
            align="center",
            size="xs",
            weight="semibold",
        ),
    ]

    return Page(
        key=key,
        entity="bookings",
        domain=domain,
        path=path,
        title=title_page,
        subtitle=subtitle_page,
        permissions=permissions,
        data_source=data_source,
        blocks=[
            TableBlock(
                title="Booking List",
                data_key="items",
                search_mode=search_mode,
                columns=columns,
                detail_as_state=False,
                actions=[
                    Action(
                        type="navigate",
                        label="View",
                        icon="eye",
                        to=detail_path,
                        permission=BusinessPermission.ADMIN_BOOKINGS_VIEW,
                    ),
                ],
                top_actions=[],
            )
        ],
    )

# accounting/fiscal_period/ui/pages/_base_fiscal_period_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_fiscal_period_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    permissions: list[str],
    create_path: str,
    edit_path: str,
    close_endpoint: str,
    search_mode: str = "client",
    extra_columns: list[TableColumn] | None = None,
):
    columns = [
        TableColumn(key="name", label="Name"),
        TableColumn(key="start_date", label="Start Date"),
        TableColumn(key="end_date", label="End Date"),
        TableColumn(key="is_closed", label="Closed"),
        TableColumn(key="closed_at", label="Closed At"),
        TableColumn(key="closed_by", label="Closed By"),
    ]

    if extra_columns:
        columns.extend(extra_columns)

    return Page(
        key=key,
        entity="fiscal_period",
        domain=domain,
        path=path,
        title="Fiscal Periods",
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
                        permission="accounting.fiscal_period.update",
                    ),
                    Action(
                        type="post",
                        label="Close",
                        icon="lock",
                        permission="accounting.fiscal_period.update",
                        confirm={
                            "title": "Close Fiscal Period",
                            "message": "Are you sure you want to close this fiscal period? This action cannot be undone.",
                            "level": "danger",
                        },
                        endpoint=close_endpoint,
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Fiscal Period",
                        to=create_path,
                        permission="accounting.fiscal_period.add",
                    )
                ],
            )
        ],
    )

# accounting/chart_of_accounts/ui/pages/_base_chart_of_account_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_chart_of_account_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    permissions: list[str],
    create_path: str,
    edit_path: str,
    search_mode: str,
    delete_endpoint: str,
    extra_columns: list[TableColumn] | None = None,
):
    columns = [
        TableColumn(key="code", label="Code"),
        TableColumn(key="name", label="Account Name"),
        TableColumn(key="account_type", label="Type"),
        TableColumn(key="parent_name", label="Parent"),
        TableColumn(key="is_active_label", label="Active"),
    ]

    if extra_columns:
        columns.extend(extra_columns)

    return Page(
        key=key,
        entity="chart_of_accounts",
        domain=domain,
        path=path,
        title="Chart of Accounts",
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
                        permission="accounting.chart_of_accounts.update"
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="accounting.chart_of_accounts.delete",
                        confirm={
                            "title": "Delete Account",
                            "message": "Are you sure you want to delete this chart_of_account?",
                            "level": "danger",
                        },
                        endpoint=delete_endpoint
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Account",
                        to=create_path,
                        permission="accounting.chart_of_accounts.add"
                    )
                ],
            )
        ]
    )

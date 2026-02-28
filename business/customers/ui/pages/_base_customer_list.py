# business/customers/ui/pages/_base_customer_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_customer_list_page(
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
        TableColumn(key="name", label="Name", priority=1),
        TableColumn(key="email", label="Email", priority=2),
        TableColumn(key="phone", label="Phone"),
        TableColumn(key="is_active", label="Active"),
    ]

    if extra_columns:
        columns.extend(extra_columns)

    return Page(
        key=key,
        entity="customers",
        domain=domain,
        path=path,
        title="Customers",
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
                        permission="business.customers.update"
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="business.customers.delete",
                        confirm={
                            "title": "Delete Customer",
                            "message": "Are you sure you want to delete this customer?",
                            "level": "danger",
                        },
                        endpoint=delete_endpoint
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Customer",
                        to=create_path,
                        permission="business.customers.add"
                    )
                ],
            )
        ]
    )

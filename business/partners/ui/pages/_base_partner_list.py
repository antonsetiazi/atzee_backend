# business/partners/ui/pages/_base_partner_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_partner_list_page(
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
        TableColumn(key="name", label="Name"),
        TableColumn(key="email", label="Email"),
        TableColumn(key="phone", label="Phone"),
        TableColumn(key="is_active", label="Active"),
    ]

    if extra_columns:
        columns.extend(extra_columns)

    return Page(
        key=key,
        entity="partners",
        domain=domain,
        path=path,
        title="Partners",
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
                        permission="business.partners.update"
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="business.partners.delete",
                        confirm={
                            "title": "Delete Partner",
                            "message": "Are you sure you want to delete this partner?",
                            "level": "danger",
                        },
                        endpoint=delete_endpoint
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Partner",
                        to=create_path,
                        permission="business.partners.add"
                    )
                ],
            )
        ]
    )

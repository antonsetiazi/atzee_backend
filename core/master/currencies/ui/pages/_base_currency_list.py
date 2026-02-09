# core/master/currencies/ui/pages/_base_currency_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_currency_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    permissions: list[str],
    create_path: str,
    edit_path: str,
    search_mode: str,
):
    columns = [
        TableColumn(key="code", label="Code"),
        TableColumn(key="name", label="Name"),
        TableColumn(key="symbol", label="Symbol"),
    ]

    return Page(
        key=key,
        entity="currencies",
        domain=domain,
        path=path,
        title="Currencies",
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
                        permission="core.currencies.update",
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Currency",
                        to=create_path,
                        permission="core.currencies.add",
                    )
                ],
            )
        ],
    )

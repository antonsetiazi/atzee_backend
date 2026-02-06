# business/products/ui/pages/_base_product_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_product_list_page(
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
        TableColumn(key="product_type", label="Type"),
        TableColumn(key="is_active", label="Active"),
    ]

    if extra_columns:
        columns.extend(extra_columns)

    return Page(
        key=key,
        entity="products",
        domain=domain,
        path=path,
        title="Products",
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
                        permission="business.products.update"
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="business.products.delete",
                        confirm={
                            "title": "Delete Product",
                            "message": "Are you sure you want to delete this product?",
                            "level": "danger",
                        },
                        endpoint=delete_endpoint
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Product",
                        to=create_path,
                        permission="business.products.add"
                    )
                ],
            )
        ]
    )

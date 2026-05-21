# business/partners/ui/pages/_base_partner_list.py

from core.ui.schema.action import Action
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.page import Page


def build_partner_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    title_page: str,
    subtitle_page: str,
    data_source: str,
    permissions: list[str],
    create_path: str,
    edit_path: str,
    search_mode: str,
    delete_endpoint: str,
    extra_columns: list[TableColumn] | None = None,
):
    columns = [
        TableColumn(key="code", label="Code", weight="semibold"),
        TableColumn(key="name", label="Name"),
        TableColumn(key="phone", label="Phone"),
        TableColumn(key="email", label="Email"),
        # 🔥 Location (pakai property dari model)
        TableColumn(key="city_name", label="City"),
        # 🔥 Business metrics
        # TableColumn(
        #     key="base_price",
        #     label="Base Price",
        #     format="currency",
        #     align="right",
        # ),
        TableColumn(
            key="rating_avg",
            label="Rating",
            align="center",
        ),
        TableColumn(
            key="rating_count",
            label="Reviews",
            align="right",
        ),
        TableColumn(
            key="is_active",
            label="Status",
            boolean_style="active_inactive",
            size="xs",
        ),
    ]

    if extra_columns:
        columns.extend(extra_columns)

    return Page(
        key=key,
        entity="partners",
        domain=domain,
        path=path,
        title=title_page,
        subtitle=subtitle_page,
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
                        permission="business.partners.update",
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
                        endpoint=delete_endpoint,
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Partner",
                        icon="add",
                        to=create_path,
                        permission="business.partners.add",
                    )
                ],
            )
        ],
    )

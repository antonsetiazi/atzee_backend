# business/reviews/ui/pages/_base_review_list.py

from core.ui.schema.action import Action
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.page import Page


def build_review_list_page(
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
        TableColumn(key="id", label="ID"),
        # 👤 USER
        TableColumn(key="user_name", label="User"),
        TableColumn(key="user_phone", label="Phone"),
        # 🤝 PARTNER
        TableColumn(key="partner_name", label="Partner"),
        # ⭐ rating
        TableColumn(
            key="rating",
            label="Rating",
            align="center",
        ),
        # 💬 comment
        TableColumn(key="comment", label="Comment", size="xs"),
        # ⏱️ created
        TableColumn(
            key="created_at",
            label="Created At",
            format="datetime",
            size="xs",
            text_style="muted",
        ),
    ]

    return Page(
        key=key,
        entity="reviews",
        domain=domain,
        path=path,
        title=title_page,
        subtitle=subtitle_page,
        permissions=permissions,
        data_source=data_source,
        blocks=[
            TableBlock(
                title="Review List",
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
                        permission="business.reviews.view",
                    ),
                ],
                top_actions=[],
            )
        ],
    )
